# Record-forcing coupling and exact rank-disarray covariance in uniform permutations

## Finding

Let \(\pi\) be uniform on the permutations of \([n]=\{1,\ldots,n\}\), with \(n\ge2\). Let \(R_i=\mathbf1\{\pi(i)=\max_{j\le i}\pi(j)\}\) for \(2\le i\le n\). For every nondecreasing convex function \(\phi:[0,\infty)\to\mathbb R\), put
\[
D_\phi(\pi)=\sum_{j=1}^{n}\phi(|\pi(j)-j|).
\]
There is a **single deterministic coupling**, independent of \(\phi\), between a uniform \(\pi\) and a permutation \(\pi^{(i)}\) whose law is uniform conditional on \(R_i=1\), such that, simultaneously for all these \(\phi\),
\[
D_\phi(\pi^{(i)})\le D_\phi(\pi)\quad\text{almost surely}.
\]
In particular, \(D_\phi\mid(R_i=1)\le_{\mathrm{st}}D_\phi\). For Spearman's footrule \(F=D_\phi\) with \(\phi(t)=t\), the order is strict, and its exact positionwise conditional mean and covariance are
\[
\mathbb E[F\mid R_i=1]=\frac{n^2-1}{3}-\frac{i(2i-1)}{3n},\qquad
\operatorname{Cov}(F,R_i)=-\frac{2i-1}{3n}.
\]
Consequently, if \(R=\sum_{i=1}^n R_i\) counts all upper records (with \(R_1\equiv1\)), then
\[
\operatorname{Cov}(F,R)=-\frac{n^2-1}{3n}.
\]
The same coupling includes squared-rank displacement \(Q=\sum_j(\pi(j)-j)^2\), for which
\[
\mathbb E[Q\mid R_i=1]-\mathbb E[Q]=-
\frac{i(i-1)(n+1)}{2(i+1)},\qquad
\operatorname{Cov}(Q,R_i)=-\frac{(i-1)(n+1)}{2(i+1)}.
\]

## Assumptions and scope

All permutations are uniform and are represented in one-line notation. Positions and values are indexed from \(1\). The record event refers to a *single prescribed upper-record position*, not to the entire record set, a prescribed number of records, or a nonuniform permutation law. Convexity and monotonicity are properties of \(\phi\) on the nonnegative real line. Stochastic ordering here means ordering of all upper-tail probabilities, not likelihood-ratio ordering.

## Proof

**A uniform record-forcing map.** Given a permutation \(p\), locate its largest entry among the first \(i\) positions, say \(a=p(r)\) at position \(r\le i\). Define \(T_i(p)\) by deleting that entry and inserting it at position \(i\), shifting \(p(r+1),\ldots,p(i)\) one position left; leave the suffix unchanged. The output has an upper record at \(i\). Conversely, every permutation \(q\) with an upper record at \(i\) has exactly \(i\) preimages: insert \(q(i)\) into any one of positions \(1,\ldots,i\), shifting the affected entries to the right. All such preimages are distinct and reproduce \(q\) under \(T_i\). Hence \(T_i(\pi)\) is uniform among permutations with \(R_i=1\), because the map has constant fibre size \(i\). In particular \(\Pr(R_i=1)=1/i\).

**Simultaneous convex-cost monotonicity.** The map \(T_i\) is a string of adjacent swaps, each exchanging a larger entry \(a\) in position \(k\) with a smaller entry \(b\) in position \(k+1\), with \(a>b\). Set \(\psi(x)=\phi(|x|)\). Since \(\phi\) is nondecreasing and convex, \(\psi\) is convex on \(\mathbb R\). For every \(a>b\), the increment \(x\mapsto\psi(x-b)-\psi(x-a)\) is nondecreasing. Therefore
\[
\psi(k-b)+\psi(k+1-a)\le\psi(k-a)+\psi(k+1-b).
\]
The left side is the displacement cost after the swap and the right side is the cost before it. Other positions are unchanged. Iterate over the swaps. The same \(T_i\) works simultaneously for every permitted \(\phi\), proving the coupling and the first-order stochastic ordering.

