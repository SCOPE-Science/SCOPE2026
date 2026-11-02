# Four cumulant observations identify a two-state fluctuating diffusivity

## Finding

An exact **four-scalar observation protocol** uniquely reconstructs the two diffusivities and both switching rates of a stationary two-state diffusivity model. Two positive observation durations may be selected arbitrarily in advance; no hidden-state observations are required.

Let \(K_j(t)=\operatorname{cum}_j(X_t)\). For fixed \(0<t_1<t_2\), the four values
\[
K_2(t_1),\quad K_4(t_1),\quad K_4(t_2),\quad K_6(t_1)
\]
determine all four parameters globally and uniquely when the two diffusivities are distinct, positive, and ordered, and both switching rates are positive. Moreover, the complete time courses of \(K_2\) and \(K_4\), without \(K_6\), leave a continuum of distinct physical parameter choices indistinguishable. Four is the smallest number of continuous scalar observations that could identify a four-dimensional open parameter domain.

Define the positive functions
\[
F(z)=\frac{z-1+e^{-z}}{z^2},\qquad
G(z)=\frac{z-2+(z+2)e^{-z}}{z^3},\qquad z>0.
\]
Let \(\lambda=\alpha+\beta\), \(p=\alpha/\lambda\), \(\delta=d_+-d_-\), and
\[
\mu=d_-+p\delta,\quad w=p(1-p)\delta^2,\quad c=p(1-p)(1-2p)\delta^3.
\]
Then for every \(t>0\),
\[
\boxed{K_2(t)=2\mu t,\qquad K_4(t)=24w t^2 F(\lambda t),\qquad K_6(t)=720c t^3 G(\lambda t).}
\]
The measured ratio
\[
R=\frac{K_4(t_1)/t_1^2}{K_4(t_2)/t_2^2}=\frac{F(\lambda t_1)}{F(\lambda t_2)}
\]
is strictly increasing in \(\lambda>0\), from \(1\) to \(t_2/t_1\). Its unique positive inverse supplies \(\lambda\). Recover
\[
\mu=\frac{K_2(t_1)}{2t_1},\qquad
w=\frac{K_4(t_1)}{24t_1^2F(\lambda t_1)},\qquad
c=\frac{K_6(t_1)}{720t_1^3G(\lambda t_1)},
\]
and subsequently
\[
\delta=\sqrt{\left(\frac cw\right)^2+4w},\quad
p=\frac12\left(1-\frac{c}{w\delta}\right),\quad
d_-=\mu-p\delta,\quad d_+=\mu+(1-p)\delta,
\]
\[
\boxed{\alpha=\lambda p,\qquad\beta=\lambda(1-p).}
\]
All equalities hold for ideal population cumulants, not noisy sample estimates.

## Assumptions and scope

Take \(0<d_-<d_+<\infty\) and \(\alpha,\beta>0\). Let \(S_t\in\{-,+\}\) be a continuous-time Markov chain switching from \(-\) to \(+\) at rate \(\alpha\) and from \(+\) to \(-\) at rate \(\beta\). Initialize \(S_0\) in its stationary law \(\mathbb P(S_0=+)=p=\alpha/(\alpha+\beta)\). Let \(B\) be a standard Brownian motion independent of the chain, set \(X_0=0\), and define
\[
X_t=\int_0^t\sqrt{2d_{S_s}}\,dB_s.
\]
All four unknown parameters are constant over the two observation durations. The cumulants are those of the unconditional displacement law. The ordering \(d_-<d_+\) removes the trivial state-label ambiguity. No drift, confinement, state observation, or simultaneous time-increment distribution is assumed.

## Proof

