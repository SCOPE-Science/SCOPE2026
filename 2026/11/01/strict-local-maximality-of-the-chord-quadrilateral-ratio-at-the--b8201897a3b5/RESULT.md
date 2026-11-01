# Strict local maximality of the chord-quadrilateral ratio at the affine-regular heptagon

## Finding
Let \(P\) be a strictly convex, counterclockwise labelled heptagon in the Euclidean plane. A chord quadrilateral is a convex polygon with at most four sides containing \(P\), each side parallel to a segment between two vertices of \(P\). Write \(q_{\mathrm{ch}}(P)\) for its least possible area. If \(P_7\) is a regular heptagon, then there is a neighborhood of the affine orbit of \(P_7\) in the space of labelled convex heptagons and a constant \(c>0\) such that every \(P\) in that neighborhood satisfies
\[
\frac{q_{\mathrm{ch}}(P)}{|P|}\le R_*-c\|z(P)\|^2,\qquad
R_*=\frac47+\frac{3}{7\cos(2\pi/7)}=1.258803773547004\ldots.
\]
Here \(z(P)\in\mathbb R^8\) is the affine-normalized displacement specified below. In particular, equality occurs locally **only** for affine images of the regular heptagon. This does **not** resolve the global chord conjecture.

## Assumptions and scope
Take the regular unit-circumradius heptagon with vertices \(v_j=(\cos(2\pi j/7),\sin(2\pi j/7))\), indexed \(j=0,\ldots,6\) modulo seven. For a nearby ordered convex heptagon, apply the unique invertible affine transformation carrying its vertices numbered \(0,1,2\) to \(v_0,v_1,v_2\). Its remaining four vertices then have the form \(v_j+(z_{2j-6},z_{2j-5})\), \(j=3,4,5,6\). This defines \(z=z(P)\). All sufficiently small such \(z\) yield strictly convex heptagons. The ratio and the chord-direction condition are invariant under invertible affine transformations.

## Proof
**Seven smooth chord quadrilaterals.** For each \(j=0,\ldots,6\), choose the supporting lines through the polygon edges numbered \(j,j+2,j+4,j+6\), in this cyclic order. At the regular heptagon these four lines form a bounded, nondegenerate quadrilateral containing the heptagon, and they continue doing so for all sufficiently small normalized perturbations. Denote its area divided by polygon area by \(f_j(z)\). Since the chosen sides are themselves chords, every \(f_j\) is a lawful chord-quadrilateral competitor, and
\[
\frac{q_{\mathrm{ch}}(P)}{|P|}\le\min_{0\le j\le6}f_j(z).
\]
These seven rational functions are smooth near the origin. Explicitly, for consecutive polygon vertices \(p_k=(x_k,y_k)\), set \(n_k=(y_{k+1}-y_k,x_k-x_{k+1})\), \(h_k=\langle n_k,p_k\rangle\). The intersection of support lines \(a,b\) is
\[
I_{ab}=\frac{(h_a n_{b,2}-h_b n_{a,2},\ n_{a,1}h_b-n_{b,1}h_a)}{\det(n_a,n_b)}.
\]
The shoelace area of the four consecutive intersections, divided by \(\tfrac12\sum_k\det(p_k,p_{k+1})\), is precisely \(f_j\).

**Exact base value.** All chord-parallel support directions of the regular heptagon have outward normals at the fourteen angles \(k\pi/7\) with \(0\le k<14\), and corresponding support distances \(1\) for even \(k\) and \(\cos(\pi/7)\) for odd \(k\). The finite exhaustive certificate described under Verification checks every four-direction choice capable of forming a bounded four-sided enclosure (511 choices). Its seven minimizers are exactly the rotated edge sets \(\{j,j+2,j+4,j+6\}\). It obtains their common exact area ratio \(R_*\). A three-sided enclosure is larger: the heptagon contains a disk of radius \(r=\cos(\pi/7)\), and any enclosing triangle has area at least \(3\sqrt3r^2\), which exceeds the minimizing quadrilateral area. To see the triangle bound, move each side until tangent to the disk and apply convexity of \(\cot\) to its three half-angles. Therefore \(q_{\mathrm{ch}}(P_7)/|P_7|=R_*\).

**First-order annihilation.** Let \(G\) denote the \(7\times8\) matrix of first derivatives of the seven functions at \(z=0\). The exact identity \(\sum_jG_{ji}=0\) for every \(i\) follows without numerics. Indeed \(\sum_jf_j\), viewed before affine gauge fixing as a function of seven vertex positions, is invariant under rotating and relabelling the regular heptagon and under all affine transformations. Its differential at the regular heptagon must be a cyclically equivariant linear functional \(\sum_j\langle a v_j+bJv_j,\delta v_j\rangle\), with \(J\) the quarter-turn; scale and rotation invariance force \(a=b=0\). Thus the derivative vanishes on the full vertex space and on the affine slice.

