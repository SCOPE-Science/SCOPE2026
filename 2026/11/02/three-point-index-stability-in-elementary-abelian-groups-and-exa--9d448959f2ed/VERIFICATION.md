---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The package's `verify.py` is a self-contained standard-library Python 3 program. Run `python3 verify.py` to reproduce all exact finite checks; its output was captured in `verification_output.txt` and ends with `VERIFY_OK`.

The exhaustive cyclic loops cover all \(\binom{p-1}{2}\) anchored three-element supports and all \(2^p-1\) nonempty candidate subsets for \(p=5,7,11\). Anchoring one support point at zero is without loss of generality by translation. For each candidate the program checks difference-set disjointness and domination by \(D=A-A\), not merely local maximality in a sampled search. Finite-field checks enumerate all subsets on the smallest binary and ternary spaces. Explicit coordinate lists and direct maximality checks confirm the rank-two negative witnesses at \(p=5,7,11\); cyclic gap constructions are independently tested for primes \(13\) through \(53\).

The infinite-dimensional theorems for \(p=2,3\), the complement lifting, and the all-primes-at-least-thirteen statement are proved symbolically in `RESULT.md`. No finite experiment is cited as proof beyond its completely exhausted fixed finite domain. Previous literature covers some individual negative examples; historical novelty is not independently certified. No external mathematical audit has been performed.
