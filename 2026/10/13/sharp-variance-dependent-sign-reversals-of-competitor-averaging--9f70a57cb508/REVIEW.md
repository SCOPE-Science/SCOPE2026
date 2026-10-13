# Self-review

## Correctness: PASS

The only interior state of a three-individual population with all three alleles present is \((1,1,1)\). Conditioning on its first nontrivial replacement supplies exactly four paths allowing target fixation; the other two immediately remove the target. Standard two-allele Moran absorption probabilities determine the four boundary continuation values. The resulting full rational expression and factorization are checked symbolically with positive denominators throughout \(a,b,c>0\). Every endpoint, symmetry case and strict/equality sign region is covered. A separate full transient Markov-chain solver using exact fractions reproduces seven examples. Limits: its finite sample checks do not substitute for the algebraic proof, and nothing is asserted for populations larger than three.

## Originality: PASS

The closest source, Braga--Wardil--Martinez-Garcia (arXiv:2604.12004v1), uses the same microscopic multiallele Moran update but gives a **first-order weak-selection** constant-fitness solution rather than an exact all-positive-fitness model-reduction error. Ferreira--Neves (arXiv:1811.09552v1) establish general finite multitype Moran equations and bounds, from which the tiny-state dynamics can be set up but not an already-stated averaging-bias sign classification. The 2026 Yuzbashyan--Feigel--Morozov paper investigates Wright--Fisher diffusion with a Kimura mean-field comparator and reports negative correction in the tested regimes; those claims do not cover a discrete exact Moran-vs-Moran comparison. The 2009 Lessard--Lahaie result concerns first-order diploid Wright--Fisher fixation, and the Rychtář--Taylor variance result concerns random fitness of two genotypes. Novelty is **only** the explicit sharp N=3 sign classification and fixed-mean variance crossover, not the process, general absorption method, or broad clonal-interference effect. Residual risks include unindexed exact small-population studies and limited full-text access to the two-genotype variance paper.

## Mathematical value: PASS

The exact bias answers whether merging two simultaneously present competitor alleles by their average can preserve the direction of fixation error. A three-individual population is the minimal finite model in which this question is nontrivial. A full parameter phase diagram and two rational witnesses show that varying competitor variance at a fixed mean can reverse the approximation error. This identifies a specific limitation of average-background reduction missed at first weak-selection order. The result is a sharp finite-population benchmark; it makes no empirical or large-population assertion.

Self-review: passed. Independent audit: not yet performed.
