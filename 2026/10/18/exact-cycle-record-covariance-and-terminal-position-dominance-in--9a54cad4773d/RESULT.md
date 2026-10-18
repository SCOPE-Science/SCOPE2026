# Exact cycle–record covariance and terminal-position dominance in uniform permutations

## Finding
Let \(\pi\) be one uniformly distributed permutation of \(\{1,\ldots,n\}\), let \(C_n\) be its number of disjoint cycles, and let \(I_{n,j}=\mathbf1\{\pi(j)>\max_{1\le i<j}\pi(i)\}\) mark a strict left-to-right maximum, with \(I_{n,1}=1\). The record count is \(R_n=\sum_{j=1}^n I_{n,j}\).

For **every integer \(n\ge1\) and every \(1\le j\le n\)**,
\[
\operatorname{Cov}(C_n,I_{n,j})=\frac{j-1}{j^2\binom{n}{j}}.
\]
Consequently, for \(n\ge2\),
\[
\operatorname{Cov}(C_n,R_n)=\sum_{j=2}^n\frac{j-1}{j^2\binom{n}{j}}>0,
\qquad
\operatorname{Cov}(C_n,R_n)=\frac1n+O\!\left(\frac{\log n}{n^2}\right).
\]
Both marginal variances are \(H_n-H_n^{(2)}\), with \(H_n=\sum_{k=1}^n1/k\) and \(H_n^{(2)}=\sum_{k=1}^n1/k^2\). In particular,
\[
\operatorname{Corr}(C_n,R_n)\sim\frac{1}{n\log n}.
\]
The record at the final position contributes \((n-1)/n^2\), which is asymptotically the entire covariance; all other record positions together contribute \(O(\log n/n^2)\). For \(n=1\), all these covariances equal zero.

## Assumptions and scope
The permutation is uniform over the entire symmetric group. A disjoint cycle is counted in the usual functional decomposition of that **same** permutation, while records are computed from its **one-line** values; these statistics must not be identified through a separate Foata-transformed permutation. No independence between the cycle and record statistics is assumed. The theorem applies to all stated finite sizes; the asymptotic statement is as \(n\to\infty\).

## Proof
Introduce the Ewens cycle tilt \(\mathbb P_\theta(\pi)=\theta^{C_n(\pi)}/(\theta(\theta+1)\cdots(\theta+n-1))\) for \(\theta>0\). Set \(p_{m,j}(\theta)=\mathbb P_\theta(I_{m,j}=1)\). Differentiating the finite normalized sum gives
\[
\left.\frac{\partial}{\partial\theta}p_{n,j}(\theta)\right|_{\theta=1}
=\operatorname{Cov}(C_n,I_{n,j}),
\]
because the logarithmic derivative of the weight at \(\theta=1\) is \(C_n\) minus its expectation.

For \(m=j\), the last entry is a record exactly when \(\pi(j)=j\), i.e. the newest maximum is introduced as a singleton cycle. Under the Ewens insertion rule, this occurs with probability \(\theta/(\theta+j-1)\). Thus
\[
p_{j,j}(\theta)=\frac{\theta}{\theta+j-1},\qquad
p_{j,j}'(1)=\frac{j-1}{j^2}.
\]
For \(m>j\), generate the Ewens permutation on \(\{1,\ldots,m\}\) by either leaving \(m\) fixed (weight \(\theta\)) or inserting \(m\) immediately after one of the \(m-1\) existing points in cycle notation (unit weight for each location). If insertion follows an index below \(j\), the new maximal value appears before \(j\) and destroys its record; if insertion follows \(j\), the value at position \(j\) becomes \(m\) and is certainly a record. An insertion after an index above \(j\), or an independent singleton, leaves the record indicator at \(j\) unchanged. This yields the exact conditional recurrence
\[
p_{m,j}(\theta)=\frac{(\theta+m-1-j)p_{m-1,j}(\theta)+1}{\theta+m-1}.
\]
Uniformity at \(\theta=1\) gives \(p_{m-1,j}(1)=1/j\): in a uniform permutation each position among the first \(j\) is equally likely to be the maximum. Differentiate the recurrence. The derivatives of its coefficients cancel exactly against \(p_{m-1,j}(1)=1/j\), leaving
\[
p'_{m,j}(1)=\frac{m-j}{m}\,p'_{m-1,j}(1).
\]
Iterating from \(m=j\) to \(m=n\) proves
\[
p'_{n,j}(1)=\frac{j-1}{j^2}\prod_{m=j+1}^n\frac{m-j}{m}
=\frac{j-1}{j^2\binom nj}.
\]
This also covers \(j=1\): the indicator is identically one and the derivative vanishes. Linearity of covariance gives the finite total formula; its strict positivity for \(n\ge2\) follows from any term with \(j\ge2\).

