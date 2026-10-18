# A sharp eight-point threshold for \(C^2\) on two equivalence relations

## Finding

For finite **nonempty** structures \((X,E,F)\) in the signature of two *named* equivalence relations, the least cardinality at which two nonisomorphic structures can satisfy exactly the same sentences of two-variable first-order logic with counting, \(C^2\), is **eight**. Every structure on at most seven elements is distinguished from every nonisomorphic such structure, regardless of the cardinality of the comparator.

At cardinality eight, there are exactly **3,017** isomorphism types and **3,016** distinct \(C^2\)-equivalence classes: one class of size two and 3,015 singleton classes. The unique exceptional pair corresponds to the incidence multigraphs \(C_8\) and \(C_4\sqcup C_4\), with named sides. Each incidence edge is one element of \(X\); sharing the first or second endpoint defines \(E\) or \(F\), respectively.

## Assumptions and scope

Here \(E\) and \(F\) are separately interpreted reflexive, symmetric, transitive binary relations. They may coincide or have nontrivial intersection. Their names cannot be exchanged by an isomorphism. \(C^2\) permits equality, Boolean operations, arbitrary counting quantifiers, and only two reusable variables. Logical comparison is **within the class of finite structures in which both relations are equivalences**; no claim is made about arbitrary relational structures. Empty structures are excluded, but allowing one would not change the first failure because cardinality is \(C^2\)-definable.

Let the \(E\)-classes be \(R_1,\ldots,R_r\) and the \(F\)-classes \(S_1,\ldots,S_s\). Associate the nonnegative integral matrix \(M=(m_{ij})\), where \(m_{ij}=|R_i\cap S_j|\). Every row and column is nonzero and \(\sum_{i,j}m_{ij}=|X|\). The isomorphism type is exactly the orbit of \(M\) under *independent* row and column permutations. Parallel edges in the associated bipartite multigraph encode intersections of size greater than one.

## Proof

**Step 1 — a complete enumeration space.** Starting with the one-cell matrix \((1)\), obtain every matrix of weight \(n+1\) from a matrix of weight \(n\) by one of four operations: increment an existing cell; add a new row with one unit in an existing column; add a new column with one unit in an existing row; or append a new row and a new column meeting in one unit. Conversely, deleting any one element of a two-equivalence structure yields exactly such an operation in reverse. Therefore this recursion generates representatives of *all* isomorphism types at each weight.

For canonicalization, put columns in ascending column-sum order (this order is invariant under isomorphism), freely permute columns inside equal-sum groups, sort rows lexicographically, and take the lexicographically minimum outcome **subject to this fixed column-sum order**. This is a unique orbit representative under arbitrary independent row and column permutations, though not necessarily the unrestricted lexicographic minimum. Thus deduplicating these canonical matrices neither identifies nonisomorphic structures nor misses any structure.

**Step 2 — a complete logical signature.** Initialize every element with one color. Given a color \(c_t\), assign to an element \(x\) the new color determined by its old color together with all counts
\[
N_t(x;a,b,d)=\bigl|\{y\in X: [E(x,y)]=a,\ [F(x,y)]=b,\ c_t(y)=d\}\bigr|,
\]
where \(a,b\in\{0,1\}\), and \([P]\) denotes the indicator of \(P\). Colors are defined *jointly* across all compared structures, not renamed independently inside each structure. The diagonal \(y=x\) is recognizable as one designated element of the \((a,b)=(1,1)\) class having color \(c_t(x)\), so explicit equality adds no missing coordinate. By the standard two-variable counting-logic/color-refinement correspondence (and directly by induction over formulas and refinement rounds), two finite structures have the same \(C^2\) sentences if and only if their stable color multisets agree. The possible counts are finite and distinguishable using counting quantifiers. Termination follows because color classes only split and the disjoint union is finite.

**Step 3 — certified finite classification.** The accompanying standalone `verify.py` implements Steps 1 and 2 using exact integer matrices, global synchronized refinement, and no third-party dependencies. It computes the following complete table; the final column counts non-singleton logical classes:

