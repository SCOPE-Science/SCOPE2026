---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Fix a witnessing tuple and let \(U\) be its set of distinct values, \(|U|=u\le k\). If a model has more than \(k+2^k\) vertices then more than \(2^u\) vertices lie outside \(U\), so two have the same adjacency vector to \(U\). In the induced graph on \(U\) plus those two vertices they are twins over the witnesses. Replacing the twin pair by any \(t\ge2\) clones preserves every atomic \((y,z)\)-type over the witnesses: same-clone assignments realize the old diagonal type and distinct-clone assignments realize the old twin-pair type. Hence every order \(n\ge k+2\) is obtained. The sharp sentence enforces distinct witnesses and distinct witness-neighbourhood bit vectors on outsiders, giving exactly \(2^k\) outsider slots and realizing every size through the endpoint. The \(k=0\) case is correctly separated. The bundled checker verifies the finite profile and clone-type table but the proof is symbolic.

## originality

PASS

The full Pikhurko--Verbitsky survey was inspected at Ramsey's Bernays--Schönfinkel spectrum theorem and proof. That classical theorem gives the finite/cofinite dichotomy and, using a general Ramsey bound, the much larger threshold \(2^k4^\ell\); for \(\ell=2\) it does not state the exact additive cutoff \(k+2^k\). The audited argument replaces the Ramsey step by a sharp pigeonhole duplicate among the \(2^u\) one-point witness types and gives an exact extremal sentence. Current Resultary search did not surface an earlier \(k+2^k\) endpoint.

## value

PASS

Exact finite-spectrum endpoints are natural quantitative invariants of a classical decidable prefix class. The theorem replaces a Ramsey-scale bound by the sharp \(k+2^k\) cutoff and provides matching sentences for every \(k\), so it is a complete exact boundary rather than a minor constant improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
