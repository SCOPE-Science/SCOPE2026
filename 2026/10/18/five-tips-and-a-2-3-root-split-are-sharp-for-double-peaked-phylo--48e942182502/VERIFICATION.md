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

Correct for both the original and the narrower repaired claim. Positive edges and unit-height ultrametricity make V_1=V_n=0, and the only two nonadjacent interior indices at order five are 2 and 4. Exact hypergeometric covariance of edge-omission indicators, evaluated for all three binary shapes in /workspace/branches/replay_2.py, independently checks the two 1+4 decompositions, the three 2+3 variances and both phase polynomials. The repaired files put the omission formula, both descendant-set/length tables, and the two exact negative expressions in the proof. In the ladder all contributing terms have strictly negative signs; for two cherries the quadratic 3y²−4yz+3z²=(y−z)²+2(y²−yz+z²) is positive for the positive stem lengths. Thus V_2<V_3 regardless of lengths in both 1+4 cases. For the frozen 2+3 witness the independent replay recovered (0,263/4800,19/400,29/600,0), with positive gaps 7/960 and 1/1200. The frozen verifier was inspected, not run. Corrected RESULT.md, REVIEW.md and SLOGAN.txt are in /workspace/repairs/2/.

## originality

PASS

PASS applies to the repaired uniform 1+4 exclusion only. The original attribution of distinct contribution to the exact 2+3 phase region cannot pass as written: the onset result and both phase inequalities are already represented in distinct catalogue record 784aa021ee67, with an explicit change of coordinates showing equivalence. Neither the priority nor the dependency of the two records follows from their catalogue dates. The corrected files credit the overlap and isolate the all-length obstruction on both 1+4 shapes, expressly left unclassified by 784aa021ee67.

## value

PASS

The repaired uniform inequality V_2<V_3 shows that the root partition is a necessary structural constraint at the first possible tip count, not just a way to construct one bimodal example. It exhausts both singleton-root shapes across a continuous length domain and turns the known phase region on one shape into a complete minimum-order classification. It does not characterize higher-order or empirically reconstructed trees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
