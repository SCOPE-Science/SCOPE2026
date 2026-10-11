# Exact Ptolemy constant of the Day--James \(\ell_p-\ell_\infty\) family above two
## Finding
For every real \(2<p<\infty\), let \(X_p\) be the Day--James plane on \(\mathbb R^2\) with
\[
\|(x,y)\|_{X_p}=
\begin{cases}
\bigl(|x|^p+|y|^p\bigr)^{1/p},&xy\ge0,\\
\max\{|x|,|y|\},&xy\le0.
\end{cases}
\]
Then its Ptolemy constant is exactly
\[
C_{\mathrm{Pt}}(X_p)=1+2^{-2/p}.
\]
Since the published James constant of this family is \(J(X_p)=1+2^{-1/p}\), one has the exact identity
\[
C_{\mathrm{Pt}}(X_p)=1+\bigl(J(X_p)-1\bigr)^2.
\]

The value interpolates strictly from \(3/2\) as \(p\downarrow2\) toward \(2\) as \(p\to\infty\).

## Assumptions and scope
The scalar field is real, the dimension is exactly two, and \(2<p<\infty\). The Ptolemy constant is
\[
C_{\mathrm{Pt}}(X)=
\sup_{x,y,z\in X\setminus\{0\},\;x,y,z\ \mathrm{pairwise\ distinct}}
\frac{\|x-y\|\,\|z\|}
{\|x-z\|\,\|y\|+\|z-y\|\,\|x\|}.
\]
The theorem concerns the classical Day--James \(\ell_p-\ell_\infty\) plane.

## Proof
Put
\[
\tau=2^{-2/p},\qquad U=x+y,\qquad V=x-y,
\]
and define the Hilbert norm
\[
H_\tau(x,y)^2=U^2+\tau V^2.
\]
Because \(p>2\), one has \(1/2<\tau<1\).

On the sector \(xy\ge0\), equivalently \(|U|\ge|V|\), put
\[
r=\frac{|V|}{|U|}\in[0,1].
\]
Then
\[
R_p(r):=\frac{H_\tau(x,y)^2}{\|(x,y)\|_{X_p}^2}
=
\frac{4(1+\tau r^2)}
{\bigl((1+r)^p+(1-r)^p\bigr)^{2/p}}.
\]
For \(a,b\ge0\) and \(p\ge2\),
\[
2^{1/p-1/2}\sqrt{a^2+b^2}
\le
(a^p+b^p)^{1/p}
\le
\sqrt{a^2+b^2}.
\]
With \(a=1+r\), \(b=1-r\), and \(2^{2/p}=\tau^{-1}\), this gives
\[
1+\tau\le R_p(r)\le4\tau.
\]

On the sector \(xy\le0\), equivalently \(|V|\ge|U|\), put
\[
s=\frac{|U|}{|V|}\in[0,1].
\]
Here
\[
\|(x,y)\|_{X_p}=\frac{|U|+|V|}{2},
\]
so
\[
R_\infty(s):=
\frac{H_\tau(x,y)^2}{\|(x,y)\|_{X_p}^2}
=
\frac{4(s^2+\tau)}{(1+s)^2}.
\]
Differentiation gives
\[
R_\infty'(s)=\frac{8(s-\tau)}{(1+s)^3}.
\]
Hence
\[
m:=\min R_\infty=\frac{4\tau}{1+\tau}
\]
at \(s=\tau\), while
\[
M:=\max R_\infty=4\tau.
\]
Also
\[
1+\tau-\frac{4\tau}{1+\tau}
=
\frac{(1-\tau)^2}{1+\tau}>0,
\]
so the same-sign sector lies between the same global extrema. Therefore
\[
\sqrt m\,\|w\|_{X_p}\le H_\tau(w)\le\sqrt M\,\|w\|_{X_p}
\qquad(w\in\mathbb R^2).
\]

The Hilbert norm \(H_\tau\) satisfies the Ptolemy inequality. The preceding two-sided comparison therefore yields
\[
C_{\mathrm{Pt}}(X_p)\le\frac{M}{m}=1+\tau.
\]

