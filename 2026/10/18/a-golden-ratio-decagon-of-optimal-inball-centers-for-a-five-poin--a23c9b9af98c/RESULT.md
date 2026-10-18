# A golden-ratio decagon of optimal inball centers for a five-point transportation norm

## Finding

Let \(X=\mathbb Z/5\mathbb Z\). For \(1\le t\le2\), define a metric \(d_t\) with \(d_t(i,j)=1\) for cyclic neighbors and \(d_t(i,j)=t\) for cyclic diagonals. Let \(H=\{z\in\mathbb R^5:\sum_i z_i=0\}\) carry its ordinary Euclidean inner product and set
\[
K_t=\operatorname{conv}\left\{\frac{e_i-e_j}{d_t(i,j)}:i\ne j\right\}\subset H.
\]
Write \(r_t\) for the radius of a largest Euclidean ball contained in \(K_t\), and \(\mathcal C_t\) for the set of its centers. Set \(\varphi=(1+\sqrt5)/2\).

**Theorem.** For every \(1<t<2\),
\[
r_t=\sqrt{\frac{5}{2(2t^2-2t+3)}}.
\]
If \(t\ne\varphi\), then \(\mathcal C_t=\{0\}\). If \(t=\varphi\), then \(r_t=1/\sqrt2\) and \(\mathcal C_t\) is an exact two-dimensional **regular decagon** centered at zero, lying in the cyclic Fourier-frequency-two plane \(W\subset H\). Its inradius within \(W\) is
\[
h=\frac{1-\sqrt{(7-\sqrt5)/5}}{\sqrt{(7-3\sqrt5)/5}},
\]
and its circumradius is \(h/\cos(\pi/10)\). Its ten supporting lines come from precisely ten distinct projections of a twenty-facet symmetry family. Both boundary metrics have unique maximal-ball center \(0\); at \(t=1\) the maximal radius is \(\sqrt{5/6}\), and at \(t=2\) it is \(\sqrt{5/14}\).

For every \(1<t<2\), exactly ten facets touch the ball centered at zero. The dual Lipschitz polytope has seventy vertices forming five orbits of sizes \(10,10,10,20,20\) under cyclic rotations, reflections and negation. The seventy-vertex aggregate count is **not** claimed as new: it agrees with the previously known generic five-point Lipschitz-polytope count.

## Assumptions and scope

All spaces and norms are real. The metric is the specified **two-distance five-cycle** metric, not the ordinary Euclidean pentagon chord metric. All inball centers and radii are Euclidean relative to the canonical zero-sum coordinate realization \(H\); the same formulas need not hold under arbitrary changes of Euclidean structure. A center \(z\) is admissible exactly when \(z+r_t B_H\subseteq K_t\), with \(B_H\) the Euclidean unit ball in \(H\). The largest ball is defined by maximizing radius jointly over centers.

For a potential \(f=(f_0,\dots,f_4)\) write \(\bar f=f-(\sum_i f_i/5)\mathbf1\). The polar dual \(K_t^\circ\), identified with \(H\), consists precisely of \(\bar f\) with \(|f_i-f_j|\le d_t(i,j)\). Each polar vertex gives a facet inequality \(\langle\bar f,z\rangle\le1\). We may normalize \(f_0=0\) when classifying these vertices.

## Proof

**1. Exhaustive affine-potential classification.** At a polar vertex, the active difference constraints have incidence rank four. Thus their edges contain a spanning tree. Conversely, four saturated constraints along a spanning tree determine a unique normalized potential, and if it satisfies all ten pair inequalities it is a polar vertex. Every spanning tree of the complete graph on five labeled sites appears uniquely among the \(5^3=125\) Prüfer words; each tree has \(2^4=16\) choices of active-edge signs. The resulting 2,000 candidates have affine coordinates \(a_i+b_i t\) with integral \(a_i,b_i\).

The accompanying standalone exact checker loops over all 2,000 candidates and solves every remaining inequality as a rational interval inside \([1,2]\), with no grid discretization. It finds 310 distinct affine assignments: 180 feasible only at \(t=1\), 70 feasible throughout \([1,2]\), and 60 feasible only at \(t=2\). It also checks that no two of the 70 interior assignments coincide at a parameter strictly between 1 and 2. The 70 interior polar vertices are partitioned by rotations, reflections and global sign into the following five orbits, represented by normalized potential rows:

