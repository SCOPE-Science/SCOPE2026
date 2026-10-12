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
# Verification of the finite chain-product endomorphism census

The attached standalone Python 3 file `verify_bi_godel.py` uses only the standard library. Invoke `python3 verify_bi_godel.py`. It constructs finite disjoint unions of chains, enumerates every set map on at most six dual points, and checks isotonicity and *both* upward/downward bounded-morphism conditions. It independently calculates the predicted weighted support histogram, inclusion-exclusion endomorphism histogram, and idempotent histogram. A separate small-case check constructs the upset algebras explicitly and tests preservation of Heyting implication and co-Heyting subtraction, then tests algebraic image cardinalities.

Observed output:

```text
VERIFY_OK length_vectors 63 candidate_maps 1545157 valid_endomorphisms 57970 direct_bi_Heyting_cases 15 direct_algebra_maps 2165
CASE (1, 2) total 2 ranks {2: 1, 6: 1} retractions {2: 1, 6: 1}
CASE (2, 3, 3) total 16 ranks {3: 4, 12: 10, 48: 2} retractions {3: 4, 12: 6, 48: 1}
CASE (1, 1, 2) total 12 ranks {2: 2, 4: 6, 6: 2, 12: 2} retractions {2: 2, 4: 2, 6: 2, 12: 1}
CASE (2, 2, 2) total 27 ranks {3: 3, 9: 18, 27: 6} retractions {3: 3, 9: 6, 27: 1}
CASE (1, 2, 3) total 8 ranks {2: 1, 6: 5, 8: 1, 24: 1} retractions {2: 1, 6: 3, 8: 1, 24: 1}
```

All checks passed for those finite cases. Tests do not independently certify the proof for unbounded inputs. No independent scientific validation has been conducted.
