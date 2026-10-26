# The critical majority-ratio phase diagram on random regular trees

## Finding
For a fixed ratio threshold \(r\in[0,1]\) and a fixed positive modal depth \(d\), the probability that an independently fair-labelled complete \(n\)-ary tree satisfies the depth-\(d\) iterated ratio-majority formula at its root has a complete sharp phase diagram. All noncentral thresholds have deterministic limits. At the unique critical threshold \(r=1/2\), parity of \(n\) prevents convergence starting at depth two, with an explicit Gaussian constant at depth two and saturated but different even/odd limits thereafter.

Set \(\rho=\Phi(\sqrt{2/\pi})=0.787531258158319\ldots\). For the weak ratio modality \(M_{\ge r}\) the limits are
\[
\begin{array}{c|c|c|c}
 & 0\le r<1/2 & r=1/2 & 1/2<r\le1\\
\hline
\text{all }d\ge1,\text{ all }n\to\infty &1 & \text{parity-dependent as below}&0\\
\end{array}
\]
At \(r=1/2\), for each fixed depth \(d\ge1\),
\[
\lim_{\substack{n\to\infty\\ n\ \mathrm{odd}}}\Pr(T_{n,d}\models M_{\ge1/2}^{d}p)=\frac12,
\qquad
\lim_{\substack{n\to\infty\\ n\ \mathrm{even}}}\Pr(T_{n,d}\models M_{\ge1/2}^{d}p)=
\begin{cases}\frac12,&d=1,\\\rho,&d=2,\\1,&d\ge3.\end{cases}
\]
The strict threshold \(M_{>r}\) has the same limiting values away from \(1/2\); at \(1/2\) its probability is exactly the complement of the weak threshold probability for every finite \(n,d\). Thus the strict even-subsequence limits are \(1/2\), \(1-\rho\), and \(0\) for depths 1, 2, and at least 3, respectively. The least depth with nonconvergence is exactly 2.

## Assumptions and scope
The directed tree \(T_{n,d}\) has one root, every nonleaf has precisely \(n\) distinct children, and the leaves are exactly distance \(d\) from the root. The only randomized information is the leaf interpretation of the propositional letter \(p\): all \(n^d\) truth bits are mutually independent with Bernoulli parameter \(1/2\). No restrictions are needed on the label of internal nodes, as the displayed formulas do not inspect it. There are no duplicate successors and no zero-successor modal evaluations before the leaves. All limits fix \(d\) and \(r\) before \(n\to\infty\).

For every internal node with \(n\) successors, \(M_{\ge r}\varphi\) means the fraction of successors satisfying \(\varphi\) is at least \(r\); \(M_{>r}\varphi\) uses strict inequality. The modality \(M_{\bowtie r}^{d}\) means \(d\) syntactic nestings of the same operator, not an update of the underlying relation. The CDF \(\Phi(t)=(2\pi)^{-1/2}\int_{-\infty}^{t}e^{-u^2/2}\,du\) is standard normal.

## Proof
**Exact recursion.** Set \(b_0=1/2\). Conditional on the independent disjoint leaf subtrees, each child at the next layer satisfies the appropriate depth formula independently with common probability \(b_j\). Thus the weak and strict probabilities are given by \(b_d\), where respectively
\[
F_{n,r}(x)=\sum_{k=\lceil nr\rceil}^{n}\binom nk x^k(1-x)^{n-k},
\qquad
G_{n,r}(x)=\sum_{k=\lfloor nr\rfloor+1}^{n}\binom nk x^k(1-x)^{n-k},
\]
with the standard interpretation of a zero or empty sum, and \(b_{j+1}=F_{n,r}(b_j)\) or \(b_{j+1}=G_{n,r}(b_j)\). In particular, this is a recursion for *independent child subtrees*, not an unjustified independence assertion about shared graph neighborhoods.

**Noncritical ratios.** For fixed \(r<1/2\), Hoeffding's inequality yields \(F_{n,r}(1/2)\to1\) and \(G_{n,r}(1/2)\to1\); for fixed \(r>1/2\), both tend to \(0\). The same inequality and induction propagate either limit through every fixed number of layers: when the input probability is bounded above the threshold by a positive gap the output tends to 1, and when it is bounded below by such a gap the output tends to 0. This includes \(r=0\) and \(r=1\), for which the boundary sums give the same conclusions.

**Odd branching at the critical ratio.** For odd \(n\), a fair binomial count has no ties, so \(F_{n,1/2}(1/2)=G_{n,1/2}(1/2)=1/2\). Iteration gives exactly \(1/2\) at every depth, not merely asymptotically.

