# Exact Ptolemy constant of the Day--James \(\ell_2-\ell_\infty\) plane
## Finding
For the real Day--James plane \(X=\ell_2-\ell_\infty\), with \(\|(u,v)\|_{2,\infty}=\sqrt{u^2+v^2}\) when \(uv\ge0\) and \(\|(u,v)\|_{2,\infty}=\max\{|u|,|v|\}\) when \(uv\le0\), the Ptolemy constant is exactly \(C_{\mathrm{Pt}}(X)=3/2\).

Here
\[
C_{\mathrm{Pt}}(X)=
\sup_{x,y,z\in X\setminus\{0\},\;x,y,z\ \mathrm{pairwise\ distinct}}
\frac{\|x-y\|\,\|z\|}{\|x-z\|\,\|y\|+\|z-y\|\,\|x\|}.
\]

## Assumptions and scope
The scalar field is real. The norm is the \(p=2,q=\infty\) Day--James norm used in the literature on the Dunkl--Williams constant. On the coordinate axes the two branch formulas agree, so the displayed definition is unambiguous. The claim concerns this two-dimensional space only.

## Proof
Define a Hilbert norm
\[
H(u,v)=\frac12\sqrt{3u^2+2uv+3v^2}.
\]
We first prove the sharp pointwise comparison
\[
H(w)\le \|w\|_{2,\infty}\le \sqrt{\frac32}\,H(w)
\qquad (w\in\mathbb R^2).
\]

If \(w=(u,v)\) has \(uv\ge0\), then \(\|w\|_{2,\infty}^2=u^2+v^2\), and
\[
\|w\|_{2,\infty}^2-H(w)^2
=\frac{(u-v)^2}4\ge0,
\]
while
\[
\frac32H(w)^2-\|w\|_{2,\infty}^2
=\frac{u^2+6uv+v^2}8\ge0.
\]

If \(uv\le0\), put \(a=|u|\), \(b=|v|\) and, by symmetry, assume \(a\ge b\). Then
\(\|w\|_{2,\infty}^2=a^2\) and
\[
H(w)^2=\frac{3a^2-2ab+3b^2}4.
\]
Hence
\[
\|w\|_{2,\infty}^2-H(w)^2
=\frac{(a-b)(a+3b)}4\ge0
\]
and
\[
\frac32H(w)^2-\|w\|_{2,\infty}^2
=\frac{(a-3b)^2}8\ge0.
\]
This proves the comparison.

Now let \(x,y,z\) be admissible in the definition of \(C_{\mathrm{Pt}}(X)\). Since \(H\) is induced by an inner product, its Ptolemy constant is \(1\). Therefore
\[
\begin{aligned}
\|x-y\|_{2,\infty}\|z\|_{2,\infty}
&\le \frac32 H(x-y)H(z)\\
&\le \frac32\bigl(H(x-z)H(y)+H(z-y)H(x)\bigr)\\
&\le \frac32\bigl(
\|x-z\|_{2,\infty}\|y\|_{2,\infty}
+\|z-y\|_{2,\infty}\|x\|_{2,\infty}
\bigr).
\end{aligned}
\]
Thus \(C_{\mathrm{Pt}}(X)\le3/2\).

For the reverse inequality, take
\[
x=(-1,-1),\qquad y=(2,-2),\qquad z=(1,-3).
\]
Then
\[
\|x-y\|_{2,\infty}=3,\qquad
\|z\|_{2,\infty}=3,
\]
and
\[
\|x-z\|_{2,\infty}=2,\quad
\|y\|_{2,\infty}=2,\quad
\|z-y\|_{2,\infty}=\sqrt2,\quad
\|x\|_{2,\infty}=\sqrt2.
\]
Consequently the Ptolemy ratio is
\[
\frac{9}{4+2}=\frac32.
\]
The upper and lower bounds coincide.

## Verification
Every inequality in the proof is an exact polynomial identity or the Ptolemy inequality in a Hilbert norm. The matrix defining \(H^2\) is positive definite, with eigenvalues \(1\) and \(1/2\), so \(H\) is indeed a Hilbert norm. The lower-bound triple consists of three distinct nonzero vectors, and its six required norms are evaluated directly. No finite search or numerical approximation is used as proof.

## Relationship to prior work
Mizuguchi, Saito, and Tanaka (2013) define the same Day--James space and compute its Dunkl--Williams constant. The inspected full text contains no Ptolemy computation.

Zuo (2012) gives general comparison formulas for Ptolemy constants of absolute normalized norms. Under the linear change of variables
\[
s=\frac{u+v}{\sqrt2},\qquad b=\frac{u-v}2,
\]
the present norm becomes the absolute normalized norm
\[
N'(s,b)=
\begin{cases}
\sqrt{s^2+2b^2},& |s|\ge\sqrt2|b|,\\
|b|+|s|/\sqrt2,& |s|\le\sqrt2|b|.
\end{cases}
\]
Its associated function is
\[
\psi(t)=
\begin{cases}
\sqrt{(1-t)^2+2t^2},&0\le t\le\sqrt2-1,\\
t+(1-t)/\sqrt2,&\sqrt2-1\le t\le1.
\end{cases}
\]
For the Euclidean comparison function
\(\psi_2(t)=\sqrt{(1-t)^2+t^2}\), the ratio \(\psi/\psi_2\) is not maximized at \(t=1/2\): its maximum is \(\sqrt{3/2}\) at \(t=2-\sqrt2\). Thus the midpoint exact-value hypothesis in Zuo (2012) does not establish the present equality; its comparison estimate gives only the matching upper bound.

Zuo (2018) develops later comparison theorems, including off-midpoint results under symmetry assumptions on the associated function. The function above is not symmetric about \(t=1/2\), so those inspected hypotheses do not directly imply the claim. A 2015 reconsideration by Zuo advertises additional sufficient conditions, but a readable full text could not be obtained after bounded open-access and institutional retrieval attempts; that source remains an explicit originality risk rather than evidence of noncoverage.

## Limitations
The theorem is only for the real two-dimensional Day--James space \(\ell_2-\ell_\infty\). The proof establishes the exact mathematical value independently of the literature search. The originality comparison remains subject to the stated access risk for the 2015 paper and to the possibility of an older equivalent result indexed under different terminology.

## References
1. H. Mizuguchi, K.-S. Saito, and R. Tanaka, “On the calculation of the Dunkl--Williams constant of normed linear spaces,” Open Mathematics 11 (2013), 1212--1227. DOI: 10.2478/s11533-013-0238-4.
2. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” Journal of Inequalities and Applications 2012, 107 (2012). DOI: 10.1186/1029-242X-2012-107.
3. Z. Zuo, “A Reconsideration on the Ptolemy Constant of Absolute Normalized Norms,” Acta Mathematica Sinica, Chinese Series 58 (2015), 337--344. DOI: 10.12386/A2015sxxb0033.
4. Z. Zuo, “On the Ptolemy constant of some concrete Banach spaces,” Mathematical Inequalities & Applications 21 (2018), 945--956. DOI: 10.7153/mia-2018-21-64.
