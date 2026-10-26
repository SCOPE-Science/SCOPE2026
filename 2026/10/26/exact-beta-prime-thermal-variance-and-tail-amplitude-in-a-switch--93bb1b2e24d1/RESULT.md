# Exact beta-prime thermal variance and tail amplitude in a switching stable–inverted harmonic trap

## Finding
For an overdamped Brownian coordinate whose restoring stiffness alternates between an attracting and an inverted harmonic trap, the stationary coordinate is **an explicit Gaussian scale mixture of two beta-prime laws**. This yields a closed stationary variance distribution, its exact algebraic-tail amplitude, all finite even moments, and an infinite sequence of critical switching-rate poles. Earlier literature provides general switching-diffusion existence and tail-exponent results; the explicitly evaluated mixing laws, amplitudes and residues constitute the claim assessed here.

Let \(\sigma\in\{+,-\}\) switch from \(+\) to \(-\) at rate \(u>0\) and from \(-\) to \(+\) at rate \(v>0\). Let
\[
 dX_t=-k_{\sigma_t}X_t\,dt+\sqrt{2D}\,dW_t,\qquad k_+=k>0,\quad k_-=-h<0,\quad D>0,
\]
with independent two-sided Brownian motion and environment. Assume \(kv>hu\). Put
\[
 a=\frac{u}{2k},\quad b=\frac{v}{2h}-\frac{u}{2k}>0,\quad c=1+\frac{k}{h},\quad
 \pi_+=\frac{v}{u+v},\quad\pi_-=\frac{u}{u+v}.
\]
In the unique invariant law there is a positive random conditional variance \(V\), independent of a standard Gaussian \(G\), such that \(X\overset{d}=\sqrt V\,G\). With \(Z=kV/D-1\), the joint environment–variance distribution is
\[
 \frac Zc\,\big|\,(\sigma=+)\sim\operatorname{BetaPrime}(a,b),\qquad
 \frac Zc\,\big|\,(\sigma=-)\sim\operatorname{BetaPrime}(a+1,b).
\]
Here \(\operatorname{BetaPrime}(A,B)\) denotes the density \(t^{A-1}(1+t)^{-A-B}/\mathrm B(A,B)\), \(t>0\); the mixing probabilities are \(\pi_+,\pi_-\). Thus the full stationary position distribution is specified without a transform inversion.

For every real \(p>0\), \(\mathbb E|X|^p<\infty\) **if and only if** \(p<2b=v/h-u/k\). As \(x\to\infty\),
\[
 \Pr(|X|>x)\sim \frac{\pi_+c^{b+1}}{b\,\mathrm B(a,b)}
 \left(\frac Dk\right)^b
 \frac{2^b\Gamma(b+1/2)}{\sqrt\pi}\;x^{-2b}.
\]
Symmetry gives half this coefficient in either one-sided tail. The exponent agrees with previous general switching-diffusion results; the explicit coefficient is part of the present evaluated finding.

For each integer \(n\ge1\) with \(n<b\), define \((z)_j=z(z+1)\cdots(z+j-1)\) and \((z)_0=1\). Then
\[
 \mathbb E X^{2n}=(2n-1)!!\left(\frac Dk\right)^n
 \sum_{j=0}^n\binom nj c^j
 \frac{\pi_+(a)_j+\pi_-(a+1)_j}{\prod_{\ell=1}^j(b-\ell)}.
\]
In the physically symmetric-rate family \(u=v=r\) with \(k>h\), the invariant distribution exists for *every* \(r>0\), yet its order-\(p\) absolute moment is finite precisely when \(r>pkh/(k-h)\). In particular, its variance diverges at \(r_1=2kh/(k-h)\), and on \(r>r_1\):
\[
 \mathbb E X^2=\frac{D[2r+(k-h)]}{r(k-h)-2kh},\qquad
 \lim_{r\downarrow r_1}(r-r_1)\mathbb E X^2=\frac{D(k+h)^2}{(k-h)^2}.
\]
More generally, for \(r_n=2nkh/(k-h)\) and \(a_n=nh/(k-h)\),
\[
 \lim_{r\downarrow r_n}(r-r_n)\mathbb E X^{2n}
 =(2n-1)!!\left(\frac Dk\right)^n c^n\,
 \frac{kh}{(k-h)(n-1)!}\big[(a_n)_n+(a_n+1)_n\big].
\]
All these limits are taken with \(k,h,D,n\) fixed.

