# An operator-order test and rising-hazard protection for unitary quantum resetting

## Finding

Consider an arbitrary finite-dimensional quantum system (dimension at least two) with unitary gate \(U\), a fixed reset density operator \(\tau\), and independent renewal waiting times. At waiting-time age \(j\ge1\), a reset occurs with probability \(r_j\in[0,1)\); otherwise the system undergoes \(X\mapsto UXU^\dagger\). Each reset replaces the state by \(\tau\), and restarts the waiting-time age. Write
\[
 S_0=1,\qquad S_t=\prod_{j=1}^{t}(1-r_j),\qquad f_j=S_{j-1}r_j,
\]
where \(S_t>0\) for every finite \(t\). Let \(\nu_k\) be the renewal-event probability at step \(k\), explicitly
\[
 \nu_k=f_k+\sum_{j=1}^{k-1}f_j\nu_{k-j},\qquad k\ge1.
\]
Define the unnormalized last-reset operator
\[
 A_0=0,\qquad
 A_t=\sum_{k=1}^{t}\nu_k S_{t-k} U^{t-k}\tau(U^\dagger)^{t-k}.
\]

**Exact divisibility criterion.** For every pair of integers \(0\le s<t\), the intervening Schrödinger-picture map is positive **if and only if** it is completely positive, and these conditions hold **if and only if**
\[
 \boxed{A_t-\frac{S_t}{S_s}U^{t-s}A_s(U^\dagger)^{t-s}\succeq0.}
\]
Here \(\succeq0\) means positive semidefinite operator order. Thus the entire evolution is positive divisible if and only if it is completely positive divisible, with an exact finite-matrix test at each adjacent step.

**Increasing-age-hazard theorem.** If \(r_{j+1}\ge r_j\) for every \(j\ge1\), then the evolution is completely positive divisible for *every* choice of dimension, unitary gate, and reset state. In particular the nonconstant ramp \(r_j=\min\{0.08,0.001(j-1)\}\), appearing in the motivating paper's correlation-engineering example, has this property at every finite time.

**Sharp failure on a decreasing-hazard pair.** Take a qubit, \(\tau=|0\rangle\langle0|\), and \(U|0\rangle=|1\rangle\), \(U|1\rangle=|0\rangle\). If \(r_1=p\), \(r_2=q\), with \(0\le q<p<1\), the intervening map from step one to two is not positive. Its operator-test matrix has the strictly negative eigenvalue \(p(q-p)\), although the trace distance of *every* pair of initial states is nonincreasing at *every* step. The monotonic-hazard sufficient hypothesis therefore cannot be dropped as an unrestricted guarantee.

## Assumptions and scope

The reset clock is a classical renewal process: after each reset its independent next waiting time follows the same age-hazard sequence. Gate applications and resets occur at integer times; a reset replaces, rather than follows, the gate at its time step. The gate and reset state are fixed for all steps. The initial state is arbitrary, and all claims concern the averaged single-time channels in the Schrödinger picture. Strict inequalities \(r_j<1\) ensure their linear invertibility; cases with sure finite-time resets are not included. The dimension is any finite integer \(d\ge2\). The results make no assertion about Heisenberg-picture divisibility or Markovianity of multi-time process tensors.

## Proof

**1. Renewal expansion and normalization.** The probability of no reset in the first \(t\) steps is \(S_t\). For any reset at time \(k\), the probability of no subsequent reset until time \(t\) is \(S_{t-k}\). The renewal identity for \(\nu_k\) accounts for every possible preceding reset. Conditioning on the final reset therefore gives, for every operator \(X\),
\[
 \Phi_t(X)=S_t U^tX(U^\dagger)^t+\operatorname{tr}(X)A_t.
\]
Since histories either have no reset or a unique final reset, \(A_t\succeq0\) and \(\operatorname{tr}A_t=1-S_t\). This is a completely positive, trace-preserving map at each time.

**2. Exact inverse and intervening map.** For \(S_s>0\), the inverse of \(\Phi_s\) as a linear map on operators is well-defined because its traceless part is multiplication by \(S_s\) followed by unitary conjugation and its trace is conserved. Direct substitution gives
\[
 \Phi_t\Phi_s^{-1}(Y)=a_{t,s}U^{t-s}Y(U^\dagger)^{t-s}
 +\operatorname{tr}(Y)Q_{t,s},
\]
where
\[
 a_{t,s}=\frac{S_t}{S_s}\in(0,1],\quad
 Q_{t,s}=A_t-a_{t,s}U^{t-s}A_s(U^\dagger)^{t-s},\quad
 \operatorname{tr}Q_{t,s}=1-a_{t,s}.
\]
If \(Q_{t,s}\succeq0\), the expression is a sum of a unitary completely positive map with nonnegative weight \(a_{t,s}\) and a positive replacement operation; hence it is completely positive and trace-preserving. Conversely, if \(Q_{t,s}\) has a negative eigenvector \(|v\rangle\), choose a unit vector \(|w\rangle\perp|v\rangle\), which exists since \(d\ge2\), and choose the input projector \(Y=U^{-(t-s)}|w\rangle\langle w|U^{t-s}\). Its output has expectation \(\langle v|Q_{t,s}|v\rangle<0\) in \(|v\rangle\), so the intervening map is not even positive. This proves the exact equivalence. Adjacent positivity implies positivity for every interval by composition, giving the full evolution criterion.

