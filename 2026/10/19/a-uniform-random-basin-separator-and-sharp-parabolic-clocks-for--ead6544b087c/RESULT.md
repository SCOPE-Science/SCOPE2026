# A uniform random basin separator and sharp parabolic clocks for a Bernoulli Arnold pair

## Finding

The Bernoulli Arnold circle-homeomorphism pair in Example 8 of Li and Lloyd has a common neutral fixed circle point but a noninteger random rotation number. Its **actual random orbits** admit a complete additional classification: a biased coin selects a deterministic side of the shared fixed point with a sharp inverse-linear convergence rate and a Gaussian reciprocal-distance fluctuation; the fair coin produces a single random separator whose distribution is **exactly uniform**. The common circle point is the unique annealed stationary state for every positive choice of the two symbol probabilities.

Write \(a=1/4\), \(b=5/4\), and on the interval \(I=[a,b]\) define
\[
h(x)=\frac{1-\sin(2\pi x)}{10},\qquad f_+(x)=x+h(x),\qquad f_-(x)=x-h(x).
\]
For each \(p\in(0,1)\), choose independent symbols \(\varepsilon_n\in\{+1,-1\}\) with \(\mathbb P(\varepsilon_n=+1)=p\), and iterate
\[
X_{n+1}^x=X_n^x+\varepsilon_n h(X_n^x),\qquad X_0^x=x\in I.
\]
Put \(\mu=2p-1\) and \(c=\pi^2/5\). The conclusions below are joint results for this single specified dynamical model.

**Biased regime.** If \(\mu>0\), on an event of probability one, \(X_n^x\to b\) and
\[
\lim_{n\to\infty}n(b-X_n^x)=\frac{1}{c\mu}
\]
**for every** initial \(x\in(a,b)\) simultaneously. If \(\mu<0\), the corresponding simultaneous statements are \(X_n^x\to a\) and
\[
\lim_{n\to\infty}n(X_n^x-a)=\frac{1}{c|\mu|}.
\]
For each deterministic \(x\in(a,b)\), let \(d_n\) be its positive distance to the selected endpoint. Then
\[
\frac{d_n^{-1}-c|\mu|n}{c\sqrt n}\ \Longrightarrow\ N(0,1-\mu^2).
\]
The variance is strictly positive because \(0<p<1\). The normal limit is a distributional statement over the driving words, **not** a pathwise limit.

**Unbiased regime.** If \(p=1/2\), there is a measurable random variable \(U\in[a,b]\), uniform on \([a,b]\), such that with probability one, simultaneously for every \(x\in[a,U)\), \(X_n^x\to a\), and for every \(x\in(U,b]\), \(X_n^x\to b\). Nothing is asserted about \(x=U\). For each fixed \(x\in I\),
\[
\mathbb P(X_n^x\to b)=x-a,\qquad
\mathbb P(X_n^x\to a)=b-x.
\]
The endpoints \(a\) and \(b\) represent the same circle point. Thus, for every \(p\in(0,1)\), the unique stationary probability measure of the **annealed circle Markov operator** is \(\delta_{a\bmod1}\). This does not imply uniqueness of all skew-product invariant measures with arbitrary dependence on the full driving history.

## Assumptions and scope

Li and Lloyd's Example 8 has two standard real lifts \(F_0(x)=x+(1-\sin(2\pi x))/10\) and \(F_1(x)=x+(9+\sin(2\pi x))/10\). The second interval-preserving lift is \(f_-(x)=F_1(x)-1\), whereas \(f_+(x)=F_0(x)\). Subtracting an integer preserves the circle map but **does not preserve the specified real-lift rotation number**. Our symbol \(+\) means the source's symbol \(0\), and \(-\) means its symbol \(1\). The standard-lift rotation number is therefore \(1-p\), not the drift \(\mu\). Throughout, \(p\) is fixed strictly inside \((0,1)\), and all random signs are independent and identically distributed.

For the translated coordinate \(y=x-a\in[0,1]\), the displacement is \(h(a+y)=(1-\cos(2\pi y))/10\), vanishing only at the endpoints. Both maps \(y\mapsto y\pm h(a+y)\) are strictly increasing diffeomorphisms of \([0,1]\), because their derivatives lie in \([1-\pi/5,1+\pi/5]\subset(0,\infty)\). Consequently every interior trajectory stays interior at every finite time, both endpoint trajectories remain fixed, and the images of different initial states preserve their order.

