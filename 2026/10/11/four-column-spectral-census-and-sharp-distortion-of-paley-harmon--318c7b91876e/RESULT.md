# Four-column spectral census and sharp distortion of Paley harmonic frames

## Finding
Let \(p\ge7\) be prime with \(p\equiv3\pmod4\). Denote by \(H\subset\mathbb F_p^\times\) the subgroup of nonzero quadratic residues and \(m=(p-1)/2\). For each \(a\in\mathbb F_p\), form the unit vector
\[
v_a=m^{-1/2}\big(e^{2\pi i ra/p}\big)_{r\in H}\in\mathbb C^m.
\]
For any unordered four-element subset \(I\subset\mathbb F_p\), let \(G_I=(\langle v_a,v_b\rangle)_{a,b\in I}\) be its Gram matrix, with the standard conjugate-linear-first inner product, and put \(E_I=(p-1)(G_I-I_4)\).

The characteristic polynomial \(\det(tI_4-E_I)\) has exactly three possibilities, classified by the induced Paley tournament on \(I\):
\[
\begin{aligned}
P_T(t)&=t^4-6(p+1)t^2+8(p+1)t+p^2-2p-3,\\
P_D(t)&=(3p-t^2-2t+3)(3p-t^2+2t-1),\\
P_S(t)&=t^4-6(p+1)t^2+8(1-p)t+p^2+14p-3.
\end{aligned}
\]
These arise from, respectively, a transitive four-vertex tournament, a four-vertex tournament with a directed triangle and a global source or sink, and the strongly connected four-vertex tournament with scores \((1,1,2,2)\). Source and sink versions share \(P_D\). All four eigenvalues of \(G_I\), with algebraic multiplicity, are exactly \(1+t/(p-1)\) as \(t\) runs through the roots of the corresponding polynomial.

The number of **unordered four-element subsets** of each type is exactly
\[
\begin{aligned}
N_T&=\frac{p(p-1)(p-3)(p-7)}{64},\\
N_D&=\frac{p(p-1)(p-3)(p+1)}{96},\\
N_S&=\frac{p(p-1)(p-3)(p+1)}{64}.
\end{aligned}
\]
For \(p=7\), the first type does not occur. For \(p\ge11\), all three occur.

Define the exact order-four spectral deviation
\[
\delta_4(p)=\max_{|I|=4}\lVert G_I-I_4\rVert_{\mathrm{op}}.
\]
For every \(p\ge11\) in the stated congruence class, if \(\tau_T\) denotes the **least real root** of \(P_T\), then
\[
\boxed{\delta_4(p)=-\frac{\tau_T}{p-1}}
\]
and **precisely** the transitive four-subsets attain this maximum. At \(p=7\), if \(\sigma_S\) denotes the **greatest real root** of \(P_S\), then \(\delta_4(7)=\sigma_S/6\), attained precisely by strongly connected four-subsets. In particular \(\delta_4(7)=1.200559710627718\ldots\) and \(\delta_4(11)=0.902541470021717\ldots\). Along primes in this class,
\[
\delta_4(p)=\frac{1+\sqrt2}{\sqrt p}+O(p^{-1}).
\]

## Assumptions and scope
The theorem concerns only **prime** orders \(p\equiv3\pmod4\), the \(m\)-row harmonic frame with all nonzero square frequencies, and **every** four distinct columns. It does not claim an unrestricted-order or arbitrary-window result. Gram entries use the convention \(\langle v_a,v_b\rangle=\sum_r\overline{(v_a)_r}(v_b)_r\). For \(p=7\), the ambient dimension is three, so four vectors are necessarily dependent; \(\delta_4(7)>1\) is consistent. For \(p\ge11\), all four-column Gram matrices are positive definite.

## Proof
**1. Fourier reduction.** Let \(\chi\) be the quadratic character of \(\mathbb F_p\), with \(\chi(0)=0\). The classical quadratic Gauss sum at \(p\equiv3\pmod4\) gives for \(a\ne b\)
\[
\sum_{r\in H}e^{2\pi ir(b-a)/p}=\frac{-1+i\sqrt p\,\chi(b-a)}2.
\]
Since \(m=(p-1)/2\), the diagonal of \(E_I\) is zero and, for \(a\ne b\),
\[
(E_I)_{ab}=-1+i\sqrt p\,\chi(b-a).
\]
Thus \(E_I=-(J_4-I_4)+i\sqrt p\,A_I\), where \(A_I\) is the real skew-symmetric sign matrix of the induced Paley tournament. This is Hermitian. Every four-vertex tournament is isomorphic to one of the four orientations described above; switching a global source to a global sink leaves the present characteristic polynomial unchanged. Direct expansion of the four canonical symbolic matrices gives the displayed three quartics. The coefficient identities are additionally verified in the standalone symbolic checker. Since the matrices are Hermitian, all their characteristic roots are real, and scaling/translation gives precisely the Gram eigenvalues.

**2. Exact multiplicities.** The Paley tournament is doubly regular: it has \(p\) vertices, every out-neighborhood has size \(m=(p-1)/2\), and every ordered pair of distinct vertices has exactly \((p-3)/4\) common out-neighbors. The last identity follows from \(\sum_x\chi(x)\chi(x-c)=-1\) for nonzero \(c\). Consequently the tournament induced on each vertex's out-neighborhood is regular, with \(m\) vertices of outdegree \((m-1)/2\).

