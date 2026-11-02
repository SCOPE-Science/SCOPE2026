# Exact length-three one-deletion covering over every even alphabet

## Finding
For every **even integer** \(q\ge 2\), let \(D(q,3,1)\) be the minimum size of a set of length-three \(q\)-ary words whose distinct outputs after **exactly one deletion** cover all \(q^2\) ordered words of length two. Then
\[
\boxed{D(q,3,1)=\left\lceil\frac{q^2}{3}\right\rceil.}
\]
A construction attaining the bound is specified by ten independently checkable finite witnesses and the standard existence theorem for three-uniform group-divisible designs. The published odd-alphabet case is separate prior work; the theorem above proves the complementary even-alphabet case.

## Assumptions and scope
The alphabet is the labeled set \(\Sigma_q=\{0,1,\ldots,q-1\}\), with even integer \(q\ge2\). A deletion removes **one** symbol from its original position; repeated results are counted only once. A covering code \(C\subseteq\Sigma_q^3\) has the property that for each ordered pair \((x,y)\in\Sigma_q^2\), some \(w\in C\) has \((x,y)\) among its three length-two subsequences. No assumptions about linearity, alphabet arithmetic, or coding rate are made.

A *three-group-divisible design*, abbreviated \(3\)-GDD, is a finite set partitioned into groups together with three-element blocks, each meeting any group in at most one point, such that each pair from different groups belongs to exactly one block. The all-parameter result uses the published existence characterization for designs of type \(6^t u^1\).

## Proof
**1. Universal lower bound.** Every length-three word has at most three distinct length-two one-deletion outputs. Since there are exactly \(q^2\) ordered outputs, every covering code has at least \(\lceil q^2/3\rceil\) codewords.

**2. A directed-edge/triple certificate.** On \(q\) alphabet symbols, suppose we have one ordered pair \((a,b_a)\) with \(b_a\ne a\) for every symbol \(a\), and a family \(T\) of three-element subsets, such that every *unordered* pair of distinct symbols is either \(\{a,b_a\}\) for some \(a\) or is contained in a member of \(T\). Add the \(q\) codewords \((a,b_a,a)\), and for each \(\{a,b,c\}\in T\) with \(a<b<c\), add both \((a,b,c)\) and \((c,b,a)\). The deletion ball of \((a,b_a,a)\) contains \((a,a)\), \((a,b_a)\), and \((b_a,a)\). The two words for a triple cover both orientations of all three unordered pairs within that triple. Thus this is a covering code of size **at most** \(q+2|T|\). When \(q+2|T|=\lceil q^2/3\rceil\), the lower bound forces all codewords to be distinct and the construction to be optimal.

**3. Exactly certified finite seeds.** For
\[
q\in\{2,4,6,8,10,12,14,16,20,22\},
\]
the file `data/base_witnesses.json` lists one outgoing directed edge per vertex and respectively
\[
|T|\in\{0,1,3,7,12,18,26,35,57,70\}.
\]
The standalone Python checker `verify.py`, requiring only the standard library, constructs the corresponding words, removes each of their three symbols and compares the **entire** resulting set with \(\Sigma_q^2\); it also checks the required sizes, distinctness of the words, and all stated edge/triple structural conditions. The exact code cardinalities are, respectively,
\[
2,6,12,22,34,48,66,86,134,162
=\left\lceil q^2/3\right\rceil.
\]
This is a finite fully enumerated verification, **not** an inference from sampling, an optimizer status, or a numerical tolerance. Its input witnesses are complete immutable data in the accompanying package.

**4. Every remaining even alphabet via \(3\)-GDDs.** Colbourn–Hoffman–Rees's existence theorem, reproduced precisely as Lemma 1.1 of Chang–Chee–Zhou [3], states that a \(3\)-GDD of type \(g^tu^1\) exists when the specified five numerical admissibility conditions hold. Set \(g=6\), \(t\ge3\), and \(u\in\{0,8,10\}\). All conditions hold: \(t\ge3\); \(u\le6(t-1)\) because \(u\le10\); \(6(t-1)+u\) is even; \(6t\) is even; and
\[
\frac{6^2t(t-1)}2+6tu=18t(t-1)+6tu\equiv0\pmod3.
\]
When \(u=0\), the extra zero-sized group is ignored. These types realize respectively all sufficiently large even alphabet sizes congruent to \(0,2,4\pmod6\):
\[
q=6t,\quad q=6t+8,\quad q=6t+10\qquad(t\ge3).
\]
Partition the alphabet according to the GDD. Within each six-point group insert a relabeled copy of the \(q=6\) seed code. If there is one group of eight or ten points, insert its corresponding seed code as well. For every transversal three-point design block add the two oppositely ordered codewords described in step 2. The local seed words cover every pair in one group, including loops; the opposite block words cover both orientations of every cross-group pair, since each cross-group unordered pair belongs to exactly one block. Consequently the assembled code covers the entire output space.

