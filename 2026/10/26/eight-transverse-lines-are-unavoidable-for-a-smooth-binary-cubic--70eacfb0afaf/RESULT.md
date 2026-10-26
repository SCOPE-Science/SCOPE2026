# Eight transverse lines are unavoidable for a smooth binary cubic surface

## Finding

Let \(S\subset\mathbf P^3_{\mathbf F_2}\) be a geometrically smooth cubic surface. An \(\mathbf F_2\)-line \(L\) is **transverse** to \(S\) when its scheme-theoretic intersection with \(S\) consists of three distinct geometric points. Write \(T(S)\) for the number of these rational lines among the \(35\) rational lines in \(\mathbf P^3_{\mathbf F_2}\).

**Theorem.** Every such surface satisfies \(T(S)\geq8\). Equality is attained, and exactly \(840\) nonzero binary cubic forms (in fixed coordinates, with the unique scalar normalization over \(\mathbf F_2\)) give equality. These forms constitute a single orbit under \(\operatorname{PGL}_4(\mathbf F_2)\), of size \(840\) and stabilizer order \(24\).

A representative, with coordinates \([X_0:X_1:X_2:X_3]\), is
\[
F=X_0^2X_3+X_0X_3^2+X_1^3+X_1X_2^2+X_1X_2X_3+X_1X_3^2+X_2^3+X_2X_3^2.
\]

## Assumptions and scope

All coefficients and rational lines are over \(\mathbf F_2\); singularity and transversality are geometric conditions over an algebraic closure. The count \(840\) counts equations in **fixed coordinates**; the projective equivalence count is one, not \(840\). A line contained in a cubic surface is not transverse. No assertions are made for fields other than \(\mathbf F_2\), or for nonsmooth cubic surfaces.

## Proof

**1. Exact finite parameter space.** A homogeneous cubic in four variables has \(20\) monomials. Fix their order by the nested loops \(a=0,\ldots,3\), \(b=0,\ldots,3-a\), \(c=0,\ldots,3-a-b\), taking exponent vector \((a,b,c,3-a-b-c)\). Thus the nonzero cubic forms correspond exactly to integer masks \(1,\ldots,2^{20}-1\). The scalar group of \(\mathbf F_2\) is trivial.

Represent the nonzero vectors of \(\mathbf F_2^4\) by integers \(1,\ldots,15\). Every rational projective line has three vectors \(\{u,v,u\oplus v\}\) and is included exactly once in the enumeration \(1\leq u<v<u\oplus v\leq15\). There are exactly \(35\) such lines.

Restrict a form to a line by putting \(X_i=u_i s+v_i t\). Encode the resulting homogeneous binary cubic \(\sum_{j=0}^3 a_j s^jt^{3-j}\) by \(\sum_{j=0}^3 2^j a_j\). The binary cubic has three distinct geometric zeros precisely when its code is one of
\[
\{6,7,9,11,13,14\}.
\]
Indeed, dehomogenization \(t=1\) gives a polynomial whose derivative is coprime to it, and the root at infinity has multiplicity at most one, exactly for these six codes. This verifies transversality over the **algebraic closure**, without finite-extension sampling.

**2. Exhaustive lower bound.** For each one of the \(2^{20}-1=1{,}048{,}575\) nonzero masks, the program `verify_census.cpp` performs all \(35\) binary-cubic restriction tests. It also checks at every one of the \(15\) rational projective points that a zero of the cubic does not have all four partial derivatives zero. This is a *necessary* condition for geometric smoothness, and so any geometrically smooth surface lies within the retained set. In particular, among forms having \(0\), \(4\), or \(6\) transverse lines, exactly **zero** pass this necessary nonsingularity test. Among those with exactly \(8\) transverse lines, exactly \(840\) pass. No other smaller values of the transverse-line count occur for nonzero forms. The full census is reproduced independently in `verify_numpy.py` using a separate polynomial expansion and vectorized parity computation; its accepted set of \(840\) masks agrees exactly with the C++ coefficient certificate `extremal_coefficients.txt`.

The exhaustive restriction histogram and rational-point nonsingularity counts are in `census_output.txt`. This computation establishes the lower bound for all geometrically smooth surfaces, but does not by itself show that every one of the \(840\) remaining forms is geometrically smooth.

