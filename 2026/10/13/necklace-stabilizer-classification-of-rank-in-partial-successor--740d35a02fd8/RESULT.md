# Necklace-stabilizer classification of rank in partial-successor cyclic automata

## Finding
For any integer \(n\ge2\) and any subset \(A\subseteq\mathbb Z/n\mathbb Z\), consider the two-letter deterministic automaton \(\mathcal C(n,A)\) with state set \(Q=\mathbb Z/n\mathbb Z\) and transition maps
\[
 a(i)=i+1\pmod n,\qquad
 b_A(i)=\begin{cases}i+1\pmod n,&i\in A,\\i,&i\notin A.\end{cases}
\]
Let \(H(A)=\{t\in Q:A+t=A\}\) be the additive translation stabilizer. If \(r(n,A)\) is the minimum possible cardinality of the image of \(Q\) under any word in the two letters, then
\[
 \boxed{r(n,A)=|H(A)|.}
\]
Equivalently, \(\mathcal C(n,A)\) is synchronizing if and only if the length-\(n\) binary indicator word of \(A\) has least cyclic period \(n\) (is aperiodic under nontrivial rotation).

The classification is enumerative as well. For each positive divisor \(d\mid n\), the number of labeled active sets with minimum rank \(d\) equals
\[
 \boxed{N_{n,d}=\sum_{e\mid(n/d)}\mu(e)2^{n/(de)}.}
\]
For \(d\nmid n\), the count is zero. More precisely, for every integer \(0\le k\le n\), the number of such sets of cardinality \(k\) equals zero unless \(d\mid k\); in the latter case it equals
\[
 \boxed{N_{n,d,k}=\sum_{e\mid\gcd(n/d,k/d)}\mu(e)
 \binom{n/(de)}{k/(de)}.}
\]
Here \(\mu\) is the number-theoretic Möbius function, and the sum also applies when \(k=0\).

The proof constructs an explicit word attaining minimum rank with length at most \(m(m-1)^2\), where \(m=n/|H(A)|\) (with the empty word sufficing for \(m=1\)).

## Assumptions and scope
All subsets \(A\), including \(\varnothing\) and \(Q\), are permitted. Transitions are functions on residue classes, so the increment of \(n-1\) wraps to zero. Each word acts from left to right on states; the empty word is allowed when defining minimum rank. The underlying automaton is strongly connected because \(a\) is a full cycle.

A binary pattern is termed *aperiodic* here solely in the finite necklace sense: the only shift preserving it is the zero shift. For \(A=\varnothing\) or \(A=Q\), \(H(A)=Q\) and both letters are permutations or identities, so minimum rank is \(n\). The formula does not assert any shortest-reset-length formula.

## Proof
**Step 1: the symmetry lower bound.** The set \(H=H(A)\) is a subgroup of \(Q\). Every \(t\in H\) commutes with both letters, in the precise sense
\[
 a(i+t)=a(i)+t,\qquad b_A(i+t)=b_A(i)+t.
\]
Induction on word length gives \(w(i+t)=w(i)+t\) for every word \(w\). Hence \(w\) maps each coset \(i+H\) bijectively onto the coset \(w(i)+H\). Every image \(w(Q)\) contains at least one entire \(H\)-coset, so \(r(n,A)\ge |H|\).

**Step 2: quotient reduction.** Put \(h=|H|\) and \(m=n/h\). Because both letters commute with every translation from \(H\), they induce transformations \(\bar a,\bar b\) on the quotient cyclic group \(Q/H\) of order \(m\), with the same partial-successor form for the quotient active set \(\bar A\). This quotient pattern has trivial translation stabilizer: if a quotient shift \(\bar t\) fixes \(\bar A\), its lift \(t\) satisfies \(A+t=A\), so \(t\in H\) and \(\bar t=0\). When \(m=1\), the empty word already has image \(Q\), one \(H\)-coset, and is optimal. Assume henceforth \(m\ge2\).

**Step 3: every quotient pair can be merged.** Work on \(\mathbb Z/m\mathbb Z\) and write \(B=\bar A\). For an ordered pair of distinct states \((x,y)\), let \(d\in\{1,\ldots,m-1\}\) be the residue \(y-x\pmod m\). Since \(B\) has trivial stabilizer and \(d\ne0\), the finite sets \(B\) and \(B-d\) differ. Thus there exists \(u\in B\) with \(u+d\notin B\); otherwise \(B+d\subseteq B\) and finiteness would give \(B+d=B\), a contradiction.

Choose \(t\in\{0,\ldots,m-1\}\) such that \(x+t=u\pmod m\). The word \(a^t b_B\) moves the first element of the pair to \(u+1\) and fixes the second at \(u+d\). Therefore the new oriented distance is exactly \(d-1\), interpreted as an integer in \(\{0,\ldots,m-2\}\). Repeating decreases the distance one at a time, so the pair merges after at most \(d\le m-1\) stages of length at most \(m\). Thus any pair of distinct quotient states is compressible by a word of length at most \(m(m-1)\).

