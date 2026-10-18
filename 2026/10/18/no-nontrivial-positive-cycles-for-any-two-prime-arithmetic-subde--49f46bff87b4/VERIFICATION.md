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

# Reproducibility and proof checks

Run `python3 verify.py` from a directory containing the extracted standalone file. The program performs exact integer-valuation and orbit regression tests over 45 pairs of primes and a prescribed finite range. It checks the smooth-state update formula, the forward-invariant threshold and finite absence of nontrivial cycles.

The crucial infinite reasoning is symbolic: on a periodic orbit, \(\prod_i c_i=(pq)^L\), so each \(c_i\) has no factors outside \(\{p,q\}\). If \(c_i<pq\), the only possibilities are \(p^u\) or \(q\): the smallest powers lead to zero and the remaining powers move strictly upward. If \(c_i\ge pq\), the exact transition either increases \(c_i\) or, for a pure power of \(q\), remains at least \(q^2-q+p\ge pq\). Finite periodicity then forces every \(c_i\ge pq\), and the product forces equality. The verifier is not an exhaustive proof over infinitely many primes, periods or positive integers.

Known literature already supplies the final fixed-point formula. The newly proved assertion is that all positive periodic points with support at exactly two arbitrary primes belong to those fixed families. No external independent mathematical audit has been performed.
