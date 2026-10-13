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

Run `python3 artifacts/verify.py` with a standard Python 3 interpreter.

The verifier constructs all \(\binom{21}{7}=116280\) multisets of seven nonempty storage subsets of four labeled servers. It checks the \(t=1\), \(k=3\) Hall condition in two independent forms: explicit unions of all one-, two-, and three-item selections, and containment counts inside every one- or two-server set. The predicates must agree for every ambient candidate.

It then confirms minimum storage \(12\), exactly \(46\) minimizing multisets, the two profile counts \(16\) and \(30\), the four server-relabeling orbit sizes \(4,12,6,24\), stabilizer orders \(6,2,4,1\), and the fully labeled count \(171360\). Separately generated structural families from the four representatives must equal the exhaustive minimizer set exactly.

The computation is finite and exhaustive only for the stated parameter. It does not certify any unbounded family or any independent audit.
