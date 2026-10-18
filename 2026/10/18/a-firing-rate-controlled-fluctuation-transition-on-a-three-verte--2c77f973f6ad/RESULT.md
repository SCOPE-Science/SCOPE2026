# A firing-rate-controlled fluctuation transition on a three-vertex reinforced path

## Finding
Consider weak power reinforcement on the path with three vertices. Its two leaves have firing rate \(p>0\) each; its central vertex has rate \(q>0\); the reinforcement exponent satisfies \(0\leq\alpha<1\). Each firing chooses an incident edge in proportion to the \(\alpha\)-th power of its current weight and increments that edge by one. Let \(W_1(t),W_2(t)\) be the two edge weights, started at arbitrary deterministic positive values, and put
\[
R=q+2p,\qquad a=\frac{\alpha q}{R},\qquad D(t)=W_1(t)-W_2(t).
\]
For \(a<1/2\), the **joint edge-weight central limit theorem** is
\[
\frac{1}{\sqrt t}\begin{pmatrix}W_1(t)-Rt/2\\W_2(t)-Rt/2\end{pmatrix}
\ \Longrightarrow\ \mathcal N_2\!\left(0,\frac R4
\begin{pmatrix}1+v&1-v\\1-v&1+v\end{pmatrix}\right),\quad v=\frac1{1-2a}.
\]
In particular the limiting edge-weight correlation is exactly \(-a/(1-a)\), strictly negative when \(\alpha>0\). The imbalance alone satisfies
\[
\frac{D(t)}{\sqrt{Rt}}\Longrightarrow\mathcal N\!\left(0,\frac1{1-2a}\right).
\]
When \(a=1/2\), instead,
\[
\frac{D(t)}{\sqrt{Rt\log(Rt)}}\Longrightarrow\mathcal N(0,1),\qquad
\frac{(W_1(t)-Rt/2,W_2(t)-Rt/2)}{\sqrt{Rt\log(Rt)}}
\Longrightarrow (Z/2,-Z/2),\quad Z\sim\mathcal N(0,1).
\]
When \(a>1/2\), a finite random variable \(L\) exists for which
\[
\frac{D(t)}{(Rt)^a}\longrightarrow L\quad\hbox{almost surely},\qquad
\frac{(W_1(t)-Rt/2,W_2(t)-Rt/2)}{(Rt)^a}
\longrightarrow (L/2,-L/2)\quad\hbox{almost surely}.
\]
No nondegeneracy or distributional identification of \(L\) is asserted. The critical reinforcement exponent is
\[\alpha_c=\frac{R}{2q}=\frac12+\frac pq.\]
It is attainable within \(\alpha<1\) **if and only if** \(q>2p\). Thus unequal vertex firing rates can create a logarithmic-to-polynomial fluctuation transition even though the edge-weight proportions always converge to the same deterministic equilibrium.

## Assumptions and scope
All statements hold for fixed \(p,q>0\), every fixed \(\alpha\in[0,1)\), and arbitrary positive deterministic starting weights. Firing clocks are independent homogeneous Poisson processes, and each edge choice has a fresh independent uniform mark. Limits are as \(t\to\infty\). The theorem concerns exactly the three-vertex path and not arbitrary graphs or joint limits in parameters.

## Proof
**Embedded event chain.** The union of the three firing clocks is a rate-\(R\) Poisson process. Its successive interarrival times are independent of vertex labels and edge-choice marks. Write \(S_n=W_{1,n}+W_{2,n}=S_0+n\), \(D_n=W_{1,n}-W_{2,n}\), and \(X_n=D_n/S_n\). Let \(\xi_{n+1}\in\{-1,1\}\) be the signed edge increment and \(\mathcal F_n\) the embedded-chain filtration. Direct conditioning gives
\[
\mathbb E(\xi_{n+1}\mid\mathcal F_n)=c F_\alpha(X_n),\qquad
c=\frac qR,\quad F_\alpha(x)=\frac{(1+x)^\alpha-(1-x)^\alpha}{(1+x)^\alpha+(1-x)^\alpha}
=\tanh(\alpha\operatorname{artanh}x).
\]
The identity includes \(\alpha=0\) with \(F_0\equiv0\). Set \(U_{n+1}=\xi_{n+1}-cF_\alpha(X_n)\). Then exactly
\[
X_{n+1}=X_n+\frac{cF_\alpha(X_n)-X_n+U_{n+1}}{S_0+n+1},\quad
\mathbb E(U_{n+1}\mid\mathcal F_n)=0,\quad |U_{n+1}|\le2,
\]
\[
\mathbb E(U_{n+1}^2\mid\mathcal F_n)=1-c^2F_\alpha(X_n)^2.
\]
Since \(|F_\alpha(x)|\le|x|\) for \(|x|<1\) and \(\alpha<1\), the drift points strictly toward zero. The homogenization theorem [1, Theorem 1.1], independently applicable to this finite positive-rate model, gives \(X_n\to0\) almost surely (and follows also by the standard bounded-noise stochastic-approximation supermartingale argument). Consequently the conditional innovation variance tends to one. The derivative of the deterministic drift at zero is
\[
\left.\frac d{dx}\bigl[cF_\alpha(x)-x\bigr]\right|_{x=0}=a-1.
\]
Moreover \(F_\alpha(x)=\alpha x+O(x^3)\) near zero. Therefore the stochastic-approximation contraction coefficient is \(\lambda=1-a\), and the deviation of the actual coefficient from \(\lambda\) is \(O(X_n^2+1/n)\).

