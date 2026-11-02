# Linear minimax blocking-pair degree from cyclic complete roommate preferences

## Finding
For every integer \(n\ge2\), a complete strict Stable Roommates instance exists such that its optimal minimax blocking-pair degree, over **all** partial matchings, equals
\[
\operatorname{OPT}(I_n)=\min_{M}\max_{v}|\operatorname{BP}_v(M)|=\left\lfloor\frac{n-1}{2}\right\rfloor.
\]
Consequently the worst-case optimum among complete-list instances is \(\Theta(n)\), improving the logarithmic lower bound established for unrestricted minimax roommates instances in the motivating literature. The smallest complete-list instance requiring at least two incident blocking pairs in every matching has five agents; that minimum size is also valid when symmetric incomplete acceptability is permitted. No exact universal worst-case leading constant for arbitrary profiles is asserted.

## Assumptions and scope
The agent set is finite, and each agent has a strict preference list covering every other agent, so acceptability is symmetric and complete. An agent prefers any acceptable agent to remaining unmatched. A partial matching is a set of vertex-disjoint unordered pairs, with unpaired agents permitted. An unordered pair \(\{u,v\}\notin M\) blocks \(M\) precisely when both agents strictly prefer one another to their assigned partners (or to remaining unmatched). Let \(\operatorname{BP}_v(M)\) denote the set of blocking pairs containing agent \(v\). No maximum-cardinality restriction is imposed anywhere in the main minimization.

For odd \(n=2k+1\), where \(k\ge1\), label agents by residues \(0,1,\ldots,2k\). Agent \(i\) ranks the other residues in forward cyclic order:
\[
i+1\succ_i i+2\succ_i\cdots\succ_i i+2k\pmod{2k+1}.
\]
For even \(n=2k+2\), where \(k\ge0\), retain this construction on \(2k+1\) core agents (trivial when \(k=0\)), and add an agent \(d\). Every core agent ranks \(d\) last, while \(d\) ranks the core agents in any strict order.

## Proof
**Circular comparison lemma.** For any three distinct core agents \(a,b,u\), exactly one of \(a\) and \(b\) prefers \(u\) over the other endpoint. Indeed, the two clockwise arcs from \(a\) to \(b\) and from \(b\) to \(a\) partition the remaining circle: if \(u\) belongs to the first arc then \(a\) prefers \(u\) to \(b\), whereas \(b\) prefers \(a\) to \(u\); in the other arc the roles reverse. Therefore, relative to a core--core matched pair \(\{a,b\}\), every unmatched core agent blocks with exactly one endpoint.

**Odd order.** Every partial matching on an odd number \(2k+1\) of core agents has \(r\) matched pairs and \(s=2k+1-2r\ge1\) unmatched agents. Choose any unmatched core agent \(u\). By the lemma, \(u\) lies in exactly one blocking pair with each of the \(r\) matched pairs, and it blocks with each of the other \(s-1\) unmatched agents. Thus
\[
|\operatorname{BP}_u(M)|=r+s-1=2k-r\ge k,
\]
proving the lower bound for all partial matchings, including the empty matching.

For the upper bound match \(\{i,i+k\}\) for \(0\le i<k\) and leave agent \(2k\) unmatched. The unmatched agent has precisely \(k\) blocking pairs by the preceding calculation. For each paired endpoint \(i\), its assigned partner is at clockwise distance \(k\), so at most \(k-1\) other agents precede the partner on its list; consequently its blocking degree is at most \(k-1\). The other endpoint \(i+k\) sees its partner at clockwise distance \(k+1\), so its blocking degree is at most \(k\). The matching therefore has maximum blocking degree exactly \(k\).

**Even order.** Consider any partial matching on the \(2k+1\) core agents plus \(d\). If \(d\) is unmatched, the odd-sized core has at least one unmatched core agent \(u\). Write \(r\) for the number of core--core pairs and \(s\ge1\) for the number of unmatched core agents, so \(2r+s=2k+1\). Agent \(u\) blocks with one endpoint from each core--core pair, each other unmatched core agent, and the unmatched \(d\); its degree is
\[
r+(s-1)+1=r+s=2k+1-r\ge k+1.
\]
If instead \(d\) is paired with some core agent \(z\), the remaining \(2k\) core agents form \(r\) core--core pairs and \(s\) unmatched agents, with \(2r+s=2k\). Since \(z\) ranks \(d\) last, it prefers every core agent to \(d\); the circular lemma implies that exactly one endpoint of each core--core pair prefers \(z\) to its partner. Each unmatched core also prefers \(z\) to remaining unmatched. Hence
\[
|\operatorname{BP}_z(M)|=r+s=2k-r\ge k.
\]
These two cases exhaust every matching and establish the even-order lower bound.

