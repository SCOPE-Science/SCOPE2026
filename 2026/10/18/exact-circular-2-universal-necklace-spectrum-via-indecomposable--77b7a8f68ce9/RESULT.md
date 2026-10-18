# Exact circular 2-universal necklace spectrum via indecomposable permutations

## Finding

Let \(q\ge 2\) and let \(\Sigma\) be a fixed, labeled alphabet of \(q\) distinct letters. A word is *2-subsequence universal* if each of the \(q^2\) length-two ordered words over \(\Sigma\) is a scattered subsequence. A circular word is *circularly 2-universal* if at least one rotation is 2-subsequence universal. Its shortest possible length is \(2q\).

At this length every qualifying word contains each letter twice. A *witness cut-pair* is an unordered pair of opposite boundaries of the circle such that both length-\(q\) arcs are permutations of \(\Sigma\); equivalently the two rotations beginning at the boundaries are 2-subsequence universal. Write \(b\) for the number of distinct witness cut-pairs.

Let \(c_m\) count *sum-indecomposable permutations* on \(m\) letters: permutations with no proper initial segment containing exactly the values \(\{1,\ldots,t\}\). Define \(a_{q,b}\) to be the number of size-\(q\) permutations with exactly \(b\) direct-sum components. These numbers are explicitly determined by the formal ordinary generating series

\[
F(z)=\sum_{m\ge 0}m!z^m,\qquad C(z)=1-\frac1{F(z)},\qquad a_{q,b}=[z^q]C(z)^b.
\]

For every \(q\ge2\) and \(1\le b\le q\), the numbers of qualifying **labeled linear words** and **cyclic necklaces** (rotation only, without reversal or relabeling) having exactly \(b\) witness cut-pairs are respectively

\[
L_{q,b}=\frac{q\,q!}{b}\,a_{q,b},\qquad
N_{q,b}=\begin{cases}\dfrac{q!}{2b}a_{q,b},&b<q,\\ (q-1)!,&b=q.\end{cases}
\]

The exceptional case \(b=q\) consists exactly of the necklaces of doubled permutation words \(PP\), whose rotation orbit has size \(q\), not \(2q\). The total number of qualifying necklaces is

\[
\boxed{N_q=\frac{q!}{2}[z^q]\log\!\left(\frac{\sum_{m\ge0}m!z^m}{1-z}\right)}.
\]

The logarithm is a formal power series, so no analytic convergence of the factorial series is asserted. The number of qualifying labeled words is \(L_q=\sum_{b=1}^q L_{q,b}\). As \(q\to\infty\),

\[
N_q=\frac{(q!)^2}{2}\left(1+O\!\left(\frac1q\right)\right),\qquad
\frac{L_q}{(2q)!/2^q}=\frac{\sqrt{\pi}\,q^{3/2}}{2^q}\left(1+O\!\left(\frac1q\right)\right).
\]

Thus a uniformly random word in which each of \(q\) labeled letters appears twice is circularly 2-universal with exponentially vanishing probability, and almost every *qualifying necklace* has precisely one witness cut-pair as \(q\) grows.

For \(q=2,3,4,5\), the corresponding pairs \((L_q,N_q)\) are \((6,2)\), \((78,14)\), \((1704,216)\), \((55320,5544)\). The novelty claim concerns the all-alphabet, cut-refined theorem, not the earlier ternary \(q=3\) special case.

## Assumptions and scope

All words are finite, and subsequences need not be contiguous. Universality is with respect to the entire fixed alphabet. A necklace is a cyclic-rotation equivalence class of length-\(2q\) labeled words; alphabet permutations and reversal are *not* identified. Opposite boundaries refer to starts separated by exactly \(q\) positions modulo \(2q\). The sums and generating functions are interpreted over rational formal power series, and all big-O constants are absolute.

## Proof

