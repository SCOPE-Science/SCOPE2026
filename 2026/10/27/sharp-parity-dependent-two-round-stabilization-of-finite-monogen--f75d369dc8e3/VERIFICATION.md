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

# Reproduction of finite checks

From the extracted package directory, run `python3 verify_mono.py`. The script uses the Python standard library and has no external inputs. It independently enumerates all eight ternary-atomic substitutions on a two-element tuple (and equality), builds the exact quantifier-rank-two extension types, compares stabilization instances, checks signatures across several indices, and directly evaluates the distinguishing sentence. The shipped `verify_output.txt` records its successful execution.

The finite test parameters are \(1\le p\le30\) with all \(1\le m\le 2\operatorname{lcm}(p,2)+4\) for the formula, plus selected larger indices for theory comparisons. This is not a machine proof of infinitely many cases. The universal argument is the residue-saturation and atomic-diagram proof in `RESULT.md`. Independently checking arbitrary high periods, all cross-period classes, and all subthreshold coincidences is outside this claim.
