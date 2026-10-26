# Cyclic-bridge maximum–position duality without sign symmetry

## Finding

Let \(n\ge2\), let \(X=(X_1,\ldots,X_n)\) be a square-integrable real random vector, and assume
\[
\sum_{i=1}^n X_i=0\quad\text{almost surely},
\]
with a law invariant under cyclic rotation. Set \(S_0=0\), \(S_j=\sum_{i=1}^jX_i\), and \(M=\max_{0\le j\le n}S_j\). For **every** \(1\le k<n\),
\[
\boxed{\operatorname{Cov}(M,S_k)=\tfrac12\operatorname{Var}(S_k).}\tag{1}
\]
Neither independent increments, exchangeability under all permutations, sign symmetry, nor a Gaussian law is required.

If, in addition, the increment vector is invariant in law under the **negated reversal**
\[
(X_1,\ldots,X_n)\ \overset d=\ (-X_n,\ldots,-X_1),
\]
then a stronger joint-law reflection holds:
\[
\boxed{(M-\tfrac12 S_k,S_k)\ \overset d=\ (M-\tfrac12S_k,-S_k).}\tag{2}
\]
Consequently, for each measurable odd \(g\) with \(\mathbb E[|M g(S_k)|+|S_k g(S_k)|]<\infty\),
\[
\boxed{\mathbb E[M g(S_k)]=\tfrac12\mathbb E[S_k g(S_k)].}\tag{3}
\]
The extra symmetry hypothesis is genuinely relevant to (2): without it, the marginal \(S_k\) need not even have a symmetric distribution, although (1) still holds.

## Assumptions and scope

The zero-sum condition is pathwise. Cyclic invariance means that for every integer \(j\), rotating the \(n\) increments by \(j\) places does not change their joint law. The maximum includes \(S_0=S_n=0\). All covariance identities in (1) are finite under the stated square-integrability assumptions.

The stronger reflection in (2) applies to all zero-sum exchangeable vectors that are also invariant under global sign change, such as symmetric iid increments conditioned on their sum being zero (where such conditioning is well-defined). It also applies to nonexchangeable laws that possess the two specified symmetries.

## Proof

**Orbit identity.** Fix any deterministic vector \((x_1,\ldots,x_n)\) with sum zero. Write \(h_0=0\), \(h_j=\sum_{i=1}^j x_i\), and take indices of \(h\) modulo \(n\). Put \(h_*=\max_{0\le j<n}h_j\). Starting the cyclic walk at site \(i\), its maximum and position at lag \(k\) are respectively
\[
m_i=h_*-h_i,\qquad s_{i,k}=h_{i+k}-h_i.
\]
Since \(\sum_i s_{i,k}=0\),
\[
\begin{aligned}
2\sum_{i=0}^{n-1}m_i s_{i,k}
&=-2\sum_i h_i(h_{i+k}-h_i)\\
&=\sum_i(h_{i+k}-h_i)^2
=\sum_i s_{i,k}^2.
\end{aligned}\tag{4}
\]
Average (4) over the random vector, and use cyclic invariance to identify the distribution of each rerooted pair with \((M,S_k)\). Also \(\mathbb E S_k=0\), by cyclic invariance and \(\sum_i s_{i,k}=0\). Thus \(2\mathbb E[MS_k]=\mathbb E[S_k^2]\), proving (1).

**Joint reflection.** First reroot the cyclic walk at \(k\). Its maximum becomes \(M-S_k\). Then reverse the direction of time in its *height path*, so that the resulting increments are the negatives of its former increments in reverse order. This operation preserves the maximum and turns its value at time \(k\) into \(-S_k\). Each operation preserves the increment law under the respective hypothesis. Accordingly
\[
(M,S_k)\ \overset d=\ (M-S_k,-S_k).
\]
Subtracting half of the second coordinate from the first establishes (2). For odd \(g\), the centered first coordinate in (2) has zero mixed expectation against \(g(S_k)\), yielding (3). This argument involves no continuity assumption or uniqueness of the maximizing time.

**Boundary.** Let \(n=3\) and choose uniformly among the three cyclic rotations of \((2,-1,-1)\). At lag one, \(S_1\) has masses \(1/3\) at \(2\) and \(2/3\) at \(-1\). Thus (2) is impossible, since it would force a symmetric marginal, while (1) holds with \(\mathbb E[MS_1]=1=\tfrac12\mathbb E[S_1^2]\).

