# Exact early section radii for higher Neil constraints

Let
\[
\mathcal N_m=\{f\in H^\infty(\mathbb D):f^{(j)}(0)=0,\ 1\le j\le m\}
=\mathbb C+z^{m+1}H^\infty(\mathbb D),
\qquad m\ge1,
\]
and write \(S_Nf(z)=\sum_{j=0}^N a_jz^j\).  Define \(R_N^{(m)}\) to be the largest
\(r\in[0,1]\) such that
\[
\|S_Nf(r\,\cdot)\|_\infty\le \|f\|_\infty
\]
for every \(f\in\mathcal N_m\).  For \(m=1\), Das--Sarkar recently determined the
optimal universal Fejér--Rogosinski radius of the Neil algebra and, in particular,
computed \(R_2^{(1)}\) and \(R_3^{(1)}\).

The higher-order constraint has an exact reduction to a classical Schur coefficient
functional for every section before the quadratic term in the Schwarz factor can
enter.

## The reduction theorem

Put \(d=m+1\), and for \(0\le k\le m\) define
\[
M_k(r)=\sup_{\|\phi\|_\infty\le1}\|S_k\phi(r\,\cdot)\|_\infty.
\]
Then
\[
\boxed{
R_{d+k}^{(m)}
=
\sup\{0\le r\le1:2r^dM_k(r)\le1\}.
}
\tag{1}
\]

Indeed, after normalizing \(\|f\|_\infty\le1\), let \(a=f(0)\) and
\[
h(z)=\frac{f(z)-a}{1-\overline a f(z)}.
\]
The vanishing derivatives imply that \(h\) has a zero of order at least \(d\), so
the generalized Schwarz lemma gives \(h(z)=z^d\phi(z)\) with
\(\|\phi\|_\infty\le1\).  Solving for \(f\),
\[
f(z)=\frac{a+h(z)}{1+\overline a\,h(z)}
=a+(1-|a|^2)\bigl(h-\overline a h^2+\cdots\bigr).
\]
Since \(k\le m=d-1\), one has \(2d>d+k\), and hence
\[
S_{d+k}f(z)=a+(1-|a|^2)z^dS_k\phi(z).
\tag{2}
\]
Writing \(A=|a|\) and \(B=r^dM_k(r)\), (2) gives
\[
\|S_{d+k}f(r\,\cdot)\|_\infty\le A+(1-A^2)B.
\]
The right side is at most \(1\) for every \(0\le A<1\) exactly when \(B\le1/2\),
because
\[
1-A-(1-A^2)B=(1-A)\bigl(1-(1+A)B\bigr).
\]
Conversely, if \(B>1/2\), choose a Schur function attaining the finite coefficient
functional \(M_k(r)\), rotate its phase so that the extremal value is positive, and
then take \(A\uparrow1\) in the inverse disk automorphism above.  This produces a
member of \(\mathcal N_m\) whose \((d+k)\)-th section exceeds \(1\).  Thus (1) is
sharp.

## An exact Schur-functional formula near the boundary

For \(k\ge1\), set
\[
b_j=\frac{\binom{2j}{j}}{4^j},\qquad
q_k=\frac{2k-1}{2k},
\qquad
C_k(r)=\sum_{j=0}^k b_j^2r^{\,k-2j}.
\]
Then
\[
\boxed{M_k(r)=C_k(r)\qquad(q_k\le r\le1).}
\tag{3}
\]

To see this, rotational invariance reduces \(M_k(r)\) to the sharp Schur-class
functional
\[
\sup_{\|\phi\|_\infty\le1}
\left|c_0+rc_1+\cdots+r^kc_k\right|.
\]
Apply the classical Szász coefficient theorem with
\(\mu_\ell=r^{k-\ell}\).  The polynomial whose square matches
\[
r^k+r^{k-1}z+\cdots+z^k
\]
through degree \(k\) is
\[
P_{k,r}(z)=r^{k/2}B_k(z/r),
\qquad
B_k(w)=\sum_{j=0}^k b_jw^j.
\]
The coefficients \(b_j\) are precisely the first \(k+1\) Taylor coefficients of
\((1-w)^{-1/2}\).  Since
\[
\frac{b_j}{b_{j+1}}=\frac{2j+2}{2j+1},
\]
Eneström--Kakeya places every zero of \(B_k\) outside
\[
|w|\ge\frac{2k}{2k-1}.
\]
Thus \(P_{k,r}\) has no zero in \(\mathbb D\) whenever \(r\ge q_k\), and the equality
case in Szász's theorem gives (3).

Consequently, whenever \(m\ge k\ge1\) and
\[
2q_k^{\,m+1}C_k(q_k)\le1,
\tag{4}
\]
the radius \(R_{m+1+k}^{(m)}\) is the unique root in \((q_k,1)\) of
\[
\boxed{
2\sum_{j=0}^k b_j^2
r^{\,m+1+k-2j}=1.
}
\tag{5}
\]
For every fixed \(k\), condition (4) holds for all sufficiently large \(m\).

## The first four nonconstant sections

The reduction gives particularly explicit formulas.

For every \(m\ge1\),
\[
\boxed{R_{m+1}^{(m)}=2^{-1/(m+1)}.}
\tag{6}
\]

For every \(m\ge1\),
\[
\boxed{
R_{m+2}^{(m)}=\rho_m,
\qquad
4\rho_m^{m+2}+\rho_m^m=2.
}
\tag{7}
\]
The root lies in \((1/2,1)\).  At \(m=1\), (7) is exactly the
Das--Sarkar cubic \(4r^3+r-2=0\).

