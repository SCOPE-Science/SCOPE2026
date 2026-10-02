# Independent audit — 2026-10-01

## Final claim

7-maximality of cyclotomic units at first layer of Z7-extension of Q(sqrt2) with lambda7=mu7=0

## Correctness — PASS

PASS. The arithmetic core was reconstructed independently. The two square roots of 2 modulo 49 are 10 and 39, so the fundamental unit 1+sqrt(2) maps to 11 and 40; their sixth powers are 15 and 36 modulo 49, neither 1. The unique index-seven local norm subgroup of Z_7^× modulo 49 is the order-six subgroup, so the fundamental unit is not a local norm and the global unit norm index is 7. Chevalley's ambiguous class-number formula then gives a trivial ambiguous class group. A nontrivial finite 7-group acted on by the order-seven Galois group cannot have trivial fixed subgroup, so the 7-primary class group of the first layer is trivial. The standard cyclotomic-unit/class-number index bridge gives 7-maximality, and the first-layer stabilization criterion applies because the primes above 7 are already totally ramified. The committed integer verifier agrees with every independently recomputed residue and norm check.

## Originality — PASS

PASS. The inspected literature supplies the general class-group/cyclotomic-unit and stabilization machinery, but no source located states this exact Q(sqrt(2)), p=7 first-layer computation or its residue certificate. Gras's full text gives the relevant arithmetic character formula and the cases in which the factor w_chi is 1; Fukuda is the standard stabilization source. Targeted searches for the exact field/prime pair did not identify a prior exact table or theorem. This is therefore best-knowledge original as a concrete certified instance, with the usual residual risk of an unindexed numerical table.

## Scientific value — PASS

PASS. Greenberg's conjecture for a concrete real quadratic field and an odd split prime is a standard, motivated Iwasawa-theoretic question. The result simultaneously certifies the first-layer 7-class vanishing, the 7-part of the cyclotomic-unit index, and lambda=mu=0 by a short local-norm obstruction, so it is a reusable exact boundary datum rather than an arbitrary parameter slice.

## Sources inspected

- Georges Gras, Application of the notion of Phi-object to the study of p-class groups and p-ramified torsion groups of abelian extensions — https://arxiv.org/abs/2112.02865: GENERAL_FRAMEWORK_NOT_EXACT_COVERAGE. Theorem 7.5 gives the arithmetic class-group index formula and states w_chi=1 for non-prime-power character order and for prime-power order with prime-power conductor; it does not compute the audited field.
- Takashi Fukuda, Remarks on Z_p-extensions of number fields — https://doi.org/10.3792/pjaa.70.264: GENERAL_STABILIZATION_NOT_EXACT_COVERAGE. The theorem is a general stabilization criterion and contains no field-specific Q(sqrt(2)), p=7 computation.

## Residual risks

- No literature search proves absolute global novelty; an unindexed historical table may exist.
- The RESULT's reproducibility prose uses the historical prefix output/artifacts, while the actual repository artifact is artifacts/verify_target.py; the replacement METADATA records the actual path.

## Disposition

**passed**