## Proof

**1. Almost-sure endpoint convergence.** For a fixed starting point let \(\mathcal F_n\) be the filtration of the first \(n\) symbols. Independence gives the exact conditional drift
\[
\mathbb E[X_{n+1}^x-X_n^x\mid\mathcal F_n]=\mu h(X_n^x).
\]
Thus \(X_n^x\) is a bounded submartingale if \(\mu>0\), a bounded supermartingale if \(\mu<0\), and a bounded martingale if \(\mu=0\). By the corresponding convergence theorem it approaches a random limit \(L\in[a,b]\) almost surely. But \(|X_{n+1}^x-X_n^x|=h(X_n^x)\), so convergence forces \(h(L)=0\); hence \(L\in\{a,b\}\), for every deterministic starting state.

**2. Biased side selection.** The exact Taylor expansions at either endpoint are
\[
h(a+d)=c d^2+O(d^4),\qquad h(b-d)=c d^2+O(d^4),\quad c=\pi^2/5.
\]
Suppose first \(\mu>0\). On the event \(X_n^x\to a\), put \(d_n=X_n^x-a\). For sufficiently large \(n\), exact reciprocation yields
\[
\frac1{d_{n+1}}-\frac1{d_n}
=-\frac{\varepsilon_n h(a+d_n)}{d_n(d_n+\varepsilon_n h(a+d_n))}
=-c\varepsilon_n+O(d_n).
\]
The strong law of large numbers and Cesàro convergence would give \((nd_n)^{-1}\to-c\mu<0\), impossible since \(d_n>0\). Hence \(X_n^x\to b\) almost surely. The same argument after reversing the endpoints excludes convergence to \(b\) when \(\mu<0\).

**3. Sharp clock and central limit law.** For \(\mu>0\) now put \(d_n=b-X_n^x\). Reciprocation gives
\[
\frac1{d_{n+1}}-\frac1{d_n}
=\frac{\varepsilon_n h(b-d_n)}{d_n(d_n-\varepsilon_n h(b-d_n))}
=c\varepsilon_n+O(d_n).
\]
When \(\mu<0\), use \(d_n=X_n^x-a\) and the corresponding increment \(-c\varepsilon_n+O(d_n)\). In both cases the strong law implies
\[
\frac{d_n^{-1}}n\longrightarrow c|\mu|>0,
\]
so \(d_n=(c|\mu|n)^{-1}(1+o(1))\) almost surely. In particular, for each sample path and initial point, \(d_n=O(n^{-1})\) eventually. Summing the displayed reciprocal expansion now improves it to
\[
 d_n^{-1}=c\operatorname{sgn}(\mu)\sum_{j=0}^{n-1}\varepsilon_j+O(\log n)
\]
almost surely. Since the bounded independent signs have mean \(\mu\) and variance \(1-\mu^2\), the classical central limit theorem and Slutsky's lemma give the claimed normal law.

For the stronger simultaneous almost-sure statements, intersect the probability-one events for the countable set of rational \(x\in(a,b)\). Because every finite composition is increasing, any arbitrary interior \(x\) can be squeezed between two rational initial points whose scaled distances satisfy the same limit. This proves the stated convergence and clock on one common probability-one set.

**4. Uniform unbiased separator.** With \(\mu=0\), \(X_n^x\) is a bounded martingale with endpoint limit. Conservation of expectation and \(b-a=1\) imply
\[
\mathbb P(X_n^x\to b)=\frac{x-a}{b-a}=x-a.
\]
On a common full-measure set every rational initial point has an endpoint limit. Order preservation implies that the rational points converging to \(a\) form an initial segment, and those converging to \(b\) form a final segment. Define \(U\) as the supremum of rational initial points converging to \(a\), taking the appropriate endpoint when the set is empty or full. This is measurable as a countable supremum. Monotone squeezing shows that all real starting points below \(U\) converge to \(a\), and all those above it converge to \(b\). For rational \(a<r<s<b\), the events \(X_n^r\to b\) and \(X_n^s\to a\) respectively constrain \(U\le r\) and \(U\ge s\). For any \(r<t<s\), the first event gives \(\mathbb P(U<t)\ge r-a\), while \(U\le t\) implies the second point \(s\) tends to \(b\), giving \(\mathbb P(U\le t)\le s-a\). Sending \(r\uparrow t\) and \(s\downarrow t\) proves \(\mathbb P(U\le t)=t-a\) for every \(a\le t\le b\). Thus \(U\) is exactly uniform and has no atoms; the exceptional event \(U=x\) has probability zero for each deterministic initial \(x\).

