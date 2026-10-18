# Review of materializer order and two-scale satisfiability

## Correctness — PASS

The complete residual cases were independently reconstructed from the Heyting adjunction rather than read from a counting formula. For nonempty Boolean antecedent \(A\), the equality with material implication fails exactly on Boolean supersets of \(A\) and on the added non-top points. For antecedent \(t_i\), it fails exactly on the interval from \(t_i\) to the predecessor of the global top. The resulting sets prove the inclusion-order isomorphism, all cardinality coefficients, and the exact failure probability. The asymptotic claims are direct normalized limits of this identity. An independent Python 3 verifier exhaustively checked \(25\) finite parameter pairs and \(8955\) ordered input pairs. It does not replace the parameter-uniform argument.

## Originality — PASS, with residual risk

Bumpus and Kocsis's *Degree of Satisfiability in Heyting Algebras* (arXiv:2110.11515; DOI:10.1017/jsl.2024.2) is the nearest primary source. It defines materializers, gives their general properties, and establishes failure of finite satisfiability gap using a Boolean algebra with a single added top. Its proof obtains a lower bound and does not state a materializer order, complete size polynomial, exact count for arbitrary appended chain length, or the two asymptotic scales. Those earlier inputs are explicitly credited rather than claimed as new. Additional mathematical-finding searches and related summary comparisons found no same-object covering statement. A differently named earlier derivation remains possible; independent priority verification is outstanding.

## Mathematical value — PASS

The antecedent-specific materializer is a motivated structural invariant: it records exactly where residual implication agrees with classical material implication. The classification recovers the nonzero Heyting order from materializer containment, while the generating polynomial contains its complete satisfaction-size profile. The exact parameterized law sharpens a published qualitative/no-gap example and separates an early defect-mechanism crossover from an order-one transition. The result is limited to Boolean--chain sums, not arbitrary finite Heyting algebras.

## Verification and limitations

Run `python verify.py`; the observed terminal output is `VERIFY_OK exhaustive_parameter_pairs=25 evaluated_input_pairs=8955`. The proof of the arbitrary-parameter formulas and their limits is in RESULT.md. There is no infinite formal certification, no broad uniqueness guarantee from searching, and no external audit.

Self-review: passed. Independent audit: not yet performed.
