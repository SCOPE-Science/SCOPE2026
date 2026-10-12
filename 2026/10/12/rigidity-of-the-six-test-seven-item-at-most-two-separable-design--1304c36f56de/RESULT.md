# Rigidity of the six-test seven-item at-most-two separable design
## Finding
Consider a binary nonadaptive group-testing matrix with six rows (tests) and a set of columns (items). For a defective set \(D\) of at most two items, its outcome is the coordinatewise Boolean OR of the columns in \(D\), with the empty-set outcome equal to the zero vector. The design is at-most-two separable when distinct defective sets of size at most two have distinct outcomes.

The maximum number of items is \(7\). Moreover, every extremal \(6\\times7\) design is equivalent under permutations of rows and columns to the matrix whose unordered columns are
\[
000011,\ 001100,\ 010101,\ 011010,\ 100110,\ 101001,\ 110000.
\]
On six labeled rows there are exactly \(30\) unordered maximum column families. The natural row-permutation group \(S_6\) is transitive on them, and the stabilizer of a maximum family has order \(24\). Hence there are exactly \(30\\cdot7!=151{,}200\) fully labeled maximum matrices.

Every maximum family has three columns of weight \(2\) and four of weight \(3\). The three weight-two supports are pairwise disjoint and partition the six rows into three pairs. Each weight-three support chooses one point from each pair, and the four such transversals form one parity class of the resulting three-dimensional binary cube. If a seventh point is added to each of the three weight-two supports, the seven resulting triples form the unique \(2\!-(7,3,1)\) design, the Fano plane.

## Assumptions and scope
Columns are binary and distinct, column order is irrelevant unless the fully labeled count is requested, and all defective sets of cardinality \(0\), \(1\), or \(2\) must be distinguished by Boolean OR. The empty outcome is automatically distinct because no zero column can occur in a valid maximum family. Equivalence means independent permutations of the six test rows and the seven item columns.

The claim is finite and exact. It does not assert a classification for other numbers of tests, other defective-set bounds, adaptive testing, noisy outcomes, or nonbinary alphabets.

## Proof
Represent a nonzero six-bit column by an integer in \(\{{1,\ldots,63}\}\). For an unordered family \(C\), define
\[
\Phi(C)=\{c:c\in C\}\cup\{c\\lor c':c,c'\in C,\ c\ne c'\}.
\]
At-most-two separability is exactly the injectivity condition
\[
|\Phi(C)|=|C|+\binom{|C|}{2},
\]
because the zero outcome of the empty defective set is separate from every nonempty Boolean OR.

The exhaustive search in `artifacts/verify.py` visits columns in strictly increasing integer order. At each node it stores exactly the singleton and pair-OR outcomes already forced by the chosen columns. A candidate column is rejected if and only if its singleton outcome or one of its new pair-OR outcomes collides with an existing outcome or with another new outcome. Thus every unordered separable family has exactly one search path, and no valid family is pruned. The search returns \(30\) families of size \(7\) and no family of size \(8\). Since every subfamily of a separable family is separable, the absence of an eight-column family proves that \(7\) is the maximum.

A direct replay recomputes all \(7+\binom72=28\) nonempty outcomes for each of the \(30\) maxima. The verifier then applies all \(6!=720\) row permutations to one representative and obtains exactly the same \(30\)-family census. Therefore there is one row-equivalence class and its stabilizer has order \(720/30=24\).

Finally, the verifier checks every maximum family structurally: its weights are exactly \(2,2,2,3,3,3,3\); its three weight-two supports are disjoint and cover all six rows; every weight-three support meets each matched pair once; and the four transversals have constant parity relative to any one of them. Adding a new point to the three matched pairs yields seven triples in which every pair of the seven points lies in exactly one triple. This is a \(2\!-(7,3,1)\) design, hence the Fano plane.

## Verification
Run `python3 artifacts/verify.py` using the Python standard library. The packaged replay is expected to print:

`VERIFY_OK nodes7=49299 nodes8=48919 maximum=7 labeled_row_families=30 fully_labeled_matrices=151200 row_group=720 orbits=1 orbit_size=30 stabilizer=24 weights=2x3,3x4 canonical=000011;001100;010101;011010;100110;101001;110000 census_sha256=7ac7fdffca94f4bf5e1ad4c5842affcbec53aff20bab076757c20c02865f9190`

The target-eight search is an exhaustive impossibility check, not a timeout inference. The target-seven census and the row-orbit calculation are recomputed from definitions. No external solver, precomputed table, or floating-point comparison is used.

## Relationship to prior work
Kautz and Singleton introduced binary superimposed codes in terms of distinguishability of coordinatewise Boolean sums, providing the historical coding formulation for this object. Their paper is indexed under primary MSC \(68P20\) and also MSC \(94B60\).

Chen's 2010 thesis treats exactly seven items and at most two defectives. It proves that deleting one row from the incidence matrix of the projective plane of order \(2\) gives a \(6\\times7\) at-most-two separable matrix, and its main theorem proves that no at-most-two separable \(s\\times t\) matrix exists with \(s<t<7\). The inspected main-result section supplies one optimal Fano-derived construction and the smaller-parameter obstruction, but it does not classify all \(6\\times7\) equality cases, count the labeled-row maxima, or determine their symmetry orbit.

The present result supplies that missing equality classification: every optimum is Fano-derived, with exactly \(30\) labeled-row families and one row-permutation orbit.

## Limitations
The classification is for the noiseless Boolean-OR model with at most two defectives and exactly six tests. The originality comparison is limited by the discoverability of historical literature; an obscure unindexed equality classification could exist. The computational proof is finite and reproducible, but it does not by itself yield a general structural theorem for larger parameters.

## References
1. W. H. Kautz and R. C. Singleton, “Nonrandom Binary Superimposed Codes,” *IEEE Transactions on Information Theory* 10(4) (1964), 363–377. DOI: 10.1109/TIT.1964.1053689.
2. Chien-Wen Chen, “A projective plane of order 2 offers the best group tests—for 7 items and at most 2 defectives,” M.S. thesis, National Chiao Tung University, 2010. Repository record: https://ir.lib.nycu.edu.tw/handle/11536/45075 .
