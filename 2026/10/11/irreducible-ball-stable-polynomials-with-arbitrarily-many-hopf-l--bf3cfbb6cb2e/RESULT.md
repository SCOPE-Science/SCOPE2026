# Irreducible ball-stable polynomials with arbitrarily many Hopf-linked boundary circles

## Finding

**Theorem.** For every integer \(m\ge 1\) and every real \(0<\varepsilon<1\), set
\[
p_{m,\varepsilon}(z_1,z_2,z_3)=1-(z_1^2+z_2^2)^m-\varepsilon z_3^2.
\]
The polynomial \(p_{m,\varepsilon}\) is irreducible in \(\mathbb C[z_1,z_2,z_3]\), has no zeros in the open unit ball \(\mathbb B_3\subset\mathbb C^3\), and has exactly the following boundary zeros:
\[
Z(p_{m,\varepsilon})\cap S^5=\bigsqcup_{j=0}^{m-1}C_j,
\qquad
C_j=\{(e^{\pi i j/m}\cos t,e^{\pi i j/m}\sin t,0):0\le t<2\pi\}.
\]
Every \(C_j\) is a smooth great circle, complex-tangential in \(S^5\), and Legendrian in the equatorial sphere \(S^3=\{(z_1,z_2,0):|z_1|^2+|z_2|^2=1\}\). The circles form fibers of a single Hopf fibration of this \(S^3\), so
\[
|\operatorname{lk}_{S^3}(C_j,C_k)|=1\qquad(j\ne k).
\]
The analytic hypersurface \(Z(p_{m,\varepsilon})\) is nonsingular at all these boundary points. In particular, the exact component count is \(b_0(Z(p_{m,\varepsilon})\cap S^5)=m\). Thus there is no universal component bound within irreducible ball-stable polynomials in fixed complex dimension three.

## Assumptions and scope

The ball is \(\mathbb B_3=\{z\in\mathbb C^3:\sum_{k=1}^3|z_k|^2<1\}\), and \(S^5=\partial\mathbb B_3\). Stability means absence of zeros in the **open** ball; boundary zeros are allowed. The integers and real parameter range are exactly \(m\in\{1,2,\ldots\}\) and \(0<\varepsilon<1\). The linking number refers to the specified equatorial \(S^3\), not to arbitrary disjoint circles considered only as subsets of \(S^5\). The word Legendrian also refers to this contact \(S^3\); the same one-dimensional curves are merely complex-tangential, not maximal-dimensional Legendrians, in the contact \(S^5\).

## Proof

**Stability and boundary exhaustiveness.** Put \(S=z_1^2+z_2^2\), \(r=|z_3|\). Whenever \(\|z\|\le1\),
\[
|S|\le|z_1|^2+|z_2|^2\le1-r^2,
\qquad
|S^m+\varepsilon z_3^2|\le(1-r^2)^m+\varepsilon r^2\le1-(1-\varepsilon)r^2.
\]
For \(r>0\) the final bound is strictly below \(1\). If \(r=0\) and \(\|z\|<1\), then \(|S|<1\). Hence \(p_{m,\varepsilon}\) does not vanish anywhere in \(\mathbb B_3\). A boundary zero must have \(r=0\), \(|z_1|^2+|z_2|^2=1\), and \(S^m=1\). Writing \(S=e^{2\pi i j/m}\), the equality \(|z_1^2+z_2^2|=|z_1|^2+|z_2|^2=1\) is equality in the triangle inequality. Consequently \((z_1,z_2)=e^{\pi i j/m}(x,y)\) with real \(x,y\) satisfying \(x^2+y^2=1\). Conversely all such points are boundary zeros. The phases \(\pi j/m\) are pairwise distinct modulo \(\pi\) for \(0\le j<m\), so the circles are disjoint and constitute all connected components.

**Irreducibility.** Work in the unique-factorization domain \(R=\mathbb C[z_1,z_2]\). The polynomial \(q=1-z_1^2-z_2^2\) is irreducible: the invertible complex-linear change \(u=z_1+iz_2\), \(v=z_1-iz_2\) changes it to \(1-uv\), which is primitive and linear in \(u\) over \(\mathbb C[v]\). Moreover,
\[
1-S^m=(1-S)(1+S+\cdots+S^{m-1}),
\qquad
(1+S+\cdots+S^{m-1})\bmod q=m\ne0.
\]
Thus the constant coefficient \(1-S^m\) of the polynomial \(p_{m,\varepsilon}\in R[z_3]\) is divisible by the prime \(q\) but not by \(q^2\). The middle \(z_3\)-coefficient is \(0\), and the leading coefficient \(-\varepsilon\) is a unit, in particular not divisible by \(q\). Eisenstein's criterion followed by Gauss's lemma proves irreducibility over \(\mathbb C[z_1,z_2,z_3]\) for every \(\varepsilon\ne0\).