## Assumptions and scope
The two-state switching process is stationary and irreducible and independent of thermal Brownian motion. Both states have positive switching rates. The attracting drift has \(k>0\), the unstable drift has \(-h<0\), and \(kv>hu\) is the **necessary and sufficient** integrability condition for the stochastic stationary solution considered here. When \(u=v=r\), also impose \(k>h\). Observables concern the coordinate's stationary one-time law and its moments, not transient covariance, response, entropy production, or work.

## Proof
**Stationary convolution and conditional Gaussianity.** The ergodic theorem gives
\[
 \lim_{T\to\infty}\frac1T\int_{-T}^0k_{\sigma_s}\,ds
 =\frac{kv-hu}{u+v}>0\quad\text{almost surely}.
\]
Consequently the past-driven stochastic convolution
\[
 X_0=\sqrt{2D}\int_{-\infty}^0\exp\!\left[-\int_s^0k_{\sigma_\tau}\,d\tau\right]dW_s
\]
exists almost surely and defines the unique stationary causal solution: under common noise, differences of solutions contract almost surely at the positive average Lyapunov exponent. Conditionally on the entire environmental past, \(X_0\) is centered normal with variance
\[
 V=2D\int_{-\infty}^0\exp\!\left[-2\int_s^0k_{\sigma_\tau}\,d\tau\right]ds.
\]
A standard Gaussian independent of the environment therefore realizes the scale mixture.

