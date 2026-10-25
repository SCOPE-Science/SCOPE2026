# The exceptional binary-field intersection spectrum of plane cubic pairs

## Finding
Let \(k=\mathbf F_2\), and let \(V=k[X,Y,Z]_3\) be the ten-dimensional vector space of ternary homogeneous cubics. Among **ordered pairs** \((F,G)\) of nonzero forms defining curves without a common geometric irreducible component, the exact distribution by the number \(r=|V(F,G)(k)|\) of distinct rational common points is:

| \(r\) | Number of ordered pairs |
|---:|---:|
| 0 | 139944 |
| 1 | 326382 |
| 2 | 325836 |
| 3 | 171108 |
| 4 | 47208 |
| 5 | 6678 |
| 6 | 420 |
| 7 | 0 |

There are exactly \(1\,017\,576\) such ordered pairs. In particular, the sharp upper bound is **six** rational intersection points, not seven. The 210 extremal **unordered** pairs form exactly five orbits under \(\operatorname{PGL}_3(k)\), with orbit sizes \(84,28,28,28,42\). For the ordered monomial basis
\[
(X^3,X^2Y,X^2Z,XY^2,XYZ,XZ^2,Y^3,Y^2Z,YZ^2,Z^3),
\]
write \(F_m\) for the polynomial whose coefficient of basis element \(j\), starting at \(j=0\), is the \(j\)-th binary digit of the integer \(m\). Representatives of the five unordered orbits are
\[
\{F_{10},F_{180}\},\quad \{F_{10},F_{660}\},\quad
\{F_{10},F_{670}\},\quad \{F_{16},F_{446}\},\quad
\{F_{57},F_{407}\}.
\]
These are classifications in fixed projective coordinates; counts are not counts of isomorphism classes of arbitrary abstract curves.

## Assumptions and scope
Here a pair is ordered for the frequency table and unordered for the five orbit types. Cubic forms over \(\mathbf F_2\) have no nontrivial scalar identifications. A component common over an algebraic closure is forbidden, including components of nonreduced or reducible curves. All rational intersection counts count distinct geometric points rational over \(\mathbf F_2\), not intersection multiplicities. Smoothness of the individual cubic curves is **not** assumed.

## Proof
There are \(2^{10}-1=1023\) nonzero ternary cubics, hence \(\binom{1023}{2}=522753\) unordered distinct pairs before the component restriction. Their rational common-point number is determined exactly by evaluating the two degree-three forms at the seven normalized nonzero vectors of \(\mathbf F_2^3\).

For distinct cubic forms, having a common geometric component is equivalent to having a positive-degree common factor over \(\mathbf F_2\). Indeed, the product of all Frobenius conjugates of a common geometric component descends to a common factor over the base field. Because the forms are distinct and both have degree three, a common factor must have degree one or two. A degree-one common factor is a nonzero homogeneous linear form; a degree-two common factor is a nonzero homogeneous quadratic form. Every cubic divisible by either is found by expanding products of one of the seven nonzero linear forms and one of the 63 nonzero quadratic forms. Thus the exact factor-membership masks built by `verify_cubic_intersections.py` detect **all** excluded pairs, without factoring over extensions or assuming smoothness.

The exhaustive count on unordered pairs before exclusion, indexed by rational intersection number \(r=0,1,\ldots,7\), is
\[
(69972,163212,163044,90300,29820,5796,588,21).
\]
Of these, the numbers with common components are
\[
(0,21,126,4746,6216,2457,378,21).
\]
Subtracting gives \((69972,163191,162918,85554,23604,3339,210,0)\), and doubling yields the ordered distribution in the statement. The integer sum is \(508788\) unordered, hence \(1017576\) ordered admissible pairs.

For the orbit classification, substitute each of the \(168\) invertible \(3\times3\) matrices over \(k\) into both cubics of every extremal unordered pair, reduce coefficients in \(k\), and sort the two resulting masks. Exhaustively removing the orbits in lexicographic order gives representatives \((10,180),(10,660),(10,670),(16,446),(57,407)\) and orbit sizes \((84,28,28,28,42)\). Their sizes total \(210\), proving completeness and disjointness. This also verifies that six is attained.

## Verification
Run `python verify_cubic_intersections.py` and `python verify_independent_count.py` with Python 3 (SymPy is required only for the latter). Their checked output files are `primary_output.txt` and `independent_output.txt`. The first program enumerates all cubic pairs and full projective orbits. The second derives the unrestricted pair histogram from **restriction-pattern multiplicities**, constructs the excluded set independently from divisor incidence, checks the full histogram, and compares 1000 sampled pairs with SymPy's exact multivariate polynomial gcd. Both independently return the same seven nonzero counts.

The executable tests use exact finite-field arithmetic; no floating-point tolerances, probabilistic inferences, unexecuted certificates, or inferred infinite-family statement are involved. The gcd sample only checks the implementation of the common-factor criterion; exhaustive common-factor coverage follows separately from the degree argument in the proof and complete multiplication tables.

## Relationship to prior work
Kaplan and Matei (first arXiv version 2020-03-31, arXiv:2003.13944) give general polynomial expressions for the rational-intersection statistics of pairs of plane cubics, but explicitly impose \(q>2\) in their main theorem. The present calculation resolves the omitted binary field and also supplies the five extremal projective classes. Asgarli and Ghioca (first arXiv version 2022-03-14, arXiv:2203.07169) study existence of pencils all of whose rational members are smooth, a different condition from unrestricted coprime pairs. Their theorems do not tabulate this spectrum. Earlier results about pairs of **smooth** binary plane cubics are stricter special families and cannot determine the distribution involving singular curves.

## Limitations
The result is specific to \(\mathbf F_2\) and degree three; it is not a replacement for the general \(q>2\) formula. The five orbit representatives classify **unordered coordinate-fixed polynomial pairs** only. The numerical counts are exact by complete enumeration, but publication-priority uncertainty remains for uncatalogued small-field tables or unpublished computational datasets. Independent external audit has not been performed.

## References
1. N. Kaplan and V. Matei, *Counting plane cubic curves over finite fields with a prescribed number of rational intersection points*, arXiv:2003.13944v1 (2020-03-31); https://arxiv.org/abs/2003.13944 .
2. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169v1 (2022-03-14); https://arxiv.org/abs/2203.07169 .
