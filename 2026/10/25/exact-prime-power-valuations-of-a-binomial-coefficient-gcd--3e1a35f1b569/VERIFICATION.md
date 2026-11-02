---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The external Guo–Qiu–Cao–Feng–Gao Lemma 4 confines prime support to n=k+1; its Lemma 9 establishes v_p(D)>0 iff b≤p^a. For b≤p^a, put c=floor(log_p(b−1)), and for each q set r=q−1, s=v_p(r). Kummer carries at digit positions s<j≤a contribute max(0,a−s); positions j=a+t with c<t≤s contribute max(0,s−c), disjoint because t>c≥0. Hence every coefficient has p-valuation at least a−c. Selecting q=1+p^a t, 1≤t≤b−1, reduces valuation exactly to a−v_p binom(b−1,t); Lucas gives a t with v_p binom(b−1,t)=c (take t=b mod p^c), giving equality. For pure p^a, the carry lower bound a and the choice q=2 supply equality. Two distinct p^a components cannot both be at least √n since their product divides n, giving single-prime support. Fresh direct exact integer gcds k=2..89 and 683 independent Legendre-factorial p-adic minimizations for n≤350 all match. The cited external lemmas were examined in the actual primary text, not inferred from source logs.

## originality

PASS

A fresh closest-prior comparison finds no accessible theorem or database record implying the final all-parameter conclusion. The exact overlap/special-case antecedents are credited and remaining literature-access or terminology risks are recorded; PASS is a best-of-knowledge judgment, not external historical certification. Exact prime-power valuations of a binomial-coefficient gcd: For k≥2, D(k)=gcd_{2≤q≤k+1} binom(qk,k), n=k+1: for p^a||n and b=n/p^a, v_p(D)=a if b=1, otherwise max(0,a−floor(log_p(b−1))); no p outside n divides D. Thus D is 1 or a power of a single prime.

## value

PASS

The gcd family and its unit/nonunit threshold were the precise subject of a 2026 OEIS conjecture resolution. This theorem strengthens that binary classification to the unknown exact exponent whenever a prime divides, gives a constructive coefficient attaining the gcd valuation, and proves the single-prime-power structure. It is a natural arithmetic invariant with uses in divisibility and prime-power strength, not a random recomputation of a table. The previously known support/positivity lemmas are explicitly credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
