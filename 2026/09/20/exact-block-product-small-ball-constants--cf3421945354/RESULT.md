# Exact constants and concentration centers for block-product anti-concentration

## Statement

Let \(d\ge 1\), let \(\mathbf m=(m_1,\dots,m_d)\in\mathbb N^d\), and let the blocks \(B_1,\dots,B_d\) be disjoint with \(|B_k|=m_k\). For \(X\) uniform on the corresponding cube, define
\[
P_{\mathbf m,d}(X)
=
\prod_{k=1}^d
\left(\frac{2}{m_k}\sum_{i\in B_k}X_i-1\right).
\]
Write
\[
M_{\mathbf m}=\prod_{k=1}^d\sqrt{m_k},
\qquad
\Phi_d(s)=s\sum_{j=0}^{d-1}\frac{\log^j(1/s)}{j!}
\quad (0<s\le 1).
\]

For \(m\ge1\), let \(a_m\) be the density of
\[
A_m=\frac1m\sum_{j=1}^m Y_j,
\qquad
Y_j\stackrel{\mathrm{iid}}{\sim}\operatorname{Unif}[-1,1],
\]
and define
\[
\beta_m=\frac{2a_m(0)}{\sqrt m}.
\]
The Irwin--Hall formula gives the explicit finite sum
\[
\boxed{
\beta_m
=
\frac{\sqrt m}{(m-1)!}
\sum_{j=0}^{\lfloor m/2\rfloor}
(-1)^j\binom mj
\left(\frac m2-j\right)^{m-1}.
}
\]
For \(m=1\), this is interpreted as \(\beta_1=1\). Put
\[
B_{\mathbf m}=\prod_{k=1}^d\beta_{m_k}.
\]

Then the centered block product has the following exact all-center property:
\[
\boxed{
\sup_{u\in\mathbb R}
\mathbb P\{|P_{\mathbf m,d}(X)-u|\le \rho\}
=
\mathbb P\{|P_{\mathbf m,d}(X)|\le \rho\}
\qquad(\rho\ge0).
}
\]

At the natural block scale from the recent product-profile theorem,
\[
\boxed{
\lim_{s\downarrow0}
\frac{
\sup_{u\in\mathbb R}
\mathbb P\{|P_{\mathbf m,d}(X)-u|\le s/M_{\mathbf m}\}
}{
\Phi_d(s)
}
=
B_{\mathbf m}.
}
\]
Thus the degree-dependent comparability constants for the canonical block-product extremizers can be replaced, at small scale, by an explicit block-size-dependent constant.

## Second logarithmic term

Let
\[
H_m(x)=2a_m(x),\qquad 0\le x\le1,
\]
so that \(H_m\) is the density of \(|A_m|\), and set
\[
c_m=H_m(0)=\sqrt m\,\beta_m,
\qquad
\delta_m=
\frac1{c_m}
\int_0^1\frac{H_m(x)-c_m}{x}\,dx.
\]
The integral converges. Since \(a_m\) is even and unimodal, \(\delta_m\le0\). In particular,
\[
\delta_1=0,\qquad \delta_2=-1.
\]

For \(d\ge2\), with \(L=\log(1/s)\),
\[
\boxed{
\begin{aligned}
&\sup_{u\in\mathbb R}
\mathbb P\{|P_{\mathbf m,d}(X)-u|\le s/M_{\mathbf m}\}\\
&\quad=
B_{\mathbf m}s
\left[
\frac{L^{d-1}}{(d-1)!}
+
\frac{
1+\log M_{\mathbf m}+\sum_{k=1}^d\delta_{m_k}
}{(d-2)!}
L^{d-2}
+
o(L^{d-2})
\right].
\end{aligned}
}
\]
Equivalently,
\[
\boxed{
\mathbb P\{|P_{\mathbf m,d}(X)|\le s/M_{\mathbf m}\}
=
B_{\mathbf m}\Phi_d(s)
+
\frac{
B_{\mathbf m}
\left(\log M_{\mathbf m}+\sum_k\delta_{m_k}\right)
}{(d-2)!}
sL^{d-2}
+
o(sL^{d-2}).
}
\]

## Density singularity and exact high-\(p\) constant

Let \(f_{\mathbf m,d}\) denote the density of \(P_{\mathbf m,d}(X)\). As \(t\to0\),
\[
\boxed{
f_{\mathbf m,d}(t)
\sim
\frac{M_{\mathbf m}B_{\mathbf m}}{2(d-1)!}
\log^{d-1}\frac1{|t|}.
}
\]
For \(d\ge2\), the next term is
\[
\boxed{
f_{\mathbf m,d}(t)
=
\frac{M_{\mathbf m}B_{\mathbf m}}2
\left[
\frac{L_t^{d-1}}{(d-1)!}
+
\frac{\sum_k\delta_{m_k}}{(d-2)!}
L_t^{d-2}
+
o(L_t^{d-2})
\right],
\qquad
L_t=\log\frac1{|t|}.
}
\]

