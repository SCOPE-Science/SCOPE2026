# Arbitrarily large least quasiperiods for lattice-diameter segments of primitive-edged parallelograms

## Finding
For every integer \(m\ge 2\), define the full-dimensional lattice parallelogram
\[
P_m=\operatorname{conv}\{(0,0),(1,m),(m+2,1),(m+3,m+1)\}.
\]
Both edge vectors are primitive. For every positive integer \(n\), let \(L_m(n)\) be the number of distinct maximal lattice-diameter segments of \(nP_m\), namely the maximal collinear lattice-point strings containing the largest number of lattice points among all lattice lines meeting \(nP_m\). The lattice diameter counts the number of unit lattice steps in such a string, rather than its number of points.

Write uniquely \(n=mp+t\) with integers \(p\ge0\) and \(0\le t<m\). Then the lattice diameter is
\[
\operatorname{diam}_{\mathbb Z}(nP_m)
=n(m+2)-\left\lceil\frac nm\right\rceil.
\]
Every maximizing segment is horizontal. Its supporting line has integer height \(y\) characterized **exactly** by \(n\le y\le mn\), together with
\[
 y\equiv0\pmod m\quad\text{if }t=0,
 \qquad y\bmod m\in\{0,t,t+1,\ldots,m-1\}\quad\text{if }1\le t<m.
\]
Consequently the complete all-dilation count is
\[
\boxed{
L_m(n)=
\begin{cases}
 n-p+1,&t=0,\\
 (m-t+1)(n-p),&1\le t<m.
\end{cases}}
\]
This is a quasipolynomial already for every \(n\ge1\), not merely eventually. Its **least eventual quasiperiod is exactly \(m\)**. The \(m\) residue-class slopes are pairwise distinct and form the exact spectrum
\[
\left\{\frac{(m-1)j}{m}:1\le j\le m\right\}.
\]
In particular, the largest to smallest slope ratio equals \(m\). Thus both least quasiperiod and relative growth-rate oscillation are unbounded among four-vertex, centrally symmetric lattice polygons with only primitive edges.

## Assumptions and scope
The ambient lattice is \(\mathbb Z^2\), and \(m,n\) are arbitrary integers with \(m\ge2\), \(n\ge1\). A primitive direction \(w\in\mathbb Z^2\) has coordinate gcd one. A lattice diameter segment is an unordered pair of extreme integer points on a lattice line whose intervening line segment contains the greatest possible number of lattice steps. There is at most one such extreme segment on each maximizing lattice line. We count distinct segments, not orientations or all subsegments.

## Proof
Set \(u=(1,m)\), \(v=(m+2,1)\), and \(\Delta=m(m+2)-1>0\). Their determinant has absolute value \(\Delta\). Write any primitive lattice direction as \(w=(a,b)\). In the basis \((u,v)\), its coefficients are
\[
\alpha=\frac{(m+2)b-a}{\Delta},\qquad
\beta=\frac{ma-b}{\Delta}.
\]
Every chord of \(nP_m\) parallel to \(w\) has length at most \(n/\max(|\alpha|,|\beta|)\) in primitive lattice steps, because the two parallelogram coordinates independently range through intervals of length \(n\). This bound applies in particular to every lattice segment.

If \(b\ne0\), put \(A=(m+2)b-a\) and \(B=ma-b\). The identity \(mA+B=\Delta b\) shows that \(\max(|A|,|B|)\ge m+1\): otherwise \(|\Delta b|\le m^2+m<\Delta\), impossible for nonzero integer \(b\). Thus every nonhorizontal primitive direction admits at most \(\lfloor n\Delta/(m+1)\rfloor\) lattice steps. For a primitive horizontal direction, necessarily \(w=\pm(1,0)\), giving maximal continuous chord length \(n\Delta/m\). Since
\[
\frac{n\Delta}{m}-\frac{n\Delta}{m+1}
=\frac{n\Delta}{m(m+1)}>1,
\]
no nonhorizontal direction can tie a horizontal lattice segment of length \(\lfloor n\Delta/m\rfloor\), provided the latter exists. It does exist by the middle-strip calculation below.

The horizontal sections of \(nP_m\) have three vertical regimes. On the middle strip \(n\le y\le mn\), their endpoints are exactly
\[
x_{\rm left}=\frac ym,\qquad
x_{\rm right}=n(m+2)+\frac{y-n}{m}.
\]
The real chord length is constant \(W=n\Delta/m\). On either outer strip, the real chord length is at most \((n-1)\Delta/m\) for every integer height, strictly smaller than \(\lfloor W\rfloor\) because \(\Delta/m=m+2-1/m>1\). Therefore no outer line can maximize the lattice diameter.

