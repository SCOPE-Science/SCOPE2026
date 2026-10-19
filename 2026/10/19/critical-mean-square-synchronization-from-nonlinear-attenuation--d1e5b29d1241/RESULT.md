# Critical mean-square synchronization from nonlinear attenuation on a noisy three-person hyperedge

## Finding

The three-person specialization of a noisy higher-order opinion-update law has an exact one-step mean-square frontier. A naturally decreasing nonlinear group-modulation function permits almost-sure and mean-square **agreement of differences at the exact variance-neutral gain**, with an explicit inverse-linear upper bound; constant modulation instead retains the original disagreement second moment at that gain.

For every \(\kappa>0\), define \(\gamma_c=3/(9+4\kappa^2)\). At every \(0<\gamma<\gamma_c\), complete random-opinion consensus holds. At \(\gamma=\gamma_c\), the centered disagreement \(S_t\) tends to zero almost surely and satisfies
\[
\mathbb{E}S_t\leq\frac{S_0}{1+\frac{3h^2S_0}{1+2S_0}t},\qquad h=2\gamma\kappa.
\]
Above \(\gamma_c\), the expected disagreement increases in one step for arbitrarily small nonuniform states. This last statement concerns one-step mean-square contraction only, not long-run divergence.

## Assumptions and scope

There are exactly three real-valued agents \(i\in\{1,2,3\}\), with the single static hyperedge \(\{1,2,3\}\). Fix \(\gamma,\kappa>0\). For each ordered pair \(i\ne j\) and time \(t\ge0\), \(w_{ij}(t)\) has mean zero and variance one; these variables are mutually independent across ordered pairs and times. No symmetry or bounded support of the noise distribution is required. The initial opinions are deterministic finite real numbers. Whenever \(\{i,j,k\}=\{1,2,3\}\), their update is
\[
x_i(t+1)=x_i(t)+2\gamma\!\sum_{j\ne i}(x_j(t)-x_i(t))
+2\gamma\kappa\!\sum_{j\ne i}\frac{(x_j(t)-x_i(t))w_{ij}(t)}{1+(x_j(t)-x_k(t))^2}.
\]
This is the directed-pair-noise form of Equation (3.1) of Shang (2023), with \(g(z)=z\) and \(f(s)=\kappa/(1+s^2)\). The distinct-noise assumption is part of this precise equation; a common noise reused for two pairs is a different model. Write \(\overline x(t)=\frac13\sum_i x_i(t)\), \(S_t=\sum_i(x_i(t)-\overline x(t))^2\), \(h=2\gamma\kappa\), \(\lambda=1-6\gamma\), and \(\rho=\lambda^2+4h^2\). All assertions are for every deterministic initial vector unless a nonconstant vector is expressly required.

## Proof

**Exact conditional variance.** Fix any state \(x\) and let \(a_i=(x_j-x_k)^2\), \(B_i=(x_i-x_j)^2+(x_i-x_k)^2\) for the other two indices \(j,k\). Define \(P=I-\mathbf1\mathbf1^{\mathsf T}/3\), so \(S=\|Px\|^2\). The deterministic centered update equals \(\lambda Px\). The random increment \(\eta_i=h[(x_j-x_i)w_{ij}+(x_k-x_i)w_{ik}]/(1+a_i)\) has independent, centered components with conditional variances \(h^2B_i/(1+a_i)^2\). Since each diagonal entry of \(P\) equals \(2/3\),
\[
\mathbb E[S_{t+1}\mid x(t)=x]
=\lambda^2S+\frac23h^2\sum_{i=1}^3\frac{B_i}{(1+a_i)^2}.\tag{1}
\]
The identity \(\sum_iB_i=6S\) proves \(\mathbb E[S_{t+1}\mid x]\le\rho S\). Scaling any nonconstant opinion vector toward its mean sends every \(a_i\) to zero while preserving the ratio, hence the supremum equals \(\rho\). Direct algebra gives \(\rho<1\) exactly for \(0<\gamma<3/(9+4\kappa^2)\); at the upper endpoint it equals one. If \(\gamma>\gamma_c\), the supremum is above one and scaling yields explicit arbitrarily small states with strictly expanding conditional mean-square disagreement.

**Subcritical consensus.** Iterating (1) yields \(\mathbb ES_t\le\rho^tS_0\). The mean \(\overline x(t)\) is a martingale, and its increment has conditional variance
\[
\mathbb E[(\overline x(t+1)-\overline x(t))^2\mid x(t)]
=\frac{h^2}{9}\sum_i\frac{B_i}{(1+a_i)^2}\le\frac23h^2S_t.
\]
Consequently \(\overline x(t)\) is bounded in \(L^2\), and converges almost surely and in \(L^2\) to \(M_\infty\), with \(\mathbb EM_\infty=\overline x(0)\) and \(\operatorname{Var}(M_\infty)\le 2h^2S_0/[3(1-\rho)]\). Since \(\sum_t\mathbb ES_t<\infty\), Markov's inequality and Borel–Cantelli give \(S_t\to0\) almost surely. Moreover \(\mathbb E|x_i(t)-\overline x(t)|^2\le\mathbb ES_t\to0\). Each individual therefore converges to \(M_\infty\) almost surely and in \(L^2\).

