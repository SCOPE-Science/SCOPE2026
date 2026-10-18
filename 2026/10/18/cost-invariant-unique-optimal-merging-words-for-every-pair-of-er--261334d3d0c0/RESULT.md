# Cost-invariant unique optimal merging words for every pair of Černý states

## Finding

For every integer \(n\ge3\), every two distinct states \(0\le i<j<n\) of the standard \(n\)-state Černý automaton have a **unique** shortest merging word, and the same word minimizes cost for **every** assignment of positive real costs \(\alpha\) and \(\beta\) to its two letters. Put \(d=j-i\). The minimum cost is
\[
\begin{cases}
\alpha((n-1)d-i)+\beta d,&2d<n,\\
\alpha((n-1)(n-d)-j)+\beta(n-d),&2d\ge n.
\end{cases}
\]
The corresponding pair of letter counts is componentwise minimal among *all* merging words, not merely optimal for the sum of the counts. For unit letter costs, the \(\binom n2\) distinct initial pairs have shortest merging lengths exactly \(1,2,\ldots,\binom n2\), with each length appearing **once**. Their unique optimal paths are nested: a unique word starting at the worst pair passes through every unordered pair exactly once, in descending distance order, until it merges the final pair.

## Assumptions and scope

The state set is \(Q=\{0,\ldots,n-1\}\). The alphabet is \(\{a,b\}\), acting on states on the right, where \(a(x)=x+1\pmod n\), \(b(n-1)=0\), and \(b(x)=x\) for \(x<n-1\). A finite input word *merges* an initial pair \(\{i,j\}\) when the two images coincide. The objective is not to reset all \(n\) states. For positive real numbers \(\alpha,\beta\), an input word with \(A\) letters \(a\) and \(B\) letters \(b\) has cost \(\alpha A+\beta B\); empty words have zero cost. There are no letter costs equal to zero or negative costs in the theorem. Pairs are unordered, normalized as \(i<j\).

## Proof

**1. Candidate cost-to-go.** For each pair \(p=\{i,j\}\), \(d=j-i\), define
\[
L(p)=\alpha((n-1)d-i)+\beta d,\qquad
R(p)=\alpha((n-1)(n-d)-j)+\beta(n-d),\qquad
F(p)=\min\{L(p),R(p)\}.
\]
Set \(F\) equal to zero on a singleton. Both branches are positive on pairs. Indeed the rotation counts in the displayed definitions are nonnegative integers: for \(L\) use \(i\le n-d-1\), and for \(R\) use \(j\le n-1\). Comparing components,
\[
A_L-A_R=(n-1)(2d-n)+d,\qquad B_L-B_R=2d-n.
\]
If \(2d<n\), both differences are strictly negative. If \(2d\ge n\), the \(a\)-count difference is strictly positive and the \(b\)-count difference nonnegative. Hence \(L(p)<R(p)\) exactly for \(2d<n\) and \(R(p)<L(p)\) exactly for \(2d\ge n\), simultaneously for **all** \(\alpha,\beta>0\). No equality case occurs.

**2. Exact one-step inequalities.** If \(j<n-1\), then \(a\) moves the pair to \(\{i+1,j+1\}\), decreasing each of \(L,R\) by exactly \(\alpha\), while \(b\) fixes the pair. Therefore
\[
F(pa)=F(p)-\alpha,
\qquad F(pb)=F(p)>F(p)-\beta.
\]
For \(j=n-1\) and \(i>0\), the actions give \(pa=\{0,i+1\}\) and \(pb=\{0,i\}\), with exact branch identities
\[
L(pa)=R(p)+(n-1)\alpha,\quad R(pa)=L(p)-\alpha,
\]
\[
L(pb)=R(p)-\beta,\quad R(pb)=L(p)+(n-1)\alpha+\beta.
\]
For the pair \(\{0,n-1\}\), \(b\) merges immediately; its \(R\)-branch equals \(\beta\) and is strictly smaller than its \(L\)-branch. Consequently every transition with letter \(x\in\{a,b\}\) satisfies
\(F(px)\ge F(p)-c(x)\). Moreover there is **exactly one** letter attaining equality: for \(j<n-1\) it is \(a\); for \(j=n-1\) it is \(a\) if \(2d<n\), otherwise \(b\). This statement includes the immediate-merger case.

