# Complete commuting-tuple series and universal Poisson window for Brandt inverse semigroups

## Finding

Let \(G\) be any finite group of size \(g\), and \(B_n(G)\) its Brandt inverse semigroup with zero and \(n\) index positions. The full exponential generating function for ordered pairwise-commuting tuples in \(B_n(G)\) admits the exact finite formula

\[
F_{n,G}(t)=e^t\left(C_G(t)^n+\sum_{\substack{a,b\ge1\\a+b\le n}}\binom{n}{a,b,n-a-b} E_{a,b,g}(t) C_G(t)^{n-a-b}\right),
\]

where \(C_G(t)\) counts ordered commuting tuples in \(G\), and

\[
E_{a,b,g}(t)=\sum_{i=0}^a\sum_{j=0}^b(-1)^{i+j}\binom ai\binom bj\exp\!\left(g(a-i)(b-j)t\right).
\]

This equality holds as a formal power-series identity, for every finite group, without a commutativity assumption on \(G\). The Brandt tuple-count series recovers the full local-group tuple-count series for fixed \(n\). Its large-index random law is unexpectedly universal: if \(G_n\) is any sequence of finite groups and \(k_n/\sqrt n\to\lambda\ge0\), the number of noncommuting pairs among \(k_n\) independent uniform Brandt elements converges to a Poisson law of mean \(\lambda^2\); hence the probability of complete pairwise commutativity tends to \(e^{-\lambda^2}\).

## Assumptions and scope

Fix a finite group \(G\), with identity \(1_G\) and \(|G|=g\ge1\), and an integer \(n\ge1\). The Brandt inverse semigroup is

\[
B_n(G)=\{0\}\cup\{(i,x,j):i,j\in[n],\ x\in G\},
\]

with absorbing zero and \((i,x,j)(k,y,\ell)=(i,xy,\ell)\) if \(j=k\), and zero otherwise. Two elements *commute* when their products in both orders agree. For a semigroup \(H\), \(c_r(H)\) counts **ordered** \(r\)-tuples \((h_1,\ldots,h_r)\) whose every pair commutes; repetition is allowed and \(c_0(H)=1\). Define the formal exponential series \(C_H(t)=\sum_{r\ge0} c_r(H)t^r/r!\). The multinomial coefficient is \(\binom{n}{a,b,n-a-b}=n!/[a!b!(n-a-b)!]\). The finite double sum in the finding is absent if \(n=1\).

For the limit theorem, both \(G_n\) and its cardinality may vary arbitrarily with \(n\), but each \(G_n\) is a nonempty finite group. The sample size \(k_n\) is a nonnegative integer and \(k_n/\sqrt n\to\lambda\in[0,\infty)\). Define \(X_n\) to count unordered pairs of *sample positions* that do not commute. No infinite group or growing sample outside this scaling regime is covered by the stated Poisson limit.

## Proof

**Commuting support dichotomy.** Write a nonzero Brandt element \((i,x,j)\) as *diagonal* if \(i=j\) and *off-diagonal* otherwise. Two off-diagonal elements \((i,x,j)\), \((k,y,\ell)\) commute if and only if \(j\ne k\) and \(\ell\ne i\): if exactly one equality holds, precisely one product is nonzero; if both hold, the two nonzero products lie at different diagonal indices, because \(i\ne j\). Thus if at least one off-diagonal element occurs in a commuting tuple, its collection of source indices \(U\) and target indices \(W\) are nonempty and disjoint. Conversely, all off-diagonal elements from \(U\times G\times W\) mutually commute when \(U\cap W=\varnothing\). Such an element fails to commute with every diagonal element indexed by \(U\cup W\), while each diagonal element at an index outside that union commutes with all such off-diagonal elements. At a given outside index, the chosen group labels must commute pairwise; different outside indices impose no cross-conditions.

