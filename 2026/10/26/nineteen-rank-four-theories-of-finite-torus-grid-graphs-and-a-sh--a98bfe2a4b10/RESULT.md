# Nineteen rank-four theories of finite torus-grid graphs and a sharp 64-vertex bound

## Finding

Let \(C_t\) be the simple undirected cycle on \(t\ge3\) vertices, and let \(T_{m,n}=C_m\square C_n\), for integers \(m,n\ge3\), be its Cartesian graph product. Let \(a=\min(m,n)\) and \(b=\max(m,n)\). In first-order logic with equality and the undirected adjacency relation only, two members of this family satisfy exactly the same sentences of quantifier rank at most four if and only if their keys in the following table coincide.

| Smallest dimension \(a\) | Distinct values of the key's second component, determined by \(b\) | Number of classes |
| --- | --- | ---: |
| \(a=3\) | \(3,4,5,6,7,\ge8\) | 6 |
| \(a=4\) | \(4,5,6,7,\ge8\) | 5 |
| \(a=5\) | \(5,6,\ge7\) | 3 |
| \(a=6\) | \(6,7,\ge8\) | 3 |
| \(a=7\) | One key for all \(b\ge7\) | 1 |
| \(a\ge8\) | One key for all \(b\ge a\) | 1 |

Keys belonging to *different rows* of the table are distinct, as are the listed buckets within each row. Thus this infinite family has exactly **19** rank-four theories. Every theory has a representative with at most **64** vertices, and that number is sharp within this family: the class of \(T_{8,8}\) has no smaller torus-grid representative. In particular, all \(T_{m,n}\) with \(m,n\ge8\) are rank-four equivalent, although the cycles \(C_8\) and \(C_{11}\) themselves are *not* rank-four equivalent.

## Assumptions and scope

The vertex set is \(\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\). Two distinct vertices are adjacent precisely when one coordinate is equal and the other differs by \(1\) or \(-1\) in its cyclic group. Dimensions are unordered because the two factors can be interchanged. No root, orientation, colors, coordinate projections, or other predicates are named. Equivalence means agreement on *all* first-order sentences in this signature of quantifier rank at most \(4\); it does not mean graph isomorphism or agreement in counting logic.

## Proof

**1. Reduction to 45 finite cases.** Brown and Hoshino's cycle-game theorem [1, Theorem 4.9, p. 211] states that, for all cycle orders \(s,t\ge3\), the four-round Ehrenfeucht–Fraïssé game has a Duplicator win precisely if \(s=t\) or both \(s,t\ge11\). It follows that \(C_t\equiv_4 C_{\min(t,11)}\).

If Duplicator can win four-round games on \(A\) versus \(A'\) and \(B\) versus \(B'\), Duplicator also wins on \(A\square B\) versus \(A'\square B'\): when Spoiler plays a vertex of a product, respond using the two factor strategies coordinatewise. The factor strategies preserve both equality and adjacency among every pair of selected coordinate values. Cartesian-product adjacency is the Boolean combination
\[
((x_1=y_1)\land E(x_2,y_2))\lor(E(x_1,y_1)\land(x_2=y_2)),
\]
so the combined replies preserve equality and graph adjacency as required. Hence every \(T_{m,n}\) is rank-four equivalent to \(T_{\min(m,11),\min(n,11)}\). Factor interchange reduces the possibilities to exactly \(45\) pairs \(3\le m\le n\le11\).

**2. An exact rank-four type recurrence.** For any finite graph \(G\), any ordered tuple \(\bar v\) (repetitions allowed), and any nonnegative integer \(r\), define
\[
\tau_0^G(\bar v)=\operatorname{atdiag}_G(\bar v),\qquad
\tau_{r+1}^G(\bar v)=\left(\operatorname{atdiag}_G(\bar v),\{\tau_r^G(\bar v,w):w\in V(G)\}\right).
\]
The atomic diagram specifies every equality and adjacency among the tuple entries. Structural induction on formulas shows that \(\tau_r^G(\bar v)\) determines, and is determined by, the truth values of all first-order formulas of quantifier rank at most \(r\) on that tuple: the atomic basis handles rank zero; Boolean combinations preserve the assertion; an existential quantifier records the presence of a matching extension type, and a universal quantifier is handled by negation. In particular, two graphs are rank-four equivalent if and only if their empty-tuple \(\tau_4\) types agree.

