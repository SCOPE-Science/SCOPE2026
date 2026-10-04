# Sharpness of the \(\varepsilon/2\) right-additivity coefficient
## Finding
For every \(0<\varepsilon<1\), there is an explicit two-dimensional polyhedral Banach space and vectors satisfying every hypothesis of the restricted right-additivity theorem of Chmieliński--Khurana--Sain for which the smallest possible approximate Birkhoff--James parameter of the sum is exactly \(\varepsilon/2\). Consequently, the coefficient \(1/2\) in that theorem is universally sharp.

More precisely, put
\[
\delta=\frac{\varepsilon}{2-\varepsilon},\qquad
\|(a,b)\|_\delta=\max\left\{|a|,\frac{|b|+\delta|a|}{1+\delta}\right\},
\]
and define
\[
x=(0,1+\delta),\quad R_+=(1,\delta),\quad R_-=(-1,\delta),
\]
\[
s=\begin{cases}1/3,&0<\varepsilon\le 2/3,\\ \varepsilon/2,&2/3\le\varepsilon<1,\end{cases}
\qquad y_1=sR_+,
\qquad y_2=R_-.
\]
Then \(d(x)=\varepsilon\), \(x\perp_B y_1\), \(x\perp_B y_2\), and
\[
\min\{\|y_1\|_\delta,\|y_2\|_\delta\}=\left\|\frac{y_1+y_2}{2}\right\|_\delta.
\]
The least \(\alpha\in[0,1)\) such that \(x\perp_B^\alpha(y_1+y_2)\) is \(\varepsilon/2\).

## Assumptions and scope
The field is real. Approximate Birkhoff--James orthogonality is the notion used in the cited source: for nonzero \(x\),
\[
x\perp_B^\alpha y
\quad\Longleftrightarrow\quad
\text{there exists }h\in J(x)\text{ with }|h(y)|\le \alpha\|y\|,
\]
for \(0\le\alpha<1\). The smoothness diameter is \(d(x)=\operatorname{diam}J(x)\). The result proves sharpness of the universal coefficient in the source theorem; it does not classify all equality cases, and it makes no pointwise sharpness claim for every \(\varepsilon\in[1,2)\).

## Proof
The unit ball of \(\|\cdot\|_\delta\) is
\[
\operatorname{conv}\{(1,1),(0,1+\delta),(-1,1),(-1,-1),(0,-1-\delta),(1,-1)\},
\]
which is the hexagon used in Example 3.1 of the cited source. Since \(0<\varepsilon<1\), one has \(0<\delta<1\) and
\[
\frac{2\delta}{1+\delta}=\varepsilon.
\]
At \(x=(0,1+\delta)\), the two extreme norming functionals are
\[
f_+(a,b)=\frac{\delta a+b}{1+\delta},\qquad
f_-(a,b)=\frac{-\delta a+b}{1+\delta},
\]
and \(J(x)=\operatorname{conv}\{f_+,f_-\}\). Therefore
\[
d(x)=\|f_+-f_-\|=\frac{2\delta}{1+\delta}=\varepsilon.
\]
Moreover \(\|R_+\|_\delta=\|R_-\|_\delta=1\), and
\[
f_-(R_+)=0,\qquad f_+(R_-)=0.
\]
The standard support-functional characterization of Birkhoff--James orthogonality gives \(x\perp_B y_1\) and \(x\perp_B y_2\).

Write \(w=y_1+y_2\). Since \(0<s<1\),
\[
w=(s-1,\delta(s+1))
\]
and a direct evaluation of the norm gives
\[
\|w\|_\delta=\max\{1-s,\varepsilon\}.
\]
If \(0<\varepsilon\le2/3\), then \(s=1/3\) and \(\|w\|_\delta=2/3=2s\). If \(2/3\le\varepsilon<1\), then \(s=\varepsilon/2\) and \(1-\varepsilon/2\le\varepsilon\), so again \(\|w\|_\delta=\varepsilon=2s\). Hence
\[
\left\|\frac{w}{2}\right\|_\delta=s
=\min\{\|y_1\|_\delta,\|y_2\|_\delta\},
\]
so the side condition is saturated.

Finally,
\[
f_+(w)=s\varepsilon,\qquad f_-(w)=\varepsilon.
\]
Every \(h\in J(x)\) is a convex combination of \(f_+\) and \(f_-\), so \(h(w)\) ranges over the positive interval \([s\varepsilon,\varepsilon]\). Therefore
\[
\inf_{h\in J(x)}\frac{|h(w)|}{\|w\|_\delta}
=\frac{s\varepsilon}{2s}
=\frac{\varepsilon}{2}.
\]
By the cited characterization of approximate Birkhoff--James orthogonality, this infimum is exactly the least admissible parameter \(\alpha\). This proves the claim.

## Verification
The proof above is symbolic and covers the full continuum \(0<\varepsilon<1\). The accompanying exact-rational checker verifies the identities on rational sample values from both branches, including the transition \(\varepsilon=2/3\). These finite checks are only regression checks; they are not used as a proof of the quantified statement.

## Relationship to prior work
Chmieliński--Khurana--Sain prove that if \(x\) is \(\varepsilon\)-smooth, \(x\perp_B y_1\), \(x\perp_B y_2\), and
\[
\min\{\|y_1\|,\|y_2\|\}\le\left\|\frac{y_1+y_2}{2}\right\|,
\]
then \(x\perp_B^{\varepsilon/2}(y_1+y_2)\). Their Example 3.1 supplies the same hexagonal norm and two orthogonal directions, but its equal scaling makes their sum collinear with \(x\) and does not satisfy the later theorem's side condition. The present rescaling is chosen so that the side condition is met with equality while the functional estimate is also met with equality, proving optimality of the coefficient.

A later paper on additive operators approximately preserving Birkhoff--James orthogonality concerns preservation by mappings rather than right-additivity at an approximately smooth point and does not imply this sharpness statement.

## Limitations
Only \(0<\varepsilon<1\) is needed and proved for the explicit sharpness family. This is enough to rule out every smaller universal coefficient. No classification of all extremizers is claimed. Literature searches cannot exclude an obscure or unindexed independent occurrence of the same sharpness construction.

## References
1. J. Chmieliński, D. Khurana, D. Sain, *Approximate smoothness in normed linear spaces*, arXiv:2109.11884, first public version 2021-09-24; Banach Journal of Mathematical Analysis 17 (2023), article 41, doi:10.1007/s43037-023-00263-4. Relevant items: characterization (1.8), Example 3.1, Theorem 3.6.
2. J. Chmieliński, R. Stypka, *Additive operators approximately preserving Birkhoff--James orthogonality*, Aequationes Mathematicae 99 (2025), 2847--2854, doi:10.1007/s00010-025-01210-4.
