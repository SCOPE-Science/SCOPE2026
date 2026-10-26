# Dyadic first-order limits for uniformly random binary Lyndon words

## Finding
Let \(L_n\) be chosen uniformly among binary Lyndon words of length \(n\), over the ordered alphabet \(0<1\). View \(L_n\) as a finite relational structure with a directed immediate-successor relation \(S\) and a unary predicate \(P\) for positions labelled \(1\); the global linear order and cyclic wrap-around edge are **not** in the signature.

**Theorem.** Every first-order sentence \(\varphi\) in \(\{S,P\}\) has an effectively computable limit \(p_\varphi\), with
\[
\Pr(L_n\models\varphi)=p_\varphi+O_\varphi(\log n/\sqrt n).
\]
The exact set of all these limits is
\[
\bigl\{p_\varphi:\varphi\text{ a first-order sentence}\bigr\}=\mathbb Z[1/2]\cap[0,1].
\]
The underlying stronger probabilistic statement is that, for every fixed positive integer \(h\), the first \(h\) letters are all \(0\) with probability tending to one, while the last \(h\) letters converge, with error \(O_h(\log n/\sqrt n)\), to independent fair bits in their first \(h-1\) positions followed by a forced final \(1\). Every fixed interior binary block occurs at least any prescribed fixed number of times with probability \(1-e^{-\Omega(n)}\).

## Assumptions and scope
A length-\(n\) word is *primitive* when no nonidentity cyclic rotation fixes it; it is *Lyndon* when it is primitive and lexicographically least in its rotation class. The measure is uniform over Lyndon words, not over all necklaces including periodic ones. A sentence and its quantifier rank are fixed as \(n\to\infty\). The successor relation contains exactly the edges between consecutive positions, with no last-to-first edge. The theorem covers \(n\ge 2\) asymptotically; the finitely many short lengths have no effect.

## Proof
**1. Uniform-rotation reduction.** If \(W_n\) has independent fair binary coordinates and \(\rho(W_n)\) denotes its least cyclic rotation, then the conditional law of \(\rho(W_n)\) given primitivity is exactly uniform on length-\(n\) Lyndon words: each primitive rotation class has \(n\) representatives. The probability of non-primitivity is \(O(n2^{-n/2})\), by a union over proper periods. The canonical rotation preserves all counts of cyclic factors.

**2. A local switching lemma.** Fix \(h\ge 1\), and set \(k=\lceil(3/4)\log_2 n\rceil\), \(\ell=\lceil5\log_2 n\rceil\), assuming \(n\) sufficiently large compared with \(h\). Consider the \(n\) cyclic length-\(\ell\) blocks of the fair word. With failure probability at most \(n(n-1)2^{-\ell}\), they are pairwise distinct. The equality probability for two blocks is \(2^{-\ell}\), including overlapping blocks: equality imposes \(\ell\) independent binary constraints on the union (for \(2\ell<n\)). Independent disjoint length-\(k+1\) trials for \(10^k\) show that the maximum run of \(0\)'s has length at least \(k\), except with probability at most \(\exp(-\lfloor n/(k+1)\rfloor 2^{-(k+1)})\). On these two events the unique least length-\(\ell\) block starts at the beginning \(i\) of a \(0\)-run of length at least \(k\), with the immediately preceding letter \(1\). It is also the position of the least full rotation.

Now consider changing arbitrarily the \(h-1\) letters in the cyclic interval from \(i-h\) through \(i-2\), leaving position \(i-1\), which contains \(1\), fixed. The length-\(\ell\) block at \(i\) is unchanged. A competing length-\(\ell\) block that changes must begin in the interval from \(i-\ell-h\) through \(i-2\). In order to become lexicographically no larger than the block at \(i\), it would have to start with at least \(k\) zeros. Its first \(k\) coordinates cannot cross the fixed \(1\) at \(i-1\). They are therefore disjoint from the run starting at \(i\) and contain at least \(k-(h-1)\) originally zero coordinates outside the edited interval. For each ordered choice of \((i,j)\) the probability of this simultaneous occurrence is at most \(2^{-2k+h-1}\). A union bound over at most \(n(\ell+h)\) such pairs gives failure probability
\[
O_h\bigl(n(\ell+h)2^{-2k+h-1}\bigr)=O_h(\log n/\sqrt n).
\]
Thus, with probability \(1-O_h(\log n/\sqrt n)\), *all* \(2^{h-1}\) modifications leave the same unique least rotation and preserve primitivity. This good set is itself invariant under the modifications, because the entire family of alternatives and the winning index are unchanged. Consequently the modifications act freely and transitively on the \(2^{h-1}\) predecessor patterns. Under the fair product measure, these patterns are therefore **exactly equiprobable on the good set**. Conditioning on primitivity only changes the error by an exponentially small amount. Hence for every \(v\in\{0,1\}^{h-1}\),
\[
\Pr\bigl(L_n\text{ ends with }v1\bigr)=2^{-(h-1)}+O_h(\log n/\sqrt n).
\]
The preceding \(k\) consecutive zeros become the first \(k\) letters of the Lyndon representative, proving fixed-prefix freezing with the same error bound.

