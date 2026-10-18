# Elementary Crofton section-type law and quadratic hexagon extinction for rectangular boxes

## Finding
For every Euclidean rectangular box \(B=[-a,a]\times[-b,b]\times[-c,c]\), with \(a,b,c>0\), take an unoriented affine plane from the Euclidean-motion-invariant measure, conditioned on intersecting \(B\). Let \(N\) be the number of vertices of its section, ignoring the null set of nongeneric planes. The probabilities of the four possible types \(N=3,4,5,6\) are given by the following **elementary finite formula** for all positive aspect ratios, without spherical integrals or numerical quadratures.

Set \(s=a+b+c\), \(\Delta=\sqrt{a^2b^2+b^2c^2+c^2a^2}\), and write \(\sum_{i<j}\) for the pairs from \((a,b,c)\). Define
\[
 T(a,b,c)=\frac{s}{2}-\frac1\pi\sum_{i<j}\sqrt{a_i^2+a_j^2}\arccos\!\left(\frac{a_i a_j}{\Delta}\right),
\]
\[
 D(x;y,z)=\frac{1}{\pi}\left[\sqrt{x^2+y^2+z^2}\arccos\!\left(\frac{yz}{\sqrt{x^2+y^2}\sqrt{x^2+z^2}}\right)
 -z\arctan\frac{x}{y}-y\arctan\frac{x}{z}\right],
\]
\[
 Q(a,b,c)=\frac{3s}{2}-\sum_{i<j}\sqrt{a_i^2+a_j^2}-2T(a,b,c)
 +D(a;b,c)+D(b;a,c)+D(c;a,b).
\]
Then
\[
 \boxed{\begin{aligned}
  \Pr(N=3)&=4T/s,\\
  \Pr(N=4)&=1-8T/s+2Q/s,\\
  \Pr(N=5)&=4T/s-4Q/s,\\
  \Pr(N=6)&=2Q/s.
 \end{aligned}}
\]
In particular, when one half-length collapses with the other two held fixed, the rare hexagonal sections obey the sharp **quadratic extinction law**
\[
 \boxed{\lim_{c\downarrow0}\frac{\Pr(N=6)}{c^2}=\frac{1}{(a+b)\sqrt{a^2+b^2}}.}
\]
The last limit has a finite, strictly positive coefficient for every fixed \(a,b>0\).

## Assumptions and scope
An unoriented affine plane is described by its unit normal \(u\in S^2\) (with \(u\) identified with \(-u\)) and offset \(t\in\mathbb R\). The invariant measure is proportional to \(d\sigma(u)\,dt\), not a product of uniform normal and uniform conditional offset. Conditioning on a nonempty intersection weights a normal \(u\) by the box's half-width \(h(u)=a|u_1|+b|u_2|+c|u_3|\). The formula applies to a box with orthogonal edges, regardless of translation, rotation, or positive common scaling; no claim is made about oblique parallelepipeds.

For independent uniformly distributed \(U\in S^2\), put \(A=a|U_1|\), \(B=b|U_2|\), \(C=c|U_3|\), \(S=A+B+C\), \(M=\max(A,B,C)\). Then \(\mathbb E S=s/2\). The two essential geometric expectations evaluated below are \(T=\mathbb E\min(A,B,C)\) and \(Q=\mathbb E(S-2M)_+\), with \(x_+=\max(x,0)\).