At an integer middle height, write \(s=y\bmod m\in\{0,\ldots,m-1\}\) and \(n=mp+t\). The number of lattice steps between the leftmost and rightmost integer points of that section is
\[
\begin{aligned}
\ell(y)&=\left\lfloor n(m+2)+\frac{y-n}{m}\right\rfloor
-\left\lceil\frac ym\right\rceil\\
&=n(m+2)-p-\mathbf1_{s<t}-\mathbf1_{s>0}.
\end{aligned}
\]
If \(t=0\), the maximum is \(n(m+2)-p=\lfloor W\rfloor\), attained precisely at \(s=0\). If \(1\le t<m\), it is \(n(m+2)-p-1=\lfloor W\rfloor\), attained precisely when \(s=0\) or \(s\ge t\). This also proves the claimed global diameter and complete supporting-line classification.

Counting integer heights in the closed strip gives \(n-p+1\) for \(t=0\). For \(1\le t<m\), there are \(n-p\) heights in each of the \(m-t+1\) admissible residue classes. This proves the count formula.

For \(t=0\) its slope as a linear function of \(n\) is \((m-1)/m\); for \(1\le t<m\) the slope is \((m-1)(m-t+1)/m\). These \(m\) slopes are pairwise distinct. If an eventual quasipolynomial period \(q\) were not divisible by \(m\), a single residue modulo \(q\) would contain infinitely many integers of at least two different residues modulo \(m\); it could not have a single linear polynomial agreeing with the two distinct slopes. Thus every eventual quasiperiod is divisible by \(m\), and the displayed period \(m\) is least. Its largest/smallest slope ratio is \(m\).

## Verification
A standalone standard-library Python checker, `checker.py`, independently enumerates every lattice point of \(nP_m\), every unordered pair, and each pair's coordinate gcd. It reconstructs all maximal segment-supporting lines without using the analytic formulas. It checks the exact lattice diameter, count, and uniqueness of the horizontal direction for all 42 combinations \(2\le m\le8\), \(1\le n\le6\). The program prints `LATTICE_PERIOD_CHECK_OK cases=42` on success. These finite checks corroborate, but do not replace, the proof for arbitrary \(m,n\).

The specialization \(m=3\) reproduces the three linear branches in Example 4.7 of the cited paper, providing an additional published consistency check.

## Relationship to prior work
Averkov, Brose, De Loera, Lopez-Campos and Torres prove eventual quasipolynomial counting of lattice diameter segments of lattice polytopes (Theorem 4.6) and explicitly compute a single parallelogram corresponding exactly to \(m=3\) here (Example 4.7). That special case and the general eventual-quasipolynomial theorem are **not** claimed to be new. The new quantified statement is that **every prescribed positive least quasiperiod of size at least two** occurs with four primitive edges, with the complete all-dilation count, all maximizing lines and an exact \(m\)-fold range of residue-class slopes. The single known \(m=3\) case does not establish these unboundedness and spectrum statements.

Soprunov and Soprunova prove eventual quasi-linearity of Minkowski length and its one-dimensional specialization (lattice diameter), which concerns the maximum *length*, rather than the *number of different maximum-length lines*. It does not imply the claimed quasiperiod or counting spectrum.

## Limitations
The construction shows existence, not a classification of all polygonal quasiperiods or any optimal bound in terms of coordinate magnitudes. It does not characterize the least period for arbitrary lattice polygons. The \(m=3\) specialization is explicitly present in prior work. Novelty of the arbitrary-\(m\) spectrum is supported by the inspected sources and searches, not an exhaustive guarantee about inaccessible or unindexed literature. Independent mathematical validation has not been performed.

## References
1. G. Averkov, A. E. Brose, J. A. De Loera, G. Lopez-Campos, and A. J. Torres, *On Lattice Diameter Segments: Algorithms and Structure*, arXiv:2508.20009v2 (2026 revision), especially Section 4, Theorem 4.6 and Example 4.7; first public version arXiv:2508.20009v1 (27 August 2025). https://arxiv.org/abs/2508.20009
2. I. Soprunov and J. Soprunova, *Eventual quasi-linearity of the Minkowski length*, arXiv:1412.4404v2, European Journal of Combinatorics 58 (2016), 107–117. https://arxiv.org/abs/1412.4404
