# Exact quadratic modal-depth spectrum of the finite Erdős–Tarski staircase

## Finding

**Theorem (exact depth filtration).** For every integer \(n\ge 2\), let \(G_n=[n]\times[n]\) be a bimodal Kripke frame with two named equivalence relations: \(R\) relates cells in the same row and \(C\) relates cells in the same column. Give it just one propositional letter \(p\), with
\[
G_n,(i,j)\models p\quad\Longleftrightarrow\quad i\le j.
\]
Let \(\mathcal D_t(n)\) be the Boolean algebra of subsets of \(G_n\) definable by formulas of basic bimodal logic over \(p\) with modal nesting depth at most \(t\). Then, for every integer \(t\ge0\),
\[
\boxed{
\log_2|\mathcal D_t(n)|=
\begin{cases}
(t+1)^2+1,&0\le t\le n-2,\\
n^2,&t\ge n-1.
\end{cases}}
\]
In particular, **exactly \(n-1\) modal rounds are necessary and sufficient to distinguish all \(n^2\) worlds**. At that depth every singleton is definable, and \(\mathcal D_{n-1}(n)=\mathcal P(G_n)\). At each earlier depth at least two worlds satisfy precisely the same formulas.

For example, on the \(5\times5\) staircase the exact number of modal types at depths \(0,1,2,3,4\) is \(2,5,10,17,25\); the corresponding numbers of definable subsets are \(2^2,2^5,2^{10},2^{17},2^{25}\). The novelty claim concerns **the quantitative depth filtration and sharp depth threshold**, not the previously known single-generator construction.

## Assumptions and scope

The frame is finite and nonempty, with both relations reflexive, symmetric and transitive. Formula constructors are the one atom \(p\), Boolean connectives, and \(\Box_R,\Box_C\) (equivalently their diamonds). Modal depth is the maximum nesting count of either box or diamond. There are no nominals, counting operators, fixed points, converse relations beyond the two stipulated equivalences, or additional atoms. The square grid and weak inequality \(i\le j\) are essential assumptions; no corresponding rectangular or different-valuation formula is asserted.

All worlds are ordered positions for notation only; neither the logic nor either accessibility relation has a built-in numeric order.

## Proof

**Finite modal types.** Let \(T_t(i,j)\) denote the equivalence class of \((i,j)\) under agreement on all formulas of depth at most \(t\). The depth-zero partition has two classes, according to \(i\le j\). Define the row and column successor signatures
\[
A_t(i)=\{T_t(i,j):1\le j\le n\},\qquad
B_t(j)=\{T_t(i,j):1\le i\le n\}.
\]
Standard one-step modal semantics gives
\[
T_{t+1}(i,j)\equiv
\bigl(T_t(i,j),A_t(i),B_t(j)\bigr).
\]
The partitions induced by \(A_t\) and \(B_t\) refine those induced at earlier depths. Since \(T_0\) records the truth value of \(p\), induction shows the equivalent simpler formula
\[
T_{t+1}(i,j)\equiv
\bigl(\mathbf 1_{i\le j},A_t(i),B_t(j)\bigr).\tag{1}
\]
Indeed \(T_t\) is determined by \(p,A_{t-1},B_{t-1}\), and the latter two signatures are determined by their refinements \(A_t,B_t\). Conversely, the first entry in the original one-step signature determines the truth of \(p\).

**Exact row/column blocks.** For \(0\le t\le n-1\) set
\[
\ell_R(t)=\lfloor t/2\rfloor+1,\quad
u_R(t)=\lceil t/2\rceil,\quad
\ell_C(t)=\lceil t/2\rceil,\quad
\nu_C(t)=\lfloor t/2\rfloor+1.
\]
We claim that equality of \(A_t\)-signatures partitions the row indices into singleton classes for the first \(\ell_R(t)\) and last \(\nu_R(t)\) rows, plus (if nonempty) one single middle class of all other rows. Equality of \(B_t\)-signatures partitions the column indices analogously, with the first \(\ell_C(t)\) and last \(\nu_C(t)\) columns singled out.

For \(t=0\), the first row is entirely \(p\)-true and all other rows contain both truth values; dually the last column is entirely true and all earlier columns have both values. This is exactly the claimed partition.

Assume the partition claim at depth \(t<n-1\). By (1), the set \(A_{t+1}(i)\) distinguishes row blocks already distinguished at depth \(t\). Within a middle row block, it is determined by the set of \(p\)-truth values present in the intersection of that row with each column block; the singleton column blocks outside the middle all have a constant \(p\)-value independent of the row.

If \(t=2s\), the two middle index intervals, where present, are
\[
M_R=[s+2,n-s],\qquad M_C=[s+1,n-s-1].
\]
Every row in \(M_R\) except the final row \(n-s\) meets \(M_C\) in both \(p\)-colors, while the final row meets it only in \(\neg p\). Hence exactly that last middle row splits off. Dually the first middle column \(s+1\) splits off, being monochromatically \(\neg p\) against \(M_R\).

If \(t=2s+1\), both middle intervals are
\[
M_R=M_C=[s+2,n-s-1].
\]
The first middle row \(s+2\) sees only \(p\) in the middle columns, whereas every later middle row sees both colors. Thus the first middle row splits off. Dually the final middle column splits off, seeing only \(p\) against the middle rows. When a middle interval has at most one point, the asserted singleton partition is already complete. No older singleton blocks can merge, since one-step signatures retain their old row/column tags. This proves the block description inductively through \(t=n-1\).

