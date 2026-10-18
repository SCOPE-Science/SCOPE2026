# Complete Crofton polygon-type law for planar sections of rectangular boxes

## Finding
Let \(a,b,c>0\) and let \(K=[-a,a]\times[-b,b]\times[-c,c]\subset\mathbb R^3\). Sample an unoriented affine plane from Euclidean-motion-invariant plane measure, conditioned on meeting \(K\) in a nondegenerate polygon, and let \(p_k\) be the probability that the section has \(k\) sides. Set
\[
D=\sqrt{a^2b^2+a^2c^2+b^2c^2},\qquad(q_1,q_2,q_3)=D^{-1}(bc,ac,ab),
\]
\[
L=\sqrt{a^2+b^2+c^2},\quad A=a+b+c,
\]
\[
Q=\sqrt{a^2+b^2}\arccos q_3+\sqrt{a^2+c^2}\arccos q_2+\sqrt{b^2+c^2}\arccos q_1,
\]
\[
H=\sqrt{a^2+b^2}\arcsin q_3+\sqrt{a^2+c^2}\arcsin q_2+\sqrt{b^2+c^2}\arcsin q_1,
\]
\[
\begin{aligned}
\beta_1&=\arccos\frac{bc}{\sqrt{a^2+b^2}\sqrt{a^2+c^2}},\\
\beta_2&=\arccos\frac{ac}{\sqrt{a^2+b^2}\sqrt{b^2+c^2}},\\
\beta_3&=\arccos\frac{ab}{\sqrt{a^2+c^2}\sqrt{b^2+c^2}}.
\end{aligned}
\]
All inverse trigonometric functions take their principal values. The **complete law** is
\[
\boxed{p_3=2-\frac{4Q}{\pi A},\quad
p_6=\frac{2L(\beta_1+\beta_2+\beta_3)-4H}{\pi A},\quad
p_5=p_3-2p_6,\quad p_4=1-2p_3+p_6.}
\]
In fact, the affine-plane relation \(p_5=p_3-2p_6\) holds for **every nondegenerate three-dimensional parallelotope**, not just orthogonal boxes.

For the cube \(a=b=c\), define \(\gamma=\arccos(1/\sqrt3)\) and \(\alpha=\arcsin(1/\sqrt3)\). Then
\[
\boxed{p_3=2-\frac{4\sqrt2}{\pi}\gamma,\qquad
p_6=\frac{2\sqrt3}{3}-\frac{4\sqrt2}{\pi}\alpha,}
\]
with \(p_5=p_3-2p_6\), \(p_4=1-2p_3+p_6\), numerically
\[
(p_3,p_4,p_5,p_6)\simeq(0.279825723213,0.486796243994,0.186930342373,0.046447690420).
\]
This is the **translated-plane hitting measure**, not the distinct uniformly oriented central-plane experiment.

## Assumptions and scope
A representative oriented plane is \(\{x:u\cdot x=t\}\), with \(u\in S^2\), \(t\in\mathbb R\). Euclidean-motion-invariant measure is proportional to \(d\sigma(u)\,dt\); double counting by \((u,t)\sim(-u,-t)\) cancels on conditioning. The plane is conditioned to have a nonempty two-dimensional intersection with the box. Plane positions passing through vertices or containing edges form a null set, so their section-side conventions are immaterial. The half-edge lengths are any positive real numbers, with no ordering or normalization restrictions.

For general parallelotopes, the same affine-plane measure is used, and the stated universal relation is an identity of section-type probabilities, not a claim that their individual probabilities equal those of an orthogonal box. Scaling all edge vectors by one factor does not change these probabilities.

## Proof
**1. Offset sweep and an affine universal identity.** Write an arbitrary full-dimensional parallelotope as \(P=x_0+[-v_1,v_1]+[-v_2,v_2]+[-v_3,v_3]\), with linearly independent generating vectors. Fix a generic unit normal \(u\), put \(x_i=|u\cdot v_i|\), and reorder these three positive values as \(X>Y>Z>0\). The eight vertex heights are the signed sums \(\pm X\pm Y\pm Z\). On each open interval between successive distinct vertex heights, the section has as many sides as the number of parallelotope edges crossed by the plane. Each of the twelve edges changes one sign in this three-bit description.

