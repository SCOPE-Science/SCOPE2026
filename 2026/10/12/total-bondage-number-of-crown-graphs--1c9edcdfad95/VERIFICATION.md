---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The identity gamma_t(H)=tau_A(H)+tau_B(H) on a bipartite graph follows from independent open-neighborhood covering of shores. For a crown both tau=2. Raising gamma_t requires >=3 on one shore; missed-pair nonneighbor blocks cover all C(n,2) pairs, and the written induction for proper blocks of size>=2 proves weighted sum(|C|-1)>=2n-3. Explicit W1,W2,W_{n-1} witness deletes precisely 2n-3 edges without isolates. Independent exhaustive subthreshold deletion checks n=3..5 and n=3..8 witnesses match. Infinite proof relies on the structural lemma, not these samples.

## originality

PASS

The inspected recent k-total-bondage primary paper treats complete bipartite graphs but not crown graphs; the older survey gives the same-invariant complete-bipartite baseline while 2016 crown literature treats ordinary bondage. Neither a different starting graph nor a different domination variant implies b_t(Cr_n). Resultary closest crown results concern other invariant families.

## value

PASS

The infinite crown family is the canonical one-factor-deleted K_n,n. Its total bondage shifts from known K_n,n baseline n to 2n-3, and the weighted pair-cover lemma explains sharp resistance to additional edge deletion. This is a motivated structural threshold, not an isolated arbitrary instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
