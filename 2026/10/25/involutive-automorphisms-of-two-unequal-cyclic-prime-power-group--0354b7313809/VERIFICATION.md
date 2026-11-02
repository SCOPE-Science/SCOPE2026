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

PASS. The unique four-parameter homomorphism matrix [[u,v],[p^{b−a}w,z]], with u,z units, parametrizes every automorphism for unequal exponents. Squaring on the two standard generators gives four exact congruences in the two moduli. For odd p, ±1 idempotent splitting of every involution decomposes the abelian p-group into complementary factors; uniqueness of elementary divisors leaves two fixed all-same-sign types and two transitive mixed-sign decompositions, each of size p^{2a}, yielding 2+2p^{2a}. For p=2, setting u=rz with r²=1 mod2^a reduces mixed constraints to (1+r)v=(1+r)w=0 and the root equation z²=1−2^h vw. The four-solution criterion modulo 2^b for b≥3 and separate exceptional a=1,b=2 case lead to 3,4,5 gap factors; a=1, a=2 and a≥3 root multiplicities are counted separately, with +32 correction in the latter regime. Independent exhaustive generator-squaring calculations for 13 small (p,a,b) examples agree exactly. The count includes the identity; exact-order-two elements number one fewer. General result rests on algebraic decomposition/case census, not these sample tests.

## originality

PASS

PASS to best of knowledge with modular-representation priority risk. Hillar–Rhea and Mader provide matrix and total automorphism-group descriptions, not involution-element counts. Hage–Harju's directly relevant primary treatment counts cyclic involutions and proves product decomposition properties but explicitly warns that product involutions cannot be counted by naive factor multiplication. Published fixed-point count results (including Resultary same groups) target a different predicate and do not determine the square-identity census. No exact equivalent mixed-exponent gap table was found, but a general modular representation classification may imply it without matching words.

## value

PASS

PASS. Counting involutions is a fundamental natural element-order statistic of the automorphism groups of unequal finite cyclic p-group sums. The sharp three-stage gap stabilization at p=2 and stark odd-prime independence are nontrivial uniform structural distinctions, much more useful than isolated small-group counts. The result can inform group actions of C2 on rank-two modules and is not a simple product of cyclic involution totals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
