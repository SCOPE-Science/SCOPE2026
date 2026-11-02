# Logarithmic Eulerian universality for minimum-of-choice permutations

## Finding

Fix an integer \(k\ge 1\). Starting with the ordered cards \(1,\ldots,n\), at each step independently draw \(k\) cards **with replacement** from those remaining, remove the smallest drawn card, and record the removal order as a permutation. Let \(D_{n,k}\) count its adjacent descents, for \(n\ge2\). For \(m=2,\ldots,n\), put
\[
 p_{m,k}=1-\frac{\sum_{r=0}^{m-1}r^k\big((r+1)^k-r^k\big)}{m^k(m-1)^k}.
\]
Then \(\mathbb E D_{n,k}=\sum_{m=2}^n p_{m,k}\). Every \(p_{m,1}=1/2\), while \(p_{m,k}<1/2\) for all \(m\ge2\) and \(k\ge2\). For each *fixed* \(k\), define \(c_k=k(k-1)/(2(2k-1))\). As \(n\to\infty\),
\[
\mathbb ED_{n,k}=\frac{n-1}{2}-c_k\log n+O_k(1),\qquad
\operatorname{Var}(D_{n,k})=\frac{n+1}{12}+O_k(\log n),
\]
\[
\frac{D_{n,k}-\mathbb ED_{n,k}}{\sqrt{n/12}}\Longrightarrow N(0,1).
\]
There is, moreover, a coupling to the classical Eulerian descent count \(E_n\) of a uniform permutation of size \(n\) such that
\[
\mathbb E|D_{n,k}-E_n|\le4kH_{n-1},\qquad H_{n-1}=\sum_{j=1}^{n-1}\frac1j.
\]
Consequently, for every fixed \(k\ge2\), the order-one Wasserstein distance between their integer-valued laws is \(\Theta_k(\log n)\), whereas at \(k=1\) the laws coincide. The individual descent indicators have a dependence graph consisting only of adjacent positions, for every \(n,k\).

## Assumptions and scope

The \(k\) draws **at each removal stage are independent and with replacement**; draws at different stages are independent. For a stage with \(m\) remaining cards, \(J_m\) denotes the rank of the removed card among those \(m\), indexed from smallest to largest. The asymptotic statements require \(k\) fixed as \(n\to\infty\), and their constants may depend on \(k\). The Wasserstein cost is absolute difference on integers, with no variance normalization. \(H_{n-1}\) denotes the harmonic sum shown above. No assertion is made for growing \(k\) about the Gaussian limit, sharp Wasserstein order, or remainder constants.

## Proof

**Independent rank representation.** At a stage with \(m\) remaining cards,
\[
\Pr\{J_m>j\}=\left(\frac{m-j}{m}\right)^k\quad(0\le j\le m).
\]
Since the choice depends only on ranks and fresh random draws are used, \(J_1,\ldots,J_n\) are mutually independent. The next removed card is smaller than the present removed card exactly when its rank among the \(m-1\) survivors is strictly less than the present rank. Thus
\[
D_{n,k}=\sum_{m=2}^n B_m^{(k)},\qquad B_m^{(k)}=\mathbf1\{J_{m-1}<J_m\}.
\]
Indicators at indices differing by at least two depend on disjoint independent rank coordinates. This gives the asserted one-dependence and yields the exact one-index formula in the finding: using \(r=m-j\), the mass of \(J_m=j\) is \(\big((r+1)^k-r^k\big)/m^k\), and the probability that \(J_{m-1}\ge j\) is \(r^k/(m-1)^k\).

**Strict downward bias.** Put \(\Delta_r=(r+1)^k-r^k\). Telescoping squares gives
\[
2\sum_{r=0}^{m-1}r^k\Delta_r=m^{2k}-\sum_{r=0}^{m-1}\Delta_r^2.
\]
For \(k=1\), \(\Delta_r=1\) and the formula gives \(p_{m,1}=1/2\). For \(k\ge2\), the positive increments \(\Delta_r\) increase strictly with \(r\), so
\[
\sum_{r=0}^{m-1}\Delta_r^2<\Delta_{m-1}\sum_{r=0}^{m-1}\Delta_r
=m^k\big(m^k-(m-1)^k\big).
\]
Substitution proves \(p_{m,k}<1/2\), for *every* integer \(m\ge2\).

**Sharp logarithmic drift.** For each fixed \(k\), expand \(\Delta_r=k r^{k-1}+\binom{k}{2}r^{k-2}+O_k((r+1)^{k-3})\) (separately interpret \(k=1\) and \(k=2\), where missing terms vanish). Summing powers by Euler--Maclaurin, or by their finite polynomial identities, gives
\[
\sum_{r=0}^{m-1}r^k\Delta_r
=\frac12m^{2k}+\left(-\frac k2+\frac{k(k-1)}{2(2k-1)}\right)m^{2k-1}+O_k(m^{2k-2}).
\]
Dividing by \(m^k(m-1)^k=m^{2k}(1-k/m+O_k(m^{-2}))\) proves
\[
p_{m,k}=\frac12-\frac{k(k-1)}{2(2k-1)m}+O_k(m^{-2}).
\]
The \(m^{-2}\) errors sum absolutely, while \(\sum_{m=2}^n m^{-1}=\log n+O(1)\), yielding the claimed mean.

