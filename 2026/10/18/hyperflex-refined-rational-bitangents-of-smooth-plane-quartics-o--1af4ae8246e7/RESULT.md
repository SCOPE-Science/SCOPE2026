# Hyperflex-refined rational bitangents of smooth plane quartics over \(\mathbf F_3\)

## Finding

Let \(k=\mathbf F_3\), and let \(F\) range over nonzero homogeneous ternary quartic equations modulo nonzero scalar. Require that \(C_F\subset\mathbf P^2_k\) be geometrically smooth. A rational line \(L\) is called a **proper rational bitangent** when the geometric intersection divisor is \(2P+2Q\) for distinct geometric points, and a **rational hyperflex line** when it is \(4P\). The contacts need not themselves be rational. Write \(r(F)\) and \(h(F)\) for the respective numbers of such lines defined over \(k\).

The complete joint spectrum among all smooth normalized quartic equations is:

| Proper \(r\) | Hyperflex \(h\) | Equations | \(\operatorname{PGL}_3(\mathbf F_3)\)-orbits |
|---:|---:|---:|---:|
| 0 | 0 | 1,123,200 | 208 |
| 0 | 1 | 689,520 | 142 |
| 0 | 2 | 81,432 | 19 |
| 0 | 4 | 2,340 | 3 |
| 1 | 0 | 1,426,464 | 270 |
| 1 | 1 | 308,880 | 60 |
| 1 | 2 | 44,928 | 8 |
| 1 | 3 | 2,808 | 1 |
| 2 | 0 | 287,820 | 62 |
| 2 | 1 | 44,928 | 8 |
| 2 | 2 | 5,616 | 2 |
| 3 | 0 | 44,928 | 8 |
| 3 | 1 | 22,464 | 8 |
| 4 | 0 | 4,212 | 2 |
| 4 | 2 | 8,424 | 2 |
| 6 | 0 | 1,404 | 1 |
| 9 | 1 | 312 | 1 |
| **All** | | **4,099,680** | **805** |

In particular \(r+h\le 10\), with equality for exactly \(312\) smooth quartic equations, constituting **one** projective equivalence class (stabilizer order \(18\)). Every maximizer has \((r,h)=(9,1)\) and exactly one rational point. One representative is
\[
F=X^4+2X^3Z+2X^2Y^2+XZ^3+Y^4.
\]
Its unique rational point is \([0:0:1]\); the hyperflex is \(X=0\), and the nine proper bitangent lines have normalized dual coefficients
\[
(0,0,1),\ (0,1,1),\ (0,1,2),\ (1,0,1),\ (1,0,2),\ (1,1,1),\ (1,1,2),\ (1,2,1),\ (1,2,2).
\]
The other three rational lines are \(Y=0\), \(X+Y=0\), and \(X+2Y=0\).

The substantive new refinement is the distribution **by geometric contact type** and the unique maximizer orbit. The unrefined count \(r+h\) alone is not asserted to be new: it can be approached through prior Frobenius-class counts of del Pezzo surfaces.

## Assumptions and scope

All arithmetic is over \(k=\mathbf F_3\). Forms are counted once up to \(k^\times\), which has order two; different polynomials defining the same projective curve are counted as one. A projective equivalence class refers to the full \(\operatorname{PGL}_3(k)\) action on these normalized forms. Geometric smoothness and contact multiplicity are assessed over an algebraic closure. There are thirteen rational points and thirteen rational lines in the plane. There is no claim about arbitrary \(\mathbf F_{3^m}\) or other fields.

The fifteen monomials are ordered \(X^iY^jZ^{4-i-j}\) in decreasing \(i\) and, at fixed \(i\), decreasing \(j\). A normalized form is encoded as the fifteen least-significant-first ternary digits of an integer, with the first nonzero digit equal to one. This convention gives \((3^{15}-1)/2=7,174,453\) projective equations. The example above has code `78805`.

## Proof

**Exact contact criterion.** Restrict \(F\) to a rational line parameterized by \([u:v]\). Its binary quartic \(f_L(u,v)\) has two double geometric roots or one quadruple root exactly when \(f_L\) is a nonzero scalar multiple of the square of a binary quadratic defined over \(k\). Indeed, the effective intersection divisor is \(k\)-rational and even, so its unique half divisor is Galois invariant; on \(\mathbf P^1\) a rational effective degree-two divisor is cut out by a binary quadratic over \(k\). A quadratic \(au^2+buv+cv^2\) has two distinct geometric roots exactly when \(b^2-ac\ne0\) (since \(4=1\) in characteristic three). There are nine projective squarefree quadratics and four repeated-root ones over \(k\); their squared restrictions classify \(r\) and \(h\) without finite-extension approximation.

