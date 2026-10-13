# Exact reset thresholds for cyclic automata with one consecutive block collapse

## Finding
For every pair of integers \(n\ge 4\), \(2\le k\le n-2\), consider the complete binary deterministic semiautomaton \(\mathcal A_{n,k}\) on \(Q=\mathbb Z/n\mathbb Z\) with letters
\[
a(i)=i+1\pmod n,\qquad
b(i)=\begin{cases}0,&n-k\le i\le n-1,\\ i,&0\le i<n-k.\end{cases}
\]
Its **exact reset threshold** (the minimum length of a word mapping all states to one state) is
\[
\boxed{R(n,k)=1+\left\lfloor\frac{n-2}{k}\right\rfloor(n-k+1).}
\]
In particular, writing \(L=n-k\) and \(t=\lfloor(n-2)/k\rfloor\), a shortest reset word is
\[
\boxed{b(a^{L}b)^t.}
\]
For fixed \(k\), the reset threshold grows quadratically with \(n\), with leading coefficient \(1/k\). For \(k\) proportional to \(n\), the threshold is linear. The restriction \(k\ge2\) excludes the classical Černý single-merge case, which the formula also recovers when \(k=1\).

## Assumptions and scope
The letters act on the right, from left to right. Thus \(Q\cdot w\) denotes the image of all states under the word \(w\); no initial state or designated accepting states are needed. The second letter fixes \(0,1,\ldots,L-1\) and collapses the consecutive terminal set \(H=\{L,\ldots,n-1\}\) to \(0\). Its image has \(L\) states, so the deficiency is exactly \(k\). All words over \(\{a,b\}\), with arbitrary alternation and repetitions, are included in the minimum. The theorem holds for every integer parameter pair in the displayed domain, not just tested sizes.

## Proof
**Inverse-image rules.** Work backward from a possible synchronized state \(q\). For a subset \(S\subseteq Q\), the preimage under \(a\) is the cyclic translation \(S-1\). Writing \(H=\{L,\ldots,n-1\}\), the preimage under \(b\) is
\[
b^{-1}(S)=\begin{cases}S\cup H,&0\in S,\\S\setminus H,&0\notin S.\end{cases}
\]
A word resets to \(q\) if and only if the full inverse image of \(\{q\}\) under that word is \(Q\). Every inverse-image operation is monotone with respect to inclusion. Therefore a shortest reverse route from a singleton to \(Q\) never uses a \(b^{-1}\) operation that fails to increase the current subset strictly: removing such an operation replaces its output by a superset and cannot prevent eventual coverage of \(Q\). Likewise, between two consecutive useful \(b^{-1}\) operations, at most \(n-1\) inverses of \(a\) are needed, since \(a^n\) is the identity.

**The first expansion.** Before the first useful \(b^{-1}\), inverse rotations leave a singleton. The first strict expansion can occur only at the singleton \(\{0\}\), yielding \(S_0=\{0\}\cup H\). Its complement, the set of states *still missing* in the reverse route, is the ordinary interval
\[
C_0=Q\setminus S_0=[1,L-1].
\]
There are exactly \(L-1\) missing states. For every later useful \(b^{-1}\), the preimage rule removes from the missing set at most the \(k\) positions of \(H\). Therefore, after the first expansion, at least
\[
t=\left\lceil\frac{L-1}{k}\right\rceil=\left\lfloor\frac{n-2}{k}\right\rfloor
\]
further useful inverse \(b\)-steps are required.

