# Sharp three-transverse-line Bertini bound for plane quartics over \(\mathbf F_3\)

## Finding

Let \(C\subset\mathbf P^2_{\mathbf F_3}\) be any geometrically smooth plane quartic. A rational line is **transverse** to \(C\) when its intersection scheme with \(C\) consists of four distinct geometric points; let \(t(C)\) be the number of such lines among the thirteen \(\mathbf F_3\)-rational lines. Then
\[
\boxed{t(C)\ge 3.}
\]
Equality holds for **exactly 624 projectively normalized quartic equations**, split into exactly **two \(\operatorname{PGL}_3(\mathbf F_3)\)-orbits**, each of size 312 and stabilizer order 18. Equivalently, exactly two \(\mathbf F_3\)-isomorphism classes of smooth plane quartics attain equality. Representatives are
\[
C_A:\quad X^4+2X^3Z+2X^2Y^2+XZ^3+Y^4=0,
\]
\[
C_B:\quad X^3Y+2X^3Z+2X^2Y^2+2XY^3+XZ^3+Y^4=0.
\]
Each representative has precisely three rational transverse lines, namely \(Y=0\), \(X+Y=0\), and \(X+2Y=0\). For \(C_A\), all three intersections have Frobenius splitting type \((1,3)\) and \(\#C_A(\mathbf F_3)=1\). For \(C_B\), they split as \((1,1,1,1)\) and \(\#C_B(\mathbf F_3)=10\). In each case the three transverse lines concur at \([0:0:1]\), which lies on the curve.

## Assumptions and scope

The base field is precisely \(\mathbf F_3\); all 15 coefficients of a homogeneous ternary quartic are allowed. Equations are identified up to a nonzero scalar by normalizing their first nonzero coefficient to 1 in the lexicographically decreasing monomial order
\[
(X^4,X^3Y,X^3Z,X^2Y^2,X^2YZ,X^2Z^2,XY^3,XY^2Z,XYZ^2,XZ^3,Y^4,Y^3Z,Y^2Z^2,YZ^3,Z^4).
\]
There are \((3^{15}-1)/2=7,174,453\) normalized equations. The term *smooth* always means geometrically smooth, not merely smooth at rational points. A projective orbit is taken under source-coordinate changes over \(\mathbf F_3\). For geometrically smooth plane quartics the canonical embedding is the displayed plane embedding, so projective equivalence agrees with \(\mathbf F_3\)-isomorphism of the curves. We make no claim about conjugacy over the algebraic closure or full spectra for larger fields.

## Proof

**Exact test for transverse lines.** Enumerate the thirteen normalized nonzero triples \((a,b,c)\in\mathbf F_3^3\) defining rational lines \(aX+bY+cZ=0\). Choose any basis \(U,V\) of each line and restrict a homogeneous quartic \(F\) to a binary quartic \(B(u,v)=F(uU+vV)\). The intersection is transverse if and only if \(B\) is squarefree over the algebraic closure. Writing \(B=\sum_{j=0}^4 b_j u^{4-j}v^j\), this is exactly the conjunction that \(B\ne0\), the smallest index with \(b_j\ne0\) is 0 or 1 (no multiple root at infinity), and the univariate polynomial \(B(t,1)\) is coprime to its derivative over \(\mathbf F_3\). This handles geometric roots of every extension degree, including nonrational tangencies.

**Complete finite enumeration.** The accompanying code enumerates every projectively normalized vector of fifteen ternary coefficients. For each line, a tabulated \(\mathbf F_3\)-linear restriction maps the coefficient vector to the five coefficients of its binary restriction; the squarefree test classifies it. The complete all-forms histogram for numbers of transverse lines \(0,1,2,3\) is respectively \(5395,15795,50544,172146\). The programs also exhaust the remaining strata, documented in `out/qhist.txt`.

**Reduction to ninety-two symmetry representatives.** Five explicit invertible ternary coordinate transformations (two coordinate swaps, one scaling by 2, and two elementary shears) generate all \(\operatorname{GL}_3(\mathbf F_3)\) (order 11232), as checked by an independent group closure enumeration. Their projective action on quartic coefficient vectors has order 5616. The exhaustive low-transversality enumerator partitions every normalized equation with \(t\le3\) into exactly 92 projective orbits: 14 with zero, 8 with one, 21 with two, and 49 with three transverse rational lines. The orbit sizes in `out/plane_qorbits.txt` sum to the full \(t\le3\) histogram. The generators preserve transversality because they permute rational lines and preserve geometric intersection multiplicities.

**Geometric smoothness on orbit representatives.** For each of these 92 orbit representatives, `tools/check_groebner.py` checks all three affine charts. On a chart, it computes a Gröbner basis over \(\mathbf F_3\) for the chart equation and its two partial derivatives; the ideal is the unit ideal exactly when the chart contains no singularity over the algebraic closure. This is an exact algebraic-closure test, not a finite point search. Precisely two representatives survive: coefficient codes 78805 and 80265, both with \(t=3\) and orbit size 312. The other 90 orbit representatives, including *all* representatives with \(t<3\), are geometrically singular. Thus every geometrically smooth quartic has at least three transverse rational lines, and precisely 624 normalized smooth quartics attain equality.

**Distinct extremal isomorphism types.** Decoding those codes gives the two displayed equations. A separate symbolic implementation recomputes the line restrictions directly (without using the C++ restriction table) for all 92 representatives and verifies that precisely the three listed lines are transverse for each extremizer. On these lines, \(C_A\) has an irreducible cubic and a linear component in the intersection, while \(C_B\) has four distinct rational intersection points. Direct enumeration of \(\mathbf P^2(\mathbf F_3)\) finds respectively one and ten rational points, proving that the two projective orbits cannot be isomorphic as curves. Since the canonical series of a smooth plane quartic is cut out by lines, the two projective orbits are exactly two arithmetic curve-isomorphism classes.

## Verification

All reproducibility files are embedded independently and use only Python 3 with SymPy and a C++17 compiler. From the package root, run:

```
python tools/generate_tables.py
python tools/generate_transform.py
python tools/check_tables.py
python tools/check_group.py
g++ -O3 -std=c++17 tools/plane_quartic_census.cpp -o census
./census > out/qhist.txt
g++ -O3 -std=c++17 tools/plane_quartic_orbits.cpp -o orbits
./orbits > out/plane_qorbits.txt
python tools/check_groebner.py > out/qorbit_smooth.txt
python tools/independent_lines.py > out/independent_lines.txt
```

The packaged execution independently regenerated every lookup value, all 92 low-transversality orbits, all 92 smoothness verdicts, the 624 equality equations and both rational-point counts. `out/check_tables.txt`, `out/check_group.txt`, `out/plane_qorbits.txt`, `out/qorbit_smooth.txt`, and `out/independent_lines.txt` provide the actual outputs. The exact integer coefficient coding is specified above; the code, not an external table, performs the exhaustive enumeration. Scripts are finite deterministic calculations, and the mathematical reduction shows why their checked parameter space exhausts the stated domain.

## Relationship to prior work

Asgarli, *Sharp Bertini theorem for plane curves over finite fields* (first posted 2018-04-04, Theorem 1.2 and Corollary 2.2), guarantees at least one transverse rational line for a smooth quartic over \(\mathbf F_3\). It does not provide the sharp number three or classify equality. Asgarli–Freidin, *On the proportion of transverse-free plane curves* (2020), concerns asymptotic proportions for increasing degree, not the exact degree-four census. Makhul–Schicho–Gallet study limiting incidence probabilities in finite-field extensions; their asymptotic results do not yield this finite-field sharp extremal orbit classification. Prior fixed-field studies of rational flexes and bitangents concern tangent-contact invariants, not the number of complementary transverse lines. These differences are comparison of mathematical conclusions, not merely titles or parameter names.

## Limitations

This is a finite-field classification at the single natural Bertini boundary \(d=q+1=4\) for \(q=3\). It does not imply a uniform bound of three for all \(q\), characterize all high-transversality strata by smoothness, or assert worldwide publication priority. The two extremal models have independent rational point counts, but their further geometric invariants are not classified here. Results rely on an exhaustive C++ enumeration with its full tables independently regenerated and all decisive orbit representatives algebraically checked; no externally certified formal proof or independent human audit has been performed.

## References

1. S. Asgarli, *Sharp Bertini theorem for plane curves over finite fields*, arXiv:1804.01569v1, 2018-04-04, Theorem 1.2 and Corollary 2.2. https://arxiv.org/abs/1804.01569
2. S. Asgarli and B. Freidin, *On the proportion of transverse-free plane curves*, arXiv:2009.13421v1, 2020-09-28, Sections 1–2. https://arxiv.org/abs/2009.13421
3. M. Makhul, J. Schicho, and M. Gallet, *Probabilities of incidence between lines and a plane curve over finite fields*, arXiv:1711.06021v1, 2017-11, incidence-limit theorems. https://arxiv.org/abs/1711.06021
