# Sharp moment-integrability phases for Gaussian Nyström compression of rotational Runge–Kutta steps

## Finding

The exact flow of a rank-one positive-semidefinite matrix differential equation stays rank-one and positive semidefinite, but compressing a conventional explicit Runge–Kutta endpoint with an **unoversampled, one-column Gaussian Nyström sketch** can produce a true one-step error with an infinite mean for arbitrarily small step sizes. Its moment integrability is decided exactly by the method's scalar imaginary-axis stability polynomial, and in the unstable phase the error has an explicit inverse-linear tail.

Put \(P_p(z)=\sum_{k=0}^p z^k/k!\), \(d_p(h)=[1-|P_p(2ih)|^2]/4\), and \(A(h)=e^{hJ}A_0e^{-hJ}\). For \(g\sim N(0,I_2)\) define the tied-sketch one-column Nyström output and true step error by
\[
 \mathcal N_{\mathrm{tie}}(Z_p;g)=\frac{(Z_pg)(Z_pg)^{\mathsf T}}{g^{\mathsf T}Z_pg},\qquad
 W_{\mathrm{tie}}=\|\mathcal N_{\mathrm{tie}}(Z_p;g)-A(h)\|_F.
\]
Denominators vanish with probability zero whenever \(Z_p\ne0\). For every integer \(p\ge1\), every \(h>0\), and every real \(q>0\):
\[
\begin{aligned}
 d_p(h)\ge0&\quad\Longrightarrow\quad\mathbb E W_{\mathrm{tie}}^q<\infty,\\
 d_p(h)<0&\quad\Longrightarrow\quad
 \lim_{r\to\infty}r\Pr\{W_{\mathrm{tie}}>r\}=\frac{2\sqrt{-d_p(h)}}\pi,\\
 d_p(h)<0&\quad\Longrightarrow\quad
 \mathbb E W_{\mathrm{tie}}^q<\infty\ \Longleftrightarrow\ 0<q<1.
\end{aligned}
\]
In particular, the exact determinants for the four classical orders are
\[
\begin{aligned}
 d_1(h)&=-h^2, & d_2(h)&=-h^4,\\
 d_3(h)&=\frac{h^4(3-4h^2)}9,&
 d_4(h)&=\frac{h^6(2-h^2)}9.
\end{aligned}
\]
Therefore Euler and Heun/explicit midpoint have infinite mean true one-step error for every positive step; classical Kutta RK3 has all moments finite precisely when \(0<h\le\sqrt3/2\); classical RK4 has all moments finite precisely when \(0<h\le\sqrt2\). For larger steps each of the latter has infinite first moment, even though the exact flow remains rank-one.

More generally, writing \(p=2m+1\) or \(p=2m\), the first nonzero small-step coefficient is respectively
\[
\begin{aligned}
 d_{2m+1}(h)&=\frac{(-1)^{m+1}(2h)^{2m+2}}{2(2m+2)!}+O(h^{2m+4}),\\
 d_{2m}(h)&=\frac{(-1)^m(2h)^{2m+2}}{2(2m+2)(2m)!}+O(h^{2m+4}).
\end{aligned}
\]
For all sufficiently small \(h>0\), tied-sketch moments are finite at every order when \(p\equiv0,3\pmod4\), but first moments diverge when \(p\equiv1,2\pmod4\). For \(p>4\) these are Taylor endpoint claims, not assertions about a \(p\)-stage Runge–Kutta tableau.

For comparison, use **independent** \(u,v\sim N(0,I_2)\) and the one-column generalized Nyström output
\[
 \mathcal N_{\mathrm{ind}}(Z;u,v)=\frac{(Zu)(v^{\mathsf T}Z)}{v^{\mathsf T}Zu}.
\]
Whenever \(Z=Z_p(h)\) is invertible, the corresponding true error \(W_{\mathrm{ind}}\) satisfies
\[
\lim_{r\to\infty}r\Pr\{W_{\mathrm{ind}}>r\}
=\frac{2|\det Z|}\pi\mathbb E_{U\sim\mathrm{Unif}(S^1)}\frac1{\|ZU\|_2}>0,
\qquad
 \mathbb EW_{\mathrm{ind}}^q<\infty\ \Longleftrightarrow\ 0<q<1.
\]
When \(Z\) is rank one, both one-column constructions reconstruct \(Z\) almost surely; the true error is then the bounded deterministic truncation error \(\|Z-A(h)\|_F\). Thus correlation of the left and right sketches changes the integrability frontier in the positive-definite phase. The independent-sketch moment obstruction is included as a comparison with existing unoversampled sketch theory, not as a general new moment-bound claim.

## Assumptions and scope

