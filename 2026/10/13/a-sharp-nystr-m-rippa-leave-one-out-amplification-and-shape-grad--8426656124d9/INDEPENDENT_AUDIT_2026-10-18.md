# Independent mathematical audit

## correctness

PASS

Exact inverse of a general positive 2x2 matrix gives E=(y1-(b/d)y2,y2-(b/a)y1). Substitution into both ridge matrices produces a rank-one discrepancy with singular value D, attained at e2. Independent SymPy differentiation confirmed D prime numerator lambda-(1+3lambda)t²-t⁴ and the loss derivatives with factors t and lambda-t²; the unique stationary point and boundary-layer limit follow analytically. The inverse-multiquadric correlation t maps bijectively to positive shape parameter, whose derivative is strictly negative, preserving opposite gradient signs. No mistaken minimum is claimed.

## originality

PASS

Lyu and Veiga introduce the same inverse-multiquadric Nyström/Rippa shape objective and discuss its numerical sensitivity, but the inspected full arXiv HTML does not derive the exact 2x2 rank-one residual operator, worst-case ridge divergence or the interval of opposite derivatives. Rippa gives the standard inverse-diagonal identity, not the matched-ridge comparison. Bucci–Nakatsukasa–Park investigate numerical Nyström stability, while this counterexample holds in exact arithmetic with core 1. The Rippa inverse-diagonal identity applies to both matrices but does not give their sharp difference or derivative sign for matched ridge; source shape numerical studies do not entail the exact classification.

## value

PASS

Ridge-Nyström Rippa cross validation is specifically used to select kernel shape; exact sign disagreement between full and surrogate gradients is directly diagnostic of tuning failure. The exact two-site phase, attained worst-data amplification and small-ridge asymptotic constant constitute a sharp natural base case, not merely a numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
