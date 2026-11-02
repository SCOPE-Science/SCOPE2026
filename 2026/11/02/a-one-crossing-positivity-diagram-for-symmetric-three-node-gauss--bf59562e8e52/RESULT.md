# A one-crossing positivity diagram for symmetric three-node Gaussian kernel quadrature

## Finding

For every \(a\in(0,1]\) and Gaussian shape \(\varepsilon>0\), form the *unaugmented* Gaussian radial-basis-function quadrature rule on \([-1,1]\) from the nodes \((-a,0,a)\) and kernel
\[
k_\varepsilon(x,y)=\exp[-\varepsilon^2(x-y)^2].
\]
Let \(Q_{a,\varepsilon}(f)=u f(-a)+v f(0)+u f(a)\) integrate each of the three kernel translates exactly against Lebesgue measure. Its two endpoint weights \(u\) are strictly positive for all parameters. Its central weight \(v\) has the following *complete* sign classification:

1. If \(a\ge1/\sqrt3\), then \(v>0\) for every \(\varepsilon>0\).
2. If \(0<a<1/\sqrt3\), there is a unique \(\varepsilon_*(a)>0\) such that \(v<0\) for \(0<\varepsilon<\varepsilon_*(a)\), \(v=0\) at \(\varepsilon=\varepsilon_*(a)\), and \(v>0\) for \(\varepsilon>\varepsilon_*(a)\).

Consequently the quadrature functional is nonnegative on every function that is nonnegative at the three nodes precisely in the nonnegative-weight regime. In the negative regime a nonnegative smooth polynomial already yields a negative quadrature output. In particular, for \(a=1/2\), the unique transition is
\[
\varepsilon_*(1/2)=1.0786096032571438128\ldots.
\]

## Assumptions and scope

The domain is the fixed interval \([-1,1]\) with uniform Lebesgue measure, not an unbounded Gaussian integration measure. The three interpolation centers \((-a,0,a)\) are distinct, with \(0<a\le1\). The kernel is the Gaussian above with one common positive shape parameter. No polynomial terms, positivity constraints, or least-squares oversampling are added. All weight assertions concern exact arithmetic and the unique interpolatory weights of the strictly positive-definite kernel matrix. The quadrature is exact on the span of the three kernel translates, but need not integrate constants exactly.

Set \(t=\varepsilon^2\), \(q=\exp(-ta^2)\), and
\[
C(t)=\int_{-1}^1e^{-tx^2}\,dx,\qquad
B(a,t)=\int_{-1}^1e^{-t(x-a)^2}\,dx.
\]
Writing the kernel matrix in the indicated node order, exactness gives
\[
\begin{pmatrix}1&q&q^4\\q&1&q\\q^4&q&1\end{pmatrix}
\begin{pmatrix}u\\v\\u\end{pmatrix}
=\begin{pmatrix}B\\C\\B\end{pmatrix}.
\]
Its exact solution is
\[
u=\frac{B-qC}{(1-q^2)^2},\qquad
v=\frac{C(1+q^4)-2qB}{(1-q^2)^2}.
\]
In the flat-kernel limit \(\varepsilon\downarrow0\), these weights tend to the quadratic-interpolation weights
\[
(u,v,u)\longrightarrow
\left(\frac1{3a^2},\ 2-\frac2{3a^2},\ \frac1{3a^2}\right).
\]
This limit does not by itself prove the unique transition at finite shape.

## Proof

**Endpoint positivity and the central sign integral.** By symmetry,
\[
B=q\int_{-1}^1e^{-tx^2}\cosh(2tax)\,dx.
\]
Hence
\[
B-qC=q\int_{-1}^1e^{-tx^2}\big[\cosh(2tax)-1\big]dx>0
\]
for every \(a,t>0\); therefore \(u>0\). Also
\[
\operatorname{sgn}v=\operatorname{sgn}S_a(t),\quad
S_a(t)=\int_0^1e^{-tx^2}
\big[\cosh(2ta^2)-\cosh(2tax)\big]dx,
\]
because the exact multiplier relating \(v\) to \(S_a(t)\) is \(4q^2/(1-q^2)^2>0\). If \(a=1\), the integrand is positive for almost every \(x\in(0,1)\).