Writing \(s=X+Y+Z\) and \(h=(Y+Z-X)_+\), direct ordering of the eight heights gives total lengths of offsets producing the four polygon types:
\[
\boxed{\ell_3=4Z,\quad \ell_4=2s-8Z+2h,\quad
\ell_5=4(Z-h),\quad\ell_6=2h.}
\]
For clarity, if \(X<Y+Z\), the successive numbers of sides as the plane rises are \(3,4,5,6,5,4,3\), with successive offset lengths \(2Z,2(Y-Z),2(X-Y),2(Y+Z-X),2(X-Y),2(Y-Z),2Z\). If \(X>Y+Z\), they are \(3,4,5,4,5,4,3\), with lengths \(2Z,2(Y-Z),2Z,2(X-Y-Z),2Z,2(Y-Z),2Z\). These cases exhaust generic normals. Both sum to \(2s\). Consequently
\[
\ell_5=\ell_3-2\ell_6
\]
**for each generic normal separately**. Integrating against any nonnegative angular weight, in particular invariant measure, proves the universal parallelotope identity.

**2. Weighted sphere and two scalar moments.** For the orthogonal box use \(x_1=a|u_1|\), \(x_2=b|u_2|\), \(x_3=c|u_3|\), and put \(m=\min_i x_i\), \(h=(x_1+x_2+x_3-2\max_i x_i)_+\). If \(U\) is uniform on \(S^2\), the normalized motion-invariant probability of a \(k\)-sided section is \(\mathbb E[\ell_k(U)]/\mathbb E[2s(U)]\). As \(\mathbb E|U_i|=1/2\), the denominator is \(A\). Thus
\[
p_3=\frac{4\mathbb Em}{A},\quad p_6=\frac{2\mathbb Eh}{A},\quad
p_5=p_3-2p_6,\quad p_4=1-2p_3+p_6.
\]
It remains to evaluate exactly \(\mathbb Em\) and \(\mathbb Eh\).

**3. Spherical triangle integration identity.** On a region \(\Omega\subset S^2\) bounded by arcs of great circles, let each arc have length \(d_j\) and unit *inward* spherical co-normal \(n_j\), constant along that arc. Since \(\Delta_{S^2}(w\cdot u)=-2w\cdot u\), Green's identity gives
\[
\int_\Omega w\cdot u\,d\sigma(u)=\frac12\sum_j d_j\,(w\cdot n_j).
\]
The formula applies to the spherical triangles below, including their boundaries of zero area.

**4. Mean of the minimum.** Work in the positive octant. The region in which \(a_i u_i\) is smallest has vertices \(e_j,e_k,q\), where
\[
q=\frac{(a^{-1},b^{-1},c^{-1})}{\sqrt{a^{-2}+b^{-2}+c^{-2}}}
=(q_1,q_2,q_3).
\]
The edge in the plane \(u_i=0\) has length \(\pi/2\). The other two edges have lengths \(\arccos q_k\) and \(\arccos q_j\), with inward unit co-normals \((-a_i e_i+a_j e_j)/\sqrt{a_i^2+a_j^2}\) and \((-a_i e_i+a_k e_k)/\sqrt{a_i^2+a_k^2}\). Apply the identity with \(w=a_i e_i\), sum over \(i=1,2,3\), and multiply by the eight-octant spherical normalization \(8/(4\pi)=2/\pi\). Pairing the two contributions to each equality edge gives
\[
\boxed{\mathbb E m=\frac A2-\frac Q\pi.}
\]

**5. Mean of the positive triangle defect.** Within the positive octant, the region where \(a_i u_i\) is largest but smaller than the other two terms combined is a spherical triangle with vertices \(q\) and the normalized coordinate-pair rays \(r_{ij}\propto a_i^{-1}e_i+a_j^{-1}e_j\), \(r_{ik}\propto a_i^{-1}e_i+a_k^{-1}e_k\). Its two edges from \(q\) have lengths \(\arcsin q_k\) and \(\arcsin q_j\); its remaining edge has length \(\beta_i\), since the dot product of the two normalized pair rays is \(a_j a_k/[\sqrt{a_i^2+a_j^2}\sqrt{a_i^2+a_k^2}]\). For the linear integrand \(h=a_j u_j+a_k u_k-a_i u_i\), the inward unit co-normals on the three edges yield the scalar products \(-\sqrt{a_i^2+a_j^2}\), \(-\sqrt{a_i^2+a_k^2}\), and \(L\). Sum the spherical identity over \(i\), pairing edges and normalizing octants. This gives
\[
\boxed{\mathbb E h=\frac{L(\beta_1+\beta_2+\beta_3)-2H}{\pi}.}
\]
Substitution into step 2 proves all four general probabilities.

