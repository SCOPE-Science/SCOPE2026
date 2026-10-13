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

Use Python 3.8 or newer, standard library only, to execute `python verify.py` in the directory containing both this file and `verify.py`. The program constructs the graphs with \(6r+1\) vertices for \(r=1,2,3\) and exhausts \(2^{6r+1}-1\) nonempty candidate subsets. Each candidate is tested against the definition of a fort; minimality is tested against all proper subsubsets, not just one-vertex deletions. Results are compared with coefficient profiles of \(3rz^2+8rz^3+12^rz^{2r+1}\), including coincident degrees at \(r=1\). The output must match `verification_output.txt` exactly.

Enumerated candidate counts were respectively 127, 8,191 and 524,287, totaling 532,605. Observed minimal-fort counts were 23, 166 and 1,761. The size profiles were \((3,20)\) for degrees \(2,3\) when \(r=1\), \((6,16,144)\) for degrees \(2,3,5\) when \(r=2\), and \((9,24,1728)\) for degrees \(2,3,7\) when \(r=3\). Direct finite checks do not establish the limit or the infinite family; the complete mathematical proof is in `RESULT.md`.

Independent audit has not been performed.
