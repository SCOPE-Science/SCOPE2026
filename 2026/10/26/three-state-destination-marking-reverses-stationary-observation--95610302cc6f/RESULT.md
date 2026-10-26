# Three-state destination marking reverses stationary-observation Kemeny defects

## Finding

For a finite irreducible semi-Markov process, mean first-passage times measured **immediately upon entering** a state yield a source-independent, stationary-target-weighted sum. At an arbitrary **stationary observation time**, however, that sum includes an exact destination-marking correction and need not be source-independent. This statement distinguishes the initial-age convention from the established entrance-time Kemeny theorem; it does not dispute that theorem.

Write \(H_{ij}\) for the expected first time to visit state \(j\) starting at a *fresh entrance* to state \(i\), and \(H_{ii}=0\). Let \(\pi\) be the continuous-time stationary state law and \(K=\sum_j\pi_j H_{ij}\), independent of \(i\). Write \(\widehat H_{ij}\) for the mean first hitting time conditional on being in state \(i\) at an **arbitrary stationary time**, with \(\widehat H_{ii}=0\); define \(\widehat K_i=\sum_j\pi_j\widehat H_{ij}\).

If \(m_i\) and \(u_i\) are the first and second moments of a newly entered state's holding duration and \(b_{ik}=\mathbb E[W_i\mathbf 1_{\{Y_i=k\}}]\) is the first marked duration moment, then

\[
\boxed{\widehat K_i=K+(1-\pi_i)\left(\frac{u_i}{2m_i}-m_i\right)-\pi_i\sum_k\left(\frac{b_{ik}}{m_i}-P_{ik}\right)H_{ki}.}
\]

Here \(P_{ik}\) is the embedded-chain probability of next visiting \(k\). In particular, if every marginal holding distribution has squared coefficient of variation one, the first correction vanishes; **destination-dependent durations can still produce either sign of defect**.

This sign ambiguity is attained on **three states**, but not on two states when self-jumps are forbidden: two-state jump destinations are deterministic, leaving no nontrivial duration–destination association.

Specifically, there are two three-state processes with identical embedded transition matrix, identical entire *unmarked* holding-time distribution at each state, identical stationary state law, and identical entrance-time hitting-time matrix, but for which

\[
\boxed{\bigl(\widehat K_1,\widehat K_2,\widehat K_3\bigr)
=\left(\frac{15}{7},\frac{16}{7},\frac{16}{7}\right)
\quad\text{or}\quad
\left(\frac{17}{7},\frac{16}{7},\frac{16}{7}\right),\qquad K=\frac{16}{7}.}
\]

Hence even perfect knowledge of the embedded transitions, all marginal holding laws, the stationary occupancy law and every entrance mean hitting time **does not identify** the random-target time to hit from a stationary observation. The association between the impending destination and the length of the ongoing interval is indispensable.

## Assumptions and scope

Let \(E=\{1,\ldots,N\}\) be finite with \(N\ge2\). On each entry to state \(i\), a new pair \((W_i,Y_i)\) is drawn with joint Markov-renewal kernel \(Q_{ik}(dw)=\Pr(W_i\in dw,Y_i=k)\). Assume that \(W_i>0\) almost surely, \(\mathbb E W_i^2=u_i<\infty\), and the embedded chain \(P_{ik}=Q_{ik}((0,\infty))\) is irreducible with \(P_{ii}=0\). Pairs on successive visits are independent conditional on their entry states. These conditions define a nonexplosive semi-Markov process; its stationary time law is the usual Markov-renewal equilibrium law, including equilibrium age and next-jump mark. The explicit example uses continuous nonlattice distributions.

Define \(m_i=\mathbb EW_i>0\), \(b_{ik}=\mathbb E[W_i\mathbf1_{\{Y_i=k\}}]\) and let \(\nu P=\nu\), \(\sum_i\nu_i=1\). The physical-time state stationary law is \(\pi_i=\nu_i m_i/\bar m\), where \(\bar m=\sum_i\nu_i m_i\). All hitting times count elapsed **physical time**, and the target state is sampled from \(\pi\) independently of the observed process. Both hitting-time matrices have zero diagonal: being already at the target gives hitting time zero, not a return time.

The two-state minimality statement refers to a duration–destination **marking defect when every unmarked squared coefficient of variation is one** and there are no self-jumps. It does not assert that all two-state age corrections vanish for arbitrary holding laws.

## Proof

**1. Entrance mean first-passage times and constancy.** For each fixed target \(j\), the Markov-renewal first-step identity is

