# Exact two-helper recovery spectrum of augmented ternary affine-half LCD codes

## Finding

For every integer \(n\ge3\), put \(m=n-1\) and
\[
B_m=\frac{3^m-1}{2}+2m+1.
\]
For the ternary LCD code of Mondal–Lee, Theorem 4.12, every coordinate admits two-helper recovery. Let \(R_2(c)\) count the **unordered, inclusion-minimal** two-helper sets for coordinate \(c\): the target generator column lies in the span of the two helper columns, but in the span of neither helper alone. Then the entire coordinatewise spectrum is:

| Coordinate class | Count \(R_2\) | Number of such coordinates |
| --- | ---: | ---: |
| Evaluation \(P(0,0)\) or constant systematic \(S_*\) | \(B_m\) | \(2\) |
| Evaluation \(P(0,y)\), with \(\operatorname{wt}(y)=1\) | \(B_m+2\) | \(2m\) |
| Evaluation \(P(0,y)\), with \(\operatorname{wt}(y)\ge2\) | \(B_m+1\) | \(3^m-1-2m\) |
| Evaluation \(P(1,0)\) | \(B_m+1\) | \(1\) |
| Evaluation \(P(1,y)\), with \(y\ne0\) | \(B_m\) | \(3^m-1\) |
| First-coordinate systematic \(S_0\) | \(3^m+1\) | \(1\) |
| Other systematic slopes \(S_j\), \(1\le j\le m\) | \(2\cdot3^m+2\) | \(m\) |

The **only** coordinates of locality \(1\) are \(P(0,0)\) and \(S_*\), which have identical columns; every other coordinate has locality exactly \(2\). Thus the number of supports of weight-three dual codewords, counted without nonzero scalar multiples, is
\[
N_3(m)=\frac{(2\cdot 3^m+1)B_m+(2m+2)3^m+4m+1}{3}.
\]
The number of individual weight-three dual codewords is \(2N_3(m)\). These counts concern all minimal recovery **pairs**, not necessarily disjoint repair availability.

## Assumptions and scope

Work over \(\mathbb F_3\). Index generator rows by \(0,1,\dots,m,*\). The generator matrix is the \((m+2)\)-by-\((2\cdot3^m+m+2)\) matrix with columns
\[
P(z,y)=(z,y_1,\ldots,y_m,1)^\mathsf T,\quad z\in\{0,1\},\ y\in\mathbb F_3^m,
\]
together with all standard unit columns \(S_0,S_1,\dots,S_m,S_*\). The source constructs precisely this systematic augmented code, since its defining set is \(\{0,1\}\times\mathbb F_3^m\). There are no zero columns; all evaluation columns are distinct, and the only repeated projective class is \(P(0,0)=S_*\). The code has dimension \(m+2\), length \(2\cdot3^m+m+2\) and minimum distance \(3^m+1\), the last property being established in the source rather than claimed here.

For a target coordinate \(c\) and a two-element subset \(\{a,b\}\) of **other coordinate positions**, we count it if and only if the target column belongs to \(\operatorname{span}_{\mathbb F_3}\{G_a,G_b\}\) but neither single column suffices. Distinct coordinate positions are kept distinct even when their columns are proportional.

## Proof

A coordinate is recoverable from a set exactly when its generator column lies in the linear span of those helper columns: the row-vector message gives every codeword, and the desired linear functional must be determined by the helper functionals. Hence two-helper recovery is the projective collinearity problem, with proportional pairs excluded by minimality.

For an evaluation target \(P(z,y)\), first take **two distinct evaluation helpers**. All three have last coordinate \(1\). Their projective collinearity forces the three affine points to be the complete ternary line. As the first-coordinate allowed values are \(0,1\), such a three-point line must hold that coordinate fixed, because the three values on a nonhorizontal line would be \(0,1,2\). The \(m\)-dimensional affine slice contains \((3^m-1)/2\) lines through each of its points, and each gives exactly one helper pair.

Next take **one evaluation helper and one slope systematic**. Since the last coordinate of the target is \(1\), an admissible helper is a point one unit away in the corresponding direction. For each of the \(m\) unrestricted axes there are two such helpers, and along the restricted first axis precisely one. This produces \(2m+1\) more pairs for every evaluation target. Their sum is \(B_m\). The extra constant-systematic column \(S_*=P(0,0)\) yields an additional pair \(\{S_*,P(0,-y)\}\) when \(z=0,y\ne0\). Pairs of systematic columns can generate an evaluation target only when one is \(S_*\) and the target is a single coordinate displacement: the \(2m\) positions \(P(0,\pm e_j)\), or \(P(1,0)\). Each of these gets one further pair. These are exhaustive by the last-coordinate argument, giving every evaluation row in the table. The same argument for \(P(0,0)\) excludes any pair using its proportional companion \(S_*\), since it would not be inclusion-minimal.

