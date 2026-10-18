# Pareto-one tails and singular ridge risk of Gaussian-noisy scalar Anderson acceleration

## Finding

Ordinary scalar depth-one Anderson acceleration applied to independently Gaussian-noisy evaluations of even a strict affine contraction produces an exact Pareto-one absolute tail and has no finite first absolute moment. A ridge penalty restores finite moments at each fixed regularization strength, but the second moment diverges at an exact inverse-square-root rate as the penalty vanishes.

**Theorem.** Fix \(-1<a<1\), \(x\in\mathbb R\), and \(\sigma>0\). Define \(h=(a-2)^2+1\), \(d_0=(a-1)^2x\), and
\[
p_0=\frac{\exp[-d_0^2/(2\sigma^2h)]}{\sigma\sqrt{2\pi h}},\qquad m=\frac{(a-1)(3-a)x}{h},\qquad v=\frac{\sigma^2}{h}.
\]
For the one-step model specified below, the unregularized accelerated output \(X\) satisfies
\[
\lim_{t\to\infty} t\Pr(|X|>t)=C:=2p_0(m^2+v)>0,
\qquad
\mathbb E|X|^q<\infty\ \Longleftrightarrow\ 0<q<1.
\]
For ridge regularization strength \(\lambda>0\), every positive moment of the output \(X_\lambda\) is finite, while
\[
\lim_{\lambda\downarrow0}\sqrt\lambda\,\mathbb E[X_\lambda^2]
=K:=\frac\pi2 p_0(m^4+6m^2v+3v^2)>0.
\]
In particular, for the exact contraction \(g\equiv0\), initial state \(x=0\), and \(\sigma=1\), the constants are \(C=2/(\sqrt{2\pi}\,5^{3/2})\) and \(K=3\pi/(2\sqrt{2\pi}\,5^{5/2})\).

## Assumptions and scope

A scalar fixed-point function is \(g(z)=az\) with \(-1<a<1\) and fixed starting value \(x_0=x\). Each call uses a fresh independent standard Gaussian, \(Z_0,Z_1\). Compute \(Y_0=ax+\sigma Z_0\), set \(x_1=Y_0\), and compute \(Y_1=ax_1+\sigma Z_1\). Set \(F_0=Y_0-x_0\), \(F_1=Y_1-x_1\), and \(D=F_1-F_0\). Undamped depth-one Anderson acceleration minimizes \(|F_1-\alpha D|^2\), giving \(\alpha=F_1/D\) for the almost-sure event \(D\ne0\); the new state is \(X=Y_1-\alpha(Y_1-Y_0)\). The penalized least-squares version minimizes \(|F_1-\alpha D|^2+\lambda\alpha^2\), for \(\lambda>0\), giving \(\alpha_\lambda=F_1D/(D^2+\lambda)\) and \(X_\lambda=Y_1-\alpha_\lambda(Y_1-Y_0)\). Noise is not reused between oracle calls. All expectations include both oracle errors.

## Proof

Because \(Y_1-Y_0=F_1\) and \(F_1=F_0+D\), direct elimination gives
\[
X=Y_1-\frac{F_1^2}{D}=x-\frac{F_0^2}{D},
\qquad
X_\lambda=x+\frac{\lambda(2F_0+D)-F_0^2D}{D^2+\lambda}.
\]
The random vector \((F_0,D)\) is jointly Gaussian, with
\[
F_0=(a-1)x+\sigma Z_0,
\quad D=(a-1)^2x+\sigma[(a-2)Z_0+Z_1].
\]
Thus \(D\) has mean \(d_0\), variance \(\sigma^2h\), and density \(p_D(0)=p_0\) at zero. Gaussian conditioning yields \(F_0\mid(D=0)\sim N(m,v)\), with \(m,v\) as above. In particular \(v>0\) ensures \(\mathbb E[F_0^2\mid D=0]=m^2+v>0\).

For any \(t>|x|\), conditioning on \(F_0=u\) gives the **exact** equivalence
\[
|X|>t\ \Longleftrightarrow\
-\frac{u^2}{t-x}<D<0\quad\text{or}\quad0<D<\frac{u^2}{t+x}.
\]
The conditional density \(p_{D\mid F_0=u}\) is Gaussian with variance \(\sigma^2\), hence continuous and bounded uniformly by \((\sigma\sqrt{2\pi})^{-1}\). Multiplying the conditional probability by \(t\) and letting \(t\to\infty\) gives \(2u^2p_{D\mid F_0=u}(0)\). For \(t>2|x|\) the product is dominated by \(4u^2/(\sigma\sqrt{2\pi})\), which is integrable. Dominated convergence therefore gives
\[
\lim_{t\to\infty}t\Pr(|X|>t)
=2\mathbb E[F_0^2p_{D\mid F_0}(0)]
=2p_D(0)\mathbb E[F_0^2\mid D=0]=2p_0(m^2+v).
\]
The tail-integral formula \(\mathbb E|X|^q=q\int_0^\infty t^{q-1}\Pr(|X|>t)\,dt\) proves finiteness exactly for \(0<q<1\), including logarithmic divergence at \(q=1\).

