# Exact affine-plane section-type probabilities for right square pyramids

## Finding
For every height \(h>0\), take the convex hull \(P_h\) of the square \((\pm1,\pm1,0)\) and apex \((0,0,h)\). Sample an unoriented affine plane by invariant measure \(d\sigma(u)\,dt\), conditioned on hitting the pyramid, where \(u\) is uniform on the unit sphere and \(t\) is the signed plane offset. Let \(N\) be the section polygon's vertex count. Put
\[
 r=\sqrt{1+h^2},\quad s=\sqrt{2+h^2},\quad
 \delta=\arccos(1/r),\quad\gamma=\arccos(1/r^2),
\]
\[
 B=2(\pi-\delta)+s\gamma,\qquad
 F=2s\arcsin(1/r^2)+4\delta-\pi\sqrt2.
\]
Then \(N\in\{3,4,5\}\) almost surely and
\[
 \Pr(N=5)=F/B,\quad
 \Pr(N=3)=4-\frac{2\pi(2+s)}{B}+F/B,\quad
 \Pr(N=4)=\frac{2\pi(2+s)}{B}-3-2F/B.
\]
For example at \(h=2\), the probabilities are approximately \((0.36485656,0.50418302,0.13096043)\). The pentagon probability is strictly positive for all \(h>0\), tends to zero as \(h\downarrow0\) and \(h\uparrow\infty\), and \(\Pr(N=5)\sim 2(2-\sqrt2)/h\) as \(h\to\infty\); hence it attains at least one interior maximum.

## Assumptions and scope
The apex lies above the center of a square of side \(2\); a similarity transformation covers every positive square side and height. Generic planes miss vertices and do not contain edges; such exceptional planes have invariant measure zero. The conditional distribution of orientations is **width-biased**: if \(w_P(u)=\max_{x\in P}u\cdot x-\min_{x\in P}u\cdot x\), the orientation density is proportional to \(w_P(u)\), then the offset is uniform on the interval of length \(w_P(u)\). It is not a uniformly oriented central section or an orthogonal shadow.

## Proof
Let \(v_0=(1,1,0)\), \(v_1=(-1,1,0)\), \(v_2=(-1,-1,0)\), \(v_3=(1,-1,0)\), and \(a=(0,0,h)\). A generic hyperplane cuts an edge exactly when its endpoints are on opposite sides. The pyramid graph has four base edges and four apex spokes. Five crossings occur if and only if \(\{a,v_i\}\) lie on one side and the remaining three base vertices on the other, for precisely one \(i\in\{0,1,2,3\}\). All other realizable nontrivial sign separations yield three or four crossings: a two-plus-three split of base vertices without the apex adjacent to a base vertex cannot be five, and the diagonally alternating base partition is unrealizable by a plane because the square's diagonals intersect.

To calculate the total signed-offset length for one chosen two-plus-three split, define
\[
 Q=\operatorname{conv}\{v_1,v_2,v_3\}-[a,v_0],\qquad Q^+=\operatorname{conv}(Q\cup\{0\}).
\]
For a unit normal \(u\), the two possible oriented separations occupy intervals with total offset length
\[
 \bigl(\min_{q\in Q}u\cdot q\bigr)_+
 +\bigl(\min_{q\in Q}(-u)\cdot q\bigr)_+
 =w_{Q^+}(u)-w_Q(u),
\]
where \((x)_+=\max(x,0)\). Thus, with mean width \(\bar w(K)=\mathbb E_{u\sim\sigma}w_K(u)\), the four disjoint pentagonal events have probability
\[
 \Pr(N=5)=\frac{4(\bar w(Q^+)-\bar w(Q))}{\bar w(P_h)}.
\]

For any three-dimensional convex polytope \(K\), the standard exact edge formula is
\[
 \bar w(K)=\frac1{4\pi}\sum_{e\in\operatorname{edges}(K)}|e|\,\vartheta_e,
\]
where \(\vartheta_e\in(0,\pi)\) is the exterior dihedral angle. The pyramid's four base edges have lengths \(2\), exterior angles \(\pi-\delta\); its four apex spokes have length \(s\), exterior angles \(\gamma\). Consequently \(\bar w(P_h)=B/\pi\).