**1. Conditional Gaussian reduction.** Let \(A_t=\int_0^t d_{S_s}\,ds\). Conditionally on the entire chain path, \(X_t\) is centered Gaussian with variance \(2A_t\), so
\[
\log\mathbb E e^{qX_t}=\log\mathbb E e^{q^2 A_t}.
\]
Matching powers gives \(K_2=2\mathbb EA_t\), \(K_4=12\operatorname{Var}(A_t)\), and \(K_6=120\operatorname{cum}_3(A_t)\). These are exact identities, not asymptotic expansions.

**2. Two- and three-time correlations.** Put \(Y_t=\mathbf1_{\{S_t=+\}}-p\). The stationary chain gives
\[
\mathbb E(Y_sY_t)=p(1-p)e^{-\lambda|t-s|}.
\]
For ordered \(s\le t\le u\), the Markov property and the two-point identity \(Y_t^2=p(1-p)+(1-2p)Y_t\) yield
\[
\mathbb E(Y_sY_tY_u)=p(1-p)(1-2p)e^{-\lambda(u-s)}.
\]
Multiplying by powers of \(\delta\), the covariance and the third joint centered moment of \(d_{S_t}\) are respectively \(w e^{-\lambda|t-s|}\) and \(c e^{-\lambda(u-s)}\). Thus
\[
\operatorname{Var}(A_t)=2w\int_0^t(t-h)e^{-\lambda h}\,dh
=2wt^2F(\lambda t),
\]
\[
\operatorname{cum}_3(A_t)=6c\int_0^t(t-h)h e^{-\lambda h}\,dh
=6ct^3G(\lambda t).
\]
The factor \(h\) in the second integral is the allowed length of the middle time between the earliest and latest times. Substitution establishes the three displayed displacement-cumulant formulas.