**3. Sharpness and projective orbit.** The displayed form is geometrically smooth. In characteristic two its partial derivatives are
\[
\begin{aligned}
F_{X_0}&=X_3^2,\\
F_{X_1}&=X_1^2+X_2^2+X_2X_3+X_3^2,\\
F_{X_2}&=X_1X_3+X_2^2+X_3^2,\\
F_{X_3}&=X_0^2+X_1X_2.
\end{aligned}
\]
A common projective zero would successively force \(X_3=X_2=X_1=X_0=0\), impossible. Hence \(S\) is smooth over the algebraic closure.

The script `verify_orbit.py` independently constructs the four standard generating changes of variables (three adjacent coordinate swaps and one elementary transvection), verifies that these generate all \(20{,}160\) members of \(\operatorname{GL}_4(\mathbf F_2)=\operatorname{PGL}_4(\mathbf F_2)\), and builds the orbit of coefficient mask `67194` representing the displayed cubic. Its orbit has \(840\) elements and equals the coefficient certificate **as a set**, not just in cardinality. Projective changes preserve geometric smoothness and \(T(S)\). Thus every one of the \(840\) extremal forms is smooth, the extremal locus is one projective orbit, and its stabilizer has order \(20{,}160/840=24\). This proves all assertions.

## Verification

From a working directory containing the bundled files, compile and run `verify_census.cpp` with a C++17 compiler. This creates `extremal_coefficients.txt`. Then run `verify_numpy.py` (NumPy required) and `verify_orbit.py` (SymPy required). The output files `census_output.txt`, `numpy_output.txt`, and `orbit_output.txt` record actual successful runs. The independent NumPy census uses different polynomial-expansion logic, computes squarefreeness by polynomial gcd, and compares **every** extremal coefficient mask with the first program. The orbit script separately checks both the full projective group and the partial-derivative proof.

## Relationship to prior work

Asgarli, Duan, and Lai (arXiv:1903.08845, first submitted 2019-03-21) develop the notion of transverse lines to surfaces over finite fields and prove large-field sufficient conditions, including a general condition \(q\geq d^2\). Their paper does not imply the small case \(q=2\), \(d=3\); its degree-\(q+2\) space-filling example emphasizes why small fields are exceptional.

Karaoğlu (2021, DOI 10.3906/mat-2102-10) classifies cubic surfaces over \(\mathbf F_2\) and tabulates rational **contained** lines, point configurations, and stabilizers. Its inspected text does not give the number of transverse ambient lines, the sharp minimum eight, or the unique extremal transverse-line orbit. A complete cubic-surface equation catalogue makes further computations possible, but contains no immediate implication to the present six squarefree restriction patterns without a new incidence calculation. Kadyrsizova et al. (arXiv:2007.12018) characterize Frobenius splitting and line configurations in characteristic two, a different invariant. Related rational-line counts (McKean, arXiv:2101.08217) concern lines contained in a surface rather than its transverse exterior sections.

## Limitations

Originality is assessed against the inspected literature and searchable mathematical records; an older unindexed small-field incidence calculation is possible. The proof is a finite exhaustive computation backed by transparent source code, plus a short symbolic geometric-smoothness proof; it is not a conceptual classification valid over arbitrary finite fields. The classification is over the base field and its projective linear group.

## References

- Shamil Asgarli, Lian Duan, Kuan-Wen Lai, *Transverse lines to surfaces over finite fields*, arXiv:1903.08845 (first public 2019-03-21), https://arxiv.org/html/1903.08845v3.
- Fatma Karaoğlu, *Non-Singular Cubic Surfaces over \(\mathbf F_{2^k}\)*, Turkish Journal of Mathematics **45** (2021), 2492–2510, DOI 10.3906/mat-2102-10, https://journals.tubitak.gov.tr/math/vol45/iss6/11/.
- Zhibek Kadyrsizova et al., *Cubic Surfaces of Characteristic Two*, arXiv:2007.12018 (2020), https://arxiv.org/abs/2007.12018.
- Stephen McKean, *Rational lines on smooth cubic surfaces*, arXiv:2101.08217 (2021), https://arxiv.org/abs/2101.08217.