All calculations are in exact real arithmetic; no regularization, clipping or oversampling is imposed. Let
\[
 J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
 A_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
 \mathcal L(X)=JX-XJ,\quad
 \dot A=\mathcal L(A),\quad A(0)=A_0.
\]
The solution is \(A(t)=e^{tJ}A_0e^{-tJ}\), so \(\operatorname{rank}A(t)=1\) and \(A(t)\succeq0\) at every time. The endpoint \(Z_p(h)\) is the full, uncompressed degree-\(p\) Taylor step for the matrix ODE. For \(p=1,2,3,4\), it also equals the full output of Euler, Heun (or explicit midpoint), classical Kutta RK3 and classical RK4 on this linear problem. Only the **endpoint** is compressed; there is no projection or random sketch inside individual Runge–Kutta stages. A single independent Gaussian is freshly drawn for the displayed one-step experiment, not a statement about multistep propagation.

All asymptotics in the probability tail are for \(r\to\infty\) with fixed \(p,h\); the small-step asymptotics are for fixed degree and \(h\downarrow0\). The meaning of \(\mathbb E W^q\) is the ordinary Lebesgue moment of the nonnegative random variable, allowing value \(+\infty\).

## Proof

**1. Exact endpoint and sign of its determinant.** Since \(\mathcal L\) acts as twice the rotation generator on traceless symmetric matrices,
\[
 Z_p(h)=\frac12\begin{pmatrix}1+c_p(h)&s_p(h)\\s_p(h)&1-c_p(h)\end{pmatrix},\quad
 c_p(h)+is_p(h)=P_p(2ih).
\]
A direct determinant calculation yields
\[
\operatorname{tr}Z_p=1,\qquad
 \det Z_p=\frac{1-c_p^2-s_p^2}4=d_p(h).
\]
Its two real eigenvalues sum to one. If \(d_p>0\), both are positive; if \(d_p=0\), one is zero and the other one; if \(d_p<0\), they have opposite signs. This proves the equivalence between positive-semidefinite endpoint and \(|P_p(2ih)|\le1\), the scalar imaginary-axis stability inequality. Expanding \(P_p\) for the first four degrees gives the four displayed determinant polynomials. The root cases \(h=\sqrt3/2\) and \(h=\sqrt2\) are singular **rank-one** endpoints; they are included in the finite-moment regime.

**2. Residual identity for one-column sketches.** Let \(Z\in\mathbb R^{2\times2}\) be any symmetric invertible matrix. For nonzero \(u,v\in\mathbb R^2\) with \(v^{\mathsf T}Zu\ne0\), direct expansion of the \(2\times2\) determinant identity gives
\[
 \left\|Z-\frac{(Zu)(v^{\mathsf T}Z)}{v^{\mathsf T}Zu}\right\|_F
 =\frac{|\det Z|\,\|u\|_2\|v\|_2}{|v^{\mathsf T}Zu|}.
\tag{1}
\]
Indeed, the numerator after multiplying by \(v^{\mathsf T}Zu\) is the outer product of perpendiculars to \(u,v\), multiplied by \(\det Z\). With \(u=v=g\), (1) becomes
\[
 \|Z-\mathcal N_{\mathrm{tie}}(Z;g)\|_F
 =\frac{|\det Z|\,\|g\|_2^2}{|g^{\mathsf T}Zg|}.
\tag{2}
\]
The square matrix \(Z\) has rank one when \(\det Z=0\); then either one-column formula equals \(Z\) almost surely (by rank-one factorization). When \(Z\succ0\), the tied-sketch residual is the positive-semidefinite matrix \(Z^{1/2}(I-P)Z^{1/2}\) for a rank-one orthogonal projector \(P\), and \(0\preceq Z-\mathcal N_{\mathrm{tie}}\preceq Z\); hence it is uniformly bounded.

**3. Sharp tail in the indefinite phase.** Suppose \(\det Z=-d<0\). Diagonalize \(Z\) with eigenvalues \(\alpha>0> -\beta\), so \(d=\alpha\beta\). A standard real Gaussian has a direction uniformly distributed on \(S^1\) and independent of its radius. Writing that direction as \((\cos\theta,\sin\theta)\), (2) becomes
\[
 H(\theta)=\frac{d}{|\alpha\cos^2\theta-\beta\sin^2\theta|}.
\]
The angular denominator has four simple zeros on a full circle; the magnitude of its derivative at each zero is exactly \(2\sqrt d\). Therefore the angular measure of \(\{H>r\}\) is
\[
 4\left(\frac{2d/r}{2\sqrt d}+o(r^{-1})\right)
 =\frac{4\sqrt d}r+o(r^{-1}).
\]
Dividing by the circle length \(2\pi\) yields
\[
 \lim_{r\to\infty} r\Pr\{H>r\}=\frac{2\sqrt d}\pi.
\]
The true error differs from \(H=\|Z-\mathcal N\|_F\) by at most the deterministic \(\|Z-A(h)\|_F\), by the reverse triangle inequality; hence it has the **same** sharp tail coefficient. For nonnegative \(W\), the layer-cake identity \(\mathbb EW^q=q\int_0^\infty r^{q-1}\Pr\{W>r\}\,dr\) gives the exact moment threshold \(q<1\). This establishes every tied-sketch assertion.

