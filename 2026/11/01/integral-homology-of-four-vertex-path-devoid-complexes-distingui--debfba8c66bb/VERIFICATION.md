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

Execute `python3 checks/verify.py` (Python 3.10+ recommended). `checks/verification_output.txt` is the deterministic expected output generated from this exact included source. Every one of the \(2^{16}\) vertex subsets is examined for each graph. Forbidden four-path supports are independently tested over all four-element subsets; the complete directed Hasse diagram is topologically sorted for matching acyclicity; integer chain differentials are formed from orientation-respecting gradient paths; no nonunit Smith factors remain after unimodular reduction. The unreduced simplicial chain complexes give independently computed mod-two ranks agreeing with the integral claim.

The calculated face counts including the empty simplex are 3,193 (Shrikhande) and 3,305 (rook). The matching leaves critical dimensions \((0,3,4,5)\) of counts \((1,38,51,6)\) and \((0,2,3,4,5)\) of counts \((1,1,17,89,18)\). The only nonzero differential ranks are respectively \(\operatorname{rank}(\partial_4)=6\), and \(\operatorname{rank}(\partial_3)=1\), \(\operatorname{rank}(\partial_4)=16\); the other differentials vanish.

Finite exhaustive certification of this pair is mathematically distinct from a theorem for all graphs. It proves integral homology, not an asserted homotopy wedge decomposition. No independent external mathematical audit has been conducted.
