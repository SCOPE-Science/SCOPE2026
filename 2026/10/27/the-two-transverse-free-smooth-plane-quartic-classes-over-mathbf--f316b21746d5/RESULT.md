# The two transverse-free smooth plane-quartic classes over \(\mathbf F_2\)

## Finding
A geometrically smooth plane quartic over \(\mathbf F_2\) has no transverse \(\mathbf F_2\)-rational line if and only if it belongs to one of exactly two projective equivalence classes. There are exactly **25 equations** in fixed coordinates: 24 equations in one orbit of \(\operatorname{PGL}_3(\mathbf F_2)\) and one invariant equation in a singleton orbit.

The 24-member orbit consists precisely of the geometrically smooth quartics containing all seven rational points of the plane. A representative is
\[
F_{\rm fill}=X^3Z+X^2Y^2+XY^3+XZ^3+Y^2Z^2+YZ^3.
\]
The singleton orbit has no rational curve points. Its equation is
\[
F_{\rm inv}=X^4+Y^4+Z^4+X^2Y^2+X^2Z^2+Y^2Z^2+X^2YZ+XY^2Z+XYZ^2.
\]
Its full ambient projective stabilizer has order 168; the filling representative's stabilizer has order seven. Thus transverse-free smooth binary plane quartics display an extreme rational-point dichotomy: their rational point count is either zero or seven, with no intermediate count. The reverse assertion does **not** hold for every pointless quartic; only the indicated singleton is exceptional. Each curve has geometric genus three.

For the singleton curve, every rational line cuts out twice the same nonsplit quadratic divisor after choosing any rational basis of that line; in such coordinates the restriction is
\[
U^4+U^2V^2+V^4=(U^2+UV+V^2)^2.
\]
For the filling class, every rational line has three distinct rational curve points and necessarily a repeated fourth intersection at one of them. These are two different geometric mechanisms for failure of finite-field Bertini transversality at the sharp degree \(q+2=4\).

## Assumptions and scope
Work over \(k=\mathbf F_2\). Quartic equations are nonzero homogeneous degree-four ternary polynomials, and multiplication by a nonzero scalar does not create a second equation because \(k^\times=\{1\}\). A rational line \(L\) is **transverse** to a geometrically smooth curve \(C\) if its scheme-theoretic intersection is geometrically reduced of degree four, equivalently its restricted binary quartic is squarefree over \(\overline{k}\). **Transverse-free** means that none of the seven rational lines is transverse. Geometrically smooth means nonsingular over the algebraic closure, not merely at the seven rational points. Projective equivalence means changes of ambient coordinates by \(\operatorname{PGL}_3(k)\); no claim is made about abstract isomorphisms.

## Proof
Enumerate the 15 monomials \(X^iY^jZ^{4-i-j}\), ordered by \(i=0,\ldots,4\), then \(j=0,\ldots,4-i\). A nonzero coefficient vector corresponds uniquely to an integer mask from 1 through 32767. This exhausts the complete parameter space, not a sample. Rational points and lines of the Fano plane are the seven nonzero binary triples; for a line given by a normal triple, choose any two of its three nonzero kernel vectors as basis.

On such a basis, write the restriction as
\[
aU^4+bU^3V+cU^2V^2+dUV^3+eV^4.
\]
The restriction is geometrically squarefree precisely when its dehomogenization has degree at least three and is coprime to its formal derivative. Direct arithmetic over \(\mathbf F_2\) gives the following equivalent finite test: either \(b=0,d=1,a=1\); or \(b=1,d=0,e=1\); or \(b=d=1,a+c+e=1\). This includes the point at infinity: a binary quartic whose dehomogenization has degree at most two has a multiple root at infinity. All seven rational-line restrictions are computed exactly from coefficients, using ordinary polynomial substitution modulo two.

Checking the 32767 nonzero masks gives **2559** equations for which none of the seven rational lines is transverse. Now impose the necessary rational smoothness condition
\[
F(P)=0\ \Longrightarrow\ (F_X(P),F_Y(P),F_Z(P))\ne(0,0,0)
\]
for each of the seven rational points. Exactly **25** of the 2559 survive. Their complete coefficient masks are

`6438, 6636, 6922, 7110, 7530, 7596, 8006, 8070, 9004, 9190, 10086, 10154, 10794, 10988, 11884, 11948, 13062, 13258, 13676, 13734, 14380, 14570, 15946, 16010, 20181`.

