# Sharp quadratic entropy of finite frames for knowing-whether introspection

## Finding
For every integer \(n\ge4\), let \(a_n\) be the number of binary relations on a labelled \(n\)-element set that validate the non-contingency axiom \(\Delta\Delta p\) under every valuation. Then
\[
2^{(\lfloor n/2\rfloor-2)\lceil n/2\rceil}\le a_n\le (n+1)^{3n}2^{(n+1)^2/4}.
\]
In particular,
\[
\lim_{n\to\infty}\frac{\log_2 a_n}{n^2}=\frac14,
\qquad
\frac{a_n}{2^{n^2}}=2^{-3n^2/4+O(n\log n)}.
\]
The precise quadratic entropy provides a quantitative sparsity law for finite frames validating a natural positive-introspection principle of knowing whether.

## Assumptions and scope
A frame is \((W,R)\) with \(W=\{1,\ldots,n\}\), nonempty, and \(R\subseteq W\times W\). Loops are allowed; seriality, reflexivity, symmetry and transitivity are not assumed. For any Boolean valuation and formula \(\varphi\), \(\Delta\varphi\) holds at a world exactly if \(\varphi\) has a constant truth value on all of its successors; the assertion is vacuous for empty successor sets. Frame validity of \(\Delta\Delta p\) means truth at every world for every valuation of the propositional letter \(p\).

Write \(R(w)=\{u:wRu\}\). Define a successor-set type \(\tau(w)\) by the special symbol \(0\) if \(|R(w)|\le1\), and by the set \(R(w)\) itself when \(|R(w)|\ge2\). The symbol \(0\) is distinct from all sets.

## Proof
**Step 1: exact successor-type criterion.** For any fixed valuation, let \(d_w\) be the Boolean truth value of \(\Delta p\) at \(w\). If \(|R(w)|\le1\), then \(d_w=1\) under every valuation. If \(|R(w)|\ge2\), then \(d_w=1\) precisely when the truth values assigned to \(p\) are constant on \(R(w)\). For two successor sets of cardinality at least two, these homogeneity predicates agree for *every* Boolean valuation if and only if the sets agree: the family of valuations constant on one set recovers that set as its unique nonsingleton equivalence block, where two vertices are equivalent if every such valuation assigns them equal values. Also, no predicate from a set of size at least two is constantly true. Therefore two worlds have identical functions \(d_w\) of the valuation exactly when their types \(\tau(w)\) agree.

The axiom \(\Delta\Delta p\) holds at \(w\) under every valuation exactly when the functions \(d_u\), for \(u\in R(w)\), are pairwise identical. It follows that
\[
(W,R)\models\Delta\Delta p\quad\Longleftrightarrow\quad
\forall w\in W\;\bigl|\{\tau(u):u\in R(w)\}\bigr|\le1.
\tag{1}
\]
This formulation rederives the known first-order correspondence for the axiom; its novelty is **not** asserted here.

**Step 2: upper bound.** Partition \(W\) by type into \(C_0=\{w:|R(w)|\le1\}\) (possibly empty) and \(k\) nonempty classes \(C_1,\ldots,C_k\) whose members have one identical nonfunctional row. The type partition can be encoded, with overcounting allowed, by assigning each vertex one of \(n+1\) labels. Hence there are at most \((n+1)^n\) such encodings.

Each vertex in \(C_0\) has an empty or singleton row, so the total number of its row choices is at most \((n+1)^n\). Every nonfunctional class \(C_i\) shares a single row \(S_i\) of size at least two. By (1), every element of \(S_i\) belongs to a *single* type class \(C_j\). There are at most \(n+1\) choices for that target class per \(i\), and at most \(2^{|C_j|}\) choices for \(S_i\) once \(j\) has been selected. Requiring distinct nonfunctional rows and cardinality at least two can only reduce the count.

