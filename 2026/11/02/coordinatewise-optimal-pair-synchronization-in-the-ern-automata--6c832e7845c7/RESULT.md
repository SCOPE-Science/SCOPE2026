# Coordinatewise-optimal pair synchronization in the Černý automata

## Finding

For every integer \(n\ge 2\), every unordered pair of distinct states of the standard \(n\)-state Černý automaton has a **unique synchronizing word minimizing cost simultaneously for every pair of strictly positive letter costs**. This word also minimizes the number of each letter separately. Furthermore, the pairwise shortest-word lengths are all different and equal, as an unordered set, to
\[
\bigl\{1,2,\ldots,\tbinom n2\bigr\}.
\]
In particular, there is exactly one unordered pair at every shortest merging length from \(1\) through \(\binom n2\).

Here is the complete formula, including the uniquely optimal word, its letter composition, and its cost. Assign any costs \(c_a>0\) and \(c_b>0\). For a pair \(P\), let \(h\) be the smaller of its two positive directed cyclic distances. If \(h<n/2\), there is exactly one \(i\in\{0,\ldots,n-1\}\) with
\[
P=\{i,(i+h)\bmod n\}.
\]
For this pair the word, its numbers of \(a\)- and \(b\)-letters, and the minimum cost are respectively
\[
W(P)=a^{\,n-1-i}b(a^{n-1}b)^{h-1},\qquad
(A(P),B(P))=\bigl(h(n-1)-i,h\bigr),
\qquad C(P)=c_a A(P)+c_b B(P).
\]
If \(n=2m\) is even and \(h=m\), represent the antipodal pair uniquely as \(P=\{i,i+m\}\) with \(0\le i<m\). In this case
\[
W(P)=a^{\,m-1-i}b(a^{n-1}b)^{m-1},\qquad
(A(P),B(P))=\bigl((m-1)n-i,m\bigr),
\qquad C(P)=c_a A(P)+c_b B(P).
\]
All exponents are nonnegative integers. The formulas for the optimal word are **independent of the actual positive costs**.

## Assumptions and scope

The automaton has state set \(Q=\mathbb Z/n\mathbb Z\), with alphabet \(\{a,b\}\). Its transitions are \(q\mathbin{\cdot}a=q+1\pmod n\) and
\[
q\mathbin{\cdot}b=\begin{cases}0,&q=n-1,\\q,&0\le q<n-1.\end{cases}
\]
A word synchronizes a starting unordered pair when the resulting two states coincide; we stop at the first coincidence. A letter cost is additive and depends only on its letter, not on the state. Costs are arbitrary positive real numbers, not assumed equal or rational. We do not assert uniqueness if either cost is zero.

The pair coordinates \((i,h)\) described above orient each nonantipodal pair along its unique shorter directed arc. For even \(n\), the antipodal orientation convention chooses the representative with \(i<m\). These conventions cover each of the \(\binom n2\) pairs exactly once.

## Proof

**Step 1: a distance potential.** Define \(R(P)=A(P)+B(P)\) using the explicit formulas in the finding, and define \(A(P)\) and \(B(P)\) as displayed. At the synchronized singleton state \(\star\), set \(A(\star)=B(\star)=R(\star)=0\). The coordinate formula becomes
\[
R(P)=\begin{cases}hn-i,&h<n/2,\\ (m-1)n+m-i,&n=2m,\ h=m.\end{cases}
\]
We now verify the following two one-step inequalities for every nonsingleton pair \(P\):
\[
A(P)-A(P\mathbin{\cdot}a)\le1,\quad B(P\mathbin{\cdot}a)=B(P),
\qquad A(P\mathbin{\cdot}b)\ge A(P),\quad
B(P)-B(P\mathbin{\cdot}b)\le1.
\tag{1}
\]
Consequently, for each letter, \(R\) can decrease by at most one.

**Step 2: explicit transition verification.** For \(h<n/2\), rotation \(a\) sends \((i,h)\) to \((i+1,h)\) when \(i<n-1\), decreasing \(R\) by one; at \(i=n-1\), it sends the pair to \((0,h)\), increasing \(R\) by \(n-1\). In the antipodal case \(n=2m\), rotation decreases \(R\) by one when \(i<m-1\), and increases it by \(m-1\) at \(i=m-1\). In every case \(B\) stays unchanged, so the first two inequalities of (1) follow.

The letter \(b\) changes a nonsingleton pair only if it contains \(n-1\). For an ordinary pair with \(i=n-1\), the other state is \(h-1\); the resulting pair is \((0,h-1)\) or the singleton when \(h=1\). For an antipodal pair with \(i=m-1\), the resulting pair is \((0,m-1)\). In both cases \(R\) drops by one and \(B\) drops by one, hence \(A\) is unchanged.

The only other effective \(b\)-transition occurs for an ordinary pair with \(i=n-1-h\), where the pair \(\{n-1-h,n-1\}\) is sent to \(\{0,n-1-h\}\). If \(h+1\le n/2\), its new shorter-arc coordinate has height \(h+1\), and direct substitution (including the antipodal endpoint) shows \(R\) rises by \(n\). Thus \(A\) rises by \(n-1\) and \(B\) rises by one. In the remaining case, \(n=2h+1\), the new height stays \(h\), and \(R\) and \(A\) both rise by \(h\). If \(b\) fixes both states, both potentials stay unchanged. This exhausts all transitions and proves (1), including the boundary cases \(n=2\) and \(n=3\).

