# Twenty-five rank-three theories of three-prime divisor lattices

## Finding

Let \(n=p^a q^b r^c\), where \(p,q,r\) are pairwise distinct primes and \(a,b,c\ge 1\). Write \(D(n)\) for the poset of all positive divisors of \(n\), ordered by divisibility, in first-order logic with equality and the single binary relation \(\mid\). No prime, lattice operation, rank predicate, or valuation coordinate is named.

Put \(A=a+1\), \(B=b+1\), \(C=c+1\). Sort \((\min(A,6),\min(B,6),\min(C,6))\) into nondecreasing order. The attached exhaustive `classification.json` assigns each such triple one of the identifiers T01–T25. For any two integers having exactly three distinct prime divisors,

\[
D(n)\equiv_3 D(m)\quad\Longleftrightarrow\quad\text{their capped sorted triples have the same T-identifier}.
\]

Thus exactly **25** quantifier-rank-three theories occur. Every lattice in the family has a rank-three-equivalent lattice with at most **150** divisors; this is the *sharp least uniform bound within the family*. The class T25 has least representative side lengths \((5,5,6)\), giving \(5\cdot5\cdot6=150\) divisors. In particular, lattices with lengths \((5,5,6)\) and \((6,6,6)\) are rank-three equivalent, as are the nonisomorphic lattices with lengths \((3,3,4)\) and \((3,4,4)\).

The three-factor geometry has a stronger cutoff than the usual three-round linear-order cutoff: every side length \(\ge6\) may be replaced by \(6\) without changing this three-factor lattice's rank-three theory.

**Complete finite classification.** Entries list the representative side lengths, its number of divisors, and *all* normalized triples with side lengths in \(\{2,3,4,5,6\}\) in that class. Sorting is implicit. This table and the machine-readable table are equivalent.

| Class | Least representative side lengths | Number of divisors | Normalized triples |
| --- | --- | ---: | --- |
| T01 | \(2,2,2\) | 8 | \(2,2,2\) |
| T02 | \(2,2,3\) | 12 | \(2,2,3\) |
| T03 | \(2,2,4\) | 16 | \(2,2,4\) |
| T04 | \(2,3,3\) | 18 | \(2,3,3\) |
| T05 | \(2,2,5\) | 20 | \(2,2,5\) |
| T06 | \(2,2,6\) | 24 | \(2,2,6\) |
| T07 | \(2,3,4\) | 24 | \(2,3,4\) |
| T08 | \(3,3,3\) | 27 | \(3,3,3\) |
| T09 | \(2,3,5\) | 30 | \(2,3,5\) |
| T10 | \(2,4,4\) | 32 | \(2,4,4\) |
| T11 | \(2,3,6\) | 36 | \(2,3,6\) |
| T12 | \(3,3,4\) | 36 | \(3,3,4\), \(3,4,4\) |
| T13 | \(2,4,5\) | 40 | \(2,4,5\) |
| T14 | \(3,3,5\) | 45 | \(3,3,5\), \(3,5,5\) |
| T15 | \(2,4,6\) | 48 | \(2,4,6\) |
| T16 | \(2,5,5\) | 50 | \(2,5,5\) |
| T17 | \(3,3,6\) | 54 | \(3,3,6\), \(3,5,6\), \(3,6,6\) |
| T18 | \(2,5,6\) | 60 | \(2,5,6\), \(2,6,6\) |
| T19 | \(3,4,5\) | 60 | \(3,4,5\) |
| T20 | \(4,4,4\) | 64 | \(4,4,4\) |
| T21 | \(3,4,6\) | 72 | \(3,4,6\) |
| T22 | \(4,4,5\) | 80 | \(4,4,5\), \(4,5,5\) |
| T23 | \(4,4,6\) | 96 | \(4,4,6\), \(4,5,6\), \(4,6,6\) |
| T24 | \(5,5,5\) | 125 | \(5,5,5\) |
| T25 | \(5,5,6\) | 150 | \(5,5,6\), \(5,6,6\), \(6,6,6\) |

## Assumptions and scope

The universe is the finite set of all positive divisors of an integer with **exactly three distinct prime factors**. The only nonlogical relation is reflexive divisibility. Quantifier rank is maximum nesting depth of first-order quantifiers, with unrestricted alternation and variable reuse. The theorem is about ordinary first-order rank-three equivalence, not three-variable logic, lattice-term language, counting logic, or isomorphism.

Prime-exponent factorization identifies \(D(p^a q^b r^c)\) with the product poset \([A]\times[B]\times[C]\), where \([s]=\{0,\ldots,s-1\}\) has the usual order and the product is ordered coordinatewise. Permuting factors yields an isomorphism.

## Proof

**1. Infinite-to-finite reduction.** For finite nonempty linear orders, the classical three-round Ehrenfeucht–Fraïssé strategy gives \([s]\equiv_3[t]\) whenever \(\min(s,7)=\min(t,7)\). Play this three-round strategy independently in every coordinate of two products having corresponding capped side lengths. If a point with three coordinates is selected, the responses are the three coordinate responses. Equality and coordinatewise order are then preserved among all selected triples because they are conjunctions of the corresponding coordinate comparisons. Thus every three-factor product with side lengths at least two is rank-three equivalent to one with each side length in \(\{2,\ldots,7\}\). There are exactly \(\binom{8}{3}=56\) sorted triples in this range.