**Two natural applications.** For a simple symmetric random walk of even length \(n\), conditioned to return to zero, the increments form a uniform permutation of equally many \(+1\) and \(-1\) steps. Their conditional covariance is \(\operatorname{Var}(S_k)=k(n-k)/(n-1)\), so
\[
\boxed{\operatorname{Cov}(M,S_k)=\frac{k(n-k)}{2(n-1)}}\qquad(1\le k<n).
\tag{5}
\]
In the continuous Gaussian setting, let \((B_t)_{0\le t\le1}\) be a standard Brownian bridge and \(M_B=\sup_{0\le t\le1}B_t\). Cyclic rerooting and reversal preserve its law. Integrating the continuous analog of (4) over all possible roots gives
\[
\boxed{\operatorname{Cov}(M_B,B_t)=\frac{t(1-t)}2}\qquad(0\le t\le1).
\tag{6}
\]
The continuous analog of (2) holds as well. In particular, for all integers \(q\ge0\),
\[
\boxed{\mathbb E[M_B B_t^{2q+1}]
=\frac{(2q+1)!!}{2}[t(1-t)]^{q+1}.}\tag{7}
\]
Equation (7) follows from (3) and centered Gaussian even moments; it is an illustrative specialization, not a claim of priority over classical Brownian reflection formulas.

## Verification

Run \(\texttt{python verify.py}\) with Python 3. The exact-integer verifier enumerates all 10,376 zero-sum strings of lengths two through seven with coordinates in \(\{-2,-1,0,1,2\}\), checking 59,387 orbit-and-lag identities. It additionally checks the full reflected joint histogram under negated reversal, enumerates 1,274 simple symmetric bridges through length twelve, checks odd powers one, three and five, and exhibits the skew three-step boundary. All tests passed when this result was prepared. The infinite claims follow from (4) and the law-preserving operations; finite checks are not substitutes for proof.

## Relationship to prior work

Bertoin, Chaumont, and Pitman (2003, §§2 and 4) explicitly study cyclic rerooting and bridge transformations, including beyond independent increments. Their cyclic operation supplies relevant background, but the reviewed results concern first-passage bridges and conditional path transforms rather than the maximum–intermediate-position mixed moment (1) or joint symmetry (2).

Lupu, Pitman, and Tang (first arXiv version 2013, journal 2015) study Vervaat transforms and path decomposition. Their inspected exposition does not state (1) for skew cyclic increment laws. Classical Gaussian bridge reflection identities may imply the Brownian specialization (6)–(7); those specializations are not the priority claim.

Anis and Gharib (1980) derive marginal maximum-variance formulas for exchangeable partial sums, rather than the universal covariance with a marked intermediate bridge position. Their complete text was not accessible in this review, so a historical-priority reservation remains.

A related publicly available maximum–endpoint identity assumes both reversal and global sign symmetry of a possibly nonexchangeable increment vector. It controls covariance with the **terminal sum**. Here the terminal sum is identically zero, and (1) allows skew cyclic increment laws without sign symmetry. Thus the earlier endpoint law does not imply the nonzero intermediate-position assertion under its hypotheses.

## Limitations

Novelty is assessed against the sources described here, not established by exhaustive historical coverage. The central contribution is the finite cyclic-bridge identity for skew laws and its joint-law refinement under negated reversal; the Brownian formulas alone are elementary consequences of known reflection and re-rooting principles. The negated-reversal assumption is sufficient, not claimed necessary, for the conditional symmetry. No analogous unconditional reflection is claimed for arbitrary skew cyclic laws. Neither sign nor moment assertions are made when the necessary expectations diverge.

## References

1. J. Bertoin, L. Chaumont, and J. Pitman, *Path transformations of first passage bridges*, Berkeley Technical Report 643, dated 14 July 2003; https://statistics.berkeley.edu/sites/default/files/tech-reports/643.pdf.
2. T. Lupu, J. Pitman, and W. Tang, *The Vervaat transform of Brownian bridges and Brownian motion*, arXiv:1310.3889v1, posted 15 October 2013; *Electronic Journal of Probability* 20 (2015), no. 51, DOI 10.1214/EJP.v20-3744.
3. A. A. Anis and M. Gharib, *On the variance of the maximum of partial sums of n-exchangeable random variables with applications*, *Journal of Applied Probability* 17 (1980), 432–439; DOI 10.2307/3213032.
4. *Reversal and sign symmetry force a half-variance maximum–endpoint law*, publicly available research result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-reversal-and-sign-symmetry-force-a-half-variance-maximum-endpoin--5e8da51794ea.
