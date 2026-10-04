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

The general theorem is verified by the symbolic bijection in `RESULT.md`. The executable check is deliberately finite and independent of that proof: it constructs labeled partial orders directly, enumerates monotone maps by definition, forms \(X\oplus A_r\), and compares the brute-force fixed-point-free count with \(\sum_g(u(g)+r-1)^r\).

`verify.py` checks all \(219\) labeled four-point posets for \(r=2\), all labeled bases of size at most three for both \(r=2\) and \(r=3\), for \(265\) theorem instances in total. Its deterministic output is stored in `verification_output.txt`.

Run with:

`python3 verify.py`

The finite enumeration is not an infinite proof and is not presented as one. It is a regression test for the definitions, boundary conditions, and extension count. The theorem is stated only for \(r\ge2\); arbitrary added posets are outside scope.
