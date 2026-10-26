# A birthday-collision identity and critical-media crossover in two-panel voter consensus

## Finding

The first-hitting probability of all-positive consensus in a complete-graph, two-panel, positively biased voter process admits an exact finite-population expression. At the critical mass-media probability, the increments of this expression are precisely the tail probabilities of a classical birthday-collision time. As population size grows, an initial positive minority of order \(\sqrt{N}\) undergoes a nontrivial Gaussian crossover; simultaneously varying the media parameter on its critical \(N^{-1/2}\) scale gives a one-parameter family of exact limiting takeover probabilities.

**Theorem.** For every integer \(N\ge3\), every \(0<p<1\), and \(0\le k\le N\), consider the asynchronous update rule in the next section. Let \(H_N(k;p)\) be the probability of eventual unanimous positive opinion. For \(0\le j\le N-2\), define
\[
w_{0,N}(p)=1,\qquad
w_{j,N}(p)=\prod_{i=1}^{j}
\frac{N-i-1}{i-1+2p(N-i-1)}\quad(j\ge1).
\]
Then
\[
\boxed{H_N(k;p)=
\frac{\sum_{j=0}^{\min\{k-1,N-2\}}w_{j,N}(p)}
{\sum_{j=0}^{N-2}w_{j,N}(p)}}
\]
with an empty numerator interpreted as zero. In particular \(H_N(N-1;p)=H_N(N;p)=1\).

At \(p=1/2\), put \(m=N-2\) and let \(T_m\in\{1,\ldots,m+1\}\) be the number of independent uniform draws from \(m\) labels through and including the first repeated label. Then
\[
\boxed{
H_N(k;1/2)=\frac{\mathbb E[\min(T_m,k)]}{\mathbb E[T_m]}}
\]
for every \(0\le k\le N\). In particular the equality holds also at \(k=0,N-1,N\).

For every fixed \(\lambda\in\mathbb R\) and sufficiently large \(N\), take \(p_N=1/2+\lambda/\sqrt N\). If integers \(0\le k_N\le N\) satisfy \(k_N/\sqrt N\to x\in[0,\infty)\), then
\[
\boxed{H_N(k_N;p_N)\longrightarrow
F_\lambda(x):=
\frac{\int_0^x e^{-t^2/2-2\lambda t}\,dt}
{\int_0^\infty e^{-t^2/2-2\lambda t}\,dt}
=1-\frac{\operatorname{erfc}((x+2\lambda)/\sqrt2)}
{\operatorname{erfc}(\sqrt2\lambda)}.}
\]
If \(k_N/\sqrt N\to\infty\), this takeover probability tends to one. For any integers \(1\le k_N=o(\sqrt N)\), the sharper limit is
\[
\boxed{H_N(k_N;p_N)\sim \frac{k_N}{\sqrt N\, I_\lambda}},
\qquad I_\lambda=e^{2\lambda^2}\sqrt{\pi/2}\,\operatorname{erfc}(\sqrt2\lambda).
\]
In particular, for one initial positive voter at critical media,
\[
\boxed{\sqrt N\,H_N(1;1/2)\longrightarrow\sqrt{2/\pi}.}
\]
At \(\lambda=0\), the critical takeover profile is \(F_0(x)=\operatorname{erf}(x/\sqrt2)\).

## Assumptions and scope

There are \(N\ge3\) distinguishable voters at the vertices of a complete graph. Each opinion is positive or negative. At each discrete update, one voter is selected uniformly, then **two distinct other voters** are selected uniformly without replacement, equivalently as a uniformly random ordered pair. A unanimous sampled pair makes the selected voter adopt its common opinion. If the pair is split, the selected voter adopts the **positive** opinion with probability \(p\), and otherwise retains its previous opinion. All random draws at different steps are independent. There are no spontaneous changes when the sample is unanimous. The unanimity states are absorbing. For \(0<p<1\) every interior population count communicates toward an absorbing state, so absorption is almost sure; the positive-consensus hitting probability is well-defined. No initial-distribution assumption is needed because permutation symmetry reduces the state to its number \(k\) of positive voters.