**4. Independent sketches.** In (1) take independent standard Gaussians \(u,v\); their radii cancel. Conditional on \(U=u/\|u\|\), the relative angle of \(V=v/\|v\|\) with \(ZU\) is uniform. Thus for sufficiently large \(r\),
\[
 \Pr\!\left\{\|Z-\mathcal N_{\mathrm{ind}}\|_F>r\mid U\right\}
 =\frac2\pi\arcsin\left(\frac{|\det Z|}{r\|ZU\|_2}\right).
\]
For invertible \(Z\), \(\|ZU\|\ge\sigma_{\min}(Z)>0\); dominated convergence yields the displayed strictly positive tail coefficient. The triangle-inequality and layer-cake arguments from Step 3 apply unchanged. For rank-one \(Z\), the random reconstruction is exact almost surely.

**5. All-order small-step sign.** Differentiating \(P_p(it)\) gives
\[
 \frac{d}{dt}|P_p(it)|^2
 =-\frac{2t^p}{p!}\Re\!\left(i^{p+1}\overline{P_p(it)}\right).
\]
For \(p=2m+1\), the leading real term of the factor in parentheses is \((-1)^{m+1}\). Integrating from zero and dividing by negative four gives
\[
 d_p(h)=\frac{(-1)^{m+1}(2h)^{p+1}}{2(p+1)!}+O(h^{p+3}).
\]
For \(p=2m\), its first nonzero real term is \((-1)^m t\), yielding
\[
 d_p(h)=\frac{(-1)^m(2h)^{p+2}}{2(p+2)p!}+O(h^{p+4}).
\]
Each coefficient is nonzero. The determinant sign therefore follows the stated period-four dichotomy for all sufficiently small positive steps, and Step 3 immediately converts it to moment-integrability regimes. This completes the proof.

## Verification

Run `python3 verify.py` from the directory containing the delivered files. The script needs only Python's standard library. It checks exactly, with rational arithmetic, the matrix Taylor identity for degrees 1–9 at three rational step sizes, the determinant expansions for degrees 1–14 and their leading parity, the determinant expressions for degrees 1–4, and 2-by-2 Nyström residual identities over a set of rational probes. High-threshold angular calculations independently check the leading constant of the tied-sketch tail in four indefinite cases, and numerical angular quadrature checks the independent-sketch leading constant on a positive-definite RK4 endpoint. The observed result is:

`VERIFY_OK 252 exact rational and asymptotic checks; independent-tail constant 0.00886391953524`

These finite checks are diagnostics. The results for all orders, all steps and all positive moment exponents rest on the analytical proof above, not on sampled tests. Floating calculations in the tail tests are not asserted to be formal certificates.

## Relationship to prior work

Lam, Ceruti and Kressner (arXiv:2409.06384v1, publicly posted 2024-09-10), introduce randomized low-rank Runge–Kutta schemes using generalized Nyström sketches and prove moment bounds under independent, **oversampled** Gaussian sketches. Their methods include stagewise compression, which the present exact one-step endpoint experiment does **not** implement. Their source formula for a generalized Nyström projection and their oversampling/moment requirements are used as motivation; their theoretical conclusions are not contradicted.

Nakatsukasa and Park (arXiv:2212.01127v1, 2022-12-02) already show that plain Nyström applied to symmetric indefinite matrices can be arbitrarily unstable and introduce safer alternatives. Classical explicit Runge–Kutta imaginary-axis stability polynomials are also known. Neither of those observations is claimed as new here. The result concerns the **precise Gaussian one-step probability tails and moment thresholds** obtained when a rank-preserving rotational matrix flow is passed through an endpoint RK/Taylor polynomial, including the sharp step thresholds, the small-step period-four behavior and the contrast with independently sketched generalized Nyström. Existing results for independent unoversampled sketches also motivate, but do not by themselves settle, the tied-sketch phase boundary.

## Limitations

This theorem treats a \(2\times2\) rank-one rotational flow and exact arithmetic, with a single unoversampled rank-one Nyström compression of the **full uncompressed endpoint**. It does not classify the original randomized stagewise integrator, its global repeated-step error, finite-precision safeguards, regularized or oversampled sketches, general nonlinear ODEs, or higher-dimensional matrices. For \(p>4\), the endpoints are polynomial Taylor steps rather than identified specific RK tableaus. The inverse-linear tail occurs at fixed positive step size: it does not say the sampled error is large with high probability at small step size. Prior generic Nyström instability and imaginary-axis Runge–Kutta stability are acknowledged; a same-result theorem under different stochastic terminology remains a literature-overlap risk.

## References

1. H. Y. Lam, G. Ceruti and D. Kressner, *Randomized low-rank Runge-Kutta methods*, arXiv:2409.06384v1, 2024-09-10, https://arxiv.org/html/2409.06384v1. In particular, Sections 2.3, 2.4 and 3 and the source's generalized Nyström formula (8).
2. Y. Nakatsukasa and T. Park, *Randomized low-rank approximation for symmetric indefinite matrices*, arXiv:2212.01127v1, 2022-12-02, https://arxiv.org/pdf/2212.01127v1. In particular, Introduction, equations (1.2)–(1.4) and the discussion of unstable indefinite Nyström compression.
