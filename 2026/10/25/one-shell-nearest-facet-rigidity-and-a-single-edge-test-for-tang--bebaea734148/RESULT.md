# One-shell nearest-facet rigidity and a single-edge test for tangential quadrilaterals

## Finding

Let \(P\subset\mathbb R^d\), \(d\ge2\), be a full-dimensional compact convex polytope with \(m\) distinct facets, \(m\ge d+1\). Pick \(X\) uniformly by volume. Define the **Euclidean clearance** \(T=\mathrm{dist}(X,\partial P)\). Away from measure-zero ties, let \(J\in\{1,\ldots,m\}\) label the facet reached by the shortest segment from \(X\) to the boundary. Let \(r>0\) be the inradius. For \(0\le t<r\), let \(P_t=\{x\in P:\mathrm{dist}(x,\partial P)\ge t\}\), and let \(A_i(t)\) be its facet area with the \(i\)-th original outward normal, taking \(A_i(t)=0\) when that facet has vanished. Write
\[
q_i(t)=\frac{A_i(t)}{\sum_j A_j(t)}.
\]

**One-shell tangency theorem.** The following are equivalent:

1. \(P\) has a Euclidean inball tangent to every facet (that is, \(P\) is tangential).
2. The random variables \(T\) and \(J\) are independent.
3. There exists **one** \(t_0\in(0,r)\) such that \(q_i(t_0)=q_i(0)\) for **every** \(i\).

Here \(q_i(t)\) is the canonical density-level conditional probability \(\Pr(J=i\mid T=t)\). In the tangential case \(T/r\) has the \(\mathrm{Beta}(1,d)\) law, and \(\Pr(J=i)=A_i(0)/\sum_j A_j(0)\).

**Sparse one-shell test.** It suffices in condition 3 to check a subset of facets, provided the untested outward unit normals \(u_j\), augmented as vectors \((1,u_j)\in\mathbb R^{d+1}\), are linearly independent. Thus every convex \(m\)-gon with \(m\ge4\) is tangential **if and only if**, at any specified \(t_0\in(0,r)\), the equalities \(q_i(t_0)=q_i(0)\) hold on any \(m-3\) named edges. In particular, **one named edge alone certifies the existence of an incircle in every convex quadrilateral**. The equality may be checked at any positive sub-inradius offset, not merely an infinitesimal shell.

## Assumptions and scope

All facets are genuine distinct \((d-1)\)-faces, and their defining outward vectors \(u_i\) have Euclidean norm one. We make no generic-position or facet-survival assumptions. At any \(0<t<r\), \(P_t\) is full-dimensional, although some original facets may disappear. A tangential polytope means one Euclidean ball touches each original facet; it does not mean merely that an inball touches some facets. \(J\) is a facet label and is observable as the minimizing normal-offset constraint, except on a set of volume zero. The conditional probabilities at zero-probability exact levels are specified by continuous facet-area profiles, rather than by arbitrary choices of conditional-probability versions.

## Proof

### 1. Clearance and coarea

Write the irredundant supporting representation
\[
P=\bigcap_{i=1}^m\{x:\langle u_i,x\rangle\le h_i\}.
\]
For every \(x\in P\), the distance to the complement and hence to the boundary is
\[
T(x)=\min_i(h_i-\langle u_i,x\rangle).
\]
Therefore \(P_t=\bigcap_i\{x:\langle u_i,x\rangle\le h_i-t\}\). Except on finitely many affine bisector hyperplanes, exactly one index minimizes the slacks and the gradient of \(T\) is \(-u_i\), whose Euclidean norm is one. Coarea on those regions gives, for almost every \(t\in(0,r)\),
\[
\frac{\Pr(J=i,T\in dt)}{dt}=\frac{A_i(t)}{\mathrm{Vol}_d(P)},\qquad
f_T(t)=\frac{\sum_j A_j(t)}{\mathrm{Vol}_d(P)}.
\]
The facet-area functions are continuous on the sub-inradius interval: each is a piecewise-algebraic facet-volume function of the continuously varying finite half-space system and tends to zero at facet loss. Consequently \(q_i(t)\) is the natural continuous version of \(\Pr(J=i\mid T=t)\), with \(q_i(0)=A_i(0)/\sum_j A_j(0)>0\).

### 2. One interior shell forces an inball touching every facet

Suppose \(q_i(t_0)=q_i(0)\) for all \(i\), for a fixed \(0<t_0<r\). Since every \(A_i(0)>0\), every \(A_i(t_0)>0\), and there is a common positive factor
\[
c=\frac{\sum_j A_j(t_0)}{\sum_j A_j(0)}
\quad\text{such that}\quad A_i(t_0)=cA_i(0)\quad(i=1,\ldots,m).
\]
Let \(s=c^{1/(d-1)}\). The polytopes \(P_{t_0}\) and \(sP\) have **identical surface-area measures**: they have the same facet-normal directions, and their corresponding facet areas agree. Minkowski's uniqueness theorem for convex polytopes gives some \(w\in\mathbb R^d\) with
\[
P_{t_0}=w+sP.
\]
Since \(P_{t_0}\subsetneq P\) and both are full-dimensional, their volumes show \(s<1\). Since all original facets survive at \(t_0\), comparing supports in each \(u_i\) gives
\[
h_i-t_0=\langle u_i,w\rangle+s h_i.
\]
Thus, with \(z=w/(1-s)\) and \(\rho=t_0/(1-s)>0\),
\[
h_i-\langle u_i,z\rangle=\rho\quad\text{for every }i.
\]
The ball \(B(z,\rho)\) lies in \(P\) and touches every facet. It is an inball: if \(B(y,R)\subseteq P\), then \(\langle u_i,y-z\rangle\le\rho-R\) for all \(i\). Multiplying by the strictly positive original facet areas and using \(\sum_i A_i(0)u_i=0\) (the divergence theorem), gives \(0\le(\rho-R)\sum_i A_i(0)\), whence \(R\le\rho\). Therefore \(\rho=r\).