**1. Optimal length and permutation-arc criterion.** The presence of \(aa\) as a subsequence forces two occurrences of each letter \(a\), so any 2-universal word has length at least \(2q\), and equality forces every letter to occur exactly twice. In a word of this minimum length, let \(f_a\) and \(\ell_a\) be the positions of the first and second occurrence of \(a\). For distinct letters \(a,b\), the subsequences \(ab\) and \(ba\) both occur if and only if their closed occurrence intervals \([f_a,\ell_a]\) and \([f_b,\ell_b]\) intersect. Necessity follows by considering the two disjoint-interval orderings; sufficiency follows because an overlap places at least one occurrence of either letter on each side of a suitable occurrence of the other (all positions are distinct). Intervals on a line satisfying pairwise intersection have a common intersection: \(\max_a f_a\le\min_a\ell_a\). In fact the inequality is strict, since all \(2q\) occurrence positions are distinct. Therefore every first occurrence precedes every second occurrence. The first \(q\) positions and the final \(q\) positions are each a permutation of \(\Sigma\). Conversely any concatenation \(PQ\) of two permutations contains every \(aa\) and both \(ab\), \(ba\) for distinct \(a,b\), proving the equivalence. A rotation is therefore 2-universal at the minimum length precisely when its consecutive halves are permutations.

**2. Cuts are sum-decomposition boundaries.** Fix one qualifying rotation \(w=PQ\), where both \(P\) and \(Q\) are permutations. For \(0\le t<q\), the shifted halves, using one-based interval notation, are \(P[t+1..q]Q[1..t]\) and \(Q[t+1..q]P[1..t]\). Each is a permutation exactly when \(\operatorname{set}(P[1..t])=\operatorname{set}(Q[1..t])\). Define \(\pi\in S_q\) by \(\pi_j=\operatorname{rank}_{P}(Q_j)\). This prefix-set condition is equivalent to \(\{\pi_1,\ldots,\pi_t\}=\{1,\ldots,t\}\), exactly a direct-sum component boundary of \(\pi\). Including \(t=0\) but excluding \(t=q\), the number of such \(t\) equals the number \(b\) of components. Each successful cut at \(t\) also gives the opposite successful cut at \(t+q\). Consequently each qualifying necklace has exactly \(2b\) successful starting boundaries and exactly \(b\) antipodal witness cut-pairs. For each \(\pi\) there are \(q!\) choices of \(P\), then a unique \(Q\), so the number of ordered qualifying splits \(P,Q\) with component count \(b\) is \(q!a_{q,b}\).

**3. Rotation orbits and the periodic exception.** A repeated proper block occurring \(r>1\) times in a length-\(2q\) word where each letter occurs exactly twice must have \(r=2\); hence the word is \(PP\), with \(P\) a permutation and fundamental period exactly \(q\). Such words are precisely the case \(\pi=\mathrm{id}\), when \(b=q\). There are \(q!\) such linear words and \((q-1)!\) necklaces, each with \(q\) distinct rotations. Every other qualifying necklace has \(2q\) distinct rotations, exactly \(2b\) of which are successful ordered permutation splits. Therefore \(N_{q,b}(2b)=q!a_{q,b}\) for \(b<q\), and \(N_{q,q}=(q-1)!\). Multiplying by the correct orbit length gives \(L_{q,b}=(2q)N_{q,b}=q\,q!a_{q,b}/b\) when \(b<q\); the same formula at \(b=q\) follows from the \(q\)-element orbits.

**4. Ordinary generating function.** Every permutation decomposes uniquely as an ordered sequence of sum-indecomposable permutations. Thus \(F(z)=(1-C(z))^{-1}\), and \([z^q]C(z)^b=a_{q,b}\). The formal identity \(\log F(z)=\sum_{b\ge1}C(z)^b/b\) gives

\[
N_q=\frac{q!}{2}\sum_{b=1}^q\frac{a_{q,b}}b+\frac{(q-1)!}{2}
=\frac{q!}{2}[z^q]\left(\log F(z)-\log(1-z)\right).
\]

Here the correction replaces the hypothetical \(q!/(2q)\) primitive-orbit count at \(b=q\) by its true double value \((q-1)!\). This proves the displayed logarithmic formula.

**5. Rarity and cut concentration.** A decomposable permutation has a proper initial segment of length \(j\) with values \(\{1,\ldots,j\}\) for some \(1\le j<q\). For fixed \(j\), exactly \(j!(q-j)!\) permutations satisfy this condition. By the union bound,

