# Sharp radius-ratio profile at fixed edge-square anisotropy for disphenoids
## Finding
Let a nondegenerate disphenoid have opposite edge pairs of lengths \(\ell,\ell\), \(m,m\), and \(n,n\), circumradius \(R\), and inradius \(r\). Define the scale-free edge-square anisotropy
\[
q=\frac{2\big((\ell^2-m^2)^2+(m^2-n^2)^2+(n^2-\ell^2)^2\big)}{(\ell^2+m^2+n^2)^2}.
\]
Then \(0\le q<1\). For \(0\le q<1/4\),
\[
\frac{1-3q-2q^{3/2}}{9(1-q)}
\le \left(\frac rR\right)^2
\le
\frac{1-3q+2q^{3/2}}{9(1-q)}.
\]
Both endpoints are attained. For \(1/4\le q<1\),
\[
0<\left(\frac rR\right)^2
\le
\frac{1-3q+2q^{3/2}}{9(1-q)},
\]
and the lower endpoint \(0\) is a sharp but unattained infimum. Every value between the sharp bounds occurs.

The upper endpoint is attained exactly, up to relabeling, by the two-equal branch with normalized coordinate squares
\[
\left(\frac{1+2\sqrt q}3,\frac{1-\sqrt q}3,\frac{1-\sqrt q}3\right).
\]
When \(q<1/4\), the lower endpoint is attained exactly by the other two-equal branch
\[
\left(\frac{1-2\sqrt q}3,\frac{1+\sqrt q}3,\frac{1+\sqrt q}3\right).
\]
Thus \(q=1/4\) is the precise transition where fixed anisotropy ceases to force a positive lower radius ratio.

## Assumptions and scope
A disphenoid is a nondegenerate Euclidean tetrahedron whose opposite edges are equal in pairs; equivalently, all four faces are congruent acute triangles. The quantities \(R\) and \(r\) are the ordinary circumradius and inradius. The result concerns only this class and makes no claim for arbitrary tetrahedra.

A standard orthogonal-coordinate model is
\[
A=(x,y,z),\quad B=(x,-y,-z),\quad C=(-x,y,-z),\quad D=(-x,-y,z),
\]
with \(x,y,z>0\). Put \(a=x^2\), \(b=y^2\), \(c=z^2\), and \(S=a+b+c\).

## Proof
In the coordinate model,
\[
R^2=S.
\]
The face through \(A,B,C\) has equation \(X/x+Y/y-Z/z=1\), so its distance from the origin is
\[
r=\frac{xyz}{\sqrt{x^2y^2+y^2z^2+z^2x^2}}.
\]
Writing \(P=ab+bc+ca\), this gives
\[
\left(\frac rR\right)^2=\frac{abc}{SP}.
\]
The three edge-pair lengths satisfy
\[
\ell^2=4(b+c),\qquad m^2=4(a+c),\qquad n^2=4(a+b).
\]
Consequently the stated geometric anisotropy equals
\[
q=\frac{(a-b)^2+(b-c)^2+(c-a)^2}{2S^2}
=1-\frac{3P}{S^2}.
\]
In particular \(0\le q<1\), because \(a,b,c>0\).

Normalize by \(S\), writing \(p_1=a/S\), \(p_2=b/S\), \(p_3=c/S\), so \(p_1+p_2+p_3=1\). Put \(s=\sqrt q\). The intersection of the plane \(p_1+p_2+p_3=1\) with the sphere determined by fixed \(q\) is parameterized by
\[
p_k=\frac{1+2s\cos(\theta+2\pi(k-1)/3)}3,\qquad k=1,2,3.
\]
Every positive triple with the fixed value of \(q\) occurs in this parameterization. Direct multiplication gives
\[
p_1p_2p_3=\frac{1-3s^2+2s^3\cos(3\theta)}{27},
\qquad
p_1p_2+p_2p_3+p_3p_1=\frac{1-s^2}3.
\]
Hence
\[
\left(\frac rR\right)^2
=\frac{1-3q+2q^{3/2}\cos(3\theta)}{9(1-q)}.
\]

