# The metric James constant is exactly a reparameterization of the James constant
## Finding
## Finding
For every real Banach space \\(X\\) with \\(\\dim X\\ge 2\\), let
\[
J(X)=\\sup_{x,y\\in S_X}\\min\\{\\lVert x+y\\rVert,\\lVert x-y\\rVert\\}
\]
and let the metric James-type constant introduced by Chen--Yang--Liu--Li be
\[
J_1(X)=\\sup_{x,y\\in S_X}\\min\\left\\{\\frac{{\\lVert x+y\\rVert}}{{1+\\lVert x+y\\rVert}},\\frac{{\\lVert x-y\\rVert}}{{1+\\lVert x-y\\rVert}}\\right\\}.
\]
Then
\[
J_1(X)=\\frac{{J(X)}}{{1+J(X)}}.
\]
Thus \\(J_1\\) contains exactly the same numerical information as \\(J\\), with inverse relation \\(J(X)=J_1(X)/(1-J_1(X))\\).

As a direct consistency consequence, the printed Corollary 2 in the 2022 source,
\[
\\rho_X(1)\\le 2\\left(1-\\frac{{3}}{{J_1(X)}}\\right),
\]
cannot be correct as written. The same paper proves \\(J_1(X)\\le 2/3\\), so the displayed right-hand side is at most \\(2(1-9/2)=-7\\), while by definition the modulus of smoothness satisfies \\(\\rho_X(1)\\ge0\\).

## Assumptions and scope
The space is real and has dimension at least two, matching the standing scope of the source paper. No compactness, reflexivity, smoothness, strict convexity, or attainment of the defining supremum is assumed.

The claim concerns the exact relation between the classical James constant and the metric James-type constant \\(J_1\\). It does not assert a new optimal inequality for the modulus of smoothness beyond identifying that the cited Corollary 2 is impossible as printed.

## Proof
Define \\(f:[0,2]\\to[0,2/3]\\) by \\(f(t)=t/(1+t)\\). This function is continuous and strictly increasing. For fixed \\(x,y\\in S_X\\), put \\(a=\\lVert x+y\\rVert\\) and \\(b=\\lVert x-y\\rVert\\). Monotonicity gives the exact pointwise identity
\[
\\min\\{f(a),f(b)\\}=f(\\min\\{a,b\\}).
\]
If \\(m(x,y)=\\min\\{\\lVert x+y\\rVert,\\lVert x-y\\rVert\\}\\), then therefore
\[
J_1(X)=\\sup_{x,y\\in S_X} f(m(x,y)).
\]
Because \\(f\\) is continuous and increasing on the compact interval containing all values of \\(m\\), it commutes with this supremum:
\[
\\sup_{x,y\\in S_X} f(m(x,y))
=f\\left(\\sup_{x,y\\in S_X}m(x,y)\\right)
=f(J(X)).
\]
This proves \\(J_1(X)=J(X)/(1+J(X))\\). The argument does not require a maximizing pair: if the supremum is not attained, take any sequence with \\(m(x_n,y_n)\\to J(X)\\) and use continuity of \\(f\\).

For the printed Corollary 2, the source's Proposition 2 yields \\(J_1(X)\\le2/3\\). Hence \\(3/J_1(X)\\ge9/2\\), so \\(2(1-3/J_1(X))\\le-7\\). On the other hand, the definition
\[
\\rho_X(1)=\\sup_{x,y\\in S_X}\\left(\\frac{{\\lVert x+y\\rVert+\\lVert x-y\\rVert}}{{2}}-1\\right)
\]
has nonnegative value: taking \\(y=x\\) gives the displayed quantity \\(0\\). Thus the printed inequality cannot hold.

## Verification
The proof was reconstructed directly from the two definitions in Section 2 of the source. The only functional step is the order identity \\(\\min\\{f(a),f(b)\\}=f(\\min\\{a,b\\})\\) for increasing \\(f\\), followed by continuity to pass a supremum through \\(f\\). Boundary values are consistent: the universal classical range \\(\\sqrt2\\le J(X)\\le2\\) maps to \\(2-\\sqrt2\\le J_1(X)\\le2/3\\), exactly the range recorded by the source.

The contradiction in the printed Corollary 2 was checked independently of the exact identity using only the source's bound \\(J_1(X)\\le2/3\\) and the defining nonnegativity of \\(\\rho_X(1)\\).

## Relationship to prior work
Chen, Yang, Liu and Li introduce \\(J_1\\) in Section 2, state the coarse comparison \\(J(X)/3\\le J_1(X)\\le J(X)\\) in Theorem 1, and state only the upper bound \\(J_1(X)\\le J(X)/(1+J(X))\\) in Proposition 1. Their Example 1 computes equality for the special family \\(\\ell_p\\), but the inspected full text does not state the all-Banach-space identity above. The same paper later prints the impossible Corollary 2 inequality identified here.

Searches for the exact identity, its inverse formulation, the metric-transform formulation, and the Corollary 2 correction did not locate a published statement covering the all-space claim. This negative search is not by itself a novelty proof; originality rests on the statement-level comparison with the full text of the defining paper and the absence of a stronger covering result in the checked literature.

MSC2020 code 46B20 is "Geometry and structure of normed linear spaces", which is the primary subject of this claim.

## Limitations
The originality check is necessarily limited by indexing and discoverability: an unindexed note may have observed the same elementary identity. The finding does not attempt to audit every subsequent theorem in the 2022 paper, and it does not infer that every result involving \\(J_1\\) is erroneous. It establishes only the exact reparameterization and the resulting impossibility of the specifically printed Corollary 2.

## References
1. B. Chen, Z. Yang, Q. Liu, Y. Li, "Some New James Type Geometric Constants in Banach Spaces", *Symmetry* 14 (2022), 405. DOI: 10.3390/sym14020405. First public date verified as 18 February 2022.
2. MSC2020, 46B20: Geometry and structure of normed linear spaces.