| \(|X|\) | Isomorphism types | \(C^2\)-classes | Non-singleton classes |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 |
| 2 | 4 | 4 | 0 |
| 3 | 10 | 10 | 0 |
| 4 | 33 | 33 | 0 |
| 5 | 91 | 91 | 0 |
| 6 | 298 | 298 | 0 |
| 7 | 910 | 910 | 0 |
| 8 | 3017 | 3016 | 1 |

It also verifies that the lone non-singleton class consists of exactly the following two canonical intersection matrices, written with named row and column sides:
\[
A=\begin{pmatrix}
0&0&1&1\\0&0&1&1\\1&1&0&0\\1&1&0&0
\end{pmatrix},\qquad
B=\begin{pmatrix}
0&0&1&1\\0&1&0&1\\1&0&1&0\\1&1&0&0
\end{pmatrix}.
\]

In \(A\) the associated bipartite graph has two four-cycle components; in \(B\) it is one eight-cycle. Hence they are not isomorphic, even without respecting the named sides. In both structures each element has exactly one other \(E\)-equivalent element, exactly one other \(F\)-equivalent element, and no *other* element equivalent for both relations. Every element therefore has the same initial relation-count profile \((1,1,1,5)\) for the four pairs \((E,F)=(1,1),(1,0),(0,1),(0,0)\). All later colors remain uniform, proving their \(C^2\)-indistinguishability without relying on the exhaustive computation.

The computed absence of collisions through order seven and uniqueness at order eight completes the proof. In addition to the main recursion, the verifier separately enumerates *pairs of labeled set partitions* through order five and checks agreement with canonical matrix counts. The entire isomorphism-count column also matches the independently established sequence OEIS A007716 (this known column is **not** claimed as new).

## Verification

Run `python3 verify.py` with an ordinary Python 3 interpreter. The program regenerates each canonical matrix family, computes joint color-refinement histograms, and asserts all table entries and the two exact witness matrices. Its output ends with `VERIFIED: full sharp C2 threshold and unique first pair`. A full local execution succeeded. All computations use exact integers; no probabilistic assumptions, timeouts treated as proofs, or external enumerator data are required. The rigorous guarantee is relative to the elementary exhaustiveness and canonicalization arguments above, not merely the agreement of printed counts.

## Relationship to prior work

Kiefer, Schweitzer and Selman (arXiv:1503.08792v1, March 2015) give a general characterization of finite relational structures identified by \(C^2\), including a structural classification and algorithm (their Theorem 27 and Corollary 29). This provides the appropriate global background for logical identification but does not enumerate the restricted two-equivalence class through eight elements or state this threshold and unique pair in the inspected text. This finding is therefore a **small-order specialization with an exact new layer**, not a new general criterion for \(C^2\).

Pratt-Hartmann (2015, DOI 10.1002/malq.201400102, especially Section 7) studies the much broader satisfiability problem with two equivalence relations and establishes undecidability in an enriched signature; that result does not determine these exact isomorphism/refinement numbers. OEIS A007716, with contributions predating 2016, records the already-known total number of matrix-orbit types (3,017 at weight eight) without the \(C^2\)-partition of them. The split between 3,017 isomorphism types and 3,016 \(C^2\)-types, and its unique witness, is the specific classification addressed here.

## Limitations

The sharp bound concerns two **named equivalences and no additional predicates**. Adding unary predicates, fixing individual elements, imposing connectedness of the incidence graph, or using a stronger logic can change the result. The \(C^2\)-collision is witnessed among finite equivalence structures; this is not a classification of arbitrary two-relation structures. The finite census is supported by a fully reproducible exact program, not by a short independent hand enumeration of all 3,017 types. Novelty remains subject to obscure or unindexed prior small-order tabulations and to human literature review; independent audit has not been performed.

## References

1. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, first public arXiv version March 30, 2015, arXiv:1503.08792v1, https://arxiv.org/abs/1503.08792.
2. I. Pratt-Hartmann, *The two-variable fragment with counting and equivalence*, *Mathematical Logic Quarterly* **61** (2015), 474–515, DOI:10.1002/malq.201400102, https://onlinelibrary.wiley.com/doi/10.1002/malq.201400102.
3. OEIS A007716, matrix orbits under separate row and column permutations, https://oeis.org/A007716 (the total-count sequence, not the logical-refinement classification).