**All three regimes.** Applying the one-dimensional bounded-increment stochastic-approximation fluctuation theorem [2, Theorem 1 and Section 2.1] to the displayed exact recursion with noise variance one gives, for \(\lambda>1/2\),
\[
\sqrt n X_n\Longrightarrow\mathcal N\!\left(0,\frac1{2\lambda-1}\right).
\]
At \(\lambda=1/2\), the required logarithmic remainder condition follows from the power-decay estimate \(n^\beta X_n\to0\) almost surely for each \(\beta<1/2\) [2, Lemma 9], using the \(O(X_n^2+1/n)\) bound above. Hence
\[
\sqrt{\frac n{\log n}}X_n\Longrightarrow\mathcal N(0,1).
\]
For \(0<\lambda<1/2\), [2, Theorem 2] applies because its coefficient-error assumption \(O(|X_n|+1/n)\) follows from the same smooth expansion, and gives \(n^\lambda X_n\to L\) almost surely for a finite random variable. As \(D_n=S_nX_n\), these yield the imbalance limits after replacing \(n\) by its asymptotic equivalent \(Rt\).

**Joint limit and rates.** Writing \(N_t\) for the rate-\(R\) Poisson event count, the total weight is exactly \(S(t)=S_0+N_t\). The Poisson central limit theorem gives \((N_t-Rt)/\sqrt{Rt}\Rightarrow\mathcal N(0,1)\). Because the embedded edge-choice sequence is independent of the Poisson waiting times, this limit is jointly independent of the Gaussian imbalance limit (use conditional characteristic functions at random indices and \(N_t/(Rt)\to1\)). The identity \(W_{1,2}=(S\pm D)/2\) gives the covariance matrix. Its correlation equals \((1-v)/(1+v)=-a/(1-a)\). At and above the critical point, Poisson total-count noise is negligible on the respective larger scales; in the supercritical regime the Poisson law of the iterated logarithm yields \(N_t-Rt=O(\sqrt{t\log\log t})\) almost surely, so the two-dimensional almost-sure limit follows. Finally \(a=1/2\) is equivalent to \(\alpha=R/(2q)\), which lies below one exactly when \(q>2p\).

## Verification
The accompanying standalone Python program `verify.py` independently computes conditional edge-choice probabilities, signed drift, conditional variances, exact unreinforced binomial distributions, and finite-horizon distributions of the reinforced imbalance. Its assertions passed (935 deterministic checks); finite-horizon calculations do not prove any asymptotic claim. The infinite-time conclusions follow from the exact recurrence and the cited stochastic-approximation theorems. The distribution and potential nondegeneracy of the polynomial-scale limit \(L\) are not established.

## Relationship to prior work
Qin [1] proves homogenization of normalized edge weights for every sublinear reinforcement exponent and positive vertex firing rates; it does not give the three fluctuation regimes or the joint edge-weight covariance stated here. Renlund [2] proves general one-dimensional stochastic-approximation central-limit, critical logarithmic and subcritical convergence theorems; **those general limit theorems are prior mathematics**, and the contribution here is their explicit, parameter-sharp identification for the graph-based firing model, including the physical-time normalization, covariance law and rate threshold. Couzinié and Hirsch [3] study homogenization without these fluctuation formulas. Crimaldi, Dai Pra and Minelli [4] establish analogous scaling transitions in a distinct mean-field interacting-urn mechanism (simultaneous per-urn updates and a random synchronized limit), not this sequential edge-selection graph model.

## Limitations
The result is a specialized graph-model consequence of established general stochastic-approximation machinery, not a new general central-limit theorem. No claim is made that analogous thresholds hold on non-path graphs. The almost-sure supercritical limiting variable is not proved nondegenerate or otherwise characterized, and no uniformity holds as parameters vary toward a boundary. Independent priority verification of possible older graph-specific fluctuation formulas remains outstanding.

## References
[1] S. Qin, *Homogenization of weakly reinforced Pólya urns on countable networks*, arXiv:2610.11780v1 (first submitted 2026-10-08), Theorem 1.1 and Sections 1, 3. https://arxiv.org/html/2610.11780v1

[2] H. Renlund, *Limit theorems for stochastic approximation algorithms*, arXiv:1102.4741 (2011), Theorems 1–2, Section 2.1 and Lemma 9. https://arxiv.org/pdf/1102.4741

[3] Y. Couzinié and C. Hirsch, *Weakly reinforced Pólya urns on countable networks*, arXiv:2010.03347 (2020), Theorem 2.2. https://arxiv.org/pdf/2010.03347

[4] I. Crimaldi, P. Dai Pra, and I. G. Minelli, *Fluctuation Theorems for Synchronization of Interacting Pólya's urns*, arXiv:1407.5043 (2015), Theorems 3.3–3.5. https://arxiv.org/pdf/1407.5043