**Smoothness, complex tangency and linking.** Along any displayed boundary circle, \(S^m=1\) and \((z_1,z_2)\ne(0,0)\). Hence
\[
(\partial_{z_1}p_{m,\varepsilon},\partial_{z_2}p_{m,\varepsilon})=-2m S^{m-1}(z_1,z_2)\ne(0,0).
\]
Every boundary zero is a smooth point of the complex hypersurface. The parametrization \(\gamma_j(t)=e^{\pi i j/m}(\cos t,\sin t,0)\) satisfies \(\sum_{k=1}^3\overline{\gamma_{j,k}(t)}\gamma'_{j,k}(t)=0\), proving complex tangency to the standard contact distribution of \(S^5\). Restricting the same contact form to \(S^3\) shows that \(C_j\) is Legendrian there (a one-dimensional maximal integral curve of the contact plane field).

Finally, the real-linear orthogonal complex structure \(J'(z_1,z_2)=(-z_2,z_1)\) on \(\mathbb R^4=\mathbb C^2\) has \((J')^2=-I\). Each real plane \(P_j=e^{\pi i j/m}\mathbb R^2\) is invariant under \(J'\); different indices yield different planes. Therefore \(C_j=P_j\cap S^3\) are distinct fibers of the Hopf fibration associated with \(J'\). Any two distinct Hopf fibers link once in absolute value. This proves the claimed complete pairwise-linking pattern and finishes the theorem.

## Verification

All displayed steps are exact and uniform in \(m\) and \(\varepsilon\). The stability bound is strict on the open ball; the equality case on the boundary gives an exhaustive parameterization, rather than numerical sampling. Eisenstein's proof checks the full polynomial ring and does not rely on irreducibility at sampled degrees. The Hopf-fiber identification proves all pairwise linking numbers, and the gradient identity excludes singular boundary points. Reproduction requires only the displayed formulas and the standard algebraic and topological facts named in the proof; no numerical certificates or software dependencies are required.

## Relationship to prior work

Knese, Pascoe and Sola study ball-stable polynomials, including the basic quadratic circle example and the one-variable lifting construction (arXiv:2602.21051v1, Sections 4.2–4.3), and explicitly observe that such lifts factor when the one-variable polynomial factors. In particular, their method applied to \(1-S^m\) yields all \(m\) circles but **a reducible polynomial** for \(m>1\). The present square-term perturbation preserves the complete boundary zero set while making the defining polynomial irreducible; that conjunction is not a conclusion of the lifting method. Their local examples and construction theorems do not assert this infinite linked family of irreducible global examples. Vavitsas, Wu and Zarvalis establish Nash-stratification and interpolation/peak-set criteria for boundary zeros (arXiv:2607.05974v2, Theorems 3.1, 4.4 and 4.5). Finite stratification of each individual zero set does not yield a uniform bound or imply the present irreducible linked construction. The earlier geometric decomposition of Vavitsas and Zarvalis (2024, Theorem 1) is likewise consistent but not dominating.

## Limitations

The construction concerns dimension three; it does **not** classify or resolve irreducible boundary-zero curves in two complex variables, nor arbitrary link types in dimension three. The lower-dimensional linking statement lives in the equatorial \(S^3\), and the curves are not claimed to be Legendrian submanifolds of the ambient \(S^5\). This is an existence theorem, not an optimal degree-versus-component bound. No independent validation has been performed.

## References

1. Greg Knese, James Eldred Pascoe and Alan Sola, *Stable polynomials and bounded rational functions in the unit ball*, arXiv:2602.21051v1 (first public 24 February 2026), especially Sections 4.2–4.3 and 5.
2. Dimitrios Vavitsas, Jujie Wu and Konstantinos Zarvalis, *Boundary zeros of stable polynomials in the unit ball*, arXiv:2607.05974v1 (first public 7 July 2026); comparison uses the revised arXiv:2607.05974v2 (16 September 2026), Sections 3–6.
3. Dimitrios Vavitsas and Konstantinos Zarvalis, *Non-cyclicity and polynomials in Dirichlet-type spaces of the unit ball*, Bulletin of the London Mathematical Society **56** (2024), 3905–3919, DOI 10.1112/blms.13176, Theorem 1.
