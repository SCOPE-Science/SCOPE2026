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

The complete infinite proof is given in `RESULT.md`. Its critical upper-bound steps are the classification into adjacent/near/far supports, the count of different singleton-weight descendants, and the distance-two path-graph constraint among near supports. The lower-bound construction separates all possible output weights and classifies output-pair residues modulo four.

Run the bundled standalone program with `python checker.py`. The actual executable checks the construction for all lengths \(3\) through \(300\), confirms its exact cardinalities, and independently enumerates the one-weight descendants and the forced collision of consecutive near candidates for lengths \(3\) through \(34\). The optional `optimizer_optional.py` constructs a separate exact finite integer linear program from scratch, using NumPy and SciPy; its default lengths are \(3\) through \(16\), and `python optimizer_optional.py 30` extends the cross-check through length \(30\). The solver must report proved zero integrality gap for each instance. This optimization is supplemental, not an infinite certificate.

None of these finite computations can replace the algebraic proof or establish originality. The published comparison is limited to the cited material; independent mathematical validation has not been performed.