For the even-order upper bound, use the \(k\) core pairs \(\{i,i+k\}\), \(0\le i<k\), and pair the remaining core agent \(2k\) with \(d\). Each paired core endpoint has at most \(k\) agents ranked ahead of its assigned core partner, so it has at most \(k\) incident blocking pairs. Agent \(2k\) ranks precisely \(2k\) core agents ahead of \(d\), but, by the circular lemma, each of the \(k\) paired core--core edges contributes exactly one blocker with \(2k\), and there are no other unmatched core agents; thus its blocking degree is exactly \(k\). Every other core agent ranks \(d\) below its assigned partner, so \(d\) participates in no blocking pairs with those agents. This gives an upper bound of \(k\). For \(k=0\), the two agents can be matched, and the optimum is zero. Combining odd and even cases yields the formula.

For arbitrary complete-list instances, each agent has at most \(n-1\) potential blocking partners. This trivial universal upper bound, together with the exhibited \(\lfloor(n-1)/2\rfloor\) lower bound, proves worst-case \(\Theta(n)\).

**First size at which two blocking pairs are unavoidable.** The five-agent circular profile has optimum \(2\), by the odd-order formula. For all sizes at most four, an independent finite census (source `census.cpp`) exhausts each undirected symmetric-acceptability graph and every strict preference permutation of each neighborhood, and for each profile all partial matchings. It finds no profile with optimum exceeding \(1\). The census checks \(1,2,18,2634\) profiles for one through four agents respectively; its completeness follows directly from enumeration of every graph edge mask, all neighborhood permutations, and the recursion giving each partial matching exactly once. Hence five agents are the exact threshold, including incomplete lists. This finite census is not used to justify the infinite-order formula.

## Verification
The supplied `verify.py` generates these cyclic complete-list instances, independently computes blockers from strict rank comparisons, and enumerates every partial matching for \(2\le n\le10\). It reproduces optimal values \(0,1,1,2,2,3,3,4,4\), verifies the proposed upper-bound matchings, and tests the circular comparison lemma on all distinct core triples. These finite tests supplement, but do not replace, the all-order proof above.

The supplied `census.cpp` performs independent exhaustive finite checking of all symmetric-acceptability strict profiles for \(1\le n\le5\), reporting \(15{,}199{,}074\) profiles at five agents, of which \(7{,}752\) have optimum at least two. In particular, \(7{,}272\) of the eight-million-scale five-agent complete-list profiles require at least two. Its all-profiles enumeration is an exact finite proof of the smallest-size clause, subject to correct execution of the fully supplied source. Reproduction: run `python3 verify.py`; compile `census.cpp` with a C++17 compiler and run the executable. There are no external packages or private data dependencies.

## Relationship to prior work
Glitzner and Manlove (2026) introduce the same minimax per-agent blocking-pair objective in Stable Roommates with Incomplete Lists. Their Proposition 3.4 and Theorem 3.5 give an explicit logarithmic worst-case lower bound even with complete preferences, using recursive three-way preference cycles. Their Proposition 3.6 and Theorem 3.7 give a linear worst-case bound for **maximum-cardinality** almost-stable matching in an **incomplete-list bipartite** setting. Crucially, that latter result does not imply a linear bound when arbitrary partial matchings are allowed: a deficient matching may avoid the forced pairs. The present cyclic family supplies linear growth while simultaneously allowing arbitrary partial matchings and complete lists. Its exact value and five-agent threshold concern a different and stronger scope. Earlier almost-stable roommates work by Abraham, Biró, and Manlove minimizes the **total** number of blocking pairs, a different invariant.

## Limitations
The exact value \(\lfloor(n-1)/2\rfloor\) is determined for the displayed family, not proved to be the universal worst-case value at each fixed order among all preference profiles. The \(\Theta(n)\) worst-case rate uses the immediate general upper bound \(n-1\). The construction concerns unit-capacity, one-to-one, strict preferences, and the per-agent count of blocking pairs. A separate independent audit and publication-priority confirmation have not been performed. Related cyclic-preference literature might contain an implicit or equivalent bound that was not located.

## References
1. Frederik Glitzner and David Manlove, *A Minimax Perspective on Almost-Stable Matchings*, arXiv:2601.14195, v1 publicly submitted 2026-01-20; see Section 3.3, especially Proposition 3.4 and Theorems 3.5 and 3.7. https://arxiv.org/abs/2601.14195
2. Frederik Glitzner and David Manlove, *Minimax and Preferential Almost-Stable Matchings*, AAMAS 2026 proceedings, 2026-05-24 online, doi:10.65109/pcde6577. https://eprints.gla.ac.uk/375889/
3. David J. Abraham, Péter Biró, and David F. Manlove, *Almost stable matchings in the Roommates problem*, WAOA 2005 proceedings (2006), doi:10.1007/11671411_1. https://eprints.gla.ac.uk/2816/
