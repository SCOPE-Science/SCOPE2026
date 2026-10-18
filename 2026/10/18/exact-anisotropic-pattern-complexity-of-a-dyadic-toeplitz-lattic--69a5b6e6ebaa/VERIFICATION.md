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

# Verification notes

The proof is contained in RESULT.md. The standalone finite checker `verify_patterns.py` needs only Python 3's standard library and can be run with `python3 verify_patterns.py` from a directory containing that file. In this run it returned `PASS: 174 finite pattern/count/recurrence checks`.

The checker exhaustively enumerates every translation residue modulo \(2^{\max\{n,m\}}\) and both singular-site bits for all \(25\) pairs \(1\le n,m\le5\). It independently enumerates length-\(2^k\) truncated valuation words for \(1\le k\le6\), compares their language bases and cardinalities, and checks 144 more recursive identities. Exhaustive enumeration concerns only the specified finite cases; no claim about arbitrarily large windows depends on numerical extrapolation. The analytical argument separately explains why this modulo-level enumeration is complete in each checked finite case.

The critical proof checks are (i) either color at the unique high-valuation hole is attained by integral translations, (ii) the four parity-lifted pattern families are disjoint when both sides have at least four sites, (iii) the one-short-side language contains no zero word once the long side has at least four sites, and (iv) the normalized subsequential-limit classification uses only integer aspect differences. These are proved in RESULT.md. Originality and value remain matters for independent scholarly assessment; no independent audit or external validation has been performed.