**Counting types.** At depth \(t\ge1\), equation (1) with signatures from depth \(t-1\) makes the modal partition the partition by row block, column block, and color. For \(1\le t\le n-2\), there are exactly \(t+1\) row blocks and \(t+1\) column blocks. Each of their \((t+1)^2\) Cartesian rectangles is monochromatic except the middle-row-block by middle-column-block rectangle, which contains both \(p\)-colors. (The two middle index intervals overlap sufficiently to contain an equality pair and a strictly reversed pair because their lengths are at least two in this range.) Exactly this one rectangle splits into two modal types. The number of types is therefore \((t+1)^2+1\). The same formula gives \(2\) at \(t=0\).

At depth \(n-1\), the depth-\((n-2)\) row and column signature partitions each have \(n\) singleton blocks, so (1) distinguishes all \(n^2\) ordered pairs. Subsequent refinement cannot create further classes.

**Boolean algebra and optimality.** On any finite Kripke model, the depth-\(t\) modal types are each definable by a depth-\(t\) characteristic formula. Inductively, a type formula asserts its depth-\((t-1)\) type and, for each of the two modalities, asserts exactly the set of depth-\((t-1)\) successor types using a conjunction of diamonds and a single box over their disjunction. Hence every union of the \(r_t\) depth-\(t\) types is definable, and two points in the same type cannot be separated at that depth. Thus \(|\mathcal D_t(n)|=2^{r_t}\). For \(t=n-2\), \(r_t=(n-1)^2+1<n^2\), while for \(t=n-1\), \(r_t=n^2\). This proves both the cardinality formula and the sharp minimal depth.

For an additional explicit (though not depth-optimal) description of the known one-generator property, put \(H_0=V_0=\bot\) and recursively
\[
H_k=\Box_R(p\lor V_{k-1}),\qquad
V_k=\Box_C(\neg p\lor H_k),\quad 1\le k\le n.
\]
Then \(H_k\) holds on precisely rows \(1,\ldots,k\), and \(V_k\) on precisely columns \(1,\ldots,k\). Consequently \((H_i\land\neg H_{i-1})\land(V_j\land\neg V_{j-1})\) defines the singleton \((i,j)\). These selectors corroborate generation, whereas the type-count proof yields the strictly sharper minimal depth.

## Verification

Run the standalone Python 3 standard-library program `VERIFIER.py` with `python3 VERIFIER.py`. Its deterministic tests independently (i) compute depth-wise two-modal bisimulation partitions and compare the exact quadratic type counts and row/column block descriptions for all square sizes \(2\le n\le60\); (ii) evaluate the explicit row and column selectors directly for \(1\le n\le30\); and (iii) separately enumerate all Boolean unions of current modal atoms and both box operations for \(n=2,3,4\), reconstructing the full depth-bounded definable Boolean algebras without invoking the bisimulation recurrence. The third test examines 1,100 Boolean unions. Its successful output is recorded in `VERIFICATION.md`.

Finite checks verify finite instances, not the all-size statement; the induction above supplies that proof.

## Relationship to prior work

Bezhanishvili and Meadors, in their 2023 preprint (journal publication 2024), prove a coloring theorem for generated algebras (Theorem 5.8) and identify the infinite Erdős–Tarski algebra as singly generated by an **upper-triangular coloring** (Example 5.10 and Theorem 5.13). **Neither one generation nor the staircase valuation is claimed as novel.** Their results do not give the exact depth-indexed number of finite modal types or the sharp \(n-1\) stabilization threshold calculated here.

Figallo and Mónica-Gomes (2023) provide a characterization of subalgebras of finite diagonal-free two-dimensional cylindric algebras (Lemma 6 and Lemma 7). Those order-theoretic statements classify final subalgebra structure; the present claim concerns the additional stratification by **modal depth for a fixed marked generator**, with its explicit quadratic rank sequence. Standard partition-refinement and characteristic-formula principles are used, not claimed as new.

## Limitations

No result is claimed for arbitrary binary valuations, nonsquare rectangular grids, additional accessibility structures, or formula length. The upper triangle and exact two named S5 equivalences are fixed. The depth profile is a bound on nesting depth, not on the number of symbols in a shortest cell-defining formula. A hidden antecedent in algebraic-logic or automata literature cannot be excluded by a literature search; there has been no independent mathematical audit.

## References

- Guram Bezhanishvili and Chase Meadors, *Local finiteness in varieties of MS4-algebras*, arXiv:2312.16754v1, first submitted 28 December 2023; *Journal of Symbolic Logic*, DOI: 10.1017/jsl.2024.89. Especially the coloring theorem, Example 5.10, and Theorem 5.13. https://arxiv.org/abs/2312.16754
- Martín Figallo and Claudia Mónica-Gomes, *The Subalgebra Lattice of A Finite Diagonal-Free Two-Dimensional Cylindric Algebra*, *Computación y Sistemas* 27(1) (2023), pp. 327–333, DOI: 10.13053/CyS-27-1-4544. https://cys.cic.ipn.mx/index.php/CyS/article/view/4544
- Robert Paige and Robert E. Tarjan, *Three Partition Refinement Algorithms*, *SIAM Journal on Computing* 16(6) (1987), 973–989, DOI: 10.1137/0216062. This is general algorithmic background only; it does not state the staircase-specific modal-depth law.
