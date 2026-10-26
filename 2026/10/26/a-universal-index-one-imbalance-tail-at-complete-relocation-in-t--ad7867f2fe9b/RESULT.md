# A universal index-one imbalance tail at complete relocation in the three-site monkey walk

## Finding

Consider the following one-dimensional reinforced walk, begun at site \(0\) at time \(0\). At a site \(0\), independently at each update it moves to either neighbour with probability \(a/2\) each, or relocates with probability \(1-a\) to the position at a uniformly sampled past integer time. At either nonzero site it necessarily relocates in this manner. Fix \(0<a<1\). Set \(N_j(n)=\sum_{k=0}^{n}\mathbf1_{\{X_k=j\}}\) and \(p_{j,n}=N_j(n)/(n+1)\), for \(j\in\{-1,0,1\}\).

Then, on the original walk's probability space, almost surely,
\[
(\log n)p_{0,n}\longrightarrow\frac1a,\qquad
p_{1,n},p_{-1,n}\longrightarrow\frac12,
\qquad (\log n)(p_{1,n}-p_{-1,n})\longrightarrow Q_a.
\]
The random variable \(Q_a\) is nondegenerate and symmetric. A joint transform that **exactly identifies its law** is as follows: on a branching-process coupling, \(Q_a=D/(aW)\), with \(W\sim\operatorname{Exp}(1)\), and for every \(s\ge0\) and real \(t\),
\[
\mathbb E\bigl[e^{-sW+itD}\bigr]
=\frac{1-a+a/(1+t^2)}{1+s+a t\arctan t}.
\tag{1}
\]
In particular, for every \(a\in(0,1)\),
\[
\boxed{\lim_{x\to\infty}x\,\mathbb P(|Q_a|>x)=1.}
\tag{2}
\]
Thus \(\mathbb E|Q_a|=\infty\), although each finite-time empirical imbalance is bounded. The exact index-one tail coefficient is **independent of** \(a\).

## Assumptions and scope

This result concerns the strict endpoint in which every update away from the origin is a relocation, rather than an ordinary random-walk step. It assumes independent fair nearest-neighbour moves at the origin, fixed \(0<a<1\), and sampling uniformly from the complete discrete history including the current time. All logarithms are natural. Site \(0\) is visited initially and every nonzero site visited thereafter is either \(-1\) or \(1\); no other sites can be reached. Both the almost-sure limits and the distribution in (1)--(2) refer to this precise initial condition. The transform is the joint law of auxiliary continuous-time limits; their ratio supplies the law of the intrinsic walk limit.

## Proof

**1. Exact three-colour embedded urn.** Inspect the visit counts *immediately before each relocation*. Before the first relocation, a first update at the origin either attempts relocation, with probability \(1-a\), or moves once to a neighbour, with total probability \(a\), followed necessarily by relocation. Consequently, the initial counts at the instant before the first relocation consist of one zero and an independent optional side colour: a variable \(B\sim\operatorname{Bernoulli}(a)\), and, if \(B=1\), an independent fair side sign \(\varepsilon\in\{-1,1\}\). Subsequent relocation steps sample a site proportionally to its visit count. If that site is a side site, it contributes one additional visit to the same side before the following relocation. If the sampled site is zero, it contributes one zero visit and, independently with probability \(a\), an additional fair side visit before the following relocation. Thus the exact replacement rule is
\[
0\mapsto0+B'\varepsilon',\qquad +\mapsto+,\qquad -\mapsto-,
\]
where notation on the right indicates **added** balls, \(B'\sim\operatorname{Bernoulli}(a)\) and \(\varepsilon'\) fair independent. Each urn update corresponds to one or two physical visits. In particular the urn composition, apart from at most two intervening visits, reproduces the physical occupation counts at every large time. The random initial side ball is essential for the numerator in (1).