\[
H_{ij}=m_i+\sum_k P_{ik}H_{kj}\quad(i\ne j),\qquad H_{jj}=0.
\]

The expected physical-time return between fresh entrances to state \(j\) is \(\bar m/\nu_j\): a stationary embedded renewal cycle contains \(1/\nu_j\) jumps on average, whose expected total duration is \(\bar m/\nu_j\) by the renewal-reward identity. Consequently

\[
(I-P)H_{\cdot j}=m-e_j\,\bar m/\nu_j.
\]

Multiplication of columns by \(\pi_j\) and summation give \((I-P)\big(\sum_j\pi_jH_{\cdot j}\big)=m-\bar m(\pi_i/\nu_i)_i=0\). The only right eigenvectors of an irreducible row-stochastic matrix at eigenvalue one are constant. Thus \(\sum_j\pi_j H_{ij}=K\) for every \(i\). This is the established entrance-time Kemeny property.

**2. Length-biased residual life with a marked destination.** At a stationary observation conditional on state \(i\), the current holding interval is length-biased, with conditional joint duration–mark measure \(wQ_{ik}(dw)/m_i\). Sampling a uniform location within the selected interval yields mean residual time \(r_i=u_i/(2m_i)\). Integrating the length-biased measure over the interval gives the next-state distribution

\[
q_{ik}=\Pr(Y_i=k\mid\text{stationary observation in }i)=b_{ik}/m_i.
\]

For \(j\ne i\), conditioning on the impending jump and then applying the strong Markov property at the next entrance yields

\[
\widehat H_{ij}=\frac{u_i}{2m_i}+\sum_k\frac{b_{ik}}{m_i}H_{kj}.
\]

The term \(k=j\) is harmless because \(H_{jj}=0\). No assumption that \(W_i\) and \(Y_i\) are independent is made.

**3. Weighted identity.** Subtract the first-step identity in step 1 from the equation in step 2, multiply by \(\pi_j\), and sum over \(j\ne i\). Since \(\sum_k(q_{ik}-P_{ik})=0\) and \(\sum_{j\ne i}\pi_j H_{kj}=K-\pi_i H_{ki}\), the difference is exactly

\[
\widehat K_i-K=(1-\pi_i)(r_i-m_i)-\pi_i\sum_k(q_{ik}-P_{ik})H_{ki},
\]

proving the formula. If holding duration and next-state mark are independent conditional on entry state, then \(b_{ik}=m_iP_{ik}\) and the last term vanishes. If the marginal squared coefficient of variation is one, then \(u_i=2m_i^2\), eliminating the first correction but **not** the marked term.

**4. Explicit pair with indistinguishable unmarked laws.** Take embedded transitions

\[
P=\begin{pmatrix}0&1/2&1/2\\1&0&0\\1&0&0\end{pmatrix}.
\]

On visits to states \(2\) and \(3\), hold independently of the next mark for exponential times of means \(1\) and \(2\), respectively. In state \(1\), each next destination has probability \(1/2\). Write \(G_1\) for a Gamma law of shape \(5/3\) and scale \(3/5\) (mean \(1\)), and \(G_3\) for a Gamma law of the **same shape** and scale \(9/5\) (mean \(3\)). Process \(A\) uses \(G_1\) before jumping to state \(2\) and \(G_3\) before state \(3\). Process \(B\) reverses these two associations, leaving their equal-probability mixture unaltered.

Both unmarked state-\(1\) holding laws equal \((G_1+G_3)/2\), with mean \(2\) and second moment \(8\). The respective unconditional means and second moments are therefore \(m=(2,1,2)\) and \(u=(8,2,8)\), giving \(u_i=2m_i^2\) for every state. The stationary embedded and physical-time laws are

\[
\nu=(1/2,1/4,1/4),\qquad \pi=(4/7,1/7,2/7).
\]

Solving the entrance first-step systems gives, for both processes,

\[
H=\begin{pmatrix}0&6&5\\1&0&6\\2&8&0\end{pmatrix},\qquad K=16/7.
\]

However, after conditioning on a stationary observation in state \(1\), the impending destination is state \(2\) with probability \(1/4\) under \(A\) and \(3/4\) under \(B\); the reverse holds for destination \(3\). The mean stationary residual time is \(2\) in both. Thus

\[
\begin{aligned}
(\widehat H_{12},\widehat H_{13})_A&=(8,7/2),\\
(\widehat H_{12},\widehat H_{13})_B&=(4,13/2).
\end{aligned}
\]

