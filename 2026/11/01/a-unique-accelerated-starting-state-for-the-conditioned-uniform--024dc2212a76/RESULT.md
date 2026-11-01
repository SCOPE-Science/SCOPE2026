# A unique accelerated starting state for the conditioned uniform moving-average chain

## Finding

A canonical moving-average persistence model has two *exactly different* pointwise total-variation relaxation rates. Let \(a\ge1\), let the innovations be independent and uniform on \([-a,1]\), and consider the condition that every consecutive sum of innovations remains positive. The limiting conditioned (Doob-transformed) chain on \((-1,1]\), denoted by \(Q\), has transition density
\[
q(x,y)=\frac{\pi}{4}\,\mathbf 1_{\{x+y>0\}}\frac{h(y)}{h(x)},
\qquad h(x)=\sin\!\left(\frac{\pi(x+1)}4\right).
\]
Its unique invariant probability density is \(\rho(y)=h(y)^2\), independently of \(a\). Put \(u(x)=\pi(x+1)/4\), and let \(d_n(x)=\|Q^n(x,\cdot)-\rho(y)\,dy\|_{\mathrm{TV}}\). For each fixed \(x\in(-1,1]\) other than \(1/3\),
\[
d_n(x)=\frac{3\sqrt3}{4\pi}\left|\frac{\sin(3u(x))}{\sin u(x)}\right|3^{-n}
+O_x(5^{-n}).
\]
At the **unique** exceptional starting state \(x=1/3\),
\[
d_n(1/3)=\frac{5}{6\pi}\left(\sin\frac\pi5+\sin\frac{2\pi}5\right)5^{-n}
+O(7^{-n}).
\]
In particular the generic sharp base \(1/3\) is replaced by the strictly smaller base \(1/5\) exactly at that state. The entire \(L^2(\rho)\) spectrum is \(\{(-1)^m/(2m+1):m=0,1,\ldots\}\cup\{0\}\); its normalized eigenfunctions are
\[
f_m(x)=\frac{\sin((2m+1)u(x))}{\sin u(x)}.
\]
All displayed conclusions hold for every \(a\ge1\), with the same kernel and constants. The new claim is the exact two-speed pointwise mixing law and uniqueness of the accelerated state; the source literature supplies the underlying limiting conditioned chain.

## Assumptions and scope

Fix a real \(a\ge1\). Let \((X_j)_{j\ge1}\) be independent with law \(\operatorname{Unif}[-a,1]\). For fixed \(x\in(-1,1]\), first condition on \(X_1=x\), then on \(X_{j+1}+X_j>0\) for all \(j=1,\ldots,N\), and take the finite-dimensional distribution limit as \(N\to\infty\). The existence and identification of that limit with a Doob transform follow from Aurzada--Worf, Theorems 1.1--1.2 (green region). Alternatively, all claims below are standalone statements about the explicitly defined Markov kernel \(Q\). The endpoint \(-1\) is excluded because the harmonic function vanishes there. Strict versus non-strict inequality does not affect the model with continuous innovations. Total variation uses \(\|\mu-\nu\|_{\mathrm{TV}}=\tfrac12\int|d\mu-d\nu|\) for densities; the asymptotic error constants may depend on the fixed starting point.

The primary topic is discrete-time Markov-chain ergodicity, MSC 60J05. This is not a statement of uniform-in-start sharp asymptotics as \(x\downarrow-1\), or a finite-horizon conditional mixing theorem.

## Proof