**2. Continuous-time embedding and almost-sure limits.** Equip every urn ball with an independent exponential clock of rate one. When a clock rings, apply its colour's replacement rule and retain the sampled ball. The sequence of rings has precisely the urn draw law. Let \(Z_0(t)\), \(Z_+(t)\), \(Z_-(t)\) be the embedded colour counts, and put \(S(t)=Z_+(t)+Z_-(t)\) and \(Y(t)=Z_+(t)-Z_-(t)\). The zero count is a standard pure-birth Yule process from a single zero, so
\[
e^{-t}Z_0(t)\longrightarrow W>0\quad\text{almost surely and in }L^2,
\qquad W\sim\operatorname{Exp}(1).
\]
The predictable drift of \(S\) is \(S+aZ_0\). Therefore
\[
H(t)=e^{-t}S(t)-a\int_0^t e^{-u}Z_0(u)\,du
\]
is a martingale; its expected quadratic variation is finite, since \(\mathbb E Z_0(u)=e^u\), \(\mathbb ES(u)=a(1+u)e^u\), and hence
\[
\mathbb E\langle H\rangle_\infty
=\int_0^\infty e^{-2u}\mathbb E(S(u)+a Z_0(u))\,du=3a<\infty.
\]
Thus \(H(t)\) converges almost surely, and Cesàro averaging of \(e^{-u}Z_0(u)\to W\) yields
\[
\frac{e^{-t}S(t)}{t}\longrightarrow aW.
\tag{3}
\]
The predictable drift of the signed count \(Y\) equals \(Y\) because side births reproduce their own sign while zero births have mean-zero signs. Therefore \(e^{-t}Y(t)\) is a square-integrable martingale, with expected quadratic variation \(3a\), and it converges almost surely and in \(L^2\) to a signed variable \(D\). Equation (3) and the Yule limit imply \(Z_0(t)/(Z_0(t)+S(t))\sim1/(at)\) and \(tY(t)/(Z_0(t)+S(t))\to D/(aW)\). Moreover \(\log(Z_0(t)+S(t))/t\to1\). Since successive relocation blocks have length at most two, interpolation between blocks transfers these statements to the empirical counts at every integer time, replacing continuous time \(t\) by \(\log n\). This proves the almost-sure assertions.

**3. Exact joint Laplace--Fourier law.** First start from a solitary zero ball, without the optional side seed, and denote its Yule martingale limit by \(W\) and its signed martingale limit by \(D_0\). At the first zero birth, at time \(T\sim\operatorname{Exp}(1)\), two independent zero-descendant families begin, and independently an optional fair-sign side family is born. Let \(U=e^{-T}\sim\operatorname{Uniform}(0,1)\), and let \(E\sim\operatorname{Exp}(1)\) denote the limiting normalized size of a single side family. Branching independence gives the distributional identity
\[
(W,D_0)\ \stackrel d=\ U\bigl(W_1+W_2,\ D_{0,1}+D_{0,2}+B'\varepsilon'E\bigr),
\]
with independent pairs of descendant limits and independent \(U,B',\varepsilon',E\). For \(F(s,t)=\mathbb E[e^{-sW+itD_0}]\), the identity becomes
\[
F(s,t)=\int_0^1F(us,ut)^2\left(1-a+\frac a{1+u^2t^2}\right)du.
\tag{4}
\]
Put \(g(z)=F(zs,zt)\). Equation (4) implies \((zg)'=g^2(1-a+a/(1+z^2t^2))\), with \(g(0)=1\), \(g'(0)=-s\). Solving this first-order equation gives, uniquely,
\[
F(s,t)=\frac1{1+s+a t\arctan t}.
\tag{5}
\]
For the **actual initial walk**, the pre-first-relocation seed contains an additional independently chosen side ball with probability \(a\); its signed Yule limit is \(B\varepsilon E\). Thus \(D=D_0+B\varepsilon E\) and \(W\) remains unchanged, proving (1). Symmetry is immediate and \(\mathbb ED^2=4a>0\), so \(Q_a\) is symmetric and nondegenerate.

