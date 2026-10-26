# Rational-bitangent frequency distribution for smooth plane quartics over \(\mathbf F_2\)

## Finding
Let \(V\) be the vector space of ternary homogeneous forms of degree four over \(\mathbf F_2\). For a nonzero \(F\in V\), assume that \(C_F=V(F)\subset\mathbf P^2_{\mathbf F_2}\) is geometrically smooth. Write \(b(F)\) for the number of \(\mathbf F_2\)-rational projective lines \(L\) for which the scheme-theoretic divisor \(C_F\cap L\) equals \(2D\) for an effective divisor \(D\) of degree two. Hyperflex lines are included.

Among all \(10,920\) forms defining geometrically smooth quartics, the exact distribution, counted by **equations in fixed projective coordinates**, is

| \(b(F)\) | Number of forms |
|---:|---:|
| 0 | 3,072 |
| 1 | 5,278 |
| 2 | 2,352 |
| 3 | 105 |
| 4 | 112 |
| 7 | 1 |
| **Total** | **10,920** |

Hence \(7,848\) of these forms admit at least one rational bitangent. The absence of five or six rational bitangents and the existence of one seven-bitangent form are **not claimed as new**: they relate to established characteristic-two bitangent geometry and earlier finite-field classifications. The finding is the full, exact, equation-weighted arithmetic frequency distribution.

## Assumptions and scope
All forms and lines are over \(\mathbf F_2\). A form is counted once as a coefficient vector in \(\mathbf F_2^{15}\setminus\{0\}\); since the multiplicative group of \(\mathbf F_2\) is trivial, this is also the collection of scalar-normalized equations. Two forms related by \(\operatorname{PGL}_3(\mathbf F_2)\) are counted separately in the main table. Smoothness is geometric, tested over the algebraic closure, not just at seven rational points. The divisor criterion is tested over the algebraic closure and includes all multiplicity-two/two or multiplicity-four intersections.

## Proof
Enumerate the \(15\) degree-four exponent triples in the order \((a,b,4-a-b)\), with \(a=0,\ldots,4\) and \(b=0,\ldots,4-a\). Encode \(F\) by a nonzero integer mask of length \(15\). The \(168\)-element group \(G=\operatorname{GL}_3(\mathbf F_2)=\operatorname{PGL}_3(\mathbf F_2)\) acts by invertible linear substitution; coefficient multiplication uses exact arithmetic modulo two.

The first program generates the group action using three elementary substitutions and partitions all \(2^{15}-1=32,767\) nonzero forms into \(279\) disjoint orbits. Each orbit representative is checked for smoothness by computing, for each affine chart \(X=1\), \(Y=1\), and \(Z=1\), the Gröbner basis over \(\mathbf F_2\) of the dehomogenized ideal
\[
(F,\partial_XF,\partial_YF,\partial_ZF).
\]
The ideal contains \(1\) exactly when it has no zeros over the algebraic closure. Thus geometric smoothness is decided exhaustively across the three charts. Exactly \(78\) smooth orbits occur, and their orbit sizes sum to \(10,920\).

For each of the seven rational lines \(L\) choose a basis \(u,v\) of its rational vector kernel. The restriction has the form
\[
F|_L=A u^4+B u^3v+C u^2v^2+Duv^3+E v^4.
\]
Since \(\mathbf F_2\) is perfect, \(F|_L\) is the square of a binary quadratic if and only if \(B=D=0\). For a smooth quartic the restriction is nonzero: a smooth plane quartic cannot contain a line, by geometric irreducibility and Bézout. Therefore the square criterion is precisely the stated bitangent divisor condition. Its truth is independent of the chosen basis. For each representative evaluate all seven restrictions. Both geometric smoothness and this count are invariant under \(G\). Summing the sizes of the \(78\) smooth orbits by their bitangent count gives exactly the six table rows.

A second implementation enumerates **all** \(168\) invertible binary matrices independently of the first program's generators, reconstructs each of the \(279\) orbits from its representative, checks disjointness and total size \(32,767\), recomputes geometric smoothness for all representatives using a second monomial representation and Gröbner order, and checks the bitangent count on every one of the \(10,920\) smooth coefficient vectors using direct binary quartic restriction. It reproduces the table exactly. Thus the finite exhaustive proof does not infer smoothness from merely rational-point tests, nor infer exhaustive coverage from a partial sample.

## Verification
Run `python3 census.py` in the package directory with Python 3 and SymPy, then run `python3 crosscheck.py`. Both exit successfully and the second prints `CROSSCHECK_OK`. The primary program writes `all_orbits.csv` (all \(279\) representatives, orbit sizes, smoothness, bitangents and rational point counts) and `smooth_orbits.csv` (all \(78\) smooth representatives). Exact recorded outputs are `census_output.txt` and `crosscheck_output.txt`. The programs take less than a few minutes on an ordinary machine; actual timing depends on the environment. The second program checks all \(10,920\) smooth forms and verifies that the seven-line statistic is constant on their group orbits. These artifacts form a standalone finite exhaustive certificate.

## Relationship to prior work
Nart and Ritzenthaler classified the isomorphism classes of all smooth characteristic-two plane quartics over finite fields, including the action of Frobenius on bitangents and automorphism groups (arXiv:math/0312366, Sections 1--3, Theorem 3.1). Their earlier classification is substantially stronger in the sense of classifying objects; it provides a second theoretical route to the statistic after additional orbit weighting. It does **not explicitly state the coefficient-equation frequency table above**, which is the limited arithmetic output asserted here. The characteristic-two geometric bitangent cardinalities and normal forms were classical and are summarized in Dolgachev--Kondō, Proposition 5.8 (arXiv:2406.16246). The special all-seven-line case has also been classified elsewhere and is not independently claimed. These results explain the admissible geometric bitangent strata but do not themselves tabulate the six numerical frequencies among fixed-coordinate equations over \(\mathbf F_2\).

## Limitations
This is a complete finite-field, fixed-degree computation, not an asymptotic or arbitrary-field theorem. The distribution weights coordinate equations rather than geometric or arithmetic isomorphism classes. The literature's existing complete classification could, in principle, imply the displayed numbers after applying stabilizer weights, so publication priority for the exact table warrants further independent examination. A missing numerical table in searched sources is not a proof of global novelty. All smoothness and counting checks are same-package finite symbolic computations; no external independent audit is claimed.

## References
- E. Nart and C. Ritzenthaler, *Non-hyperelliptic curves of genus three over finite fields of characteristic two*, arXiv:math/0312366 (first submitted 2003-12-18), especially Sections 1--3 and Theorem 3.1; https://arxiv.org/abs/math/0312366.
- I. Dolgachev and S. Kondō, *Bitangent surfaces and involutions of quartic surfaces*, arXiv:2406.16246 (first submitted 2024-06-24), especially Proposition 5.8 in the publicly available later revision; https://arxiv.org/abs/2406.16246.
- C. T. C. Wall, *Quartic curves in characteristic 2* (1995), geometric classification cited by the preceding papers.
