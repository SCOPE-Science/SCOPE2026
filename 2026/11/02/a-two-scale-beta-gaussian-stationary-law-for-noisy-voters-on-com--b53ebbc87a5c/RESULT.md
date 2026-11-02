# A two-scale Beta–Gaussian stationary law for noisy voters on complete bipartite graphs

## Finding

**Theorem (finite covariance and critical stationary fluctuations).** Let \(a,b\ge2\) be integers, and let the noisy voter chain on the complete bipartite graph \(K_{a,b}\) have two possible opinions \(0,1\). Each vertex copies a uniformly sampled neighbor at rate \(1\), independently resets to a fair \(\{0,1\}\)-valued opinion at rate \(\theta>0\), and all clocks are independent. The unique stationary distribution is denoted by \(\pi_{a,b,\theta}\). Write \(P_A\) and \(P_B\) for the fractions of ones in the two parts and set \(h=1/a+1/b\).

Let \(x\) be the stationary correlation of the \(\{-1,+1\}\)-encoded spins at two distinct vertices of the same part, and let \(z\) be that of vertices in different parts. Then correlations within either part agree, and
\[
 x=\frac{h}{h+2\theta(2+\theta)},\qquad
 z=(1+\theta)x,\qquad
 \mathbb E(P_A-P_B)^2=\frac{h\theta(1+\theta)}{2[h+2\theta(2+\theta)]}.
\]
In particular, cross-part correlation is strictly greater than within-part correlation for every finite admissible parameter choice, despite the absence of edges inside parts.

For any sequence \(a_n,b_n\to\infty\), without a restriction on their ratio, take \(h_n=1/a_n+1/b_n\), \(\theta_n>0\) with \(\theta_n/h_n\to\lambda/2\) for some fixed \(\lambda>0\). If \((P_{A,n},P_{B,n})\) has its stationary distribution and
\[
 U_n=\frac{P_{A,n}+P_{B,n}}2,\qquad W_n=\frac{P_{A,n}-P_{B,n}}{\sqrt{h_n}},
\]
then
\[
 (U_n,W_n)\ \Longrightarrow\ \left(P,\sqrt{\frac{P(1-P)}2}\,Z\right),
 \quad P\sim\operatorname{Beta}(\lambda,\lambda),\quad Z\sim N(0,1),\quad P\perp Z.
\]
Thus \(W\mid P=p\sim N(0,p(1-p)/2)\), whereas the unconditional \(W\) is a non-Gaussian centered normal-scale mixture, with
\[
 \operatorname{Var}(W)=\frac{\lambda}{4(2\lambda+1)},\qquad
 \frac{\mathbb EW^4}{(\mathbb EW^2)^2}-3=\frac{3}{\lambda(2\lambda+3)}>0.
\]

## Assumptions and scope

Every copying clock has rate one **per vertex**, not per edge. A reset clock has rate \(\theta\) per vertex; resetting to the already held opinion is allowed and gives no change. The model is a continuous-time Markov chain; fixed \(\theta>0\) ensures irreducibility and a unique finite stationary law. The class fractions, rather than their raw counts, are the observables. The critical limit assumes both part sizes diverge but allows one part to grow arbitrarily faster than the other. The same \(\lambda\) governs the noise-to-effective-inverse-size ratio, \(\theta_n/h_n\to\lambda/2\).

## Proof

### Exact two-point equations

For each vertex \(v\), define \(\sigma_v=2\xi_v-1\in\{-1,+1\}\). Symmetry and uniqueness imply stationary mean zero. Permutations within each part are stationary symmetries. Write \(x_A,x_B\) for two-vertex same-part spin correlations and \(z\) for cross-part spin correlations. Applying the generator to \(\sigma_i\sigma_j\) for distinct vertices of part A or B gives, respectively,
\[
 0=2z-2(1+\theta)x_A,\qquad 0=2z-2(1+\theta)x_B.
\]
Consequently \(x_A=x_B=x\). For a cross-part pair, the copying vertex may select the other endpoint, yielding the positive self-correlation \(1\). The pair equation is
\[
 0=\left(\frac1a+\frac1b\right)
   +\left(2-\frac1a-\frac1b\right)x-2(1+\theta)z.
\]
Solving yields the stated expressions for \(x,z\). Since \(\mathbb E P_A=\mathbb E P_B=1/2\), expansion of the two class-mean squares yields
\[
 \mathbb E(P_A-P_B)^2
 =\frac{h+(2-h)x-2z}{4}=\frac{\theta z}{2}.
\]
This proves all finite-parameter assertions and the exact bound \(\mathbb E(P_A-P_B)^2=O(h)\) when \(\theta/h\) is bounded.

