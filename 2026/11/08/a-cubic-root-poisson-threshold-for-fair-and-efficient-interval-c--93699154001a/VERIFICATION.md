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

Run `python VERIFY.py` using Python 3 without third-party packages.

The checker compares literal Pareto comparisons against the two endpoint conditions for all \(2{,}032\) nonempty committee strings of lengths \(3\) through \(10\). It compares the literal JR definition with the quota/forbidden-run formula over the same strings. It independently enumerates all cohesive voter subsets to check EJR versus JR for \(498\) strings of lengths \(3\) through \(8\). Finally, it checks the four-state polynomial recurrence versus independent direct enumeration for all \(75\) pairs of committee size and candidate count with \(3\le m\le12\).

All tests passed in the supplied version. Selected exact ratios computed by the recurrence are \(2668/8008\) at \((m,k)=(16,10)\), \(18927496/64512240\) at \((32,22)\), and \(143415189318227/488526937079580\) at \((64,48)\).

These are exhaustive finite checks within specified bounds, **not** a proof for arbitrary \(m\). The infinite finite-\(m\) classifications are proved by direct incidence, Pareto-welfare and transfer-state arguments. The Poisson limit and sharp threshold are established by factorial moments and a variance bound; the checker does not certify these asymptotics.

No independent audit was carried out.