For the asymptotic, isolate the last term \((n-1)/n^2=1/n-1/n^2\). The penultimate term is \((n-2)/(n(n-1)^2)=O(n^{-2})\). For \(n\ge4\) and \(2\le j\le n-2\), the binomial coefficient satisfies \(\binom nj\ge\binom n2\). Hence
\[
0\le\sum_{j=2}^{n-2}\frac{j-1}{j^2\binom nj}
\le\frac{1}{\binom n2}\sum_{j=2}^{n-2}\frac1j
=O\!\left(\frac{\log n}{n^2}\right).
\]
The familiar independent-Bernoulli decompositions of cycle count (Ewens insertion) and uniform record count (sequential ranks) give identical variances \(\sum_{k=1}^n(k-1)/k^2=H_n-H_n^{(2)}\sim\log n\). Dividing the covariance by that variance establishes the correlation limit. No joint central limit theorem or independence assertion is needed.

## Verification
The accompanying standalone standard-library program `verify.py` enumerates every permutation at each size \(2\le n\le9\), independently computes cycle and record statistics, and compares exact rational covariances at every record position and globally against the displayed formulas. It also validates the Ewens recursion and its parameter derivative over a broad exact-rational range, and independently enumerates Ewens-weighted permutations for seven small sizes at two nonuniform parameter values. Running `python3 verify.py` completed 1,720 exact assertions. Enumeration validates finite cases, while the analytic insertion proof establishes the unbounded quantifiers.

## Relationship to prior work
Kabluchko and Marynych [1] provide the record/counting interpretation of Stirling numbers and the Lah family of records in random compositions; they give the established one-statistic background, not a joint same-permutation cycle/record covariance. Gnedin [2] studies distributions tilted by upper/lower record counts and explains that cycle-weighted Ewens and record-weighted Ewens correspond under a bijection: the transformed permutation is generally **not the original permutation**, so this marginal correspondence does not imply our covariance. Dubach [3] gives marginal record laws for uniform and conjugation-invariant random permutations, but its record-limit theorem likewise does not yield the finite positionwise mixed moments here. Separately, published inversion–cycle covariance formulas concern inversion indicators rather than the nonlinear prefix-maximum events defining records. The contribution claimed here is exclusively the positionwise same-permutation covariance and its concentration near the final position; classical marginal laws and the Ewens insertion construction are credited as known.

## Limitations
No claim is made about arbitrary conjugation-invariant laws, joint independence, or other permutation statistics. The bound on off-terminal contributions is sufficient for the stated first-order asymptotic, not a complete higher-order expansion. The search and inspected sources do not rule out an older equivalent mixed generating-function identity or unpublished solution; independent priority assessment has not been performed.

## References
[1] Z. Kabluchko and A. Marynych, *Lah distribution: Stirling numbers, records on compositions, and convex hulls of high-dimensional random walks*, arXiv:2105.11365 (first publicly posted 2021-05-24), https://arxiv.org/abs/2105.11365 ; full text https://arxiv.org/html/2105.11365v2 .

[2] A. Gnedin, *Coherent random permutations with record statistics*, Discrete Mathematics & Theoretical Computer Science Proceedings AH (2007), https://dmtcs.episciences.org/en/articles/3551/download .

[3] V. Dubach, *A geometric approach to conjugation-invariant random permutations*, Probability Theory and Related Fields (2025), Section 2.3, https://doi.org/10.1007/s00440-025-01449-7 .