The certified \(6\times6\) minor with the first six rows of \(G\) and normalized-coordinate columns \(0,1,3,4,6,7\) is enclosed in
\[
-0.000055654 <\det G_{\mathrm{minor}}<-0.000055653.
\]
Consequently \(\operatorname{rank}G=6\), and \(K=\ker G\subset\mathbb R^8\) has dimension two. The sum-zero relation also shows that for every \(w\) outside \(K\), at least one \(\langle G_j,w\rangle\) is strictly negative.

**Second-order obstruction on the common kernel.** Let \(\overline H=\tfrac17\sum_{j=0}^6D^2f_j(0)\). Write the complementary normalized-coordinate indices as \(2,5\). The first six gradient rows uniquely determine kernel vectors from these two free coordinates. Thus \(K=\operatorname{im}B\), where \(B_{(2,5),:}=I_2\), and its other six rows are minus the inverse of the above gradient minor times the corresponding two gradient columns. The rigorously enclosed reduced matrix is
\[
B^T\overline H B\in
\begin{pmatrix}
(-0.279368,-0.279367)&(0.089920,0.089922)\\
(0.089920,0.089922)&(-0.194606,-0.194605)
\end{pmatrix},
\]
with determinant in \((0.0462806,0.0462807)\). Sylvester's criterion proves strict negative definiteness on \(K\).

**Nonsmooth local maximality and quadratic deficit.** Split every sufficiently small \(z\) uniquely as \(z=k+w\), with \(k\in K\) and \(w\) in the fixed six-dimensional coordinate complement. Because the seven linear forms sum to zero and have kernel \(K\), compactness of the unit sphere in that complement gives \(\min_j\langle G_j,w\rangle\le -c_1\|w\|\) for some \(c_1>0\). Smoothness therefore gives
\[
\min_j f_j(z)\le R_*-c_1\|w\|+C\|z\|^2.
\]
If \(\|w\|\ge L\|k\|^2\), choose \(L\) large and \(\|z\|\) sufficiently small to obtain a deficit bounded below by a positive multiple of \(\|w\|\), hence of \(\|z\|^2\). Otherwise \(\|w\|<L\|k\|^2\), and the exact zero-average gradient and negative definite average Hessian yield
\[
\min_jf_j(z)\le\frac17\sum_jf_j(z)\le R_*-c_2\|k\|^2+o(\|k\|^2).
\]
As \(\|z\|\asymp\|k\|\) in this regime, this again yields the asserted quadratic deficit. Both cases are strict unless \(z=0\). Undoing affine normalization proves the theorem.

## Verification
Run `python verify.py` with `mpmath` installed. The script uses outward-rounded 45-digit interval arithmetic, not heuristic tolerance tests: it constructs all seven rational second-order jets at the regular heptagon, proves the gradient sum encloses zero, certifies the rank-six minor, computes the reduced Hessian on the two-dimensional kernel and checks its negative definiteness. The exact sum-zero identity is proved geometrically above; interval inclusion of zero alone would not prove that identity. The script additionally exhausts 511 bounded combinations of four of the fourteen chord-normal support directions and excludes possible three-sided minimizers by the incircle bound. Its outputs contain certified enclosures and PASS lines. The interval matrix is not a claim that its rounded displayed decimals are exact identities; the programmed interval signs are the certificate.

## Relationship to prior work
Vígh, *A note on Kuperberg's quadrilateral conjecture* (arXiv:2610.08168v1, 6 October 2026), introduces the chord-restricted optimization and reports numerical runs ending at affine-regular heptagons, which **appear** to be local maxima (Section 2, Numerical experiments). The contribution here is a proof of strict local maximality modulo affine maps and a local quadratic deficit, not the mere numerical identification of the regular heptagon's area ratio. Fodor and Grundbacher, *On the minimal area of quadrangles circumscribed about planar convex bodies* (arXiv:2506.05185v1), prove a global weak approximation bound for unrestricted circumscribed quadrilaterals, not this chord-restricted heptagon stability theorem. The previously known exact regular-heptagon value is independently rederived in the finite-direction certificate rather than claimed as new.

## Limitations
Only sufficiently small perturbations of the affine-regular heptagon are covered, with no explicit optimal stability radius or sharp quadratic constant. The global chord conjecture for arbitrary polygons, including all heptagons, remains open. The mathematical correctness assessment is based on an analytic proof and reproducible interval certificates, not an independent human audit. Historical publication priority is not independently established.

## References
1. V. Vígh, *A note on Kuperberg's quadrilateral conjecture*, arXiv:2610.08168v1 (6 October 2026), https://arxiv.org/html/2610.08168v1 .
2. F. Fodor and F. Grundbacher, *On the minimal area of quadrangles circumscribed about planar convex bodies*, arXiv:2506.05185v1 (5 June 2025), https://arxiv.org/html/2506.05185 .