For every \(m\ge2\),
\[
\boxed{
R_{m+3}^{(m)}=\sigma_m,
\qquad
64\sigma_m^{m+3}+16\sigma_m^{m+1}
+9\sigma_m^{m-1}=32.
}
\tag{8}
\]
Indeed \(q_2=3/4\), \(C_2(3/4)=17/16\), and
\[
2(3/4)^3C_2(3/4)=\frac{459}{512}<1,
\]
so (4) already holds at the smallest permitted \(m=2\).

There is also a fourth exact family.  For \(k=3\),
\[
B_3(w)=1+\frac12w+\frac38w^2+\frac5{16}w^3.
\]
In fact all its zeros satisfy \(|w|>4/3\), improving the general
Eneström--Kakeya radius \(6/5\).  To verify this, reciprocate and scale:
the zeros of \(16u^3+8u^2+6u+5\) must be shown to lie in \(|u|<3/4\).
Writing \(u=(3/4)v\) gives \(27v^3+18v^2+18v+20\); under
\(v=(1+s)/(1-s)\), the transformed polynomial is
\[
7s^3+105s^2+21s+83.
\]
The cubic Hurwitz criterion applies because all coefficients are positive and
\(105\cdot21>7\cdot83\).  Hence \(|v|<1\), as claimed.  Therefore
\(M_3(r)=C_3(r)\) already for \(r\ge3/4\).  Since
\[
2(3/4)^4 C_3(3/4)=\frac{5331}{8192}<1,
\]
for every \(m\ge3\),
\[
\boxed{
R_{m+4}^{(m)}=\tau_m,
}
\tag{9}
\]
where \(\tau_m\) is the unique root in \((3/4,1)\) of
\[
\boxed{
256\tau_m^{m+4}+64\tau_m^{m+2}
+36\tau_m^m+25\tau_m^{m-2}=128.
}
\tag{10}
\]

All roots in (7), (8), and (10) are unique because their left sides are strictly
increasing on \((0,1)\).

## Asymptotic hierarchy

For each fixed \(k\), equation (5) gives
\[
R_{m+1+k}^{(m)}
=
1-\frac{\log(2C_k(1))}{m}+O_k(m^{-2})
\qquad(m\to\infty).
\tag{11}
\]
Thus the first four boundary constants are
\[
\log2,\qquad
\log\frac52,\qquad
\log\frac{89}{32},\qquad
\log\frac{381}{128}.
\]
The successive constants strictly increase.  In particular, later early sections
eventually become more restrictive even though every one of these radii tends to
\(1\) as the order of the vanishing constraint grows.

## Context and novelty

Das--Sarkar, arXiv:2609.17114 (2026), establish the sharp Fejér--Rogosinski theorem
for the Neil algebra \(\mathcal N_1\), including (6) and (7) at \(m=1\), and state
that their work is, to their knowledge, the first attempt to obtain an improved
Fejér--Rogosinski radius for a proper subalgebra of \(H^\infty\).  They do not treat
the higher constraints \(\mathcal N_m\), the reduction (1), the general root law
(5), or the new exact section families (8)--(10).

Kovalev, arXiv:2507.04544 (2025), restates the classical Szász coefficient theorem
and studies sharp three-term segments of unrestricted bounded power series.  The
present use is different: the disk automorphism and the order-\(m+1\) zero reduce a
constrained initial-section problem to a weighted Schur functional, and the degree
barrier \(2(m+1)>m+1+k\) makes the reduction exact.

Targeted searches did not locate the higher-\(m\) section-radius formulas above or an
equivalent reduction.  Classical work of Rogosinski, Schur--Szegő, Szász, Nabetani,
and later work on Rogosinski radii concerns unrestricted bounded analytic functions
or other mapping settings.  Rhoda Manning's 1942 paper *On the Derivatives of the
Sections of Bounded Power Series* is title-adjacent but its full text was not
independently inspected here; it remains a residual originality risk, as do the
full texts of Nabetani's 1935 section papers and unindexed concurrent work prompted
by the recent Neil-algebra preprint.

## Limitations

This record determines a reduction for offsets \(0\le k\le m\), gives an exact
formula under the explicit zero-free condition (4), and resolves the first four
nonconstant sections as above.  It does **not** determine the optimal single radius
valid simultaneously for every section of \(\mathcal N_m\) when \(m>1\).  For
larger offsets, the corresponding Szász extremal polynomial must remain zero-free
at the candidate radius; the general zero geometry can become nontrivial.  No claim
is made about sections beyond the degree range where the \(h^2\) term is absent.

## References

1. N. Das and J. Sarkar, *Fejér-Rogosinski theorem for the Neil algebra*,
   arXiv:2609.17114 (2026).
2. L. V. Kovalev, *Sharp bounds for some segments of bounded power series*,
   arXiv:2507.04544 (2025).
3. O. Szász, *Ungleichungen für die Koeffizienten einer Potenzreihe*,
   Math. Z. 1 (1918), 163--183.
4. W. Rogosinski, *Über Bildschranken bei Potenzreihen und ihren Abschnitten*,
   Math. Z. 17 (1923), 260--276.
5. R. Manning, *On the Derivatives of the Sections of Bounded Power Series*,
   Ann. of Math. 43 (1942), 617--622.
