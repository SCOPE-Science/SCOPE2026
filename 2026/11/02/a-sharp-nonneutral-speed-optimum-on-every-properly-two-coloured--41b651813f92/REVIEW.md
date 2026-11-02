# Scientific review of a nonneutral speed optimum on a Moran star

## Correctness — PASS

The finding specifies a discrete, habitat-matched birth–death chain on an undirected \(\ell\)-leaf star with \(\ell\ge2\), \(r>0\), and a single red individual at the RED hub. The proof verifies the four nontrivial update probabilities, conditions on a genotype-changing step, and obtains an \(r\)-independent two-branch embedded chain. Its bounded martingale \(h+\ell k\) establishes the full-state fixation harmonic function. Transient visit balance, Doob conditioning by that function, and exact geometric holding times yield \(T_\ell(r)=A_\ell r+B_\ell+C_\ell/r\) with explicitly summed rational/harmonic coefficients. Because \(C_\ell>A_\ell>0\), differentiation proves the unique minimizer \(r_\ell^*>1\). The full-configuration rational verifier independently checks the formula on labelled states, rather than assuming the symmetry-reduced equations, and the separate jump-chain checks agree: 128 exact assertions passed. Tests do not substitute for the all-parameter proof.

## Originality — PASS within inspected literature, with residual priority risk

The matching-fitness process and \(r\)-independence of fixation probability are explicitly **known** in Maciejewski–Puleo (2013), Theorem 1; the finding claims neither as a new principle. Their duration discussion studies a different three-background-colour comparison, not the exact all-size two-colour star speed law. Broom–Hadjichrysanthou–Rychtář (2010) give general star equations for genotype-constant fitness or pairwise game payoffs, whose genotype-only payoff matrix cannot identify a red hub and red leaf with different fecundities under identical neighbouring genotypes; their equations do not state this harmonic closed form or optimizer. Hindersin–Traulsen (2014) study constant mutant fitness rather than fixed matching habitats. Kaveh et al. (2020) explicitly include two-chromatic stars but derive fixation-probability laws rather than the conditional duration and speed minimum. The inspected statements are not equivalent to or stronger than the specific theorem, although the universal finite-state Markov recurrence is prior mathematical machinery. No claim of independent novelty certification is made; a hidden equivalent historical computation remains possible.

Primary comparisons: https://arxiv.org/abs/1311.3214 ; https://openaccess.city.ac.uk/id/eprint/1005/1/Evolutionary%20games%20on%20graphs%20and%20the%20speed%20of%20the%20evolutionary%20process_Final.pdf ; https://arxiv.org/abs/1406.4415 ; https://doi.org/10.1371/journal.pcbi.1008402 .

## Value — PASS

Proper graph colourings were introduced to separate habitat adaptation from genotype-wide fitness advantage, and the known neutrality of the *fixation probability* creates a meaningful question: can an adaptation parameter change *how quickly* fixation occurs without changing *whether* it occurs? The theorem answers this question uniformly for every number of star leaves, identifies a unique strict optimum beyond neutrality, proves a harmonic closed form, and exhibits a vanishing large-network departure from neutral selection. It isolates a structural difference between successful trajectory geometry (unchanged) and waiting times (changed), usable as a benchmark for finite stochastic evolutionary systems. It is more than a single small-case computation or a renaming of a textbook formula. Biological extrapolation and general graph extensions are explicitly excluded.

## Limits and audit status

The proof covers only the stated hub-initialized, properly two-coloured, discrete-time star; fixation may behave differently under other start positions or clock conventions. Literature priority remains provisional; no external or independent scientific review has been performed.

Self-review: passed. Independent audit: not yet performed.
