# Catalan maximal commuting families of nuclei on finite Gödel chains

## Finding

Let \(G_n=\{0<1<\cdots<n-1\}\) be the finite Heyting (Gödel) chain, with \(n\geq1\). Let \(\mathcal N_n\) comprise all nuclei \(j:G_n\to G_n\): extensive, monotone, idempotent maps preserving binary meets. For a nucleus, a *fiber* is the inverse image of one of its values. A collection of nonempty intervals is *laminar* if any two are disjoint or one contains the other. A *maximal commuting family* is a subset of \(\mathcal N_n\) whose members commute pairwise under composition and which is maximal by inclusion among such subsets.

**Theorem.** Two nuclei commute exactly when their union of fiber intervals is laminar. Maximal commuting families correspond bijectively to full rooted plane binary trees with leaf order \(0,1,\ldots,n-1\). Specifically, the family attached to a tree contains precisely the nuclei whose fiber partitions are frontier cuts of that tree. Consequently there are exactly

\[
\frac{1}{n}\binom{2n-2}{n-1}
\]

maximal commuting families. If \(q(T)\) is their cardinality, \(q(\mathrm{leaf})=1\) and, for the two child subtrees,

\[
q(T)=1+q(T_L)q(T_R).
\]

The number \(b_n\) of **ordered pairs** of commuting nuclei, including equal pairs, satisfies

\[
b_1=1,\quad b_2=4,\qquad b_{n+2}=4b_{n+1}-2b_n\quad(n\geq1),
\]

and hence

\[
b_n=\frac{(1+\sqrt2)(2+\sqrt2)^{n-1}+(1-\sqrt2)(2-\sqrt2)^{n-1}}2.
\]

For independent uniform nuclei this yields the exact commutation probability \(b_n/4^{n-1}\), asymptotic to

\[
\frac{1+\sqrt2}{2}\left(\frac{2+\sqrt2}{4}\right)^{n-1}.
\]

## Assumptions and scope

Composition is ordinary composition of total self-maps; the direction of functional composition does not affect the commutation relation. The set of all nuclei is labelled by the fixed chain and includes the identity and the constant-top map. The case \(n=1\) is included with one map, one maximal family, and one commuting ordered pair. A full rooted plane binary tree has every internal vertex of degree two and is equipped with the left-to-right leaf order. A *frontier cut* consists of pairwise disjoint node leaf intervals whose union is all leaves, and may contain the root.

## Proof

**1. Fixed-point/interval normal form.** Every monotone map on a chain preserves meets. If \(j\) is a nucleus, its fixed-point set \(S=\{x:j(x)=x\}\) contains the maximum. Extensivity and idempotence force \(j(x)\in S\) and \(j(x)\geq x\), while monotonicity applied to the least fixed point above \(x\) forces

\[
j(x)=\min\{s\in S:s\geq x\}.
\]

Conversely any \(S\) containing the maximum gives such a nucleus. Each fiber is a nonempty contiguous interval ending at its maximum, and each partition of the chain into consecutive blocks determines one nucleus by mapping each block to its right endpoint. There are \(2^{n-1}\) nuclei, one for each set of internal block boundaries.

**2. Exact commutation criterion.** For nuclei \(f,g\), let \(\mathcal B_f,\mathcal B_g\) be their interval-block families. Suppose two blocks cross: \(A=[a,b]\in\mathcal B_f\) and \(B=[c,d]\in\mathcal B_g\), with \(a<c\leq b<d\). The \(g\)-block containing \(a\) ends below \(c\), so \(f(g(a))=b\); meanwhile \(g(f(a))=g(b)=d\), contradiction. The reversed crossing direction is symmetric.

