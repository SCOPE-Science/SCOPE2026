# A quadratic contact threshold for the Löwner ellipsoid of partial permutohedra

## Finding
For integers \(n\ge3\) and \(m\ge n\), let
\[
\mathcal P(m,n)=\operatorname{conv}\{x\in\{0,1,\ldots,n\}^{m}:\text{the nonzero entries of }x\text{ are distinct}\}.
\]
Write \(S=n(n+1)/2\), \(Q=n(n+1)(2n+1)/6\), \(H=\mathbf1\mathbf1^{\mathsf T}/m\), and \(T=n(n+1)-1\). Define
\[
 t=\frac{S}{m+1},\qquad
 a=\frac{m(mQ-S^2)}{(m+1)(m-1)},\qquad
 b=\frac{mS^2}{(m+1)^2},
\]
and the ellipsoid
\[
 E_{m,n}=\left\{x:\frac{\|(I-H)(x-t\mathbf1)\|_2^2}{a}+
 \frac{\|H(x-t\mathbf1)\|_2^2}{b}\le1\right\}.
\]
**Theorem.** The ellipsoid \(E_{m,n}\) is the unique minimum-Euclidean-volume ellipsoid containing \(\mathcal P(m,n)\) **if and only if** \(m\ge T\). In this regime its volume is exactly
\[
\operatorname{vol}_m(E_{m,n})=\kappa_m\sqrt{b\,a^{m-1}},
\qquad \kappa_m=\frac{\pi^{m/2}}{\Gamma(1+m/2)}.
\]
For \(m>T\), its complete polytope-vertex contact set consists of the origin and all coordinate permutations of \((n,n-1,\ldots,1,0,\ldots,0)\). For \(m=T\), the additional contacts are exactly all coordinate permutations of \((n,n-1,\ldots,2,0,\ldots,0)\). Thus there are \(1+m!/(m-n)!\) contacting vertices above the threshold, and exactly \(1+m!/(m-n)!+m!/(m-n+1)!\) at the threshold.

For \(n\le m<T\), the displayed ellipsoid fails to contain every vertex of the orbit with entries \((n,n-1,\ldots,2,0,\ldots,0)\). No formula for the true Löwner ellipsoid in this lower regime is asserted. The transition dimension is quadratic in the maximum permitted entry: \(m=T=n(n+1)-1\).

## Assumptions and scope
The ambient space is ordinary \(\mathbb R^m\) with its standard coordinate Euclidean metric. All indicated parameters are integers, with \(n\ge3\) and \(m\ge n\). The ellipsoid is full dimensional since \(mQ>S^2\) for \(m\ge n\). An enclosing ellipsoid is described by a center \(c\) and a positive-definite shape matrix \(R\), through \((x-c)^{\mathsf T}R^{-1}(x-c)\le1\). The object is a *minimum-volume enclosing* ellipsoid, not a maximum-volume inscribed ellipsoid or a minimum enclosing ball.

## Proof
**1. All vertex orbits.** A linear functional on \(\mathcal P(m,n)\) is maximized by putting the descending positive values \(n,n-1,\ldots,n-k+1\) into the \(k\) positions having the largest positive coefficients, leaving the other coordinates zero. By perturbing the coefficients to be distinct and nonzero, every such vector is exposed. Consequently the vertex set is the disjoint union of orbits \(V_k\), \(0\le k\le n\), where \(V_0=\{0\}\) and \(V_k\) consists of all coordinate permutations of \((n,n-1,\ldots,n-k+1,0,\ldots,0)\). This is also the standard vertex description of the partial permutohedron (Behrend et al., Proposition 2.7 and Corollary 5.8).

**2. Candidate from a contact measure.** Put probability \(1/(m+1)\) at the origin and probability \(m/(m+1)\), uniformly distributed, on \(V_n\). Its mean is \(\mu=t\mathbf1\), and its covariance is \(C=(a(I-H)+bH)/m\). Indeed, the full-orbit vectors have common sum \(S\), squared length \(Q\), uniform mean \((S/m)\mathbf1\), and transverse coordinate covariance scalar \((mQ-S^2)/(m(m-1))\). The two-point mixture of their sum and the zero sum has variance \(S^2/(m+1)^2\) along \(\mathbf1/\sqrt m\). This gives exactly the above \(a\) and \(b\).