**Critical algebraic disagreement decay.** Set \(\rho=1\). For any nonnegative \(a\), \(1-(1+a)^{-2}\ge a/(1+a)\). We have \(a_i\le2S\) and, for three collinear real opinions,
\[
\sum_i a_iB_i=2\sum_{i<j}a_ia_j=\frac92S^2.
\]
Subtracting (1) from \(S\) therefore yields
\[
\mathbb E[S_{t+1}\mid x(t)=x]
\le S-\frac{3h^2S^2}{1+2S}.\tag{2}
\]
Thus \(S_t\) is a nonnegative supermartingale. The function \(s\mapsto s^2/(1+2s)\) is convex for \(s\ge0\), so Jensen's inequality for \(u_t=\mathbb ES_t\le S_0\) implies
\[
u_{t+1}\le u_t-\frac{3h^2u_t^2}{1+2u_t}
\le u_t-\frac{3h^2}{1+2S_0}u_t^2.
\]
If \(S_0=0\) the opinions are and remain identical. If \(S_0>0\), the reciprocal inequality \(1/u_{t+1}\ge1/u_t+3h^2/(1+2S_0)\) (with zero values treated by continuity) gives the advertised inverse-linear bound. Since \(S_t\) converges almost surely by the nonnegative supermartingale theorem and \(\mathbb ES_t\to0\), Fatou's lemma forces its almost-sure limit to be zero.

**Necessity of nonlinear attenuation for the critical second-moment conclusion.** Replacing \(f(s)=\kappa/(1+s^2)\) by the constant \(f(s)=\kappa\) removes the denominators in (1), leaving the exact recursion \(\mathbb E[S_{t+1}\mid x(t)]=\rho S_t\). At \(\gamma=\gamma_c\), \(\mathbb ES_t=S_0\) for every time, so no convergence in mean-square disagreement occurs for a nonconstant initial state.

## Verification

The included standalone \(\texttt{verify.py}\) uses only Python's standard library. It computes all \(2^6\) equiprobable directed-pair Rademacher noise outcomes per selected rational state and compares their exact expectation with (1). It also verifies (2), \(\sum_{i<j}a_ia_j=9S^2/4\), and the gain-boundary identity, giving 58 exact rational assertions. These finite checks corroborate the algebra but do not replace the all-state proofs above. Run \(\texttt{python3 verify.py}\) in a directory containing the extracted program.

## Relationship to prior work

Shang (2023), Equations (3.1)–(3.3), defines the general noisy temporal-hypergraph model; its Theorem 2 and Corollary 3 give general sufficient **strict** small-gain conditions and random consensus results. That paper also examines rates under its hypotheses. The present statement specializes to a static single three-person hyperedge to obtain an exact conditional-amplification supremum and establish critical-gain inverse-linear mean-square agreement where strict-contraction results do not apply. Neuhäuser and collaborators investigate nonlinear higher-order deterministic consensus, without the independent noises and critical stochastic identity. Ni and Li study continuous-time noise-corrupted consensus, not this discrete higher-order critical endpoint. No general novelty is claimed for martingale convergence, Jensen's inequality, or the three-point distance identity.

## Limitations

The explicit threshold characterizes uniform **one-step mean-square contraction**, not an if-and-only-if boundary for every long-time concept of stochastic consensus. At the critical gain only \(S_t\to0\) almost surely and in mean square is established; a finite almost-sure or \(L^2\) limit for the common mean is not established. Above the critical gain, local expected expansion does not rule out eventual synchronization. The result assumes precisely three agents, one fixed hyperedge, mutually independent directed-pair noises, and the displayed nonlinear modulation. The inverse-linear expression is an upper bound, not a proved matching lower asymptotic rate. Priority relative to broader uninspected stochastic synchronization theory remains uncertain and independent assessment is outstanding.

## References

1. Y. Shang (2023), “Non-linear consensus dynamics on temporal hypergraphs with random noisy higher-order interactions,” *Journal of Complex Networks* 11(2), cnad009, DOI: 10.1093/comnet/cnad009. First online 13 March 2023. Open full text: https://academic.oup.com/comnet/article/11/2/cnad009/7076856.
2. L. Neuhäuser and collaborators (2020), higher-order nonlinear consensus on hypergraphs, arXiv:2004.00901. https://arxiv.org/abs/2004.00901.
3. W. Ni and D. Li (2013), consensus with multiplicative measurement noise, arXiv:1302.6685. https://arxiv.org/abs/1302.6685.
