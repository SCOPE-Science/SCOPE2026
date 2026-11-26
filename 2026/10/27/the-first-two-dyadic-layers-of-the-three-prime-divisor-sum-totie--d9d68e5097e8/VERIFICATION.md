---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Multiplicativity reduces the two cases to H_p(b)H_q(c)=4/3 or 8/7. Each H_r(t) increases in t with minimum (r+1)/(r−1) and strict upper limit (r/(r−1))²; both endpoints decrease in r. Exact reproduction with python3 /workspace/audit_evidence/dyadic.py checks the bounds that restrict the prime search, obtains exactly (11,19) for a=1 and 13 possible supports for a=2, and verifies the five equality supports. On five supports the lower endpoint already equals the target, forcing both exponents to be one. On seven other supports the b=1 upper bound lies below target and b≥2 lower bound lies above. The last two require b≥3, so p divides the right side of σ=4φ. Since p∤σ(4)σ(p^b), it must divide σ(q^c), requiring c+1 divisible by the order of q modulo p (16 and 18 respectively). Substitution into the increasing lower bound rules out both tails. This covers arbitrary positive exponents and gives exactly the five printed integers; the frozen bounded scan is not used as an unbounded exclusion.

## originality

PASS

Pass for proving that all quotient-four solutions in the two specified three-prime layers have both odd exponents one. All five individual solutions and the squarefree odd-part family are known. Broughan–Zhou place the even three-prime case outside their relevant proved classification; their list is examples, not a proof against repeated odd-prime powers. The primary-literature and Resultary searches surfaced no inspected earlier result settling these two unrestricted layers.

## value

PASS

The two lowest positive valuations of 2 are a natural complete boundary in the already posed even quotient-four three-prime case. The work upgrades an observed exponent pattern to a rigorous classification over two unbounded odd exponents. The order constraints resolve the supports that endpoint bounds alone do not eliminate; merely recomputing the five previously known values would not suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