**5. Stationarity on the circle.** Denote by \(T\) the annealed Markov operator of the circle maps. All circle projections \(X_n^x\bmod1\) tend almost surely to \(a\bmod1\), since both endpoint limits project there. If \(\nu\) is any stationary circle probability measure, start with an independent initial \(X_0\sim\nu\), then for each bounded continuous circle observable \(g\), dominated convergence and stationarity yield
\[
\int g\,d\nu=\mathbb E[g(X_n\bmod1)]\longrightarrow g(a\bmod1).
\]
Therefore \(\nu=\delta_{a\bmod1}\), which is stationary because both maps fix that circle point.

## Verification

The accompanying standalone `verify.py` reproduces the quadratic endpoint coefficient, the exact fair-coin martingale identity, two reciprocal-limit signs at both boundaries, strict order-preservation checks, the inverse-Jacobian balance and seeded numerical tests of the biased inverse-linear clock. All numerical tests are finite diagnostics. The almost-sure endpoint statements, uniform separator distribution, law of large numbers and central limit theorem follow from the analytical proof above, not from simulation. The verifier does not purport to certify stochastic infinite-time convergence computationally.

## Relationship to prior work

Li and Lloyd, arXiv:2603.18617v1, Example 8 (Section 3, equations (35)–(36)), establish the common fixed point and the **standard-lift rotation number** \(1-p\) for this exact Arnold pair; these are inputs, not new results. Their Theorems A and B concern random periodic cycles and rotation-number arithmetic, not the forward orbit boundary-selection, its sharp parabolic clock, reciprocal-distance normal law, or uniform critical basin separator.

Gelfert and Stenflo, *Random iterations of homeomorphisms on the circle* (2017), establish qualitative synchronization results in minimality-related regimes. This pair has a common fixed point, so it is not forward minimal; their minimality-based theorem does not imply the quantified conclusions here.

Gelfert and Salcedo, *Synchronization rates and limit laws for random dynamical systems* (arXiv:2311.11338v1), study local exponential contraction and central limit theorems for additive observables under a local contraction hypothesis. Here each generator has derivative exactly one at the common fixed point, and the attraction clock is polynomial. Their exponential-contraction framework does not itself determine the present inverse-distance CLT or the fair-coin uniform separator.

General bounded-martingale convergence, the strong law, and classical central limit theory are used as **standard tools**; no originality is attributed to these theorems. The scientific claim is the exact joint structural classification in this particular recent random-circle example.

## Limitations

The bias is fixed independently of time; no scaling limit as \(p\to1/2\) jointly with \(n\to\infty\) is proved. The Gaussian statement applies to reciprocal endpoint distance only in the biased regimes, and does not assert deterministic centering on sample paths. At the unbiased separator \(x=U(\omega)\), the orbit's limit is not classified. The uniqueness of the stationary law concerns the annealed circle Markov operator, not arbitrary skew-product measures. These claims do not extend automatically to other random Arnold families, maps with different endpoint degeneracies, or arbitrary correlated symbol processes. Bibliographic priority remains subject to independent expert checking, especially in the broader literature on random interval homeomorphisms and martingales.

## References

1. Zixu Li and Simon Lloyd, *Periodicity and rotation number for random circle homeomorphisms*, arXiv:2603.18617v1 (publicly posted 2026-03-19), Section 3 Example 8, https://arxiv.org/html/2603.18617v1.
2. Katrin Gelfert and Örjan Stenflo, *Random iterations of homeomorphisms on the circle*, Modern Stochastics: Theory and Applications 4 (2017), 253–271, https://doi.org/10.15559/17-VMSTA86.
3. Katrin Gelfert and Graccyela Salcedo, *Synchronization rates and limit laws for random dynamical systems*, arXiv:2311.11338v1 (2023), https://arxiv.org/html/2311.11338v1.
