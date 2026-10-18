# Equal-spacing minimax law for imperfect absorption on discrete cycles

## Finding
Let \(n\ge3\) and \(1\le r\le n\) be integers with \(r\mid n\), put \(q=n/r\), and fix any killing strength \(\kappa>0\). For a set \(S\) of \(r\) distinct vertices of the unit-edge cycle \(C_n\), let \(L\) be its unnormalized nearest-neighbor Laplacian and
\[
R_S=(L+\kappa\operatorname{diag}(\mathbf1_S))^{-1}.
\]
Then the exact minimax endpoint resolvent norm is
\[
\boxed{\min_{\substack{S\subseteq V(C_n)\\ |S|=r}}
\|R_S\|_{\ell^\infty\to\ell^\infty}
=\min_{\substack{S\subseteq V(C_n)\\ |S|=r}}
\|R_S\|_{\ell^1\to\ell^1}
=\frac{n}{r\kappa}+\frac12\left\lfloor\frac{q^2}{4}\right\rfloor.}
\]
Every equally spaced trap set \(S=\{s,s+q,\ldots,s+(r-1)q\}\) attains the minimum, for every positive \(\kappa\). This is an existence-of-minimizers assertion, not a uniqueness classification. The first term depends on the killing strength, while the geometric excess term does not.

## Assumptions and scope
The vertices are \(\mathbb Z/n\mathbb Z\), with simple-cycle edges joining adjacent residues; the Laplacian is \((Lu)(i)=2u(i)-u(i-1)-u(i+1)\). All edge jump rates are one and exactly \(r\) sites have a common strictly positive killing rate \(\kappa\), with no other killing. We use real or complex sequence spaces with counting measure. At \(r=n\), every vertex is trapped and the formula reduces to \(1/\kappa\). The divisibility hypothesis \(r\mid n\) is essential to the present exact-minimum formula; no exact minimum for other lengths is asserted. The probabilistic interpretation is the largest expected time before killing among all starting sites of the corresponding continuous-time nearest-neighbor walk.

## Proof
**1. Invertibility and endpoint norm.** For every vector \(v\),
\[
\langle v,(L+\kappa\mathbf1_S)v\rangle
=\sum_{\{i,j\}\in E(C_n)}|v_i-v_j|^2+\kappa\sum_{i\in S}|v_i|^2.
\]
The right side is strictly positive unless \(v=0\), so the inverse exists. The discrete maximum principle makes it entrywise nonnegative: a negative minimum of the solution to \((L+\kappa\mathbf1_S)v=f\ge0\) would propagate along edges to a trap and contradict \(\kappa>0\). Write \(u=R_S\mathbf1\). Since \(R_S\) is symmetric and nonnegative entrywise, both its maximum absolute row-sum and column-sum norms equal \(\max_i u_i\). Equivalently, \(u_i\) is the integral of the surviving mass at time \(t\) from starting vertex \(i\), and hence the mean lifetime.

**2. Conservation at the traps.** Enumerate the marked sites cyclically by \(s_1,\ldots,s_r\), with positive integer successive gap lengths \(\ell_1,\ldots,\ell_r\), so \(\sum_{i=1}^r\ell_i=n\). Let \(a_i=u(s_i)\), with cyclic indices. Summing \((L+\kappa\mathbf1_S)u=\mathbf1\) over all vertices and using \(\sum_i(Lu)_i=0\) gives
\[
\kappa\sum_{i=1}^r a_i=n.
\]
The case \(r=1\) uses the single arc from its trap back to itself and is covered by the same calculation.

**3. Exact interpolation on a trap-to-trap arc.** Between \(s_i\) and \(s_{i+1}\), parametrize the \(\ell_i+1\) successive vertices by \(j=0,1,\ldots,\ell_i\). At each unmarked interior vertex the equation is \(2u_j-u_{j-1}-u_{j+1}=1\); the exact solution with endpoints \(a_i,a_{i+1}\) is
\[
u_{i,j}=\Bigl(1-\frac{j}{\ell_i}\Bigr)a_i
+\frac{j}{\ell_i}a_{i+1}
+\frac{j(\ell_i-j)}2.
\]
This identity also holds at both endpoints, including an arc of one edge, where there is no interior equation.

