# A spectral matching law and a four-level cooling enhancement of single-shot work extraction

## Finding

**Theorem.** Let \(d\ge2\), let \(E_0<E_1<\cdots<E_{d-1}\) be a finite, nondegenerate Hamiltonian spectrum, let \(\beta\ge0\), and let \(w>0\). Prepare the Gibbs state with level weights \(p_i(\beta)=e^{-\beta E_i}/Z_\beta\). Perform an arbitrary closed-system unitary stroke with the *same* initial and final Hamiltonian, and record extracted work by two projective energy measurements, \(W=E_i-E_j\).

For each source level define the number of threshold-eligible target levels
\[
 k_i(w)=\#\{j:E_j\le E_i-w\}.
\]
Start with the empty set \(G_w\), scan \(i=0,\ldots,d-1\) in increasing order, and include \(i\) exactly when \(k_i(w)>|G_w|\). Then the exact maximum over **all** unitaries is
\[
 \boxed{\sup_U\Pr_U\{W\ge w\}=\sum_{i\in G_w}\frac{e^{-\beta E_i}}{Z_\beta}.}
\]
A permutation unitary always attains the optimum, so coherence and transition mixing cannot improve the threshold-success probability. The chosen set \(G_w\) depends only on the spectrum and threshold, not on the positive temperature. When \(\beta>0\), every maximizing permutation has *exactly* \(G_w\) as its winning source levels. The optimum can be computed in \(O(d)\) additional operations after ordering the spectrum.

A second, sharp conclusion is a minimum-dimension result: in every dimension \(d\le3\), the optimized threshold-success probability is nonincreasing as inverse temperature \(\beta\) increases. This property fails already in dimension four. In particular, for
\[
 (E_0,E_1,E_2,E_3)=\left(0,2,\frac{19}{5},\frac{39}{10}\right),\qquad w=\frac{39}{20},
\]
only a transition to the ground level can meet the threshold, and
\[
 \boxed{\sup_U\Pr_U\{W\ge w\}=\frac{e^{-2\beta}}{1+e^{-2\beta}+e^{-19\beta/5}+e^{-39\beta/10}}.}
\]
This optimum initially **increases upon cooling** from infinite temperature, with right derivative \(17/160\) at \(\beta=0\), reaches a unique interior maximum at \(\beta_*=0.159740688468\ldots\) with probability \(0.258748957763\ldots\), and then decreases to zero. Nevertheless every positive-success protocol has strictly *negative mean extracted work* for every \(\beta>0\), by Gibbs passivity.

## Assumptions and scope

The Hilbert space is \(\mathbb C^d\), and the Hamiltonian is fixed at both measurement instants, with strictly increasing finite energies and no degeneracies. There is exactly one closed unitary stroke, with unrestricted unitary control and no heat contact, ancilla, feedback, measurement postselection, or constraint on stroke duration or driving strength. The two-point-measurement joint law is \(\Pr(i,j)=p_i(\beta)|U_{ji}|^2\), with a nonnegative extraction convention \(W=E_i-E_j\). The positive threshold \(w\) is inclusive; a statement about strictly positive work is obtained by taking any \(w>0\) smaller than the smallest positive spectral gap. All dimensions, inverse temperatures \(\beta\ge0\), and thresholds \(w>0\) are covered. The source-dimension uniqueness assertion requires \(\beta>0\).

## Proof

**1. Unitary reduction to a weighted spectral matching.** The matrix \(T_{ji}=|U_{ji}|^2\) is doubly stochastic, and the objective \(\sum_i p_i\sum_{j:E_i-E_j\ge w}T_{ji}\) is linear in \(T\). By the Birkhoff--von Neumann decomposition, any such matrix is a convex combination of permutation matrices. Every permutation matrix is itself induced by a unitary, so maximizing among all unitaries is *exactly* the maximum among permutations; optimizing over the larger doubly stochastic polytope introduces no gap.

