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

# Reproducible verification
Run `python3 proof_certificate.py` from the same directory as this document. Python's standard library is the only dependency. The program enumerates all \(2^{16}=65536\) assignments of signs to the 16 independent facet-normal inner products and checks an exact integer upper bound on the squared Euclidean projection onto the closed cone \(\{u_1\ge\cdots\ge u_5\ge0\}\).

The certificate scales gradients by \(D=10^{10}\), sets \(Q=2921101299\), and encloses the optimal coefficient strictly between \(Q/D\) and \((Q+1)/D\) by integer squares. For all but masks 65256 and 65535 it checks \(\|\Pi_{\mathcal C}(D v-Qe_1)\|^2\le(7D/10)^2\); the output's largest integer quantity \(60\|\Pi_{\mathcal C}(D v-Qe_1)\|^2\) is 2917995876580389748020 at mask 65520, below 2940000000000000000000. The exceptions are independently asserted by the code to have vectors \((3/8,\ldots,3/8)\) and \(e_1\), which the mathematical proof handles exactly.

The code does not itself verify the Cauchy projection formula or the Moreau inequality; both are explicitly derived or cited as standard results in `RESULT.md`. No infinite-dimensional, other-dimensional, or publication-priority claim follows from the finite certificate. This verification is not an independent audit.
