# Review of the power-of-two Kneser orientation finding

## Correctness — PASS
The proof explicitly constructs all local \(p_n\)-spheres, establishes a maximal simplex with entire \(2n\)-element support, builds integral cocycles dual to the embedded sphere classes, and verifies the full rank and primitive integral splitting of their span. The determinant comparison of the permutation and complementary-pair actions gives the local orientation character. The valuation identity \(v_2(\binom{2r}{r})=s_2(r)\) proves the power-of-two criterion. Rational transfer gives the quotient consequence, and Feng's Theorem 18 supplies *only* the triple-case full rational rank. Independent finite checks in the supplied program pass for the documented instances. The main claims do not rely on extrapolating finite checks.

## Originality — PASS, qualified
Feng–Wang (2024, Lemma 9 and Theorem 10) already prove that the sphere classes are independent; Feng (2026, Theorem 18) already computes the rank in the triple case. Those are not new findings. The inspected texts do not give the all-parameter sign-versus-trivial stabilizer action, its binary-power criterion, the integral induced representation, the full triple-case rational character, or the forced quotient classes in non-power cases. The latter statements are deductions from the published geometric construction plus new orientation analysis. Search could miss an unindexed equivalent formulation; this remains a genuine risk.

## Mathematical value — PASS
The theorem determines the natural group action on an infinite family of primitive high-dimensional integral homology sublattices and identifies a sharp arithmetic dichotomy among otherwise identical dimension-lower-bound constructions. It produces concrete nonvanishing rational classes on highly symmetric quotient spaces, information not available from the previously published Betti lower bound. For triples the formula determines an entire rational homology representation, not only a dimension.

## Closest literature and limits
Feng–Wang (2024) is the direct geometric antecedent, and Feng (2026) supplies the complete rational rank for triples. Ramos–White (2017) gives broader representation-stability context without an exact statement here. Integral torsion outside the displayed free summand is not ruled out, nor is the other rational degree-\(p_n\) homology for \(n\ge4\).

Self-review: passed. Independent audit: not yet performed.
