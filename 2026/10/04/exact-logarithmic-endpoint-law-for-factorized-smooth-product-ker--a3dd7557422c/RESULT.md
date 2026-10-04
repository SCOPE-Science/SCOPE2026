# Exact logarithmic endpoint law for factorized smooth product kernels

## Finding

Let \(n,m\ge2\). For \(i=1,2\), set \(d_1=n\) and \(d_2=m\), and let
\[
\Omega_i\in C^1(S^{d_i-1})
\]
be real-valued, nonzero, and satisfy
\[
\int_{S^{d_i-1}}\Omega_i\,d\sigma=0.
\]
Define
\[
K_i(x)=\frac{\Omega_i(x/|x|)}{|x|^{d_i}},
\qquad
\Omega(\theta,\phi)=\Omega_1(\theta)\Omega_2(\phi).
\]
Let \(T_\Omega\) be the product principal-value singular integral with kernel
\[
K(x,y)=K_1(x)K_2(y).
\]

Suppose \(f_i\) is real-valued, compactly supported, belongs to
\[
L^1(\mathbb R^{d_i})\cap L^p(\mathbb R^{d_i})
\]
for some \(1<p<\infty\), and has nonzero mass
\[
M_i=\int_{\mathbb R^{d_i}} f_i.
\]
For \(f=f_1\otimes f_2\),
\[
\lim_{\lambda\downarrow0}
\frac{\lambda}{\log(1/\lambda)}
\left|\left\{(x,y)\in\mathbb R^n\times\mathbb R^m:
|T_\Omega f(x,y)|>\lambda\right\}\right|
=
C_{\Omega,f},
\]
where
\[
C_{\Omega,f}
=
\frac{|M_1M_2|}{nm}
\left(\int_{S^{n-1}}|\Omega_1(\theta)|\,d\sigma(\theta)\right)
\left(\int_{S^{m-1}}|\Omega_2(\phi)|\,d\sigma(\phi)\right).
\]

Hence the logarithm in the global \(L\log L\) endpoint scale is already unavoidable for smooth factorized kernels, and its leading coefficient is determined exactly by the two masses and the spherical \(L^1\) sizes of the angular factors.

For the coordinate Riesz factors
\[
\Omega_1(\theta)=\theta_1,\qquad
\Omega_2(\phi)=\phi_1
\]
and the tensor input
\[
f=\mathbf 1_{B^n}\otimes\mathbf 1_{B^m},
\]
the coefficient is
\[
C_{\Omega,f}
=
\frac{4V_nV_{n-1}V_mV_{m-1}}{nm},
\]
where \(V_d=|B^d|\).

## Assumptions and scope

The principal values are the standard one-parameter Calderón--Zygmund principal values in each factor. For a tensor input and a factorized kernel, the doubly truncated operator factors:
\[
T_{\Omega,\varepsilon_1,\varepsilon_2}(f_1\otimes f_2)(x,y)
=
T_{\Omega_1,\varepsilon_1}f_1(x)\,
T_{\Omega_2,\varepsilon_2}f_2(y).
\]
Passing to the principal-value limit gives
\[
T_\Omega(f_1\otimes f_2)(x,y)
=
h_1(x)h_2(y)
\]
almost everywhere, where
\[
h_i=T_{\Omega_i}f_i.
\]

The \(C^1\) angular assumption is used only to obtain a uniform first-order far-field expansion. Compact support supplies a finite first moment. The \(L^p\) assumption with \(p>1\) supplies standard Calderón--Zygmund \(L^p\) control, which is used only to show that high-amplitude pieces contribute lower order \(O(\lambda^{-1})\) terms.

The theorem does not cover nonfactorized angular kernels, zero-mass inputs, or the next asymptotic term.

## Proof

First consider one factor in dimension \(d\). Write
\[
K(x)=\frac{\Omega(x/|x|)}{|x|^d},
\qquad
h=K*f
\]
in the principal-value sense, with \(f\) compactly supported and
\[
M=\int_{\mathbb R^d}f\ne0.
\]
Because \(K\) is homogeneous of degree \(-d\) and \(C^1\) away from the origin, for \(|x|\) larger than twice the support radius,
\[
h(x)=M K(x)+O(|x|^{-d-1}),
\]
uniformly in the direction \(x/|x|\). Thus, for every fixed \(y\ne0\),
\[
\frac{h(t^{-1/d}y)}{t}
\longrightarrow
M\frac{\Omega(y/|y|)}{|y|^d}
\qquad(t\downarrow0).
\]