The finite formula holds for every integer population size, every initial count, and every fixed strictly interior media probability. The asymptotic limits concern the specified moving probabilities \(p_N\) and initial population counts. They do not describe finite network topologies other than a complete graph, replacement sampling, or a media rule that is active on unanimous samples.

## Proof

**1. Exact microscopic birth and death probabilities.** Write \(K\) for the positive count and \(a_k=\Pr(K_{t+1}=k+1\mid K_t=k)\), \(b_k=\Pr(K_{t+1}=k-1\mid K_t=k)\). For \(1\le k\le N-1\), an upward jump requires selecting one of \(N-k\) negative voters; its pair is either two positive voters or a split pair followed by the positive media choice. A downward jump requires selecting one of \(k\) positive voters and a pair of two negative voters. Thus
\[
\begin{aligned}
a_k&=\frac{k(N-k)\{k-1+2p(N-k-1)\}}{N(N-1)(N-2)},\\
b_k&=\frac{k(N-k)(N-k-1)}{N(N-1)(N-2)}.
\end{aligned}
\]
The remaining probability is a self-loop. For all \(1\le k\le N-1\) we have \(a_k>0\), and \(b_k\ge0\); specifically \(b_{N-1}=0\).

**2. Exact absorption law.** Set \(h_k=H_N(k;p)\). The Dirichlet problem has \(h_0=0\), \(h_N=1\), and
\[
a_k(h_{k+1}-h_k)=b_k(h_k-h_{k-1}).\]
For \(\Delta_j=h_j-h_{j-1}\), this is \(\Delta_{k+1}=(b_k/a_k)\Delta_k\). Hence \(\Delta_{j+1}=w_{j,N}(p)\Delta_1\) for \(0\le j\le N-2\). The final equation \(b_{N-1}=0\) yields \(\Delta_N=0\). Summing increments and imposing \(h_N=1\) determines \(\Delta_1=(\sum_{j=0}^{N-2}w_{j,N}(p))^{-1}\), proving the finite formula for all \(k\). Because the finite chain is absorbing almost surely, the harmonic solution equals its true hitting probability.

**3. Birthday-collision identity.** At \(p=1/2\), every denominator in the product for \(w_{j,N}\) reduces to \(N-2=m\). Consequently
\[
w_{j,N}(1/2)=\frac{m(m-1)\cdots(m-j+1)}{m^j}
=\Pr(T_m>j)\quad(0\le j\le m).
\]
Here \(\Pr(T_m>j)\) means that the first \(j\) draws were all distinct; the probability is one for \(j=0\). The integer-tail identity \(\mathbb E[\min(T_m,k)]=\sum_{j=0}^{k-1}\Pr(T_m>j)\) and \(\mathbb E[T_m]=\sum_{j=0}^{m}\Pr(T_m>j)\) give the claimed identity, including endpoint saturation since \(T_m\le m+1=N-1\).

**4. Critical parameter and population window.** Write \(m=N-2\), \(\delta_N=2\lambda/\sqrt N\). From the product,
\[
\log w_{j,N}(p_N)=\sum_{r=0}^{j-1}
\left[\log\left(1-\frac r m\right)
-\log\left(1+\delta_N\left(1-\frac r m\right)\right)\right].
\]
For every fixed \(B<\infty\), Taylor expansion uniformly over integers \(0\le j\le B\sqrt N\) gives
\[
\log w_{j,N}(p_N)
=-\frac{j(j-1)}{2m}-\delta_N j+o(1),
\]
where the remainder is uniform in this range. Hence for \(j/\sqrt N\to t\in[0,B]\), \(w_{j,N}(p_N)\to e^{-t^2/2-2\lambda t}\), uniformly on bounded rescaled intervals.

