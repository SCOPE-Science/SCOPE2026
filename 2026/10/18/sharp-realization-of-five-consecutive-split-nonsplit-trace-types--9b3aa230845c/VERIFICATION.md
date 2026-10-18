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

# Reproduction

Run `python3 verify.py` using Python 3. The script has no dependencies outside the standard library and does not use any network resources. A successful run prints `VERIFY_OK`, the number of odd primes tested (\(1651\)), the number of exceptional primes (\(40\)), and the last exception (\(233\)). The full masks on all primes below \(1600\) are compared with a distinct Euler-criterion implementation, covering \(250\) odd primes. The final list also reports that only word `0` (all five minus signs) is missing at \(233\).

# Mathematical checks and limits

For \(p>8\), the nine branch roots are distinct except for the root shared by \(f_0\) and \(f_4\). Expanding the \(32\)-normalization yields a base \(\sqrt p\) coefficient of \(129\); the eight subsets containing both endpoints save two each, giving \(113\) and an absolute correction of \(8\). Each of nine zero-discriminant arguments contributes at most \(16\), giving the error constant \(152\). These are human-checkable finite identities, not heuristic bounds. The quadratic Weil estimate and positivity for \(p\ge14000\) prove the infinite portion; the script proves the remaining finite assertion by full enumeration. This is not a formal or independent audit.
