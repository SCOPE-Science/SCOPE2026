# Four complete primitive rotation orbits at every dyadic Rudin–Shapiro length

## Finding
Let \(r=r(0)r(1)\cdots\) be the classical binary Rudin–Shapiro sequence, where \(r(n)\) is the parity of the number of overlapping occurrences of `11` in the base-two expansion of \(n\). For every integer \(k\geq 3\), its length-\(2^k\) factor language contains **at least four distinct complete primitive cyclic conjugacy classes**. In each class, all \(2^k\) distinct cyclic rotations of a representative occur as contiguous factors of \(r\). Consequently, the Lie complexity, counting conjugacy classes completely represented among factors, satisfies
\[
 L_r(2^k)\geq4\qquad(k\geq3),
\]
and these classes account for at least \(4\cdot 2^k\) distinct factors of that length. The statement is a lower bound, **not** a formula claiming exactly four classes.

## Assumptions and scope
Work with the four-letter morphism
\[
 h(a)=ab,\quad h(b)=ac,\quad h(c)=db,\quad h(d)=dc
\]
and coding \(\pi(a)=\pi(b)=0\), \(\pi(c)=\pi(d)=1\). Its fixed point \(s=h^\omega(a)\) codes to \(r=\pi(s)\). For each letter \(x\), let \(W_k(x)=\pi(h^k(x))\), a binary word of length \(2^k\). A *complete conjugacy class* is one for which every cyclic rotation is an occurring factor, whereas *primitive* means that a representative is not a proper power. Rotation equivalence here is ordinary cyclic conjugacy, not reversal or letter complementation. The four asserted classes are those containing \(W_k(a),W_k(b),W_k(c),W_k(d)\).

## Proof
**1. Complete rotation orbits.** The adjacent pairs appearing as images of letters are `ab`, `ac`, `db`, `dc`. Each of the corresponding alternating triples occurs in \(s\), in both orders: `aba`, `bab`, `aca`, `cac`, `dbd`, `bdb`, `dcd`, `cdc`. This is a finite fact: they all occur in \(h^8(a)\); their zero-based first positions are respectively \(0,7,2,13,22,5,24,11\). Thus whenever \(h(x)=pq\), both `pqp` and `qpq` occur in the fixed point. Put \(P=W_{k-1}(p)\), \(Q=W_{k-1}(q)\), each of length \(2^{k-1}\). Then \(W_k(x)=PQ\), while both \(PQP\) and \(QPQ\) are factors of \(r\) under the morphism/coding. Every rotation of \(PQ\) by fewer than \(|P|\) positions appears in \(PQP\); every rotation by at least \(|P|\) positions appears in \(QPQ\). Consequently **every** rotation of every \(W_k(x)\) occurs, for all \(k\geq1\).

**2. Primitivity.** For \(k=1\), the four coded blocks in letter order are `00`, `01`, `10`, `11`, hence pairwise different. The four ordered pairs of letters \((a,b),(a,c),(d,b),(d,c)\) are different. Therefore, by induction, all four blocks \(W_k(x)\) are pairwise distinct for every \(k\geq1\): each is a concatenation of two uniquely identifiable smaller blocks. As every \(h(x)=pq\) has \(p\ne q\), the two halves \(P,Q\) of \(W_k(x)\) differ for \(k\geq2\). Any proper power of length \(2^k\) repeats its smaller root an even number of times and therefore has equal length-\(2^{k-1}\) halves. Thus every \(W_k(x)\) for \(k\geq2\) is primitive and has exactly \(2^k\) distinct rotations.

**3. Four distinct rotation classes.** We distinguish representatives by rotation invariants: \(w_k(x)=|W_k(x)|_1\), and \(q_k(x)\), the number of cyclic (wrap-around included) occurrences of the four-letter pattern `0100` in \(W_k(x)\). Let the coordinates always be ordered \((a,b,c,d)\).

The elementary recurrence \(w_{k+1}(x)=w_k(p)+w_k(q)\) for \(h(x)=pq\), from \(w_1=(0,1,1,2)\), gives, for every \(m\geq1\),
\[
\begin{aligned}
 w_{2m+1}&=(2^{2m}-2^m,\ 2^{2m},\ 2^{2m},\ 2^{2m}+2^m),\\
 w_{2m}&=(2^{2m-1}-2^{m-1},\ 2^{2m-1}-2^{m-1},\ 2^{2m-1}+2^{m-1},\ 2^{2m-1}+2^{m-1}).
\end{aligned}
\]
In the odd case only the pair \((b,c)\) remains to separate; in the even case only the pairs \((a,b)\) and \((c,d)\) remain.

