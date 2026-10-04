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

The theorem is proved symbolically in `RESULT.md`; no finite experiment is used to infer the statement for arbitrary \(n\).

The standalone standard-library checker `verify.py` performs the following independent replay checks:

1. For every \(1\le n\le8\) and every pair of basis strings, it verifies exactly modulo four that the shortest-time hypercube phase corrected by Hamming-weight phases equals the Walsh-Hadamard sign pattern.
2. It computes the minimal circular covering arc of the distinct required fourth roots and checks the exact values \(\pi/2\), \(\pi\), and \(3\pi/2\) for the three dimensional regimes.
3. It checks explicit accumulated-time schedules made from durations \(\pi/2\) for \(n=1\), two durations \(\pi/2\) for \(n=2\), and durations \(\pi\) and \(\pi/2\) for \(n\ge3\).
4. It checks that the runtime identity \(T_n^*=n\pi/4+\pi\min\{n,3\}\) reproduces the three displayed cases.

Run:

`python3 verify.py`

Expected output:

`VERIFY_OK`

The checker does not search over more general dynamic-walk architectures and does not establish novelty. Those are outside computational verification.