In a regular tournament on odd \(m\) vertices, the number of transitive triples is \(m\binom{(m-1)/2}{2}=m(m-1)(m-3)/8\), because each has a unique source. Subtracting from \(\binom m3\) leaves \(m(m-1)(m+1)/24\) cyclic triples. A transitive four-tournament has a unique global source, so summing transitive triples in each out-neighborhood gives \(N_T=p\,m(m-1)(m-3)/8\). A cyclic triple and a global source are counted \(p\,m(m-1)(m+1)/24\) times; reversing all edges gives the same count for global sinks. These yield \(N_D\). All remaining four-sets are strongly connected and give \(N_S=\binom p4-N_T-N_D\), yielding the stated formulas. These are counts of four-sets, not labeled quadruples.

**3. The sharp maximum.** Write \(R_D=1+\sqrt{3p+4}\), the largest absolute root of \(P_D\), from its explicit quadratic factors. If \(r_T>0\) is the largest positive root of \(P_T\), then \(P_T(-r_T)=-16(p+1)r_T<0\). Because \(P_T(t)\to+\infty\) as \(t\to-\infty\), its least root has absolute value strictly exceeding \(r_T\). If \(r_S>0\) is the greatest positive root of \(P_S\), the identity \(P_S(r)-P_S(-r)=16(1-p)r\) similarly proves that \(r_S\) exceeds the absolute value of every negative root of \(P_S\).

The exact polynomial identities
\[
P_S(t)-P_T(t)=16p(1-t),\qquad P_T(-r_S)=-16(p+r_S)<0,
\]
show that the magnitude of the least root of \(P_T\) strictly exceeds the spectral radius of the \(S\) type. Substituting \(R_D\) yields
\[
P_T(-R_D)=-8p\big(p+\sqrt{3p+4}+2\big)<0,
\]
so the same transitive root exceeds the \(D\)-type radius. Thus, whenever \(N_T>0\), which is exactly \(p\ge11\), transitive four-subsets are the unique maximizers up to membership in that type. For \(p=7\), \(N_T=0\), and the remaining \(D\)-type radius is exactly \(6\), whereas \(P_S(6)=-576<0\), so the largest positive \(S\)-root is greater than \(6\), and the \(S\) type uniquely dominates.

**4. Asymptotics.** Under \(t=\sqrt p\,u\), each quartic divided by \(p^2\) converges coefficientwise to \(u^4-6u^2+1\), whose real roots are \(\pm(1+\sqrt2)\) and \(\pm(\sqrt2-1)\). Its roots are simple, so the extremal root magnitude is \((1+\sqrt2)\sqrt p+O(1)\). Dividing by \(p-1\) proves the asymptotic statement.

## Verification
The included standalone `check_paley4.py` uses SymPy 1.14.0 and NumPy 2.3.5. It computes the characteristic polynomials of four canonical Hermitian tournament matrices symbolically, verifies the key comparison identities symbolically, and independently enumerates every four-subset of four prime-field cases \(p=7,11,19,23\), totaling 13,096 subsets. For each it directly builds the quadratic-residue Fourier frame, computes its four-column Gram matrix, checks polynomial coefficients, and matches the predicted exact type counts. Run `python check_paley4.py`. A successful run prints `VERIFY_OK exact_symbolic_characteristic_polynomials_and_comparison_identites=PASS ... counts=PASS`. Finite numerical enumeration corroborates but does not establish the unbounded prime-range theorem; that range follows from the preceding algebraic and combinatorial proof.

## Relationship to prior work
Renes's equiangular tight-frame construction (arXiv:math/0408287, equations (5)–(6) and section 3) already gives the full quadratic-residue/Paley-tournament Gram input, so the Fourier and tournament representation itself is **not** claimed as new. Satake (arXiv:2011.02907) analyzes restricted isometry of a related augmented Paley matrix and transitive subtournaments, rather than the exact four-column census for the present unaugmented harmonic frame. Magsino–Mixon–Parshall (arXiv:1905.04360) studies random principal subensembles of real Paley ETFs asymptotically, rather than this deterministic complex four-column classification. The contribution assessed here is the full finite-four-subset spectral multiplicity distribution and its exactly attained worst deviation, including the \(p=7\) boundary.

## Limitations
Priority against every historical treatment of four-vertex subtournament spectra, conference frames or small-order restricted isometry is not independently certified; an equivalent formulation may exist. The mathematical claim is specific to the stated complex quadratic-residue Fourier frame and primes. It does not give higher-order restricted-isometry constants, an independent audit, or conclusions for all prime powers. The source Gram formula and general tournament regularity are established prerequisites, not claimed contributions.

## References
1. J. M. Renes, *Equiangular Tight Frames From Paley Tournaments*, arXiv:math/0408287 (initially public 2004-08-20), especially equations (5)–(6), section 3. https://arxiv.org/abs/math/0408287
2. S. Satake, *On the Restricted Isometry Property of the Paley Matrix*, arXiv:2011.02907 (2020). https://arxiv.org/abs/2011.02907
3. M. Magsino, D. G. Mixon and H. Parshall, *Kesten–McKay Law for Random Subensembles of Paley Equiangular Tight Frames*, arXiv:1905.04360 (2019). https://arxiv.org/abs/1905.04360
