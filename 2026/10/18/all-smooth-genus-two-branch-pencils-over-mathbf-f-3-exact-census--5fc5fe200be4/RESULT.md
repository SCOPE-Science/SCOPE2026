# All-smooth genus-two branch pencils over \(\mathbf F_3\): exact census and 440 symmetry types

## Finding
Let \(V=H^0(\mathbf P^1_{\mathbf F_3},\mathcal O(6))\). A *pencil* is a two-dimensional \(\mathbf F_3\)-subspace \(W\subset V\), with its four projective members \(\mathbf P(W)(\mathbf F_3)\). Say that it is *all-smooth* when the zero scheme on \(\mathbf P^1_{\overline{\mathbf F}_3}\) of every one of these four binary sextics is reduced of degree six. Equivalently, each corresponding quadratic double cover of \(\mathbf P^1\) is a smooth genus-two curve (the quadratic-twist choice for its equation is not part of the classification).

**Exact census.** Of the \(99{,}463\) pencils in \(\mathbf P(V)\), exactly \(10{,}005\) are all-smooth. Under the natural change-of-variable action of \(\operatorname{PGL}_2(\mathbf F_3)\), these form exactly \(440\) orbits, whose sizes are:

| Orbit size | Number of orbits |
| ---: | ---: |
| 3 | 1 |
| 6 | 1 |
| 12 | 43 |
| 24 | 395 |

If \(B(W)\) is the greatest common reduced zero divisor of the four sextics over the algebraic closure, its degree has the exact distribution:

| \(\deg B(W)\) | Number of pencils |
| ---: | ---: |
| 0 | 9,612 |
| 2 | 195 |
| 3 | 72 |
| 4 | 54 |
| 5 | 72 |

In particular, precisely \(9{,}612\) pencils are base-point-free; each defines a degree-six map \(\mathbf P^1\to\mathbf P^1\) whose four rational target fibres are geometrically reduced.

For a pencil, let the four rational-root counts of its members on \(\mathbf P^1(\mathbf F_3)\), sorted in nondecreasing order, be \(\rho(W)\). The complete distribution is:

| \(\rho(W)\) | Pencils |
| --- | ---: |
| \((0,0,0,4)\) | 183 |
| \((0,0,1,3)\) | 1,944 |
| \((0,0,2,2)\) | 1,134 |
| \((0,1,1,2)\) | 5,592 |
| \((1,1,1,1)\) | 1,152 |

The accompanying `orbit_catalogue.json` gives an explicit coefficient-pair representative, its orbit size, its common-divisor degree and its rational-root profile for every one of the 440 symmetry types.

## Assumptions and scope
The field is exactly \(\mathbf F_3\). Coefficient vectors are written \((c_0,\ldots,c_6)\) for the homogeneous sextic
\[
F(X,Z)=\sum_{i=0}^{6}c_i X^iZ^{6-i}.
\]
All counts are of actual two-dimensional subspaces of this seven-dimensional vector space, not ordered bases, and not isomorphism classes of the resulting genus-two curves. In particular \([F]\) and \([2F]\) are identified as projective branch divisors; their associated quadratic twists need not be identified as curves over \(\mathbf F_3\). Only source-coordinate substitutions \(\operatorname{PGL}_2(\mathbf F_3)\) act in the stated orbit classification; the change of pencil basis is already factored out by regarding a pencil as a subspace.