If \(s<1/2\), all three coordinates \(p_k\) stay positive for every \(\theta\), so \(\cos(3\theta)\) runs through the full interval \([-1,1]\). This yields both displayed endpoints, with equality exactly at the two two-equal branches above, modulo permutation.

If \(s\ge1/2\), positivity cuts each angular chamber before \(\cos(3\theta)\) reaches \(-1\). On a chamber containing the upper branch, the product \(p_1p_2p_3\) is continuous, has its maximum at \(\cos(3\theta)=1\), and tends to \(0\) at the chamber boundary where one \(p_k\) tends to zero. Thus the attainable range is exactly the stated half-open interval. Continuity also gives every intermediate value. At \(s=1/2\), the lower two-equal branch itself has one zero coordinate, explaining the transition \(q=1/4\).

## Verification
The accompanying `verify_profile.py` independently reconstructs the coordinate geometry, compares the plane-distance inradius with \(3V/A_{\mathrm{surface}}\), checks the edge definition of \(q\), checks the trigonometric parameterization, tests both equality branches, and samples the claimed profile. It reports `VERIFY_OK` over 157750 deterministic checks. The largest recorded relative inradius-formula error was \(4.441\times10^{-16}\), the largest edge-anisotropy discrepancy was \(9.992\times10^{-16}\), the largest parameterization discrepancy was \(4.829\times10^{-16}\), and the largest sampled profile violation was zero. These computations are checks of the algebra and implementation; the infinite statement is proved above.

## Relationship to prior work
Hajja and Walker give the standard equifacial characterization, prove coincidence of the circumcenter, incenter, and centroid, and derive \(R^2=(\ell^2+m^2+n^2)/8\) for a disphenoid. Their inspected full text does not state a fixed-anisotropy range for \(r/R\), and a text search of that source did not locate an inradius formula beyond the center discussion.

Hajja's 2007 paper develops a symmetric-optimization method for acute face angles and applies it to the solid-angle sum of equifacial tetrahedra. Its inspected statement and method do not give the conditional radius-ratio profile here. The closest published-results database hit found in the overlap search concerns normalized Ptolemy slacks of arbitrary tetrahedra at fixed \(R,V,L\); its invariants and conclusion differ and do not imply a sharp range at fixed edge-square anisotropy.

Two older items remain access risks: Leech's 1950 paper on isosceles tetrahedra and Scott's 2006 one-page note titled “An inequality associated with the equifacial tetrahedron.” Public metadata and available excerpts were checked, but full text could not be read in this run. No claim is made that negative search results prove absolute novelty.

## Limitations
The result is restricted to nondegenerate disphenoids. At \(q\ge1/4\), the lower value zero belongs only to the degenerate closure and is not attained by a tetrahedron of positive volume. The originality conclusion is limited by the inaccessible historical items named above and by the usual possibility of an equivalent formula under older terminology such as isosceles, equifacial, bisphenoid, or isotetrahedron.

## References
1. M. Hajja and P. Walker, “Equifacial tetrahedra,” *International Journal of Mathematical Education in Science and Technology* 32 (2001), 501–508. DOI: 10.1080/00207390110038231. Author-uploaded full text publicly dated 2016-08-31.
2. M. Hajja, “A method for establishing certain trigonometric inequalities,” *JIPAM* 8 (2007), Article 29. EuDML record 128563.
3. J. Leech, “Some Properties of the Isosceles Tetrahedron,” *The Mathematical Gazette* 34 (1950), 269–271. DOI: 10.2307/3611029.
4. J. A. Scott, “90.53 An inequality associated with the equifacial tetrahedron,” *The Mathematical Gazette* 90 (2006), 320. DOI: 10.1017/S0025557200179872.
