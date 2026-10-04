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

The executable check is `verify_zero_free.py`, requiring mpmath 1.3.0 as pinned in `requirements.txt`.

It reconstructs the depth-\(42\) matrix product over adaptive interval boxes covering \([0,1000]\). Each box is accepted only when one coordinate of the complex interval enclosure stays strictly farther from zero than the analytic truncation radius
\[
\frac{88}{21}\frac{1000}{2^{42}},
\]
where \(88/21>4\pi/3\). The terminal-vector estimate follows from support in \([0,2/3]\) and the max-row-sum norm \(\|M(\xi)\|_\infty=1\).

The recorded replay output is in `verification_output.txt`. It reports 10,908 certified leaves, 908 adaptive splits, and a minimum post-tail coordinate margin of approximately \(2.1511\times10^{-7}\), compared with a tail radius below \(9.529\times10^{-10}\).

The finite computation certifies only \(|\xi|\le1000\). It does not certify any point outside that range or global zero-freeness. The checker relies on the interval enclosure semantics of mpmath 1.3.0; no independent interval library was used.
