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
# Verification of the Rees zero-matrix classification

Run `python3 verify.py` with Python 3 and no third-party dependencies. The program constructs groups \(C_1\), \(C_2\), \(C_3\), and \(S_3\), their exact multiplication, and Rees zero-matrix semigroups. For every choice of the two conjugators in the adjoined monoid, it computes the defining domain directly and stores the graph of the resulting partial map. Separately it enumerates the predicted map graphs from each pair of nonzero idempotents and inner conjugation, and compares the exact sets. It also checks the claimed number of maps and, when small enough, closure under all pairwise map compositions.

Fourteen cases were checked, including the one-by-one group-with-zero case, Brandt matrices, sandwich entries different from the group identity, rectangular supports, zero rows/columns, and an all-zero matrix. The result was `ALL CHECKS PASSED`. The two seven-element trivial-group examples were exhaustively tested against all bijections and have respectively zero and twenty-four complete mappings.

The symbolic proof in `RESULT.md` supplies the general all-group/all-index conclusion. The enumerations do not cover arbitrary groups or prove novelty. Full independent mathematical audit has not occurred.
