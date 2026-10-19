# Two selection-strength reversals in a six-individual Moran game

## Finding
A single **nonnegative** three-strategy payoff matrix realizes two strict reversals in the fixation preference between two distinct rare mutants invading the *same* resident, as the strength of selection increases. Take
\[
M=\begin{pmatrix}23&3&7\\7&7&7\\7&10&0\end{pmatrix},\qquad N=6,
\]
with strategy order \(A,B,C\). Let \(\rho_A(w)\) be the probability that one \(A\) individual fixes among five \(B\) individuals, and let \(\rho_C(w)\) be the analogous probability for a single \(C\) individual in an otherwise \(B\) population. In both experiments, no further mutations occur.

Set \(z=e^w>1\) and
\[
P(z)=-z^{25}+2z^{24}-2z^{17}-z^{16}+z^{12}+1.
\]
The polynomial has exactly three positive roots: \(1\), \(\alpha\approx1.15219564351786\), and \(\beta\approx1.97922001091733\). For all \(w>0\),
\[
\rho_A(w)>\rho_C(w)\quad\Longleftrightarrow\quad 1<e^w<\alpha\ \text{or}\ e^w>\beta,
\]
while the reverse strict inequality holds for \(\alpha<e^w<\beta\). The positive crossover strengths are approximately \(0.1416693773\) and \(0.6827028332\). Equality also holds at zero selection.

## Assumptions and scope
There are exactly six individuals. At each step every individual plays all five *other* individuals in a well-mixed pairwise game, taking the arithmetic average of its row payoffs. Exponential fitness is \(f=e^{w\pi}\) with \(w>0\). Each transition selects one reproducer proportional to fitness and independently a uniformly random individual for replacement (including possibly the reproducer). The homogeneous all-mutant and all-resident states are absorbing. The object compared is single-mutant **fixation probability**, not fixation time or stationary abundance under recurrent mutation.

## Proof
For a pair of types \(X\in\{A,C\}\) and \(B\), let \(i\in\{1,2,3,4,5\}\) denote the number of \(X\) individuals. Under the specified no-self-interaction convention, their average payoffs are
\[
\pi_X(i)=\frac{(i-1)M_{XX}+(6-i)M_{XB}}{5},\qquad
\pi_B(i)=\frac{iM_{BX}+(5-i)M_{BB}}{5}.
\]
The payoff advantages and prefix sums are
\[
\begin{array}{c|ccccc}
 i&1&2&3&4&5\\\hline
 \pi_A(i)-\pi_B(i)&-4&0&4&8&12\\
 \sum_{j=1}^i[\pi_A(j)-\pi_B(j)]&-4&-4&0&8&20\\
 \pi_C(i)-\pi_B(i)&3&1&-1&-3&-5\\
 \sum_{j=1}^i[\pi_C(j)-\pi_B(j)]&3&4&3&0&-5
\end{array}.
\]
Let \(T_i^+\) and \(T_i^-\) be the probabilities of gaining and losing a mutant. The Moran update yields \(T_i^-/T_i^+=e^{w(\pi_B(i)-\pi_X(i))}\). Solving the standard absorbing birth-death recurrence, by successively taking differences, gives
\[
\rho_X(w)^{-1}=1+\sum_{k=1}^{5}
 \exp\left(-w\sum_{j=1}^{k}[\pi_X(j)-\pi_B(j)]\right).
\]
Substitution into this identity gives the two exact positive denominators
\[
D_A(z)=2+2z^4+z^{-8}+z^{-20},\qquad
D_C(z)=2+2z^{-3}+z^{-4}+z^5.
\]
Their difference satisfies
\[
z^{20}\big(D_A(z)-D_C(z)\big)=P(z).
\]
The descending sequence of nonzero coefficients of \(P\) is \((-1,2,-2,-1,1,1)\), which has **three sign changes**. Descartes' rule therefore bounds the number of its positive real roots, counted with multiplicity, by three. Direct exact arithmetic gives
\[
P(1)=0,\qquad P'(1)=-15<0,\qquad P(6/5)>0,\qquad P(2)<0.
\]
The intermediate value theorem forces a root in each disjoint interval \((1,6/5)\) and \((6/5,2)\). With the root at \(1\), these exhaust Descartes' upper bound, so the two nonunit roots are unique and simple. Since all denominators are positive, the sign of \(\rho_A-\rho_C\) is the **opposite** of the sign of \(P\). Its leading term is negative; the displayed sign tests and absence of further positive roots give the claimed strict three-regime ordering over all \(z>1\). This is an all-parameter proof, not an inference from sampled selection strengths.

## Verification
The accompanying standard-library-only `verify.py` reconstructs the payoff differences and prefix sums directly from the payoff matrix, verifies the polynomial identity using exact rational test values, and checks the fixation formula independently against the five-state absorbing Markov-chain linear system using rational Gaussian elimination. It checks the exact root sign bracket and coefficient variation count. Execute `python verify.py` with Python 3. No numerical root finding is required for the proof; the displayed decimal roots are approximations only.

## Relationship to prior work
Antal and colleagues (2009) analyze *weak-selection* evolutionary games with multiple strategies and mutation-selection equilibrium. Cooney, Allen and Veller (first preprint 2015) derive the same general Moran fixation recurrence under exponential fitness, but their main comparison is between opposite fixation directions in the *same two-strategy game* while varying assortment, rather than two distinct mutants invading a common third resident as selection strength changes. Wu and colleagues (2015) compare evolutionary update mechanisms, not the two same-model invaders considered here. General direct Moran fixation formulas and computational approaches also appear in the 2019 Scientific Reports study. The present contribution is a fully explicit exact **cross-mutant reentry** witness, not a new fixation formula. No claim of an exhaustive literature priority search is made.

## Limitations
The construction uses one deliberately chosen, frequency-dependent nonnegative payoff matrix; it is not a universal phenomenon or an empirical biological forecast. The two mutant invasions are separate rare-mutation experiments; a population containing both mutants may behave differently. The example does not establish the minimum population size or number of strategies needed for two crossovers. Independent audit and complete exclusion of equivalent older constructions are outstanding.

## References
- T. Antal et al., “Mutation–selection equilibrium in games with multiple strategies,” *Journal of Theoretical Biology*, first online publication 24 February 2009 (journal issue 21 June 2009), https://pmc.ncbi.nlm.nih.gov/articles/PMC2684574/ .
- D. Cooney, B. Allen, C. Veller, “Assortment and the evolution of cooperation in a Moran process with exponential fitness,” initial preprint 18 September 2015, arXiv:1509.05757, https://arxiv.org/html/1509.05757v2 .
- B. Wu, B. Bauer, T. Galla, A. Traulsen, “Fitness-based models and pairwise comparison models of evolutionary games are typically different—even in unstructured populations,” 2015.
- “Computation and Simulation of Evolutionary Game Dynamics in Finite Populations,” *Scientific Reports* 9 (2019), https://www.nature.com/articles/s41598-019-43102-z .
