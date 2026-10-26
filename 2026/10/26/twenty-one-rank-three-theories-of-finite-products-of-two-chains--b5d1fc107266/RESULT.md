# Twenty-one rank-three theories of finite products of two chains

## Finding

For every two positive integers \(a,b\), let \(P_{a,b}\) be the partially ordered set \(\{1,\ldots,a\}\times\{1,\ldots,b\}\), with \((i,j)\preceq(k,\ell)\) if and only if \(i\leq k\) and \(j\leq\ell\). Use the first-order language with the **single** reflexive binary relation \(\preceq\) and equality; the two coordinates, endpoints, cover relation, meet and join are not named.

**Theorem.** As \(a,b\) range over all positive integers, there are exactly **21** equivalence classes of the structures \(P_{a,b}\) under agreement on first-order sentences of quantifier rank at most three. A complete classification follows by setting \(\alpha=\min\{\min(a,b),7\}\) and \(\beta=\min\{\max(a,b),7\}\), and reading the class number from the triangular table below. The 21 labels represent pairwise different rank-three theories; equal labels are equivalent.

| \(\alpha\) | \(\beta\) and class label |
|---|---|
| 1 | 1:1, 2:2, 3:3, 4:4, 5:6, 6:7, 7:9 |
| 2 | 2:5, 3:8, 4:10, 5:12, 6:13, 7:13 |
| 3 | 3:11, 4:14, 5:15, 6:17, 7:17 |
| 4 | 4:16, 5:18, 6:19, 7:19 |
| 5 | 5:20, 6:21, 7:21 |
| 6 | 6:21, 7:21 |
| 7 | 7:21 |

Every class has a representative with at most **30 elements**; this bound is sharp within the family. The unique class whose smallest representative has 30 elements is class 21, represented by \(P_{5,6}\), and it also includes \(P_{5,7}\), \(P_{6,6}\), \(P_{6,7}\), and \(P_{7,7}\). In particular, \(P_{5,6}\equiv_3P_{7,7}\) in the indicated order language.

## Assumptions and scope

The orders are finite and nonempty: \(a,b\in\mathbb Z_{\geq1}\). The order relation is reflexive. Quantifier rank is the maximum number of quantifiers on any nested branch of a first-order formula; Boolean combinations do not increase it. Distinct sentences are compared over the original single-relation structures, without additional predicates or parameters. Coordinate transposition yields \(P_{a,b}\cong P_{b,a}\).

The same structures are canonically the divisibility posets of all positive divisors of an integer having at most two distinct prime factors, with two exponent ranges of lengths \(a\) and \(b\), including exponents zero. The classification is a statement about their partial order, **not** about their cardinality or numbers of order-preserving maps.

## Proof

**Step 1: three-round saturation of finite chains.** Let \(C_t\) denote a reflexively linearly ordered set with \(t\geq1\) elements. The duplicator wins the three-round Ehrenfeucht–Fraïssé game between \(C_s\) and \(C_t\) whenever \(s=t\), or both \(s,t\geq7\). Here is a direct invariant. With \(r\) moves remaining, corresponding open intervals determined by previously chosen points, including the left and right end gaps, have equal unchosen cardinalities or both have at least \(2^r-1\) unchosen points. It holds initially because \(r=3\). If the spoiler selects a point in a corresponding interval of unequal large sizes, the duplicator replies so that each of the two new subintervals has either the same small number of points on both sides or at least \(2^{r-1}-1\) on both sides. Such a choice always exists, since \(2^r-1=2(2^{r-1}-1)+1\). When the interval sizes agree, copy the relative position. The invariant maintains all equality and order comparisons. At \(r=0\), partial isomorphism follows. This argument also covers already selected points and repeated moves.

**Step 2: product game reduction.** If \(C_a\equiv_3 C_c\) and \(C_b\equiv_3 C_d\), run the two duplicator strategies in parallel on the corresponding coordinates. At every round, choosing \((i,j)\) in one product is answered by the pair of coordinate responses in the other. Equality of product elements is the conjunction of the two coordinate equalities; product order is the conjunction of the two coordinate orders. Therefore the resulting correspondence is a partial isomorphism in the product language after every move. Thus
\[
P_{a,b}\equiv_3P_{\min(a,7),\min(b,7)},
\]
where reduction first uses an isomorphism to interchange the coordinates if necessary. Hence it suffices to classify the 28 canonical unordered pairs of lengths in \(\{1,\ldots,7\}\).

**Step 3: complete rank-three invariant and finite classification.** For a finite poset \(P\), write \(D_0(x,y,z)\) for the full atomic diagram of an ordered triple, including equality and all comparisons for each pair. Recursively set
\[
D_1(x,y)=\{D_0(x,y,z):z\in P\},\qquad
D_2(x)=\{D_1(x,y):y\in P\},\qquad
D_3(P)=\{D_2(x):x\in P\}.
\]
These are exact finite objects, not hash codes or frequency approximations. Two finite structures satisfy the same sentences of rank at most three exactly when their \(D_3\) objects agree. To prove this, an atomic diagram describes a rank-zero tuple type; at each recursive stage the set of extensions records both the possible existential witnesses and the prohibition of any other extension type. Induction produces a characteristic first-order formula of the corresponding rank, with universal conditions expressing the latter prohibition. Conversely, equality of the type sets gives the duplicator a response to every challenge. This is the finite-type Ehrenfeucht–Fraïssé theorem.

