# A complete Poisson–binomial classification for stationary binary Markov switch counts

## Finding
Consider a stationary irreducible two-state Markov chain with transition matrix
\[
P=\begin{pmatrix}1-a&a\\b&1-b\end{pmatrix},\qquad 0<a,b<1.
\]
For every integer \(m\ge2\), let \(T_m=\sum_{i=0}^{m-1}\mathbf1\{X_i\ne X_{i+1}\}\) count state changes in \(m\) transitions. Then
\[
T_m\text{ is Poisson–binomial}\quad\Longleftrightarrow\quad a=b.
\]
In the symmetric case, \(T_m\sim\operatorname{Bin}(m,a)\). In every asymmetric case, the following *exact, strictly positive* variance gap excludes any independent-Bernoulli representation:
\[
\operatorname{Var}(T_m)-m\mu(1-\mu)
=\frac{2ab(a-b)^2}{(a+b)^2}\,
\frac{(m-1)-m\lambda+\lambda^m}{(1-\lambda)^2}>0,
\quad\mu=\frac{2ab}{a+b},\quad\lambda=1-a-b.
\]
This statement includes negative \(\lambda\), where nonadjacent switch indicators may have negative covariances. For \(m=1\), the count is Bernoulli under every stationary chain, so \(m=2\) is the earliest informative horizon.

## Assumptions and scope
The chain is stationary, with \(\Pr(X_i=0)=b/(a+b)\) and \(\Pr(X_i=1)=a/(a+b)\). Both transition probabilities are strictly interior. A Poisson–binomial distribution means the law of a sum of \(m\) independent Bernoulli variables with possibly distinct parameters in \([0,1]\). This definition does not require the actual switch indicators to be independent.

## Proof
Put \(J_i=\mathbf1\{X_i\ne X_{i+1}\}\). Stationarity gives \(\mathbb E J_i=\mu=2ab/(a+b)\). For consecutive switches, the two possible alternating three-state paths have total probability \(ab\), so
\[
\operatorname{Cov}(J_i,J_{i+1})=ab-\mu^2
=\frac{ab(a-b)^2}{(a+b)^2}=:c.
\]
The nonconstant eigenvalue of \(P\) is \(\lambda=1-a-b\). Let \(u(s)=\Pr(J_{i+1}=1\mid X_{i+1}=s)\), so \(u(0)=a\), \(u(1)=b\). For every integer \(h\ge1\), the two-state transition relation implies
\[
\mathbb E(J_{i+h}\mid X_{i+1})
=\mu+\lambda^{h-1}\bigl(u(X_{i+1})-\mu\bigr).
\]
The Markov property therefore yields
\[
\operatorname{Cov}(J_i,J_{i+h})=c\lambda^{h-1}
\quad(h\ge1).
\]
Summing diagonal and off-diagonal terms gives
\[
\operatorname{Var}(T_m)=m\mu(1-\mu)
+2c\sum_{h=1}^{m-1}(m-h)\lambda^{h-1}.
\]
For \(\lambda\ne1\), the sum is \(((m-1)-m\lambda+\lambda^m)/(1-\lambda)^2\). Its numerator \(f(\lambda)=(m-1)-m\lambda+\lambda^m\) satisfies \(f(1)=0\) and \(f'(\lambda)=m(\lambda^{m-1}-1)<0\) for every \(-1<\lambda<1\). Thus \(f(\lambda)>0\). Because \(c>0\) whenever \(a\ne b\), the asserted gap is strictly positive.

If \(T_m\) were distributed as \(\sum_{j=1}^m B_j\) with independent Bernoulli parameters \(q_j\), its mean would give \(\sum_jq_j=m\mu\), while Jensen's inequality implies
\[
\operatorname{Var}\Bigl(\sum_jB_j\Bigr)=\sum_jq_j(1-q_j)\le m\mu(1-\mu).
\]
This contradicts the strict variance gap when \(a\ne b\). Conversely, if \(a=b\), the conditional probability of a switch is \(a\) regardless of the current state. By iterated conditioning all \(J_i\) are independent Bernoulli\((a)\), proving the converse and binomial formula. For \(m=1\), stationarity makes \(J_0\) Bernoulli\((\mu)\) irrespective of symmetry. This completes the proof.

## Verification
The independent arithmetic checker `verify.py` enumerates all binary paths of lengths \(m+1\) with rational stationary Markov probabilities and compares exact empirical probability generating coefficients, means, variances, every individual lag covariance, and the closed-form variance expression. It checks multiple regimes of positive, zero, and negative \(\lambda\). The enumerations are finite corroboration; the preceding proof establishes the statement for every interior real \(a,b\) and every integer \(m\ge2\).

## Relationship to prior work
Engländer and Volkov's *Turning a Coin over Instead of Tossing It* identifies independent turn counts in a symmetric (possibly inhomogeneous) two-state chain. Dekking and Kong's *Multimodality of the Markov binomial distribution* studies the **occupation count** \(\sum_i\mathbf1\{X_i=1\}\) and its variance, not the **number of changes** \(\sum_i\mathbf1\{X_i\ne X_{i+1}\}\). Baker's 2020 *Discrete distributions from a Markov chain* develops related Markov-dependent count models. The classification here is specific to the stationary switch count; the distinction between occupation and switch counts is essential, and the symmetric implication is known from Engländer and Volkov.

## Limitations
Initial stationarity and a two-state homogeneous model are assumed. No characterization for arbitrary initial distributions, time-inhomogeneous asymmetric chains, or alphabets with more than two states is claimed. The finding does not assert novelty for the elementary variance identity in isolation; the proposed contribution is the exact, all-horizon distribution-class boundary. Equivalence under unsearched alternate terminology remains a historical risk. No independent audit has been performed.

## References
1. Engländer, J. and Volkov, S., *Turning a Coin over Instead of Tossing It*, Journal of Theoretical Probability (2018), first online 25 November 2016, https://doi.org/10.1007/s10959-016-0725-1.
2. Dekking, M. and Kong, D., *Multimodality of the Markov binomial distribution*, Journal of Applied Probability 48 (2011), 938–953; arXiv:1102.3613, first public 17 February 2011.
3. Baker, R., *Discrete distributions from a Markov chain*, arXiv:2006.13766, first public 24 June 2020.
