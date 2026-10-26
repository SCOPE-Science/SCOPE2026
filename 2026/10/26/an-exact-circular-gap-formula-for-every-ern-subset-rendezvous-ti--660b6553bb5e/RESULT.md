# An exact circular-gap formula for every Černý subset rendezvous time

## Finding

For every integer \(n\ge2\), consider the deterministic automaton on \(Q=\mathbb Z/n\mathbb Z\) with letters \(a(i)=i+1\pmod n\) and \(b(0)=1\), with \(b\) fixing all other states. For every nonempty subset \(S\subseteq Q\), let \(t(S)\) be the minimum length of a word sending all states of \(S\) to one state.

For \(|S|=1\), \(t(S)=0\). Otherwise, let \(p_S(x)\) be the predecessor of \(x\) among members of \(S\) in cyclic order and define \(g_S(x)=(x-p_S(x))\bmod n\in\{1,\ldots,n-1\}\) and \(r(x)=(-x)\bmod n\in\{0,\ldots,n-1\}\). Then the exact distance for **every** prescribed subset is

\[
t(S)=\min_{x\in S}\left[r(x)+n\bigl(n-g_S(x)-1\bigr)+1\right].
\]

For any minimizer \(x\), an explicit shortest merging word, read from left to right, is

\[
a^{r(x)}\bigl(ba^{n-1}\bigr)^{n-g_S(x)-1}b.
\]

Equivalently, the integer-valued function \(F(S)=n(n-1)+1-\max_{x\in S}\{ng_S(x)-r(x)\}\) on nonsingleton subsets is the exact shortest distance to the singleton layer. Consequently an optimal length and a compressed optimal word are computable from the ordered occupied states in linear time.

## Assumptions and scope

The alphabet consists of the two transformations just defined; no arbitrary synchronizing automaton is covered. The integer \(n\) is quantified over all \(n\ge2\), and \(S\) is every nonempty set of distinct initial states. Word concatenation is interpreted left to right. The residue representative used for \(r(x)\) is always in \(\{0,\ldots,n-1\}\). Cyclic predecessor and gap apply only when \(|S|\ge2\). The exponent \(n-g_S(x)-1\) is always a nonnegative integer.

## Proof

**1. Upper bound and constructive optimal candidate.** Fix \(x\in S\) and rotate by \(a^{r(x)}\); the state \(x\) becomes \(0\). By the predecessor definition, every other occupied state is represented in \(\{1,\ldots,n-g_S(x)\}\), and the maximal such state is exactly \(n-g_S(x)\). One block \(ba^{n-1}\) acts on state representatives as \(j\mapsto\max\{j-1,0\}\): both \(0\) and \(1\) map to \(0\), while each \(j\ge2\) maps to \(j-1\). After \(n-g_S(x)-1\) such blocks, all images lie in \(\{0,1\}\). The final \(b\) maps both to \(1\). The displayed word therefore synchronizes \(S\) and has length \(r(x)+n(n-g_S(x)-1)+1\).

**2. A one-step lower-bound potential.** For nonsingleton \(T\), write

\[
H(T)=\max_{x\in T}\bigl(ng_T(x)-r(x)\bigr),\qquad F(T)=n(n-1)+1-H(T),
\]

and extend \(F\) to singleton sets by \(F(T)=0\). Because every cyclic gap is at most \(n-1\) and \(r(x)\ge0\), \(F(T)\ge1\) for nonsingletons.

We prove that for either letter \(c\in\{a,b\}\),

\[
F(cT)\ge F(T)-1
\]

for all nonempty \(T\). The notation \(cT\) denotes the pointwise image of \(T\). If \(c=a\), gaps are unchanged by rotation. For each old state \(x\ne0\), its new score \(ng-r\) increases by exactly \(1\), because \(r(a(x))=r(x)-1\); for \(x=0\), its score decreases by \(n-1\). Hence \(H(aT)\le H(T)+1\) when \(|T|\ge2\).