## Proof
**1. Fixed-normal section enumeration.** For a fixed generic normal, sort the three positive projected half-lengths as \(\xi\ge\eta\ge\zeta\). An affine plane crosses a box edge precisely when the signed values of its endpoint supporting linear functional straddle its offset. Enumerating the twelve edges and sweeping \(t\) from \(-h\) to \(h\), using symmetry under \(t\mapsto-t\), gives the following total lengths of **positive-offset** intervals of each section type:
\[
 \ell_3=2\zeta,\quad
 \ell_6=(\eta+\zeta-\xi)_+,\quad
 \ell_5=2\min(\xi-\eta,\zeta),\quad
 \ell_4=2(\eta-\zeta)+(\xi-\eta-\zeta)_+.
\]
These sum to \(h=\xi+\eta+\zeta\). In particular \(\ell_6=(S-2M)_+\). Normalizing the invariant plane measure by \(\mathbb E h=s/2\) proves \(p_6=2Q/s\) and \(p_3=4T/s\). The pointwise identity \(\ell_3-\ell_5-2\ell_6=0\), combined with \(\sum\ell_k=h\), gives \(p_5=p_3-2p_6\), \(p_4=1-2p_3+p_6\), exactly the claimed four formulas. The generic exceptional normals and offsets have zero invariant measure.

**2. Evaluation of the minimum.** By symmetry, perform all spherical integrals in the positive octant with normalized measure \(2\,d\sigma/\pi\). The boundaries between the three cells where \(a u_1\), \(b u_2\), or \(c u_3\) is smallest are great-circle arcs. Their common interior vertex is the direction proportional to \((bc,ac,ab)\). For a spherical polygon with vertices \(v_j\), the integral of the position vector is exactly
\[
 \int_{\mathrm{polygon}}u\,d\sigma(u)=\frac12\sum_{\mathrm{edges}\ [v_j,v_{j+1}]}
 \theta_j\frac{v_j\times v_{j+1}}{\|v_j\times v_{j+1}\|},
\]
where \(\theta_j=\arccos(v_j\cdot v_{j+1})\) and edge orientation agrees with outward-facing spherical Stokes orientation. This follows componentwise by applying Stokes to a constant vector field's tangential projection; equivalently integrate the oriented great-circle boundary. Apply it separately to the three minimum cells and sum the linear forms \(a u_1\), \(b u_2\), \(c u_3\). The boundary arcs have endpoint angle factors \(\arccos(ab/\Delta)\), \(\arccos(ac/\Delta)\), and \(\arccos(bc/\Delta)\); the octant-axis contributions sum to \(s/2\). The remaining terms are exactly \(-\pi^{-1}\sum_{i<j}\sqrt{a_i^2+a_j^2}\arccos(a_ia_j/\Delta)\). Thus the expression for \(T\) is the required spherical expectation. No approximation is involved.

**3. Evaluation of each dominance defect.** The positive octant where \(x u_1>y u_2+z u_3\) is a spherical triangle with vertices
\[
 e_1,\qquad\frac{(y,x,0)}{\sqrt{x^2+y^2}},\qquad
 \frac{(z,0,x)}{\sqrt{x^2+z^2}}.
\]
Integrating \(x u_1-y u_2-z u_3\) on this triangle with the same vector-area identity gives the exact formula
\(\mathbb E(x|U_1|-y|U_2|-z|U_3|)_+=D(x;y,z)\), including its two arctangent terms.

**4. Reduction of the hexagon expectation.** At most one of the three numbers \(2A-S\), \(2B-S\), \(2C-S\) is positive. Therefore, pointwise,
\[
 (S-2M)_+=S-2M+(2A-S)_++(2B-S)_++(2C-S)_+.
\]
The exact inclusion-exclusion identity for three numbers is
\(M=S-\min(A,B)-\min(A,C)-\min(B,C)+\min(A,B,C)\).
A two-dimensional polar integral in the \((u_i,u_j)\)-coordinate plane yields
\[
 \mathbb E\min(x|U_i|,y|U_j|)=\frac{x+y-\sqrt{x^2+y^2}}2.
\]
Insert these pair expectations, the formula for \(T\), and the three evaluated positive parts \(D\). Collecting terms yields \(\mathbb E(S-2M)_+=Q(a,b,c)\), proving the entire distribution.

