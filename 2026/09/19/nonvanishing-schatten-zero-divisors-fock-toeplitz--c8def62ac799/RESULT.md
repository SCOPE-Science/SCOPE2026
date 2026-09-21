# Nonvanishing bounded symbols yield all-Schatten zero divisors on Fock space

## Statement

Let \(F^2(\mathbb C^n)\) be the standard Fock space, \(n\ge 2\), with reproducing kernels \(K_a\). Write
\[
z=(\xi,z'),\qquad \xi=(z_1,z_2)^T,\qquad
X=|z_1|^2-|z_2|^2,\quad
Y=2\operatorname{Im}(\overline z_1z_2),\quad
Z=2\operatorname{Re}(\overline z_1z_2).
\]
For parameters \(q,\rho\ge0\), put \(a=1+q\) and define
\[
\begin{aligned}
f_{q,\rho}(z)
&=2e^{-q|\xi|^2-\rho|z'|^2}
 \left[
 i e^{-iaY}\sin\!\bigl(a(X-Z)\bigr)
 - e^{iaY}\sin\!\bigl(a(X+Z)\bigr)
 \right],\\
g_{q,\rho}(z)
&=2e^{-q|\xi|^2-\rho|z'|^2}
 \left[
 e^{-iaY}\cos\!\bigl(a(X+Z)\bigr)
 + i e^{iaY}\cos\!\bigl(a(X-Z)\bigr)
 \right].
\end{aligned}
\]
When \(n=2\), the \(z'\)-terms are omitted.

Then \(f_{q,\rho}\) and \(g_{q,\rho}\) are bounded smooth nonradial symbols and
\[
T_{f_{q,\rho}}T_{g_{q,\rho}}=0.
\]
Both Toeplitz operators are nonzero and have infinite rank.

Moreover:

1. If \(n=2\), then for every \(q\ge0\),
   \[
   T_{f_{q,0}},T_{g_{q,0}}\in\bigcap_{p>0}S_p.
   \]
2. If \(n>2\) and \(\rho>0\), then for every \(q\ge0\),
   \[
   T_{f_{q,\rho}},T_{g_{q,\rho}}\in\bigcap_{p>0}S_p.
   \]
3. If \(n>2\) and \(\rho=0\), both operators are noncompact.

At the bounded endpoint \(q=0\), the symbols have no decay in the active \(\mathbb C^2\)-directions. In particular, for \(n=2\),
\[
\begin{aligned}
f_0(z)
&=2\left[
 i e^{-iY}\sin(X-Z)-e^{iY}\sin(X+Z)
 \right],\\
g_0(z)
&=2\left[
 e^{-iY}\cos(X+Z)+i e^{iY}\cos(X-Z)
 \right]
\end{aligned}
\]
do not tend to zero at infinity, while
\[
T_{f_0},T_{g_0}\in\bigcap_{p>0}S_p,\qquad
T_{f_0}T_{g_0}=0.
\]
Thus bounded symbols can remain macroscopic at infinity while their Toeplitz operators are simultaneously infinitely smoothing in the Schatten scale and form a nontrivial zero product.

## Gaussian transfer lemma

Set
\[
E_1=\begin{pmatrix}i&0\\0&-i\end{pmatrix},\quad
E_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
E_3=\begin{pmatrix}0&i\\i&0\end{pmatrix},
\]
and
\[
W(\varepsilon_1,\varepsilon_2,\varepsilon_3)
=\frac12\left(I_2+\varepsilon_1E_1+\varepsilon_2E_2+\varepsilon_3E_3\right).
\]
As in Qin's construction, every such \(W\) is unitary, satisfies \(W+W^*=I_2\), and has determinant one.

For any such \(U\), define
\[
\sigma_{U;q,\rho}(z)
=
\exp\!\left(
\bigl((I_2-2(1+q)U^*)\xi\bigr)\cdot\xi
-\rho|z'|^2
\right),
\]
where \(u\cdot v=v^*u\). Since \(U+U^*=I_2\),
\[
|\sigma_{U;q,\rho}(z)|
=e^{-q|\xi|^2-\rho|z'|^2}.
\]
Combining the symbol with the Fock Gaussian gives the matrix
\[
M_{U;q,\rho}
=
\operatorname{diag}\!\left(2(1+q)U^*,(1+\rho)I_{n-2}\right).
\]
The same complex Gaussian integral used in Qin's Lemma 2.1 yields
\[
T_{\sigma_{U;q,\rho}}K_b
=
\kappa_{q,\rho}\,
K_{D_{U;q,\rho}^*b},
\]
where
\[
D_{U;q,\rho}
=
\operatorname{diag}\!\left(
\frac{U}{2(1+q)},\frac{I_{n-2}}{1+\rho}
\right),
\qquad
\kappa_{q,\rho}
=
\frac{1}{4(1+q)^2(1+\rho)^{n-2}}.
\]
The empty passive block is omitted for \(n=2\).

For \(q=\rho=1\), this is precisely Qin's Gaussian kernel map:
\(D=\operatorname{diag}(U/4,I/2)\) and
\(\kappa=2^{-n-2}\). The endpoint \(q=0\) changes the active symbol modulus from Gaussian decay to modulus one while the active linear contraction remains \(U/2\).

## Quaternionic cancellation and the zero product

Use
\[
\begin{aligned}
U_1&=W(-1,-1,-1),&
U_2&=W(1,1,-1),&
U_3&=W(1,-1,1),&
U_4&=W(-1,1,1),\\
V_1&=W(1,-1,-1),&
V_2&=W(-1,1,-1),&
V_3&=W(-1,-1,1),&
V_4&=W(1,1,1),
\end{aligned}
\]
with coefficient vectors
\[
(c_1,c_2,c_3,c_4)=(1,i,1,i),\qquad
(d_1,d_2,d_3,d_4)=(1,-i,-1,i).
\]
Direct grouping of the sixteen products gives
\[
\sum_{(j,k):\,U_jV_k=H}c_jd_k=0
\]
for every product value
\[
H\in\{I_2,\pm E_1,\pm E_2,\pm E_3\}.
\]
Set
\[
g_{q,\rho}=\sum_{j=1}^4c_j\sigma_{U_j;q,\rho},
\qquad
f_{q,\rho}=\sum_{k=1}^4d_k\sigma_{V_k;q,\rho}.
\]
Expanding the exponentials gives exactly the trigonometric formulas in the statement.

Since
\[
D_{U_j;q,\rho}D_{V_k;q,\rho}
=
\operatorname{diag}\!\left(
\frac{U_jV_k}{4(1+q)^2},
\frac{I_{n-2}}{(1+\rho)^2}
\right),
\]
the kernel action depends on \((j,k)\) only through \(U_jV_k\). Therefore the displayed coefficient cancellations imply
\[
T_{f_{q,\rho}}T_{g_{q,\rho}}K_b=0
\quad\text{for every }b\in\mathbb C^n.
\]
The span of the reproducing kernels is dense, so
\[
T_{f_{q,\rho}}T_{g_{q,\rho}}=0.
\]

## Schatten smoothing

From the kernel formula,
\[
T_{\sigma_{U;q,\rho}}
=
\kappa_{q,\rho}\,C_{D_{U;q,\rho}^*}^*,
\]
where \(C_Ah=h(Az)\). The singular values of
\(D_{U;q,\rho}\) are
\[
\frac1{2(1+q)},\ \frac1{2(1+q)},
\quad
\underbrace{\frac1{1+\rho},\ldots,\frac1{1+\rho}}_{n-2\text{ times}}.
\]
For a strict linear contraction with singular values \(s_1,\ldots,s_n\), the normalized monomial basis gives
\[
\|C_A\|_{S_p}^p
=
\prod_{r=1}^n(1-s_r^p)^{-1},
\qquad p>0.
\]
Hence, whenever \(n=2\) or \(\rho>0\),
\[
\|T_{\sigma_{U;q,\rho}}\|_{S_p}^p
=
\kappa_{q,\rho}^p
\left(1-[2(1+q)]^{-p}\right)^{-2}
\left(1-(1+\rho)^{-p}\right)^{-(n-2)}.
\]
The last factor is absent for \(n=2\). Thus every Gaussian building block lies in every Schatten class \(S_p\), \(p>0\), and so do the finite sums \(T_{f_{q,\rho}}\) and \(T_{g_{q,\rho}}\).

This calculation explains why the nondecaying endpoint is possible. At \(q=0\), the symbol has no active amplitude decay, but its quadratic phase produces the strict contraction \(U/2\) on the Fock side.

## Nonvanishing symbols and infinite-rank operators

At \(q=0\) and \(z'=0\), put \(p_t=(t,0)\). Then
\[
f_{0,\rho}(p_t)=2(i-1)\sin(t^2).
\]
For \(t_k^2=\pi/2+2\pi k\),
\[
|f_{0,\rho}(p_{t_k})|=2\sqrt2.
\]
Thus \(f_{0,\rho}\) does not tend to zero at infinity. If
\(r_t=(t/\sqrt2,it/\sqrt2)\), then \(X=Z=0\), \(Y=t^2\), and
\[
f_{0,\rho}(r_t)=0,\qquad
|g_{0,\rho}(r_{t_k})|=2\sqrt2,
\]
while \(g_{0,\rho}(p_{t_k})=0\). Hence both symbols are nonradial and neither tends to zero at infinity along the active plane.

The corresponding Toeplitz operators have infinite rank. Indeed, each
\(C_{D^*}^*\) preserves the orthogonal decomposition into homogeneous polynomial degrees. If a finite sum such as \(T_{f_{q,\rho}}\) had finite rank, all sufficiently high homogeneous blocks would vanish. Consequently, for fixed \(a,z\),
\[
s\longmapsto
(T_{f_{q,\rho}}K_{\overline s a})(z)
\]
would be a polynomial in \(s\). The kernel formula instead makes this a finite sum
\[
\kappa_{q,\rho}
\sum_{k=1}^4d_k e^{s(D_{V_k;q,\rho}z)\cdot a}.
\]
One may choose \(a,z\) supported in the active \(\mathbb C^2\) so that the four exponents are pairwise distinct: the excluded choices form a finite union of proper bilinear zero sets because the \(V_k\) are distinct. A nontrivial finite sum of exponentials with distinct exponents cannot be a polynomial. This contradiction proves infinite rank. The same argument applies to \(T_{g_{q,\rho}}\).

In particular,
\[
\operatorname{ran}T_{g_{q,\rho}}
\subseteq
\ker T_{f_{q,\rho}},
\]
so the kernel of the first factor is infinite dimensional. Taking adjoints shows that \(\ker T_{g_{q,\rho}}^*\) is also infinite dimensional; equivalently, the closure of the range of the second factor has infinite codimension.

## Exact passive-direction compactness boundary

For \(n>2\), the parameter \(\rho\) has a sharp effect inside this family. If \(\rho=0\), both symbols depend only on the first two coordinates. Under
\[
F^2(\mathbb C^n)
\cong
F^2(\mathbb C^2)\otimes F^2(\mathbb C^{n-2}),
\]
their Toeplitz operators factor as
\[
T_{f_{q,0}}=
T_{f_{q,0}}^{(2)}\otimes I,
\qquad
T_{g_{q,0}}=
T_{g_{q,0}}^{(2)}\otimes I.
\]
The active factors are nonzero, so these tensor products are not compact. For every \(\rho>0\), the preceding Schatten formula puts both operators in every \(S_p\). Thus any positive passive Gaussian damping changes this explicit zero-product pair from noncompact to all-Schatten, while no active damping is needed.

## Relation to the literature

Jie Qin's 2026 preprint constructs bounded nonradial Schwartz symbols with zero Toeplitz product for \(n\ge2\). His Gaussian lemma corresponds to the interior parameter choice \(q=\rho=1\), and the paper does not state compactness, trace-class, or Schatten conclusions. The present observation is a deformation of that construction to the bounded endpoint \(q=0\), where active Gaussian decay disappears, together with the exact Schatten analysis and the passive compactness boundary.

Bauer and Le (2011) previously produced zero products on Segal--Bargmann space, including a two-factor example with unbounded radial symbols at critical growth and a three-factor example with bounded radial symbols. Their work is prior art for the zero-product mechanism, not for the endpoint statement above.

Lin, Lu and Zu (2026) give a Fourier criterion for bounded-symbol Toeplitz representability and applications to weighted composition operators. That work is relevant prior art for recognizing individual weighted-composition-type operators as Toeplitz operators; no novelty is claimed here for such a general recognition principle.

Isralowitz and Zhu (2010) characterize compactness and Schatten membership for Toeplitz operators with positive measure symbols. Those positivity results do not cover the oscillatory complex symbols used here.

## Limitations

The result concerns \(n\ge2\) and this explicit quaternionic Gaussian family. It does not resolve the still-open two-bounded-symbol zero-product problem in one complex dimension, classify all bounded nondecaying symbols whose Toeplitz operators are compact or Schatten, or give optimal Schatten quasi-norms for the finite sums \(T_f,T_g\). The exact formula above is for the Gaussian building blocks. The originality claim is only to the best of our knowledge.

The full text of Bauer--Le (2011) was not inspected here; its abstract and the detailed account of its zero-product examples in Qin's paper were inspected. This leaves a residual risk that an equivalent endpoint deformation or ideal-membership observation occurs there under different notation. Lin--Lu--Zu (2026) was inspected at the abstract level for its weighted-composition application, so its detailed formulas may subsume the single-building-block representation; that representation is therefore not claimed as new.

## References

- J. Qin, *Zero-product problem for Toeplitz operators on the Fock space*, arXiv:2609.20555v1 (2026), https://arxiv.org/abs/2609.20555.
- W. Bauer and T. Le, *Algebraic properties and the finite rank problem for Toeplitz operators on the Segal--Bargmann space*, J. Funct. Anal. 261 (2011), 2617--2640, https://doi.org/10.1016/j.jfa.2011.07.006.
- Z. Lin, Y. Lu and C. Zu, *A Fourier Criterion for Recognizing Toeplitz Operators on Fock Spaces*, arXiv:2607.04102 (2026), https://arxiv.org/abs/2607.04102.
- J. Isralowitz and K. Zhu, *Toeplitz operators on the Fock space*, Integral Equations Operator Theory 66 (2010), 593--611, https://doi.org/10.1007/s00020-010-1768-9.