**Exact smoothness criterion.** Let \(S_d=k[X,Y,Z]_d\). The partial derivatives of \(F\) are ternary cubics. Because the degree four is invertible modulo three, Euler's formula makes common projective zeros of \((F_X,F_Y,F_Z)\) equivalent to singularities of \(C_F\). Thus \(C_F\) is geometrically smooth exactly when these three cubics have no common projective zero. Such homogeneous cubics are then a regular sequence, whose quotient has Hilbert series \((1+t+t^2)^3\), with its last nonzero graded piece in degree six. It follows equivalently that the \(k\)-linear map
\[
S_4^{\oplus3}\longrightarrow S_7,\qquad (A,B,C)\longmapsto AF_X+BF_Y+CF_Z
\]
has rank \(\dim_k S_7=36\). Conversely, if the partial derivatives share a projective zero over the algebraic closure, evaluation at that point gives a nonzero functional on the degree-seven quotient, so the rank is below \(36\). Rank is invariant under field extension, proving the criterion over the algebraic closure.

**Exhaustive projective enumeration.** The finite coordinate group \(\operatorname{PGL}_3(k)\) has order \(5616\). A transvection, two coordinate swaps, and a diagonal scaling generate this group. For each normalized quartic not previously reached, the supplied `census.cpp` explores the entire orbit under those generators and marks every visited form. This partitions all \(7,174,453\) forms into exactly \(1557\) orbits, with summed orbit sizes equal to that full coefficient count. One representative per orbit is tested by the exact rank criterion, and its thirteen rational line restrictions are compared with the nine proper and four hyperflex quadratic-square patterns. Orbit sizes give the joint multiplicities above. The rank test selects \(805\) smooth orbits of total size \(4,099,680\); the sole \((9,1)\) orbit has size \(312\).

**Extremal orbit and incidence.** Independent substitution into the thirteen rational line equations gives the ten contact lines listed above; exact point evaluation gives the sole rational point. Because all \(312\) maximizers lie in one orbit, this describes every maximum case, and its projective stabilizer has size \(5616/312=18\).

## Verification

The self-contained coefficient generator `make_tables.py` produces the finite-field action, line restrictions, and gradient matrices as `tables.hpp`. Compile `census.cpp` as ISO C++17; its stdout `results.txt` contains all seventeen joint bins and orbit counts; `orbits.csv` gives an auditable representative, orbit size, smoothness flag, contact-type counts and point count for **all 1557** projective orbits. Rebuilding from source reproduces these outputs exactly.

A separate `independent_groebner.py` verifies geometric smoothness for each of the 1557 orbit representatives using Gröbner bases in all three affine charts, rather than the gradient multiplication rank. The separate `verify_independent.py` independently constructs the rational projective geometry, checks order \(5616\) by a permutation-group computation and verifies the thirteen-line contact classifications for each of the 805 smooth representatives with independently generated binary restriction polynomials. All programs were executed successfully against the embedded `orbits.csv`.

The computation is exhaustive **because every normalized equation is assigned to a generated projective orbit** and each orbit is checked; this is not a claim based on random samples or a bounded search for counterexamples. Instructions and deterministic expected hashes are provided in `REPRODUCE.md`.

## Relationship to prior work

Classical theory gives twenty-eight geometric bitangents, corresponding to odd theta characteristics. Bergvall (2022, Theorem 4.1/Table 1) counts degree-two del Pezzo surfaces by Frobenius classes over all odd finite fields; these classes govern the Galois action on the 28 bitangents and provide strong prior coverage of the **unrefined** rational-bitangent counts. Bergvall (2023, §2.2 and Corollary 4.6) defines proper bitangents versus hyperflexes and counts various marked-moduli spaces over odd finite fields. The current joint \((r,h)\) table depends on the actual divisor of contact and is not supplied by those Frobenius permutation counts. Its unique extremal orbit and complete contact configuration are also separate assertions. Markwig–Payne–Shaw (2022) address tropical bitangent rationality over valued fields; Costa–Harvey–Sutherland (2022) address rational point counts of quartics. Neither supplies the hyperflex-refined finite census. Full primary comparisons appear in `AUDIT.json` and `REVIEW.md`.

## Limitations

The statement is confined to \(\mathbf F_3\) plane quartics and to equivalence under its rational projective coordinate group. All enumerative certificates are finite executable computations, not formal proofs in a proof assistant; they need a working C++17 compiler and, for independent cross-checks, Python with SymPy. The underlying group and rank tests admit direct mathematical verification. A previously unpublished or unindexed hyperflex refinement or projective orbit classification could duplicate the result. No claim is made that the unrefined bitangent count distribution is historically new; the strongest related prior work may already imply it.

## References

1. O. Bergvall, *Frobenius actions on Del Pezzo surfaces of degree 2*, arXiv:2211.12855 (first public 2022-11-23), Theorem 4.1 and Table 1. https://arxiv.org/abs/2211.12855
2. O. Bergvall, *Arithmetic and topology of classical structures associated with plane quartics*, European Journal of Mathematics 9 (2023), article 117, DOI:10.1007/s40879-023-00711-3, §§2.2 and 4. https://doi.org/10.1007/s40879-023-00711-3
3. H. Markwig, S. Payne, K. Shaw, *Bitangents to plane quartics via tropical geometry: rationality, A1-enumeration, and real signed count*, arXiv:2207.01305 (first public 2022-07-04). https://arxiv.org/abs/2207.01305
4. E. Costa, D. Harvey, A. Sutherland, *Counting points on smooth plane quartics*, arXiv:2208.09890 (2022). https://arxiv.org/abs/2208.09890
