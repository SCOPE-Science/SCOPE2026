# Scientific review

## Correctness — PASS
The claim is specifically that the 2012 nonnilpotent-operator dyadic inequality fails for the displayed invertible \(4\times4\) matrix. The dyadic series converges absolutely, and submultiplicativity bounds its first two terms by \(3\|T\|/4\) and its entire remaining tail by \(\|T^4\|^{1/4}/4\). The exact finite binomial bound for \(T^4\) gives \(D(T)<31503/40000<4/5\). The normalized path-sine vector gives \(w(T)>(1+\sqrt5)/4>4/5\). Determinant \(\varepsilon^4\) establishes invertibility. Uniform convergence on norm-bounded sets and numerical-radius Lipschitz continuity establish the open-set assertion. `verify.py` reproduces the rational certificate and matrix-power identities. The computation does not claim to numerically sum all infinitely many terms.

## Originality — PASS, with explicit antecedent
Paul and Bag's 2012 Example 2.5 already displays the nilpotent \(S\) and its strict inequality in the *opposite* direction from the conjectured bound, but their Conjecture 2.7 explicitly excludes nilpotent operators. The new, nonnilpotent counterexample is therefore not an instance covered by the premise of the original example or by the stated conjecture, and no inspected later paper states this refutation. The continuity proof is elementary, so this is a narrow negative answer, not a claim to discovering the seed nilpotent or proving a new general norm inequality. Searches for alternative wording and stronger numerical-radius bounds did not identify a prior exact implication. Residual risk: the argument might have circulated unpublished or in an unindexed note, and the source already contains all ingredients except the explicit continuity deduction.

## Value — PASS
This is a motivated, definitive negative answer to a published numerical-radius conjecture in its intended nonnilpotent domain, not a random matrix computation. The invertible witness prevents repairing the claimed inequality merely by excluding nilpotents, and the open-set argument shows the failure is robust rather than a singular boundary artifact. The sharp rational separation is supplied only to make the scientific conclusion checkable, not marketed as an optimized constant. A finer valid replacement inequality remains open.

Same-model review: passed. Independent audit: not yet performed.
