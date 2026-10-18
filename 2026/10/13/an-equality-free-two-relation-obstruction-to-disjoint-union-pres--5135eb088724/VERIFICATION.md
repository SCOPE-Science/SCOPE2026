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

The exact signature has two arbitrary binary relations and NO identity symbol; domains nonempty. For two or more nonempty union summands satisfying Psi, take U-elements in different components: cross E is absent, supplying B; singleton unions preserve the model directly. For A on {a,b}, E has only loops aa,bb and Q only bb, so a is the unique U, B false, C true. Bmodel on {a,b,c}, E loops all, Q loops bb,cc, so a remains unique U but C false at (b,c). The two A embeddings {a,b},{a,c} into Bmodel are induced and relation-closed, cover Bmodel, and satisfy forward transfer for every comparison-language matrix by structural induction: atomic/negated atomic reflect through induced embedding; existentials copy witnesses; relation closure traps every guarded-universal witness in the embedded image. Universal outer x then transfers membership to every element of Bmodel, contradiction. Independent direct Python model evaluations and closure checks verified the finite interface; no finite-enumeration inference is used for the arbitrary-rank separation.

## originality

PASS

Best-of-knowledge PASS. The searched equivalence class includes disjoint-union one-way preservation, guarded universal/existential syntax, relation-closed induced covers, and equality-free logical signatures. The new sentence and separation lemma address the open case not logically supplied by the published identity witness. The published example cannot imply a definability counterexample in the strictly equality-free syntax on all arbitrary E,Q models, and the publication expressly excludes the stronger claim. The exact transfer lemma closes that logical gap. Residual priority/access caveats explicitly included; no search absence alone is interpreted as novelty.

## value

PASS

Gives an explicit negative answer to the exact identity-free open variant of a cited logical preservation conjecture, using only two unrestricted binary relations and a three-element obstruction. The relation-closed induced-image cover transfer lemma is a portable syntactic tool distinguishing one-way disjoint-union preservation from invariance; this is an important natural classification boundary, not a renamed identity-based counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