**1. Exact killed spectrum.** On \(L^2([-1,1],dx)\), the sub-Markov integral operator relevant to the surviving states is
\[
(K_a g)(x)=\frac1{a+1}\int_{-x}^{1}g(y)\,dy.
\]
It is compact and self-adjoint: its symmetric integral kernel is \((a+1)^{-1}\mathbf1_{\{x+y>0\}}\). For \(m=0,1,\ldots\), set \(k_m=(2m+1)\pi/4\) and \(\phi_m(x)=\sin(k_m(x+1))\). The functions \(\phi_m\) are an orthonormal complete basis of \(L^2([-1,1])\), as the mixed Dirichlet--Neumann eigenfunctions on an interval of length two: \(\phi_m(-1)=\phi_m'(1)=0\). Direct integration, using \(\cos(2k_m)=0\), yields
\[
K_a\phi_m(x)=\frac{\cos(k_m(1-x))}{(a+1)k_m}
=\frac{4(-1)^m}{\pi(a+1)(2m+1)}\phi_m(x).
\]
Thus every nonzero eigenvalue is \(\lambda_m=4(-1)^m/[\pi(a+1)(2m+1)]\); completeness excludes any other nonzero eigenvalue. In particular the simple positive principal eigenvalue is \(\lambda_0=4/[\pi(a+1)]\) and its eigenfunction \(h=\phi_0\) is positive on \((-1,1]\).

**2. Markov chain and invariance.** The Doob kernel is \(Q(x,dy)=\lambda_0^{-1}h(y)K_a(x,dy)/h(x)\), which reduces to the stated density independent of \(a\). The equation \(K_a h=\lambda_0 h\) proves its total mass is one. Since \(\int_{-1}^1h^2\,dx=1\), the probability measure \(\rho(x)dx=h(x)^2dx\) satisfies detailed balance:
\[
\rho(x)q(x,y)=\frac\pi4 h(x)h(y)\mathbf1_{\{x+y>0\}}=
\rho(y)q(y,x).
\]
Hence it is invariant. The same spectral argument below proves uniqueness. In addition, direct two-step integration gives the independent check
\[
q^{(2)}(x,z)=\frac{\pi^2}{16}\frac{h(z)}{h(x)}(1+\min\{x,z\}),
\qquad -1<x,z\le1,
\]
where the density is with respect to Lebesgue measure.

**3. Complete \(L^2\) relaxation spectrum.** Multiplication by \(h\) is a unitary map \(U:L^2(\rho)\to L^2(dx)\), and \(UQU^{-1}=K_a/\lambda_0\). Thus the normalized eigenfunctions are \(f_m=\phi_m/h\), with eigenvalues \(\nu_m=(-1)^m/(2m+1)\); \(f_0=1\). Since \(|\nu_m|<1\) for all \(m\ge1\), constants are the only invariant \(L^2\) functions. Uniqueness holds even among invariant probabilities whose densities need not lie in \(L^2(\rho)\): the explicit two-step density is strictly positive for all interior states and outputs. If two distinct invariant probabilities existed, apply \(Q^2\) to the positive and negative parts of their nonzero signed difference. Both resulting absolutely continuous measures have strictly positive densities almost everywhere, hence overlap and strictly reduce total variation, contradicting invariance. Thus \(\rho\) is the unique invariant probability.

For each fixed \(x>-1\), the one-step density relative to \(\rho\) lies in \(L^2(\rho)\): indeed it equals \(\pi\mathbf1_{\{y>-x\}}/[4h(x)h(y)]\), whose squared \(L^2(\rho)\)-integral is finite. Expansion of that density in the \(f_m\)-basis has coefficients \(\nu_m f_m(x)\). Therefore, for every integer \(n\ge1\),
\[
\frac{dQ^n(x,\cdot)}{\rho(y)dy}(y)=1+
\sum_{m=1}^{\infty}\nu_m^n f_m(x)f_m(y)
\quad\text{in }L^2(\rho).
\]
For any fixed \(x>-1\), \(\sum_{m\ge1}\nu_m^2f_m(x)^2<\infty\). Since \(|\nu_1|=1/3\), \(|\nu_2|=1/5\), and \(|\nu_m|\le1/7\) for \(m\ge3\), the remainder beyond mode one is \(O_x(5^{-n})\) in \(L^2(\rho)\), and that beyond mode two is \(O_x(7^{-n})\). By the \(L^1\)-to-\(L^2\) inequality for a probability measure, the same bounds apply to total variation after division by two.

**4. Two leading modes.** With \(u=u(x)\in(0,\pi/2]\),
\[
f_1(x)=\frac{\sin(3u)}{\sin u}=3-4\sin^2u.
\]
It vanishes on the state space only when \(u=\pi/3\), equivalently \(x=1/3\). The first-mode contribution to total variation is \(\tfrac12|f_1(x)|3^{-n}\|f_1\|_{L^1(\rho)}\), and splitting the integral where \(\sin(3u)\) changes sign gives
\[
\|f_1\|_{L^1(\rho)}
=\frac4\pi\int_0^{\pi/2}\sin u\,|\sin(3u)|\,du
=\frac{3\sqrt3}{2\pi}.
\]
At \(x=1/3\), the first mode disappears identically and
\[
f_2(1/3)=\frac{\sin(5\pi/3)}{\sin(\pi/3)}=-1,
\qquad
\|f_2\|_{L^1(\rho)}=\frac4\pi\int_0^{\pi/2}\sin u\,|\sin(5u)|\,du
=\frac5{3\pi}\left(\sin\frac\pi5+\sin\frac{2\pi}5\right).
\]
Splitting at \(u=\pi/5\) and \(u=2\pi/5\) proves the latter elementary integral. Taking the absolute value inside the \(L^1(\rho)\) integral and bounding the other modes using the preceding step gives both asymptotic formulas. Their positive leading coefficients certify the sharp bases and the uniqueness of the accelerated starting point. \(\square\)

## Verification

Run `python3 checker.py` using only the Python standard library. Its output is recorded in `checker_output.txt`. The program independently checks the first twelve killed eigenpairs on eight starting values, finite orthogonality and normalization identities, transition normalization, detailed balance, the direct two-step kernel, modal regressions, and the two sign-resolved absolute-mode constants. It also compares finite truncations with the stated limiting leading coefficients. All 233 finite checks pass. The infinite spectral completeness, analytic remainder bounds and unique-exception theorem are proved above, not inferred from finite samples.

## Relationship to prior work

Aurzada and Worf (arXiv:2606.01832v1, publicly submitted June 1, 2026) identify the limiting conditioned Markov chain and its Doob kernel in all non-expanding parameter regimes. They explicitly describe the principal harmonic function and persistence exponent; their stationary-density remark specifies a product of left and right eigenfunctions, but their results do not state a pointwise sharp total-variation relaxation expansion or an exceptional state. Aurzada and Raschel (arXiv:2507.04427) determine persistence generating functions, not these conditioned-chain mixing asymptotics. General exponential-ergodicity theorems for quasi-stationary \(Q\)-processes give qualitative or bounded rates, without determining the present sharp bases and constants. This result relies on the established kernel but additionally resolves its complete relaxation spectrum and a unique cancellation of the slowest nonconstant mode.

The spectrum can also be understood through classical mixed-boundary Sturm--Liouville theory, so the claim is not that sine eigenfunctions or spectral expansion are themselves new. The specific two-speed sharp total-variation laws are the assessed contribution.

## Limitations

The result addresses a fixed starting state in \((-1,1]\) and integer time \(n\to\infty\), with \(a\ge1\) and the coefficient of the neighboring innovation equal to plus one. It is not a uniform-in-start estimate near the excluded endpoint \(-1\), nor a theorem for arbitrary innovation distributions or general coupling parameters. Finite verification cannot establish spectral completeness or novelty. The priority assessment is qualified by the possibility of older implicit formulas for the same kernel in work on alternating permutations and quasi-stationary processes; an independent literature audit has not been performed.

## References

1. F. Aurzada and V. Worf, *MA(1) processes with uniform innovations conditioned to stay positive in the non-expanding regime*, arXiv:2606.01832v1 (2026), https://arxiv.org/abs/2606.01832, especially Theorems 1.1--1.2, Remarks 1--2 and 4, and the green-region argument.
2. F. Aurzada and K. Raschel, *Persistence probabilities for MA(1) sequences with uniform innovations*, arXiv:2507.04427v1 (2025), https://arxiv.org/abs/2507.04427, especially the introductory theorems, persistence generating functions, and references.
3. N. Champagnat and D. Villemonais, *Exponential convergence to quasi-stationary distribution and Q-process*, Probab. Theory Relat. Fields 164 (2016), 243--283, https://doi.org/10.1007/s00440-014-0611-7, general comparison for ergodicity rather than exact pointwise spectral rates.