Multiplication by target weights \((\pi_2,\pi_3)=(1/7,2/7)\) yields \(\widehat K_1(A)=15/7\) and \(\widehat K_1(B)=17/7\). The exponential, destination-independent holds in states \(2\) and \(3\) yield \(\widehat K_2=\widehat K_3=K=16/7\). This establishes both directions of the nonidentifiability pair by exact arithmetic.

**5. Minimal number of states.** With two states and \(P_{ii}=0\), each next destination is deterministic, forcing \(q_{ik}=P_{ik}\) independently of the holding law. If both marginal squared coefficients of variation equal one, also \(r_i=m_i\), so \(\widehat K_i=K\) for both states. Three states are therefore the smallest class admitting the exhibited pure duration–destination marking phenomenon.

## Verification

The accompanying standalone script `verify.py` requires only Python's standard library and tests the two three-state examples using exact rational Gaussian elimination for stationary distributions and first-passage systems. It checks every reported fraction, the Gamma first and second moments, the marked residual laws, and the derived identity. It also checks the algebraic identity across 64 distinct rational three-state kernels under independent marking. Running `python verify.py` prints the output reproduced verbatim in `verification_output.txt`. The generic tests are finite consistency checks, not a substitute for steps 1–5.

## Relationship to prior work

Hunter (2018) analyzes several Kemeny functions for Markov renewal processes and establishes the stationary-target-weighted **fresh-entrance** constant. Voits (2026), Proposition 16 and its preceding hitting-time theorem, gives the graph-theoretic formulation of the same fresh-entrance constancy and motivates this question. These are not being claimed as new and are not contradicted by the stationary-observation distinction.

A related finite semi-Markov result for the same semi-Markov source characterizes when **fresh-entrance second hitting-time moments** coincide with those of a pseudo-rate Markov chain: it requires both unit marginal squared coefficients of variation and zero first marked-duration discrepancy. That result is acknowledged as a different moment-comparison problem. The present opposite-defect models deliberately have nonzero marked-duration discrepancy, and their distinction is in **stationary-observation first hitting-time averages** under identical entire unmarked holding laws, not in a Markov second-moment matching criterion.

Khorshidian and Fathizadeh (2022) derive general age-conditioned semi-Markov first-passage and mean residual-life formulas, so the *residual first-step principle itself is prior art*. The contribution assessed here is the precise weighted marked-duration defect, together with a minimal three-state pair proving that all unmarked holding laws and **all entrance mean hitting times combined** do not identify the equilibrium random-target mean, even when every marginal holding-time squared coefficient of variation equals one. General age-conditioned first-passage formulas can be specialized to derive some ingredients, and this limits the novelty of the derivation viewed in isolation. The published 2025 follow-up remains a plausible uninspected source for an equivalent specialization.

## Limitations

This concerns finite, irreducible Markov-renewal processes with finite holding-time second moments, zero diagonal of the embedded chain, and the stated *zero-at-target* hitting-time convention. It does not classify all stationary-observation Kemeny defects or assert uniqueness of the three-state witnesses. The two constructions establish failure of identifiability using the given reduced observables, not failure if the full marked kernel is known. The correction formula follows by standard renewal residual-life reasoning; scientific originality is concentrated in the exact minimal marked-observability obstruction. Historical priority is not independently certified, especially for all variants of the 2025 age-conditioned hitting-time literature. Independent audit has not been performed.

## References

1. J. B. Voits, *Graph-theoretic framework for semi-Markov networks: transient and stationary occupation probabilities, hitting times and weak ergodicity breaking* (2026), arXiv:2610.13505v1; https://arxiv.org/abs/2610.13505 (first publicly posted October 9, 2026; Proposition 16 and preceding sections).
2. J. J. Hunter, *Kemeny's Function for Markov Chains and Markov Renewal Processes* (2018), arXiv:1802.08330; https://arxiv.org/abs/1802.08330.
3. K. Khorshidian and M. Fathizadeh, *Conditional Hitting Time and Mean Residual life in Semi-Markov Models* (2022), DOI:10.21203/rs.3.rs-2184300/v1; https://doi.org/10.21203/rs.3.rs-2184300/v1.
4. M. Fathizadeh and K. Khorshidian, *Conditional hitting time and state-dependent measures in semi-Markov models* (2025), DOI:10.1080/03610926.2025.2483291; https://doi.org/10.1080/03610926.2025.2483291 (possible stronger prior coverage; full text not accessible in this review).
