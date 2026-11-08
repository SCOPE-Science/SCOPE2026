---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

D_f=f∂ is all derivations since derivative of x^(2M) vanishes, and in characteristic 2 D_f²(g)=ff′g′. Decomposition f=a(t)+xb(t), t=x², reduces square zero to ab=0=b² over Fq[t]/t^M. Valuations partition every f without overlap; image is fB of rank M−min(v(a),v(b)). This derives all enumerator coefficients and the total. For nonzero b the order j is exactly uniform on ceil(M/2)..M−1, while rank deficit has geometric tail, implying W1 O(1/M). Independent exhaustive F2 operator matrix squares/ranks up to truncation 12 match formula; source verifies additional q=4,8 cases.

## originality

PASS

Classical Witt/restricted-Lie algebra accounts prove that D^p is a derivation, not the exact finite-field 2-nilpotent operator-rank enumeration and uniform asymptotic. Briggs–Rubio y Degrassi discuss integrability and p-operations; Yao–Zhao consider 2-local derivations on p-truncated Jacobson–Witt algebras; Premet/Chen impose larger characteristic in cited theorems. Semantic Resultary comparison did not locate the same enumerator.

## value

PASS

Exact rank spectrum and a nondegenerate uniform limit law describe a natural restricted-Lie nilpotent locus across all truncation lengths. This is more than checking a single tiny algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