## Proof
A nonzero form admits a unique representative whose *last nonzero* coefficient in \((c_0,\ldots,c_6)\) is one. This produces \((3^7-1)/2=1093\) projective sextics. Write \(f(T)=F(T,1)\), and let \(d=\deg f\). The divisor \(F=0\) is geometrically reduced of degree six if and only if \(d\ge5\) and \(\gcd(f,f')=1\) in \(\mathbf F_3[T]\): if \(d=5\), the additional zero at infinity is simple; if \(d\le4\), it is multiple. The Euclidean algorithm is exact, even when \(f'=0\). Applying the criterion gives precisely \(648\) reduced projective sextics.

Every projective pencil has exactly four members \([F],[G],[F+G],[F-G]\). Two-dimensional subspaces admit unique reduced-row-echelon bases. Enumerating the echelon pivot pairs in seven columns, with arbitrary entries only in their allowed free positions, gives
\[
\genfrac{[}{]}{0pt}{}{7}{2}_{3}=
\frac{(3^7-1)(3^7-3)}{(3^2-1)(3^2-3)}=99{,}463
\]
subspaces. For each, the four explicitly constructed projective forms are tested by the preceding polynomial-gcd criterion. Exactly \(10{,}005\) pass. This is a finite exhaustive proof because the echelon parameterization is bijective and the gcd criterion is necessary and sufficient for geometric reduction.

The group \(\operatorname{PGL}_2(\mathbf F_3)\) has order \(24\) and acts by substitutions \((X,Z)\mapsto(aX+bZ,cX+dZ)\), with determinant nonzero. All 24 projective matrices are enumerated. Their permutations of the 1093 normalized vectors give a complete orbit partition of the 10,005 passing pencils. The resulting orbit sizes are \(3,6,12,24\), with multiplicities \(1,1,43,395\), respectively; the weighted sum is \(10{,}005\). The published catalogue records one normalized representative pair per orbit, so this is an explicit classification of the complete finite set.

For two normalized basis forms, the degree of the greatest common homogeneous factor is
\[
6-\max(\deg f,\deg g)+\deg\gcd(f,g),
\]
where the first term accounts for a possible common zero at infinity. The enumerated degrees yield the second table. Since every member is reduced, the common divisor is reduced as well. A common rational root is impossible: on a two-dimensional pencil, the linear functional imposing derivative zero at such a root has a nonzero kernel, producing a member with a repeated root. Thus the common degree cannot be one, and every rational point of the source occurs as a simple zero of exactly one of the four members. This proves \(\sum\rho(W)=4\); direct evaluation at the four source points computes the displayed five-profile distribution.

For concreteness, the pencil generated by
\[
F_0=X^6+XZ^5,\qquad F_1=X^6+X^5Z+Z^6
\]
is all-smooth and base-point-free. Its four members pass the same gcd test; its source-coordinate symmetry orbit has size \(24\). There is therefore no existence gap hidden in the enumeration.

The maximum dimension of an all-smooth projective linear *system* is one, as a separate elementary boundary observation: if \(\dim W\ge3\), the two linear jet conditions \(F(P)=0\) and \(dF(P)=0\) at any rational source point \(P\) have a nonzero common solution in \(W\), contradicting reducedness. This dimension argument is not claimed to be an independent new theorem.

## Verification
Run `python3 verify_enumeration.py` with `orbit_catalogue.json` in the same directory; it enumerates projective forms and projective pencils, tests polynomial gcds by direct \(\mathbf F_3\) Euclidean arithmetic, and reconstructs every orbit using the full 24-element projective group. It also checks the complete reference catalogue.

Run `python3 verify_independent.py` (requires SymPy). This independent implementation enumerates pencils by reduced-row-echelon matrices, tests sextic squarefreeness with SymPy polynomial gcds, and computes the orbits using three explicit generating transformations. It reproduces the same five rational-root profiles and five base-divisor degrees. Both programs were executed successfully from the packaged files and agree on every aggregate in this claim.

## Relationship to prior work
Asgarli and Ghioca, *Smoothness in pencils of hypersurfaces over finite fields* (arXiv:2203.07169, 2022), formulate the discriminant-avoiding linear-system problem and prove existence for sufficiently large fields for projective ambient dimension at least two; they give specific low-degree examples. Their inspected paper does not provide the complete \(\mathbf F_3\) binary-sextic pencil census or its projective symmetry partition. Zobernig, *Genus 2 Curves in Small Characteristic* (arXiv:2111.07270, 2021), studies moduli and characteristic-three \(p\)-rank strata of individual genus-two curves, not linear pencils of their reduced branch divisors. The branch/pencil distinction is essential: orbit counts of individual sextic forms do not determine the orbit structure of two-dimensional subspaces.

## Limitations
The classification is specific to degree six over \(\mathbf F_3\). The orbit count is for branch-divisor pencils under source-coordinate changes, not for isomorphism classes of families of double covers with chosen twists. The finite exhaustive proof is reproducible but is not a closed symbolic formula for general field size or general degree. An unindexed earlier finite census or a stronger universal exact counting formula could affect publication priority. Independent mathematical review has not been performed.

## References
- S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, initially public 2022-03-14, https://arxiv.org/abs/2203.07169 ; full text https://webpages.scu.edu/ftp/sasgarli/smoothness-in-pencils.pdf .
- L. Zobernig, *Genus 2 Curves in Small Characteristic*, arXiv:2111.07270, initially public 2021-11-14, https://arxiv.org/abs/2111.07270 .
- A. Entin, *Monodromy of Hyperplane Sections of Curves and Decomposition Statistics over Finite Fields*, arXiv:1805.05454, 2018; its asymptotic statistics are distinguished from the exact small-field pencil census here.
