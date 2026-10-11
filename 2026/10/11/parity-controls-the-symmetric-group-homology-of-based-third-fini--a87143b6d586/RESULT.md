# Parity controls the symmetric-group homology of based third finite-subset spaces of sphere bouquets
## Finding
For integers \(n\ge 1\) and \(d\ge 1\), let
\[
W_{n,d}=\bigvee_{i=1}^{n}S_i^d
\]
with common basepoint \(*\), and let \(S_n\) act by permuting the sphere summands through orientation-preserving identifications. Put \(P_n=\mathbb Z^n\) with its natural permutation action. Then the reduced integral homology of the based third finite-subset space \(\operatorname{Sub}_3(W_{n,d},*)\) is, as a \(\mathbb Z[S_n]\)-module,
\[
\widetilde H_q\bigl(\operatorname{Sub}_3(W_{n,d},*);\mathbb Z\bigr)\cong
\begin{cases}
P_n\otimes\mathbb Z/2, & q=d+1+r,\quad 1\le r<d-1,\ r\text{ odd},\\
P_n\oplus \mathbb Z\!\binom{[n]}2, & q=2d,\quad d\text{ even},\\
\bigwedge^2 P_n, & q=2d,\quad d\text{ odd},\\
0, & \text{otherwise}.
\end{cases}
\]
Here \(\mathbb Z\!\binom{[n]}2\) is the permutation lattice on unordered two-element subsets. Thus the free top-degree part changes character with the parity of \(d\): for even \(d\) it is an ordinary singleton-plus-pair permutation module, while for odd \(d\) it is the exterior square. In particular,
\[
\widetilde H_2\bigl(\operatorname{Sub}_3(W_{n,1},*);\mathbb Z\bigr)\cong\bigwedge^2\mathbb Z^n,
\]
and
\[
\operatorname{Sub}_3(W_{n,2},*)\simeq\bigvee^{\binom{n+1}{2}}S^4
\]
non-equivariantly.

## Assumptions and scope
The based third finite-subset space consists of subsets of cardinality at most three that contain the chosen basepoint. The action considered here only permutes the labeled sphere summands and preserves their chosen orientations. The statement is about integral homology as a module over the integral group ring; it does not claim an equivariant homotopy decomposition.

The notation \(\overline{\operatorname{SP}}^{2}(X)=\operatorname{SP}^{2}(X)/\operatorname{SP}^{1}(X)\) denotes the reduced symmetric square.

## Proof
Kallel and Sjerve identify the homology of \(\operatorname{Sub}_3(X,*)\) with a quotient of the homology of \(\operatorname{SP}^{2}(X)\) by the diagonal relations. For a suspension, every positive-dimensional reduced homology class is primitive, and their Proposition 5.6 gives the corresponding reduced-symmetric-square homology. Since the quotient map and the diagonal construction commute with based self-maps, this homology identification is equivariant for the permutation action on \(W_{n,d}\).

There is a canonical decomposition of the reduced symmetric square of a finite wedge:
\[
\overline{\operatorname{SP}}^{2}\!\left(\bigvee_i X_i\right)
\cong
\left(\bigvee_i\overline{\operatorname{SP}}^{2}(X_i)\right)
\vee
\left(\bigvee_{i<j}X_i\wedge X_j\right).
\]
Indeed, an unordered pair either lies in one wedge summand or has one point in each of two distinct summands. Distinct such strata meet only through pairs containing the common basepoint, and precisely that subspace is collapsed in the reduced symmetric square. Applying this with \(X_i=S_i^d\) gives \(n\) diagonal pieces and \(\binom n2\) off-diagonal pieces.