Direct evaluation of the seven rational points shows that the first 24 masks have all seven rational points on their curves, while the last mask has none. All 168 invertible three-by-three matrices over \(\mathbf F_2\) act on the quartic coefficient space by substitution. Exact orbit enumeration gives precisely the two orbits, represented by masks 6438 and 20181, of sizes 24 and one. These cover all 25 candidates; their stabilizer orders are therefore seven and 168. No unexamined orbit or zero coefficient vector is involved.

It remains to prove geometric smoothness rather than assume it from the rational test. For each representative \(F\), on each affine chart \(X=1\), \(Y=1\), and \(Z=1\), exact Gröbner-basis computations over \(\mathbf F_2\) give the unit ideal for the simultaneous equations \(F=F_X=F_Y=F_Z=0\). Thus both representative curves are smooth over the algebraic closure. Projective coordinate changes preserve geometric smoothness, so all 25 candidates are smooth. Conversely, any geometrically smooth transverse-free quartic was among the 25 rationally smooth candidates. This proves exhaustiveness and the classification.

For the singleton, substituting each of the seven line bases gives the identical binary coefficient mask 21, namely \(U^4+U^2V^2+V^4\). The nonsplit quadratic has two conjugate geometric roots, each of intersection multiplicity two. For the filling orbit, all three rational points on each line belong to the curve; a degree-four Frobenius-invariant intersection divisor with these three distinct points must repeat one of them, proving nontransversality without relying on the restriction calculation.

## Verification
Run `python classify.py` using Python 3 to reconstruct all 32767 coefficient masks, the seven line restrictions, rational smoothness, both complete projective orbits and the coefficient certificate `classification.json`. The program asserts the count 25, point-count split, matrix-group size 168 and orbit sizes one and 24. Its recorded raw transverse-free total is 2559.

Run `python secondary_scan.py` for a separately implemented direct-binomial expansion and rational-Jacobian scan of all 32767 forms; it must reproduce exactly the 25 masks. Run `python verify.py` with SymPy installed for independently constructed seven line restrictions and all 75 affine-chart Jacobian/F unit-ideal tests (25 equations times three charts). The reference outputs are `secondary_output.txt` and `verification_output.txt`. The latter lists both polynomial representatives. No finite extension-point scan is used to infer geometric smoothness.

## Relationship to prior work
Asgarli–Freidin, *On the proportion of transverse-free plane curves* (first posted 2020-09-28, arXiv:2009.13421), investigates transverse-free smooth plane curves primarily in the large-degree density regime, defines the condition via the dual plane, and does not in its inspected relevant sections present this degree-four binary orbit census. Asgarli, *Sharp Bertini theorem for plane curves over finite fields* (first posted 2018-04-04, arXiv:1804.01569), gives the sharp degree \(q+2\) filling-curve examples but not the exceptional pointless orbit or the two-class exhaustiveness statement.

The historical quartic classifications of Dickson (1915, *Quartic curves modulo 2*, DOI 10.2307/1988711, and related classification articles) are a **substantive prior-coverage risk**: these classify many binary quartics by rational-point and bitangent data, and may encode the present conclusion in tables. The publicly accessible descriptive record was checked, but full-text comparison was unavailable; the classification above is not asserted to supersede those historical results. The 24 smooth filling forms and the exceptional seven-bitangent curve are known separately. The assessed distinction here is the explicit exhaustive equivalence between transverse-freeness and the union of precisely those two arithmetic projective classes, excluding every intermediate rational-point stratum.

## Limitations
The theorem applies only to geometrically smooth plane quartics over \(\mathbf F_2\), and to transversality with **rational lines**. It is not an assertion about all point-free quartics, higher degrees, or other fields. The classification is projective, not an abstract moduli statement. The finite certificate establishes mathematical exhaustiveness when its fully specified tests are replayed; no independent external audit or publication-priority certification is claimed. Earlier extensive classifications of binary quartics may already imply the dichotomy, a risk requiring further historical full-text comparison.

## References
- S. Asgarli and B. Freidin, *On the proportion of transverse-free plane curves*, arXiv:2009.13421 (first public version 2020-09-28).
- S. Asgarli, *Sharp Bertini theorem for plane curves over finite fields*, arXiv:1804.01569 (first public version 2018-04-04).
- L. E. Dickson, *Quartic curves modulo 2*, Trans. Amer. Math. Soc. **16** (1915), 111–120, DOI:10.2307/1988711.
