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

# Verification and proof boundaries

The supplied `verify.py` is Python 3 standard-library only; running `python3 verify.py` emits the checked text in `verification_output.txt`. It constructs the four-state constraint matrix from the selected/unselected edge rule, verifies all 16 entries of \(M^4=M^3+M\), verifies the four entries of \(M^3h=M^2h+h\), and reconstructs all nine base counts.

The independent brute-force branch enumerates every edge subset of every lollipop with \(c\ge3\), \(t\ge1\), and \(c+t\le15\); it also directly enumerates PED-sets of cycles on 3 through 15 vertices. The grid \(3\le c\le30\), \(1\le t\le30\) checks the two recurrences and their strict comparison numerically. These are finite tests only.

The infinite proof is the transfer decomposition at the unique degree-three cycle vertex, the exact polynomial identities, and the strict positivity of the nine seed differences propagated through both recurrences. No independence or external certification is claimed.
