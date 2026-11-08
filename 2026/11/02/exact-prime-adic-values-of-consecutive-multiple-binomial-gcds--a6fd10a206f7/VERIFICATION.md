---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Reconstructed Kummer carry proof with K=p^a b-1. For j=floor(log_p b)<a, three exhaustive cases v_p(q-1)<=j, j<v_p(q-1)<a, v_p(q-1)>=a force at least a-j carries. The explicit t=p^a(1+((b-1) mod p^j)) gives a-j carries by the split b-1=s p^j+r; b=1 follows from the special prime-power carry pattern. For j>=a Guo et al. Lemma 9 supplies an actual zero-valuation binomial. To exclude all other prime factors, integer-valued degree-k polynomial F(X)=binom(kX,k) and Newton difference F(0)=sum_h(-1)^h Delta^h F(1) yield r|(k+1) for any common prime r. Independently recomputed 73 direct integer gcds n=3..75 from all binomials. Exact integers and finite checks corroborate, not replace, the uniform proof.

## originality

PASS

Guo–Qiu–Cao–Feng–Gao arXiv:2606.22997 proves gcd-one criterion and Lemma 9 gives only divisibility of D(k) by a given prime, not its full p-adic exponent; the cited original was read through primary theorem, digit-box and Lemma 9. Known pure-prime-power case D(p^a-1)=p^a and OEIS unit table are credited. The all-composite exact valuation plus explicit local minimizer is stronger, so best-of-knowledge O PASS with uncatalogued gcd identities as risk.

## value

PASS

The original named arithmetic problem asks when its gcd is one; this theorem determines the entire positive gcd for every k, including previously unknown composite-case exponents and explicit minimizing binomial witnesses. It is a natural exact invariant and nontrivial carry calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
