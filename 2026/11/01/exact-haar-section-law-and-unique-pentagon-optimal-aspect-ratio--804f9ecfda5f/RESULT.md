# Exact Haar section law and unique pentagon-optimal aspect ratio for regular triangular prisms

## Finding
For every \(h>0\), let \(P_h\subset\mathbb R^3\) be the right regular triangular prism with vertices
\[
 v_{i,\pm}=(\cos(2\pi i/3),\sin(2\pi i/3),\pm h),\qquad i=0,1,2.
\]
Its centroid is the origin. Let \(U\) be uniform on the unit sphere, and let \(N_h\) be the number of sides of the central polygon \(P_h\cap U^\perp\). Almost surely \(N_h\in\{3,4,5\}\). Write
\[
 S_h=\arccos\frac{h^2-1/2}{1+h^2},\quad
 O_h=\arccos\frac{-h^2-1/2}{1+h^2},\quad
 V_h=\arccos\frac{1-h^2}{1+h^2}=2\arctan h.
\]
The complete probability law is
\[
 \begin{aligned}
 \mathbb P(N_h=3)&=\frac{3O_h}{\pi}-2,\\
 \mathbb P(N_h=4)&=9-\frac{6(O_h+S_h)+3V_h}{\pi},\\
 \mathbb P(N_h=5)&=\frac{3(O_h+2S_h+V_h)}{\pi}-6.
 \end{aligned}
\]
The pentagon probability has precisely one global maximum as \(h\) ranges through all positive real numbers. Its maximizing half-height \(h_*\) is the unique positive solution of
\[
 1+\frac{h_*}{\sqrt{4h_*^2+3}}=\frac{2\sqrt3\,h_*}{\sqrt{4h_*^2+1}}.
\]
Numerically \(h_*=0.5314695510636\ldots\) and \(\max_{h>0}\mathbb P(N_h=5)=0.3851558056742\ldots\). The exact expected number of section sides is
\[
 \mathbb E N_h=\frac{6S_h+3V_h}{\pi}.
\]

## Assumptions and scope
The base triangle has circumradius one and side length \(\sqrt3\); the prism's full height is \(2h\). The law uses a **Haar-uniform plane through the centroid**, not a uniformly offset affine plane and not an area-weighted stereological sampling model. Reversing \(U\) leaves the plane unchanged. Planes containing a vertex have probability zero and are excluded from the generic side count. Scale invariance shows that only the half-height-to-base-circumradius ratio matters.

## Proof
**1. Reduction to a signed spherical arrangement.** Number the top vertices \(0,1,2\) and the bottom vertices \(3,4,5\), in matching cyclic order. The prism has exactly the nine edges
\[
 (01),(12),(20),(34),(45),(53),(03),(14),(25).
\]
Away from the six great circles \(\langle U,v_i\rangle=0\), an edge contributes one vertex to the central section exactly when its endpoint signs disagree. Therefore \(N_h\) is the number of disagreements on these nine pairs.

Each vertex normal has squared length \(1+h^2\). There are three distinct angular separations between the vertex normals: \(S_h\) for two vertices in the same horizontal triangle, \(O_h\) for vertices from opposite horizontal triangles at different base corners, and \(V_h\) for the vertically paired vertices. The displayed formulas follow from the base dot products \(1\) and \(-1/2\).

**2. Complete, deformation-independent arrangement census.** The six great circles have no triple intersection for any \(h>0\). Indeed, write the normals as \((x,\sqrt3 y,hz)\), where the six rational triples \((x,y,z)\) are
\[
 (1,0,\pm1),\quad(-1/2,1/2,\pm1),\quad(-1/2,-1/2,\pm1).
\]
Every determinant of three distinct rational triples is nonzero, with absolute value in \(\{1/2,1,3/2\}\). The corresponding Euclidean determinant is that rational number multiplied by \(h\sqrt3\). Thus the signs of all triple determinants and the spherical arrangement's oriented combinatorics are independent of \(h>0\).

For a proposed sign vector \(\sigma\in\{-1,+1\}^6\), each potential spherical chamber corner lies on the intersection of two great circles, hence on a ray \(\epsilon(v_i\times v_j)\) for \(i<j\) and \(\epsilon\in\{-1,+1\}\). This ray belongs to the closure of that chamber precisely when
\[
 \sigma_k\epsilon\det(v_i,v_j,v_k)>0\qquad\text{for every }k\notin\{i,j\}.
\]
There are no other vertices, since triple intersections do not occur. Evaluating these *exact rational determinant signs* for all \(64\) sign vectors yields precisely \(32\) positive-area chambers and the following complete census. In the angle column \(\theta\) abbreviates an interior angle, not a normal separation; \(\pi-S\) means \(\pi-S_h\), etc.

| Section sides | Chambers | Spherical chamber corners | Interior-angle multiset | One chamber area |
|:--:|--:|:--:|---|---|
| 3 | 2 | 6 | \(6\times O_h\) | \(6O_h-4\pi\) |
| 4 | 12 | 3 | \(2\times(\pi-O_h),\ \pi-S_h\) | \(2\pi-2O_h-S_h\) |
| 4 | 6 | 4 | \(2\times(\pi-S_h),\ 2\times(\pi-V_h)\) | \(2\pi-2S_h-2V_h\) |
| 5 | 12 | 4 | \(O_h,\ 2\times S_h,\ V_h\) | \(O_h+2S_h+V_h-2\pi\) |

