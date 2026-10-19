# Scientific review

## Correctness

PASS. The finite-population neutral Fermi specialization has independent Bernoulli copying decisions with rates \(a=p_s/2\) and \(b=p_g/2\). The proof derives the conditional drifts of the cross-population product and the paired empirical frequency, constructs an explicitly bounded harmonic martingale, and proves almost-sure absorption by a uniform positive-probability path. The ratio of drifts yields the exact common coefficient for both self-allowed and self-excluded model sampling. Symbolic differentiation proves the strict sharp parameter maximum. A packaged standard-library exact-rational checker passed 1,230 full-transition harmonic checks and 88 independent absorbing-chain solves. These finite tests are supporting evidence only; the algebra covers arbitrary population size and initial label alphabets.

## Originality

PASS under the documented search scope, with residual specialist-literature risk. The closest source [1] defines the exact independent game/strategy Fermi update (its Eq. (11)) and discusses selection-driven empirical correlations, but does not provide an exact neutral terminal joint distribution for arbitrary initial game and strategy labels. Source [2] has a coupled tolerance/opinion voter dynamics with feedback-conditioned rates and different model sampling; its quantitative conclusions do not imply this formula. The broader two-locus genealogy literature [3] supplies general mathematical machinery, but its stochastic generators and sampling-likelihood theorems do not state or directly cover this fixed-initial-condition joint terminal table under shared-pair independent imitation. Published mathematical-result searches for the explicit coefficient, duality, two-trait fixation and aliases did not identify a stronger covering claim. Missing or unindexed equivalent formulas remain possible.

## Value

PASS. The motivating source emphasizes strong game–strategy association, while its neutral reference dynamics had no exact joint-absorption benchmark. Here a single all-initial-state formula specifies the complete joint terminal table, proves exact preservation of zero initial association, and gives the sharp maximal amount of neutral coupling \(1/(N+1)\). The invariant clarifies how much of an observed terminal association could arise from shared parent sampling rather than selection, which is a mathematically natural and biologically interpretable comparison. The mechanism is restricted enough that no claim about empirical nonneutral selection is made.

## Closest literature and limitations

The main model and its transition rates are in [1]; [2] provides a mathematically distinct two-layer voter process; [3] develops broad ancestral-recombination machinery. This is a finite-size neutral specialization with no mutation, a shared focal/model pair and independent copying. It is not a proof about nonzero selection, general network structures, or correlated copy decisions. A classical two-locus duality argument might yield an equivalent formula in uninspected specialist literature.

## References

[1] Sadekar et al., *Evolutionary game selection creates cooperative environments*, arXiv:2311.11128 (2023), https://arxiv.org/abs/2311.11128.

[2] Vega-Oliveros et al., *Bi-layer voter model*, arXiv:2201.02218 (2022), https://arxiv.org/abs/2201.02218.

[3] Kamm et al., *Two-Locus Likelihoods Under Variable Population Size*, *Genetics* 203 (2016), https://doi.org/10.1534/genetics.115.184820.

Self-review: passed. Independent audit: not yet performed.