**Single-crossing lemma.** Fix \(0<a<1\) and write \(S_a(t)=P_a(t)-N_a(t)\), where
\[
\begin{aligned}
P_a(t)&=\int_0^a e^{-tx^2}\big[\cosh(2ta^2)-\cosh(2tax)\big]dx,\\
N_a(t)&=\int_a^1 e^{-tx^2}\big[\cosh(2tax)-\cosh(2ta^2)\big]dx.
\end{aligned}
\]
Both are strictly positive for \(t>0\). We prove that \(P_a(t)/N_a(t)\) is strictly increasing, rather than merely verifying crossings numerically. For \(0\le x<a<y\le1\), denote their respective positive integrands by \(F_t(x)\) and \(G_t(y)\). The identity \(\cosh U-\cosh V=2\sinh[(U+V)/2]\sinh[(U-V)/2]\) gives
\[
\begin{aligned}
F_t(x)&=2e^{-tx^2}\sinh[ta(a+x)]\sinh[ta(a-x)],\\
G_t(y)&=2e^{-ty^2}\sinh[ta(y+a)]\sinh[ta(y-a)].
\end{aligned}
\]
For \(s>0\) let \(H_t(s)=s\coth(ts)\). Direct differentiation shows
\[
0<H_t'(s)=\coth(ts)-ts\operatorname{csch}^2(ts)<1.
\]
Indeed, for \(z=ts>0\), the first inequality follows from \(\sinh z\cosh z>z\), and the second from \(\sinh z e^{-z}=(1-e^{-2z})/2<z\). Thus \(H_t\) is increasing and strictly one-Lipschitz on the positive half-line (with continuous endpoint value \(H_t(0)=1/t\)). Differentiating the logarithmic integrand ratio gives
\[
\begin{aligned}
\partial_t\log\frac{F_t(x)}{G_t(y)}
={}& y^2-x^2+H_t[a(a+x)]+H_t[a(a-x)]\\
&-H_t[a(y+a)]-H_t[a(y-a)].
\end{aligned}
\]
The sum of its last two negative terms relative to the corresponding positive ones is bounded above by
\[
a(y-x)+a\max\{0,y+x-2a\}.
\]
If \(y+x<2a\), this is at most \(y^2-x^2=(y-x)(y+x)\), because \(y+x\ge a\). If \(y+x\ge2a\), it equals \(2a(y-a)\), which is at most \(y^2-x^2\) because
\[
y^2-x^2-2a(y-a)=(y-a)^2+a^2-x^2\ge0.
\]
The inequalities are strict for interior \(0<x<a<y<1\). Thus \(F_t(x)/G_t(y)\) strictly increases with \(t\). Integrating the cross-products over \((x,y)\in(0,a)\times(a,1)\) proves \(P_a(t_2)/N_a(t_2)>P_a(t_1)/N_a(t_1)\) whenever \(t_2>t_1>0\).

**Boundary signs and uniqueness.** Taylor expansion uniformly on \([0,1]\) yields
\[
\lim_{t\downarrow0}\frac{S_a(t)}{t^2}
=2a^2\int_0^1(a^2-x^2)dx
=2a^2\left(a^2-\frac13\right).
\]
The same expansion for \(P_a\) and \(N_a\) shows that their limiting ratio is below, at, or above one according as \(a^2<1/3\), \(a^2=1/3\), or \(a^2>1/3\). In the equality case, strict monotonicity gives \(P_a(t)>N_a(t)\) for every positive \(t\).