To control the entire denominator rather than only a finite window, use \(\log(1-u)\le-u\) and \(-\log(1+v)\le |v|+C_\lambda v^2\) whenever \(|v|\le |\delta_N|\le1/2\). It follows that for all \(0\le j\le N-2\), for sufficiently large \(N\),
\[
\log w_{j,N}(p_N)\le
-\frac{j(j-1)}{2(N-2)}+
\left(\frac{2|\lambda|}{\sqrt N}+\frac{C_\lambda}{N}\right)j.
\]
The right side has a uniform summable Gaussian envelope on the grid \(j/\sqrt N\). Therefore the scaled denominator converges:
\[
\frac1{\sqrt N}\sum_{j=0}^{N-2}w_{j,N}(p_N)
\longrightarrow I_\lambda=\int_0^\infty e^{-t^2/2-2\lambda t}\,dt.
\]
The similarly rescaled partial numerator tends to the integral through \(x\), proving the finite-\(x\) formula. For \(k_N/\sqrt N\to\infty\), the omitted Gaussian tail tends to zero, so the ratio tends to one. For \(1\le k_N=o(\sqrt N)\), all first \(k_N\) weights are \(1+o(1)\) uniformly, giving a numerator \(k_N(1+o(1))\). Completing the square evaluates \(I_\lambda\), and the quoted special cases follow.

## Verification

The standalone Python standard-library script `verify.py` rederives one-step transition probabilities by enumerating every ordered triple of distinct participants for \(3\le N\le9\). It computes exact rational absorption probabilities a second way by solving the finite Dirichlet linear system, compares all interior initial states at four distinct media probabilities, and checks the birthday identity. It separately computes the finite expressions numerically at \(N\in\{1000,4000,16000,64000\}\), \(\lambda\in\{-1,0,1\}\), and \(x\in\{1/2,1,2\}\) against their asymptotic predictions. The program passed **336 checks**. These computations corroborate the finite identities and convergence rates but do not substitute for the analytical infinite-population arguments above.

Run with `python verify.py`. No packages beyond Python's standard library are required.

## Relationship to prior work

Muslim, NQZ, and Khalif introduced this media-conditioned nonlinear voter mechanism and studied its threshold, effective potential, diffusion/Fokker–Planck approximation, exit probabilities, and finite-size scaling [1]. In particular, the approximate threshold \(p\approx 1/2\) for a two-voter panel and a general diffusion exit-probability integral are **already established**. Those observations are not claimed as new. Their treatment does not supply the exact finite-chain birthday-collision identity or the joint parameter-and-seed critical window proved here. The quantitative crossover can be understood as a rigorous microscopic refinement of the established diffusion picture, rather than a new class of opinion dynamics. Azhari and Muslim studied related external-field effects in larger unanimity panels [2]. Castellano, Muñoz, and Pastor-Satorras developed the foundational nonlinear voter framework under a different (symmetric) noise rule [3]. The statements and their implications were compared, not merely their titles; generic birth–death harmonic recurrences and the birthday paradox are acknowledged as standard ingredients.

## Limitations

The finite and asymptotic statements are exact only for the explicitly specified two-panel, without-replacement, complete-graph rule. They do not give absorption-time asymptotics, multitype voter systems, arbitrary panel sizes, or topology-dependent bounds. When the media parameter differs from the critical value by a fixed amount, a different initial-seed scaling may apply. The use of an existing Markov-chain identity does not itself establish publication priority; general scale-function literature might subsume part of the result. The paper that motivates the model contains an approximate exit-probability formula, so the new claim is the **exact stochastic critical crossover and birthday identity**, not the qualitative existence of a critical-media threshold.

## References

1. R. Muslim, R. A. NQZ, and M. A. Khalif, *Mass media and its impact on opinion dynamics of the nonlinear q-voter model*. SSRN preprint 4384780 (publicly posted 15 March 2023), https://ssrn.com/abstract=4384780; arXiv:2305.06053, https://arxiv.org/abs/2305.06053.
2. Azhari and R. Muslim, *The external field effect on the opinion formation based on the majority rule and the q-voter models on the complete graph*, arXiv:2305.06051, https://arxiv.org/abs/2305.06051.
3. C. Castellano, M. A. Muñoz, and R. Pastor-Satorras, *Nonlinear q-voter model*, arXiv:0907.1775, https://arxiv.org/abs/0907.1775.