**Exact footrule regression.** The unordered set of the first \(i\) values is uniformly distributed among \(i\)-subsets of \([n]\), both unconditionally and conditional on \(R_i=1\): given that set, the location of its maximum is uniform over the \(i\) prefix positions. Write \(M\) for its maximum and \(U\) for a uniform value in \([n]\). Then \(\mathbb E M=i(n+1)/(i+1)\). Conditional on the record event, the entry at position \(i\) is \(M\); each earlier prefix position receives the remaining \(i-1\) sample values symmetrically, and each suffix position retains its unconditional distribution. For any position \(j\le i\), define \(h(j)=\mathbb E|M-j|-\mathbb E|U-j|\). The preceding symmetry implies that the change in expected footrule is
\[
\Delta_i=h(i)-\frac1{i-1}\sum_{j=1}^{i-1}h(j).
\]
Since \(M\ge i\ge j\) and \(\mathbb E|U-j|=(n+1)/2-j+j(j-1)/n\),
\[
h(j)=\frac{(n+1)(i-1)}{2(i+1)}-\frac{j(j-1)}n
\quad(1\le j\le i).
\]
Using \(\sum_{j=1}^{i-1}j(j-1)=(i-1)i(i-2)/3\), obtain
\[
\Delta_i=-\frac{i(2i-1)}{3n}.
\]
Directly \(\mathbb EF=(n^2-1)/3\), and multiplication by \(\Pr(R_i=1)=1/i\) gives the covariance. Summing over \(i=2,\ldots,n\) gives \(\operatorname{Cov}(F,R)=-(n^2-1)/(3n)\). As \(\Delta_i<0\), the stochastic order for \(F\) is strict.

**Squared-rank corollary.** Put \(c=\mathbb E M-\mathbb E U=(i-1)(n+1)/(2(i+1))\). For squared displacement, the analogue of \(h(j)\) is an affine function of \(j\) with slope \(-2c\). Hence its difference between position \(i\) and the average of positions \(1,\ldots,i-1\) equals \(-ic\). Multiplication by \(1/i\) gives the stated squared-rank covariance. This completes the proof for every \(n\ge2\) and \(2\le i\le n\).

## Verification

Run `python3 verify.py` using Python's standard library. It exhaustively enumerates all permutations through \(n=8\), verifies every fibre has cardinality \(i\), checks all adjacent-bubble couplings for five convex nondecreasing costs, reconstructs the conditional footrule distribution and all its upper tails, and checks the exact conditional-mean and summed-covariance identities using rational arithmetic. The extracted verifier passed 1,901,150 exact assertions. Finite enumeration corroborates but is not used to establish the all-size theorem, which follows from the fibre counting, convex Monge inequality, and conditional expectation calculation above.

## Relationship to prior work

Diaconis and Graham (1977) established the classical marginal Spearman-footrule theory and compared displacement with inversion counts. Their proof discusses the change in footrule under a single adjacent transposition; that deterministic ingredient is not claimed as new here. Gnedin (2006, first available arXiv version November 17, 2006) developed coherent permutations with record statistics and uniform initial-rank encodings, but did not state this record-position conditional rank-disarray coupling or its covariance profile. The contribution here is the constant-fibre record-forcing map combined with convex-order-compatible pathwise transport, and the exact regression and covariance identities for footrule and squared displacement.

## Limitations

The theorem conditions on **one specified upper-record position**, and it does not assert monotone ordering conditional on an entire set of record positions or on the total number of records. The coupling uses uniform permutations; general biased permutation models are outside scope. Stochastic ordering is not likelihood-ratio ordering. The result is a mathematical observation about rank statistics; it does not by itself establish an improvement in test power. Historical implicit coverage through a broader permutation-transport theorem remains possible. Independent external validation has not been performed.

## References

- P. Diaconis and R. L. Graham, *Spearman's Footrule as a Measure of Disarray*, Journal of the Royal Statistical Society B 39 (1977), 262–268, DOI: `10.1111/j.2517-6161.1977.tb01624.x`; full text: https://mathweb.ucsd.edu/~ronspubs/77_04_spearmans.pdf.
- A. Gnedin, *Coherent random permutations with record statistics*, arXiv:math/0611538, initial version November 17, 2006, https://arxiv.org/abs/math/0611538.
- H. K. Ury and D. C. Kleinecke, *Tables of the Distribution of Spearman's Footrule*, Applied Statistics 28 (1979), 271–275, DOI: `10.2307/2347198`; its subject is the marginal footrule distribution.