**Step 3: componentwise lower bound.** Read any word sending \(P\) to a singleton. Telescoping (1) along its transitions, every \(a\)-letter can decrease \(A\) by at most one while no \(b\)-letter can decrease \(A\), so the word contains at least \(A(P)\) copies of \(a\). Similarly, every \(b\)-letter can decrease \(B\) by at most one while \(a\) keeps \(B\) fixed, so the word contains at least \(B(P)\) copies of \(b\). Every synchronizing word therefore costs at least \(c_a A(P)+c_b B(P)\).

**Step 4: attainability and uniqueness.** For an ordinary pair \((i,h)\), the prefix \(a^{n-1-i}\) rotates the first coordinate to \(n-1\). Then \(b\) reduces the height from \(h\) to \(h-1\), leaving first coordinate zero. Repeating \(a^{n-1}b\) successively reduces the height until the singleton, giving exactly \(W(P)\). For an antipodal pair the same argument begins with \(a^{m-1-i}b\). These words have exactly \(A(P)\) letters \(a\) and \(B(P)\) letters \(b\), hence attain the two coordinatewise lower bounds.

If another word has the same minimum positive weighted cost, the nonnegative deficits in both letter counts must be zero. It therefore has exactly \(R(P)\) letters. At each step, \(R\) can decrease by at most one, so every letter must decrease \(R\) by exactly one. But the transition analysis in Step 2 gives **exactly one** such outgoing letter at every nonsingleton state: it is \(a\) except at the rotation wrap position, where it is \(b\). Thus the entire word is forced and equals \(W(P)\). This proves uniqueness simultaneously for every choice of positive costs.

**Step 5: complete length spectrum.** For each height \(1\le h<n/2\), the \(n\) possible values \(i=0,\ldots,n-1\) yield every integer in the interval
\[
\{(h-1)n+1,\ldots,hn\}
\]
exactly once as \(R(P)\). If \(n\) is odd, these intervals terminate at \(R=\binom n2\). If \(n=2m\), they terminate at \((m-1)n\), and the \(m\) antipodal pairs yield the remaining consecutive values
\[
(m-1)n+1,\ldots,(m-1)n+m=\binom n2.
\]
This proves the exact, multiplicity-one spectrum.

## Verification

Run `python3 verify.py` using Python 3 and its standard library. The code independently enumerates every pair and all transitions for \(2\le n\le50\). It checks the two potential inequalities, exact optimal word and letter counts, unique rank-decreasing transitions, and the complete consecutive length spectrum. For \(2\le n\le17\), reverse Dijkstra calculations independently compute shortest cost and numbers of optimal paths for five positive weight choices \((1,1)\), \((1,4)\), \((4,1)\), \((3,7)\), and \((11,2)\). All tests produce `VERIFY_OK`.

These finite checks do not prove the infinite theorem; Steps 1–5 above do. They are independent computational cross-checks of its critical finite-state transition identities.

## Relationship to prior work

The classical Černý automata provide extremal full-state reset thresholds. Gusev (2014, arXiv:1404.6731v1, Section 3, Lemma 1 and Theorems 3–4) constructs their pair automaton, including a coordinate graph for odd state counts, to derive **expected** random-input time to merge a particularly difficult pair (for both parities). That article's explicit pair graph can be used as an alternative starting point for our analysis; it does **not state** a deterministic formula for the uniquely optimal word of every pair under *all* positive letter costs, the coordinatewise Parikh-minimality theorem, or the multiplicity-one shortest-distance spectrum. Its cycle letter and collapsing letter are named in reverse order from the convention used here, and its state indices are shifted.

Kisielewicz–Kowalski–Szykuła (2013) develop general algorithms to compute shortest reset words, rather than this uniform closed-form weighted all-pair statement. General subsequent results about weighted synchronization concern broader automaton classes and complexity, not this exact same-word-for-every-weight classification. These distinctions concern **claims and logical implications**, not mere title differences. No broad uniqueness assertion about historical publication priority is established here.

## Limitations

This result concerns the explicitly defined two-letter Černý automata and synchronizing individual unordered pairs; it does not imply the same pairwise behavior for general synchronizing automata, subsets of size three or more, state-dependent costs, or zero/negative letter costs. The formula concerns the first merging time, not the shortest full-state reset word. The historical-priority comparison includes accessible primary text but cannot exclude unindexed older notes deriving the same shortest-path spectrum directly from the pair graph. An independent mathematical audit has not been performed.

## References

1. V. V. Gusev, *Synchronizing automata with random inputs*, 2014, arXiv:1404.6731v1 (first public version dated 2014-04-27), Section 3, Lemma 1 and Theorems 3–4. https://arxiv.org/abs/1404.6731 ; author-uploaded complete text: https://www.researchgate.net/publication/261952170_Synchronizing_Automata_with_Random_Inputs .
2. A. Kisielewicz, J. Kowalski, M. Szykuła, *Computing the shortest reset words of synchronizing automata*, Journal of Combinatorial Optimization, DOI:10.1007/s10878-013-9682-0. https://doi.org/10.1007/s10878-013-9682-0 .
3. J. Ruszil, *Approximation algorithm for finding short synchronizing words in weighted automata*, 2021, arXiv:2103.16185. https://arxiv.org/abs/2103.16185 .
