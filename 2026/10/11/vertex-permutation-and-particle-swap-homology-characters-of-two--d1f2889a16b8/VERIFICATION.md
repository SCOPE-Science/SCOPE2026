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

# Reproducibility and limits

Run `python3 verify_sink_complete.py` using Python 3.9 or later in the directory containing both standalone artifacts, then compare standard output with `verification_results.json`. The script requires no third-party packages.

For each \(m\in\{4,5,6\}\), the checker constructs the complete \(m^2\) zero-cells, \(2m\binom m2\) one-cells, and \(\binom m2(\binom m2-1)\) two-cells of the graph-product sink complex, checks every column of \(\partial_1\partial_2=0\), and constructs for every edge two integral triangle cycles whose coordinate product is a unit in that edge and zero elsewhere. It computes the two boundary ranks modulo \(2,3,5,7\), verifies all Betti numbers, and exhaustively checks the signed cellular Lefschetz traces for all \(2m!\) graph-permutation/label-swap combinations.

The verified outcomes are \((16,48,30)\) cells with Betti ranks \((1,6,3)\) at \(m=4\), \((25,100,90)\) with \((1,12,26)\) at \(m=5\), and \((36,180,210)\) with \((1,20,85)\) at \(m=6\). The respective counts of checked group elements are \(48,240,1440\).

These finite computations do not establish any infinite statement by enumeration and modular ranks alone cannot exclude torsion. The all-parameter proof in `RESULT.md` uses an integral surjectivity argument and the integral relative homology long exact sequence, independently of bounded experiments. Group characters are rational and are not claimed to be a classification of integral group lattices. Independent audit status: not performed.
