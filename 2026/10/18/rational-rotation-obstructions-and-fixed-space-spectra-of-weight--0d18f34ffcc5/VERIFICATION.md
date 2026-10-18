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
# Verification and limitations

The exact formulas can be recomputed without external packages by running `python3 verify.py`. This script enumerates every possible weighted-rotation monomial matrix directly from the defining multiplication relations, obtains the dimension of its \(1\)-eigenspace by finite-field Gaussian elimination, and compares the resulting distribution with the two-arithmetic-obstruction formula. The run covered 843 configurations in the prime and extension fields \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_8,\mathbb F_9,\mathbb F_{11},\mathbb F_{13},\mathbb F_{16},\mathbb F_{19},\mathbb F_{31},\mathbb F_{43}\), with dimensions at least two and multiple nonzero twist parameters in each field. The result was `VERIFY_OK 843 independent finite-field configurations`.

The same program exhaustively checks the special \(n=6\), \(q=43\), \(t=37\) configuration: precisely \(63\) automorphisms exist, the identity fixes the entire six-dimensional algebra, and each of the other \(62\) automorphisms has zero-dimensional fixed space. The group-order and noncommutativity assertions also follow from explicit arithmetic in the proof: the diagonal subgroup has order \(21\), an allowed shift acts nontrivially on it by the exponent \(16\), and shifts \(2\) and \(4\) have no fixed-vector lifts.

These experiments are finite cross-checks, not an exhaustive test over all fields, all dimensions, or all twists. The universal result is supported by the monomiality argument, recurrence, cyclic-group power-equation counts and fixed-cycle computation in `RESULT.md`. The proof and calculations have not been independently audited by another mathematician. Originality is subject to the documented residual risk from specialized literature not located or inspected.
