# The Hasse–Weil zeta function of two 58-line quartic K3 surfaces over \(\mathbb F_3\)

## Finding
For \(\lambda=1,2\), consider the characteristic-three quartic
\[
X_\lambda:\quad x_1^3x_2-x_1x_2^3+x_0^3x_3-x_0x_3^3=\lambda x_0^2x_1x_2\subset\mathbb P^3_{\mathbb F_3}.
\]
The two nonzero prime-field fibers are projectively isomorphic: swapping \(x_1\) and \(x_2\) and negating \(x_3\) sends the parameter \(\lambda\) to \(-\lambda\). Both therefore have the same complete zeta function:
\[
\boxed{Z(X_\lambda/\mathbb F_3,t)=\frac1{(1-t)(1-9t)(1-3t)^6(1-3^8t^8)^2}.}
\]
For **every** integer \(n\ge1\), therefore,
\[
\boxed{\#X_\lambda(\mathbb F_{3^n})=1+3^{2n}+3^n\bigl(6+16\mathbf1_{8\mid n}\bigr).}
\]
Their rational geometric Picard representations have Frobenius characteristic polynomial \((T-1)^6(T^8-1)^2\); in particular their geometric Picard ranks are \(22\) and their arithmetic Picard ranks are \(8\). The already-known 58-line geometry and the previously calculated orbit length distribution alone do **not** determine the zeta function: the missing ingredient is the rational rank of the Frobenius-equivariant intersection lattice.

## Assumptions and scope
The ground field is \(\mathbb F_3\), with geometric constructions over its algebraic closure. The parameter is restricted to the two nonzero elements \(\lambda\in\mathbb F_3^\times\). The statement concerns the full second étale cohomology and all point counts, not just lines over bounded extensions. An intersection graph is the graph of **geometric** lines meeting on the smooth surface; its integral Gram matrix has diagonal \(-2\), off-diagonal \(1\) for meeting pairs, and \(0\) for disjoint pairs. Here \(\mathbf1_{8\mid n}\) is the divisibility indicator.

## Proof
**Smoothness and cohomology.** Put the displayed quartic equation on the left as \(F\). In characteristic three, \(\partial F/\partial x_3=x_0^3\). Hence a singular point would have \(x_0=0\). The remaining partial derivatives successively force \(x_2=0\), \(x_1=0\), and \(x_3=0\), a projective contradiction. Thus each \(X_\lambda\) is a smooth quartic K3 surface. Its second \(\ell\)-adic Betti number is \(22\); distinct straight lines are smooth rational curves meeting transversally at at most one projective point, and each has self-intersection \(-2\).

**All geometric lines, by six Grassmann charts.** The following 58 distinct lines are exhibited explicitly in four of the six row-echelon charts. To prove exhaustiveness, invoke Veniani, Example 5.1: for every nonzero finite parameter this smooth family has **exactly** 58 geometric lines. The attached verifier independently checks each listed line lies on the surface by six evaluations (enough to establish the quartic restriction vanishes identically), rather than assuming the count follows from sampled points:

* In pivot chart \((0,1)\): \(27\) lines \(A_{b,t}\), \(b\in\mathbb F_3\), \(t^9+\lambda t^3-t=0\), spanned by
\[
(1,0,t,b),\qquad(0,1,0,t^3+\lambda t).
\]
* In pivot chart \((0,2)\): \(27\) lines \(B_{c,u}\), \(c\in\mathbb F_3\), \(u^9-\lambda u^3-u=0\), spanned by
\[
(1,u,0,c),\qquad(0,0,1,\lambda u-u^3).
\]
* In chart \((1,3)\): the three lines \(C_s\), \(s\in\mathbb F_3\), spanned by \((0,1,s,0)\) and \((0,0,0,1)\).
* In chart \((2,3)\): the single line \(D\), spanned by \((0,0,1,0)\) and \((0,0,0,1)\). The two other pivot charts contain no lines.

Both displayed linearized polynomials are separable of degree nine; each has nine roots, including zero. The explicit two-parameter substitutions into the quartic equation vanish identically, and the displayed echelon forms are pairwise distinct. We therefore have \(27+27+3+1=58\) geometric lines. Veniani's independently established exact total (for these nonzero parameters) rules out unlisted lines; no unsupported finite-field completeness inference is needed. Each line is infinitesimally rigid, since its normal bundle is \(\mathcal O_{\mathbb P^1}(-2)\).

**Frobenius and incidence.** On roots of \(t^9+\lambda t^3-t\), the map \(\varphi(t)=t^3\) satisfies \(\varphi^2+\lambda\varphi-1=0\); on roots of \(u^9-\lambda u^3-u\), it satisfies \(\varphi^2-\lambda\varphi-1=0\). Both quadratics are irreducible over \(\mathbb F_3\) and have roots of multiplicative order eight in \(\mathbb F_9\). Therefore each nonzero eight-element root set is one Frobenius orbit, and the 58 lines split into ten fixed lines and six eight-cycles.

Two different \(A\)-lines meet iff they share \(t\); similarly two different \(B\)-lines meet iff they share \(u\). The mixed line incidence is exactly
\[
A_{b,t}\cap B_{c,u}\ne\varnothing\quad\Longleftrightarrow\quad tu^3+t^3u=c-b.
\]
All four lines \(C_0,C_1,C_2,D\) meet one another. The line \(C_0\) meets every \(A\)-line, \(D\) meets every \(B\)-line, and there are no other incidences involving those four lines. These statements follow by computing the rank of the \(4\times4\) matrix of the two line bases.

For an explicit Galois-marked matrix, work in \(\mathbb F_{3^8}=\mathbb F_3[\theta]/(\theta^8+\theta^2-1)\). Choose \(\gamma\) with \(\gamma^2=-1\); take \((t_0,u_0)=(\theta,\gamma\theta)\) for \(\lambda=1\) and \((t_0,u_0)=(\gamma\theta,\theta)\) for \(\lambda=2\). Put \(t_i=t_0^{3^i}\) and \(u_j=u_0^{3^j}\). The eight mixed pairing values \(t_0u_j^3+t_0^3u_j\), for \(j=0,\ldots,7\), are respectively
\[
(0,1,1,2,0,2,2,1)\quad(\lambda=1),\qquad
(0,1,2,2,0,2,1,1)\quad(\lambda=2).
\]
For general \((i,j)\), use entry \(j-i\pmod8\). These rules describe **every** edge of the 58-vertex intersection graph and are independently reconstructible using the attached verifier. In each case there are \(357\) edges and line degrees \(3\) (two lines), \(12\) (54 lines), and \(30\) (two lines).

**Rank and the full zeta function.** Construct the rational intersection Gram matrix \(G\) from the incidence rules. Exact Gaussian elimination yields \(\operatorname{rank}_{\mathbb Q}(G)=22\). Hence the rational span of the line classes has dimension \(22\) and exhausts \(H^2_\mathrm{et}(X_{\overline{\mathbb F}_3},\mathbb Q_\ell(1))\). The Frobenius-fixed subspace for \(\varphi^d\) is spanned by sums over its line orbits: averaging is exact over characteristic-zero coefficients. Because Frobenius preserves the nondegenerate intersection form, its invariant subspace is also nondegenerate. Consequently the ranks of the Gram matrices of orbit sums equal the invariant dimensions; for \(d=1,2,4,8\), the exact ranks are
\[
8,\quad10,\quad14,\quad22.
\]
Frobenius has order dividing eight on the generated space. The four invariant dimensions force its characteristic polynomial to be \((T-1)^6(T^8-1)^2\). Untwisting by the cyclotomic factor \(3\), the eigenvalues on \(H^2\) are \(3\) times those roots of unity. The Lefschetz trace formula gives the asserted point-count formula for **all** extension degrees, and its exponential generating function gives the displayed zeta function. The order of the pole at \(t=1/3\) is eight, agreeing with the independently computed arithmetic Picard rank.

## Verification
Run the attached self-contained `verify_veniani_zeta.py` with Python 3. It implements field arithmetic in \(\mathbb F_{3^8}\), checks both additive root spaces, verifies the 58 line equations by exact polynomial-identity evaluation and every intersection by an independent Plücker wedge test, evaluates all 58-by-58 line incidences and the 357 edge count, performs exact rational Gaussian elimination on the Gram and orbit-sum matrices, and independently counts surface points over \(\mathbb F_3\) and \(\mathbb F_9\). It reports, for **each** \(\lambda\), ranks \((22;8,10,14,22)\) and point counts \((28,136)\). An additional independently executed finite-field point counter gives \(7048\) points over \(\mathbb F_{81}\) for each parameter, as predicted. Those point counts are corroboration; the cohomological argument proves the claim for all \(n\).

## Relationship to prior work
Veniani originally supplied this 58-line characteristic-three quartic family, while Degtyarev classified possible maximal supersingular line configurations. The geometric 58-line count, the known geometric supersingularity, and the earlier determined Frobenius cycle pattern \(1^{10}8^6\) (equivalently its Fano-line counting polynomial) are **prior** information. The additional conclusion here comes from a Frobenius-marked *intersection* pairing: its rank 22 and fixed subspace ranks permit passage from arithmetic of lines to the **complete** surface cohomology and hence the Hasse–Weil zeta function. The known orbit lengths by themselves do not determine whether the line classes span \(H^2\), nor the exact Frobenius character on it.

## Limitations
The result concerns only \(\lambda\in\mathbb F_3^\times\), not every parameter over arbitrary finite extensions or a universal moduli family. These two prime-field fibers represent only **one** \(\mathbb F_3\)-isomorphism class, by the explicit coordinate exchange described above; two distinct geometric/arithmetic isomorphism classes are **not** claimed. No full Néron–Severi discriminant or integral Galois lattice classification is asserted. A specialized published finite-field table or a reformulation under a different quartic model could contain an equivalent zeta calculation; targeted search and inspection did not locate one.

## References
- D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, original preprint 15 August 2016, arXiv:1608.04209, Example 6.1 (preprint) / Example 5.1 (journal), https://arxiv.org/abs/1608.04209.
- A. Degtyarev, *Lines in supersingular quartics*, original preprint 20 April 2016, arXiv:1604.05836, Theorem 1.2 and discussion of the 58-line configurations, https://arxiv.org/abs/1604.05836.
