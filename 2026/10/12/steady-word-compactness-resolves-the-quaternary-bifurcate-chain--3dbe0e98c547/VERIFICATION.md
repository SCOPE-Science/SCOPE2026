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
# Verification

The proof is noncomputational, so there is no finite certificate whose successful replay could establish the infinite conclusion.

The two nonstandard mathematical inputs were checked in the full public preprint of Dębski, Grytczuk, and Pawlik:

1. Theorem 1 gives arbitrarily long steady words over a four-letter alphabet.
2. Theorem 3 says that, over a fixed alphabet with at least three letters, every steady word is bifurcate.
3. Conjecture 2 asks for an infinite sequence of quaternary bifurcate words in which each next word is a single-letter extension of the preceding word.

The new proof then has two independently inspectable logical steps.

First, steadiness is factor-hereditary. If \(U\) is a factor of a steady word \(W\), then \(U\) is square-free. After deleting any chosen letter of \(U\), the resulting word is a factor of the word obtained by deleting the corresponding letter of \(W\). The latter is square-free by steadiness, so the former is square-free.

Second, fixed-alphabet steady words form a prefix-closed tree with at most four children per vertex and with vertices at arbitrarily large depths. König's infinity lemma gives an infinite branch. Every finite factor of the branch lies in a steady prefix and is therefore steady; Theorem 3 then makes it bifurcate.

The argument proves existence only. It does not give a computable formula for a particular infinite branch, nor does it produce a complete bifurcate tree over four or five letters. Independent audit has not been performed.