Let
\[
F_h(t)=|\{x:|h(x)|>t\}|.
\]
The same far-field estimate gives
\[
|h(x)|\le C|x|^{-d}
\]
outside a fixed ball. Therefore, after the scaling \(x=t^{-1/d}y\), the rescaled superlevel sets are uniformly contained in one fixed ball in the \(y\)-variable. Their indicator functions converge almost everywhere to the indicator of
\[
E=
\left\{
y:
|M|\frac{|\Omega(y/|y|)|}{|y|^d}>1
\right\}.
\]
The boundary of \(E\) has Lebesgue measure zero: on every ray with \(\Omega\ne0\) it contains at most one radius, and directions where \(\Omega=0\) contribute no radial interval. Dominated convergence therefore yields
\[
\lim_{t\downarrow0}tF_h(t)=|E|.
\]
Polar coordinates give
\[
|E|
=
\frac{|M|}{d}\int_{S^{d-1}}|\Omega(\theta)|\,d\sigma(\theta).
\]
Define this constant by
\[
A(h)=
\frac{|M|}{d}\int_{S^{d-1}}|\Omega|\,d\sigma.
\]
Consequently
\[
F_h(t)\sim\frac{A(h)}{t}
\qquad(t\downarrow0).
\]

We now use a product-tail lemma. Suppose nonnegative measurable functions \(a\) and \(b\) satisfy
\[
|\{a>t\}|\sim\frac{A}{t},
\qquad
|\{b>t\}|\sim\frac{B}{t}
\qquad(t\downarrow0),
\]
with \(A,B>0\), and suppose that for every fixed \(t_0>0\),
\[
\int_{\{a>t_0\}}a<\infty,
\qquad
\int_{\{b>t_0\}}b<\infty.
\]
Then
\[
|\{ab>\lambda\}|
\sim
\frac{AB}{\lambda}\log\frac1\lambda.
\]

To prove the lemma, fix \(t_0>0\) in the tail regime. Contributions where \(a>t_0\) or \(b>t_0\) are \(O(\lambda^{-1})\), by the high-level integrability assumptions and the bounds
\[
|\{b>s\}|\le \frac{C}{s},
\qquad
|\{a>s\}|\le \frac{C}{s}
\]
for sufficiently small \(s\). On the main region, where both variables are below \(t_0\), one integrates the tail of \(b\) at the threshold \(\lambda/a\). For every \(\varepsilon>0\), once \(t_0\) is small enough,
\[
\frac{(1-\varepsilon)B}{s}
\le
|\{b>s\}|
\le
\frac{(1+\varepsilon)B}{s}
\]
throughout the relevant low-level range. Hence the main contribution is squeezed between
\[
\frac{(1-\varepsilon)B}{\lambda}
\int_{\lambda/t_0<a\le t_0}a
+O(\lambda^{-1})
\]
and the analogous expression with \(1+\varepsilon\).

Layer-cake integration and
\[
|\{a>s\}|\sim\frac{A}{s}
\]
give
\[
\int_{\lambda/t_0<a\le t_0}a
=
A\log\frac1\lambda+o\!\left(\log\frac1\lambda\right).
\]
Dividing by \(\lambda^{-1}\log(1/\lambda)\), taking \(\lambda\downarrow0\), and then \(\varepsilon\downarrow0\) proves the product-tail lemma.

Apply the lemma to
\[
a=|h_1|,\qquad b=|h_2|.
\]
The standard \(L^p\) boundedness of the smooth one-parameter singular integrals gives
\[
h_i\in L^p,
\]
so
\[
\int_{\{|h_i|>t_0\}}|h_i|
\le
t_0^{1-p}\|h_i\|_p^p<\infty.
\]
The one-factor calculation gives
\[
A(h_1)
=
\frac{|M_1|}{n}\int_{S^{n-1}}|\Omega_1|\,d\sigma,
\qquad
A(h_2)
=
\frac{|M_2|}{m}\int_{S^{m-1}}|\Omega_2|\,d\sigma.
\]
Therefore
\[
|\{|T_\Omega f|>\lambda\}|
\sim
\frac{A(h_1)A(h_2)}{\lambda}\log\frac1\lambda,
\]
which is the stated formula.