**3. Exact gauge deficit at every vertex.** For \(0\le k\le n\), define
\[
 S_k=\frac{k(2n-k+1)}2,\qquad
 Q_k=Q-\frac{(n-k)(n-k+1)(2(n-k)+1)}6.
\]
Every \(v\in V_k\) has the same squared ellipsoidal gauge \(L_k\). Directly decomposing the squared Euclidean norm along \(\mathbf1\) and perpendicular to it gives
\[
 L_k=\frac{Q_k-S_k^2/m}{a}+\frac{(S_k-mt)^2}{mb}.
\]
The endpoints satisfy \(L_0=L_n=1\). For \(1\le k\le n-1\), put \(r=n-k\) and
\[
 A_k=\frac{k n(n+1)r(r+1)(2nr+r+n+1)}{24},\qquad
 B_k=\frac{k n^2(n-1)(n+1)^2r(r+1)(r-1)}{12}.
\]
Substitution of \(S,S_k,Q,Q_k\) and collection of powers of \(m\) yields the exact identity
\[
 1-L_k=\frac{(m+1)\{A_k(m-T)+B_k\}}{S^2m(mQ-S^2)}.
\]
All denominators and \(A_k\) are strictly positive in the stated range; \(B_k\ge0\), and \(B_k=0\) exactly for \(k=n-1\). For \(m\ge T\) all vertices lie in \(E_{m,n}\). At \(m=T\), exactly \(V_{n-1}\) adds to the two endpoint contact orbits, whereas for \(m>T\) all intermediate orbits are strictly inside. For \(n\le m<T\), the \(k=n-1\) deficit is strictly negative, so \(E_{m,n}\) is not enclosing. These implications are exact for all allowed integers, not experimental extrapolations.

**4. Globally minimal volume and uniqueness.** Let \(E(c,R)\) be any enclosing ellipsoid, with \(R\succ0\). Average its containment inequalities against the probability measure from step 2. Since its mean is \(\mu\) and covariance is \(C\),
\[
 \operatorname{tr}(R^{-1}C)+(\mu-c)^{\mathsf T}R^{-1}(\mu-c)\le1.
\]
Thus \(\operatorname{tr}(R^{-1}(mC))\le m\). The arithmetic–geometric mean inequality applied to the positive eigenvalues of \(R^{-1/2}(mC)R^{-1/2}\) gives \(\det R\ge\det(mC)=ba^{m-1}\). Equality holds only if \(c=\mu\) and \(R=mC\). When \(m\ge T\), step 3 proves the candidate encloses the entire polytope, and this determinant bound proves both global optimality and uniqueness. Since the optimum is unique, its contact set is precisely the set described in step 3.

## Verification
The accompanying standalone standard-library script `verify.py` checks exact rational orbit gauges, the explicit factor identity, the sign transition, and the covariance parameters for \(3\le n\le22\) at multiple values of \(m\), including each threshold and its two neighbors. It also reconstructs the Euclidean parallel and transverse squared norms for representative coordinate vertices. Run `python3 verify.py` from the directory holding the file. The script reports `CHECKS_PASSED` and fails on any assertion violation. These finite checks are independent reproducibility aids: the theorem for every integer \(n\ge3\) follows from the algebraic identity and the determinant–trace proof.

## Relationship to prior work
Heuer and Striker (arXiv:2012.09901, first posted 2020-12-17) introduced the partial permutohedra and determined their facets and face structure. Behrend et al. (arXiv:2207.14253, first posted 2022-07-28, primary MSC2020 52B05) developed the vertex descriptions, enumerative invariants, and anti-blocking permutahedron interpretation used here. Their inspected full HTML texts develop combinatorial and Ehrhart properties, not the present two-orbit Euclidean enclosing-ellipsoid threshold. General Löwner-ellipsoid dual certificates are classical; the contribution here is their exact evaluation for this two-parameter family and a sharp support-orbit transition.

## Limitations
The minimum-volume enclosing ellipsoid is determined explicitly only in the specified large-dimension regime \(m\ge n(n+1)-1\), with \(n\ge3\). Below this threshold the proposed formula is provably infeasible, but the actual optimum is not computed. The result is not an independence or machine-certified proof; the provided checks cover finitely many parameter instances. Equivalent prior evaluations may exist under anti-blocking permutahedron or optimal-design terminology.

## References
1. Dylan Heuer and Jessica Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, https://arxiv.org/html/2012.09901v3 (first public preprint 2020-12-17).
2. Roger E. Behrend, Federico Castillo, Anastasia Chavez, Alexander Diaz-Lopez, Laura Escobar, Pamela E. Harris, and Erik Insko, *Partial permutohedra*, arXiv:2207.14253, https://arxiv.org/html/2207.14253v3 (first public preprint 2022-07-28).
3. Nathaniel Bowman and Michael T. Heath, *Computing minimum-volume enclosing ellipsoids*, Mathematical Programming Computation 15 (2023), 621–650, https://doi.org/10.1007/s12532-023-00242-8 (general computational background only).
