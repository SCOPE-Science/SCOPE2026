# Exact rank-three type census for binary chains with two to four red markers

## Finding

A **binary coloured chain** is a finite linearly ordered set with two named unary colours \(B\) and \(R\), partitioning its points. For \(k\in\{2,3,4\}\) and nonnegative integers \(a_0,\ldots,a_k\), write
\[
W_k(a_0,\ldots,a_k)=B^{a_0}RB^{a_1}R\cdots RB^{a_k}.
\]
The quantifier-rank-three equivalence classes represented by chains with exactly \(k\) red points have the following **exact cardinalities and sharp least-representative lengths within that stratum**:

| Number \(k\) of red points | Number of rank-three classes | Greatest minimum length | Unique longest-minimum class, canonical blue-gap tuple |
| ---: | ---: | ---: | --- |
| 2 | 310 | 19 | \((6,5,6)\) |
| 3 | 1865 | 25 | \((6,5,5,6)\) |
| 4 | 11196 | 31 | \((6,5,5,5,6)\) |

For each row, exactly one rank-three equivalence class has the displayed greatest minimum length **among representatives with exactly \(k\) red points**. Its indicated tuple is the unique representative of that least length within that stratum. The equivalence-class test for arbitrary blue-gap lengths is the explicit finite signature below, after capping all gaps at seven. Thus these numbers classify every chain in the stated families, not merely words of bounded length.

## Assumptions and scope

First-order logic uses equality, strict order, and the two unary colour predicates. Quantifier rank is the maximum quantifier nesting depth. There are no named constants or successor predicate. The red points are indistinguishable except through order. The number \(k\) is fixed to 2, 3, or 4 when seeking a shortest representative; the theorem does not assert that the minimal representative across the entire two-colour language has the same length if it is permitted to have a different number of red points.

Define \(H_1(w)\) as the set of colours in the word \(w\), including \(H_1(\epsilon)=\varnothing\). Recursively, for \(q\ge1\), let
\[
H_{q+1}(w)=\{(c,H_q(u),H_q(v)):w=ucv\}.
\]
For words in the specified families, equality of \(H_3\) is an exact decision procedure for rank-three equivalence. In particular, \(H_2(w)\) is the set of triples comprising a point's colour and the colour sets strictly before and after it.

## Proof

**Character lemma.** Two finite coloured chains have the same rank-\(q\) theory exactly when their \(H_q\) signatures agree. For \(q=1\), this is the assertion that the same colours occur. For the inductive step, equality of \(H_{q+1}\) says that every choice of an initial point of a given colour on either side can be answered by a point whose left and right subchains each have the matching rank-\(q\) type. The response combines the two independent residual back-and-forth strategies because the order between the left and right blocks is fixed. Conversely, Spoiler can play the first point witnessing a missing character and then direct the remaining game to the side on which the rank-\(q\) types differ. This proves the equivalence; it is the character method of Mwesigye and Truss.

**Seven-point reduction.** For monochromatic finite linear orders, the same induction gives \(B^s\equiv_q B^t\) if and only if \(\min(s,2^q-1)=\min(t,2^q-1)\), for \(q\ge1\). In particular, all pure-blue blocks containing at least seven points have the same rank-three theory. Rank-three equivalence is preserved by concatenation with fixed left and right words: the back-and-forth strategy inside an equivalent block may be combined with copying the other blocks. Therefore, in every \(W_k\) with \(k\in\{2,3,4\}\), simultaneously replace each blue-gap length \(a_i\) by \(\min(a_i,7)\) without changing its rank-three theory. There are exactly \(8^{k+1}\) capped parameter tuples to consider. Every uncapped word thus has a capped equivalent of no greater length. Conversely, every capped word belongs to the original family; hence searching the capped universe computes **all** class counts and exact minimum lengths.

**Finite exact classification.** For each capped tuple, compute its colour word, then its \(H_2\) and \(H_3\) as the sets in the preceding definitions. Group the capped tuples by exact equality of \(H_3\). For each group take the tuple minimizing first the number of letters \(k+\sum_i a_i\), then lexicographic order. Enumerating the 512, 4096, and 32768 capped tuples at \(k=2,3,4\), respectively, gives exactly 310, 1865, and 11196 distinct signatures. The maximum of these group-minimal lengths is, respectively, 19, 25, and 31; in each stratum a single group attains it, with the gap tuple displayed in the finding. This is an exhaustive finite argument justified by the exact signature lemma and seven-point reduction, not extrapolation from a numerical sample. The complete enumeration procedure, with two independently implemented signature methods that agree on every capped tuple, is included in `verify.py`.

For the two-red stratum the 19-point extremal word also has no shorter rank-three-equivalent **binary coloured chain with another red count**: rank-three sentences can assert at least two red points and exclude three red points. Thus the example yields an exact 19-point obstruction in the full binary language. This is not asserted to improve the best known general lower bounds for all binary coloured chains.

## Verification

Run `python3 verify.py` with the Python 3 standard library. The checker evaluates \(H_3\) by direct examination of every red/blue position and independently by right-append transitions of bit-packed \(H_2\) and \(H_3\) characters. It tests their equality for each capped word; counts the exact signature classes; determines the least-length representative in each class; verifies the unique extremal class and its tuple; and checks the finite boundary \(7\to8\) in the two- and three-red cases. The recorded successful output is in `verification_output.txt`. The infinite seven-point reduction and the logical character lemma are proved above and are not inferred from this boundary experiment.

## Relationship to prior work

Mwesigye and Truss (published online 7 September 2010; 2011 journal issue) established general finite-coloured-order bounds, the rank-character recurrence, and exact global optimum lengths for rank one and two; they did not give these three rank-three marker-stratum counts. Their later paper (online 2018, journal 2019) examines the challenging unrestricted two-colour rank-three problem and constructs 70- and 74-point optimal words, but its results do not determine the exact numbers of types and the sharp relative minimum lengths in the fixed two-, three-, and four-red families. The earlier published one-red classification gives 51 rank-three types and a sharp 13-point representative, which is a calibration and does not imply the present multi-marker counts. Our use of the general character lemma and monochromatic cutoff is expressly credited rather than claimed as new.

## Limitations

The restriction to exactly two, three, or four red points is essential to the enumerated counts. In the three- and four-red rows the shortest-word claims hold among words with the same number of red points; an equivalent word with more red points is not excluded by the argument. The exact global optimum \(g(2,3)\) for unrestricted binary coloured chains is not determined here. A finite exhaustive program is part of the proof of the enumerated constants; its logic and data representations must be scrutinized if those constants are reused. Independent mathematical review has not been performed. Earlier unindexed results may contain the same sparse-marker evaluations.

## References

1. F. Mwesigye and J. K. Truss, *Classification of Finite Coloured Linear Orderings*, *Order* 28 (2011), 387–397. DOI: 10.1007/s11083-010-9178-9; available public online 2010-09-07. Theorem 1.2 supplies the rank-character recurrence.
2. F. Mwesigye and J. K. Truss, *On Optimal Representatives of Finite Coloured Linear Orders*, *Order* 36 (2019), 107–117. DOI: 10.1007/s11083-018-9458-3; online 2018-05-02.
3. *Exact quantifier-rank profiles for finite one-red linear orders*, published research record (2026-10-04), identifier `2026/10/4/SCOPE-exact-quantifier-rank-profiles-for-finite-one-red-linear-orders--eec9053b6af5`; used solely for the one-red comparison, with the record's summary inspected.
4. J. G. Rosenstein, *Linear Orderings*, Academic Press, 1982 (classical finite linear-order rank cutoff).
