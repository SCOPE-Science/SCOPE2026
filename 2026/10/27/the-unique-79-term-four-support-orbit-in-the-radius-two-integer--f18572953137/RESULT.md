# The unique 79-term four-support orbit in the radius-two integer cube

## Finding

Let \(B=[-2,2]^3\cap\mathbb Z^3\). A multiset \(S\) on \(B\) is *minimal zero-sum* if its vector sum is zero but no nonempty proper submultiset has zero sum. Consider such multisets having exactly four different support vectors.

**Theorem.** Every such \(S\) satisfies \(|S|\le79\). There are exactly **48** distinct multisets with \(|S|=79\). They constitute one free, transitive orbit under the group of 48 signed permutations of the three coordinates.

A representative is specified by the following exact table:

| Vector | Multiplicity |
| --- | ---: |
| \((-2,-2,-2)\) | \(15\) |
| \((-2,1,2)\) | \(20\) |
| \((1,2,-2)\) | \(18\) |
| \((2,-1,1)\) | \(26\) |

Its vector sum vanishes because \(15(-2,-2,-2)+20(-2,1,2)+18(1,2,-2)+26(2,-1,1)=(0,0,0)\). The four coefficients are coprime, and their support matrix has rank three, so the multiset is minimal zero-sum.

## Assumptions and scope

Vectors are integer triples, each coordinate lying in \(\{-2,-1,0,1,2\}\). The order of terms in a multiset does not matter. Support size is **exactly four**; neither larger support sizes nor the unrestricted Davenport constant are classified. Symmetries are arbitrary permutations of the three coordinate axes and independent sign reversals, acting on each vector without changing its multiplicity.

## Proof

**1. Rank reduction.** Let \(A\) be the \(3\times4\) integer matrix whose columns are the four distinct supporting vectors, with each column assigned its positive integer multiplicity. If \(\operatorname{rank}(A)\le2\), choose at most two coordinate projections whose restrictions to the rational span of the columns are jointly injective. Such a projection preserves all zero-sum submultisets and their minimality. Its image lies in \(\{-2,-1,0,1,2\}^2\), whose Davenport constant is bounded by \((2m+1)(4m+1)=45\) for \(m=2\), by the established two-dimensional box bound [1, Section 1, equation (3)]. For rank one choose one injective coordinate, and compose with the inclusion into the two-dimensional box. Thus rank at most two cannot support length 79 or greater.

**2. Primitive cofactor parameterization.** Assume \(\operatorname{rank}(A)=3\), and write its columns as \(v_0,v_1,v_2,v_3\). Define the signed minors

\[
r_j=(-1)^j\det(v_0,\ldots,\widehat v_j,\ldots,v_3),\qquad 0\le j\le3.
\]

The vector \(r=(r_0,r_1,r_2,r_3)\) spans \(\ker_{\mathbb Q}A\). A strictly positive integer relation exists exactly when all signed cofactors are nonzero and have the same sign. Set \(g=\gcd(|r_0|,|r_1|,|r_2|,|r_3|)\). Its primitive positive multiplicity vector is \(c=(|r_0|/g,\ldots,|r_3|/g)\); its length is

\[
L(A)=\frac{|r_0|+|r_1|+|r_2|+|r_3|}{g}.
\]

All integer kernel vectors are integer multiples of \(c\) up to sign. Therefore \(c\) defines a minimal zero-sum multiset, and every minimal zero-sum multiset with rank-three four-element support must use this primitive multiplicity vector. Any larger positive multiple would contain the primitive relation as a proper zero-sum submultiset. There is consequently a **bijection** between positive four-column circuits (support sets without ordering) and eligible rank-three multisets.

**3. Complete exact finite enumeration.** Index the \(125\) vectors lexicographically by

\[
i(x,y,z)=25(x+2)+5(y+2)+(z+2).
\]

Visit all strictly increasing index quadruples \(0\le a<b<c<d<125\). There are exactly \(\binom{125}{4}=9{,}691{,}375\). For each quadruple compute its four signed \(3\times3\) minors using the three-product integer determinant formula; discard the quadruple unless all minors are nonzero with one common sign. Divide their magnitudes by their common gcd and add. The self-contained executable `census.c` implements precisely this algorithm using integers; it returns the following exhaustive counts:

| Quantity | Exact count |
| --- | ---: |
| Unordered four-point subsets examined | \(9{,}691{,}375\) |
| Positive rank-three four-point circuits | \(779{,}864\) |
| Maximum primitive coefficient sum | \(79\) |
| Circuits attaining the maximum | \(48\) |

The program separately reruns the complete index traversal to write all 48 maximizers to `extremizers.tsv`. Both passes use exact integer arithmetic. The rank-reduction step proves that no omitted lower-rank support can reach length 79, so this census proves the length bound and the exact multiplicity count for all four-support minimal zero-sum multisets.

**4. Exactly one symmetry orbit.** The independent script `check_orbit.py` reads all 48 rows, recomputes their signed minors, primitive gcd, zero-sum property and coefficient totals, and converts the ordered indexed columns back to multisets. It applies every one of the \(3!\cdot2^3=48\) signed coordinate permutations to the representative above. The resulting orbit has cardinality 48 and agrees as a set *exactly* with the 48 rows of the complete census. Therefore the action is transitive and its stabilizer of the representative is trivial; the orbit is free. This proves the theorem.

## Verification

The accompanying code and finite certificate are complete and require only a C99 compiler and Python 3 standard library. From the directory containing the files, execute:

```sh
cc -O2 -std=c99 -Wall -Wextra census.c -o census
./census extremizers.tsv
python3 check_orbit.py extremizers.tsv
```

The exact expected output is recorded in `run_output.txt`. The shipped `extremizers.tsv` records all 48 maximizers and is independently regenerated by the C program. The proof reduces the infinite-looking multiset statement to a finite exhaustive set of primitive signed-cofactor relations; it does not infer an infinite theorem from a nonexhaustive sample.

## Relationship to prior work

Girard and Plagne [1] introduced the refined support-size invariant, established the planar box bound used above, and exhibited four-support three-dimensional constructions. Their later focused paper [2] proves bounds for \(\mathsf D^{(4)}([-m,m]^3)\) and reports computational agreement with the proposed length for \(2\le m\le7\); however it explicitly **conjectures**, rather than proves, essential uniqueness of the extremizers under symmetries and term reordering. Our theorem supplies the precise orbit classification at \(m=2\), including the exact number of extremizing multisets and a complete replayable finite certificate. It does not establish uniqueness at any larger radius.

## Limitations

The argument is confined to support size four and the five-level integer cube. It does not determine the full Davenport constant of the cube, which permits arbitrary support size. The general conjectural inverse theorem for \(m>2\) remains open. An exhaustive finite computation is used as a proof certificate; separate independent mathematical review has not been performed. Undetected equivalent results in other literature are still possible.

## References

1. B. Girard and A. Plagne, *The Davenport constant of balls and boxes*, arXiv:2510.20412v1, first publicly posted 2025-10-23, especially equation (3) and Section 11. https://arxiv.org/abs/2510.20412
2. B. Girard and A. Plagne, *The Davenport constant of low-dimensional boxes*, arXiv:2610.16562v1, posted 2026-10-12, Section 2 and Section 4. https://arxiv.org/abs/2610.16562