Let \(M\) be the maximum size of a nonempty type class. Since at least \(k-1\) nonfunctional classes remain outside a maximum class, \(k\le n-M+1\), including when the maximum class is \(C_0\). Consequently,
\[
Mk\le M(n-M+1)\le (n+1)^2/4.
\]
The product of row-subset choices is at most \(2^{Mk}\). Combining the three independent overcounts proves
\[
a_n\le(n+1)^{3n}2^{(n+1)^2/4}.
\tag{2}
\]
The argument includes the degenerate case \(k=0\), when every row has size at most one.

**Step 3: lower bound.** Partition \(W\) into fixed labelled parts \(A\) and \(B\) with \(|A|=\lfloor n/2\rfloor=:a\) and \(|B|=\lceil n/2\rceil=:b\). Put \(R(u)=\varnothing\) for every \(u\in A\). Choose two fixed distinct vertices \(s,t\in A\). Independently for each \(v\in B\), choose any subset \(T_v\) of \(A\setminus\{s,t\}\) and put \(R(v)=\{s,t\}\cup T_v\). Every successor of every world in this construction lies in \(A\), and all vertices of \(A\) have type \(0\). Thus (1) holds. Distinct choices yield distinct labelled relations, of which there are exactly
\[
2^{(a-2)b}.
\tag{3}
\]
This proves the lower bound for \(n\ge4\).

**Step 4: asymptotic conclusion.** The logarithm of the lower bound is \(n^2/4-O(n)\), whereas the logarithm of (2) is \(n^2/4+O(n\log n)\). Dividing by \(n^2\) and taking limits proves the stated entropy. The density follows by dividing by the total \(2^{n^2}\) labelled binary relations. □

## Verification
A standalone Python checker evaluates every one of the \(2^{n^2}\) binary relations on \(n=1,2,3,4\) labelled worlds, testing both the structural criterion (1) and the raw truth table of \(\Delta\Delta p\) for all \(2^n\) Boolean valuations. Both tests agree on all 2, 16, 512 and 65,536 relations respectively; the numbers satisfying the axiom are 2, 10, 128 and 3,070. It also checks explicit lower-bound family constructions for \(4\le n\le11\) (and their complete valuation tables for \(n\le6\)). Run `python3 checker.py` with Python 3.8 or later. These finite tests independently check small instances, not the asymptotic theorem; the latter follows from Steps 1–4.

## Relationship to prior work
Zolin, *Completeness and Definability in the Logic of Non-contingency* (1999), proves a first-order correspondent for the axiom \(\Delta\Delta p\) in Theorem 4.1 and classifies related non-contingency frame conditions. Accordingly no originality is claimed for first-order definability or the qualitative structural criterion (1). Sierra Miranda, Wang and Zenger, *Proof Theory for Non-Contingency Logic* (2026), develop sound and complete labelled sequent calculi for broad families of frames. Their result motivates renewed study of the finite frame classes but is proof-theoretic, not an asymptotic labelled-frame count. The original aspect claimed here is the sharp quadratic counting exponent \(1/4\) for this one non-contingency axiom, derived from the class partition bound and matching bipartite family.

## Limitations
The result concerns labelled finite frames without restrictions on loops or other frame axioms, and only the single schema \(\Delta\Delta p\). It establishes a leading quadratic exponent with an \(O(n\log n)\) remainder, not a sharp second-order term or an exact enumeration formula for arbitrary \(n\). The source comparison cannot exclude unindexed or terminologically different earlier asymptotic counting results. Its small-frame computations are corroborative rather than an infinite proof.

## References
1. B. Sierra Miranda, Y. Wang and L. Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975, first public 2026-09-30. Full-text PDF: https://arxiv.org/pdf/2609.38975.
2. E. E. Zolin, *Completeness and Definability in the Logic of Non-contingency*, Notre Dame Journal of Formal Logic (1999), Theorem 4.1. Public full text: https://www.cs.man.ac.uk/~ezolin/pub/zolin_1999_NDJFL.pdf.