A winning source level \(i\) can be sent to precisely the target indices \(0,\ldots,k_i(w)-1\). Because \(w>0\) and the energies increase strictly, \(k_0=0\), \(0\le k_i\le i\), and the allowed target sets are nested as \(i\) increases. Given winning source indices \(s_1<\cdots<s_m\), a permutation realizing success at all these indices exists if and only if
\[
 \boxed{k_{s_t}(w)\ge t\quad\text{for each }1\le t\le m.}
\]
Necessity follows because the first \(t\) winning sources have only \(k_{s_t}\) distinct target levels in their union. Sufficiency follows by assigning \(s_t\) to target \(t-1\) for each \(t\), then completing the partial one-to-one assignment arbitrarily to a permutation.

**2. Optimality of the greedy source set.** Denote the ascending greedy indices by \(g_1<\cdots<g_r\). The algorithm selects \(g_t\) as the earliest available index after \(g_{t-1}\) for which \(k_{g_t}\ge t\). For any feasible winning set \(s_1<\cdots<s_m\), induction on \(t\) shows \(s_t\ge g_t\) for every \(t\le m\); feasibility ensures the requisite \(k_{s_t}\ge t\). In particular \(m\le r\). Since the Gibbs weights satisfy \(p_0\ge p_1\ge\cdots>0\),
\[
 \sum_{t=1}^{m}p_{s_t}\le\sum_{t=1}^{m}p_{g_t}\le\sum_{t=1}^{r}p_{g_t}.
\]
The constructed permutation attaining success on \(G_w\) proves equality in the claimed optimum. At \(\beta>0\) the Gibbs weights are strictly decreasing: either a missing greedy source or any strictly larger winning index causes a strict loss. Thus every optimal permutation wins at precisely \(G_w\). More generally, any optimizing unistochastic matrix can be decomposed into winning-set-optimal permutations. One may calculate all \(k_i\) using a single moving destination pointer, followed by the linear greedy scan.