Conversely assume there are no crossings. For each \(x\) its \(f\)-block \(A\) and \(g\)-block \(B\) intersect, so one contains the other. If \(A\subseteq B\), then \(g(f(x))=\max B\). Let \(C\) be the \(f\)-block containing \(\max B\). Laminarity yields either \(C\subseteq B\), so \(\max C=\max B\), or \(B\subseteq C\), in which case \(A\subseteq C\) forces \(A=C\) because distinct \(f\)-blocks are disjoint, and the inclusions imply \(A=B=C\). In both cases \(f(g(x))=f(\max B)=\max B\). The case \(B\subseteq A\) is symmetric. Thus \(fg=gf\). This proves both directions without any reliance on finite experiments.

**3. From maximal commuting families to trees.** Given a commuting family \(F\), unite all its fiber blocks into \(\mathcal H(F)\). By Step 2 this is a laminar collection of intervals. For maximal \(F\), it contains every singleton because the identity nucleus commutes with every map and therefore belongs to \(F\); it contains the whole chain because the constant-top nucleus likewise commutes with every map and belongs to \(F\). For each nonempty interval \(I\), define \(j_I\) to collapse \(I\) to its right endpoint and fix every point outside \(I\). The fibers of \(j_I\) are \(I\) and exterior singletons. If \(I\) is compatible with every interval of \(\mathcal H(F)\), then Step 2 makes \(j_I\) commute with all \(F\); maximality forces \(j_I\in F\) and therefore \(I\in\mathcal H(F)\). Thus \(\mathcal H(F)\) is a maximal laminar family of consecutive intervals.

View inclusion in such a family as a rooted tree: the whole interval is the root, and singleton intervals are its ordered leaves. At any internal interval its inclusion-maximal proper subintervals must partition the parent (all leaf singleton descendants are present). If a parent had at least three children, adjoining the union of the first two consecutive children would preserve laminarity, contradiction. Hence each parent has exactly two children. Conversely the node intervals of a full ordered binary tree are a maximal laminar interval collection: any interval compatible with all nodes must be a node, as can be seen by descending from the root into one child until the interval is exactly a node. Thus full ordered binary trees are exactly the maximal interval hierarchies.

Each tree \(T\) gives the commuting family \(F(T)\) of all nucleus fiber partitions consisting of node intervals forming a cut. It is pairwise commuting by Step 2, and maximal because any nucleus commuting with every block-collapse map \(j_I\) for node intervals \(I\) must itself have all fiber intervals among the tree nodes. Different trees give different families, since \(j_I\in F(T)\) detects every node. Conversely maximality of \(F\) ensures that it contains **every** cut nucleus of \(\mathcal H(F)\), so \(F=F(T)\). This establishes the claimed bijection.

A full binary ordered tree either is a single leaf or splits uniquely into ordered left/right subtrees; the Catalan recurrence \(c_1=1\), \(c_n=\sum_{i=1}^{n-1}c_i c_{n-i}\) yields \(c_n=\binom{2n-2}{n-1}/n\). A cut either selects the root alone or is formed from independent cuts of its two children, giving the stated \(q(T)\) recurrence.

**4. Ordered commuting pairs.** Encode the \(n-1\) positions between consecutive chain points with four boundary states: neither nucleus fixes the lower point, only \(f\) does, only \(g\) does, or both do. The topmost point is fixed by both and closes the final segment. By Step 2, the fiber partitions have no crossing if and only if each run between successive common boundaries (including the initial run) contains exclusive boundaries of at most one type. A run with an \(f\)-only boundary followed by a \(g\)-only boundary, or vice versa, forces two fiber blocks to cross; if no such mixed run exists, all blocks are laminar.

While scanning the \(n-1\) boundary positions left-to-right, let \(a_k\) count valid prefixes whose current run contains no exclusive boundary, and let \(u_k\) count prefixes whose current run has exclusively one of the two types. A `both` symbol resets either state; a `neither` symbol preserves it; a chosen exclusive symbol moves the empty state to the corresponding single-type state; and the opposite exclusive symbol is forbidden from a nonempty state. Consequently

