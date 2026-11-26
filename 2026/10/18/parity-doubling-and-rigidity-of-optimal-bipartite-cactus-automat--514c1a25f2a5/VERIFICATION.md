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

Inserting a positive closed subwalk at a state of an accepting run preserves acceptance and changes length by a multiple of m. Transition-compatible two-colouring also makes its length even. Hence the first h=lcm(m,2) states of a sufficiently long accepting run are distinct, and at equality the next state is necessarily the first. The resulting directed h-cycle is usable on an accepting run at every state. For any arc i→j, following it with the forward cycle path from j to i would give an insertable closed walk of length between 1 and h, so that length must be h and j must be i+1. This directly checks the rigidity step, even without using cactus to exclude chords. A word of sufficiently large accepted length can prescribe any letter at any phase, forcing all labels on each arc. With those transitions, acceptance forces exactly the residues stated. The construction is an even undirected cycle, or one simple edge at h=2. Dropping the even-length constraint gives the unrestricted m-state lower bound and matching modular DFA. The source's reference to an exception at m=4 in the reverse-arc argument is unnecessary: h≥4 always implies m≥3, and m=4 also does not divide 2. Frozen logged checks cover construction consistency, not arbitrary optimum NFAs; the uploaded script was inspected but not run.

## originality

PASS

Pass for the combined exact optimum and all-minimizers classification, not for independent originality of the state-count formula or modular pumping. The thresholded unary result covers the minimum for the whole target via its unary specialization and restriction to one letter. It proves a cycle lower bound and constructs one optimum; the supported distinct conclusion is that every optimum is the fully labelled cycle with the specified start and final set. This is an equality analysis, not a new numeric case of the threshold formula. No historical priority is inferred from catalogue path dates.

## value

PASS

The restricted state complexity is a natural family question left open by the general construction, and the full equality result says considerably more than that a small DFA exists: nondeterminism, deletion of letters and alternative accepting sets are all impossible at the optimum. The independent unrestricted count and arithmetic factor alone would not justify a separate value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
