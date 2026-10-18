# Persistence-filtered rook normal form for finite-chain flat Heyting–Lewis implication

## Finding
Fix an integer \(n\geq 1\), and let \(W_n=\{0<1<\cdots<n-1\}\). Consider the flat Heyting–Lewis strict-implication operation \(\rightsquigarrow\) on upsets of \(W_n\), induced by any binary relation \(R\subseteq W_n\times W_n\). Its **persistence axiom** is
\[
\mathsf p_a:\quad (p\rightsquigarrow q)\to (\top\rightsquigarrow(p\rightsquigarrow q)).
\]

Associate to each row \(j\) the value \(t_j=\min R[j]\), taking \(t_j=n\) for an empty row. For \(p\in W_n\), let \(\ell_p=\max\{j:t_j=p\}\), with \(\ell_p=-1\) when no such row exists. Thus \(\ell\) is a partial injection from value labels to row indices. Every partial injection is attained, and two relations give the same strict-implication operation exactly when their maps \(\ell\) agree.

**Theorem.** Such an operation validates \(\mathsf p_a\) for every valuation if and only if its occupied rooks \((p,i)\) with \(i=\ell_p\geq0\) satisfy
\[
(p,i),(q,j)\text{ occupied and }i<j\quad\Longrightarrow\quad q>i.
\]
Equivalently, list the rooks by increasing occupied row \(i_1<\cdots<i_k\) with labels \(p_1,\ldots,p_k\). Then \(p_j>i_{j-1}\) for all \(2\leq j\leq k\). The exact number \(A_n\) of distinct operations (also their number up to Heyting-chain isomorphism) validating \(\mathsf p_a\) is
\[
A_n=1+\sum_{k=1}^{n}(n-k+1)
 \sum_{0\leq i_1<\cdots<i_k<n}
 \prod_{h=1}^{k-1}(n-k+h-i_h).
\]
The empty product is \(1\). The first eight values, for \(n=1,\ldots,8\), are \(2,6,21,82,352,1645,8302,44940\).

## Assumptions and scope
The underlying intuitionistic order is the finite total order \(W_n\), with truth sets all suffix upsets \([a,n)=\{a,\ldots,n-1\}\), including \([n,n)=\varnothing\). The modal relation is arbitrary and need not be reflexive, serial, transitive, or upward closed. Strict implication is interpreted, as in de Groot and Litak, by
\[
J_R(A,B)=\{w\in W_n:\text{for every }v\geq w,
 \ R[v]\subseteq A\implies R[v]\subseteq B\}.
\]
Intuitionistic implication \(\to\) is the Heyting implication on this chain. The formula \(\mathsf p_a\) is universally valid precisely when \(J_R(A,B)\subseteq J_R(W_n,J_R(A,B))\) for all upsets \(A,B\). No statement about infinite chains, general posets, or proof-theoretic finite-model properties is asserted.

## Proof
**Step 1 (last occurrences).** For \(0\leq a,b\leq n\), the upset \([a,n)\) contains a nonempty row precisely when \(t_j\geq a\). Empty rows are contained in every upset. Thus a row violates the implication from \([a,n)\) to \([b,n)\) exactly when \(a\leq t_j<b\). Put \(\max\varnothing=-1\). Directly from the semantics,
\[
J_R([a,n),[b,n))=[K(a,b),n),\qquad
K(a,b)=1+\max_{a\leq p<b}\ell_p.
\]
Taking \(a=p,b=p+1\) gives \(K(p,p+1)=\ell_p+1\), so the operation recovers every \(\ell_p\); conversely the displayed formula shows \(\ell\) determines the whole operation. Any partial injection \(\ell\) is realized by taking \(R[\ell_p]=\{p\}\) at occupied rows and all remaining rows empty.

**Step 2 (persistence criterion).** With \(\Box B:=J_R(W_n,B)\), the formula \(\mathsf p_a\) is valid exactly when
\[
 [K(a,b),n)\subseteq\Box[K(a,b),n)
 \quad\text{for all }a,b.
\]
For any \(0\leq k\leq n\), the defining formula gives
\[
\Box[k,n)=\left[1+\max_{p<k}\ell_p,n\right).
\]
Hence the inclusion holds exactly when \(\ell_p<k\) for every \(p<k\). Every positive value of \(K(a,b)\) is some \(\ell_q+1\), and every such value occurs from \(a=q,b=q+1\). Consequently it suffices, and is necessary, that for every occupied \((q,i)\) and every label \(p\leq i\), one has \(\ell_p\leq i\). This is exactly the claimed rook exclusion: a later occupied rook \((p,j)\) with \(j>i\) must have \(p>i\). The case \(k=0\) is automatic.

**Step 3 (counting).** Fix \(k\geq1\) occupied row positions \(0\leq i_1<\cdots<i_k<n\). The labels at these positions must be pairwise distinct and satisfy \(p_j>i_{j-1}\) for \(j\geq2\). Choose them backwards, from \(p_k\) to \(p_1\). The available sets are nested suffixes of labels; at the selection of \(p_{h+1}\) there are \(n-k+h-i_h\) choices after accounting for the labels already selected at later positions. At the last selection \(p_1\) there remain \(n-k+1\) choices. Their product counts exactly the admissible injections on these row positions. Sum over the row positions and \(k\), and add the empty injection. Every counted injection corresponds to exactly one induced operation by Step 1. A finite chain has no nonidentity order automorphism, so no two counted operations become isomorphic by relabeling.

## Verification
The standalone standard-library script `verify.py` independently evaluates the persistence formula for every pair of upset valuations on all \((n+1)^n\) upward-flat row-threshold assignments for \(1\leq n\leq6\); compares those evaluations to the rook criterion; checks operation tables against last-occurrence maps; and enumerates all partial rook placements against the product-sum formula through \(n=8\). The program completed with `VERIFY_OK`; its full output is included in `checker_output.txt`. These exhaustive finite instances test the proof but are not substitutes for the proof for arbitrary \(n\).

## Relationship to prior work
De Groot and Litak, *Relational Semantics for Flat Heyting-Lewis Logic* (arXiv:2603.28402, initially public March 30, 2026), define the flat semantics, the persistence axiom \(\mathsf p_a\), and its general frame correspondence. The present theorem addresses a different question: the exact **operator-level** normal form and enumeration of the \(\mathsf p_a\)-valid expansions of a finite Heyting chain. A prior complete last-occurrence parametrization counts all chain strict-implication operations but does not impose the persistence axiom or give its restricted counts. Results counting frames for other axiom combinations, such as \(\mathsf t_{\Box}\) together with \(\mathsf{4_a}\), do not supply this enumeration.

## Limitations
The census concerns distinct induced operations, not the number of raw relations satisfying \(\mathsf p_a\). It does not claim a new derivation of the general correspondence for \(\mathsf p_a\), the unrestricted all-operator census, or the finite-model property for the logic with this axiom. The theorem is restricted to finite total orders. Mathematical originality is assessed relative to inspected sources and searches, not guaranteed by the absence of identical wording or integer sequences.

## References
1. Jim de Groot and Tadeusz Litak, *Relational Semantics for Flat Heyting-Lewis Logic*, arXiv:2603.28402v1 (March 30, 2026); v2 (June 30, 2026), especially Sections 3.1–3.2 and 5.1. https://arxiv.org/abs/2603.28402 ; https://arxiv.org/html/2603.28402v2 .
2. Jim de Groot and Tadeusz Litak, *Relational Semantics for Flat Heyting-Lewis Logic*, Electronic Proceedings in Theoretical Computer Science 447 (2026), 445–463, DOI:10.4204/EPTCS.447.25 .