The accompanying self-contained `verify.py` computes \(D_3\) for every one of the 28 canonical rectangles. It implements each atomic triple diagram both as a three-pair four-valued comparison vector and independently as a full nine-entry Boolean relation matrix. Although the encodings differ, the two implementations' complete equality partitions among the 28 models agree, yielding **21** classes, exactly the table in the Finding section. The checker also performs direct three-round, two-sided game recursion for 64 ordered pairs among eight small models, yielding the same equivalences. All 21 computed signatures are pairwise distinct, so the characteristic-formula argument supplies a rank-at-most-three distinguishing sentence for each pair of classes (the individual expanded sentences need not be printed). This finite enumeration is exhaustive for the 28 canonical models.

**Step 4: sharp size.** The minimum representatives of classes 1 through 21, in order, have dimensions
\[
(1,1),(1,2),(1,3),(1,4),(2,2),(1,5),(1,6),
(2,3),(1,7),(2,4),(3,3),(2,5),(2,6),(3,4),
(3,5),(4,4),(3,6),(4,5),(4,6),(5,5),(5,6).
\]
The largest product of two entries on this list is \(5\cdot6=30\); the next largest is 25. The canonical table identifies every possible class of every larger grid by Step 2. To see that class 21 has no representative with fewer than 30 points, note that any such grid with its shorter side at least five must be \(P_{5,5}\), which is class 20; if its shorter side is at most four it has one of classes 1 through 19 by the table. Thus no grid of size less than 30 has class 21. This proves both the complete classification and sharp bound.

## Verification

Run `python3 verify.py` with Python 3 and the standard library; no input files are required. The included `verification_output.txt` records the exact triangular class table, all 21 least representatives, agreement of two independent atomic encodings on all 28 canonical models, checks on ten additional grids exceeding a coordinate size of seven (up to dimensions \(11\) by \(12\)), and 64 direct three-round game tests. The program terminates with `VERIFY_OK`. The infinite reduction in Steps 1–2 is a mathematical proof, not an inference from the finite tests. The code is an exact finite certificate of Step 3 and the representative-size computation.

## Relationship to prior work

The Ehrenfeucht–Fraïssé game theorem and characteristic-type recurrences are standard; see Otto's *Finite Model Theory* notes (2016), Section 2.1, especially Theorem 2.1.7, Lemma 2.1.8 and Exercise 2.1.11. The Feferman–Vaught work on products of structures (1959) and Makowsky's 2004 survey give powerful general product methods; the exact 21-class rank-three table for the order reduct of two-chain products, including the class-21 collapse and the sharp 30-element bound, was not located in the inspected material. Yuguo He's 2014 study of quantifier-structure hierarchies concerns a distinct logical hierarchy and supplies general finite-model context, not this rectangular-poset classification.

The same rectangles admit a divisor-lattice description, but a result about the number of morphisms, the FO theories of a graph built on a rectangular vertex set, or the FO theories of Boolean hypercubes would not by itself imply the present single-order-relation classification. The table is derived from the exact rank-three types above rather than from those other invariants.

## Limitations

The theorem is restricted to two **chains**, all positive lengths, the **pure** order language and **quantifier rank three**. Adding coordinate predicates, cover relations, lattice operations, constants or more quantifier nesting may distinguish classes joined here. The representative bound is optimal **within this family**, not among arbitrary finite posets. The finite verifier cannot replace the separately presented proof of saturation for unbounded parameters. The available historical literature search was not exhaustive: the original Feferman–Vaught article could not be inspected in full, and unindexed equivalent treatments remain possible. Independent scientific validation has not been performed.

## References

1. S. Feferman and R. L. Vaught, “The first order properties of products of algebraic systems,” *Fundamenta Mathematicae* 47 (1959), 57–103. DOI: `10.4064/fm-47-1-57-103`. Bibliographic record and description inspected; the complete primary article was inaccessible.
2. J. A. Makowsky, “Algorithmic uses of the Feferman–Vaught Theorem,” *Annals of Pure and Applied Logic* 126 (2004), 159–213. DOI: `10.1016/j.apal.2003.11.002`. Accessible article text inspected for product methods and grid constructions.
3. Y. He, “On the strictness of the quantifier structure hierarchy in first-order logic,” *Logical Methods in Computer Science* 10(4) (2014), 1–38. Public arXiv v1: 2014-09-26, `arXiv:1409.7488`; full open-access PDF inspected.
4. M. Otto, *Finite Model Theory*, lecture notes (2016), Section 2.1, Theorem 2.1.7, Lemma 2.1.8, Exercise 2.1.11, Example 2.1.13. `https://www2.mathematik.tu-darmstadt.de/~otto/LEHRE/FMT16.pdf`.