**3. Saturation of all interior neighborhoods.** Fix a binary block \(b\) of length \(d\) and a positive threshold \(t\). In a fair word, inspect \(\lfloor n/d\rfloor\) pairwise disjoint locations: the number of occurrences of \(b\) at these locations is binomial with fixed positive success probability \(2^{-d}\), so it exceeds \(t+2d\) except with probability \(e^{-\Omega_{b,t}(n)}\). Passing to the least rotation preserves cyclic occurrences and loses at most \(2d\) occurrences near the two linear endpoints. Thus every fixed binary block appears at least \(t\) times strictly in the interior, with exponentially high probability.

**4. Logical locality and effectiveness.** The Gaifman degree of a successor word is at most \(2\). Effective bounded-degree Hanf locality supplies, from any sentence \(\varphi\), a radius \(R\) and count threshold \(T\) such that truth depends only on radius-\(R\) rooted-neighborhood counts truncated at \(T\). Put \(h=2R+1\). On the high-probability event, all interior neighborhoods occur more than \(T\) times; all boundary-neighborhood counts are fixed by the prefix \(0^h\) and a suffix \(v1\) of length \(h\). For each of the \(2^{h-1}\) suffixes, construct a sufficiently long deterministic binary word beginning with \(0^h\), ending with that suffix, and containing every length-\(2R+1\) binary block more than \(T+4R\) times in the interior. Such a word can be built by concatenating explicit copies of all binary blocks. Evaluate \(\varphi\) on these representatives. The set of accepting suffixes is finite and computable; its cardinality divided by \(2^{h-1}\) is \(p_\varphi\). The switching and saturation errors yield the asserted \(O_\varphi(\log n/\sqrt n)\) convergence rate.

**5. Exact spectrum.** Every limit above is dyadic. Conversely, for any \(m\ge0\) and any integer \(0\le a\le2^m\), choose \(a\) distinct binary patterns of length \(m\) and take the first-order disjunction asserting that those patterns occur in the \(m\) positions immediately preceding the last position. Since the last letter is \(1\), the limiting probability is exactly \(a/2^m\). This realizes every dyadic rational in \([0,1]\).

## Verification
Run `python3 checker.py` using a standard Python installation. The checker exhaustively enumerates all binary words of lengths \(2\) through \(16\), verifies the Witt–Möbius Lyndon counts, and checks that the least rotation starts at a longest cyclic zero-run and ends in \(1\). It also samples canonical rotations at three larger lengths and displays terminal-window frequencies; the limiting law is **not** inferred from finite samples. A successful replay prints `LYNDON_EXACT_OK 131068 8798 12`.

## Relationship to prior work
Markström and Räty (arXiv:2610.22218v1, first public 15 October 2026) establish first-order logical limit laws for small permutation classes using regular-language encodings; their theorem neither covers the nonregular language of all binary Lyndon words nor supplies this terminal-window classification. The Lyndon language is nonregular, for instance its intersection with \(0^+10^+1\) contains exactly \(0^a10^b1\) with \(a>b\ge1\). Marchand and Zohoorian Azad (arXiv:math/0407016v1, 2004) establish the probabilistic reduction to primitive necklaces and the asymptotics of the standard right-factor length; their long-run/block techniques are prior foundations, not claimed as new. Zohoorian Azad and Chassaing (arXiv:1004.4062, original 2010, later version 2021) generalize results on Lyndon factor lengths. Neither inspected analysis yields the explicit fixed-terminal-window switching lemma or the first-order successor-spectrum statement. Effective Hanf locality is classical; the new mathematical step here is the probabilistic reduction to one-sided boundary data. The dyadic *numerical set* also occurs for other random-word models, so numerical coincidence alone is not asserted as novelty.

## Limitations
The theorem does not apply unchanged to a full order symbol, a palindrome or rotation comparison predicate, unlabelled necklaces without a chosen root, other alphabet distributions, or logics stronger than first order. The convergence constant depends on the fixed sentence, and the \(O_\varphi(\log n/\sqrt n)\) rate is not claimed optimal. Priority relative to unlocated general theorems on extremal-rotation local limits remains a risk. No independent scientific validation has been performed.

## References
1. K. Markström and E. Räty, *Logical isomorphism and logical limit laws for small permutation classes and regular languages*, arXiv:2610.22218v1 (15 October 2026), https://arxiv.org/html/2610.22218v1.
2. R. Marchand and E. Zohoorian Azad, *Limit law of the length of the standard right factor of a Lyndon word*, arXiv:math/0407016v1 (1 July 2004), https://arxiv.org/pdf/math/0407016.
3. E. Zohoorian Azad and P. Chassaing, *Asymptotic behavior of some factorizations of random words*, arXiv:1004.4062, https://arxiv.org/pdf/1004.4062.
4. L. Libkin, *Elements of Finite Model Theory*, Springer (2004), bounded-degree Hanf locality.
