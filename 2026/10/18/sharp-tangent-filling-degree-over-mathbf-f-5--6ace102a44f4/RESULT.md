# Sharp tangent-filling degree over \(\mathbf F_5\)

## Finding

A plane curve \(C\subset\mathbf P^2_{\mathbf F_5}\) is *tangent-filling* when the union of its tangent lines at smooth \(\mathbf F_5\)-rational points is all of \(\mathbf P^2(\mathbf F_5)\). The minimum degree of a geometrically irreducible tangent-filling plane curve over \(\mathbf F_5\) is exactly \(4\). In fact **no nonzero plane equation of degree \(1\), \(2\), or \(3\) is tangent-filling, even if the curve is singular or reducible**. Equality is attained by the geometrically smooth quartic

\[
C:\quad X^4+X^3Y+Y^3Z-Z^4=0
\]

of genus \(3\). Its \(11\) rational points have \(11\) distinct rational tangent lines, and those lines cover every one of the \(31\) points of \(\mathbf P^2(\mathbf F_5)\).

## Assumptions and scope

All coefficients, point coordinates, and derivatives are computed in \(\mathbf F_5\). Curves are homogeneous plane hypersurfaces. *Smooth rational point* means a rational zero where the gradient is not the zero vector; the tangent line there is the homogeneous linear form given by the gradient. Geometric smoothness of the displayed quartic is proved over the algebraic closure, rather than inferred from a finite enumeration. The optimality assertion ranges over every plane form over \(\mathbf F_5\), up to multiplication by a nonzero scalar, in each of the three lower degrees.

## Proof

**1. Geometric smoothness of the witness.** Write \(F=X^4+X^3Y+Y^3Z-Z^4\). Its partial derivatives modulo \(5\) are
\[
F_X=X^2(4X+3Y),\qquad F_Y=X^3+3Y^2Z,\qquad F_Z=Y^3+Z^3.
\]
If \(X=0\), the equations \(F_Y=F_Z=0\) force \(Y=Z=0\), which is not a projective point. If \(X\ne0\), the equation \(F_X=0\) gives \(Y=2X\); then \(F_Y=0\) gives \(Z=2X\), but \(F_Z=X^3\ne0\). Thus the three partial derivatives have no common projective zero over \(\overline{\mathbf F}_5\). The projective quartic is geometrically smooth and hence geometrically irreducible. By the plane adjunction formula, its genus is \((4-1)(4-2)/2=3\).

**2. The witness is tangent-filling.** Use the complete list of normalized projective points
\[
\{(u,v,1):u,v\in\mathbf F_5\}\ \cup\ \{(u,1,0):u\in\mathbf F_5\}\ \cup\ \{(1,0,0)\}.
\]
Exactly \(11\) of these lie on \(C\). The distinct tangent lines have the following normalized coefficient triples \((a,b,c)\), where a triple denotes \(aX+bY+cZ=0\):
\[
\begin{gathered}
(0,0,1),\ (0,2,1),\ (0,4,1),\ (1,1,1),\ (1,4,1),\\
(2,1,1),\ (2,3,1),\ (3,2,1),\ (4,1,0),\ (4,1,1),\ (4,4,1).
\end{gathered}
\]
The line \(Z=0\) covers all six points at infinity. Substituting each of the \(25\) affine triples \((u,v,1)\) into the other ten linear forms shows that each affine point lies on at least one of them. The exact \(31\)-point incidence computation, together with the full list of rational curve points, is independently reproduced by `verify_witness.py`. Thus the witness is tangent-filling.

**3. Exhaustive lower-degree exclusion.** For each degree \(d\in\{1,2,3\}\), let \(M_d\) be the ordered list of all degree-\(d\) monomials in \(X,Y,Z\), ordered by descending exponent of \(X\) and then descending exponent of \(Y\). It has \(N_d=\binom{d+2}{2}\) elements. Every nonzero homogeneous form is a unique scalar multiple of a vector whose first nonzero coefficient, in this order, is \(1\). For each leading index \(i\), the remaining \(N_d-i-1\) coefficients vary independently over the five elements of the field, giving exactly
\[
\sum_{j=0}^{N_d-1}5^j=\frac{5^{N_d}-1}{4}
\]
projective equations. These are \(31\), \(3906\), and \(2441406\) respectively.

