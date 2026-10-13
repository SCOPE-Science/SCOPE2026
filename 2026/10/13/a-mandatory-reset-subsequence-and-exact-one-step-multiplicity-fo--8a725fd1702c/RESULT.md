# A mandatory reset subsequence and exact one-step multiplicity for the Černý automata

## Finding
For every \(n\ge2\), in the standard \(n\)-state Černý automaton defined below, let
\[
W_n=b(a^{n-1}b)^{n-2},\qquad L_n=(n-1)^2.
\]
Every reset word contains \(W_n\) as a **scattered subsequence**, and \(W_n\) is itself a reset word. It is therefore the unique shortest reset word. The number of distinct reset words of the first longer length is exactly
\[
\boxed{R_n(L_n+1)=n^2-4n+7.}
\]
The statement includes \(n=2\); the first values for \(n=2,3,4,5,6,7,8\) are \(3,4,7,12,19,28,39\). This counts literal binary input words, without quotienting by relabelings, automorphisms, or final states.

## Assumptions and scope
The state space is \(Q=\mathbb Z/n\mathbb Z\). Words act in reading order from left to right. The two total deterministic input letters are
\[
a(i)=i+1\pmod n,\qquad b(i)=\begin{cases}0&i=n-1,\\i&0\le i<n-1.\end{cases}
\]
A reset word sends all of \(Q\) to a single state. A scattered subsequence is obtained by deleting any number of input letters while preserving the order of remaining letters (the retained letters need not be adjacent). The exponent in \(a^{n-1}\) denotes repetition, not composition in the opposite order. No transition costs or partial transitions are considered.

## Proof
**Step 1: an unavoidable scattered subsequence.** Fix any reset word \(v\), and follow separately the trajectories of all \(n\) initial states \(i\in Q\). Let \(A\) be the number of letters \(a\) in \(v\), and \(B_i\) the number of letters \(b\) read when the trajectory starting at \(i\) is at state \(n-1\). A letter \(a\) increases the current state by one modulo \(n\); a letter \(b\) increases it by one modulo \(n\) exactly in the \(B_i\) recorded instances. Therefore the final state of trajectory \(i\) is
\[
i+A+B_i\pmod n.
\]
Since all final states agree, the \(n\) nonnegative integers \(B_0,\ldots,B_{n-1}\) have pairwise distinct residues modulo \(n\). Consequently one is at least \(n-1\). On that particular trajectory, every counted \(b\) changes state \(n-1\) to \(0\); before the next counted \(b\) the trajectory must traverse the cycle from \(0\) back to \(n-1\), requiring at least \(n-1\) occurrences of \(a\). Other \(b\)'s along this interval do not change that trajectory. Choosing the first \(n-1\) counted \(b\)'s and \(n-1\) intermediate \(a\)'s between consecutive choices displays \(W_n\) as a subsequence of \(v\).

**Step 2: attainment and uniqueness at shortest length.** After the first \(b\), the image is \(S_1=\{0,\ldots,n-2\}\). For \(1\le j<n-1\), applying \(a^{n-1}b\) to \(S_j=\{0,\ldots,n-j-1\}\) gives \(S_{j+1}=\{0,\ldots,n-j-2\}\): the rotation shifts the set backward one step and the last \(b\) merges the predecessor \(n-1\) into \(0\). Thus \(QW_n=\{0\}\). There are \(n-1\) letters \(b\) and \((n-2)(n-1)\) letters \(a\) in \(W_n\), so its length is \(L_n=(n-1)^2\). The necessary subsequence lower bound proves optimal length and forces any reset word of length \(L_n\) to equal \(W_n\) literally.

**Step 3: insertions of \(a\).** A reset word of length \(L_n+1\) must be obtained by inserting a single letter into \(W_n\), by Step 1. Prefixing with \(a\) preserves reset because \(Qa=Q\); suffixing with \(a\) preserves the singleton image. Inserting \(a\) into any of the \(n-2\) intervening rotation runs changes one \(a^{n-1}\) to \(a^n\). If it follows the \(j\)-th \(b\), the image is then \(S_j\), still missing \(n-1\), so the next \(b\) is the identity on this image, and only \(n-j-2\) subsequent \(b\)'s remain. Starting with \(n-j\) states, they can lower the rank by at most \(n-j-2\), leaving at least two states. Consequently exactly the two endpoint insertions of \(a\) reset.

