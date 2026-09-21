# A quantitative bracket for reciprocal polylogarithmic smoothing into the class \(\mathcal U\)

Let \(\mathbb D=\{z:|z|<1\}\), let \(\mathcal S\) be the normalized univalent class, and write
\[
\frac{z}{f(z)}=1+\sum_{n\ge1}b_n z^n,\qquad f\in\mathcal S.
\]
For real \(\sigma\), define the reciprocal polylogarithmic smoothing
\[
q_\sigma(z):=
1+\sum_{n\ge1}\frac{b_n}{(n+1)^\sigma}z^n
=
\frac{z}{f(z)} * \frac{\operatorname{Li}_\sigma(z)}{z}.
\]
Whenever \(q_\sigma\) is zero-free in \(\mathbb D\), put
\[
F_\sigma(z)=\frac{z}{q_\sigma(z)}.
\]
The class \(\mathcal U\) consists of normalized analytic functions \(F\) satisfying
\[
\left|U_F(z)\right|<1,\qquad
U_F(z):=F'(z)\left(\frac{z}{F(z)}\right)^2-1.
\]

Ali, Obradović and Ponnusamy proved in 2013 that \(F_\sigma\in\mathcal U\) for every \(f\in\mathcal S\) when \(\sigma\ge3/2\), and asked for the smallest universal parameter.

## Result

Define
\[
B(\sigma):=
\sum_{m=1}^\infty\frac{1}{m(m+2)^{2\sigma}},
\qquad
H(\sigma):=2^{1-\sigma}+\sqrt{B(\sigma)}.
\]
On \((0,\infty)\), \(H\) is continuous and strictly decreasing from \(+\infty\) to \(0\). Let \(\sigma_*\) be the unique solution of
\[
H(\sigma_*)=1.
\]
Then
\[
1.413519<\sigma_*<1.413520,
\]
and for every \(f\in\mathcal S\),
\[
\boxed{\sigma\ge\sigma_*\quad\Longrightarrow\quad F_\sigma\in\mathcal U.}
\]

Conversely, no universal \(\mathcal U\)-threshold can be below \(1\): for every real \(\sigma<1\) there exists \(f\in\mathcal S\) for which \(F_\sigma\notin\mathcal U\). Thus if
\[
\sigma_{\mathcal U}:=
\inf\left\{s:\ F_\sigma[f]\in\mathcal U
\text{ for every }f\in\mathcal S\text{ and every }\sigma\ge s\right\},
\]
then
\[
\boxed{1\le \sigma_{\mathcal U}\le \sigma_*<1.413520.}
\]

This improves the published universal upper bound \(3/2\). It does not determine the exact value of \(\sigma_{\mathcal U}\), nor the corresponding optimal threshold for membership merely in \(\mathcal S\).

## Proof of the upper bound

The area theorem gives
\[
\sum_{n=2}^\infty (n-1)|b_n|^2\le1,
\]
and the Bieberbach bound gives
\[
|b_1|=|a_2|\le2.
\]

Fix \(r=|z|<1\). By Cauchy--Schwarz,
\[
\begin{aligned}
|q_\sigma(z)-1|
&\le \frac{|b_1|}{2^\sigma}r
+\sum_{n=2}^\infty\frac{|b_n|}{(n+1)^\sigma}r^n\\
&\le 2^{1-\sigma}r+
\left(
\sum_{n=2}^\infty
\frac{r^{2n}}{(n-1)(n+1)^{2\sigma}}
\right)^{1/2}.
\end{aligned}
\]
After \(m=n-1\), the second series at \(r=1\) is exactly \(B(\sigma)\).
Hence, if \(H(\sigma)\le1\), then for every \(r<1\),
\[
|q_\sigma(z)-1|<H(\sigma)\le1.
\]
Therefore \(q_\sigma\) is zero-free in \(\mathbb D\), so \(F_\sigma\) is analytic there.

Now
\[
U_{F_\sigma}(z)
=q_\sigma(z)-zq_\sigma'(z)-1
=
-\sum_{n=2}^\infty
\frac{(n-1)b_n}{(n+1)^\sigma}z^n.
\]
A second use of Cauchy--Schwarz yields
\[
|U_{F_\sigma}(z)|
\le
\left(
\sum_{n=2}^\infty
\frac{(n-1)r^{2n}}{(n+1)^{2\sigma}}
\right)^{1/2}.
\]
It is enough to bound this at \(r=1\). Since \(\sigma_*>7/5\), for every \(\sigma\ge\sigma_*\),
\[
\sum_{n=2}^\infty
\frac{n-1}{(n+1)^{2\sigma}}
<
\sum_{n=2}^\infty n^{-9/5}.
\]
The integral test gives
\[
\sum_{n=2}^\infty n^{-9/5}
\le
2^{-9/5}+3^{-9/5}+\int_3^\infty x^{-9/5}\,dx
=
2^{-9/5}+3^{-9/5}+\frac54\,3^{-4/5}
<0.945<1.
\]
Consequently \(|U_{F_\sigma}(z)|<1\) throughout \(\mathbb D\), proving
\(F_\sigma\in\mathcal U\).

