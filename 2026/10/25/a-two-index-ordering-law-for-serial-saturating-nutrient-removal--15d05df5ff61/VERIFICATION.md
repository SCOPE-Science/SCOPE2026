---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Every T_i is strictly increasing, positive and below x because T_i’=1-u_i K_i/(K_i+x)^2>0. Exact common-denominator expansion gives T_j(T_i(x))-T_i(T_j(x))=-uv x² P(x)/D(x), D>0, P(x)=(K-L)x²+[(K-L)(K+L)-Ku+Lv]x+KL(K-L-u+v). For K>L, if K-u>=L-v, all P coefficients nonnegative and at least leading and linear strictly positive, so larger-K-first wins at every x>0. If K-u<L-v, the leading coefficient is positive, constant negative, and the quadratic has exactly one positive zero x*, so preference reverses there. A finite family has finitely many switches; low-x inputs and all intermediate stage inputs are below them, whereas for high-x, all intermediate inputs remain >x-sum(u_i), above the switches. Strict adjacent interchanges improve any inverted pair under those ranges, producing unique optimal total orders, and their difference rules out any universal order. Independently reduced symbolic commutator to zero and verified exact rational example P=(x-1)(x+5/6) with switch x=1.

## originality

PASS

Michaelis–Menten saturation, ordering of stream reaches and monotone-map interchange arguments are established. Covino–McGlynn–Baker discuss spatial sequence and observed uptake curves, but not a theorem comparing every permutation for the precise rational maps at every x. The exact two-index iff, strict universal-optimal ordering and unique switch for reversed pairs are the candidate new statement. Sakamoto 1994 consecutive reaction transfer-functions is plausible, but only its abstract available; nonaccess alone is not automatic failure.

## value

PASS

A complete robust universal ordering test (and precise failure mechanism) is a natural optimization question for multiple saturable finite-step removal stages. It replaces parameter-dependent brute-force permutation searches with a two-index criterion while sharply explaining concentration-induced reversals. A reusable exact result in a motivated discrete environmental processing model, not a claim of field validation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