For **every** such coefficient vector, the finite algorithm evaluates the form at all \(31\) normalized rational points, computes all three formal partial derivatives at each rational zero, discards any zero with vanishing gradient, and unions the rational points of the associated tangent lines. A curve is tangent-filling if and only if this union has size \(31\). The complete enumeration in the self-contained exact-arithmetic `verify_tangent_f5.cpp` returns **zero** tangent-filling equations in each of the three degrees. Each loop has explicitly fixed finite bounds, all operations are integer arithmetic reduced modulo \(5\), and scalar-normalization gives an exhaustive, repetition-free census; no probabilistic sampling or singularity assumptions are used. An separately implemented vectorized census `verify_vectorized_numpy.py` again obtains \(2441406\) cubic forms and zero tangent-filling cases. This proves the lower bound and, with the quartic, the theorem.

## Verification

The package contains `verify_tangent_f5.cpp` (standalone C++17), `verify_witness.py` (Python standard library), and `verify_vectorized_numpy.py` (independent optional NumPy replay for the cubic census). All were executed with their actual packaged contents. The C++ program reported

```text
degree=1 normalized_forms=31 tangent_filling=0
degree=2 normalized_forms=3906 tangent_filling=0
degree=3 normalized_forms=2441406 tangent_filling=0
smooth_quartic_witness_rational_points=11 tangent_points=11 union_points=31
MINIMUM_DEGREE_4_VERIFIED
```

The Python witness checker reported `WITNESS_VERIFIED` and \(11\) tangent lines covering \(31\) points. The separate NumPy census reported `vectorized numpy census 2441406 0`. Reproduce with `c++ -O2 -std=c++17 verify_tangent_f5.cpp -o verify_tangent_f5 && ./verify_tangent_f5`, then `python3 verify_witness.py`; NumPy is needed only for the optional third script. Geometric smoothness uses the hand proof above, not finite-field sampling.

## Relationship to prior work

Asgarli and Ghioca's *Tangent-filling plane curves over finite fields* (first public version 26 February 2023, arXiv:2302.13420) defines the property and explicitly asks for the minimum degree over each finite field (Question 1.5). Their main construction has degree \(q-1\) for \(q\ge11\), in odd characteristic exceeding three. Their Remark 1.4 says the same displayed construction is **not** tangent-filling when \(q=5\). The present result treats the separate case \(q=5\) and supplies a different smooth degree-four witness as well as the sharp lower bound. Their general nonexistence bounds have hypotheses far above \(q=5\) for cubic curves and therefore do not give this small-field exclusion. Their full accessible arXiv text, including the introductory question, nonexistence arguments, construction, and small-field remarks, was checked.

The related paper *Plane-filling curves of small degree over finite fields* (Asgarli–Ghioca, arXiv:2307.03072) concerns the stronger condition of containing **all rational points**, rather than covering them by tangent lines. Its cited smooth plane-filling minimum of \(q+2\) does not determine the tangent-filling minimum. Previously recorded exact tangent-filling classifications in characteristics \(2\), \(3\), and over \(\mathbf F_4\) concern other fields and do not imply the result over \(\mathbf F_5\).

## Limitations

The theorem determines the **minimum degree over one field**, not a uniform formula for all prime powers or the number of tangent-filling quartic isomorphism classes. The lower bound is certified by an exhaustive finite computation and two independently implemented cubic enumerations, not by a conceptual uniform obstruction. A hidden or unindexed prior small-field computation could affect originality; targeted published-literature and mathematical-record searches have not identified one. No independent external audit has been performed.

## References

1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420 (first posted 2023-02-26), *Bull. Aust. Math. Soc.* 109 (2024), 301–315, DOI:10.1017/S0004972723000382. Accessible full text: https://arxiv.org/html/2302.13420v2 .
2. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072 (2023), https://arxiv.org/abs/2307.03072 .