The root location is easy to certify. At \(\sigma=7/5\), the first three
terms of \(B(\sigma)\) already give
\[
H(7/5)>1.003,
\]
whereas at \(\sigma=3/2\),
\[
B(3/2)=
\frac{17}{16}-\frac{\pi^2}{24}-\frac{\zeta(3)}2
\]
and \(H(3/2)<0.932\). Strict monotonicity therefore gives a unique root in
\((7/5,3/2)\). The reproducibility script certifies the narrower bracket
\(1.413519<\sigma_*<1.413520\) using a finite partial sum and an explicit
integral upper bound for the tail.

## Proof of the lower obstruction

Fix \(\sigma<1\). Choose
\[
0<\alpha<\min\{1,1-\sigma\}
\]
and consider
\[
f_\alpha(z)=\frac{z}{(1-z)^\alpha}.
\]
Since
\[
\operatorname{Re}\frac{z f_\alpha'(z)}{f_\alpha(z)}
=
\operatorname{Re}\left(1+\alpha\frac{z}{1-z}\right)
>1-\frac{\alpha}{2}>0,
\]
the function \(f_\alpha\) is starlike and hence belongs to \(\mathcal S\).

Its reciprocal factor is
\[
\frac{z}{f_\alpha(z)}
=(1-z)^\alpha
=1+\sum_{n\ge1}b_nz^n,
\]
where, for \(0<\alpha<1\),
\[
b_n
=-\frac{\alpha\,\Gamma(n-\alpha)}
{\Gamma(1-\alpha)\Gamma(n+1)}<0
\qquad(n\ge1).
\]
For \(0<r<1\),
\[
q_\sigma(r)-rq_\sigma'(r)-1
=
\sum_{n=2}^\infty
\frac{(n-1)|b_n|}{(n+1)^\sigma}r^n.
\]
Moreover,
\[
\frac{(n-1)|b_n|}{(n+1)^\sigma}
\sim
\frac{\alpha}{\Gamma(1-\alpha)}n^{-\alpha-\sigma}.
\]
Because \(\alpha+\sigma<1\), the boundary series diverges. By monotone
convergence the displayed quantity tends to \(+\infty\) as \(r\uparrow1\).
If \(q_\sigma\) has a zero in \(\mathbb D\), then \(F_\sigma\) is not even
analytic on the disk; otherwise the \(\mathcal U\)-inequality itself fails
for some \(r<1\). In either case \(F_\sigma\notin\mathcal U\).

## Context and originality

The 2013 paper states the transform above, proves the explicit bound
\(\sigma\ge3/2\), and ends with the problem of determining the smallest
parameter giving universal membership in \(\mathcal U\) or \(\mathcal S\).
The present result narrows the \(\mathcal U\) side to
\[
1\le\sigma_{\mathcal U}<1.413520.
\]

Targeted searches were made for the exact 2013 problem and DOI, the
\(F_\sigma\)/\(\operatorname{Li}_\sigma\) notation, reciprocal Hadamard
convolutions, polylogarithmic univalence operators, and later literature on
the class \(\mathcal U\). No source located in those searches states this
bracket, the defining equation for \(\sigma_*\), or the power-starlike
obstruction at every \(\sigma<1\).

The older polylogarithm literature of Ponnusamy--Sabapathy (1996) and the
convolution-transform paper of Obradović--Ponnusamy (2007) are the most
plausible sources of equivalent prior machinery. Their available
descriptions concern geometric properties of polylogarithms and transforms
of already restricted univalent classes; no statement located there
resolves the 2013 universal smoothing problem. Full theorem-by-theorem text
of the 1996 paper was not available in the inspected sources, so equivalent
coverage there remains a residual originality risk. Originality is therefore
claimed only to the best of our knowledge.

## Limitations

- The exact universal threshold \(\sigma_{\mathcal U}\) remains open inside
  \([1,\sigma_*]\).
- The argument gives no lower obstruction for universal membership in
  \(\mathcal S\); failure of the stronger class \(\mathcal U\) does not imply
  failure of univalence.
- The upper bound uses only Bieberbach plus the area theorem. Sharper coupled
  information about reciprocal coefficients could lower \(\sigma_*\).
- The numerical bracket for \(\sigma_*\) is auxiliary; the theorem is stated
  intrinsically by \(H(\sigma_*)=1\).
- Originality is to the best of our knowledge, with the 1996 polylogarithm
  paper the principal incompletely inspected literature risk.

## Reproducibility

`artifacts/verify_threshold.py` checks the numerical root bracket using
100,000 terms and a rigorous elementary tail majorant, and checks the
elementary \(9/5\)-series majorant used in the proof.

## References

1. R. M. Ali, M. Obradović and S. Ponnusamy, *Necessary and sufficient
   conditions for univalent functions*, Complex Variables and Elliptic
   Equations 58 (2013), 611--620.
   DOI: https://doi.org/10.1080/17476933.2011.599116
2. S. Ponnusamy and S. Sabapathy, *Polylogarithms in the theory of univalent
   functions*, Results in Mathematics 30 (1996), 136--150.
   DOI: https://doi.org/10.1007/BF03322186
3. M. Obradović and S. Ponnusamy, *Univalence and starlikeness of certain
   transforms defined by convolution of analytic functions*, J. Math. Anal.
   Appl. 336 (2007), 758--767.
   DOI: https://doi.org/10.1016/j.jmaa.2007.03.020
4. S. B. Joshi, H. Pawar and D. Srivastava, *On a certain subclass of
   analytic functions involving integral operator defined by polylogarithm
   function*, Mathematics 7 (2019), 66.
   DOI: https://doi.org/10.3390/math7010066