For \(S_j\), \(1\le j\le m\), both helpers must be evaluations on one affine line parallel to the \(j\)-th axis, or be \(S_*\) and an evaluation with \(y=\pm e_j,z=0\). In each of two slices there are \(3^{m-1}\) parallel lines, each containing three evaluation points and yielding \(\binom32=3\) unordered pairs. Thus \(R_2(S_j)=2\cdot3^m+2\). For \(S_0\), the evaluation helpers are exactly the \(3^m\) pairs \(\{P(0,y),P(1,y)\}\), plus \(\{S_*,P(1,0)\}\), giving \(3^m+1\). The remaining systematic \(S_*\) has the same projective point as \(P(0,0)\), and therefore count \(B_m\). The argument also rules out any missing pairs between systematic columns: two nonconstant slopes have last coordinate zero and span no affine target, and a slope other than the target cannot combine with another slope to generate the target.

Exactly two coordinates have identical projective columns; all other projective columns occur once, so those two have locality one. Every other coordinate has positive \(R_2\) and no singleton recovery, proving locality two. Every unordered projective three-circuit supports exactly three target–helper-pair incidences and exactly two nonzero ternary dual vectors. Summing the table therefore gives the displayed \(N_3(m)\) and dual weight-three count.

## Verification

The standalone, standard-library Python program `verify.py` constructs every actual generator column, enumerates every unordered distinct helper pair, tests the two nontrivial points on its projective line over \(\mathbb F_3\), and counts all minimally recoverable target positions. It independently compares those numbers with every coordinate class in the theorem, including the exceptional proportional pair. It exhaustively checks \(n=3,4,5\), with respective lengths \(22,59,168\), total target–pair incidences \(234,1329,8814\), and weight-three dual-circuit counts \(78,443,2938\). Run `python3 verify.py` and expect `VERIFY_OK`. The proof, not these finite tests, establishes all \(n\ge3\).

## Relationship to prior work

Mondal and Lee [1, Theorem 4.12 and Remark 4.11] supply this code family, its systematic augmented generator, LCD property, minimum distance and ordinary Hamming-weight distribution. None of these foundational results is claimed as new. The new statement is the complete coordinate-dependent count of inclusion-minimal two-helper recovery sets. Its summed dual three-circuit count is included for consistency, but as an aggregate it can also be obtained from the source ordinary weight enumerator by the MacWilliams identities; it is not claimed independently novel. Haymaker–Malmskog–Matthews [2] exploit affine-line geometry for locality and availability of Reed–Muller and fiber-product codes; their affine-line principle underlies one component of this count, but their evaluated families do not have this restricted first coordinate and appended systematic basis with the single repeated projective column. Grezet–Hollanti [3] give hierarchical localities for punctured simplex families, a different projective-column geometry; the enumerated targetwise recovery counts here are not consequences of their locality-parameter statements alone.

## Limitations

This is an exact theorem for the specified ternary family, not a claim about arbitrary LCD codes or fields of other sizes. It counts recovery pairs without requiring disjointness and does not determine larger recovery sets, maximum disjoint availability, or full dual weight enumerators. General geometric line-recovery ideas are known; an unindexed equivalent calculation remains possible despite comparisons with primary literature and available research records. Computational examples do not replace the all-dimensional proof. Independent audit has not been performed.

## References

[1] N. K. Mondal and Y. Lee, *Infinite families of LCD codes and their weight distributions*, Applicable Algebra in Engineering, Communication and Computing (first public 2026-09-04), Theorem 4.12, Remark 4.11, DOI: 10.1007/s00200-026-00756-3; https://link.springer.com/article/10.1007/s00200-026-00756-3.

[2] K. Haymaker, B. Malmskog and G. L. Matthews, *Algebraic hierarchical locally recoverable codes with nested affine subspace recovery*, Designs, Codes and Cryptography 93 (2025), 111–132, DOI: 10.1007/s10623-024-01510-x; https://link.springer.com/content/pdf/10.1007/s10623-024-01510-x.pdf.

[3] M. Grezet and C. Hollanti, *The complete hierarchical locality of the punctured Simplex code*, Designs, Codes and Cryptography 89 (2021), 105–125, DOI: 10.1007/s10623-020-00810-2; https://link.springer.com/article/10.1007/s10623-020-00810-2.