**2. Exact finite logical invariant.** For a finite poset \(P\), define the comparison code \(\tau(x,y)\) to be one of \(=,<,>,\parallel\). For each ordered pair let
\[
E_P(x,y)=\{(\tau(x,z),\tau(y,z)):z\in P\},
\]
\[
Q_P(x)=\{(\tau(x,y),E_P(x,y)):y\in P\},
\qquad\Sigma(P)=\{Q_P(x):x\in P\}.
\]
The first set is precisely the complete *one-remaining-move* atomic extension profile of the selected pair; the second is the two-remaining-move profile of a selected point; the third is the three-round sentence profile. Induction on the remaining moves (or the Ehrenfeucht–Fraïssé game characterization) yields
\[
P\equiv_3 P'\quad\Longleftrightarrow\quad\Sigma(P)=\Sigma(P').
\]
This is an exact criterion: equality, both directions of order, and incomparability are all recorded; every possible response of either player is represented by a member of the relevant set.

**3. Exhaustive extension masks without approximation.** For \(x=(x_i)\), \(y=(y_i)\), and a potential reply \(z=(z_i)\), record in each coordinate the four truth values \(x_i\le z_i\), \(z_i\le x_i\), \(y_i\le z_i\), and \(z_i\le y_i\). For fixed \(x_i,y_i\), enumerate the resulting finite set of four-bit masks over every \(z_i\) in that coordinate's chain. The allowable combined four-bit masks are exactly all bitwise intersections of one local mask from each coordinate, since product order is coordinatewise and \(z\)'s coordinates vary independently. Each combined mask uniquely gives \(\tau(x,z)\) and \(\tau(y,z)\). Taking the set of these pairs computes \(E_P(x,y)\) exactly, with no heuristic sampling. `verify.py` implements this finite proof directly, using only Python's standard library.

**4. The finite classification and improved cutoff.** Enumerating the \(56\) sorted triples with sides \(2\) through \(7\) and grouping by the fully computed \(\Sigma\) gives exactly \(25\) distinct signatures. Moreover for every \(a,b\in\{2,\ldots,7\}\),
\[
\Sigma([a]\times[b]\times[6])=\Sigma([a]\times[b]\times[7]).
\]
These are \(36\) explicit exact comparisons. Combined with Step 1, they show that the uniform coordinate cutoff improves to \(6\) when all three factors have lengths at least two. There are then only \(\binom{7}{3}=35\) sorted capped tuples, divided into \(25\) classes, exactly as shown in the table. The attached `classification.json` includes all \(56\) originally reduced triples as well as the complete class-membership table.

**5. Sharp least representative.** Every original side length is at least its six-capped value, so the number of divisors of any original lattice is at least the product of its capped lengths. For each of the \(25\) signatures, the table lists a member with the *smallest* such product. The largest of these minima is \(150\), uniquely at class T25, whose smallest triple is \((5,5,6)\). Therefore \(150\) is not just an upper bound but the sharp largest minimum within this three-prime family.

## Verification

Running `python3 verify.py` with standard Python regenerates `classification.json` and verifies: all \(56\) reduced cases, the \(36\) coordinate-six/seven comparisons, exactly \(25\) classes, the sharp \(150\)-divisor bound, and the class-size distribution. An independently coded whole-vertex enumeration of every third-move response agrees with the coordinate-mask algorithm on twelve additional nontrivial instances. Five checks with side length eight confirm the expected reduction boundary but are not used to prove the infinite statement. Exact run output is included as `verification_output.txt`.

The infinite claim is justified by the coordinatewise game proof and the complete finite classification, not extrapolated from tested large instances. `classification.json` contains both class representatives and every member of the finite canonical domain.

## Relationship to prior work

Mwesigye and Truss (2010, publicly available from 7 September 2010) develop Ehrenfeucht–Fraïssé equivalence, characters and finite representative bounds for coloured *linear* orders, including the familiar exact monochromatic size cutoff. Their results provide the one-coordinate method of Step 1, but not the three-coordinate lattice classification, its \(25\) equivalence classes, its improved cutoff \(6\), or its \(150\)-element sharp representative bound. Their subsequent 2018 publication develops optimal representatives of coloured linear orders, again without a three-factor product classification. The present result concerns uncoloured divisor posets in a single binary relation, rather than linear orders with named colour predicates.

## Limitations

This result is confined to finite divisor lattices with exactly three distinct prime divisors in the pure divisibility language and to quantifier rank at most three. It does not classify integers with four or more prime factors, arbitrary distributive lattices, or richer signatures involving gcd, lcm, prime labels, or counting. The complete finite calculation is exact, but it has not received independent external validation. A relevant result hidden in inaccessible or unindexed literature could affect originality.

## References

1. F. Mwesigye and J. K. Truss, *Classification of Finite Coloured Linear Orderings*, **Order** 28 (2011), 387–397, published online 7 September 2010, DOI: `10.1007/s11083-010-9178-9`; lawful institutional repository full text: `https://ir.must.ac.ug/bitstreams/ce8f9fc1-8064-4e56-b7ae-a30dd6b401c0/download`.
2. F. Mwesigye and J. K. Truss, *On Optimal Representatives of Finite Coloured Linear Orders*, **Order** 36 (2019), 107–117, published online 2 May 2018, DOI: `10.1007/s11083-018-9458-3`; OA full text: `https://eprints.whiterose.ac.uk/id/eprint/129275/15/Mwesigye-Truss2019_Article_OnOptimalRepresentativesOfFini.pdf`.