For \(\lambda>0\), the displayed rational expression for \(X_\lambda\) has no real pole; \(|D/(D^2+\lambda)|\le(2\sqrt\lambda)^{-1}\) and \(\lambda/(D^2+\lambda)\le1\), so it is bounded by a constant times a polynomial in \(|F_0|,|D|\), which has moments of every order. Split
\[
X_\lambda=U_\lambda+V_\lambda,
\quad U_\lambda=-\frac{F_0^2D}{D^2+\lambda},
\quad V_\lambda=x+\frac{\lambda(2F_0+D)}{D^2+\lambda}.
\]
The family \(V_\lambda\) is uniformly bounded in \(L^2\). Let \(M_4(d)=\mathbb E[F_0^4\mid D=d]\). Gaussian conditioning makes \(M_4(d)\) a nonnegative quartic polynomial and \(M_4(0)=m^4+6m^2v+3v^2\). The inverse-square-root rescaling \(d=\sqrt\lambda s\) yields
\[
\sqrt\lambda\,\mathbb E U_\lambda^2
=\int_{\mathbb R}\frac{s^2}{(1+s^2)^2}\,p_D(\sqrt\lambda s)M_4(\sqrt\lambda s)\,ds
\longrightarrow \frac\pi2 p_0M_4(0).
\]
Indeed the product \(p_D(d)M_4(d)\) is bounded for all real \(d\); thus dominated convergence applies, with \(\int_\mathbb R s^2(1+s^2)^{-2}\,ds=\pi/2\). Finally Cauchy–Schwarz and the uniform \(L^2\) bound on \(V_\lambda\) give \(\sqrt\lambda\,|\mathbb E(U_\lambda V_\lambda)|\to0\), and \(\sqrt\lambda\,\mathbb E V_\lambda^2\to0\). This proves the claimed limit for \(\mathbb E X_\lambda^2\). Strict positivity follows from \(p_0,v>0\).

## Verification

The standalone `verify.py` reproduces all direct scalar Anderson and ridge identities for independent Gaussian draws, evaluates Gaussian conditional integrals by independent quadrature, checks that finite-threshold tails approach \(C/t\), and checks that the rescaled ridge second moments approach \(K\) on four parameter choices. Running `python verify.py` with NumPy and SciPy completed 3,636 finite algebraic and numerical checks. The program is **not** an infinite-moment or limiting-distribution certificate; those follow from the analytic proof above. The checks are performed on a real one-step stochastic oracle, without an implicit shared-noise assumption.

## Relationship to prior work

Adler, He, Hu and Lefebvre (2026, arXiv:2609.13091v1, first released 2026-09-11) provide deterministic linear fixed-point error-propagation and a two-grid interpretation for Anderson acceleration and nonlinear GMRES. Their depth-one formulation supplies the algorithmic motivation, not the present noisy one-step law. Scalar depth-one Anderson acceleration also has an elementary rational extrapolation form closely related to classical Aitken delta-squared; the identity itself is not asserted as novel. Toth and collaborators (2017, DOI 10.1137/16M1080677) specifically study Anderson acceleration with inaccurate map evaluations and include stochastic errors with unbounded support; the accessible abstract provides no exact tail law or vanishing-ridge moment constant, but the unavailable full text is a remaining possible overlap. Lupo Pasini and Laiu (2024, DOI 10.1002/nla.2562) address approximate calculations, with only the accessible summary inspected. The proposed contribution is the explicit joint-Gaussian tail constant, complete absolute-moment threshold, and exact singular ridge-risk coefficient for the specified one-step model, not general assertions that noisy acceleration is unstable or that a rational Gaussian ratio is heavy-tailed.

## Limitations

The distributional statements hold for one undamped scalar depth-one step using two fresh independent Gaussian map evaluations and an affine contraction; they do not address higher-depth or multidimensional Anderson acceleration, bounded-noise or shared-noise oracles, safeguard/restart policies, long-run iteration convergence, or adaptive regularization. The alternative classical Aitken representation may make parts of the singularity mechanism familiar. Earlier inaccurate-evaluation research could not be fully inspected, and unindexed equivalent formulations remain a bibliographic risk. Numerical quadrature and finite simulations do not establish infinite-support integrability conclusions by themselves. 
## References

1. J. Adler, Y. He, X. Hu, and S. Lefebvre, *A Unified Two-Grid Framework for Anderson Acceleration and Nonlinear GMRES*, arXiv:2609.13091v1 (2026-09-11), https://arxiv.org/abs/2609.13091.
2. A. Toth, J. A. Ellis, T. Evans, S. Hamilton, C. T. Kelley, R. Pawlowski, and S. Slattery, *Local Improvement Results for Anderson Acceleration with Inaccurate Function Evaluations*, SIAM Journal on Scientific Computing 39 (2017), DOI:10.1137/16M1080677.
3. M. Lupo Pasini and M. P. Laiu, *Anderson acceleration with approximate calculations*, Numerical Linear Algebra with Applications (2024), DOI:10.1002/nla.2562.
4. A. C. Aitken, *On Bernoulli's Numerical Solution of Algebraic Equations*, Proceedings of the Royal Society of Edinburgh (1926).
