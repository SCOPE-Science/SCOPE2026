# Poisson orientation profiles at the growing-successor collision threshold

## Finding

Fix an integer \(j\geq3\). The asymptotic law of all \(j\)-relation adjacency overlaps among a growing collection of independently uniform successor relations has a sharp orientation-resolved Poisson transition at \(k\asymp n^{1-2/j}\). Specifically, at \(k/n^{1-2/j}\to c\in(0,\infty)\), the counts in every minority-orientation class converge jointly in total variation to independent Poisson variables with explicit parameters; below the threshold they vanish, and above it the associated existential properties hold with high probability.

## Assumptions and scope

Choose \(j\geq3\) once and hold it fixed as \(n\to\infty\). Let \(V_n=\{1,\ldots,n\}\), with \(n\geq2\). Independently sample \(k_n\) uniformly random permutations of \(V_n\), each interpreted as a directed Hamiltonian path successor relation \(S_i\). There are no extra predicates and no restrictions relating the orders. The number \(k_n\), unlike \(j\), may depend on \(n\).

An unordered edge \(e=\{u,v\}\), with \(u<v\), carries a positive direction in \(S_i\) if \(S_i(u,v)\) holds, a negative direction if \(S_i(v,u)\) holds, and no direction otherwise. For each index set \(I\subseteq\{1,\ldots,k_n\}\) of size \(j\), call \((e,I)\) a witness if all \(j\) indices provide a direction. Define its minority class \(h=\min(\#\text{positive},\#\text{negative})\). Write \(W_{j,h}\) for the count over all distinct pairs \((e,I)\), where \(0\leq h\leq\lfloor j/2\rfloor\).

Define
\[
w_{j,h}=\begin{cases}2\binom{j}{h},&2h<j,\\\binom{j}{h},&2h=j.\end{cases}
\]
For all \(n\ge2\), with the convention \(\binom{k_n}{j}=0\) for \(k_n<j\), the exact means are
\[
\mathbb E W_{j,h}=\binom{n}{2}\binom{k_n}{j}\frac{w_{j,h}}{n^j}.
\]
If \(k_n/n^{1-2/j}\to c\in(0,\infty)\), then
\[
(W_{j,h})_{h=0}^{\lfloor j/2\rfloor}\xrightarrow{\mathrm{TV}}\bigotimes_{h=0}^{\lfloor j/2\rfloor}\mathrm{Poisson}\!\left(\lambda_{j,h}\right),\qquad
\lambda_{j,h}=\frac{w_{j,h}c^j}{2j!}.
\]
In particular, for \(j=3\), the all-aligned count has mean \(c^3/6\), and the count with a reversed direction has mean \(c^3/2\), independently. The sum of the limiting Poisson means is \(2^{j-1}c^j/j!\).

Each event \(\{W_{j,h}>0\}\) is definable by a sentence using only the variables \(x,y\): existentially select two distinct elements, disjoin over \(j\)-subsets of the designated successor symbols and over the permitted oriented diagrams. The relevant quantifier-free disjunct tests \(S_i(x,y)\) or \(S_i(y,x)\) for each selected index. As the vocabulary grows, the sentence family grows accordingly; **this is not a claim about a single fixed sentence in a fixed vocabulary**.

## Proof

**One-order block formula.** A specified oriented adjacency \(u\to v\) occurs in exactly \((n-1)!\) of the \(n!\) linear orders, hence with probability \(1/n\). More generally, if \(s\) distinct directed adjacencies in one order form disjoint directed paths, contracting those paths gives exactly \((n-s)!\) orders, so their probability is \((n-s)!/n!=1/(n)_s\); inconsistent constraints have probability zero. Thus for each fixed \(s\), the probability of any \(s\) specified undirected adjacency requirements, whatever compatible orientations are allowed, is at most \(2^s/(n)_s=O_s(n^{-s})\). Requirements across distinct orders are independent.

**Exact means.** There are \(\binom n2\binom{k_n}j\) pairs \((e,I)\). Every designated successor index independently realizes one of the two orientations of \(e\) with probability \(1/n\) each. Exactly \(w_{j,h}\) of the \(2^j\) sign patterns have minority class \(h\). This proves the displayed expectation formula.

**Joint mixed factorial moments.** Fix nonnegative integers \(a_h\), put \(m=\sum_h a_h\), and expand \(\mathbb E\prod_h(W_{j,h})_{a_h}\) as a sum over \(m\) distinct witnesses of prescribed classes. The implied constants below may depend on fixed \(m,j\), but not on \(n,k_n\). Group witnesses having the same unordered vertex pair \(e\). For a group using \(t\) distinct relation indices, one witness requires \(t=j\); two or more *distinct* witnesses on the same edge require \(t\ge j+1\). For \(r\) different underlying edges with group index-union sizes \(t_1,\ldots,t_r\), the choices of edges and relation indices number at most \(O_{j,m}(n^{2r}k_n^{\sum t_g})\). The block formula applied separately to each relation index bounds the probability of realizing those requirements by \(O_{j,m}(n^{-\sum t_g})\), including edges sharing endpoints and conflicting requests (which have zero probability). At \(k_n=\Theta(n^{1-2/j})\), every singleton-edge group has total factor \(O(1)\), whereas any group with repeated underlying edge contributes an additional factor at most \(k_n/n=O(n^{-2/j})\). As \(m\) is fixed, the sum of all repeated-edge terms is \(o(1)\).

We may therefore assume all \(m\) witnesses use distinct edges. Terms for which two of their index subsets intersect contribute \(o(1)\), since there are \(O_{j,m}(k_n^{jm-1})\) assignments of relation indices versus \(\Theta(k_n^{jm})\) for disjoint subsets, while the probability for \(jm\) distinct edge-by-relation adjacency requests is \(O_{j,m}(n^{-jm})\). For the remaining terms the index subsets are disjoint; the witness events are independent across the underlying random orders, even if their vertex pairs intersect, and each has exact probability \(w_{j,h}n^{-j}\). Counting edge choices and disjoint index subsets gives
\[
\mathbb E\prod_h(W_{j,h})_{a_h}
=\prod_h\left(\frac{w_{j,h}c^j}{2j!}\right)^{a_h}+o(1).
\]
The right side is the joint factorial moment of independent Poisson variables. The multivariate factorial-moment criterion gives weak convergence. Since all variables are integer-valued and the limit is a probability mass function on a countable discrete space, pointwise convergence of masses and truncation of the limiting tails give convergence in total variation.

**Thresholds and distinct-edge interpretation.** For \(k_n=o(n^{1-2/j})\), the exact expectations tend to zero, and Markov's inequality gives absence of all such witnesses. For \(k_n/n^{1-2/j}\to\infty\), fix \(C>0\), retain only the first \(\lfloor Cn^{1-2/j}\rfloor\) orders, and use monotonicity of \(W_{j,h}>0\) as more orders are added. Its lower limiting probability is at least \(1-\exp[-w_{j,h}C^j/(2j!)]\); let \(C\to\infty\). At critical scaling, let \(M_e\) be the number of successor relations joining the unordered pair \(e\), irrespective of orientation. Then
\[
\mathbb E\sum_e\binom{M_e}{j+1}
=\binom n2\binom{k_n}{j+1}(2/n)^{j+1}
=O(n^{-2/j})\to0.
\]
Thus with probability \(1-o(1)\), no pair participates in more than \(j\) successors; on this event each witness is a different vertex pair. Finally, \(\Pr(W_{j,h}>0)\to1-e^{-\lambda_{j,h}}\), with asymptotic independence of the different class-existence events.

## Verification

The standalone `checker.py` uses only Python standard-library modules. Run `python3 checker.py`. For every tuple of \(n!\) possible orders in the tested cases, one implementation directly enumerates witness triples \((e,I,h)\) and a separate implementation counts them from edge-orientation frequencies; exact rational averages are compared with the formula. The tested cases are \((n,k,j)=(2,3,3),(3,3,3),(4,3,3),(3,4,4),(4,4,4)\), including \(331776\) ordered samples in the last case. It also checks exact one- and two-edge adjacency probabilities for all \(2\leq n\leq7\) and checks the orientation weights for \(3\leq j\leq11\). Execution gives `ALL_CHECKS_OK`. These finite checks do not certify the asymptotic conclusion; that requires the factorial-moment proof above.

## Relationship to prior work

Jeż, Michaliszyn and Witkowski study finite satisfiability in two-variable logic with an arbitrary finite number of linear-order successor relations (arXiv:2610.19943v1, first public October 14, 2026); their work motivates the question of how multi-relation overlap constraints behave but addresses satisfiability and complexity, **not** probabilities under independently random orders. Bender and Canfield (1999) prove Poisson laws for edges in the intersection of a **fixed** collection of randomly embedded graphs. Their theorem is substantial prior coverage of the fixed-index-set Poisson mechanism, but its fixed collection does not itself establish simultaneous counts over the \(\binom{k_n}j\) index subsets when \(k_n\) grows, the orientation-stratified independence, or the sharp scaling \(n^{1-2/j}\). Diaconis, Evans and Graham (2013) study adjacency pairs in random permutations. Bóna, Burghart and Wagner (2025) study the intersection of pairs of random trees, a different fixed-number model. The collision theorem here uses classical permutation-block enumeration and a Poisson factorial-moment argument; neither ingredient is claimed to be a new general method.

## Limitations

The number \(j\) of coincident successor relations is **fixed**; no conclusion is asserted when \(j=j_n\) grows. The orders are **independent and uniformly random**. The theorem concerns a growing vocabulary and a family of two-variable sentences, not a single fixed finite-vocabulary sentence. Total-variation convergence is qualitative; no uniform rate in \(j\) or \(c\) is proved. The proof does not address correlated orders, nonuniform orders or common intersections of arbitrary graphs. Older sparse-random-graph Poisson approximation or occupancy results might imply related special cases, and a comprehensive historical priority assessment remains open.

## References

1. A. Jeż, J. Michaliszyn, P. Witkowski, *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, arXiv:2610.19943v1 (2026), https://arxiv.org/abs/2610.19943.
2. E. A. Bender and E. R. Canfield, *Intersections of Randomly Embedded Sparse Graphs are Poisson*, Electronic Journal of Combinatorics 6 (1999), R36, https://doi.org/10.37236/1468.
3. P. Diaconis, S. N. Evans, R. L. Graham, *Unseparated Pairs and Fixed Points in Random Permutations*, 2013 preprint, https://statistics.berkeley.edu/sites/default/files/tech-reports/unseparated_pairs.pdf.
4. M. Bóna, F. Burghart, S. Wagner, *On the intersection of pairs of trees*, arXiv:2501.18570v4 (2025), https://arxiv.org/abs/2501.18570.