**Step 4: attain the lower bound.** Start with the entire quotient state set. Unless its image is a singleton, select two distinct states in the current image and append a word merging them as in Step 3. The image cardinality never increases under a letter and strictly decreases at the end of this appended word. At most \(m-1\) repetitions produce a quotient reset word \(w\) of length at most \(m(m-1)^2\). Lift the same word to \(Q\). Its full-state image lies inside the single coset corresponding to the quotient reset state, hence has cardinality at most \(h\). Step 1 forces equality, establishing \(r(n,A)=h\).

**Step 5: exact rank enumerators.** A length-\(n\) binary indicator pattern has stabilizer of cardinality exactly \(d\) if and only if it consists of \(d\) repetitions of a binary block of length \(m=n/d\) whose least cyclic period is \(m\). Let \(P(m)\) count the latter primitive blocks. Each length-\(m\) word has a unique primitive root whose length divides \(m\), so \(2^m=\sum_{j\mid m}P(j)\). Möbius inversion yields
\[
 P(m)=\sum_{e\mid m}\mu(e)2^{m/e},
\]
which proves the unweighted count. Holding the number \(w=k/d\) of active sites in the primitive block fixed, the identical argument restricted to Hamming weight gives
\[
 \binom mw=\sum_{e\mid\gcd(m,w)}P(m/e,w/e)
\]
when primitive blocks are indexed by their length and weight, and Möbius inversion yields
\[
 P(m,w)=\sum_{e\mid\gcd(m,w)}\mu(e)\binom{m/e}{w/e}.
\]
To be explicit, the preceding divisor sum counts words that are a repeated \(e\)-fold copy of a shorter block; inversion isolates those with no nontrivial repetition. For \(w=0\), divisors of \(\gcd(m,0)=m\) are used. Substituting \(m=n/d\), \(w=k/d\) completes the proof.

## Verification
The standalone `verify.py` implements independent finite checks. It computes exact reachable-subset minima by breadth-first search for all \(1020\) binary active masks at state counts \(2\le n\le9\); checks minimum-rank distributions for all \(65{,}532\) masks at \(2\le n\le15\); checks \(449\) weighted count cases; constructs and replays the explicit quotient-merging procedure for \(1320\) additional pseudorandom masks at \(10\le n\le42\); and checks \(394\) equally spaced active sets. It reports:

`VERIFY_OK exhaustive_pairs=1020 counted_masks=65532 weighted_cases=449 constructive_samples=1320 stride_cases=394 max_n=42`

These tests are finite consistency checks. The proof of the all-\(n\), all-\(A\) assertion is symbolic in Steps 1–5.

## Relationship to prior work
Kari, Ryzhikov, and Varonka (2019) study bounds and extremal constructions for shortest minimum-rank words, including circular automata; their Corollary 1 and Proposition 4 give families with prescribed rank, and their Theorem 3 gives a general circular-automaton length bound. Those statements do not determine the rank from the translation stabilizer of an arbitrary partial-successor letter, nor do they enumerate all masks by rank.

Volkov (2023) gives sufficient synchronization conditions for primitive automata with special singular letters. Rystsov and Szykuła (2023) prove synchronization for primitive automata with semiconstant letters. A partial-successor letter with several independently advancing states or a nontrivial chain need not be semiconstant; these hypotheses do not directly establish the present all-mask classification. Hoffmann (2020) studies complete reachability and state complexity of synchronizing-word languages in circular automata, rather than this rank spectrum.

Special cases where an active mask has one state, or where the cyclic permutation group is primitive, connect to familiar synchronization criteria. The claim of interest is the uniform exact rank and enumerator for every mask, including periodic masks on composite cycles. For example, on six states \(A=\{0,2,4\}\) has minimum rank three, whereas \(A=\{0,2\}\) has rank one; both automata have a full-cycle letter. The formulas classify the complete family without searching the subset automaton.

## Limitations
The theorem addresses minimum image cardinality, not exact lengths of shortest words of minimum rank. The constructive cubic bound in quotient size is not asserted to be sharp. The familiar Möbius formula is used as a counting identity, not claimed as a new number-theoretic fact. The literature comparison below cannot exclude every unindexed equivalent presentation of this automaton family.

## References
1. M. V. Volkov, *Synchronization of primitive automata*, arXiv:2306.13317, first posted June 23, 2023; https://arxiv.org/abs/2306.13317.
2. I. Rystsov and M. Szykuła, *Primitive Automata that are Synchronizing*, arXiv:2307.01302, first posted July 3, 2023; https://arxiv.org/abs/2307.01302.
3. J. Kari, A. Ryzhikov, and A. Varonka, *Words of Minimum Rank in Deterministic Finite Automata*, DLT 2019, pp. 74–87, DOI:10.1007/978-3-030-24886-4_5; publicly available author final draft: https://www.utupub.fi/bitstreams/df55c125-3bb6-4f4f-b3ef-3799b3cff98c/download.
4. S. Hoffmann, *State Complexity of the Set of Synchronizing Words for Circular Automata and Automata over Binary Alphabets*, arXiv:2011.14404; https://arxiv.org/abs/2011.14404.
