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

For any permutation sigma, equivariance of each unordered-input-pair orbit forces a choice in Fix(sigma^ell), giving exact probability n^{-binom(n,2)} product over edge orbits of |Fix(sigma^ell)|. A transposition fixes binom(n-2,2)+1 pairs and pairs up 2(n-2) other inputs into n-2 orbits, yielding p_n=n^{-(n-2)}(1-2/n)^{binom(n-2,2)+1}. A permutation with support k>=3 has edge-orbit compression D>=k(2n-k-2)/4; splitting k<=n/2 and k>n/2 gives the displayed explicit B_n=o(p_n/n²). Two distinct transposition automorphisms have a product moving >=3 labels, so outside tail event the entire group is either trivial or unique C2; this yields Pr(E_n)=binom(n,2)p_n(1+o(1)) and first Burnside correction. Expansion of the exact p_n gives e^4/2 e^{-n} n^{4-n}. Independent complete enumeration of all 27 n=3 and 4096 n=4 operation tables found 9 and 400 nontrivial, 6 and 336 unique-C2 respectively, and 7 and 192 unlabeled classes; these finite checks support but do not replace the all-n orbit bound.

## originality

PASS

Bergman–Szendrei Lemma 5.4 proves qualitative almost-sure asymmetry of random idempotent linear conditions; Tureček provides Burnside formulas for general finite magmas; OEIS A030257/A030259 list finite unlabeled commutative-idempotent isomorphism counts. None of the inspected relevant statements gives the exact leading labelled nonrigidity probability, the e^4/2 constant, or conditional unique transposition group. Cardó 2023 qualitative groupoid asymmetry has only its accessible abstract inspected; full text remains material priority risk. The Burnside correction is a consequence, not a wholly new enumeration theory.

## value

PASS

The event of rare symmetry has mathematical content beyond ordinary unlabeled Burnside census. The sharp asymptotic probability, leading constant and almost-sure complete automorphism group conditional on failure of rigidity refine classical zero-one rigidity results for a natural universal algebra model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
