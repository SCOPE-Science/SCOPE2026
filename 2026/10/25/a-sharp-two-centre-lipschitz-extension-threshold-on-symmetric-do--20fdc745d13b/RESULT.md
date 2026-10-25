# A sharp two-centre Lipschitz extension threshold on symmetric double stars

## Finding
Let \(m\ge 2\) be an integer and \(t>0\). Form the weighted double-star tree \(T_{m,t}\) with central vertices \(u,v\) joined by a length-\(t\) edge, with \(m\) unit-length leaves incident to each central vertex. Let \(X\) consist of its \(2m\) leaves and \(Y=X\cup\{u,v\}\) carry the tree path metric. The smallest \(L\ge1\) such that **every** \(1\)-Lipschitz map from \(X\) to **every real Banach space** admits an extension to \(Y\) with Lipschitz constant at most \(L\) is also the smallest norm of a real-linear, constant-preserving scalar Lipschitz extension operator. It equals
\[
\Lambda_m(t)=\begin{cases}
\displaystyle\frac{(t+2)(t+4-2/m)}{t^2+(2+2/m)t+4},&m=2\text{ or }0<t\le\frac{2m}{m-2},\\[5pt]
\displaystyle 2-\frac2m,&m>2\text{ and }t\ge\frac{2m}{m-2}.
\end{cases}
\]
The two expressions coincide at the threshold; when \(m=2\), only the first branch applies. The minimum is attained by **positive simultaneous interpolation**. For \(m>2\), its optimal cross-cluster interpolation weight drops to exactly zero at \(t=2m/(m-2)\), after which the sharp constant is independent of \(t\). In contrast, for \(m=2\), the cross-cluster weight remains positive for every finite \(t\) and \(\Lambda_2(t)\to1\) as \(t\to\infty\).

## Assumptions and scope
Each tree edge has its specified positive length and distances are path lengths, so leaves in one cluster are distance \(2\) apart, and leaves in distinct clusters are distance \(t+2\) apart. Write \(A=\{a_1,\dots,a_m\}\), \(B=\{b_1,\dots,b_m\}\), and denote the means by \(\bar f_A=m^{-1}\sum_i f(a_i)\) and \(\bar f_B=m^{-1}\sum_i f(b_i)\). Scalar operators preserve constants and agree with the original values on \(X\). Banach-valued extensions may be nonlinear in the original map and may depend on the target space; the asserted constant is uniform over all such maps and targets. No restriction of positivity is imposed in the minimization.

## Proof
**1. Reduction to a real-linear universal operator.** For a finite metric space \(X\), its real Lipschitz-free space \(\mathcal F(X)\) has canonical isometric map \(x\mapsto\delta_x\) (relative to any basepoint). Every Banach-valued Lipschitz map on \(X\) linearizes to a bounded operator of the same norm on \(\mathcal F(X)\). A simultaneous extension with factor \(L\) of the canonical map \(x\mapsto\delta_x\) yields two vectors \(z_u,z_v\in\mathcal F(X)\). Writing them as affine combinations of the \(\delta_x\) defines a constant-preserving linear extension operator of norm at most \(L\). Conversely, a linear extension with this norm applied to arbitrary Banach-valued data has the same Lipschitz bound. Thus optimization over universal Banach-valued extensions equals optimization over real-linear scalar extension operators. The affine coefficients sum to one because the \(\delta_x\) are represented relative to the chosen basepoint.

**2. Symmetry reduction.** The group of permutations of \(A\), permutations of \(B\), and simultaneous interchange of \((A,u)\) with \((B,v)\) acts isometrically. Averaging any admissible extension operator over this finite group preserves its extension property and cannot increase its operator norm. Hence some optimal operator has one real parameter \(\alpha\), with
\[
Ef(u)=\alpha\bar f_A+(1-\alpha)\bar f_B,\qquad Ef(v)=(1-\alpha)\bar f_A+\alpha\bar f_B.
\]
These identities hold for all scalar-valued functions on \(X\), so \(\alpha\) may initially be any real number.