**3. Optimality and uniqueness.** Summing these inequalities along any merging word gives \(\mathrm{cost}(w)\ge F(p)\), since the terminal singleton has potential zero. Following the unique equality letter strictly decreases \(F\) by a positive amount at every step. A finite pair-state space forbids an infinite path of strictly decreasing potentials, and the path cannot stop at a pair because an equality letter is always available. Thus it reaches a singleton at total cost exactly \(F(p)\). If any word departs from the equality letter at the first point of departure, strict inequality yields cost strictly greater than \(F(p)\), proving the **unique** optimum. Step 1 makes the equality policy independent of the positive cost ratio. If a competing word had fewer occurrences of either letter, making that letter sufficiently expensive while keeping the other cost positive would contradict universal optimality. Thus the unique optimal word minimizes both letter counts separately and has the component counts of its selected branch.

**4. Spectrum and nesting.** For unit letter costs, \(L=nd-i\), \(R=n(n-d)-j\). Let \(k=\min(d,n-d)\). If \(k<n/2\), pairs with direct gap \(k\) give the lengths \(nk-i\) for \(i=0,\ldots,n-k-1\), and pairs with direct gap \(n-k\) give the lengths \(nk-j\) for \(j=n-k,\ldots,n-1\). Their union is precisely
\[
\{(k-1)n+1,\ldots,kn\}.
\]
When \(n\) is even and \(k=n/2\), the \(n/2\) pairs with that gap give the final interval
\(\{(k-1)n+1,\ldots,(k-1)n+k\}\). These disjoint intervals concatenate to all integers \(1,\ldots,\binom n2\), each once. The maximum is attained uniquely by \(\{0,\lfloor n/2\rfloor\}\). Under unit costs every chosen equality move decreases \(F\) by one; because every value appears on exactly one pair, the optimal path from the maximum visits all pairs in decreasing order and all other optimal words are its suffixes. This completes the proof.

## Verification

Two stand-alone standard-library programs provide independent finite checks, not substitutes for the all-\(n\) proof. Run `python3 verify_weighted.py`: for every \(3\le n\le40\), it constructs the full two-state transition graph from the letter definitions, uses reverse Dijkstra shortest paths for seven integer pairs of positive letter weights, and compares the resulting costs, strict optimal outgoing transitions, unit-cost spectra, and unique worst pair with the formulas. Run `python3 verify_bruteforce.py`: for every \(3\le n\le23\), forward BFS independently starts at each pair, counts shortest words, constructs a shortest witness, and checks length, uniqueness and separate letter counts. Both terminate with explicit `*_VERIFY_OK` output when all assertions succeed. Arbitrary positive real costs are handled algebraically by the proof, not by finite weight samples.

## Relationship to prior work

Černý's original automata are classical examples with extremal **full-set** reset lengths. Vorel's work concerns subset synchronization thresholds in general binary automata, including complexity and exponential lower bounds, without this all-pair cost-rigidity formula. Gusev's *Synchronizing automata with random inputs* is much closer: its Section 3 explicitly develops the Černý **pair automaton** and studies expected pair-merging times for random input letters. Its complete transition-graph description necessarily contains the finite graph on which our optimal-control problem lives; nevertheless the inspected text concerns expectations, not the parameter-uniform, uniquely shortest deterministic path formula, joint Parikh minimality, or exact bijective unit-distance spectrum. Ruszil investigates general **weighted** automata with approximation algorithms, not exact Černý-pair optimal policies. The contribution here is this joint all-parameter weighted structural statement and its consequences, not the pair-automaton construction itself.

## Limitations

The theorem applies to exactly the specified two-letter Černý transition convention, initial subsets of size two, and strictly positive letter costs; arbitrary DFAs, alternative automaton conventions without relabeling, zero-cost letters, full-state reset words, and larger initial subsets are not covered. The cited pair-automaton literature may make some individual unweighted calculations implicit, and a previously unindexed equivalent weighted characterization cannot be ruled out without independent literature review. This is a mathematical proof and computational reproducibility check, not independent certification.

## References

1. V. Vorel, *Subset Synchronization and Careful Synchronization of Binary Finite Automata*, arXiv:1403.3972v1 (first posted 2014-03-16). https://arxiv.org/abs/1403.3972
2. V. V. Gusev, *Synchronizing Automata with Random Inputs*, arXiv:1404.6731v1 (first posted 2014-04-27), especially Section 3 and the Černý pair-automaton figure. https://arxiv.org/abs/1404.6731
3. J. Ruszil, *Approximation Algorithm for Finding Short Synchronizing Words in Weighted Automata*, arXiv:2103.16185v1 (first posted 2021-03-30). https://arxiv.org/abs/2103.16185
4. M. V. Volkov, *Synchronizing Automata and the Černý Conjecture*, LATA (2008), survey of classical synchronization bounds.
