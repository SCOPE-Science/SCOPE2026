# Exact maximal-pattern profiles and de Bruijn extremizers for decorated Sturmian rotations

## Finding
Fix a binary Sturmian coding of an irrational circle rotation, insert it into one residue class of a period-\(m\) word, and fill the other residue classes with constant symbols from an alphabet disjoint from the binary one. The maximal pattern complexity of the resulting sequence has an **exact formula for every window size**, rather than only an eventual affine law. Its extremal additive offset over all decorations has a sharp alphabet-dependent formula, realized by de Bruijn words.

For \(m,q\ge2\), define
\[
s_q(m)=\min\{1\le s\le m:q^s\ge m-s\}.
\]
For every window size \(k\ge1\), the largest possible maximal pattern complexity in this family is
\[
\boxed{\max_c p_{y(c)}^*(k)=2k+\min\{q^k,m-s_q(m)\}.}
\]
The maximum is attained explicitly by a periodic decoration whose entries are cut from a cyclic de Bruijn word of order \(\min\{k,s_q(m)\}\). For fixed \(q\) and large \(m\), the sharp eventual additive offset is \(m-\log_q m+O(1)\).

## Assumptions and scope
Let \(\alpha\in(0,1)\) be irrational and \(\theta\in\mathbb R/\mathbb Z\). Write \(x_j=\mathbf 1_{[0,\alpha)}(\theta+j\alpha)\) for \(j\ge0\); any choice of boundary convention gives the same sets of finite patterns. Let \(B\) be an alphabet of exactly \(q\ge2\) symbols with \(B\cap\{0,1\}=\varnothing\). For \(m\ge2\), choose a decoration vector \(c=(c_1,\ldots,c_{m-1})\in B^{m-1}\). Define the infinite word \(y=y(c)\) by
\[
y_{mj}=x_j,\qquad y_{mj+r}=c_r\quad(j\ge0,\ 1\le r<m).
\]
For each \(k\ge1\), define its maximal pattern complexity using arbitrary strictly increasing offsets:
\[
p_y^*(k)=\max_{0\le t_1<\cdots<t_k}
\#\{(y_{N+t_1},\ldots,y_{N+t_k}):N\ge0\}.
\]
For every nonempty residue set \(S\subseteq\mathbb Z/m\mathbb Z\), define the **inactive-phase signature count**
\[
D_c(S)=\#\bigl\{(c_{r+s})_{s\in S}:r\in\mathbb Z/m\mathbb Z,\ 0\notin r+S\bigr\}.
\]
Here every decoration subscript is read modulo \(m\), and the condition \(0\notin r+S\) means that no undefined value \(c_0\) occurs. The tuple is ordered using the fixed standard order of \(S\) inside \(\{0,\ldots,m-1\}\). Set
\[
C_{c,k}=\max_{\varnothing\ne S\subseteq\mathbb Z/m\mathbb Z,
\ |S|\le\min(k,m)}D_c(S).
\]

**Exact profile theorem.** For every decoration and every \(k\ge1\),
\[
\boxed{p_{y(c)}^*(k)=2k+C_{c,k}.}
\]
In particular, the offsets form a nondecreasing sequence in \(k\), stabilize by \(k=m\), and are computable from at most \(2^m-1\) subsets without enumerating orbit words. Combining this theorem with the extremal formula above gives a complete finite-window optimization over all periodic decorations on a prescribed alphabet.

## Proof
**1. Sturmian subsequence bound and attainability.** For distinct nonnegative indices \(n_1,\ldots,n_t\), the circle rotation phases at which any of their \(t\) binary symbols changes lie among the \(2t\) endpoints \(-n_j\alpha\) and \(\alpha-n_j\alpha\) modulo one. Therefore the \(t\)-coordinate sampled pattern set has cardinality at most \(2t\). This remains true if two endpoints coincide or the coding interval is half-open: boundary values reproduce neighboring configurations and create no further patterns.

For every \(t\ge1\), indices may instead be chosen so that the \(t\) phases \(-n_j\alpha\) are distinct and all lie inside an arc of length smaller than both \(\alpha\) and \(1-\alpha\). This is possible with arbitrarily large indices because the irrational rotation orbit is dense. Along the circle, the \(t\) entrances to the translated coding intervals then occur consecutively, followed by all \(t\) exits. The resulting binary vectors change one coordinate at a time from all-zero to all-one and back, and all \(2t\) intervening vectors are pairwise distinct. Hence the upper bound \(2t\) is sharp, using choices of arbitrarily large indices. The same conclusion holds for arbitrary common translations of the selected indices.

