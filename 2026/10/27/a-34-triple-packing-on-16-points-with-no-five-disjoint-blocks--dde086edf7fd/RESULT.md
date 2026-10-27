# A 34-triple packing on 16 points with no five disjoint blocks

## Finding

Let \(\beta(\rho,v)\) denote the maximum number of blocks in a partial Steiner triple system on \(v\) points whose largest partial parallel class has exactly \(\rho\) blocks. There is a partial Steiner triple system on \(V=\{0,\ldots,15\}\) with 34 blocks and largest partial parallel class of size exactly 4. Therefore

\[
34\leq \beta(4,16)\leq 37.
\]

The lower bound improves the previously recorded construction of 33 blocks by one block. The value of \(\beta(4,16)\) is not determined here.

The 34 blocks are the following triples:

```text
(1,4,12) (8,9,10) (10,13,15) (4,7,11) (0,6,15) (7,12,15)
(8,11,14) (7,10,14) (2,6,11) (3,9,13) (6,9,14) (0,3,10)
(5,8,12) (4,6,13) (3,6,8) (0,11,13) (1,9,15) (5,11,15)
(0,4,5) (0,1,14) (3,11,12) (2,12,14) (3,5,7) (0,9,12)
(6,10,12) (2,5,13) (4,8,15) (2,3,15) (1,6,7) (1,10,11)
(0,7,8) (1,8,13) (2,4,10) (2,7,9)
```

## Assumptions and scope

A partial Steiner triple system is a set of 3-element subsets (blocks) of a finite point set in which each unordered pair of points occurs in at most one block. A partial parallel class is a subfamily of pairwise disjoint blocks. The maximum partial parallel class is the largest such subfamily. Thus the claim is finite and concerns the exact parameter pair \((\rho,v)=(4,16)\). It does not assert that 34 is the exact maximum.

## Proof

Every block contributes three unordered point-pairs. The accompanying checker verifies directly that the listed 34 blocks are distinct, all lie in \(V\), and no pair occurs twice; it therefore verifies the partial Steiner triple system condition and counts 102 distinct pairs.

The four blocks

\[
(1,4,12),\quad (8,9,10),\quad (0,6,15),\quad (3,5,7)
\]

are pairwise disjoint. Hence the maximum partial parallel class has size at least 4.

For the upper side of that equality, the checker examines every one of the \(\binom{34}{5}=278256\) five-block subfamilies and finds no five pairwise disjoint blocks. Consequently the maximum partial parallel class has size at most 4, and hence exactly 4. This finite exhaustive check is exact: each possible five-block subfamily is inspected, and five disjoint triples exist if and only if one of those subfamilies has 15 distinct vertices.

Finally, in any partial Steiner triple system on 16 points, a point lies in at most \(\lfloor15/2\rfloor=7\) blocks, since blocks through that point use disjoint pairs among the other 15 points. If there are \(B\) blocks, summing point-degrees gives \(3B\le16\cdot7=112\), so \(B\le\lfloor112/3\rfloor=37\). Combining this general upper bound with the explicit construction proves \(34\le\beta(4,16)\le37\).

## Verification

The standalone `verify.py` uses only Python's standard library. It checks block uniqueness, all 102 point-pairs, the degree sequence, the explicit four-block partial parallel class, and all 278256 five-block subfamilies. Its output is included as `verification_output.txt`. The exhaustive finite check proves the stated property of this specific family; it does not prove an upper bound of 34 for arbitrary partial Steiner triple systems.

## Relationship to prior work

Stinson defines \(\beta(\rho,v)\) and gives general construction and counting bounds for partial Steiner triple systems. At \((4,16)\), those general constructions do not supply this 34-block family. The closest searched record, `2026/9/9/SCOPE045`, gives two 33-block witnesses and the general 37-block ceiling, explicitly leaving 34–37 unresolved. The present family is a distinct 34-block witness and therefore improves the lower bound, but it neither determines the exact extremal value nor classifies all extremal systems.

Demirkale, Donovan and Grannell enumerate maximum partial triple systems on 16 points and report structural statistics, but their inspected text does not tabulate maximum partial parallel class sizes or give this 34-block witness. The result is an explicit finite construction, not a claim about a new general theorem for all \(v\) or \(\rho\).

## Limitations

The exact value of \(\beta(4,16)\) remains in \(\{34,35,36,37\}\). No upper bound below 37 and no isomorphism classification are proved. The result does not claim uniqueness of the construction, optimality of any search procedure, or bibliographic uniqueness beyond the sources and database queries recorded in the review. The finite verifier establishes only the stated finite witness and elementary counting bound. Independent audit and independent validation have not been performed.

## References

1. D. R. Stinson, *On partial parallel classes in partial Steiner triple systems*, arXiv:2007.11033v1 (first submitted 2020-07-21), especially the definition of \(\beta(\rho,v)\), Theorems 2.4 and 3.2, and Theorem 4.1.
2. F. Demirkale, D. Donovan and M. Grannell, *Enumerations of maximum partial triple systems on 16 and 17 points*, arXiv:1708.07646v1 (first submitted 2017-08-25), especially the abstract and the enumeration of maximum partial triple systems on 16 points.
3. published-finding corpus record `2026/9/9/SCOPE045`, *Full-parallel-class-free packings on 16 points: beta(4,16) in [33,37] with two non-isomorphic 33-triple witnesses*.