Kallel and Sjerve's sphere calculation gives
\[
\overline{\operatorname{SP}}^{2}(S^d)\simeq\Sigma^{d+1}\mathbb{RP}^{d-1}.
\]
Hence every diagonal piece contributes a copy of
\[
\widetilde H_r(\mathbb{RP}^{d-1};\mathbb Z)
\]
shifted upward by \(d+1\). The reduced integral homology of \(\mathbb{RP}^{d-1}\) is \(\mathbb Z/2\) in odd degrees \(r\) with \(1\le r<d-1\), and additionally \(\mathbb Z\) in degree \(d-1\) exactly when \(d\) is even. Permuting sphere labels merely permutes these \(n\) diagonal copies, giving the stated \(P_n\)-modules.

Each off-diagonal piece is
\[
S_i^d\wedge S_j^d\cong S^{2d}.
\]
If a permutation carries the pair \(\{i,j\}\) to \(\{a,b\}\) without reversing the ordered factors, the top class maps with sign \(+1\). Reversing the two smash factors has degree
\[
(-1)^{d^2}=(-1)^d.
\]
Therefore the off-diagonal top classes form the ordinary permutation lattice \(\mathbb Z\!\binom{[n]}2\) when \(d\) is even, but the oriented-pair lattice \(\bigwedge^2P_n\) when \(d\) is odd. Combining diagonal and off-diagonal contributions proves the formula and shows there are no other reduced homology groups.

For a permutation with \(X_1\) fixed points and \(X_2\) two-cycles, the rational character in degree \(2d\) is consequently
\[
X_1+\binom{X_1}{2}+X_2
\]
when \(d\) is even and
\[
\binom{X_1}{2}-X_2
\]
when \(d\) is odd. This gives a directly testable signature of the parity change.

## Verification
The accompanying `verify.py` constructs the singleton and oriented/unoriented pair modules for \(1\le n\le7\) and \(1\le d\le6\). It verifies the Coxeter relations for the adjacent transpositions, exhaustively checks the displayed character formulas on every permutation for \(n\le7\), and checks the homology-degree and reduced-Euler-characteristic consequences of the projective-space summands.

The computation verifies consequences of the symbolic proof; it is not used to extrapolate from finite \(n\) or \(d\).

## Relationship to prior work
Kallel and Sjerve prove the non-equivariant reduced-symmetric-square description for based third finite-subset spaces of suspensions and compute the one-sphere diagonal term. Their paper does not state a symmetric-group representation for bouquets, and targeted full-text searches found no use of “equivariant” or “representation” in this connection. The new point is the complete integral \(S_n\)-module structure for all bouquet sizes and sphere dimensions, including the parity-sensitive sign on off-diagonal smash classes.

Tuffley's earlier graph calculation gives homology for finite-subset spaces of bouquets of circles and discusses natural symmetric-group actions in a different cellular setting. It does not give the all-dimensional module formula above. Mostovoy and Sadykov later prove connectivity for finite-subset spaces of bouquets of spheres, which likewise does not determine these representations.

## Limitations
The result is for the based third finite-subset space and the summand-permuting action. It does not determine actions of arbitrary self-homotopy equivalences of the bouquet, nor does it claim an equivariant homotopy splitting. The originality check covered the exact finite-subset, reduced-symmetric-square, bouquet, and representation formulations, but an unindexed equivariant symmetric-product source could conceivably contain an equivalent module calculation.

## References
Sadok Kallel and Denis Sjerve, *Remarks on Finite Subset Spaces*, Homology, Homotopy and Applications **11** (2009), 229–250, DOI `10.4310/HHA.2009.v11.n2.a12`, arXiv `0902.3773`. The first public arXiv version is dated 2009-02-22. The paper lists 2000 Mathematics Subject Classification `55U10, 55S15`.

Christopher Tuffley, *Finite subset spaces of graphs and punctured surfaces*, Algebraic & Geometric Topology **3** (2003), 873–904, DOI `10.2140/agt.2003.3.873`, arXiv `math/0210315`.

Jacob Mostovoy and Rustam Sadykov, *On the connectivity of finite subset spaces*, Fundamenta Mathematicae **217** (2012), 279–282, DOI `10.4064/fm217-3-6`.