**Even branching at the critical ratio.** For even \(n\), symmetry of the fair binomial gives
\[
F_{n,1/2}(1/2)=\frac12+\frac12\binom{n}{n/2}2^{-n}
=\frac12+\frac{1+o(1)}{\sqrt{2\pi n}}.
\]
Writing \(u_n=F_{n,1/2}(1/2)\), Stirling's estimate yields \(\sqrt n(u_n-1/2)\to1/\sqrt{2\pi}\). The triangular-array binomial central limit theorem, applied to \(X_n\sim\operatorname{Bin}(n,u_n)\), gives
\[
F_{n,1/2}(u_n)=\Pr(X_n\ge n/2)
\longrightarrow\Phi\left(\sqrt{2/\pi}\right)=\rho>\frac12.
\]
The weak depth-three probability therefore tends to 1 by Hoeffding's inequality, since for some fixed \(\eta>0\) its input lies above \(1/2+\eta\) for all sufficiently large even \(n\). Induction maintains the limit 1 at each further *fixed* depth.

**Strict modality by complementation.** For every \(n\) and every \(x\in[0,1]\), binomial symmetry gives \(G_{n,1/2}(x)=1-F_{n,1/2}(1-x)\). Starting both recursions at \(1/2\), induction proves \(G_{n,1/2}^{\circ d}(1/2)=1-F_{n,1/2}^{\circ d}(1/2)\). Thus all claimed strict limits follow without a separate approximation. Finally, at depth one both even and odd probabilities approach \(1/2\), while at depth two they have different even and odd limits, proving minimal depth exactly two.

## Verification
The accompanying standard-library-only `checker.py` enumerates all Boolean leaf valuations on seven small tree shapes (\(n=2\), depths 1, 2, 3; \(n=3\), depths 1, 2; \(n=4\), depths 1, 2) with both weak and strict modalities, and compares empirical exact fractions against the binomial recurrence. It exhaustively considers 132,696 formula--valuation evaluations (including both modalities). It separately checks rational complement identities for all \(1\le n\le20\) and depths 1 through 3, and checks the numerical approach of even-depth-two probabilities to the asserted Gaussian limit along six increasing even branching factors. Its output terminates in `ALL_CHECKS_OK`. These finite checks corroborate the exact recursion only; the infinite limits are proved analytically by Stirling, the binomial central limit theorem and concentration bounds.

Reproduce with `python3 checker.py` in a directory containing only the embedded checker file; no network or third-party dependencies are needed.

## Relationship to prior work
Schönherr and Lutz (arXiv:2507.18145v1, publicly submitted 24 July 2025) define ratio modal logic and relate it to the expressive power of mean-aggregating graph neural networks. Their nested strict-majority example is used to separate expressive classes of networks; their paper does not establish the random-tree parity phase diagram, the Gaussian even-depth-two value or the least depth of nonconvergence. The present statement concerns satisfaction probabilities under an explicitly specified random leaf valuation. It does **not** infer uniform realizability by a single continuous mean-GNN.

Pacuit and Salame's *Majority Logic* provides the earlier weak-majority modal operator and its axiomatic semantics. It does not assert this probabilistic asymptotic classification. The paper *Tradeoffs in Hierarchical Voting Systems* establishes the recursive binomial model for hierarchical voting, explicitly assuming an odd number of children so that ties cannot occur; the recurrence itself is not new here. Engels, Garg, Makino and Rao investigate Boolean circuits composing majority gates to compute the majority of all their input bits, rather than the distribution of nested formulas with a growing **even** branching factor and fair inputs. The novel claim is the combined sharp logical threshold/depth/parity limiting classification, not the classical binomial identity, normal approximation or concentration inequality separately.

## Limitations
Only complete disjoint-subtree frames, mutually independent fair leaf bits, one predicate and a fixed modal depth are covered. Growing modal depth, correlated leaf bits, variable branching profiles, and general random graphs may yield different asymptotics. The normal-limit constant is a consequence of classical probability estimates, not a new probability limit theorem on its own. An older equivalent result in recursive voting or threshold-circuit literature under different terminology remains a priority risk. No independent external audit has been performed.

## References
1. M. Schönherr and C. Lutz, *Logical Characterizations of GNNs with Mean Aggregation*, arXiv:2507.18145v1 (24 July 2025), https://arxiv.org/html/2507.18145v1.
2. E. Pacuit and S. Salame, *Majority Logic: Axiomatization and Completeness*, *Studia Logica* (2006), preprint https://pacuit.org/api/files/pubs/proceedings/majlog_sl_final.pdf.
3. *Tradeoffs in Hierarchical Voting Systems*, arXiv:2110.02298v1 (5 October 2021), https://arxiv.org/html/2110.02298v1.
4. C. Engels, M. Garg, K. Makino and A. Rao, *On Expressing Majority as a Majority of Majorities* (2017), https://homes.cs.washington.edu/~anuprao/pubs/majmaj.pdf.