Let the group sizes be \(g_1,\ldots,g_s\), where all but at most one equal six and the exceptional size is either eight or ten. The number of transversal design blocks is
\[
B=\frac{q^2-\sum_i g_i^2}{6},
\]
because each block contains three cross-group unordered pairs. Each six-point group uses exactly \(6^2/3=12\) local words; the optional exceptional group has exactly \((u^2+2)/3\) local words. Thus the total number of assembled words is
\[
\sum_i\left\lceil\frac{g_i^2}{3}\right\rceil+2B
=\frac{q^2+\varepsilon}{3},
\]
where \(\varepsilon=0\) for \(u=0\), and \(\varepsilon=2\) for \(u\in\{8,10\}\). Since \(q^2\equiv0\pmod3\) in the first case and \(q^2\equiv1\pmod3\) in the others, this equals \(\lceil q^2/3\rceil\).

**5. Exhaustion of even sizes.** The sizes not included in the three \(t\ge3\) families are exactly \(2,4,6,8,10,12,14,16,20,22\), already checked in step 3. Hence the upper construction and universal lower bound agree for **every even** \(q\ge2\).

## Verification
Execute `python3 verify.py` from the directory containing this file, `verify.py`, and the `data` folder. The supplied `verification_output.txt` records `VERIFY_OK` and ten full-cover checks. The checker constructs every base codeword, independently derives its deletion ball, checks all \(q^2\) targets for each base size, and verifies the cross-group block-count algebra on parameter ranges \(3\le t\le100\). The **infinite** existence of the GDDs is supplied by the cited published theorem, and the symbolic congruences above cover all \(t\ge3\); a finite program does not purport to certify an infinite existence theorem by enumeration.

## Relationship to prior work
Xie, Sun and Ge [1] define \(D(q,n,R)\) exactly as used here, prove the counting lower bound and asymptotically tight large-alphabet deletion coverings, and construct general nonbinary single-deletion covers via differential VT completion; neither their Theorem V.1 nor V.3 gives the exact fixed-length-three even-alphabet optimum. Lenz, Rashtchian, Siegel and Yaakobi [2] give general insertion/deletion covering inequalities and constructions, not this exact all-even finite-length statement. The structural design theorem [3,4] provides cross-group triples but does not, by itself, address ordered deletion outputs or equal-symbol outputs; the local certificates and their orientation form the necessary coding-theoretic bridge.

An earlier publicly indexed mathematical finding [5] establishes the **same numerical value for odd** \(q\ge3\), using a quadratic-leave triple-system approach. Those results are credited; the proved even family is not a corollary of an odd-only quantifier. Combining that prior odd case with the present even case yields the numerical all-alphabet identity, but the present finding **claims only even alphabets**.

## Limitations
The theorem fixes source length three, exactly one deletion, and even alphabets. The finite seeds are explicitly stored and checked; an optimal code is proven to **exist** at each size, without classifying all optimal codes or giving a polynomial-time algorithm to construct the auxiliary \(3\)-GDD at arbitrary size. The conclusion relies on the published \(3\)-GDD existence theorem; its proof is not reproduced. The exact numerical claim is mathematically supported, but independent priority searches cannot exclude all unindexed literature. No claims are made for longer source words, several deletions, or deletion-error *correction*.

## References
1. C. Xie, Y. Sun and G. Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379v1, 13 June 2026, Section V, https://arxiv.org/abs/2606.15379 (open full text: https://pdfs.assets.alphaxiv.org/2606.15379v1.pdf).
2. A. Lenz, C. Rashtchian, P. H. Siegel and E. Yaakobi, *Covering Codes using Insertions or Deletions*, arXiv:1911.09944v4, https://arxiv.org/abs/1911.09944 (open full text: https://pdfs.assets.alphaxiv.org/1911.09944v4.pdf).
3. Y. Chang, Y. M. Chee and J. Zhou, *A pair of disjoint 3-GDDs of type \(g^tu^1\)*, arXiv:1008.4408v1 (2010), Lemma 1.1, https://arxiv.org/pdf/1008.4408.
4. C. J. Colbourn, D. G. Hoffman and R. Rees, *A new class of group divisible designs with block size three*, Journal of Combinatorial Theory A 59 (1992), 73–89, DOI:10.1016/0097-3165(92)90099-G.
5. *Exact length-three single-deletion covering number for odd alphabets* (publicly indexed mathematical result, 2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-length-three-single-deletion-covering-number-for-odd-alpha--9607d49b27ed. The publicly available complete RESULT.md explicitly states that even alphabet sizes remain unsettled by that odd-alphabet theorem.