**The exact beta-prime law.** The conditional variance is a piecewise deterministic Markov process obeying \(\dot V=2D-2k_\sigma V\). Its attracting-state equilibrium is \(D/k\), and the backward integral is strictly above this value almost surely because unstable excursions occur with positive probability. Setting \(Z=kV/D-1>0\), its drifts are
\[
 f_+(z)=-2kz,\qquad f_-(z)=2h(z+c).
\]
Writing the joint stationary densities as \(p_+(z),p_-(z)\), stationary probability balance gives
\[
 0=-(f_+p_+)' -up_++vp_-,\qquad
 0=-(f_-p_-)' +up_+-vp_-.
\]
The total flux is constant. Integrability at infinity and zero gives flux zero, hence \(f_+p_+=-f_-p_-=:J(z)\). For the signed current \(J<0\), the first balance becomes
\[
 \frac{J'(z)}{J(z)}=\frac{a}{z}-\frac{a+b}{z+c}.
\]
Thus \(J(z)=-Cz^a(z+c)^{-a-b}\). Dividing by the two drifts yields
\[
 p_+(z)\propto z^{a-1}(z+c)^{-a-b},\qquad
 p_-(z)\propto z^a(z+c)^{-a-b-1}.
\]
On transforming \(t=z/c\), these become the indicated beta-prime laws. Their integrated weights must equal the unique Markov environmental stationary probabilities \(\pi_+,\pi_-\); the beta-function identity \(\mathrm B(a+1,b)=a\mathrm B(a,b)/(a+b)\) also gives the correct relative normalization. The Gaussian mixture proves the position assertion. The constructive stationary convolution together with the density and normalization also establishes the relevant invariant-law uniqueness.

**Power moments and the exact tail amplitude.** Both beta-prime densities have large-\(t\) tail proportional to \(t^{-b-1}\). Their mixture therefore has \(\Pr(Z>z)\sim Cz^{-b}\). Summing the two beta-prime survival coefficients and using \(\pi_- (a+b)/a=\pi_+k/h\) gives
\[
 C=\frac{\pi_+c^{b+1}}{b\,\mathrm B(a,b)}.
\]
Since \(V=(D/k)(1+Z)\), \(\Pr(V>w)\sim C(D/k)^bw^{-b}\). Write \(|X|=\sqrt V|G|\). By the product-tail theorem (or direct dominated integration using Gaussian moments), \(\Pr(|X|>x)\sim C(D/k)^b\mathbb E|G|^{2b}x^{-2b}\), and \(\mathbb E|G|^{2b}=2^b\Gamma(b+1/2)/\sqrt\pi\). Likewise \(\mathbb E|X|^p\) is finite exactly when \(\mathbb EV^{p/2}\) is, equivalent to \(p/2<b\). Expand \(V^n=(D/k)^n(1+cT)^n\) and apply the beta-prime moment identity \(\mathbb ET^j=(A)_j/[(b-1)\cdots(b-j)]\) to obtain the finite even-moment sum.

**Symmetric-rate thresholds and residues.** With \(u=v=r\), \(b=r(k-h)/(2kh)\), so \(2b>p\) exactly when \(r>pkh/(k-h)\). The explicit second-moment expression follows either from the sum with \(n=1\) or directly from the stationary generator equations. For general integer \(n\), only the \(j=n\) term of the moment sum has a pole at \(b=n\); all lower terms remain finite. Since \(b-n=(k-h)(r-r_n)/(2kh)\), the limit is the displayed residue. This pole is strictly positive. No interchange of the \(n\to\infty\) and \(r\downarrow r_n\) limits is asserted.

## Verification
The standalone script `verify_switching_trap.py` establishes symbolic stationary-flux identities, checks 180 independent random exact-rational instances of stationary even moments against a *separately derived* Markov-generator recurrence, and checks six high-tail asymptotics through incomplete beta functions. The analytical arguments above, not finitely many tests, prove the infinite-domain statements. Run with Python 3 and the dependencies in `requirements.txt`.

## Relationship to prior work
Guyon, Iovleff and Yao (2004) analyze general linear switching diffusions. De Saporta and Yao (2005), including their two-state example, already establish the heavy-tail exponent for mixed stable/unstable drifts. Bardet, Guérin and Malrieu (2009) give general switching-OU moment and heavy-tail criteria. Huang and coauthors (2014) give general transform and moment recurrences for Markov-modulated OU processes. Bena (2006) surveys dichotomous-noise dynamics. None of the inspected materials stated the normalized two-component beta-prime **conditional thermal-variance mixture**, its evaluated stationary-coordinate tail coefficient, and the symmetric-rate critical-moment residues jointly. This is a qualified literature assessment, not a claim of comprehensive priority.

## Limitations
The model is scalar, overdamped and linear with two Markovian switching states and additive Brownian thermal forcing; the diffusion coefficient is the same in both states. The tail is an invariant one-time marginal, not a sample-path maximum or work distribution. The known tail exponent and moment finiteness threshold are not independently claimed as novel. A specialized prior publication may contain the explicit beta-prime representation or amplitude, so priority remains open to independent bibliographic audit. If \(kv\le hu\), the normalized stationary stochastic convolution studied here does not exist. All rate-pole limits fix the restoring and repulsive strengths.

## References
1. Guyon, Iovleff, Yao (2004), *Linear diffusion with stationary switching regime*, *ESAIM: Probability and Statistics* **8**, 25–35, https://www.numdam.org/item/PS_2004__8__25_0.pdf .
2. B. de Saporta and J.-F. Yao (2005), *Tail of a linear diffusion with Markov switching*, arXiv:math/0503527, version 1 dated 2005-03-24, https://arxiv.org/abs/math/0503527 .
3. J.-B. Bardet, H. Guérin, F. Malrieu (2009), *Long time behavior of diffusions with Markov switching*, arXiv:0912.3231, https://arxiv.org/abs/0912.3231 .
4. H. Huang et al. (2014), *Markov-modulated Ornstein-Uhlenbeck processes*, arXiv:1412.7952, https://arxiv.org/abs/1412.7952 .
5. I. Bena (2006), *Dichotomous Markov noise: Exact results for out-of-equilibrium systems*, arXiv:cond-mat/0606116, https://arxiv.org/abs/cond-mat/0606116 .