**Step 4: insertions of \(b\).** Inserting \(b\) directly next to one of the \(n-1\) existing \(b\)'s is harmless because \(b^2=b\) as a transformation. Such insertions give exactly \(n-1\) distinct words (count each existing \(b\) once, not both sides separately). For an insertion within the rotation block after the \(j\)-th \(b\), with \(1\le j\le n-2\), let \(t\) be the number of its \(a\)'s preceding the insertion, with \(1\le t\le n-2\). Immediately before the extra \(b\), the image is the cyclic interval \(T=a^tS_j\), whose \(n-j\) occupied coordinates start at \(t\). If \(t<j\), it misses \(n-1\), so the extra \(b\) fixes the image. If \(t>j\), it contains both \(0\) and \(n-1\), so the extra \(b\) strictly reduces the image by removing \(n-1\); the originally resetting suffix then still resets the smaller image, by monotonicity of set images.

For \(t=j\), the interval is \(\{j,\ldots,n-1\}\), and the extra \(b\) moves \(n-1\) to the previously vacant state \(0\) instead of compressing. If \(j=n-2\), direct application of the remaining \(a^{n-1-j}b\) leaves \(\{0,1\}\), not a singleton. Otherwise put \(m=n-j-1\ge2\). After the next originally present \(b\), the image is
\[
P_m=\{0,1,\ldots,m-2\}\cup\{m\}.
\]
On these sets, the ordinary block map \(F(S)=b(a^{n-1}S)\) satisfies \(F(P_r)=P_{r-1}\) for \(r\ge3\), while \(F(P_2)=\{0,1\}\). Exactly \(m-1\) such blocks remain, so the final image is again \(\{0,1\}\). Thus precisely the single interior position \(t=j\) is forbidden in each of the \(n-2\) blocks.

There are \(n-3\) safe nonadjacent positions in each of \(n-2\) blocks when \(n\ge3\), and none when \(n=2\). These words are all distinct from each other and from the adjacent-\(b\) and endpoint-\(a\) insertions. Therefore
\[
R_n(L_n+1)=2+(n-1)+(n-2)(n-3)=n^2-4n+7,
\]
where the same expression also gives \(3\) at \(n=2\). This proves the assertion for all \(n\ge2\).

## Verification
Two independent executable checks accompany this result. `verify_dynamic.py` performs exact subset-image dynamic programming over *all* binary input words of lengths \(L_n\) and \(L_n+1\) for each \(2\le n\le12\); it reproduces a unique shortest reset word and the asserted counts. `verify_insertion.py` independently simulates each state under every possible one-letter insertion into \(W_n\) for all \(2\le n\le30\), producing exactly the asserted number of reset insertions. Both programs were executed successfully; output manifests are embedded. These computations test small cases and do not replace the all-\(n\) argument above.

## Relationship to prior work
The Černý family and its classical extremal shortest-reset length \((n-1)^2\) are old. Kisielewicz, Kowalski and Szykuła's 2013 open-access primary article studies shortest-word algorithms, not the number of reset words one symbol longer or the mandatory scattered-subsequence statement. A published later result on \(k\)-avoiding thresholds of the Černý family proves a different invariant, \(kn\) for avoiding a worst \(k\)-set, by reverse subset actions; it does not entail a count of near-shortest reset input words or the letter-event subsequence invariant here. Recent complexity work concerning synchronized words and subsequence ordering addresses problems over arbitrary DFAs rather than this exact reset language. The claimed new contribution is only the mandatory subsequence structural property and the closed first-excess count, not the automaton construction or shortest-reset length.

## Limitations
The characterization is necessary, not sufficient: containing \(W_n\) as a scattered subsequence does not ensure that an arbitrary longer word resets. The count concerns **only length \(L_n+1\)**, not other excess lengths or other automata. The proof treats complete deterministic two-letter automata with the specified transitions and labeled words. A comprehensive search cannot rule out equivalent statements in older literature under other names; independent literature audit has not been performed.

## References
1. A. Kisielewicz, J. Kowalski and M. Szykuła, *Computing the shortest reset words of synchronizing automata*, Journal of Combinatorial Optimization 29 (2015), 88–124; first online 17 November 2013, https://doi.org/10.1007/s10878-013-9682-0 .
2. R. Ferens, M. Szykuła and V. Vorel, *Lower Bounds on Avoiding Thresholds*, MFCS 2021, https://doi.org/10.4230/LIPIcs.MFCS.2021.46 .
3. *Exact k-avoiding thresholds of the Černý automata*, published research record, https://raw.githubusercontent.com/published-finding corpus/2026/main/2026/9/17/SCOPE-cerny-k-avoiding-thresholds--5cdbaf373a0f/RESULT.md .
4. *Synchronizing words and monoid factorization, yielding a new parameterized complexity class?*, Mathematical Structures in Computer Science (2022), https://www.cambridge.org/core/journals/mathematical-structures-in-computer-science/article/synchronizing-words-and-monoid-factorization-yielding-a-new-parameterized-complexity-class/2910A2134026357AC684F256DB5C0349 .
