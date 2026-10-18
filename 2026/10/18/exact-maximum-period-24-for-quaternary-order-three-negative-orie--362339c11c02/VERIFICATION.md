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
# Reproducibility and bounds

Run `python3 verify.py` without additional dependencies. The program enumerates every length-three word over the four symbols (exactly \(64\)), builds all involution classes (eight fixed and \(28\) paired), checks all ten quotient degrees and exactly two three-edge perfect matchings on six odd vertices, and recomputes the orientation-independent divergence sums \(-2\) and \(+2\). It then directly checks the \(24\) cyclic windows of the candidate, including reversal-negation separation.

The proof uses an exact finite table of \(28\) edge classes, not an uncertified search across all potentially long cyclic words. The parity lemma and the invariance of \(\Phi_v\) are proved algebraically in the accompanying mathematical result. Computational output agrees with `verification_output.txt`; this is reproducible checking, not an independent external audit.
