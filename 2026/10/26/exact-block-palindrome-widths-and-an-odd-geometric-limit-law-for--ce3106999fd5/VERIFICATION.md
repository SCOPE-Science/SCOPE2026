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

# Reproduction and limits

Run `python3 VERIFY.py` with Python 3 and the standard library. The verifier enumerates all nonempty Dyck words of semilength \(1\) through \(12\), computes shortest literal borders directly, and checks complete width histograms against independently generated coefficients of the proved bivariate generating function. It also checks Catalan marginals through semilength \(80\), checks \(11\) initial unbordered-Dyck counts, and bounds the omitted terms in the numerical evaluation of \(\alpha=U(1/16)\) by \((1/4)^{81}/(1-1/4)\).

Expected success marker: `DYCK_BP_PASS`. Exactly \(290511\) nonempty Dyck words are examined. All arithmetic for enumeration and coefficient identities is integer-exact; the constant uses 45-digit decimal arithmetic with a rigorous separate tail bound.

The finite tests do not establish the generating function for arbitrary semilength or the limiting law. The infinite reasoning is fully provided in `RESULT.md`, including the border-closure lemma, reversible shortest-border decomposition, maximization argument, and square-root asymptotic transfer. Independent review is not performed.