\[
\binom{a_{k+1}}{u_{k+1}}=
\begin{pmatrix}2&1\\2&2\end{pmatrix}\binom{a_k}{u_k},\qquad (a_0,u_0)=(1,0),
\]

and \(b_n=a_{n-1}+u_{n-1}\). The transfer matrix has characteristic polynomial \(t^2-4t+2\). The initial totals \(b_1=1\) and \(b_2=4\) give the recurrence and closed form. Since the second eigenvalue has smaller modulus, division by the \(4^{n-1}\) total ordered pairs of nuclei gives the displayed asymptotic probability.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. The verifier independently enumerates all extensive, isotone, idempotent maps through five chain points; all fixed-point nuclei through nine points; checks both directions of the laminar criterion through nine points; checks the ordered-pair recurrence through nine points; constructs full ordered binary trees and their cut profiles through nine points; and independently enumerates maximal commuting cliques through six points. It prints `VERIFY_OK` on success. Finite exhaustive checks corroborate but do not replace Steps 1–4.

Small cases: for chain sizes \(n=1,2,3,4,5,6\), the numbers of maximal families are \(1,1,2,5,14,42\); the numbers of ordered commuting pairs are \(1,4,14,48,164,560\). For four points the five maximal families have sizes \(4,4,4,4,5\).

## Relationship to prior work

Nuclei and their logical/locale semantics are established; Fellin and Schuster (2021, Section 3) treat nuclei as abstract closure modalities and provide a conservation theorem. The Catalan monoid of all extensive order-preserving maps of a chain is classical, and Sapir and Volkov (2022/2023, Sections 2 and 4) investigate its finite-basis and semigroup properties. In particular **not every Catalan-monoid element is idempotent**, while the present result concerns precisely the idempotent elements and their pairwise commuting families. Margolis and Steinberg (2018, Section 2) give a representation of the entire Catalan monoid via interval-related partial cross-sections and establish an incidence-algebra result, not the maximal commuting-nucleus classification. The Catalan formula for the number of ordered full binary trees is classical; only its new identification with maximal commuting families and the joint pair law are proposed here.

Closely related published results on fixed-point forms of finite-chain preconditionals, monadic Gödel rounding operators, and commuting modal-relation condensations address respectively binary implications, paired adjoint operators, and particular closures on relation spaces, rather than the set of all nuclei on the Gödel chain. The present statements are neither special cases nor direct corollaries of those claims without the new laminar/compatibility lemma and tree classification.

## Limitations

The classification uses the total order and idempotence essentially; it does not apply verbatim to products of chains, diamond lattices, partial injective Catalan transformations, or non-idempotent Catalan-monoid elements. Novelty comparisons cannot exclude an older equivalent formulated in Catalan semigroup or interval hierarchy terminology. The finite verifier does not prove infinite statements. The result does not count all commuting collections of arbitrary cardinality, only maximal families and ordered pairs.

## References

1. G. Fellin and P. Schuster, *A General Glivenko–Gödel Theorem for Nuclei*, arXiv:2112.14049v1, first public 2021-12-28, https://arxiv.org/html/2112.14049v1 (particularly Sections 1 and 3).
2. O. B. Sapir and M. V. Volkov, *Catalan monoids inherently nonfinitely based relative to finite R-trivial semigroups*, arXiv:2211.12952v1, first public 2022-11-23, https://arxiv.org/html/2211.12952v3 (Sections 2, 4 and 5, later open version).
3. S. Margolis and B. Steinberg, *The algebra of the Catalan monoid as an incidence algebra: A simple proof*, arXiv:1806.06531v1, first public 2018-06-18, https://arxiv.org/abs/1806.06531 (Sections 1–2).
4. Published results comparing finite-chain preconditionals, Frobenius-adjoint/monadic Gödel expansions, and commuting relation condensations, https://github.com/published-finding corpus/2026/ (specific comparison identifiers in the accompanying review).