**3. Rising hazards.** For \(t\ge1\), expand the adjacent order-test matrix using the renewal expansion, \(S_{j+1}=S_j(1-r_{j+1})\), and \(S_{t+1}/S_t=1-r_{t+1}\):
\[
 \boxed{
 Q_{t+1,t}=\nu_{t+1}\tau+
 \sum_{k=1}^{t}\nu_k S_{t-k}
 (r_{t+1}-r_{t+1-k})
 U^{t+1-k}\tau(U^\dagger)^{t+1-k}.}
\]
Every summand is positive semidefinite when the age hazard is nondecreasing. Therefore \(Q_{t+1,t}\succeq0\) for all \(t\); the case \(t=0\) follows from \(\Phi_1\) being a channel. Hence the entire evolution is completely positive divisible. The specified increasing ramp satisfies these inequalities and never attains probability one.

**4. Exact two-step obstruction.** For \(r_1=p\), \(r_2=q\), one has \(\nu_1=p\) and \(\nu_2=p^2+(1-p)q\). The adjacent test is
\[
 Q_{2,1}=\bigl[p^2+(1-p)q\bigr]\tau+p(q-p)U\tau U^\dagger.
\]
For the bit-flip and pure reset above, the two projectors are orthogonal. The second eigenvalue is exactly \(p(q-p)<0\), disproving positivity. Nevertheless, for any two density operators \(\rho,\sigma\), cancellation of the reset term gives
\[
 \tfrac12\|\Phi_t(\rho)-\Phi_t(\sigma)\|_1
 =S_t\tfrac12\|\rho-\sigma\|_1.
\]
The sequence \(S_t\) is nonincreasing for every classical hazard law, so this failure of positive divisibility has no two-state trace-distance revival. This completes the proof.

## Verification

Run `python verify.py` with the NumPy dependency specified in `requirements.txt`. It reconstructs renewal-event probabilities in two ways (convolution and enumeration of all reset/no-reset histories for short horizons), verifies channel normalizations, computes exact intervening-map compositions, compares positive semidefiniteness of the order-test matrices with the Choi conditions, tests random nondecreasing hazards in dimensions two through four, checks the analytic qubit obstruction for several parameter pairs, and tests 99 adjacent steps of the rising ramp. The recorded run passed 13,298 finite assertions.

These finite checks are not a proof of the all-dimensional or all-time assertions, which follow from the analytic matrix-order argument above. Small numerical negative eigenvalues near zero are judged with a specified floating-point tolerance; the exact qubit obstruction has the algebraic negative eigenvalue above.

## Relationship to prior work

Carollo and Wald (arXiv:2601.13367, 2026) provide the discrete-time renewal channel, numerical examples of Schrödinger and Heisenberg indivisibility, a periodic protocol that is Schrödinger CP-divisible, and a rising-hazard correlation-engineering ramp. Their result does not state the all-dimensional if-and-only-if operator-order criterion, the rising-hazard sufficient theorem, or the explicit two-step decreasing-hazard obstruction. The renewal-channel formula itself is prior art and is not claimed as new here. The ramp consequence says only that its **single-time Schrödinger maps** are CP-divisible; it does not negate the paper's discussion of other kinds of memory.

Settimo and collaborators (arXiv:2506.08103, 2025) establish the distinction between Schrödinger and Heisenberg divisibility and analyze explicit qubit examples, but not the present renewal last-reset order condition. Megier, Smirne, and Vacchini (Entropy 22, 796, 2020) develop quantum semi-Markov descriptions and show CP-divisibility in a different diagonalizing-jump case for arbitrary waiting-time laws; it does not imply the all-unitary/noncommuting-reset hazard theorem without additional work. Megier, Ponzi, Smirne, and Vacchini (Entropy 23, 905, 2021) focus on renewal processes and trace-distance witnesses, a weaker diagnostic for the exact obstruction here. Earlier general distinguishability/divisibility criteria are consistent with, but do not by themselves provide, this model-specific order test. No independent exhaustive priority search has been performed.

## Limitations

The theorem does not classify processes after a survival probability becomes zero, nonunitary between-reset channels, conditional quantum resets, or individual multi-time trajectory memory. Nondecreasing age hazard is sufficient, but it is **not claimed necessary** for a particular gate and reset state. The example proving the sufficient hypothesis cannot simply be removed is a two-age witness; no universal converse over arbitrary hazard sequences is asserted. Source-priority assessment is qualified by the possibility of a broader earlier theorem covering the same affine channel subclass.

## References

1. F. Carollo and S. Wald, *Stochastic resetting induces quantum non-Markovianity*, arXiv:2601.13367 (first submitted 19 January 2026). https://arxiv.org/abs/2601.13367
2. F. Settimo et al., *Divisibility of dynamical maps: Schrödinger vs. Heisenberg picture*, arXiv:2506.08103 (2025). https://arxiv.org/abs/2506.08103
3. N. Megier, A. Smirne, and B. Vacchini, *Evolution Equations for Quantum Semi-Markov Dynamics*, Entropy 22, 796 (2020). https://doi.org/10.3390/e22070796
4. N. Megier, M. Ponzi, A. Smirne, and B. Vacchini, *Memory Effects in Quantum Dynamics Modelled by Quantum Renewal Processes*, Entropy 23, 905 (2021). https://doi.org/10.3390/e23070905
5. S. Utagi, S. Banerjee, and R. Srikanth, *On the non-Markovianity of quantum semi-Markov processes*, arXiv:2012.11219 (2020). https://arxiv.org/abs/2012.11219