For completeness, the six vertices of \(Q\) are \((-1,1,-h),(-1,-1,-h),(1,-1,-h),(-2,0,0),(-2,-2,0),(0,-2,0)\). The origin is exterior to the prism, beyond its diagonal rectangular side; forming \(Q^+\) replaces that side by three triangular facets. Compare the exterior-angle contributions of each edge, using the outward unit normals of the unchanged two coordinate sides \((-h,0,-1)/r\), \((0,-h,-1)/r\), the removed diagonal side \((h,h,2)/\sqrt{2h^2+4}\), and the three new facets \((1,1,0)/\sqrt2\), \((0,h,1)/r\), \((h,0,1)/r\). Direct dot products yield the following exact differences in the total sum \(\sum_e|e|\vartheta_e\): the changed two length-\(2\sqrt2\) edges jointly contribute \(-\pi\sqrt2\); the two old length-\(s\) edges contribute \(2s[\arccos(-1/r^2)-\arccos(-s/(\sqrt2r))]\); the two new length-\(s\) edges contribute \(2s\arccos(h/(\sqrt2r))\); and the two new length-\(2\) edges contribute \(4\arccos(1/r)\). All other edge contributions cancel. Since \(h^2+s^2=2r^2\), the bracketed angle combination with the extra length-\(s\) term equals \(\arcsin(1/r^2)\). Hence
\[
 4\pi[\bar w(Q^+)-\bar w(Q)]=2s\arcsin(1/r^2)+4\delta-\pi\sqrt2=F.
\]
Combining gives \(\Pr(N=5)=F/B\).

To obtain the rest of the distribution, apply the same orientation-and-offset normalization to edge crossings. For every fixed segment of length \(\ell\), its average projected length is \(\mathbb E|u\cdot e|=\ell/2\). Summing over all four base edges and four spokes gives
\[
 \mathbb E N=\frac{4\cdot2+4s}{2\bar w(P_h)}=\frac{2\pi(2+s)}{B}.
\]
Since the probabilities for \(3,4,5\) sum to one, and their weighted sum is \(\mathbb EN\), elementary elimination yields the displayed expressions.

Every \(h>0\) admits an open set of directions and offsets with a strict two-versus-three split, proving \(\Pr(N=5)>0\). Continuity and the formulas give \(F\to0\) and \(B\to2\pi\) as \(h\downarrow0\); as \(h\to\infty\), \(F\to\pi(2-\sqrt2)\) and \(B/h\to\pi/2\), yielding the stated asymptotic and existence of at least one interior maximizer.

## Verification
The accompanying executable `check.py` independently constructs the pyramid and the two auxiliary polyhedra as convex hulls, computes their mean widths from actual hull facets, and compares the closed expression at five heights. It also samples random orientation-offset pairs with the **correct width bias** and independently counts crossed edges. All checks pass with stated numerical tolerances. These finite and floating-point checks corroborate, but do not prove, the exact continuum identities; the proof is the edge-angle and Crofton calculation above.

## Relationship to prior work
Birkemeyer–Brose–Brandenburg–Prün [1] study combinatorial reconstruction from hyperplane sections, which motivates a probabilistic law for a concrete polytope. Brandenburg–De Loera–Meroni [2] optimize and classify affine sections in a different deterministic setting. A published exact law for five-vertex **orthogonal projections** of pyramids [4] is a different observable and sampling measure and does not imply the affine-section formula. Earlier stereological formulas for regular **prisms** [3] do not supply the square-pyramid distribution. The full text of [1] remained inaccessible in this check; its abstract alone does not certify the absence of an analogous calculation, so bibliographic priority remains uncertain.

## Limitations
This covers only right **square** pyramids and Euclidean-motion-invariant random affine planes. The proof does not determine the number or exact location of maximizing positive heights for the pentagonal probability, or provide arbitrary-rectangle and skew-pyramid analogues. An inaccessible recent full text and potentially unindexed stereological sources remain historical-overlap risks. No independent scientific audit has been performed.

## References
1. Anna Birkemeyer, Anouk E. Brose, Marie-Charlotte Brandenburg, Niklas Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195 (first public 2026-09-14). https://arxiv.org/abs/2609.16195
2. Marie-Charlotte Brandenburg, Jesús A. De Loera, Chiara Meroni, *The best ways to slice a polytope*, Mathematics of Computation **94** (2025), 1003–1042, arXiv:2304.14239. https://arxiv.org/abs/2304.14239
3. *Stereology for some classes of polyhedrons*, Advances in Applied Probability **27** (1995), 384–396. https://doi.org/10.2307/1427832
4. published-finding corpus record: *Exact five-vertex shadow law and unique height optimum for right rectangular pyramids*, 2026/10/11/SCOPE-exact-five-vertex-shadow-law-and-unique-height-optimum-for-right--2273575e8a0a (different random orthogonal-shadow observable).