For completeness, the representative sign patterns for the rows, in top-then-bottom order, are \(---+++\), \(----++\), \(--+--+\), and \(--+-++\), respectively. The 64-case test and these four multiplicities are reproduced by the standalone exact-arithmetic verifier; it uses no floating-point inequality to classify a chamber. The angle formula is elementary: the wedge defined by the inward hemispheres \(\sigma_i\langle U,v_i\rangle\ge0\) and \(\sigma_j\langle U,v_j\rangle\ge0\) has angle \(\pi-\arccos(\sigma_i\sigma_j\langle v_i,v_j\rangle/(1+h^2))\). The spherical polygon's area is its angle sum minus \((k-2)\pi\), where \(k\) is its number of corners. Substituting the exact census gives the table. Its area-weighted total is identically \(4\pi\), since all angular terms cancel.

**3. The probability formulas.** The uniform sphere has area \(4\pi\). Multiplying the four chamber areas by the respective chamber counts and dividing by \(4\pi\) gives the displayed probabilities. The two quadrilateral-chamber rows both correspond to four-sided *sections* (chamber corner count and section side count are distinct concepts). Their contributions are combined in \(\mathbb P(N_h=4)\).

**4. Uniqueness of the pentagon maximum.** Differentiation gives
\[
 \frac{d}{dh}\mathbb P(N_h=5)=\frac6{\pi(1+h^2)}f(h),\qquad
 f(h)=1+\frac{h}{\sqrt{4h^2+3}}-\frac{2\sqrt3\,h}{\sqrt{4h^2+1}}.
\]
Moreover,
\[
 f'(h)=\frac3{(4h^2+3)^{3/2}}-\frac{2\sqrt3}{(4h^2+1)^{3/2}}<0
\]
for every \(h\ge0\), because \(2\sqrt3>3\) and \(4h^2+1<4h^2+3\). Since \(f(0)=1\) and \(\lim_{h\to\infty}f(h)=3/2-\sqrt3<0\), there is exactly one positive root. The sign of the derivative changes from positive to negative there, proving the unique global maximum. The limits of the pentagon probability at both endpoints are zero.

**5. Independent first-moment identity.** For a Haar-uniform normal, the probability that an edge joins opposite signs is the angle between its endpoint position vectors divided by \(\pi\). Six horizontal edges contribute \(6S_h/\pi\) in expectation and three vertical edges contribute \(3V_h/\pi\). Their sum independently matches the expectation computed from the three-point law.

## Verification
The accompanying `verify_prism.py` is a standalone Python 3 script using only the standard library. It exactly evaluates all twenty determinant signs, all sixty-four proposed sign patterns, the complete thirty-two-chamber census, and the cancellation identity giving total area \(4\pi\). It also checks the independent edge-crossing expectation, numerically solves the unique critical equation, and compares the formulas against 400,000 deterministic-seed independent Gaussian-normal samples distributed across five values of \(h\). Its successful run prints `VERIFY_OK`. Numerical samples are corroboration only: the all-parameter statement follows from the exact determinant census and the analytic angle/derivative arguments.

## Relationship to prior work
Birkemeyer, Brose, Brandenburg, and Prün (first posted 2026-09-14) prove a general combinatorial relationship between prism slices and slabs of the base polytope; they do not evaluate Haar measures of the normal-direction chambers or optimize those measures over the prism aspect ratio. The 1995 stereology study of regular-prism populations by the authors of *Stereology for some classes of polyhedrons* addresses simulation-derived inversion kernels for random spatial ensembles, a different selection model. Konstantinova and Shchur (2023 preprint, 2024 journal publication) numerically estimate angle densities for random sections, including a regular triangular prism. Their accessible abstracts do not state this exact central-plane three-point law, and their full paper was unavailable for a definitive whole-document comparison. The distinction between unconditional random affine sections and Haar-uniform planes constrained to pass through the centroid is essential.

## Limitations
No claim is made for uniformly offset affine planes, non-equilateral bases, oblique prisms, or section areas and angles. The historical-priority comparison is limited by inaccessible full texts of two stereological studies; an equivalent previously published exact central-section law cannot be categorically excluded. The normal-direction measure is precisely specified, and the theorem does not imply a corresponding distribution under other notions of a random plane. Independent mathematical validation has not been performed.

## References
1. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg, N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195 (initial public posting September 14, 2026), especially Proposition 3.6 and Section 3, https://arxiv.org/abs/2609.16195.
2. E. P. Konstantinova and L. N. Shchur, *Algorithm for density of angle distribution in random sections of polyhedron*, Expert Systems with Applications 235 (2024), 121195; DOI:10.1016/j.eswa.2023.121195; preprint SSRN:4485810 (June 20, 2023).
3. *Stereology for some classes of polyhedrons*, Advances in Applied Probability 27 (1995), 384–396; DOI:10.2307/1427832.