**3. Strict time-ratio monotonicity.** Both \(F\) and \(G\) are strictly positive from the representations
\[
F(z)=\int_0^1(1-u)e^{-zu}\,du,\qquad
G(z)=\int_0^1u(1-u)e^{-zu}\,du.
\]
Write
\[
H(z)=-\frac{zF'(z)}{F(z)}
=2-\frac{z(1-e^{-z})}{z-1+e^{-z}}.
\]
Direct differentiation gives
\[
H'(z)=\frac{e^z\,[2\cosh(z)-2-z^2]}{(ze^z-e^z+1)^2}>0,
\]
since \(\cosh z>1+z^2/2\) for \(z>0\). Consequently,
\[
\frac{d\log R}{d\log\lambda}=H(\lambda t_2)-H(\lambda t_1)>0.
\]
The limits \(F(z)\to1/2\) as \(z\downarrow0\) and \(zF(z)\to1\) as \(z\to\infty\) give the range \((1,t_2/t_1)\). Hence \(\lambda\) is determined by \(R\) without extraneous roots.

**4. Algebraic recovery.** Given \(\lambda\), the formulas isolate \(\mu,w,c\), with \(w>0\). Their identities in \(p,\delta\) imply \(c/w=(1-2p)\delta\) and \((c/w)^2+4w=\delta^2\). Since \(\delta>0\), the stated formulas uniquely recover \(\delta,p,d_-,d_+,\alpha,\beta\), including the symmetric case \(c=0\). This establishes injectivity and explicit inversion on the complete parameter domain.

**5. The information barrier without sixth cumulants.** Fix any physically admissible \(\mu>0,w>0,\lambda>0\). For every \(p\) in the nonempty open interval
\[
0<p<\frac{\mu^2}{\mu^2+w},
\]
set \(\delta(p)=\sqrt{w/[p(1-p)]}\), \(d_-(p)=\mu-p\delta(p)>0\), \(d_+(p)=d_-(p)+\delta(p)\), \(\alpha(p)=\lambda p\), and \(\beta(p)=\lambda(1-p)\). All these distinct admissible models have the same \(K_2(t)\) and \(K_4(t)\) for **every** \(t>0\); their \(K_6\) generally differs. Finally, no continuous injective map from a nonempty open subset of \(\mathbb R^4\) into \(\mathbb R^3\) exists: embedding the alleged image into a coordinate hyperplane of \(\mathbb R^4\) contradicts invariance of domain. Four continuously varying real scalar observations are therefore topologically minimal.

## Verification

The standalone `check_identifiability.py` program uses a separately derived two-state Markov-generator moment hierarchy through degree three for \(A_t\), solved by fourth-order Runge–Kutta. It compares the resulting second, fourth, and sixth displacement cumulants with the analytic formulas at 75 independently sampled positive parameter sets, then independently inverts four synthetic exact observations for each set. It tests an explicit non-identifiable family with matching second/fourth cumulants and differing sixth cumulants, and checks the strict positivity underlying the time-ratio derivative. Run with `python3 check_identifiability.py`; the completed run passed 802 deterministic assertions. These tests are finite corroboration, while steps 1–5 supply the general proof.

## Relationship to prior work

The two-state switching-diffusivity transport model, conditional Gaussian mixture, and occupation-time representation are established in Hidalgo-Soria, Barkai, and Burov (2020), particularly their model, Section I.3.2, and Appendix A. Their equations determine the forward occupation-time law, including asymmetric exponential sojourns. Miyaguchi, Uneyama, and Akimoto (2019) study two-state fluctuating diffusivity and its relaxation functions. Neither inspected work states this fixed-four-observation inverse theorem or the strict fourth-cumulant time-ratio lemma.

Guéneau, Majumdar, and Schehr (2025) derive **exact finite-time moments and even a complete forward characteristic transform** for reset-to-fresh-diffusivity dynamics; their two-atom distribution reduces to the very same two-state continuous-time Markov model (see their supplementary Section IV.3, equations (90)–(92)). Thus the forward cumulant formulas here are **not** presented as conceptually new physics or as independent of that stronger forward result. The evaluated four-observable global inverse theorem, strict monotonicity, and sharp insufficiency of second/fourth cumulants are the assessed addition. A direct published inverse consequence of the 2025 forward transform, or a general inverse theorem not located in the inspected sources, could subsume the contribution; this residual priority risk is explicit.

Cheng and Masuda (2024) treat a different inference experiment, with high-frequency observations of the switching state as well as the diffusion trajectory and statistical estimation, rather than four population displacement cumulants without states. Prior related physical inference results do not supply finite-sample stability for the present reconstruction.

## Limitations

The theorem assumes a *strictly two-state stationary Markov environment* and ideal ensemble cumulants. It does not claim an accurate or numerically well-conditioned inversion from noisy finite samples. In particular, the fourth-cumulant ratio approaches an endpoint when switching is extremely slow or fast, so practical recovery can be ill conditioned even though population identifiability is exact. Diffusivity degeneracy \(d_+=d_-\), vanishing switching rates, initial nonstationarity, and more than two hidden states are excluded. The published 2025 exact forward moments substantially reduce the novelty scope: the finding is a finite-observation inverse classification, not a new general forward propagator.

## References

1. M. Hidalgo-Soria, E. Barkai, and S. Burov, *Cusp of non-Gaussian density of particles for a diffusing diffusivity model*, arXiv:2012.11265v1 (first public 2020-12-21); full text https://arxiv.org/html/2012.11265v2.
2. T. Miyaguchi, T. Uneyama, and T. Akimoto, *Brownian motion with alternately fluctuating diffusivity: Stretched-exponential and power-law relaxation*, arXiv:1907.06819 (2019), https://arxiv.org/abs/1907.06819.
3. M. Guéneau, S. N. Majumdar, and G. Schehr, *Large Deviations in Switching Diffusion: from Free Cumulants to Dynamical Transitions*, arXiv:2501.13754 (2025), including supplementary Sections III and IV, https://arxiv.org/html/2501.13754v2.
4. Y. Cheng and H. Masuda, *Statistical inference for ergodic diffusion with Markovian switching*, arXiv:2410.11333v1 (2024), https://arxiv.org/html/2410.11333v3.