For each fixed \(a>0\), \(C(t)\) is asymptotic to \(\sqrt{\pi/t}\), while \(0<B(a,t)\le2\) and \(q\to0\) exponentially. The exact formula for \(v\) therefore shows \(v>0\) for all sufficiently large \(t\). Equivalently \(P_a(t)>N_a(t)\) eventually. Strict monotonicity of \(P_a/N_a\), continuity, and the small-shape limits now give the stated unique transition, or positivity for every positive shape when \(a\ge1/\sqrt3\).

**Positivity preservation and sharp witness.** A linear combination \(u f(-a)+v f(0)+u f(a)\) is nonnegative for all nonnegative node data exactly when all its weights are nonnegative. If \(v<0\), the smooth polynomial \(f(x)=(1-x^2/a^2)^2\) is nonnegative throughout the interval but satisfies \(f(-a)=f(a)=0\), \(f(0)=1\), so \(Q_{a,\varepsilon}(f)=v<0\). The threshold is therefore an actual failure of positive numerical integration rather than only a signed coefficient phenomenon.

## Verification

The standalone \(\texttt{verify.py}\) uses arbitrary-precision arithmetic to check the three-by-three linear solve independently against the closed weight formulas, the equivalent integral formula, the strict positive-versus-negative regions for selected parameters, the flat-kernel limits, pointwise ratio monotonicity, and the example transition for \(a=1/2\). It completed **389 finite checks**. Execute \(\texttt{python verify.py}\) with Python 3 and \(\texttt{mpmath}\) installed. The analytic one-crossing lemma, not finite sampling, proves the universal statement.

The root for \(a=1/2\) is the unique positive solution in \(\varepsilon\) of
\[
C(\varepsilon^2)(1+e^{-\varepsilon^2})
=2e^{-\varepsilon^2/4}B(1/2,\varepsilon^2).
\]
This is the original exact condition \(C(1+q^4)=2qB\) specialized to \(a=1/2\); that condition, rather than the rounded decimal, defines the root. All numbers are reported from arbitrary-precision evaluation.

## Relationship to prior work

Glaubitz and Reeger's 2023 study [1] defines interpolatory RBF quadrature weights as integrated cardinal functions and analyzes large-node stability, compact support, and oversampled least-squares remedies. It does not state the present fixed-three-node, all-shape sign classification. Karvonen, Kanagawa, and Särkkä [2] prove that at least half the weights of a one-dimensional totally positive kernel quadrature are positive, and that all are positive for locally optimal node sets. Those implications neither fix the sign of the remaining central weight nor establish the unique shape-parameter crossing for a prescribed symmetric node set. Karvonen and Särkkä [3] analyze Gaussian integration measures and scaled Gauss–Hermite centers, unlike the bounded uniform measure and freely placed symmetric nodes here. The fixed-node positivity frontier is therefore a separate statement. General positive quadrature constructions with oversampling or node optimization are not contradicted.

## Limitations

The proof covers only three symmetric nodes on one bounded interval, one common Gaussian shape, Lebesgue integration, and unaugmented interpolatory kernel quadrature in exact arithmetic. It does not classify asymmetric centers, kernels other than Gaussian, polynomial augmentation, floating-point sign errors in ill-conditioned flat limits, or optimal integration error. Although targeted literature and research-record searches found no statement implying the exact phase diagram, specialized unpublished or hard-to-find prior results may exist. Independent audit has not been performed.

## References

[1] J. Glaubitz and J. A. Reeger, *Towards stability results for global radial basis function based quadrature formulas*, arXiv:2301.12998v1, first public 2023-01-30. https://arxiv.org/abs/2301.12998

[2] T. Karvonen, M. Kanagawa, and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509, first public 2018-12-20; *Statistics and Computing* 29 (2019). https://arxiv.org/abs/1812.08509

[3] T. Karvonen and S. Särkkä, *Gaussian kernel quadrature at scaled Gauss–Hermite nodes*, arXiv:1803.09532, first public 2018-03-26; *BIT Numerical Mathematics* 59 (2019). https://arxiv.org/abs/1803.09532
