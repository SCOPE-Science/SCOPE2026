---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

At lengths at least four the two start parities are disjoint: in an odd window, two initial unequal pairs would require three equal underlying letters, which are absent. A circularly extendible aligned word is the image of an extendible parent; the odd-start counterpart is its one-step rotation. This gives exactly the rotations of T_k from the base E(4), and they are distinct since the unique defect-free circular pairing forces any period to be even and to descend to a period of T_(k-1). An odd window with unequal underlying endpoints has precisely one defect in its natural pairing at the wrap pair and at least two defects in the opposite pairing (at least two underlying transitions in length m+1≥5). Any rotation that occurs must therefore be an odd window of the same kind with that very defect still at the wrap pair, forcing the identical displayed factor. All remaining odd windows contribute once for each extendible parent, and the defect-free pairing makes aligned conjugacy descend exactly. The endpoint count doubles under the two odd-length desubstitutions, giving 2m new singletons at length 2m. Applied to the four classes at length four, this proves the full induction, including that the three named images remain distinct doubletons. Independent replay `python3 -B /workspace/reproduce_frozen.py 5` produced the histogram, extendible core and all three distinct doubletons through N=256 using digit parity, complete prefixes certified by the four adjacent pairs, and naïve rotations. The finite replay corroborates rather than replaces the induction.

## originality

PASS

The supported contribution is the exact occupancy spectrum and named exceptional classes, not c_t(N), the general conjugacy predicate, or the existence of full-rotation classes. Earlier primary sources inspected determine aggregate counts or partial structure, not this refinement. A distinct later-dated catalogue entry does explicitly give the same histogram and full class; it is a real content overlap, but its available record does not establish earlier coverage of the frozen result, and the inspected passage does not give the three named size-two representatives.

## value

PASS

Dyadic lengths are the natural self-similar scales of the substitution. The result gives the exact failures of reconstruction up to rotation from the occurring language, distinguishing a dense core from three persistent pairs and a growing population of isolated classes. The aggregate complexity misses precisely that information; named representatives and the extendible-core argument are useful for subsequent factor and conjugacy calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