Conversely, if an inball \(B(z,r)\) touches every facet, then \(h_i=\langle u_i,z\rangle+r\), and for all \(0\le t<r\),
\[
P_t=z+(1-t/r)(P-z),\qquad A_i(t)=(1-t/r)^{d-1}A_i(0).
\]
Hence every \(q_i\) is constant, proving the equivalence of conditions 1 and 3. In this case \(\mathrm{Vol}(P_t)/\mathrm{Vol}(P)=(1-t/r)^d\), so \(T/r\) is \(\mathrm{Beta}(1,d)\). Coarea factorization yields independence of \(J\) and \(T\). Conversely, independence implies \(q_i(t)\) equals a constant for almost every \(t\); continuity and passage to \(t\downarrow0\) identify this constant with \(q_i(0)\), proving condition 3.

### 3. Sparse facet tests

The flux-balancing identities \(\sum_i A_i(t)u_i=0\) and \(\sum_i A_i(0)u_i=0\) imply, with \(\delta_i=q_i(t_0)-q_i(0)\),
\[
\sum_i\delta_i=0,\qquad\sum_i\delta_i u_i=0.
\]
If the tested facets have \(\delta_i=0\), these equations reduce to a linear dependence among the augmented vectors \((1,u_i)\) of the untested facets. If those vectors are linearly independent, all \(\delta_i=0\), so part 2 yields tangency. For any convex polygon, distinct edge outward unit normals are distinct points on the unit circle, and no three distinct points of a circle are collinear. Therefore any three augmented normals are independent. Testing any \(m-3\) edges suffices if \(m\ge4\). Every triangle has an incircle, so there is no exceptional three-edge case. For a quadrilateral, this reduces to a test of just one edge.

## Verification

The embedded standalone `CHECK.py` reproduces facet-length proportions for scalene triangles, squares, rhombi, rectangles, oblique parallelograms, and a trapezoid, using the exact inward-parallel edge-length identity for a fixed combinatorial regime, and checks corresponding facet areas for three-dimensional boxes. It verifies that tangential examples preserve all proportions while non-tangential quadrilaterals change **each** of the four proportions. The script is a finite diagnostic, not a replacement for the analytic proof.

As an exact example, for the rectangle \([0,4]\times[0,2]\), at offset \(t=1/4\) one long-side shell proportion changes from \(1/3\) to \(7/20\), while one short-side proportion changes from \(1/6\) to \(3/20\). In contrast, every triangle, irrespective of shape, has constant facet-label proportions at every level below its inradius.

## Relationship to prior work

Minkowski uniqueness from facet normals and their areas is classical (recalled in Alexandrov, arXiv:math/0211286). Linke and Saorín Gómez, *Decomposition of polytopes using inner parallel bodies* (preprint 2013, published 2015), study support functions, facet survival, Minkowski summands, and the already-known equivalence between **all** offsets being homothetic and tangency to the form body (their §2, citing Schneider, Lemma 3.1.10). Larson, *A bound for the perimeter of inner parallel bodies* (arXiv:1508.06414; revised 2020), proves a sharp **total** surface-area inequality and characterizes its equality shapes. In particular, scalar inradius-normalized clearance bounds and the homothetic law for tangential bodies are **not** claimed novel. The assessed claim is the joint nearest-facet/depth criterion, its **one-shell** converse without a known scaling factor, and the sparse one-facet quadrilateral characterization, obtained by combining coarea, Minkowski uniqueness and equilibrium of facet normals. These statements are not asserted to supersede the cited inner-parallel-body theory.

## Limitations

The result requires convex polytopes and Euclidean clearance; it does not characterize arbitrary nonconvex domains or provide a quantitative stability constant under noisy sampling. A conditional probability at a single exact depth is a population-level density concept, not a finite-sample test without estimation error. For polytopes with many facets, a single facet's proportion is generally insufficient; the stated sparse condition requires affine independence of the remaining augmented normals. All claims are analytical; floating-point checks are illustrations. An equivalent unstated reformulation in older work on form bodies or surface-area measures cannot be ruled out by text searches alone.

## References

1. V. Alexandrov, *Minkowski-type and Alexandrov-type theorems for polyhedral herissons*, arXiv:math/0211286 (initial public version 2002-11-19), https://arxiv.org/abs/math/0211286.
2. E. Linke and E. Saorín Gómez, *Decomposition of polytopes using inner parallel bodies*, *Monatshefte für Mathematik* **176** (2015), 575–588, DOI:10.1007/s00605-014-0629-z. Open manuscript: https://user.math.uni-bremen.de/~esaoring/Decomp%20polytopes%20inner.pdf.
3. S. Larson, *A bound for the perimeter of inner parallel bodies*, arXiv:1508.06414 (initial public version 2015-08-26; corrected 2020), https://arxiv.org/html/1508.06414v3.