**Quantitative coupling and Gaussian law.** Take independent variables \(Y_m\), each the minimum of \(k\) independent continuous uniforms on \((0,1)\); their common density is \(k(1-y)^{k-1}\le k\). The variables \(\lceil mY_m\rceil\) have precisely the independent rank laws above. On the same space define \(A_m=\mathbf1\{Y_{m-1}<Y_m\}\) and \(E_n=\sum_{m=2}^n A_m\). Because the \(Y_m\) are independent with a common continuous law, \(E_n\) has the Eulerian descent-count distribution of a uniform permutation. If \(|Y_m-Y_{m-1}|>2/(m-1)\), the two ceiling ranks have the same strict ordering as their continuous inputs; hence
\[
\Pr(B_m^{(k)}\ne A_m)\le\Pr\big\{|Y_m-Y_{m-1}|\le2/(m-1)\big\}\le\frac{4k}{m-1}.
\]
Summing proves the explicit coupling bound. Wasserstein distance is at most the expectation under this coupling. It is at least the absolute difference of the two means, which equals \(c_k\log n+O_k(1)\) for fixed \(k\ge2\). This proves the \(\Theta_k(\log n)\) order.

The \(A_m\) are one-dependent with \(\mathbb EA_m=1/2\) and \(\mathbb E(A_mA_{m-1})=1/6\). The rank-comparison error bound gives \(\mathbb EB_m^{(k)}=1/2+O_k(1/m)\) and \(\mathbb E(B_m^{(k)}B_{m-1}^{(k)})=1/6+O_k(1/m)\). Nonadjacent covariances vanish exactly. Summing the variance and adjacent-covariance terms yields \(\operatorname{Var}(D_{n,k})=(n+1)/12+O_k(\log n)\). The bounded, one-dependent \(A_m-1/2\) have a central limit theorem: split them into independent blocks of length \(\lfloor n^{1/3}\rfloor\) separated by one omitted indicator; the omitted terms have variance \(O(n^{2/3})\), and independent block sums satisfy the Lindeberg condition because their magnitudes are \(o(\sqrt n)\). The Eulerian variance is \((n+1)/12\). Finally, Markov's inequality and the coupling show \((D_{n,k}-E_n)/\sqrt n\to0\) in probability; centering changes by \(O_k(\log n)\). Slutsky's theorem gives the stated Gaussian limit.

## Verification

The standalone standard-library program `checker.py` reconstructs weighted removal permutations independently of the one- and two-index rank formulas. It enumerates every permutation through seven cards for four choice parameters and checks its descent number against the rank indicators, checks exact normalization, means, variances and adjacent joint probabilities, and evaluates one-index probabilities and strict inequalities across additional sizes and parameters. Its execution produced `PASS` with 24,443 counted checks. These finite checks are independent diagnostics, not substitutes for the proofs for all \(n\) and \(k\). To reproduce: execute `python3 checker.py` from the directory containing this file and the checker.

## Relationship to prior work

Travers introduced the minimum-of-choice model and proved that the relative ranks are independent, deriving inversion and longest-increasing-subsequence results. The rank law used here is explicitly credited to his Proposition 6. Neither the descent regression, its strict bias, its logarithmic constant, nor the coupling theorem is stated in the inspected full text. Savage and Visontai study unweighted ascent statistics of generalized inversion sequences, not the present nonuniform product-rank measure. Jasińska and Ráth obtain permuton limits and **nonconsecutive** pattern-density laws for a generalization including this model; those laws do not imply adjacent-descent statistics or their logarithmic correction. Fang and collaborators analyze descent-generated walks for uniform and Mallows-distributed permutations, rather than the minimum-of-choice law. Borodin, Diaconis and Fulman establish much more general one-dependent and determinantal descent processes, including a distinct stationary Mallows model; their general one-dependence results do not specify the nonstationary minimum-of-choice logarithmic bias or the rank-quantile Wasserstein comparison. These comparisons support the claimed distinctness, not an assertion of exhaustive historical priority.

## Limitations

Historical priority outside the inspected literature is not certified. The independence of the rank coordinates is a previously established ingredient, not claimed as new. The exact finite-size probability, strict-bias argument, logarithmic correction and sharp-order coupling form the present result. The \(O_k\) constants are not uniform in increasing \(k\). No local limit theorem, exact finite-size variance polynomial, or sharp leading constant for Wasserstein distance is proved.

## References

- N. F. Travers, *Inversions and Longest Increasing Subsequence for \(k\)-Card-Minimum Random Permutations*, arXiv:1406.3911, first posted 2014-06-16, especially Sections 2 and 3 and Proposition 6. https://arxiv.org/abs/1406.3911
- C. D. Savage and M. Visontai, *The \(\mathbf{s}\)-Eulerian polynomials have only real roots*, arXiv:1208.3831, first posted 2012-08-19, especially Sections 1--2. https://arxiv.org/abs/1208.3831
- J. Jasińska and B. Ráth, *Permuton limit of a generalization of the Mallows and \(k\)-card-minimum models*, arXiv:2412.07258, first posted 2024-12-10, Sections 2--3. https://arxiv.org/abs/2412.07258
- A. Borodin, P. Diaconis and J. Fulman, *On adding a list of numbers (and other one-dependent determinantal processes)*, arXiv:0904.3740, first posted 2009-04-23, especially Sections 4--5. https://arxiv.org/abs/0904.3740
- X. Fang et al., *Arcsine laws for random walks generated from random permutations with applications to genomics*, arXiv:2001.08857, first posted 2020-01-24, Sections 2--3. https://arxiv.org/abs/2001.08857
