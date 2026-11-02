# Review of the five-adic derangement residue census

## Correctness — PASS

The recurrence \(D_n=nD_{n-1}+(-1)^n\) and falling-factorial representation give \(D_n=(-1)^nF(n)\) for the uniformly convergent five-adic series \(F\). Each derivative tail beyond index nine vanishes modulo five. Direct polynomial evaluation yields \(F(a)\bmod5=(1,0,1,3,4)\) and \(F'(a)\bmod5=(1,3,4,2,4)\), so every residue disk has a unit slope. The difference quotient and digit lifting prove one preimage per matching disk at each power, giving the precise frequencies \((2,3,1,1,3)\). A standalone independent recurrence program confirms all complete periods through exponent six. Finite computations are supporting evidence only.

## Originality — PASS, subject to priority risk

The key antecedent is Piotr Miska (2015, arXiv:1508.01987): its period theorem and Hensel method are prior art, not new contributions. The exact five-adic preimage multiplicity distribution and surjectivity for every power of five were not found in the inspected relevant sections of that paper, in the earlier prime-level congruence works (arXiv:1008.1573; arXiv:1009.2929), or in the later general interpolation work (arXiv:2012.04615). The new claim does not assert a new general period law or new interpolation method. Specialized sources beyond those inspected could already imply the complete result; independent priority review is needed.

## Value — PASS

This is an exact, infinite-level classification of a natural arithmetic statistic: the distribution of fixed-point-free permutation counts over residue classes of prime powers. It proves universal five-adic coverage, gives nonuniform *exact* natural densities among indices and identifies the smallest prime with full prime-power coverage. These are stronger and more informative than repeating a period formula or listing computations at a fixed modulus.

## Scientific limitations

The result is for powers of five, not arbitrary prime powers; index density is distinct from density by numerical magnitude. The literature comparisons do not establish global novelty by exhaustion. The proof, not the finite verifier, carries the infinite quantifiers.

Self-review: passed. Independent audit: not yet performed.