**4. Universal lower bound.** Define \(f(\ell)=\lfloor\ell^2/4\rfloor\). Take \(j_-=\lfloor\ell_i/2\rfloor\) and \(j_+=\lceil\ell_i/2\rceil\). The average of the two actual values at these central positions is exactly
\[
\frac{u_{i,j_-}+u_{i,j_+}}2
=\frac{a_i+a_{i+1}}2+\frac{f(\ell_i)}2.
\]
Each such average is at most \(M=\max_v u(v)\). Averaging over all arcs and applying the trap conservation identity yields
\[
M\ge\frac{n}{r\kappa}+\frac1{2r}\sum_{i=1}^rf(\ell_i).
\]
The integer function \(f\) is discretely convex because
\(f(\ell+1)-f(\ell)=\lceil\ell/2\rceil\) is nondecreasing. Whenever \(\sum_i\ell_i=rq\), smoothing any pair of unequal gap lengths without changing their sum shows
\(\sum_i f(\ell_i)\ge r f(q)\). Hence
\[
M\ge\frac{q}{\kappa}+\frac12\lfloor q^2/4\rfloor
\]
for every admissible trap set.

**5. Equality for equally spaced traps.** If every gap equals \(q\), rotational symmetry and uniqueness of the linear-system solution force all marked-site values to be identical. By trap conservation they equal \(q/\kappa\). Along each arc the interpolation formula becomes
\[
u_{i,j}=\frac{q}{\kappa}+\frac{j(q-j)}2.
\]
Its maximum, over integers \(0\le j\le q\), is \(q/\kappa+\frac12\lfloor q^2/4\rfloor\). This attains the universal lower bound and proves both endpoint identities. No numerical evidence is used to establish the infinite family.

## Verification
The standalone `verify.py` independently constructs the finite cycle Laplacian, solves the killed Poisson system for every trap placement in several sizes with \(r\mid n\), and compares against the proposed closed form. It performs 516 exact-rational finite cases and 17,274 additional floating-point finite cases; equally spaced placements attain equality in every tested case. Run `python3 verify.py` with NumPy installed. These checks are finite consistency tests, not a substitute for the analytic minimax proof.

## Relationship to prior work
Aspelmeier–Magnin–Graupner–Täuber (arXiv:cond-mat/0107434) study imperfect trapping and a one-trap ring approximation to long-time survival in disordered systems, but do not optimize the endpoint resolvent norm over all multiple-trap positions. Robledo–Woodhouse (1978) investigate periodic lattices and give analytic results for single or equally spaced perfect traps. Evans–Nord (1985) develop multiple-trap walk-length formulas for fully absorbing sites; their described objective and models do not state all-positive-strength minimax endpoint norms on cycles. Lin–Julaiti–Zhang (arXiv:1209.6165) analyze mean passage time to a single deep trap, not arbitrary equal-strength imperfect multi-trap positioning with worst starting site. The classical inputs here are the discrete Poisson interpolation identity, the maximum principle, and convexity; the claim is the exact joint optimization over \(S\) and its \(\kappa\)-independent geometric excess.

## Limitations
The theorem concerns one-dimensional cycles, identical site killing strengths, unit unweighted edges, and divisible trap counts. It does not classify every minimizing trap set, treat nondivisible lengths or unequal killing strengths, optimize the spectral decay rate, or determine higher moments of the lifetime. Historical priority is provisional: a plausible 1978 multiple-trapping article could only be assessed from its abstract, not its complete text. Related formulas might occur under Markov-chain lifetime, absorbing potential, or Green-resolvent terminology. 
## References
1. T. Aspelmeier, J. Magnin, W. Graupner and U. C. Täuber, *Random walks with imperfect trapping in the decoupled-ring approximation*, arXiv:cond-mat/0107434, first public v1 2001-07-20.
2. A. Robledo and L. Woodhouse, *Multiple trapping of random walkers on periodic lattices*, J. Stat. Phys. 19 (1978), 129–147, DOI:10.1007/BF01012507.
3. J. W. Evans and R. S. Nord, *Random walks on finite lattices with multiple traps: Application to particle-cluster aggregation*, Phys. Rev. A 32 (1985), 2926–2943, DOI:10.1103/PhysRevA.32.2926.
4. Y. Lin, A. Julaiti and Z. Zhang, *Mean first-passage time for random walks in general graphs with a deep trap*, arXiv:1209.6165, first public v1 2012-09-27.
