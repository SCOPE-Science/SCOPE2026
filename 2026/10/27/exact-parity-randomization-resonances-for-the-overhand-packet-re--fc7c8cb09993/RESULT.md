# Exact parity-randomization resonances for the overhand packet-reversal shuffle

## Finding
Consider the independent-gap packet-reversal shuffle on a deck of \(n\ge2\) labeled cards. Each of its \(n-1\) gaps is cut with probability \(p\in(0,1)\), independently; each resulting consecutive packet is reversed in place. Write \(q=1-p\), let \(R\) denote one random shuffle permutation, and define the sign-character eigenvalue \(a_n(p)=\mathbb E[\operatorname{sgn}(R)]\). This is the entire bias of the induced walk on the canonical two-element quotient \(S_n/A_n\).

**Exact law and resonance count.** The generating function and recurrence are
\[
\sum_{n\ge1}a_n(p)z^n=\frac{z(1-qz)}{1-pz+qz^2},\qquad
 a_1(p)=1,\quad a_2(p)=2p-1,\quad a_n(p)=pa_{n-1}(p)-qa_{n-2}(p)\quad(n\ge3).
\]
Set \(p_*=2(\sqrt2-1)\). For every \(n\ge2\), the equation \(a_n(p)=0\) has **exactly \(\lfloor n/2\rfloor\) distinct simple solutions in \(0<p<p_*\)** and has no solutions in \(p_*\le p<1\). These are precisely the cut probabilities for which a single complete shuffle produces perfectly uniform parity, even though the full permutation is not thereby claimed uniform.

**Distribution of resonance parameters.** Let \(p_{n,1},\ldots,p_{n,m_n}\) be these distinct roots (in any order), where \(m_n=\lfloor n/2\rfloor\). As \(n\to\infty\), their empirical measure converges weakly on \([0,p_*]\) to the probability density
\[
 f(p)=\frac{2-p}{\pi(1-p)\sqrt{4(1-p)-p^2}}\,\mathbf1_{(0,p_*)}(p).
\]
In particular, exact-parity resonance points have an integrable square-root density singularity at \(p_*\). For every fixed \(0<p<p_*\), the bias \(a_n(p)\) takes both signs infinitely often as \(n\to\infty\); for \(p\ge p_*\), it is positive for every \(n\ge1\).

For a deterministic initial deck \(\sigma_0\) and any integer \(t\ge1\), the sign after \(t\) independent shuffles has exact law
\[
 \Pr\{\operatorname{sgn}(\sigma_t)=+1\}=\frac{1+\operatorname{sgn}(\sigma_0)a_n(p)^t}{2}.
\]
Consequently, the parity marginal is exactly stationary after one step at any of the \(m_n\) resonances, and its total-variation distance from the uniform parity law at time \(t\) is \(|a_n(p)|^t/2\). The physical packet-order-reversal convention multiplies the sign eigenvalue by \((-1)^{\binom n2}\), so all zero locations and parity distances are unchanged.

## Assumptions and scope
Every gap has the same fixed independent cut probability \(p\), and every packet is reversed **internally**, not reordered with the other packets. The claims hold for every integer deck size \(n\ge2\), all \(0<p<1\), and every nonnegative integer number of independent shuffles (the explicit probability identity is also valid for \(t=0\)). The root-count and limiting-root statements concern the variation of \(p\) at fixed \(n\), not the stochastic trajectory's positions. No asymptotics in the shuffle time are needed.

## Proof
**1. Signed composition generating function.** A reversed packet of length \(\ell\ge1\) has sign \((-1)^{\binom\ell2}\), whose values for successive lengths are \(+,-,-,+,+,-,-,+,\ldots\). A cut vector creates a composition \((\ell_1,\ldots,\ell_m)\) of \(n\) with probability \(p^{m-1}q^{n-m}\). Since packet supports are disjoint, its sign is the product of the packet signs. Thus the signed single-packet series is
\[
 B(z)=\sum_{\ell\ge1}(-1)^{\binom\ell2}q^{\ell-1}z^\ell
 =\frac{z(1-qz)}{1+q^2z^2}.
\]
Summing over one or more packets gives \(A(z)=B(z)/(1-pB(z))=z(1-qz)/(1-pz+qz^2)\). Coefficient comparison proves the recurrence.

**2. Trigonometric form below the critical probability.** The quadratic characteristic roots become complex exactly when \(p^2<4q\), i.e. \(0<p<p_*\). Put \(r=\sqrt q\) and introduce the unique \(\theta\in(0,\pi/2)\) such that \(p=2r\cos\theta\). Inverting the rational generating function yields
\[
 a_n(p)=r^{n-1}\frac{\sin(n\theta)-r\sin((n-1)\theta)}{\sin\theta}.
\]
Let \(\phi(\theta)=\arg(1-r e^{-i\theta})\in(0,\pi/2)\). Since \(r^2+2r\cos\theta=1\),
\[
 r=\sqrt{1+\cos^2\theta}-\cos\theta,\qquad
 \phi(\theta)=\arctan\frac{\sin\theta}{\sqrt{1+\cos^2\theta}}.
\]
This is continuous and strictly increasing from \(0\) to \(\pi/4\) as \(\theta\) goes from \(0\) to \(\pi/2\). Furthermore, \(p=1-r^2\) decreases strictly from \(p_*\) to \(0\) along this interval. The numerator of \(a_n\) has the same sign as
\[
 \sin\big(n\theta+\phi(\theta)\big).
\]
Hence its zeros correspond exactly to \(n\theta+\phi(\theta)=j\pi\). The left side increases strictly from \(0\) to \(n\pi/2+\pi/4\). For integer \(n\ge2\), the admissible positive integers are exactly \(j=1,\ldots,\lfloor n/2\rfloor\). Strict derivatives of the phase and of the change of variable give simplicity of each root.