For \(c=b\), if \(0\notin T\) the set is fixed. Suppose \(0\in T\) and \(|T|\ge2\). If \(1\notin T\), the point \(0\) moves to \(1\) and the size is unchanged. Its gap increases by \(1\), and its score changes from \(ng_T(0)\) to \(ng_T(0)+1\); the score of its old cyclic successor decreases by \(n\); all other scores are unchanged. If \(1\in T\) and \(bT\) is not a singleton, \(0\) is deleted; the successor \(1\) acquires score \(ng_T(0)+1\), and all other scores are unchanged. In both cases \(H(bT)\le H(T)+1\). The only nonsingleton-to-singleton transition is \(T=\{0,1\}\) under \(b\). Its gap at \(0\) is \(n-1\), so \(H(T)=n(n-1)\), \(F(T)=1\), and the one-step inequality still holds. A singleton remains a singleton under both letters, so the inequality also holds there.

Therefore every letter reduces \(F\) by **at most one**. Any word sending \(S\) to a singleton has length at least \(F(S)\).

**3. Sharpness.** Expanding the definition of \(F\) gives

\[
F(S)=\min_{x\in S}\bigl[r(x)+n(n-g_S(x)-1)+1\bigr].
\]

Part 1 provides a word of this exact length, proving the equality and the construction for every \(n\) and every nonempty \(S\).

## Verification

A standalone standard-library checker `verify.py` independently constructs all one-letter transitions in the subset automaton for each \(2\le n\le15\). It computes exact distances by reverse breadth-first search from every singleton, then compares the obtained distance with the circular-gap formula for all \(65{,}518\) nonempty subsets across those values. It also checks the classical full-set threshold \((n-1)^2\). It prints `CERNY_SUBSET_GAP_PASS n=2..15 subsets=65518` on success. The all-\(n\) proof is the potential argument above; finite tests alone would not establish it.

## Relationship to prior work

Behague and Johnson define the weight of an individual \(k\)-set and investigate minima and maxima over all \(k\)-sets of an automaton. In particular, they cite Cardoso's construction of a heavy \(k\)-set in the Černý automaton and state exact results about certain minimum weights. Those size-wise extremal bounds do not specify the shortest synchronization time for each labeled subset. This result supplies the complete pointwise distance function across all subset sizes. The classical full-set reset time and special pair distances are recognized as prior facts and are **not** asserted as new.

The general subset-power-automaton shortest-path method, including improved implementations, is also established in the literature. The contribution is a direct closed formula and an explicit optimal word for the classical family, requiring no exponential state-space search. A previous exact pair-distance labeling likewise addresses only two-state subsets. Cardoso's thesis was identified as particularly relevant, but its complete text was not accessible for this review; possible coverage under another formulation remains an originality risk.

## Limitations

The formula is confined to the standard two-letter Černý family with the stated labeling; it is not a bound for all synchronizing automata, nor a new proof of the general Černý conjecture. It establishes no uniqueness or enumeration of shortest words, and it does not claim novel pair-only or full-state results. Exhaustive verification covers only \(n\le15\), although the proof covers every \(n\ge2\). The 2014 Cardoso thesis was not fully inspected; a later independent mathematical audit has not been performed.

## References

1. N. C. Behague and J. R. Johnson, *Synchronizing Times for \(k\)-sets in Automata*, arXiv:2008.12166 (first public 2020-08-27); *Electronic Journal of Combinatorics* 29(3), P3.41 (2022), DOI 10.37236/9819. https://arxiv.org/abs/2008.12166
2. A. F. P. Cardoso, *The Černý Conjecture and Other Synchronization Problems*, Ph.D. thesis, Universidade do Porto (2014), DOI 10.34626/607f-t921. A relevant prior bound is cited in reference 1; the full thesis was not inspected here.
3. M. Szykuła and A. Zyzik, *An Improved Algorithm for Finding the Shortest Synchronizing Words*, arXiv:2207.05495 (2022). https://arxiv.org/abs/2207.05495