**6. The cube.** If \(a=b=c\), then \(q_i=1/\sqrt3\), \(\beta_i=\pi/3\), \(Q=3\sqrt2a\gamma\), \(H=3\sqrt2a\alpha\), \(L=\sqrt3a\), and \(A=3a\). Substitution proves the displayed cube formulas and completes the proof. \(\square\)

## Verification
A standalone Python 3 standard-library checker `verify.py` independently constructs the eight signed vertex heights and all twelve cuboid edges. It counts crossed edges at the midpoint of each open height interval, reconstructs the four offset-length totals, and tests them against the algebraic sweep without assuming the latter in the independent count. Five varied aspect ratios, including the cube and a strongly anisotropic box, were checked for 25,000 reproducible randomly selected unit normals each (125,000 configurations and up to 875,000 nondegenerate offset intervals), along with numerical sphere-average comparisons to the closed formula. All tests passed with the final output `VERIFY_OK`. They check implementations and examples; the proof above, not sampling, establishes the identities for every positive aspect ratio and generic orientation.

## Relationship to prior work
Lonke, *On random sections of the cube* (1998), computes face-count expectations for **central linear sections**. In dimension three such central sections are almost surely quadrilaterals or hexagons. The published result titled *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes* gives the same central-plane model for all unequal boxes. Neither central-plane law covers the present translated-plane, hit-conditioned Crofton measure: its cube hexagon probability is about \(0.04644769\), rather than the known central-plane value about \(0.35095931\). The present theorem also gives four rather than two possible section types.

Marichal and Mossinghoff, *Slices, slabs, and sections of the unit hypercube* (arXiv first public version 2006), give general formulas for fixed-plane section **areas/volumes** and integrals over cubical slices; the full text does not give a motion-invariant affine-plane distribution of polygon side counts. Those slice formulas are important related prior geometric machinery, not an assertion of this four-probability law. Chakerian and Logothetti, *Cube slices, pictorial triangles, and probability* (1991), is a plausible historical overlap source whose full text was not accessible in the checks; its contents therefore remain a specific historical-priority risk, not a certified negative. Classical kinematic measure and spherical integration identities are likewise not claimed as new.

## Limitations
No claim is made for other plane-selection models such as Haar-distributed central planes, planes chosen by sampling a point uniformly in the volume, or arbitrary changes to angular weighting (except that the pointwise identity continues to hold after consistent angular averaging). For oblique parallelotopes, only the identity \(p_5=p_3-2p_6\) is asserted, not the orthogonal-box closed formulas. The probability classifications exclude a measure-zero set of degenerate tangent/vertex-containing planes. Related unindexed historical formulas may affect priority; independent validation has not been performed. The numerical checker alone is not a universal proof.

## References
[1] Y. Lonke, *On random sections of the cube*, arXiv:math/9812123v1, initially public 1998-12-21, https://arxiv.org/html/math/9812123v1.

[2] J.-L. Marichal and M. J. Mossinghoff, *Slices, slabs, and sections of the unit hypercube*, arXiv:math/0607715v1, initially public 2006-07-27; full-text revised version https://arxiv.org/html/math/0607715v2.

[3] D. Chakerian and D. Logothetti, *Cube Slices, Pictorial Triangles, and Probability*, Mathematics Magazine 64 (1991), 219–241, https://doi.org/10.2307/2690829.

[4] R. Coleman, *Random paths through convex bodies*, Journal of Applied Probability 6 (1969), 430–441, https://doi.org/10.2307/3212012 (distinct random-line model).

[5] OEIS A349605, central-plane hexagonal-section probability of a cube, https://oeis.org/A349605 (different sampling law).
