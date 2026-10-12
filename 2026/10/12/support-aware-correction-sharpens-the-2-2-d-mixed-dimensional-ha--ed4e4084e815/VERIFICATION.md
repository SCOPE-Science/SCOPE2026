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

The proof is support-theoretic and exact for every integer \(d\ge5\).

For \(\mathcal H=\mathbb C^2\otimes\mathbb C^2\otimes\mathbb C^d\), every support containing the qudit has physical dimension at least \(d\ge5\). Hence the error set of dimensional weight at most \(4\) is precisely the full operator algebra on the two-qubit subsystem. If \(E_a\) and \(E_b\) lie in this algebra, then \(E_a^\dagger E_b\) lies in the same algebra and has dimensional weight at most \(4<5\). The distance-\(5\) detection condition therefore supplies the Knill--Laflamme pair condition for the whole set.

An orthogonal error basis on the two-qubit subsystem has \(4^2=16\) elements. Under non-degeneracy these give \(16\) mutually orthogonal \(K\)-dimensional images, inside ambient dimension \(4d\). Thus \(16K\le4d\).

`artifacts/verify.py` checks the support classification and the count \(1+6+9=16\) for any user-supplied integer \(d\ge5\). It is a reproducibility check only; finite executions are not used to prove the universal quantifier.

Scientific limits: Theorem 21 remains valid under its explicit sufficient hypothesis \(T^2<D\). No construction or attainability statement is made for \(K=\lfloor d/4\rfloor\).