Consequently the order-sharp \(L^p\) estimate for these examples has an exact limiting constant:
\[
\boxed{
\lim_{p\to\infty}
\frac{
\|f_{\mathbf m,d}\|_{L^p(\mathbb R)}
}{
p^{d-1}M_{\mathbf m}^{1-1/p}
}
=
\frac{B_{\mathbf m}}{2(d-1)!}
\left(\frac{d-1}{e}\right)^{d-1}.
}
\]
For \(d=1\), the factor \(((d-1)/e)^{d-1}\) is interpreted as \(1\), and the limit is \(\beta_{m_1}/2\).

## Large-block limit

The block constant has a universal Gaussian limit with a first correction:
\[
\boxed{
\beta_m
=
\sqrt{\frac6\pi}
\left(
1-\frac{3}{20m}+O(m^{-2})
\right).
}
\]
Hence, for fixed \(d\) and \(\min_km_k\to\infty\),
\[
\boxed{
B_{\mathbf m}
=
\left(\frac6\pi\right)^{d/2}
\left[
1-\frac3{20}\sum_{k=1}^d\frac1{m_k}
+
O_d\!\left((\min_km_k)^{-2}\right)
\right].
}
\]

## Proof

### 1. Exact concentration center

Each \(a_m\) is even and log-concave, hence nonincreasing on \([0,\infty)\). If \(U,V\) are independent random variables with even densities \(f,g\) that are nonincreasing on \([0,\infty)\), then for \(t>0\) the density of \(UV\) is
\[
h(t)=2\int_0^\infty f(x)g(t/x)\,\frac{dx}{x}.
\]
For each fixed \(x>0\), the integrand is nonincreasing in \(t\), so \(h\) is nonincreasing on \((0,\infty)\). Induction shows that \(P_{\mathbf m,d}(X)\) has an even density nonincreasing in \(|t|\). For every even decreasing density, an interval of fixed length has maximal mass when centered at zero. This proves the all-center identity.

### 2. Mellin-to-additive reduction

Let \(W_m=|A_m|\) and \(T_m=-\log W_m\). The density of \(T_m\) is
\[
q_m(u)=e^{-u}r_m(u),
\qquad
r_m(u)=H_m(e^{-u}),
\qquad u\ge0.
\]
As \(u\to\infty\),
\[
r_m(u)\to c_m,
\]
and
\[
g_m(u):=r_m(u)-c_m\in L^1(0,\infty),
\qquad
\int_0^\infty g_m(u)\,du=c_m\delta_m.
\]
The last identity is the substitution \(x=e^{-u}\).

For
\[
T=\sum_{k=1}^dT_{m_k},
\]
independence gives
\[
q_T(u)
=
e^{-u}(r_{m_1}*\cdots*r_{m_d})(u).
\]
Writing \(r_{m_k}=c_{m_k}+g_{m_k}\) and expanding the convolution, the constant term and the terms containing exactly one \(g\) give
\[
(r_{m_1}*\cdots*r_{m_d})(u)
=
C_{\mathbf m}
\left[
\frac{u^{d-1}}{(d-1)!}
+
\frac{\sum_k\delta_{m_k}}{(d-2)!}u^{d-2}
+
o(u^{d-2})
\right],
\]
where
\[
C_{\mathbf m}=\prod_kc_{m_k}=M_{\mathbf m}B_{\mathbf m}.
\]
Terms containing at least two \(g\)'s are lower order; this follows from \(g_m\in L^1\) (and here the \(g_m\) are bounded and exponentially decaying after the logarithmic change of variables).

Now
\[
\prod_kW_{m_k}\le \frac{s}{M_{\mathbf m}}
\quad\Longleftrightarrow\quad
T\ge L+\log M_{\mathbf m}.
\]
For every integer \(r\ge0\),
\[
\int_x^\infty e^{-u}\frac{u^r}{r!}\,du
=
e^{-x}\sum_{j=0}^r\frac{x^j}{j!}.
\]
Substitution of the convolution expansion, followed by expansion of
\(x=L+\log M_{\mathbf m}\), proves the leading constant and the second logarithmic term.

### 3. Density and \(L^p\) norm

