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

Run `python3 verify_colored_paths.py` with Python 3.10 or later (standard library only). The supplied `verification_output.txt` is the output from an execution of exactly this program.

The program compares coefficient formulas against all admissible independent path subsets for each \(m\in\{4,\ldots,16\}\), including empty remainders and all congruence classes of path blocks. It constructs two-color simplicial face chains for \(m=4,5,6,7\), directly projects each chain group to eigenchains for selected fiber transpositions, computes modular ranks at 101 and 103, and compares degree-by-degree homology dimensions and traces. It independently compares fixed-face alternating Euler traces with diagonal character formulas for \(m=4,\ldots,8\) and \(n=2,3,4\).

The modular computations do not prove rational homology in untested dimensions or exclude torsion at untested primes. The infinite-family result follows from the exact rational chain splitting, the path-link suspension recurrence, and the published numerical Betti formula; the verifier tests these identities in finite examples. No independent mathematical audit or external certification was conducted.