**Enumeration.** If a commuting tuple has no off-diagonal entries, its nonzero entries at each of the \(n\) diagonal positions form an arbitrary ordered commuting tuple in \(G\), and zero entries are arbitrary. Exponential labeled-product counting gives \(e^t C_G(t)^n\). In the other case choose the *exact* nonempty source set \(U\subseteq[n]\) of size \(a\) and exact nonempty target set \(W\subseteq[n]\) of size \(b\) with \(U\cap W=\varnothing\), in \(\binom{n}{a,b,n-a-b}\) ways. All possible labeled off-diagonal elements form the \(gab\)-element alphabet \(U\times G\times W\). Require that every source position in \(U\) and every target position in \(W\) occur at least once among them. Inclusion-exclusion over omitted source rows and target columns yields their ordered-word exponential series \(E_{a,b,g}(t)\) exactly. The remaining \(n-a-b\) diagonal positions contribute \(C_G(t)^{n-a-b}\); the freely inserted zero elements contribute \(e^t\). Every tuple with off-diagonal entries is counted once, by its unique exact \((U,W)\). Summing proves the displayed identity, including \(r=0\) and \(n=1\).

**Recoverability.** The degree-one coefficient of \(F_{n,G}(t)\) is \(|B_n(G)|=1+n^2g\), hence determines \(g\) when \(n\) is known. Define \(D_{n,G}(t)=e^{-t}F_{n,G}(t)\). Each \(E_{a,b,g}(t)\) with \(a,b\ge1\) has zero constant term (in fact starts at degree at least \(\max(a,b)\)). At degree \(r\ge1\), the coefficient in the exponential basis of \(C_G(t)^n\) is \(n c_r(G)\) plus a function of \(c_0(G),\ldots,c_{r-1}(G)\). Every term involving \(E_{a,b,g}(t)\) depends only on \(c_j(G)\) with \(j<r\). Thus the coefficient of \(t^r/r!\) in \(D_{n,G}\) uniquely determines \(c_r(G)\) recursively after previous coefficients are known.

**Poisson window.** Draw \(k_n\) independent uniform elements from \(B_n(G_n)\). Since \(|B_n(G_n)|=1+n^2|G_n|\), the probability any sampled element is zero is at most \(k_n/(1+n^2|G_n|)\); the probability of any diagonal nonzero sample is at most \(k_n n|G_n|/(1+n^2|G_n|)\). Both tend to zero for \(k_n=O(\sqrt n)\). Conditional on the absence of zeros, the source and target indices \((I_a,J_a)\), across sample positions \(a\), are independent uniform ordered pairs of indices in \([n]^2\). Their labels in \(G_n\) do not affect whether a pair of *off-diagonal* elements commutes.

Define \(Y_n=\sum_{a\ne b}\mathbf1_{\{J_a=I_b\}}\), with the sum over ordered distinct sample positions. The event of a diagonal sample or zero sample has probability \(o(1)\). Moreover, for each unordered pair \(\{a,b\}\), simultaneous equalities \(J_a=I_b\) and \(J_b=I_a\) have probability \(n^{-2}\); by the union bound, the probability of any such double equality is at most \(\binom{k_n}{2}n^{-2}=o(1)\). Hence \(X_n=Y_n\) outside an event whose probability tends to zero.