For every \(k\geq3\), blocks \(W_k(a),W_k(b)\) begin with `000` and \(W_k(c),W_k(d)\) begin with `111`, while each block ends with either `010` or `101`. Check all three possible splits of `0100` across a boundary: for a block ending `010`, the three-one split contributes precisely when the next block begins `000`; for a block ending `101`, the two-two split contributes precisely under the same condition. No other split contributes. Hence **one** cross-boundary occurrence of `0100` is contributed exactly when the succeeding block has type \(a\) or \(b\), independent of the preceding block. This also describes the wrap-around contribution inside each individual block. It follows that for *any circular concatenation* of these blocks, the cyclic `0100` count is the sum of their individual cyclic `0100` counts.

As
\[
 h^2(a)=abac,\quad h^2(b)=abdb,\quad
 h^2(c)=dcac,\quad h^2(d)=dcdb,
\]
we obtain for every \(k\geq3\)
\[
 q_{k+2}=Tq_k,\qquad
 T=\begin{pmatrix}2&1&1&0\\1&2&0&1\\1&0&2&1\\0&1&1&2\end{pmatrix}.
\]
Direct inspection of the explicit blocks of lengths \(8\) and \(16\) gives
\[
 q_3=(2,1,0,0),\qquad q_4=(3,2,1,0).
\]
The row vector extracting \(q_k(b)-q_k(c)\) is a left eigenvector of \(T\) with eigenvalue \(2\). Hence for odd \(k=2m+1\geq3\),
\[
 q_k(b)-q_k(c)=2^{m-1}>0.
\]
For even \(k=2m\geq4\), the identity \(q_k(a)+q_k(d)=q_k(b)+q_k(c)\) holds at \(k=4\) and is preserved by \(T\); using it in the recurrence gives
\[
 q_k(a)-q_k(b)=q_k(c)-q_k(d)=2^{m-2}>0.
\]
Thus the ordered pairs \((w_k(x),q_k(x))\) are pairwise distinct for every \(k\geq3\). As both statistics are invariant under cyclic rotation, the four complete primitive conjugacy classes are pairwise distinct. Steps 1–3 prove the theorem.

## Verification
The included `verify_rudin_rotations.py` reconstructs the state morphism, coding, cyclic `0100` counts, and binary-digit Rudin–Shapiro definition. Running `python3 verify_rudin_rotations.py` produces `VERIFY_OK`. For exponents \(3\) through \(12\), it checks the weight formulas, cyclic-pattern recurrence, pairwise-distinct invariants, and primitivity. For exponents \(3\) through \(9\), it also verifies actual occurrence of **all** rotations in directly generated Rudin–Shapiro prefixes; additional checks compare both sequence generators. These finite tests do not substitute for the all-exponent proof above.

## Relationship to prior work
Cassaigne–Fici–Sciortino–Zamboni (2014) initiated systematic study of cyclic complexity, which identifies occurring factors up to rotations without requiring *all* rotations to occur. Bell–Shallit (2021) introduced and studied Lie complexity as the stricter number of completely occurring conjugacy classes, giving evaluations for several standard automatic and morphic sequences, including Thue–Morse, but no Rudin–Shapiro specialization located in the inspected full text. The present claim is a lower bound with four explicit families of witnesses in the Rudin–Shapiro sequence. Allouche–Shallit (1993) concerns its ordinary factor complexity; Li (2022) concerns general Lie-complexity bounds. No result inspected implies this four-orbit construction. Coverage by an unindexed source cannot be ruled out.

## Limitations
Only the guaranteed existence of **at least** four complete primitive classes at dyadic lengths \(2^k\), \(k\geq3\), is established. Neither equality for Lie complexity nor any nondyadic classification, global upper bound, factor-frequency distribution, or orbit classification is claimed. The embedded program verifies bounded ranges; the infinite theorem is proved in the text. The originality assessment is limited to accessible, actually inspected sources and recorded searches. No independent audit has been performed.

## References
- J. Cassaigne, G. Fici, M. Sciortino, L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843 (initial public version 2014-02-24), https://arxiv.org/abs/1402.5843 .
- J. P. Bell and J. Shallit, *Lie Complexity of Words*, arXiv:2102.03821 (2021), https://arxiv.org/abs/2102.03821 .
- J.-P. Allouche and J. Shallit, *The Rudin–Shapiro Sequence*, in *Theoretical Computer Science* (1993), published reference discussing factor complexity and automatic descriptions.
- S. Li, *A note on the Lie complexity and beyond*, arXiv:2207.05859 (2022), https://arxiv.org/abs/2207.05859 .