For the coordinate Riesz example,
\[
\int_{S^{d-1}}|\theta_1|\,d\sigma(\theta)=2V_{d-1}.
\]
Taking \(M_1=V_n\) and \(M_2=V_m\) yields
\[
A(h_1)A(h_2)
=
\frac{4V_nV_{n-1}V_mV_{m-1}}{nm}.
\]

## Verification

The proof has three independent checks.

First, the far-field coefficient is forced by homogeneity:
\[
K(r\theta)=r^{-d}\Omega(\theta),
\]
and compact support gives
\[
K(x-z)=K(x)+O(|x|^{-d-1})
\]
uniformly for \(z\) in the support of the input.

Second, the one-factor tail coefficient can be recomputed directly in polar coordinates:
\[
\left|
\left\{
y:
|M||\Omega(y/|y|)|>|y|^d
\right\}
\right|
=
\frac{|M|}{d}\int_{S^{d-1}}|\Omega|\,d\sigma.
\]

Third, the logarithmic product law is the exact regular-variation convolution of two tails of index one. High-amplitude pieces are only \(O(\lambda^{-1})\), while the middle range contributes
\[
\frac{AB}{\lambda}\int_{\lambda/t_0}^{t_0}\frac{ds}{s},
\]
which has the unique leading term
\[
\frac{AB}{\lambda}\log\frac1\lambda.
\]

No finite numerical experiment is used to justify an infinite-domain or limiting statement.

## Relationship to prior work

Chen, Fan, Hu, and Wang prove in their 2026 preprint that rough product singular integrals are bounded on \(L^p(\mathbb R^n\times\mathbb R^m)\) for every \(1<p<\infty\) when the angular kernel belongs to product \(H^1\) and satisfies separate cancellation. Every smooth factorized kernel in the present theorem lies inside that class. Their theorem stops at \(p>1\) and does not state an endpoint distribution asymptotic.

Cowling, Lee, Li, and Pipher prove global hyperweak \(L\log L\) bounds for double Riesz transforms and more general product operators. Their introduction also recalls that product singular integrals are not of weak type \((1,1)\) and gives the classical double-Hilbert-transform unit-square example with distribution comparable to
\[
\frac{\log(e+1/\lambda)}{\lambda}
\]
at small \(\lambda\). That comparison establishes the logarithmic scale but not an exact leading coefficient.

The present result identifies the exact coefficient for an infinite family of smooth factorized kernels and compact tensor inputs. It is compatible with, but not implied by, the known \(L\log L\) upper bounds or the older comparability example.

## Limitations

The theorem requires factorization of both the kernel and the input. For a general product angular function \(\Omega(\theta,\phi)\), the far-field geometry is not a product of two one-parameter tails, so the argument does not apply directly.

The masses \(M_1\) and \(M_2\) must be nonzero. If either mass vanishes, the leading homogeneous term cancels and the decay order changes; no claim about that regime is made here.

The result determines the leading small-\(\lambda\) coefficient only. It does not give a second-order term, an optimal universal endpoint constant over all kernels, or a converse characterization.

## References

1. J. Chen, D. Fan, W. Hu, and M. Wang, *Rough Singular Integrals and Marcinkiewicz Integrals on Product Spaces, with \(H^1\) Characterizations on Product Spheres*, arXiv:2609.33696v1, 2026.
2. M. G. Cowling, M.-Y. Lee, J. Li, and J. Pipher, *An endpoint estimate for product singular integral operators on stratified Lie groups*, Canadian Journal of Mathematics, published online 27 January 2025, DOI 10.4153/S0008414X25000057.
3. R. Fefferman, classical local \(L\log L\) endpoint estimate for product Calderón--Zygmund operators, as cited and summarized in Reference 2.
