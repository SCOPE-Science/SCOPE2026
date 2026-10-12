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

# Reproducibility and mathematical boundaries

Run `python3 verify.py` next to `COMPONENTS.tsv`, using the Python 3 standard library. A successful run prints `EXACT_CERTIFICATE_OK` with `blocks=192`, `components=140`, `gaps=139`, `finite_primes=33602`, `worst_next_prime_count=10`, `machin_terms=20`, and `graph_components=140`. The accompanying table encodes the exact rational coefficients for each of the 140 closed intervals.

The script constructs prime numbers by an exhaustive sieve through 430000 and applies exact rational inequalities to every prime from 17 to 396737. For larger primes, the proof invokes Dusart's published theorem, not an unbounded loop or experimental extrapolation. It checks the required elementary implication from the explicit prime gap estimate; it does not attempt to re-prove Dusart's theorem. Sanna's published general interval-filling lemma covers the infinite compactness/closure argument.

The script computes rational bounds for \(\pi\) from twenty alternating terms in each of the two arctangent series in Machin's identity; all strict interval comparisons use these rational bounds and integer arithmetic. In addition to the direct 192-block sweep it separately implements Sanna's backward interval recurrence, and a union-find graph check of overlap connectivity. The checks establish the specific theorem within the stated external mathematical premises and do not assert an independent audit or a formal proof assistant certification.