**Interval obstruction to faster steps.** We show inductively that immediately after each useful inverse \(b\)-step, provided the missing set is nonempty, it is \(C=[u,L-1]\) for some integer \(1\le u\le L-1\). This holds initially. Suppose it holds at one such step. Let \(r\in\{0,\ldots,n-1\}\) be the number of inverse rotations before the next useful \(b^{-1}\). If \(0\le r<u\), then \(C-r=[u-r,L-1-r]\subseteq[1,L-1]\), so the missing set does not meet \(H\) and the next inverse \(b\) cannot enlarge the state subset. If \(u\le r\le L-1\), the translated missing set contains \(0\); the preimage rule then cannot enlarge the subset. Thus a useful inverse \(b\) requires \(r\ge L\). In this last case, the translated missing set is the ordinary interval
\[
C-r=[n+u-r,n+L-1-r]\subseteq[1,n-1].
\]
It contains no zero, so the useful inverse \(b\) simply intersects it with \([1,L-1]\), leaving either the empty set or another interval \([u',L-1]\). This proves the inductive shape and the lower bound of \(L\) inverse rotations between every two useful inverse \(b\)-steps.

Consequently, each of the \(t\) useful steps after the first costs at least \(L\) copies of \(a^{-1}\) and one copy of \(b^{-1}\). Including the first \(b^{-1}\), every reset word therefore has length at least
\[
R(n,k)\ge 1+t(L+1).
\]
The argument rules out *all* candidate words, not merely words sharing the proposed alternating pattern.

**Attainment.** Starting with missing set \([1,L-1]\), perform exactly \(L\) inverse rotations, then one useful inverse \(b\). If the current nonempty missing set is \([1+jk,L-1]\), the reverse rotations send it to \([1+(j+1)k,n-1]\), and \(b^{-1}\) leaves missing set \([1+(j+1)k,L-1]\), understood as empty when the lower endpoint exceeds the upper endpoint. After \(t=\lceil(L-1)/k\rceil\) repetitions, the missing set is empty. Reversing this route yields the word \(b(a^{L}b)^t\), of length \(1+t(L+1)\), proving equality.

## Verification
A complete stand-alone standard-library Python program is provided in `verify.py`. It independently computes shortest reset words by breadth-first search over all reachable nonempty state subsets for all \(4\le n\le15\), \(2\le k\le n-2\); verifies the symbolic interval-step obstruction across 2,803,079 finite parameter-and-position configurations; and replays the claimed shortest-word construction at several larger sizes, including \(n=317\). It prints `VERIFY_OK` only after all assertions succeed. These are finite cross-checks. The proof of the unrestricted parameter theorem is the preceding inverse-image argument, which is independent of any enumeration cutoff.

## Relationship to prior work
The case \(k=1\) is the classical Černý automaton and its known quadratic reset threshold; our claimed novelty is restricted to the entire consecutive-collapse family with \(k\ge2\). Volkov's unimodal-letter theorem and the semiconstant-letter results of Rystsov and Szykuła establish broad synchronizability statements that include or motivate this family, but their cited theorems do not give the sharp two-parameter shortest-word length. Rystsov and Szykuła's transformation-monoid work derives general quadratic upper bounds for one-point singular automata; that bound is not the exact \((n,k)\) formula. The exact cyclic-interval inverse obstruction and matching construction resolve the length for this specific family. These distinctions are about implications of the stated theorems, not uniqueness of mathematical ideas.

## Limitations
No shortest-word enumeration, uniqueness of the optimal word, or result for nonconsecutive collapsed source sets is claimed. The proof uses the arrangement \(H=[n-k,n-1]\) and its disjoint fixed image \([0,n-k-1]\) essentially. Computational confirmation has finite scope and is not a substitute for the infinite lower bound. Earlier equivalent formulas not detected in the inspected literature remain a bibliographic possibility; no independent audit has been performed.

## References
- M. V. Volkov, *Synchronization of Primitive Automata*, arXiv:2306.13317, first publicly posted 2023-06-23, particularly Theorem 1, Lemma 2, and Corollaries 3 and 5. https://arxiv.org/abs/2306.13317
- I. Rystsov and M. Szykuła, *Primitive Automata that are Synchronizing*, arXiv:2307.01302, first publicly posted 2023-07-03, especially Section 4.3 and Theorem 25. https://arxiv.org/abs/2307.01302
- I. Rystsov and M. Szykuła, *Reset Thresholds of Transformation Monoids*, arXiv:2309.08321, first publicly posted 2023-09-15, especially Section 6 and Corollary 10. https://arxiv.org/abs/2309.08321
- H. Don, *The Černý Conjecture and 1-Contracting Automata*, Electronic Journal of Combinatorics 23(3), #P3.12 (2016). https://doi.org/10.37236/5616