**2. Exact decomposition by starting phase.** Fix a window \(T=\{t_1<\cdots<t_k\}\), and put \(S=T\bmod m\), with \(k_s=\#\{t\in T:t\equiv s\pmod m\}\). If a starting time has phase \(r\pmod m\), exactly the positions corresponding to \(s=-r\pmod m\) sample the binary Sturmian residue; all remaining positions have fixed decorative symbols. If \(-r\notin S\), the entire pattern is the single all-decoration signature associated with \(r\), and the distinct signatures over these inactive phases are counted by \(D_c(S)\).

For each of the \(|S|\) active phases, the number of distinct patterns is at most \(2k_s\) by part 1. Two distinct active phases have binary symbols in disjoint nonempty coordinate sets, so their pattern families are disjoint. These also cannot overlap any inactive all-decoration pattern because \(B\cap\{0,1\}=\varnothing\). Therefore
\[
\#F_y(T)\le2\sum_{s\in S}k_s+D_c(S)=2k+D_c(S).
\]
Conversely, for any selected nonempty \(S\), choose \(k_s\ge1\) with \(\sum_{s\in S}k_s=k\). For every \(s\) independently choose the quotient indices of the sample positions \(t=m n+s\) using part 1, so that the active phase at \(-s\) realizes exactly \(2k_s\) distinct Sturmian vectors. Their decorative coordinates remain fixed, and every choice of positive starting phase is visited at arbitrarily many starting times; irrational rotation density ensures all permitted binary patterns occur. Inactive phases still contribute exactly \(D_c(S)\). Thus \(\#F_y(T)=2k+D_c(S)\), proving the exact profile after maximizing over \(S\).

**3. Universal upper bound for the additive offset.** Suppose \(|S|=t\). Exactly \(m-t\) starting phases avoid the sampled Sturmian residue, and each inactive signature is a \(t\)-letter word over \(B\). Consequently
\[
D_c(S)\le\min\{m-t,q^t\}.
\]
Set \(s=s_q(m)\). Minimality of \(s\) implies \(q^{s-1}<m-s+1\), hence \(q^{s-1}\le m-s\). For \(t<s\), the bound is at most \(q^t\le\min\{q^k,m-s\}\) when \(t\le k\); for \(t\ge s\), it is at most \(m-t\le m-s\), and \(q^t\le q^k\) when \(t\le k\). Therefore \(C_{c,k}\le\min\{q^k,m-s\}\).

**4. Sharpness via de Bruijn necklaces.** Let \(t=\min\{k,s\}\) and take a cyclic \(q\)-ary de Bruijn word of order \(t\), in which every \(t\)-letter word occurs exactly once as a cyclic block. Fill \(c_1,\ldots,c_{m-1}\) using the first \(m-1\) letters of the infinite periodic repetition of that word. Choose \(S=\{0,1,\ldots,t-1\}\). The \(m-t\) inactive starting phases are precisely \(r=1,\ldots,m-t\), and their signatures are the consecutive length-\(t\) blocks beginning at those positions of the periodic de Bruijn word. They have exactly \(\min\{m-t,q^t\}\) distinct values. If \(k<s\), minimality of \(s\) shows \(q^k\le m-s\le m-k\), so this number is \(q^k\). If \(k\ge s\), the count is \(m-s\). In either case it equals \(\min\{q^k,m-s\}\), matching the universal bound. Finally, \(s_q(m)=\log_q m+O(1)\) follows immediately from the minimality inequalities \(q^{s-1}<m-s+1\le m\) and \(q^s\ge m-s\), with a fixed-size correction for sufficiently large \(m\).

## Verification
The supplied standalone `verify.py` implements exact residue-signature enumeration, q-ary de Bruijn generation, and the closed extremal expression. Running `python3 verify.py` returns `VERIFY_OK finite_extremal_instances=91`: all decoration vectors and all window sizes were exhaustively compared for binary decorations through period nine, ternary decorations through period seven, and quaternary decorations through period six. It additionally tests a nonextremal period-five decoration and a period-twelve binary decoration attaining additive offset eight at window size three. These computations are finite sanity checks; parts 1–4 provide the proof for unbounded \(m,q,k\).

## Relationship to prior work
Schlortt's 2025 preprint (Theorem 1.3 and its proof) already establishes eventual affinity \(p^*(k)=2k+C\) for periodic interleavings of a pattern Sturmian sequence with constant residues, and its Example 6.2 gives one enhanced-intercept construction. These results and the shared active-phase counting decomposition are credited as the starting point. The present theorem establishes the missing **every-window** additive profile as an explicit finite signature invariant and the **sharp alphabet-dependent maximum** across all decorations via de Bruijn sequences; neither statement follows from knowing that an unspecified eventual intercept exists. This work is for standard irrational-rotation Sturmian words and decorative symbols disjoint from \(\{0,1\}\), not for arbitrary pattern-Sturmian residues or decorations that reuse binary symbols. Le–Pavlov–Schlortt (2025) classify low-pattern-complexity subshifts but do not provide this extremal profile.

## Limitations
No claim is made for non-Sturmian pattern-Sturmian residues, overlapping alphabets, multiple aperiodic residue classes, nonperiodic decorations, or other notions of complexity such as Abelian pattern complexity. The profile is exact for the specified symbolic family only. Known existence and eventual-affinity results are not claimed as new. Bibliographic priority is subject to checking additional unavailable theses and terminology variants. No independent mathematical audit has been performed.

## References
1. Casey Schlortt, *On the structure of sequences with minimal maximal pattern complexity*, arXiv:2505.05627v1 (first posted 2025-05-08), especially Theorem 1.3, proof, and Examples 6.1–6.2. https://arxiv.org/html/2505.05627v1
2. Anh N. Le, Ronnie Pavlov, and Casey Schlortt, *On subshifts with low maximal pattern complexity*, arXiv:2508.13420v1 (2025-08-19), notably Proposition 4.7. https://arxiv.org/abs/2508.13420
3. Teturo Kamae and Lubomíra Zamboni, *Sequence entropy and maximal pattern complexity of infinite words*, Ergodic Theory and Dynamical Systems 22 (2002), 1191–1199.
4. Teturo Kamae and R. N. Rao, *Maximal pattern complexity of words over ℓ letters*, European Journal of Combinatorics 27 (2006), 125–137.