**5. Quadratic extinction under flattening.** Fix \(a,b>0\) and let \(c\downarrow0\). Write \(X=a|U_1|\), \(Y=b|U_2|\), \(Z=|U_3|\), \(f=X-Y\). Except on the region \(X,Y\le cZ\), the identity
\[
 (X+Y+cZ-2\max\{X,Y,cZ\})_+=(cZ-|f|)_+
\]
holds. The exceptional region occupies spherical area \(O_{a,b}(c^2)\) and both expressions are \(O(c)\), so it contributes \(O_{a,b}(c^3)\) to the expected difference. The coarea formula near the smooth level curves \(f=0\), together with the triangular kernel \((cZ-|f|)_+\), gives
\[
 \lim_{c\downarrow0}\frac{Q(a,b,c)}{c^2}
 =\frac1{4\pi}\int_{f=0}\frac{U_3^2}{|\nabla_{S^2}f|}\,ds.
\]
On each open octant the level curve is parametrized by \(U=(\pm b\sin\theta/R,\pm a\sin\theta/R,\pm\cos\theta)\), with \(R=\sqrt{a^2+b^2}\), \(0<\theta<\pi/2\), and \(|\nabla_{S^2}f|=R\). There are eight octant arcs, and \(\int_0^{\pi/2}\cos^2\theta\,d\theta=\pi/4\). Hence \(Q/c^2\to(8/(4\pi R))(\pi/4)=1/(2R)\). Dividing \(2Q\) by \(a+b+c\) gives the asserted coefficient. Endpoint singularities are harmless: removing spherical caps of radius \(\varepsilon\), applying smooth coarea on the remainder, and then letting \(\varepsilon\downarrow0\) bounds omitted terms by their vanishing area. This completes the proof.

## Verification
The standalone `checker.py` contains an independent edge-crossing algorithm: for each sampled affine plane it tests all twelve box edges and counts their intersected interiors, rather than evaluating the fixed-normal type-length formulas. For five distinct sets of positive half-lengths it samples 250,000 normals each, with offsets uniform on the corresponding intersecting interval; it uses the requisite width weights in averaging. Every observed type distribution agrees with the analytical formula within the stated sampling tolerances. It also checks normalization, the exact expected vertex count four, and the classical cube special case. An additional high-precision evaluation of the elementary formula for \((a,b)=(1,1),(0.7,1.5),(3,2)\) and \(c\in\{0.1,0.01,0.001,0.0001\}\) shows the ratios \(p_6/c^2\) converging to the exact coefficient. These finite checks are corroboration; the proof above establishes exactness for all parameters.

## Relationship to prior work
Bray (2009, Chapter 10) tabulated the complete motion-invariant affine section-type probabilities for the **cube**; those cube constants are prior work. The already documented all-rectangular-box triangular section probability in terms of \(\mathbb E\min(A,B,C)\), together with its cubic extremizer and stability, is also prior work. The present finding does **not** claim discovery of those facts or of the known mean-four identity. Its distinct claims are the elementary, all-aspect-ratio, four-type law involving the new general-box hexagon integral \(Q\), and the sharp flattening coefficient. The 2026 combinatorial slicing literature analyzes possible polytope section types and reconstruction rather than the unequal-box motion-invariant type probabilities. Haar-random *central* sections are a different probability model; replacing conditional offsets by zero changes the probabilities and cannot imply the present law.

## Limitations
This is a theorem about all Euclidean **rectangular** boxes, not general affinely sheared parallelepipeds. It uses the invariant affine-plane measure conditioned on hitting the box; uniform normal/independently uniform conditional offset defines another measure. The theorem does not assert a new cube value, nor does it characterize shape extremizers of the six-sided probability over all three aspect ratios. The result has no independent external audit, and equivalent earlier treatments under different integral notation may exist.

## References
- D. Birkemeyer, P. Brose, M.-C. Brandenburg, and S. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195, first public 2026-09-14. https://arxiv.org/abs/2609.16195
- B. M. Bray, *Invariant measures on multifids of convex polytopes*, University of Wollongong, Ph.D. thesis, 2009, Chapter 10. https://ro.uow.edu.au/theses/3403
- M.-C. Brandenburg and C. Meroni, *Combinatorics of slices of cubes*, arXiv:2510.09265, first public 2025-10-10. https://arxiv.org/abs/2510.09265
