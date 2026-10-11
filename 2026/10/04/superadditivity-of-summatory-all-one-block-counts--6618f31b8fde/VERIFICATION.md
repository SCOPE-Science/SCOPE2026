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

The count decomposes by least-significant block position into functions \(F_q(N)=q\lfloor N/(2^rq)\rfloor+\max\{0,(N\bmod 2^rq)-(2^rq-q)\}\). The residue interval is the terminal interval of each period, and the three possible locations of the two residuals give superadditivity of every \(F_q\); summing the finitely many active positions proves the theorem. The equality strip follows because prepending the top binary one creates a crossing \(1^r\) block only after the stated threshold. A fresh independent brute-force replay for \(2\le r\le5\), all addends through 100, and dyadic equality strips through exponent eight found no violations.

## originality

PASS

Allouche and Stipulanti explicitly ask whether their summatory digit inequalities extend to block-counting functions and give the number of binary \(11\) occurrences as the concrete example. The older Muramoto et al. primary paper gives exact formulas for general subblock summatory counts but does not state the two-argument superadditivity or dyadic equality strip. Targeted Resultary search did not retrieve an equivalent additive inequality.

## value

PASS

The theorem answers an explicit published question at \(r=2\) and supplies a uniform proof for every longer all-one block. The equality strip gives sharp structural information beyond bare superadditivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
