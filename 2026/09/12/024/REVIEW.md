# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. The arithmetic core was reconstructed independently. The two square roots of 2 modulo 49 are 10 and 39, so the fundamental unit 1+sqrt(2) maps to 11 and 40; their sixth powers are 15 and 36 modulo 49, neither 1. The unique index-seven local norm subgroup of Z_7^× modulo 49 is the order-six subgroup, so the fundamental unit is not a local norm and the global unit norm index is 7. Chevalley's ambiguous class-number formula then gives a trivial ambiguous class group. A nontrivial finite 7-group acted on by the order-seven Galois group cannot have trivial fixed subgroup, so the 7-primary class group of the first layer is trivial. The standard cyclotomic-unit/class-number index bridge gives 7-maximality, and the first-layer stabilization criterion applies because the primes above 7 are already totally ramified. The committed integer verifier agrees with every independently recomputed residue and norm check.

Originality: PASS. The inspected literature supplies the general class-group/cyclotomic-unit and stabilization machinery, but no source located states this exact Q(sqrt(2)), p=7 first-layer computation or its residue certificate. Gras's full text gives the relevant arithmetic character formula and the cases in which the factor w_chi is 1; Fukuda is the standard stabilization source. Targeted searches for the exact field/prime pair did not identify a prior exact table or theorem. This is therefore best-knowledge original as a concrete certified instance, with the usual residual risk of an unindexed numerical table.

Scientific value: PASS. Greenberg's conjecture for a concrete real quadratic field and an odd split prime is a standard, motivated Iwasawa-theoretic question. The result simultaneously certifies the first-layer 7-class vanishing, the 7-part of the cyclotomic-unit index, and lambda=mu=0 by a short local-norm obstruction, so it is a reusable exact boundary datum rather than an arbitrary parameter slice.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
