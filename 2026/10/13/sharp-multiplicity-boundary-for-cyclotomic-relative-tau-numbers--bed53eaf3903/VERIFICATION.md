---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For prime p,k≥1, any n>1 with τ(n)|Φ_{p^k}(n) has Ω(n)≥p−1. For p=2, Ω≥1 trivially; prime equality witnesses must be odd q because Φ_{2^k}(q)=q^{2^{k−1}}+1 is even iff q odd. For odd p, Φ_{p^k}(n)=Σ_{j=0}^{p−1}n^{jp^{k−1}} is always odd; τ(n) therefore odd, forcing every prime exponent e_i even. If r≠p divides Φ_{p^k}(n), r∤n and the multiplicative order ord_r(n)=p^k (else the sum would be p mod r), so r>p. If Ω(n)<p−1 then any prime r|τ(n)=Π(e_i+1) satisfies r≤e_i+1≤Ω+1<p, contradicting cyclotomic order. At Ω=p−1 all primes in τ(n) must equal p, hence e_i+1=p and exactly one factor q^{p−1}; q≠p because Φ_{p^k}(q^{p−1})≡1 mod p if q=p. Conversely for q≠p, Fermat gives q^{p−1}≡1 mod p and Φ_{p^k}(q^{p−1})≡p≡0 mod p=τ(q^{p−1}). The proof is uniform in k and q. Independent divisibility checks for n up to 5000 on sampled p,k reproduced 2054 relative hits and 1384 boundary instances; they do not establish the infinite theorem.

## originality

PASS

Abel–Lauer–Redi (2021) Corollary 2 specifically gives infinitely many τ-numbers relative to Φ_{p^k} using the general condition Φ_{p^k}(1)=p. It constructs exponent p−1 witnesses from a congruence progression, but does not prove Ω≥p−1 for all nontrivial solutions, classify all equality cases, or allow every prime q≠p at the extremal layer. Zelinsky 2002 introduced polynomial-relative τ-numbers and an overbroad infinitude assertion later repaired. A related published SCOPE theorem for Φ_{2p^k} concerns a different cyclotomic family with a unique trivial solution, so it does not imply this one. Result is a sharp natural multiplicity boundary, with priority risk from classical cyclotomic order folklore.

## value

PASS

Prime-power cyclotomic polynomials are explicitly singled out in the original relative-τ literature, and Ω is the canonical complexity measure counting prime factors with multiplicity. The theorem proves that p−1 is an intrinsic minimum, not an artifact of a witness construction, and classifies every equality case for all k. It identifies an exact natural invariant over an infinite parameter family, with nonexistence below the boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