**3. Exact operator norm.** For any zero-total-mass signed measure \(\mu\) supported on leaves, its Lipschitz-free norm on \(X\) equals its transportation cost in the tree. Removing each pendant edge and the central edge gives the exact identity
\[
\|\mu\|_{\mathcal F(X)}=\sum_{x\in X}|\mu(x)|+t\left|\sum_{x\in A}\mu(x)\right|.
\]
Indeed, an arbitrary leaf-supported mass balance forces the signed flow across every tree edge; the sum of the absolute flows times edge lengths is both a feasible transport cost and a sharp lower bound (equivalently realized by tree Lipschitz potentials). Applying this to the edge differences \(Ef(u)-f(a_i)\), \(Ef(v)-f(b_j)\), and \(Ef(u)-Ef(v)\), divided by their respective edge lengths \(1,1,t\), yields exactly
\[
\|E_\alpha\|=\max\left\{1,F(\alpha),\frac{t+2}{t}|2\alpha-1|\right\},
\quad
F(\alpha)=\left|\frac\alpha m-1\right|+\frac{m-1}{m}|\alpha|+(1+t)|1-\alpha|.
\]
Checking only the tree edges suffices, by summing along shortest paths; the identity on \(X\) already has norm one.

**4. Global minimization including signed coefficients.** The function \(F\) is decreasing for \(\alpha<0\), strictly decreasing on \([0,1]\), and increasing for \(\alpha>1\) (its slopes on \((1,m)\) and \((m,\infty)\) are positive). The second function \(|2\alpha-1|\) is decreasing for \(\alpha<1/2\) and increasing for \(\alpha>1/2\). Consequently no parameter outside \([1/2,1]\) gives a smaller norm than the closer endpoint. On this interval
\[
F(\alpha)=t+2-\left(t+\frac2m\right)\alpha,
\qquad
\frac{t+2}{t}|2\alpha-1|=\frac{t+2}{t}(2\alpha-1).
\]
One function strictly decreases, the other strictly increases. Their intersection occurs at
\[
\alpha_*(m,t)=\frac{(t+1)(t+2)}{t^2+(2+2/m)t+4}.
\]
It belongs to \([1/2,1]\) exactly when \(m=2\) or \(t\le2m/(m-2)\) for \(m>2\); otherwise the minimizer is \(\alpha=1\). Substitution gives the displayed formula for \(\Lambda_m(t)\). In both cases the optimal \(\alpha\in[1/2,1]\), so the interpolation coefficients are nonnegative. At \(t=2m/(m-2)\), both expressions coincide. Since \(\Lambda_m(t)\ge1\), the initially included maximum with one is redundant. This completes the proof for every integer \(m\ge2\) and every real \(t>0\).

## Verification
The accompanying standalone Python checker `verify_bistar.py` tests the exact rational formulas for \(m=2,3,4\), and \(t\in\{1/3,1,3,12\}\); it also independently solves the full unrestricted signed-coefficient linear program on the \(2m\)-point source using all \(2^{2m+1}\) sign representations of the tree transportation norm. All twelve exact-formula/linear-program comparisons passed to numerical optimization tolerance. These finite tests corroborate, but do not replace, the all-parameter proof above. Run `python verify_bistar.py` with Python 3, NumPy and SciPy.

## Relationship to prior work
Albiac, Ansorena, Cúth and Doucha (2020), arXiv:2005.06555, develop complementation and linearized extension frameworks for Lipschitz-free spaces, including general doubling-space results, but do not supply this exact two-center optimal constant or its support threshold. Basso (2017), arXiv:1707.06593, gives general bounds for extending to finitely many points; Basso (2021), arXiv:2104.14238, describes linear-programming and projection-constant equivalences. Neither inspected paper contains the two-cluster tree-specific formula derived here. The classical Blatter–Cheney formula for hyperplanes in \(\ell_1\), as discussed by Foucart, covers one-center weighted stars (codimension one) but does not directly cover simultaneous two-center extension (codimension two). Previously described equilateral two-center extensions likewise use a different source metric; for \(t>0\), this source has intracluster distance \(2\) and intercluster distance \(t+2\), and therefore is not equilateral. Related more general codimension-two results remain a residual bibliographic risk; no claim of exhaustive literature uniqueness is made.

## Limitations
The tree has equal numbers of equally long pendant edges at the two hubs. The theorem does not classify unequal cluster sizes, heterogeneous pendant lengths, more than two internal vertices, or fixed-target extension constants. The result describes a universal Banach-target constant; independent mathematical validation has not been performed.

## References
1. F. Albiac, J. L. Ansorena, M. Cúth, M. Doucha, *Lipschitz free spaces isomorphic to their infinite sums and geometric applications*, arXiv:2005.06555 (first public 2020-05-13).
2. G. Basso, *Lipschitz extensions to finitely many points*, arXiv:1707.06593 (first public 2017-07-20).
3. G. Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238 (first public 2021-04-29).
4. S. Foucart, *Computation of Minimal Projections and Extensions*, preprint, discussion of the 1974 Blatter–Cheney hyperplane formula.