For the reverse inequality, choose
\[
x=(-\tau,-\tau),\qquad
y=(1,-1),\qquad
z=x+y=(1-\tau,-1-\tau).
\]
Then
\[
\|x\|_{X_p}=\sqrt\tau,\quad
\|y\|_{X_p}=1,\quad
\|z\|_{X_p}=1+\tau,
\]
and
\[
\|x-y\|_{X_p}=1+\tau,\quad
\|x-z\|_{X_p}=1,\quad
\|z-y\|_{X_p}=\sqrt\tau.
\]
Thus the Ptolemy ratio is
\[
\frac{(1+\tau)^2}{1+\tau}=1+\tau.
\]
Hence
\[
C_{\mathrm{Pt}}(X_p)=1+2^{-2/p}.
\]
Using the published identity
\[
J(X_p)=1+2^{-1/p}
\]
gives
\[
C_{\mathrm{Pt}}(X_p)=1+\bigl(J(X_p)-1\bigr)^2.
\]

## Verification
The proof covers both sign sectors and all directions. The same-sign estimate is a global sharp two-coordinate \(\ell_p/\ell_2\) comparison, while the opposite-sign sector has one explicitly solved critical point. No finite sample is used as an infinite proof.

For the extremizing triple, \(1/2<\tau<1\) places \(x\) in a same-sign quadrant and \(y,z,x-y\) in opposite-sign quadrants. The identity
\[
2^{1/p}\tau=\sqrt\tau
\]
follows directly from \(\tau=2^{-2/p}\), so all six displayed norms are exact.

## Relationship to prior work
Nilsrakoo and Saejung define the generalized Day--James construction and the classical \(\ell_p-\ell_\infty\) family. Their Corollary 3.8 gives
\[
J(\ell_p-\ell_\infty)=1+2^{-1/p}.
\]
The inspected material computes the James constant, not the Ptolemy constant of the full parameter family.

Zuo's 2012 paper proves exact Ptolemy formulas for absolute normalized norms under a midpoint extremality hypothesis. Normalize the present Day--James norm by
\[
a=2^{1/p-1}(x+y),\qquad b=\frac{x-y}{2}.
\]
The resulting norm is absolute and normalized, and \(H_\tau\) becomes a scalar multiple of the Euclidean norm. Its sharp norm-to-Euclidean comparison occurs at
\[
\frac{|a|}{|b|}=2^{-1/p},
\]
equivalently at
\[
t=\frac{1}{1+2^{-1/p}},
\]
which is not \(1/2\) for \(p>2\). Thus the midpoint exactness theorem does not imply this family formula.

A 2015 reconsideration advertises additional sufficient conditions for Ptolemy constants of absolute normalized norms, but only bibliographic metadata and an abstract-level description were readable in the bounded inspection. A 2018 treatment develops further comparison methods and concrete examples; the inspected material did not state the Day--James \(\ell_p-\ell_\infty\) formula.

## Limitations
The theorem is restricted to \(2<p<\infty\). The endpoint \(p=2\) has the limiting value \(3/2\), while \(p=\infty\) is only a limiting statement here. No formula is asserted for \(1\le p<2\) or for general Day--James \(\ell_p-\ell_q\) planes.

The literature search cannot exclude an older equivalent calculation under different terminology. In particular, the 2015 reconsideration remains a bibliographic coverage risk because a readable full text was not obtained in the bounded source inspection.

## References
1. W. Nilsrakoo and S. Saejung, “The James constant of normalized norms on \(\mathbb R^2\),” *Journal of Inequalities and Applications* 2006, Article ID 26265, DOI 10.1155/JIA/2006/26265; published 2006-05-04.
2. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” *Journal of Inequalities and Applications* 2012, Article 107, DOI 10.1186/1029-242X-2012-107; published 2012-05-17.
3. Z. Zuo, “A Reconsideration on the Ptolemy Constant of Absolute Normalized Norms,” *Acta Mathematica Sinica, Chinese Series* 58 (2015), 337--344, DOI 10.12386/A2015sxxb0033; published 2015-03-15.
4. Z. Zuo, “On the Ptolemy constant of some concrete Banach spaces,” *Mathematical Inequalities & Applications* 21 (2018), 945--956, DOI 10.7153/mia-2018-21-64.
