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
# Verification and reproducibility

The theorem is proved algebraically in `RESULT.md`. The standalone Python program `verify_graph_face_jordan.py` independently constructs the basis and multiplication matrices and performs direct finite-field row reduction. Its predicted distribution is computed separately from the graph-support formula; the program compares joint ranks of multiplication and its square and refines by support cardinality.

A successful execution reports `ALL_GRAPH_FACE_JORDAN_CHECKS_PASSED 99 full configurations, 128 support configurations`. The full configurations include all labeled simple graphs through four vertices over \(\mathbb F_2\), all labeled graphs through three vertices over \(\mathbb F_3\) and \(\mathbb F_4\), selected further cases over \(\mathbb F_5\), and exact paw/four-cycle examples. The separate 128 cases verify the support-only formula for all labeled graphs on four vertices over \(\mathbb F_3\) and \(\mathbb F_5\).

Execute `python3 verify_graph_face_jordan.py` in a directory containing the embedded checker. No third-party dependencies are needed. The program works over the extension field \(\mathbb F_4\) using an explicit irreducible quadratic. These are finite consistency tests and do not prove the uniform statement; the proof rests on the graph incidence kernel argument and the radical-cube truncation. The historical originality assessment is necessarily bounded by the inspected sources. Independent mathematical audit has not been performed.