**4. Sharp tail coefficient.** Laplace inversion in \(s\) in (5), using the exponential density of \(W\), gives the conditional characteristic function
\[
\mathbb E[e^{itD_0}\mid W=w]=\exp[-awt\arctan t],\qquad w>0,
\]
therefore \(\mathbb E[D_0^2\mid W=w]=2aw\). The initial side limit \(B\varepsilon E\) is independent of \((W,D_0)\). Decompose
\[
Q_a=R_a+J_a,\qquad R_a=\frac{D_0}{aW},\qquad J_a=\frac{B\varepsilon E}{aW}.
\]
For \(x\ge2\), conditional Chebyshev and the exponential density give
\[
\mathbb P(|R_a|>x)\le\int_0^\infty e^{-w}
\min\left\{1,\frac{2}{ax^2w}\right\}\,dw
=O_a\!\left(\frac{\log x}{x^2}\right)=o(x^{-1}).
\]
By independence of \(B,E,W\),
\[
\mathbb P(|J_a|>x)=a\,\mathbb E[e^{-axW}]=\frac a{1+ax}\sim\frac1x.
\]
For every fixed \(\delta\in(0,1)\), the triangle inequalities sandwich \(\mathbb P(|Q_a|>x)\) between \(\mathbb P(|J_a|>(1+\delta)x)-\mathbb P(|R_a|>\delta x)\) and \(\mathbb P(|J_a|>(1-\delta)x)+\mathbb P(|R_a|>\delta x)\). Multiply by \(x\), take limits and send \(\delta\downarrow0\) to get (2). Integrating its asymptotic tail proves \(\mathbb E|Q_a|=\infty\).

## Verification

The bundled standard-library script `verification.py` independently evaluates the nonlinear integral equation (4) by composite Simpson integration on a parameter grid, checks the analytic transform (1), performs exact-rational enumeration of the *original* walk's finite-step transition law and reflection symmetry, and checks relevant moment consistency. Its recorded output appears in `verification_output.txt`. These finite checks corroborate explicit formulas and boundary conventions but cannot replace the infinite-time martingale, branching, Laplace-uniqueness, and tail arguments above.

## Relationship to prior work

Armfield and Mailler (2026), *Localisation of the monkey walk with an “impurity” at the origin*, define the spatially inhomogeneous walk and derive a general measure-valued urn representation. Their Theorem 1.1 assumes the strictly subunit away-from-origin relocation probability and establishes occupation-measure convergence in that regime; neither the complete-relocation endpoint's signed second-order limit nor its transform and tail appear in the inspected manuscript. Boyer, Falcón-Cortés, Giuggioli and Majumdar (2019) analyze an impurity model with self-consistent approximations; their one-dimensional complete-reset endpoint predicts an equal half-mass on each neighbouring site. That **first-order** prediction is not claimed as new. Janson (2024), in the equal-diagonal case of his triangular-urn theorem and Example 14.3, already supplies general logarithmic occupation scaling. The claim here concerns the more refined random signed imbalance, its exact conditional law, and the unexpected parameter-independent index-one tail.

## Limitations

The theorem covers one dimension, a fixed initial visit at the impurity, a symmetric local jump kernel, and **complete** relocation from nonzero sites. It neither establishes uniform convergence as the away-from-origin relocation probability approaches one from below nor treats dimension two or higher. The auxiliary pair \((W,D)\) depends on the branching embedding, but its ratio has the intrinsic walk limit law. The almost-sure result does not assert finite moments of the limiting imbalance: its first absolute moment is infinite. This is a mathematical result supported by the stated derivation and computational consistency checks, not an independently certified theorem; possible older coverage under different urn terminology remains a priority risk.

## References

- Wilfred Armfield and Cécile Mailler, *Localisation of the monkey walk with an “impurity” at the origin*, arXiv:2610.21864, first submitted 2026-10-15. https://arxiv.org/abs/2610.21864
- Denis Boyer, Andrea Falcón-Cortés, Luca Giuggioli, and Satya N. Majumdar, *Anderson-like localization transition of random walks with resetting*, arXiv:1902.00817, first submitted 2019-02-02. https://arxiv.org/abs/1902.00817
- Svante Janson, *Almost sure and moment convergence for triangular Pólya urns*, arXiv:2402.01299, first submitted 2024-02-02. https://arxiv.org/abs/2402.01299
