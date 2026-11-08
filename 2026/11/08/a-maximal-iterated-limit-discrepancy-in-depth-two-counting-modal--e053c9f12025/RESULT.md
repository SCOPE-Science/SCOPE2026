# A maximal iterated-limit discrepancy in depth-two counting modal logic

## Finding

Let \(K^{\#}\) be the propositional counting modal language with integral linear comparisons of successor counts. On uniformly independently labelled full \(n\)-ary rooted trees, define
\[
B := (2\#p=\#\top)\lor(2\#p=\#\top+1),
\qquad
\Psi := (\#B=0).
\]
An equality of count expressions abbreviates the conjunction of its two opposite weak inequalities. The formula \(\Psi\) has modal depth two and uses exactly one propositional letter. For every integer \(n\ge1\), its ordinary probability is
\[
\mu_n^{\mathcal T}(\Psi)=\left(1-\frac{\binom n{\lceil n/2\rceil}}{2^n}\right)^n.
\]
Consequently,
\[
\lim_{n\to\infty}\mu_n^{\mathcal T}(\Psi)=0,
\qquad
\mu'_{\infty}(\Psi)=1,
\]
where \(\mu'_{\infty}\) is the iterated-limit quantity of Ghosh--Schwarzentruber [1, Definition 26]. Thus its Conjecture 38, which predicts that the iterated limit is an adherence point of the ordinary sequence, fails even for an ordinarily convergent sequence. The discrepancy of one is the largest possible between two probabilities. No formula of modal depth at most one, or with zero propositional letters at any finite depth, can witness such a discrepancy in the same model family.

More quantitatively, with \(c=\sqrt{2/\pi}\),
\[
\log\mu_n^{\mathcal T}(\Psi)=-c\sqrt n-\frac1\pi+O(n^{-1/2}).
\]

## Assumptions and scope

A model is a full rooted \(n\)-ary tree of height two. Every vertex independently receives a fair Boolean value of the single letter \(p\). The satisfaction probability \(\mu_n^{\mathcal T}\) is computed under this product valuation measure. The counting term \(\#\theta\) at a vertex counts its immediate successors satisfying \(\theta\); \(\#\top=n\) at each internal vertex. The probability depends only on valuations at the leaves, even though values are independently assigned at all vertices. Count expressions use only addition, integer multiplication, constants, and indicators and successor counts, exactly as in [1, Definition 3]. The resulting formula is therefore legal \(K^{\#}\) syntax. The surrogate \(\mu'_n\) follows [1, Definition 26]: limiting probabilities of direct subformulas are substituted before the root branching factor is taken to infinity. All limits are over positive integers \(n\to\infty\).

## Proof

For any one child of the root, let \(X\) denote the number of its \(n\) children satisfying \(p\). Then \(X\sim\operatorname{Bin}(n,1/2)\), and \(B\) holds precisely when \(2X=n\) or \(2X=n+1\). Exactly one of these is possible for each parity of \(n\). Hence
\[
q_n:=\Pr(B)=\binom n{\lceil n/2\rceil}2^{-n}.
\]
The \(n\) child subtrees of the root use disjoint sets of leaf valuations, so their \(B\)-events are independent. The event \(\Psi\) says none is successful. This proves the exact expression \(\mu_n^{\mathcal T}(\Psi)=(1-q_n)^n\).

The classical central-binomial estimate, equally valid along even and odd \(n\), gives
\[
q_n=\sqrt{\frac{2}{\pi n}}\bigl(1+O(n^{-1})\bigr).
\]
In particular \(q_n\to0\) but \(nq_n\to\infty\). Therefore \(0\le(1-q_n)^n\le e^{-nq_n}\to0\). Expanding the logarithm yields
\[
n\log(1-q_n)=-nq_n-\tfrac12nq_n^2+O(nq_n^3)
=-\sqrt{\frac{2n}{\pi}}-\frac1\pi+O(n^{-1/2}),
\]
proving the refined asymptotic.

Since \(B\) has depth one, its iterated-limit probability equals its ordinary limit, namely \(\mu'_\infty(B)=\lim_nq_n=0\). In the iterated-limit construction for \(\Psi\), each direct child satisfies \(B\) with probability zero, independently of the chosen root branching factor. Thus \(\mu'_n(\Psi)=1\) at every root branching factor, and \(\mu'_\infty(\Psi)=1\). The ordinary sequence converges to zero, so its sole adherence point is zero, contradicting [1, Conjecture 38]. A gap of one is maximal because both terms belong to \([0,1]\).

For sharp depth, [1, Definition 26] agrees with ordinary tree probabilities for every formula of depth at most one, so no depth-one formula whose ordinary limit exists can yield a different value. For the zero-letter statement, fix any finite-depth \(K^{\#}\)-formula without propositional variables. The unique valuation-free full \(n\)-ary tree has identical truth values at all vertices of a given remaining depth. By induction on modal depth, each subformula's truth value at an appropriate internal vertex is eventually constant as \(n\to\infty\): if its direct subformulas are eventually constant, every successor-count term is eventually either \(0\) or \(n\), and every numerical comparison is eventually the sign of an integral affine function of \(n\). Boolean connectives preserve eventual constancy. The iterated-limit semantics substitutes those same eventual truth values and therefore agrees with the ordinary eventual truth of the formula. Thus at least one letter and depth two are necessary.

The amplification mechanism is general: replacing an event with probability \(q_n\to0\) by the limiting zero event need not preserve its *absence* among \(n\) independent opportunities when \(nq_n\to\infty\). Here the central-binomial window realizes precisely that regime.

## Verification

The included standalone `checker.py` can be run with `python checker.py` using only the Python standard library. It independently enumerates every atomic valuation of the full regular height-two trees with branching \(n=1,2,3\), evaluates the two count equalities on every child, and compares root satisfaction with the closed formula. A separate child-block polynomial count agrees through \(n=12\). Exact values include \(1/2,1/4,125/512,625/4096\) for \(n=1,2,3,4\). The checker tests the surrogate value using the stated iterated-limit substitution. No finite experiment substitutes for the all-\(n\) proof above.

## Relationship to prior work

Ghosh and Schwarzentruber [1] introduce the counting-model setup, the iterated-limit construction in Definition 26, and Conjecture 38. Their Proposition 25 uses separate parity-sensitive balanced events to produce an *oscillating* ordinary probability; in that example the surrogate value one remains an actual subsequential limit. The present formula instead merges the two parity cases into a single depth-one rare event and asks whether it occurs among the root's children. The ordinary probability now converges to zero, while the iterated limit remains one, so their example does not imply the present counterexample merely by restating its conclusion. The central-binomial asymptotic used here is classical. Earlier asymptotic GNN work [2] concerns different aggregation assumptions and does not state this comparison of the two limits.

## Limitations

The statement concerns uniformly independent fair valuations on **full** regular rooted trees, not arbitrary random graphs, biased valuations, or tree families with random degrees. It refutes the general adherence conjecture but supplies no complete characterization of formulas for which iterated-limit substitution is sound. Historical priority has been checked against the motivating paper, targeted public searches, and accessible research records, but an equivalent unindexed counterexample remains possible. Independent mathematical verification and independent historical-priority audit have not been performed.

## References

[1] A. Ghosh and F. Schwarzentruber, *On Counting Graphs for Modal Logic with Counting*, arXiv:2610.26187v1, first posted 2026-10-19. https://arxiv.org/html/2610.26187v1 (especially Definitions 3 and 26, Proposition 25, Example 27, Conjecture 38, and Appendix proof of Theorem 39).

[2] S. Adam-Day, M. Benedikt, İ. İ. Ceylan and B. Finkelshtein, *Almost Surely Asymptotically Constant Graph Neural Networks*, arXiv:2403.03880, first posted 2024-03-06. https://arxiv.org/abs/2403.03880.
