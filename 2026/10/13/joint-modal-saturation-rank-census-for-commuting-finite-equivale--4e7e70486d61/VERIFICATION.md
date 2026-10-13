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

# Reproducible checks and proof limits

Run `python3 verify.py` with Python 3 and its standard library, from the directory containing the standalone script.

The script implements the exact integer Stirling-number recurrence and computes \(N_n(a,b,c)\) through \(n=9\). It independently enumerates all partitions and all ordered pairs through \(n=6\), checks relational commutation via the defining ordered-pair condition, derives join-component counts with union-find, and compares every refined cell with the recurrence. For \(n\leq4\), it evaluates both modal compositions on every Boolean subset, checks whether the maps commute and whether one composition is idempotent, and compares their distinct output counts with \(2^c\). It tests the sharp support criterion in \(2025\) parameter cases and verifies all unweighted totals through \(n=9\) against independently published OEIS A354458.

Expected final output begins with `VERIFY_OK`; the latest replay reported `n_to_6_pairs 44168`, `direct_boolean_modal_pairs 255`, `support_tested 2025`, and the unrefined totals \(1,1,4,19,117,864,7459,73749,818960,10078023\).

The brute-force enumeration is finite. It does not independently certify all infinite-parameter statements or establish that no older equivalent formula exists. Unrestricted correctness rests on the proof in `RESULT.md`. Independent audit has not been performed.