**3. Why two and three levels cannot benefit from cooling.** Write \(\bar E_\beta=\sum_i p_iE_i\). Direct differentiation gives
\[
 p_i'(\beta)=p_i(\bar E_\beta-E_i),\qquad
 \bar E_\beta'=-\operatorname{Var}_\beta(E)<0.
\]
For \(d=2\), the only nonempty greedy set is \(\{1\}\); its probability decreases with \(\beta\). For \(d=3\), the only possible nonempty greedy sets are \(\{2\}\), \(\{1\}\), and \(\{1,2\}\). The probability for \(\{2\}\) decreases because \(E_2>\bar E_\beta\). The probability for \(\{1,2\}\) is \(1-p_0\), which decreases because \(p_0\) increases. To obtain \(G_w=\{1\}\), write \(\Delta_1=E_1-E_0\) and \(\Delta_2=E_2-E_1\). Necessarily \(\Delta_2<w\le\Delta_1\), so \(\Delta_2<\Delta_1\). Therefore \(\bar E_0-E_1=(\Delta_2-\Delta_1)/3<0\), and the strict decrease of \(\bar E_\beta\) forces \(p_1'(\beta)<0\) at every \(\beta\ge0\). Empty greedy sets give zero. This proves the dimension bound.

**4. Four-level witness and uniqueness of the thermal peak.** In the displayed spectrum, \(E_i-E_0\ge w\) for \(i=1,2,3\), whereas \(E_i-E_j<w\) whenever \(i>j\ge1\), since the largest excited-sector gap is \(E_3-E_1=19/10<w=39/20\). Thus \(k_1=k_2=k_3=1\) and \(G_w=\{1\}\). The formula becomes \(p_1(\beta)\). Its uniform-temperature energy mean is \(\bar E_0=97/40\), hence
\[
 p_1'(0)=\frac14\left(\frac{97}{40}-2\right)=\frac{17}{160}>0.
\]
As \(\beta\to\infty\), \(\bar E_\beta\to E_0=0<2\); since \(\bar E_\beta\) is strictly decreasing, there is exactly one \(\beta_*>0\) at which \(p_1'(\beta_*)=0\). Its exact defining equation is
\[
 -2+\frac95 e^{-19\beta_*/5}+\frac{19}{10}e^{-39\beta_*/10}=0.
\]
Monotonicity of \(\bar E_\beta\) proves this point is the unique global maximizer; the numerical values in the finding follow by root isolation and evaluation.

**5. Mean work remains negative.** With \(q_j=\sum_iT_{ji}p_i\), doubly stochastic mixing implies \(\sum_{j=0}^{m-1}q_j\le\sum_{j=0}^{m-1}p_j\) for each \(1\le m<d\). Summation by parts yields
\[
 \sum_j q_jE_j-\sum_i p_iE_i
 =\sum_{m=1}^{d-1}(E_m-E_{m-1})
 \left(\sum_{i=0}^{m-1}p_i-\sum_{j=0}^{m-1}q_j\right)\ge0.
\]
For \(\beta>0\), all Gibbs weights are distinct; if a unitary produces positive-probability energy-lowering transitions, at least one majorization inequality is strict. Thus \(\mathbb EW<0\) despite any cooling-induced improvement in the probability of a successful shot. This is consistent with, rather than a violation of, thermal passivity.

## Verification

The self-contained Python 3 script `check.py` exhaustively compares the greedy formula with the best of every permutation of the levels for 325 deterministic integral-spectrum instances spanning dimensions two through six. All comparisons use exact rational Gibbs weights and include thresholds coinciding with energy gaps, so equality conventions are exercised. It also checks the maximizing source sets of every optimal permutation. A separate four-level test verifies the exact \(17/160\) temperature derivative, strict passivity at test temperatures, and the location and value of the unique thermal maximum. Running `python3 check.py` prints one `PASS` line. These finite computations corroborate but do not substitute for the dimension-uniform proof above.

## Relationship to prior work

Cheng et al. (arXiv:2610.30555, first public October 22, 2026) examine Gibbs-weighted two-projective-measurement work statistics of finite-rate, two-stroke quasiperiodic quantum Otto engines and report trajectories with positive work more frequently than their negative mean suggests (Sections II, IV and Appendix C). Their cycle combines two isolated strokes with thermal contacts, whereas the theorem here concerns a single closed unitary at fixed initial/final spectrum and maximizes its probability of exceeding a positive work threshold over *all* unitaries. The greedy spectral-matching formula and the dimension-four onset of nonmonotonic temperature dependence are not among their stated results.

Cavina, Mari and Giovannetti (Scientific Reports **6**, 29282, 2016) optimize threshold-work success for general Jarzynski-compatible transformations, including protocols with quasi-static isothermal transformations and complete thermalizations (Introduction, main results and Methods for multi-level systems). Their optimized operation class allows thermal contact and intermediate Hamiltonian changes, so their general-protocol probability bounds and attainable two-point work distributions do not provide the exact probability within the restricted one-stroke, fixed-spectrum, closed-unitary class. Standard Gibbs passivity, Birkhoff's theorem and nested-neighborhood matching are acknowledged established ingredients; the claim does not assert novelty for those facts in isolation.

## Limitations

The result does not optimize two-stroke Otto engines, feedback-assisted or bath-assisted extraction, coherent non-TPM work quasiprobabilities, constrained driving, finite-time control cost, or degenerate spectra. The \(d=4\) temperature effect is a finite-system unitary threshold-probability effect, not a claim about monotonic engine output or majority-positive cycles. The greedy algorithm is an application of classical matching, and broader unlocated work-tail optimization results could imply parts of the theorem. Originality conclusions are based on specific accessible searches and comparisons, not proof of absolute priority. No independent mathematical validation has yet occurred.

## References

1. Shujie Cheng, Lucas C. Céleri, Norton G. de Almeida, Gao Xianlong and G. D. de Moraes Neto, *Probing quasiperiodic spectral accessibility with a finite-rate quantum Otto cycle*, arXiv:2610.30555 (first public 2026-10-22), https://arxiv.org/abs/2610.30555.
2. Vasco Cavina, Andrea Mari and Vittorio Giovannetti, *Optimal processes for probabilistic work extraction beyond the second law*, Scientific Reports **6**, 29282 (2016), https://doi.org/10.1038/srep29282.
3. Raffaele Salvia and Vittorio Giovannetti, *Zero-Fluctuation Quantum Work Extraction*, arXiv:2402.16964 (2024), https://arxiv.org/abs/2402.16964.
4. Standard mathematical ingredients: Birkhoff--von Neumann decomposition of finite doubly stochastic matrices, Hall's marriage theorem for nested neighborhoods, and majorization/rearrangement inequalities.