### Lumped generator and slow consensus coordinate

Let \(i=aP_A\) and \(j=bP_B\). The four nonzero rates of the lumped count process \((i,j)\), respectively increasing and decreasing \(i\), then increasing and decreasing \(j\), are
\[
 \begin{aligned}
 r_{i+}&=(a-i)\left(j/b+\theta/2\right),&
 r_{i-}&=i\left(1-j/b+\theta/2\right),\\
 r_{j+}&=(b-j)\left(i/a+\theta/2\right),&
 r_{j-}&=j\left(1-i/a+\theta/2\right).
 \end{aligned}
\]
Put \(U=(P_A+P_B)/2\), \(V=P_A-P_B\), and \(Q=P_A+P_B-2P_AP_B=2U(1-U)+V^2/2\). Directly from the rates, the generator \(L\) and quadratic-variation brackets satisfy the **exact** identities
\[
 LU=\theta(1/2-U),\quad LV=-(2+\theta)V,
 \quad \Gamma(U)=\frac h4(Q+\theta/2),\quad
 \Gamma(V/\sqrt h)=Q+\theta/2.
\]
Here \(\Gamma(f)=L(f^2)-2fLf\), and \(\Gamma(U,V/\sqrt h)\) is uniformly \(O(\sqrt h)\). The jump sizes of \(U\) tend to zero, and the stationary second-moment calculation above implies \(V\to0\) in probability and a uniform bound on \(\mathbb E(V/\sqrt h)^2\) in the critical regime.

Because \(U\in[0,1]\) is tight, each subsequence has a weakly convergent further subsequence. For every twice continuously differentiable \(f\), the stationary identity \(\mathbb E[Lf(U)/h]=0\), Taylor's theorem and the jump brackets show that any limiting marginal measure \(\mu\) satisfies
\[
 \int_0^1\left[\frac\lambda2(1/2-u)f'(u)
 +\frac14u(1-u)f''(u)\right]d\mu(u)=0.
\]
The Taylor remainders tend to zero uniformly: the sum of rate-weighted cubic jump sizes, after division by \(h\), is bounded by a constant times \((a^{-2}+b^{-2})/h\le h\). For polynomial \(f(u)=u^k\), put \(m_k=\int u^k\,d\mu\) and \(m_0=1\). The preceding identity gives
\[
 (2\lambda+k-1)m_k=(\lambda+k-1)m_{k-1},\qquad k\ge1.
\]
These are exactly the moments of \(\operatorname{Beta}(\lambda,\lambda)\). Uniqueness of probability measures on \([0,1]\) from their moments establishes \(U_n\Rightarrow P\) with that beta law.

### Conditional fast fluctuation

Set \(W=V/\sqrt h\). The exact second-moment bound makes \(W\) tight jointly with \(U\). For \(t\in\mathbb R\) and \(\phi\in C^2([0,1])\), apply stationarity to \(F(U,W)=\phi(U)e^{itW}\). The bounded jump sizes and generator identities yield
\[
 L e^{itW}=e^{itW}\left[-it(2+\theta)W
 -\frac{t^2}{2}(Q+\theta/2)\right]+R_h,
 \qquad \lvert R_h\rvert\le C_t\sqrt h.
\]
Indeed the sum of rate-weighted third powers of the jumps in \(W\) is \(O((a^{-2}+b^{-2})h^{-3/2})=O(\sqrt h)\). Moreover \(L\phi(U)=O(h)\) uniformly and the mixed-jump product remainder in \(L[\phi(U)e^{itW}]\) is \(O(\sqrt h)\). The uniform stationary second moment makes \(W\) uniformly integrable in first moment, permitting passage to subsequential joint limits. With \(V\to0\) and \(\theta\to0\), the stationary identity becomes
\[
 \mathbb E\left[\phi(P)e^{itW}\left(-2itW-t^2P(1-P)\right)\right]=0.
\]
Disintegrate over \(P\), and let \(\psi_p(t)=\mathbb E[e^{itW}\mid P=p]\). Uniform integrability justifies differentiating the conditional characteristic function for almost every \(p\) (simultaneously on a countable dense set of \(t\), then continuously). The identity implies
\[
 2\psi'_p(t)+t p(1-p)\psi_p(t)=0,
 \qquad \psi_p(0)=1.
\]
Its unique solution is \(\psi_p(t)=\exp[-p(1-p)t^2/4]\), proving the stated conditional Gaussian law. Every subsequential limit is thus the same; the full joint convergence follows. No uniform-ratio assumption on \(a/b\) entered the argument.