**3. No roots above the critical point.** At \(p=p_*\), the characteristic polynomial has repeated root \(r=\sqrt{1-p_*}\), and direct limiting inversion gives
\[
 a_n(p_*)=r^{n-1}\big[n-(n-1)r\big]>0.
\]
For \(p_*<p<1\), the roots \(\lambda_+>\lambda_->0\) of \(x^2-px+q=0\) satisfy \(q<\lambda_-<\lambda_+<1\), because their product is \(q\) and \(\lambda_+<1\). The explicit expression is
\[
 a_n(p)=\frac{\lambda_+^{n-1}(\lambda_+-q)-\lambda_-^{n-1}(\lambda_--q)}{\lambda_+-\lambda_-}>0,
\]
where the inequality holds because \(x\mapsto x^{n-1}(x-q)\) strictly increases on \(x>q\).

**4. Root-density law.** Write \(\theta_{n,j}\) for the solution of \(n\theta+\phi(\theta)=j\pi\). The phase bounds imply
\[
 \frac{(j-1/4)\pi}{n}<\theta_{n,j}<\frac{j\pi}{n},
 \qquad1\le j\le\lfloor n/2\rfloor.
\]
Thus the empirical \(\theta\)-law converges to uniform density \(2/\pi\) on \([0,\pi/2]\). Since \(\theta(p)=\arccos\big(p/(2\sqrt{1-p})\big)\), differentiation gives
\[
 \left|\frac{d\theta}{dp}\right|=\frac{2-p}{2(1-p)\sqrt{4(1-p)-p^2}}.
\]
The pushforward density is the one claimed. The singularity at the endpoint follows from the simple zero of \(4(1-p)-p^2\) at \(p_*\).

**5. Sign oscillations and time evolution.** Below \(p_*\), the phase \(n\theta+\phi\) traverses positive and negative sine values infinitely often: if \(\theta/\pi\) is irrational this follows from density modulo \(2\pi\); if rational, its finite rotation orbit contains points in both semicircles and repeats periodically. Above \(p_*\), positivity was proved in step 3. Because sign is a homomorphism of the permutation group, independent passes multiply independent \(\pm1\) signs with common mean \(a_n(p)\). This establishes the probability and total-variation statements. For the physical convention use the fixed full-deck reversal \(J\), whose sign is \((-1)^{\binom n2}\).

## Verification
An accompanying pure-Python verifier enumerates every cut pattern for deck sizes \(1\) through \(10\) at each of four rational cut probabilities, and checks all **40** exact rational signed expectations against the recurrence, without floating-point rounding. The finite tests independently reconstruct the packet lengths and permutation signs from each cut vector. The analytic phase monotonicity and root-count proof above establish the claims for all deck sizes; no finite experiment is used to infer infinite validity. The root-density formula can also be independently checked by substitution \(\theta=\arccos(p/(2\sqrt{1-p}))\), which gives total mass one.

## Relationship to prior work
Jiang, *Cutoff for the Overhand Shuffle* (2026), studies precisely this Bernoulli-gap packet-reversal convention and proves the full permutation walk's total-variation cutoff. Its Section 3 establishes ergodicity, the physical-convention equivalence, and a one-card cosine spectral decomposition. Those are distinct from the full-deck **sign-character** eigenvalue and the classification of cut probabilities giving exact parity equilibrium in one step. The root-density law is not a corollary of the quoted cutoff time: it concerns varying \(p\) with finite deck size. Earlier overhand-shuffle works by Pemantle (1989) and Jonasson (2006) provide mixing-order estimates. The packet composition and sign-character calculation use standard tools; novelty is asserted only for the specific complete resonance spectrum and its limiting edge distribution, subject to historical-priority qualifications.

## Limitations
This is a result about the canonical two-point parity projection; uniform parity does **not** imply a uniform permutation. The resonance law does not sharpen the leading full-deck cutoff time. It requires uniform independent cut probabilities and the specified packet model. Priority is assessed from the available principal new manuscript, published-record searches and available historical abstracts. An older overhand-shuffle article's complete text could not be inspected, so unnoticed historical treatment of parity remains a risk. No independent external audit has been performed.

## References
1. Y. Jiang, *Cutoff for the Overhand Shuffle*, arXiv:2610.00137v1, first publicly available 2026-09-10, https://arxiv.org/abs/2610.00137.
2. R. Pemantle, *Randomization Time for the Overhand Shuffle*, Journal of Theoretical Probability **2** (1989), 37–49, DOI:10.1007/BF01048267.
3. J. Jonasson, *The Overhand Shuffle Mixes in \(\Theta(n^2\log n)\) Steps*, Annals of Applied Probability **16** (2006), 241–243.