Each \(T_{m,n}\) is vertex-transitive by coordinate translations, so the empty-tuple \(\tau_4\) type is determined by \(\tau_3\) at the vertex \((0,0)\). The first implementation in `verify.py` computes this type by enumerating the following exact data: for each ordered triple beginning at \((0,0)\), its atomic equality/adjacency diagram and the **set of all** equality/adjacency extensions by a fourth vertex; for each ordered pair beginning at \((0,0)\), the set of corresponding triple types; and, finally, the set of these pair types. The quadruple extension set is encoded by a 64-bit incidence mask; this compression is lossless because a fourth vertex has exactly six relevant binary tests against the three selected coordinates (three equalities and three adjacencies). Every vertex, including repeated selections, is considered.

The second implementation generates the entire twelve-bit atomic diagram of each ordered quadruple independently from a cyclic-generator edge list, then forms nested sets of quadruple, triple, and pair types. Every nonempty set of four-vertex extensions already fixes its three-vertex prefix, so this second representation is equivalent to the recurrence above. Both are finite, exhaustive implementations of the explicit definition, not heuristic graph invariants.

**3. Exact finite classification.** Both implementations calculate all \(45\) canonical graph types and yield identical partitions into exactly \(19\) nonempty classes. The file `classification.json` lists every canonical pair in its class; `verify.py` checks the partition against that complete table and against the condensed six-row formula stated above. In particular it checks, rather than assumes, that no types from different rows coincide. Combining this finite equality/inequality certificate with Step 1 proves the table for every pair of integer dimensions, not merely the computed orders.

**4. Sharpness.** The largest least-order canonical representative in the table is \(T_{8,8}\), of order \(64\). Its class consists exactly of the canonical pairs with both dimensions at least eight. If any noncanonical torus-grid graph of fewer than \(64\) vertices belonged to this class, truncating its dimensions at \(11\) would give a canonical representative in the same class with no more vertices, contradicting the exhaustively computed canonical minimum \(64\). This proves optimality within the family.

## Verification

Place `verify.py` beside `classification.json` and execute `python3 verify.py` using Python 3 and its standard library. It performs two independent finite atomic-diagram classifications of all \(45\) dimension pairs, checks the explicit class table, verifies that there are exactly \(19\) classes, and calculates the sharp \(64\)-vertex representative bound. Six additional larger parameter pairs test the stability predictions but are **not used** as proof of the infinite reduction. The recorded output is in `verification_output.txt`:

```text
FINITE_CENSUS_OK canonical_pairs=45 classes=19 implementations=2
CUTOFF_TABLE_OK 3:8 4:8 5:7 6:8 7:7 8+:8+
SHARP_BOUND_OK largest_least_representative=64 graph=C8_square_C8
SUPPLEMENTAL_OK instances=6
VERIFY_OK
```

The finite proof certificate is the full deterministic type recurrence and the embedded explicit parameter table; a success log by itself is not the proof.

## Relationship to prior work

Brown and Hoshino [1] determine exact game equivalence for a *pair of cycles*, and thereby supply the dimension-\(11\) bound in Step 1. Their result does **not** classify Cartesian products of two cycles: in particular it does not imply the \(19\) cross-parameter classes or the product threshold \(8\). The graph family and its usual product structure are documented by Weisstein [2], which discusses graph-theoretic and embedding properties, not rank-four logical equivalence. The distinct object and finite-type computations here give the additional information needed beyond the cycle theorem and product-game preservation.

## Limitations

Only finite, loopless, unmarked Cartesian products of **two** undirected cycles and first-order quantifier rank at most \(4\) are classified. The theorem does not address higher quantifier ranks, richer signatures, toroidal quotients with a twist, or products of three or more cycles. The \(64\)-vertex bound is optimal among members of the stated family, not among arbitrary finite graphs. The literature comparison is not a proof of absolute historical novelty; unindexed or inaccessible earlier work might contain equivalent coverage.

## References

[1] J. I. Brown and R. Hoshino, “The Ehrenfeucht–Fraïssé Game for Paths and Cycles,” *Ars Combinatoria* **83** (2007), 193–212. Published April 30, 2007. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf

[2] E. W. Weisstein, “Torus Grid Graph,” *MathWorld*, Wolfram Research. https://mathworld.wolfram.com/TorusGridGraph.html
