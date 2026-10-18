# Six rational-bitangent strata of pointless plane quartics over \(\mathbf F_5\)

## Finding
Let \(k=\mathbf F_5\). A rational bitangent of a smooth plane quartic \(C=V(F)\subset\mathbf P^2_k\) means an \(L\in(\mathbf P^2_k)^\vee(k)\) for which the degree-four Cartier divisor \(C\cap L\) over \(\bar k\) has even multiplicity at every geometric point. This includes hyperflex lines with contact multiplicity four. For the 31 \(k\)-isomorphism classes of smooth **pointless** plane quartics, the number \(b(C)\) of rational bitangents has exact distribution:

| \(b(C)\) | Number of isomorphism classes |
| ---: | ---: |
| 0 | 3 |
| 1 | 14 |
| 2 | 8 |
| 4 | 4 |
| 6 | 1 |
| 16 | 1 |

Thus \(b(C)\le16\) for every smooth pointless plane quartic over \(k\), with equality for exactly one \(k\)-isomorphism class, represented by the Fermat quartic \(X^4+Y^4+Z^4=0\). Its rational bitangents are precisely the 16 lines \(X+bY+cZ=0\) for \(b,c\in k^\times\). The next largest value is six.

## Assumptions and scope
The base field is exactly \(\mathbf F_5\); curves are geometrically smooth projective plane quartics having no \(k\)-points. Classification is up to \(k\)-isomorphism of abstract curves, which for nonhyperelliptic genus-three curves is projectively induced by their canonical embeddings. The exhaustive 31 source equations are those supplied in Faber–Grantham–Howe, *On the Maximum Gonality of a Curve over a Finite Field* (first arXiv release 2022-07-28), in the authors' file `scripts/AllGenus3.magma` (field-five list `list5`). The supplied `curves_f5.txt` transcribes those 31 equations in their published order. Counts are not claimed for smooth quartics having rational points.

## Proof
The cited source proves that its 31 field-five equations represent every smooth pointless plane quartic, each exactly once up to \(k\)-isomorphism (Table 1 and supplementary models). The bitangent count is preserved by the projective coordinate changes induced by any isomorphism of canonical genus-three curves.

There are \((5^3-1)/(5-1)=31\) rational projective lines. Normalize the coefficient triple \((a,b,c)\) of each line \(aX+bY+cZ=0\) by making its first nonzero entry one. Substituting a linear parameterization \((X,Y,Z)=(\ell_0(s,t),\ell_1(s,t),\ell_2(s,t))\) gives a nonzero binary quartic \(G_L(s,t)\) (nonzero because \(C\) is smooth and contains no line). Its intersection divisor has even geometric multiplicities if and only if \(G_L\) is a scalar multiple, over the algebraic closure, of a square of a binary quadratic. Because \(k\) is perfect of odd characteristic, the half-divisor is Frobenius-invariant and is cut out by a quadratic over \(k\); therefore it suffices to test membership up to scalar in the set of squares of nonzero \(k\)-quadratics.

`bitangent.py` independently tests whether every finite root of a dehomogenization of \(G_L\) has even multiplicity, and whether its vanishing order at infinity is even, by exact squarefree factorization in characteristic five. `bitangent_crosscheck.py` instead precomputes normalized coefficient vectors of all homogeneous squares of degree-two binary forms and checks membership directly. Each program examines every line on all 31 curves. Their individual counts coincide and are printed in `verification_output.txt`; grouping yields the table. The thirty-first equation is exactly the Fermat quartic, and its line list is precisely the claimed 16 triples.

For clarity, this Fermat curve is smooth because its three partial derivatives have no common projective zero. It has no rational point because every nonzero fourth power in \(\mathbf F_5\) equals one, so the sum of three fourth powers is never zero. Its 16 counted bitangents are all the rational lines whose three coefficients are nonzero; the programs also exclude the remaining 15 rational lines. The full classification, rather than a finite experimental sample, establishes the sharp bound and its unique attaining isomorphism class.

## Verification
Run `python census.py` and `python bitangent_crosscheck.py` from the directory containing the included scripts and the 31-equation `curves_f5.txt` data (requires Python 3 and SymPy). Compare their full outputs after ignoring the cross-check's explanatory `FERMAT_LINES` line; they agree exactly. `verification_output.txt` records the common 31 counts and six-stratum distribution. The second verifier asserts that the Fermat line set has 16 elements, each coefficient nonzero. All calculations are exact modulo five, and both methods independently implement the geometric bitangency criterion.

## Relationship to prior work
Faber–Grantham–Howe, arXiv:2207.14307, proved the global excessive-curve classification and provided the exact 31 field-five quartic models, real Weil polynomials, and automorphism-group labels. Their text and inspected source models do **not** present rational-bitangent counts. Howe–Lauter–Top established existence and nonexistence ranges for pointless plane quartics, not this bitangent distribution. The classical correspondence between 28 geometric bitangents and odd theta characteristics motivates this arithmetic refinement but alone does not provide the six numbers or the uniqueness of the 16-bitangent locus. Searches for the same statements via bitangents, Frobenius-fixed theta characteristics, Fermat quartics and pointless curves did not locate equivalent coverage; lack of indexing does not establish historical priority.

## Limitations
The 31 models and their exhaustive representativeness are inherited from the cited primary authors and are not independently reclassified here. The source-equation transcription is reproduced for auditability, and computations are exact, but a previous unindexed bitangent census might exist. Rational lines are counted without distinguishing two simple tangencies from a fourth-order hyperflex. The theorem does not address all smooth plane quartics or other finite fields; no independent external mathematical audit has been performed.

## References
1. X. Faber, J. Grantham, E. W. Howe, *On the Maximum Gonality of a Curve over a Finite Field*, arXiv:2207.14307, first publicly submitted 2022-07-28, especially Table 1 and §8. https://arxiv.org/abs/2207.14307
2. Faber–Grantham–Howe supplementary equations, `scripts/AllGenus3.magma`, field-five `list5` (31 records); https://github.com/RationalPoint/excessive/blob/main/scripts/AllGenus3.magma (retrieved version blob `684ea266a0a862882fb8412572efa652889be49b`).
3. E. W. Howe, K. E. Lauter, J. Top, *Pointless curves of genus three and four*, 2004, arXiv:math/0403178 (existence and bounds on pointless quartics).
