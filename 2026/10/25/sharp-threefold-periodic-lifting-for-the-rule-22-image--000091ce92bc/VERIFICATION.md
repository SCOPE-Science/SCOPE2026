---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

From exact Rule 22 truth table, two-bit overlap relations on states 00,01,10,11 are L0=(1,8,2,12), L1=(2,4,1,0) as four bit masks. A word w repeated cyclically has a kn-periodic antecedent iff the Boolean relation R(w)^k has a loop; any periodic image word yields a directed cycle in its four-state return graph. An independent exact integer BFS from the identity, closing under both symbols without word-length cutoff, found exactly 2375 reachable relations and multiplier classes {1:2012,2:130,3:2,4:0,none:231}. The only multiplier-three-first relations are L1 and L1². Augmenting reachable relation with a flag recording an encountered zero gives 2375 augmented states and no zero-containing path with first return 3. L1 is a directed 3-cycle, proving all-one output needs factor3 precisely when 3 does not divide n; the word 001 has no 3-period antecedent but has a 6-period one. Thus uniform multiplier≤3, mixed/zero≤2, and both sharpness witnesses hold for every n, by exhaustive state closure, not a finite word cutoff.

## originality

PASS

General four-state labeled de Bruijn and Boolean-semigroup techniques are established, and the broad theorem on periodic preimages of SURJECTIVE CAs by Mariot et al (2017), and WPP decidability by Salo (2022), were materially compared. Rule 22 is NONSURJECTIVE and nonlinear/non-bipermutive; the prior general statements do not give its exact 2375-relation exhaustive classification, only exceptional all-one triple inflation, or the mixed-output factor-two theorem. The 2019 Martínez et al Rule 22 de Bruijn/subset diagrams were acknowledged; no evaluated same-multiplier result in inspected primary material. Best-knowledge PASS with potential older exact CA computations risk.

## value

PASS

Period lifting is a natural invariant of the image shift and periodic-point fibers of a classical nonlinear CA. An all-period exact and sharp multiplier classification (1,2,3), with the unique family requiring tripling and finite exhaustive semigroup proof, distinguishes strong periodic-point failure from complete image surjectivity; substantially more than numerical enumeration of short rings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