| Family | Potential \((f_0,f_1,f_2,f_3,f_4)\) | Orbit size | \(\|\bar f\|_2^2\) |
| --- | --- | ---: | --- |
| A | \((0,-1,-t,-t,-1)\) | 10 | \(2(3t^2-4t+3)/5\) |
| B | \((0,-1,-t,-1,0)\) | 10 | \(2(2t^2-2t+3)/5\) |
| C | \((0,-1,-1,0,-1)\) | 10 | \(6/5\) |
| D | \((0,-1,-t,-t,1-t)\) | 20 | \(2(3t^2-5t+5)/5\) |
| E | \((0,-1,-t,1-t,-1)\) | 20 | \(2(3t^2-7t+7)/5\) |

The family assignment and all five squared norms are exact, with programmatically checked rational polynomial identities. In particular, if \(q_J\) denotes family \(J\)'s displayed squared norm, then
\[
q_B-q_A=\frac{2t(2-t)}5,\quad
q_B-q_C=\frac{4t(t-1)}5,\quad
q_B-q_D=\frac{2(t-1)(2-t)}5,\quad
q_B-q_E=\frac{2(t-1)(4-t)}5.
\]
These quantities are all strictly positive when \(1<t<2\). Consequently, the ten \(B\)-orbit facets are the only origin-contacting facets, and the centered candidate inradius is \(1/\sqrt{q_B}\). To see that this is the **global** inradius, average the center of an arbitrary feasible ball over the rotation group and central inversion: because \(K_t\) is invariant under these orthogonal symmetries and the feasibility set at a fixed radius is convex, the averaged center is feasible with the same radius, but is zero. This proves the asserted formula for \(r_t\).

**2. Generic uniqueness and the exceptional parameter.** The inequality for a facet with centered normal \(v\) to contain a Euclidean ball of radius \(r_t\) about \(z\) is exactly \(\langle v,z\rangle+r_t\|v\|\le1\). For the ten \(B\)-family normals we have equality in the second term. Since that family is closed under negation, every optimal center is orthogonal to the span of these normals. Form the four-by-four matrix whose rows are the first four cyclic shifts of the \(B\) potential, each normalized to zero at site zero and restricted to the other four sites. The determinant is
\[
(t^2-t-1)^2.
\]
Therefore the \(B\)-normals span all of \(H\), except at \(t=\varphi\). At the exceptional parameter their span has dimension exactly two: all \(B\)-normals have vanishing frequency-two projection (verified below), and the first two cyclic shifts have a nonzero two-by-two minor equal to \(-1\). The orthogonal complement is the two-dimensional plane \(W\).

**3. The regular decagon of centers.** The orthogonal projection \(P:H\to W\), extended to \(\mathbb R^5\), has entries
\[
P_{ij}=\begin{cases}
2/5&i=j,\\
-\varphi/5&i,j\text{ cyclic neighbors},\\
(\varphi-1)/5&i,j\text{ cyclic diagonals}.
\end{cases}
\]
The exact checker proves \(P^2=P\), \(P\mathbf1=0\), and \(P\bar f=0\) for the \(B\)-family at \(t=\varphi\). For each family the values of \(V=\|\bar f\|^2\) and \(Q=\|P\bar f\|^2\) become
\[
\begin{array}{c|cc}
J&V&Q\\\hline
A&(11-\sqrt5)/5&(3-\sqrt5)/5\\
B&2&0\\
C&6/5&(3+\sqrt5)/5\\
D&(14-2\sqrt5)/5&(7-3\sqrt5)/5\\
E&(16-4\sqrt5)/5&(8-2\sqrt5)/5
\end{array}.
\]
On \(W\), the corresponding inequalities are \(\langle P\bar f,z\rangle\le \delta_J\), where \(\delta_J=1-\sqrt{V_J/2}\). All non-\(B\) offsets are strictly positive. The 20 inequalities belonging to family \(D\) project onto exactly ten *different*, equally long, regularly spaced normal directions, the signed dihedral orbit of one projected normal. All ten offsets equal \(\delta_D\); these inequalities therefore define a regular decagon in \(W\) with inradius
\[
\delta_D/\sqrt{Q_D}=
\frac{1-\sqrt{(7-\sqrt5)/5}}{\sqrt{(7-3\sqrt5)/5}}=h.
\]
Since consecutive outward normals are separated by \(\pi/5\), the circumradius is \(R=h/\cos(\pi/10)\).

