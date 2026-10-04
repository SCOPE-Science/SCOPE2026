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

The proof uses three exact identities. First, if \(s_1\) is the largest singular value of the Bloch matrix of a unital qubit channel, all output eigenvalues lie in \([(1-s_1)/2,(1+s_1)/2]\), and antipodal singular-vector inputs attain both endpoints. This proves \(\varepsilon_*=2\operatorname{arctanh}(s_1)\).

Second, unitary canonicalization makes the normalized Choi state Bell diagonal. The unital entanglement-breaking octahedron and the Bell-diagonal concurrence formula give \(C=[s_1+s_2+s_3-1]_+/2\).

Third, \(\varepsilon\)-QLDP gives \(s_1\le\tanh(\varepsilon/2)\), hence \(C\le[3\tanh(\varepsilon/2)-1]_+/2\); the depolarizing channel has equality in all three singular values and therefore attains the bound.

The bundled checker performs deterministic finite-grid consistency tests on Pauli channels and representative equality cases. It does not certify the continuous theorem by enumeration; the analytic argument above does.

Limits: the result is for unital qubit CPTP channels and pure QLDP only. No external independent audit has been performed.
