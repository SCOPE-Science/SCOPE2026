# Review of the characteristic-three nine-variable quartic

## Correctness

PASS. The precise domain is an algebraically closed field of characteristic three. Euler's relation identifies gradient zeros with quartic singular support. The common cubic for coordinate values limits all critical vectors to three values. For three distinct values, comparison of the first two symmetric coefficients rules out all multiplicity residues except one modulo three, and the third coefficient leaves exactly the \((1,1,7)\) and \((1,4,4)\) patterns with the displayed linear constraints. All one- and two-value possibilities are checked by a complete eight-row derivative table. Distinctness of the \(351\) lines and normality follow from the resulting one-dimensional singular support. The standalone exact-coefficient checker returns `VERIFY_OK` and independently checks all \(\mathbb P^8(\mathbb F_3)\) points.

## Originality

PASS on the available comparison, with residual literature risk. Cafure--Matera--Privitelli prove a partition-bound, Orzel studies dimension criteria, and Xie proves the exact dimension and generic local rings of coordinate components. Xie explicitly leaves lower-dimensional components unclassified. For this quartic, those results do not entail the enumeration of the \(315\) noncoordinate balanced lines or prove there are no further components. Searches for the exact \(351\)-line statement, its multiplicity patterns and equivalents in the research database and on the web produced no covering statement. Earlier results about degree-three elementary-symmetric polynomials in characteristic three or degree-four examples in characteristic two do not imply the present degree/characteristic combination. The risk of an implicit equivalent in other literature remains.

## Mathematical value

PASS. The result gives a complete, exact reduced singularity classification for a canonical characteristic-three symmetric quartic sevenfold. It distinguishes \(315\) noncoordinate components from the \(36\) coordinate components already treated by broader theory while the overall dimension stays unchanged. The degree \(351\), purity, and normality are natural geometric consequences, not merely an arbitrary finite count. No general formula for all dimensions or complete Jacobian primary decomposition is asserted.

## Limitations and related literature

The proof does not compute generic/non-generic nilpotent thickening or line-intersection multiplicities. Closest sources: arXiv:1109.2265v1 §3, arXiv:2509.05009v3 §2, arXiv:2610.00259v1 Theorems 1.1--1.4 and §7, MathOverflow 264226. Independent verification by an external specialist remains outstanding.

Self-review: passed. Independent audit: not yet performed.