If \(V=\prod_kW_{m_k}\), then the density of \(V\) at \(v\in(0,1)\) is
\[
(r_{m_1}*\cdots*r_{m_d})\!\left(\log\frac1v\right).
\]
The product sign is symmetric and independent of the magnitudes, so
\[
f_{\mathbf m,d}(t)
=
\frac12
(r_{m_1}*\cdots*r_{m_d})
\!\left(\log\frac1{|t|}\right),
\qquad 0<|t|<1.
\]
This gives the density expansion.

Let \(q=d-1\) and
\[
K=\frac{M_{\mathbf m}B_{\mathbf m}}{2q!}.
\]
Near zero, \(f(t)\sim K\log^q(1/|t|)\), while \(f\) is bounded on every set separated from zero. Thus
\[
\int_0^1\log^{qp}(1/t)\,dt=\Gamma(qp+1)
\]
and Stirling's formula yield
\[
\|f\|_p
\sim
K\left(\frac{qp}{e}\right)^q.
\]
After division by \(p^qM_{\mathbf m}^{1-1/p}\), the asserted constant follows.

### 4. Central block density

The displayed finite formula for \(\beta_m\) is the classical Irwin--Hall density evaluated at the central point and rescaled from a sum of \(\operatorname{Unif}[0,1]\) variables to the average of \(\operatorname{Unif}[-1,1]\) variables.

For the large-\(m\) expansion, the density of \(Z_m=\sqrt m\,A_m\) at zero is
\[
f_{Z_m}(0)
=
\frac1{2\pi}\int_{\mathbb R}
\left[
\frac{\sin(t/\sqrt m)}{t/\sqrt m}
\right]^m\,dt,
\qquad
\beta_m=2f_{Z_m}(0).
\]
Using
\[
\log\frac{\sin x}{x}
=
-\frac{x^2}{6}-\frac{x^4}{180}+O(x^6)
\]
and Laplace expansion around \(t=0\) gives
\[
f_{Z_m}(0)
=
\sqrt{\frac{3}{2\pi}}
\left(1-\frac3{20m}+O(m^{-2})\right),
\]
which proves the stated asymptotic.

## Checks and examples

If every \(m_k=1\), then each \(|A_{m_k}|\) is uniform on \([0,1]\), so \(B_{\mathbf m}=1\), every \(\delta_{m_k}=0\), and the exact product law reduces to the classical profile \(\Phi_d\).

For \((m_1,m_2)=(2,2)\), \(H_2(x)=2(1-x)\), hence \(B_{\mathbf m}=2\), \(M_{\mathbf m}=2\), and \(\delta_2=-1\). In this case, for \(0<\varepsilon<1\),
\[
\mathbb P\{W_1W_2\le\varepsilon\}
=
\varepsilon\left[
5\varepsilon-2(\varepsilon+2)\log\varepsilon-4
\right].
\]
Taking \(\varepsilon=s/2\) gives
\[
2s\left(\log\frac1s+\log2-1\right)+o(s),
\]
exactly matching the general two-term formula.

## Relation to prior work and limitations

Abakumov--Friedland--Yomdin prove that these centered block products attain the product profile and the full block-size scale up to degree-dependent constants, and they prove matching \(p^{d-1}\) density growth up to degree-dependent constants. The present result refines those canonical extremizers by identifying the exact concentration center, the exact small-ball coefficient, the next logarithmic term, and the exact high-\(p\) density coefficient.

The Irwin--Hall formula and general Mellin-convolution methods for products of random variables are classical and are not claimed as new. The contribution is their explicit synthesis for the recent block-product extremizers and the resulting sharp constants and second-order terms.

The result does not determine the optimal constant for arbitrary multi-affine polynomials or arbitrary admissible partitions. It does not close the source paper's gap between the singleton-partition dimensional exponents \(d/2\) and \(d-1/2\). The second-order formulas hold with the block sizes fixed while \(s\downarrow0\); no uniform second-order remainder over growing block sizes is claimed.

## References

1. E. Abakumov, O. Friedland, Y. Yomdin, *Product-profile anti-concentration for block-structured multi-affine polynomials*, arXiv:2609.19473 (2026).
2. J. E. Marengo, D. L. Farnsworth, L. Stefanic, *A Geometric Derivation of the Irwin-Hall Distribution*, International Journal of Mathematics and Mathematical Sciences 2017, Article 3571419, doi:10.1155/2017/3571419.
3. M. D. Springer, W. E. Thompson, *The Distribution of Products of Beta, Gamma and Gaussian Random Variables*, SIAM Journal on Applied Mathematics 18 (1970), 721--737, doi:10.1137/0118065.
4. A. M. Mathai, H. J. Haubold, *Mellin convolutions of products and ratios*, Frontiers in Applied Mathematics and Statistics (2025), doi:10.3389/fams.2025.1526541.