It remains to show that the other facet families do not cut this decagon. The following strict rational bounds, proved by exact comparisons in \(\mathbb Q(\sqrt5)\) and rational squaring, are sufficient:
\[
R<0.106;\quad \delta_A>0.06,\ \sqrt{Q_A}<0.391;\quad
\delta_C>0.22,\ \sqrt{Q_C}<1.024;\quad
\delta_E>0.159,\ \sqrt{Q_E}<0.841.
\]
Indeed \(0.106\cdot0.391<0.06\), \(0.106\cdot1.024<0.22\), and \(0.106\cdot0.841<0.159\). Every point in the family-\(D\) decagon has norm at most \(R\), so Cauchy–Schwarz gives strict satisfaction of all \(A,C,E\) inequalities; the \(B\) inequalities hold as equalities. This proves that \(\mathcal C_\varphi\) is **exactly** the stated regular decagon, not merely a region containing such a decagon.

**4. Endpoint metrics.** The same complete tree enumeration gives exactly thirty distinct polar vertices for each of \(t=1\) and \(t=2\). At \(t=1\), twenty balanced two-level potentials have squared Euclidean length \(6/5\); they span \(H\), and no vertex has larger length. At \(t=2\), twenty polar vertices have squared norm \(14/5\), again spanning \(H\), while the others are shorter. Averaging proves optimality of the centered ball, and the spanning property forces uniqueness of its center. The radii are the reciprocals of the respective maximal normal lengths.

## Verification

Run \(`python3 pentagon_verify.py`\) from a directory containing the bundled standalone Python file. It uses only the Python standard library: `fractions.Fraction`, `itertools`, `collections`, and `dataclasses`. It enumerates every Prüfer tree, every tree sign pattern and all parameter-feasible affine potentials; verifies all orbit decompositions and polynomial norms; computes the exact determinant and Fourier projections; and certifies the quantitative strict inequalities excluding the noncontact facet families at the exceptional parameter. The expected final line is `ALL EXACT CHECKS PASSED`. This finite computation is exhaustive because every vertex has a spanning tree of active constraints, as proved above; isolated numeric samples are not used as an infinite-parameter argument.

## Relationship to prior work

Gordon and Petrov (2016 preprint, 2017 journal) proved a generic \((n+1)\)-site Lipschitz polytope has \(\binom{2n}{n}\) vertices. Their generic five-site total is therefore 70; the count alone is covered, and the present classification is used as a tool toward the different Euclidean-inball problem. D’Alì, Delucchi and Michałek (2019) examine symmetric edge polytopes and their connections to Lipschitz and Kantorovich–Rubinstein duality. Aliaga (2021) studies extreme points of Lipschitz-free balls over compact metric spaces. The specific exceptional parameter, complete locus of optimal Euclidean centers and its regular-decagon structure are not consequences of the cited general counting and extremality statements, and were not identified in the inspected relevant passages. The absence of a detected prior classification does not prove global bibliographic uniqueness.

## Limitations

The conclusion is specific to the canonical zero-sum Euclidean realization of the real transportation norm of this five-point two-distance metric. The result does not classify Euclidean inballs for arbitrary pentagons, arbitrary five-point metrics, or complex scalars. The proof of the finite potential classification is a self-contained exhaustive certificate requiring replay of the included program. Equivalent unindexed work may exist. No independent scientific audit is asserted.

## References

- J. Gordon and F. Petrov, *Combinatorics of the Lipschitz Polytope*, arXiv:1608.06848v1 (2016); *Arnold Mathematical Journal* 3 (2017), 205–218. https://arxiv.org/abs/1608.06848
- A. D’Alì, E. Delucchi and M. Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193 (2019). https://arxiv.org/abs/1910.05193
- R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219v1 (2021), primary MSC2020 46B20. https://arxiv.org/abs/2102.01219