### Non-Gaussian shape

For \(P\sim\operatorname{Beta}(\lambda,\lambda)\), elementary beta-integrals give
\[
 \mathbb E[P(1-P)]=\frac\lambda{2(2\lambda+1)},\qquad
 \mathbb E[P^2(1-P)^2]=\frac{\lambda(\lambda+1)}{4(2\lambda+1)(2\lambda+3)}.
\]
The conditional second and fourth Gaussian moments give the displayed unconditional variance and positive excess kurtosis. Positivity for every finite \(\lambda>0\) proves that the limit is not a single Gaussian distribution.

## Verification

The independent finite-state checker `checker.py` solves the complete lumped chain's stationary linear system using exact rational Gaussian elimination. It passed 409 assertions over 49 systems with \(1\le a,b\le4\) and multiple rational reset rates, testing stationary probabilities, marginal means, same-part and cross-part correlations, the difference variance and an independent fourth-moment datum. This finite calculation is a check of the exact formulas, not a proof of the infinite scaling law. Separately, stationary numerical solutions at \(a=b=8,16,32\) in the critical regime \(\theta=1/a\) showed the fast variance and excess kurtosis moving toward their derived limits \(1/12\) and \(3/5\); numerical trends are not used to establish convergence. The analytic proof above supplies the infinite statement.

## Relationship to prior work

A stochastic pair-approximation analysis of noisy voters on heterogeneous networks was developed by Peralta, Carro, San Miguel and Toral (2018); it derives network-dependent noise fluctuations but uses closure approximations rather than the exact bipartite stationary mixture here. Mori, Hisakado and Nakayama (2018) discuss voter models and multivariate beta laws for a different multi-population setup. Ben-Ari, Panzo, Speegle and VandenBerg (2020) study **quasi-stationarity without noise** on a bipartite graph with one fixed-size part: that is not this irreducible stationary critical-noise regime. Pymar and Rivera (2021) establish general noisy-voter density distribution and correlation tools, including Gaussian and Bernoulli regimes; their generic duality can support the elementary pair calculations, but a separate two-coordinate fast/slow argument is needed for the precise conditional Gaussian-mixture statement. Aljovin, Jara and Xiang (2024) treat noisy-voter equilibrium and thermalization, including complete-graph beta-type behavior; the bipartite fast-disagreement joint law is distinct from that one-population result. The already-known homogeneous beta limit is **not** claimed as a discovery. No assertion of definitive historical priority is made.

## Limitations

The model uses fair two-opinion independent resetting, rate-one per-vertex neighbor copying, complete bipartite mixing and stationary initialization. A different reset law, multiple communities or sparse networks could have different coefficients or distributions. The result gives distributional convergence, not a quantitative rate, process-level approximation or asymptotic independence in any stronger sense than the explicit representation of the joint limiting law. A general uninspected multi-scale diffusion theorem or other earlier network-specific calculation could affect historical priority, which has not been independently audited.

## References

1. A. F. Peralta, A. Carro, M. San Miguel and R. Toral, *Stochastic pair approximation treatment of the noisy voter model*, arXiv:1807.04615 (first posted 2018-07-12). https://arxiv.org/abs/1807.04615
2. T. Mori, M. Hisakado and K. Nakayama, *A voter model on networks and multivariate beta distribution*, arXiv:1810.05643 (first posted 2018-10-12). https://arxiv.org/abs/1810.05643
3. I. Ben-Ari, H. Panzo, P. Speegle and R. O. VandenBerg, *Quasi-Stationary Distributions for the Voter Model on Complete Bipartite Graphs*, arXiv:2004.10187 (first posted 2020-04-21). https://arxiv.org/abs/2004.10187
4. R. Pymar and N. Rivera, *On the stationary distribution of the noisy voter model*, arXiv:2112.01478 (first posted 2021-12-02). https://arxiv.org/abs/2112.01478
5. A. Aljovin, M. Jara and H. Xiang, *Thermalization and convergence to equilibrium of the noisy voter model*, arXiv:2409.05722 (first posted 2024-09-09). https://arxiv.org/abs/2409.05722
