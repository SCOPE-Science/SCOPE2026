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

# Verification details
Run \(\texttt{python3 artifacts/verify.py}\) with Python 3 (standard library only). The script explicitly forms all products of finite binary path-basis elements, enumerates algebra inputs, builds all polynomial evaluation functions by linear closure, and confirms the following dimensions:

- One vertex, one variable: dimension \(2\).
- Two isolated vertices, two variables: dimension \(4\).
- One arrow, two variables: dimension \(24\).
- Two parallel arrows, two variables: dimension \(24\).
- Three-vertex directed chain, one variable: dimension \(6\).
- Two arrows to a sink, one variable: dimension \(4\).

It also verifies \(36\) independent diagonal separator supports for a three-vertex chain over \(\mathbb F_2\) with two variable coordinates at each vertex. The check is finite and supplements the symbolic proof; it does not certify the theorem over all fields and quivers. No independent audit has been conducted.