For fixed \(r\ge1\), compute the factorial moment \(\mathbb E (Y_n)_r\). An ordered selection of \(r\) *distinct* constraints \(J_a=I_b\) corresponds to a bipartite graph with independent index variables \(J_a\) on its left and \(I_b\) on its right, and \(r\) distinct edges, with \(a\ne b\). If the graph has \(v\) vertices and \(c\) connected components, its simultaneous-equality probability is exactly \(n^{-(v-c)}\). Disjoint-edge configurations account for \((k_n)_{2r}(1+o(1))\) ordered selections, each of probability \(n^{-r}\), and their total tends to \(\lambda^{2r}\). All configurations with an edge-sharing connected component have some component of at least three vertices; such a component has \(O(k_n^v)\) choices and equality probability at most \(n^{-(v-1)}\), yielding \(O(n^{1-v/2})=o(1)\) for \(v\ge3\). For fixed \(r\) there are finitely many graph patterns, and components of size two contribute only bounded factors because \(k_n=O(\sqrt n)\). Thus \(\mathbb E(Y_n)_r\to\lambda^{2r}\) for each fixed \(r\). These are the factorial moments of \(\operatorname{Poisson}(\lambda^2)\), which determine that distribution. The same conclusion for \(\lambda=0\) follows directly from \(\mathbb EY_n=k_n(k_n-1)/n\to0\). The \(o(1)\) comparison between \(X_n\) and \(Y_n\) proves the claimed distributional convergence, and taking the probability of zero noncommuting pairs yields \(e^{-\lambda^2}\).

## Verification

The accompanying pure-Python script `brandt_commuting_checker.py` constructs Brandt multiplication directly, enumerates all ordered commuting tuples of feasible lengths, and independently evaluates the inclusion-exclusion generating function. It checks twelve configurations spanning the trivial group, \(C_2\), and the nonabelian \(S_3\) for index sizes \(n=1,2,3,4\), with maximum tuple lengths adjusted to feasible exhaustive enumeration. It reports `ALL_BRANDT_COMMUTING_COUNTS_PASSED 12` when successful. The asymptotic theorem is established by the preceding factorial-moment argument, not by finite simulation.

## Relationship to prior work

The 2017 Brandt-subsemigroup-complex paper of Margolis, Rhodes and Silva [1] studies chains in subsemigroup lattices and the resulting simplicial complex; its verified primary classification is 20M18. Kumar, Dalal and Pandey [2] study commuting graphs of Brandt semigroups, including the source/target bipartition underlying the present decomposition. Paulista [3] studies commuting graphs of completely simple Rees semigroups, not the complete ordered-tuple series. These established structural ingredients are not claimed as new. A previous finite-Brandt classification of **inclusion-maximal commutative subsemigroups and their size polynomial** also supplies the source-target dichotomy. Its size polynomial counts maximal containers rather than all ordered commuting tuples, with unavoidable overlaps among group-abelian fibers; it therefore does not imply the present exact series simply by substituting its coefficients. The new mathematical statements assessed here are the all-length EGF including nonabelian local-group data, its recursive reconstruction property, and the sharp group-independent Poisson scaling limit. The derivation uses known commuting-support structure and elementary inclusion-exclusion and rare-event methods.

## Limitations

The counting identity concerns pairwise commutation, not arbitrary word equations. For nonabelian groups the answer is expressed in terms of their complete commuting-tuple series; a numerical evaluation still requires computing those group counts. The Poisson conclusion assumes \(k_n/\sqrt n\) has a finite limit and does not claim a limit at larger scales or for biased sampling. Finite enumerations cannot certify the infinite theorem, and the novelty comparison cannot exclude an older equivalent EGF or probabilistic formulation indexed under other terminology. In particular the source/target classification and ordinary Poisson factorial-moment method are prior mathematical tools, not claimed innovations. Independent review of historical priority is not asserted.

## References

[1] S. Margolis, J. Rhodes and P. V. Silva, *On the subsemigroup complex of an aperiodic Brandt semigroup*, arXiv:1705.04956v1 (first publicly posted 2017-05-14), especially the Brandt-semigroup sections. https://arxiv.org/abs/1705.04956

[2] J. Kumar, S. Dalal and P. Pandey, *On the Commuting graphs of Brandt Semigroups*, arXiv:2010.05000v1 (2020), especially Sections 2--3. https://arxiv.org/abs/2010.05000

[3] T. Paulista, *Commuting graphs of completely simple semigroups*, arXiv:2412.06560v1 (2024), especially Sections 2--4. https://arxiv.org/abs/2412.06560
