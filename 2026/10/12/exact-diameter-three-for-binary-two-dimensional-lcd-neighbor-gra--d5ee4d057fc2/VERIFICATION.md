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

The all-length proof is symbolic. Its critical steps are:

1. For independent \(c,z\), the plane \(\langle c,z\rangle\) is LCD exactly when
\[
q(c)q(z)+B(c,z)=B(c,T(z))=1.
\]
2. For any two LCD planes, vectors excluded by \(C\cup D\cup T^{-1}(C^\perp)\cup T^{-1}(D^\perp)\) do not fill \(\mathbb F_2^n\). The even-\(n\) count is at most \(2^{n-1}+7\), and the odd-\(n\) count is at most \(3\cdot2^{n-2}+7\); both are strictly below \(2^n\) in the stated ranges.
3. For the explicit lower-bound pair, every mixed plane \(\langle c,d\rangle\) is degenerate because \(B(c,d)=q(c)q(d)\).

`verify.py` performs exact finite checks with no third-party dependencies. It exhaustively constructs the LCD neighbor graphs for \(n=4,5,6\), verifies that their diameters are \(3\), checks the displayed distance-three witness, and validates the Gram identity on all vector pairs in those ambient spaces.

The finite checks do not certify the infinite quantifier; the counting argument in the proof does.
