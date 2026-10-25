---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The substitution h(a)=ab,h(b)=ac,h(c)=db,h(d)=dc and coding a,b→0,c,d→1 generate the digit-defined Rudin–Shapiro sequence. The eight alternating substitution triples occur in h^8(a); for each h(x)=pq both h^{k-1}(p)h^{k-1}(q)h^{k-1}(p) and its QPQ converse occur, so all 2^k rotations of W_k(x) are factors. The four W_1 blocks 00,01,10,11 are distinct and injectivity lifts to each level; different halves imply W_k(x) primitive for k>=2 (every nonprimitive power of 2 length repeats its two halves). Their one-count vector plus wrap-around 0100 count is invariant under rotation. Explicit w_even/w_odd recurrences and the k→k+2 q-matrix distinguish each of the four entries for k>=3. Independent direct-digit factors verify every rotation up to k=8, and recurrences/distinct invariants k=3..10. These finite cases are not the all-k proof; substitution and induction supply it.

## originality

PASS

The established Lie-complexity theory defines and studies the invariant and proves general automatic-sequence properties; its read full text does not analyze Rudin–Shapiro four-orbit families. The construction is a specific infinite factor-language refinement. No claim of exact Lie complexity or global novelty proof.

## value

PASS

Lie complexity requires complete occurrence of cyclic orbits, a stronger combinatorial property than ordinary or cyclic complexity. Four explicit, distinct primitive witness families at infinitely many dyadic lengths yield a natural nontrivial lower bound, rather than a one-off finite word enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