\[
0\le q!-c_q\le\sum_{j=1}^{q-1}j!(q-j)!=q!\sum_{j=1}^{q-1}\binom qj^{-1}=O(q!/q).
\]

For example, splitting the sum at the two edges and using \(\binom qj\ge\binom q2\) for \(2\le j\le q-2\) proves the last bound. Hence \(a_{q,1}=c_q=q!(1-O(1/q))\) and \(\sum_{b\ge2}a_{q,b}=O(q!/q)\). Inserting these into the exact formulas gives \(N_q=(q!)^2(1+O(1/q))/2\), and \(L_q=q(q!)^2(1+O(1/q))\). Since there are exactly \((2q)!/2^q\) distinct double-occurrence words, division and \(\binom{2q}{q}=4^q/\sqrt{\pi q}\,(1+O(1/q))\) prove the probability limit. The same \(b=1\) dominance proves the claimed concentration among qualifying necklaces.

## Verification

`checker.py` directly enumerates every double-occurrence word for alphabet sizes \(q=2,3,4,5\), for a total of 116016 words. It checks all circular rotations by greedy two-arch factorization; for \(q\le4\), it separately checks every length-two scattered subsequence directly, without invoking the factorization theorem. The verifier computes actual rotation necklaces and witness cut-pair histograms and compares both the labeled and necklace distributions with the direct-sum-component recurrence. Expected necklace spectra by number of cut-pairs are \((1,1)\), \((9,3,2)\), \((156,42,12,6)\), and \((4260,960,240,60,24)\) for \(q=2,3,4,5\) respectively. It also checks exact integer divisibility in every tested bin. Run using `python3 checker.py`. The proof, not finite enumeration, establishes all \(q\).

## Relationship to prior work

Barker, Fleischmann, Harwardt, Manea, and Nowotka introduced circular scattered-factor universality and established the shortest possible length and connections between rotation and universality index (arXiv:2003.04629v1, sections 2 and 4). Fleischmann, Germann, and Nowotka gave general-alphabet results on repeated words and efficient computation of circular universality (arXiv:2104.09063v1, sections 4 and 5). Adamson developed counting and ranking algorithms for *linear* subsequence-universal words (arXiv:2304.04583v1, sections 3–5). Fleischmann’s dissertation (2021, chapter 3) develops circular universality via repetition and permutation actions, likewise without the cut-refined necklace enumeration in the relevant inspected sections. These results motivate the invariant and supply algorithmic context but the inspected statements do not supply the refined necklace counts or direct-sum phase correspondence. An earlier ternary counting result already gives \(N_3=14\) at universality depth two. The new asserted contribution is the alphabet-general distribution by witnessing cut-pairs and its logarithmic generating function and large-alphabet asymptotics, which do not follow from that one ternary value.

## Limitations

The theorem treats universality depth exactly two, the minimum word length \(2q\), labeled alphabets, and rotations only. It does not enumerate longer circularly universal words or universality depth at least three. The asymptotic estimates concern the regime where the alphabet size tends to infinity. Enumeration for \(q\le5\) is a finite cross-check, not a proof beyond those values. A mathematically equivalent statement in unindexed literature or a table of decomposable permutations could exist; the expression in terms of indecomposable permutations is not itself claimed as a newly discovered permutation identity. No independent mathematical audit has been performed.

## References

1. M. Barker, P. Fleischmann, F. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1 (first publicly posted 2020-03-10), https://arxiv.org/abs/2003.04629.
2. P. Fleischmann, S. B. Germann, D. Nowotka, *Scattered Factor Universality — The Power of the Remainder*, arXiv:2104.09063v1 (2021), https://arxiv.org/abs/2104.09063.
3. D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583v1 (2023), https://arxiv.org/abs/2304.04583.
4. P. Fleischmann, *On Special k-Spectra, k-Locality, and Collapsing Prefix Normal Words*, PhD thesis, Kiel University (2021), https://d-nb.info/1231275863/34.
