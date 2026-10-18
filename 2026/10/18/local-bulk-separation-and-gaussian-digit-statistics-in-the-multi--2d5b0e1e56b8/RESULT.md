# Local–bulk separation and Gaussian digit statistics in the multiplicative golden-mean system

## Finding

Let
\[
X=\{x\in\{0,1\}^{\mathbb N}:x_jx_{2j}=0\text{ for every }j\ge1\}.
\]
For each integer \(N\ge1\), let \(U_N\) be uniform on its admissible \(N\)-digit prefixes. We regard a sampled prefix as an element of \(X\) by putting zero at every coordinate beyond \(N\), and write \(S_N=\sum_{j=1}^N x_j\).

Define three integer sequences by
\[
(a_0,b_0,c_0)=(1,0,0),\quad (a_1,b_1,c_1)=(2,1,1),
\]
and, for every \(k\ge2\),
\[
\begin{aligned}
a_k&=a_{k-1}+a_{k-2},\\
b_k&=b_{k-1}+b_{k-2}+a_{k-2},\\
c_k&=c_{k-1}+c_{k-2}+2b_{k-2}+a_{k-2}.
\end{aligned}
\]
Set
\[
\alpha=\sum_{k\ge1}\frac{b_k}{2^{k+1}a_k},\qquad
\sigma^2=\sum_{k\ge1}\frac{1}{2^{k+1}}\left(\frac{c_k}{a_k}-\frac{b_k^2}{a_k^2}\right).
\]
Then \(\alpha=0.366541662066731\ldots\) and \(\sigma^2=0.148936034454920\ldots>0\), and
\[
\frac{S_N}{N}\xrightarrow[U_N]{\mathrm{prob.}}\alpha,\qquad
\frac{S_N-\alpha N}{\sigma\sqrt N}\xrightarrow[U_N]{\mathrm{law}}\mathcal N(0,1).
\]

The probability measures \(U_N\) converge on every fixed finite collection of coordinates to a probability measure \(\nu\) on \(X\). To define \(\nu\), independently for each positive odd \(i\), run a golden-mean Markov chain on the positions \(i,2i,4i,\ldots\) with initial law \((1/\varphi,1/\varphi^2)\) on \((0,1)\) and transition matrix
\[
P=\begin{pmatrix}\varphi^{-1}&\varphi^{-2}\\1&0\end{pmatrix},
\qquad \varphi=\frac{1+\sqrt5}{2}.
\]
This locally limiting measure has the **different** almost-sure digit density
\[
\nu\!\left(\lim_{N\to\infty}\frac{S_N}{N}=\beta\right)=1,
\qquad \beta=\frac{2}{4+\sqrt5}=0.320714913181856\ldots.
\]
In fact \(\alpha>1/3>\beta\). With \(\delta=\alpha-\beta>0\), the total variation distance of the two measures on the first \(N\) coordinates satisfies, for all sufficiently large \(N\),
\[
\boxed{\left\|U_N-\nu|_{\{1,\ldots,N\}}\right\|_{\mathrm{TV}}
\ge 1-4\exp\!\left(-\frac{\delta^2N}{48}\right).}
\]
Thus convergence of all fixed-coordinate distributions coexists with asymptotically maximal total-variation separation at the growing-volume scale.

## Assumptions and scope

All logarithms in calculations are natural unless indicated otherwise. The alphabet is binary, the constraint is the multiplicative nearest-neighbor exclusion \(x_jx_{2j}=0\), and the finite-volume law is **uniform on admissible prefixes**, not a preselected Markov or dimension-maximizing probability law. Convergence on fixed coordinates means convergence of every finite-coordinate cylinder probability; it is distinct from total-variation convergence on all first \(N\) digits. The infinite measure \(\nu\) is not claimed to be invariant under the additive left shift; the defining system is multiplicative.

## Proof

**1. Exact independent-chain factorization.** Every positive integer has a unique representation \(2^r i\), with \(r\ge0\) and \(i\) odd. The constraints connect only consecutive elements of each chain \(i,2i,4i,\ldots\). For odd \(i\le N\), its length in the first \(N\) coordinates is
\[
L_i(N)=1+\left\lfloor\log_2(N/i)\right\rfloor.
\]
The uniform finite-volume law is exactly the independent product of uniform legal golden-mean words of the respective lengths. The number \(d_k(N)\) of chains of length \(k\) satisfies
\[
d_k(N)=\#\{i\text{ odd}:N/2^k<i\le N/2^{k-1}\}
=\frac{N}{2^{k+1}}+O(1)
\]
for \(1\le k\le1+\lfloor\log_2N\rfloor\). The count and independence are exact; only the displayed approximation has a bounded rounding error.

**2. Exact single-chain moments.** For a uniform legal length-\(k\) binary word, let \(W_k\) count its ones. Its unnormalized exponential generating polynomial is
\[
Z_0(t)=1,\quad Z_1(t)=1+e^t,\quad
Z_k(t)=Z_{k-1}(t)+e^tZ_{k-2}(t),\quad k\ge2.
\]
Partitioning according to an initial zero or an initial \(10\) proves this recurrence. Consequently \(a_k=Z_k(0)\), \(b_k=Z'_k(0)\), \(c_k=Z''_k(0)\). Thus
\[
\mathbb E W_k=\frac{b_k}{a_k},\quad
\operatorname{Var}(W_k)=\frac{c_k}{a_k}-\left(\frac{b_k}{a_k}\right)^2,
\]
which reconstructs all stated recurrences. The finite-volume mean and variance are exactly the corresponding sums over the \(L_i(N)\).

**3. Bulk limits and the central limit theorem.** Because \(0\le W_k\le k\), its mean is bounded by \(k\), and its variance by \(k^2/4\). The dyadic series defining \(\alpha\) and \(\sigma^2\) therefore converge absolutely. Substituting the chain counts and bounding the tail beyond \(1+\lfloor\log_2N\rfloor\) gives
\[
\mathbb E_{U_N}S_N=\alpha N+O((\log N)^2),\quad
\operatorname{Var}_{U_N}(S_N)=\sigma^2N+O((\log N)^3).
\]
The \(k=1\) chains alone contribute \(2^{-2}\cdot\tfrac14=\tfrac1{16}\) to \(\sigma^2\), so \(\sigma^2>0\). The centered chain totals form an independent triangular array. Their individual absolute sizes are at most \(1+\log_2N=o(\sqrt N)\); hence Lindeberg's condition holds, yielding a Gaussian limit after centering by the true mean and normalizing by its true standard deviation. The displayed error estimates allow the asserted deterministic centering and normalization. Chebyshev's inequality gives the finite-volume law of large numbers.

**4. Cylinderwise local limit.** Write \(A=\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\). Its Perron eigenvalue is \(\varphi\), and a positive right eigenvector is \(r=(\varphi,1)\). For any fixed legal word \(a_0\cdots a_{h-1}\), the number of length-\(L\) legal continuations is \((A^{L-h}\mathbf1)_{a_{h-1}}\). Perron–Frobenius asymptotics, divided by the total number \(\mathbf1^{T}A^{L-1}\mathbf1\), give the limiting cylinder probability
\[
\frac{r_{a_{h-1}}}{(r_0+r_1)\varphi^{h-1}}
=\frac{r_{a_0}}{r_0+r_1}
\prod_{j=0}^{h-2}\frac{A_{a_ja_{j+1}}r_{a_{j+1}}}{\varphi r_{a_j}}.
\]
These are precisely the initial law and transition probabilities specified for \(\nu\). Each fixed finite coordinate collection involves finitely many chains, each of which has length tending to infinity under \(U_N\); independence proves local weak convergence to their product law \(\nu\).

**5. Almost-sure digit density of the local limit.** Put \(s=\varphi^{-2}\) and let \(q_r\) be the probability that the digit at position \(2^ri\) is one under \(\nu\), where \(i\) is any odd integer. The Markov chain gives
\[
q_0=s,\qquad q_{r+1}=s(1-q_r),\qquad
q_r=\frac{s}{1+s}+\frac{s^2}{1+s}(-s)^r.
\]
The density of indices with dyadic valuation exactly \(r\) tends to \(2^{-r-1}\). The uniform boundedness of the \(q_r\) then gives
\[
\lim_{N\to\infty}\frac{\mathbb E_\nu S_N}{N}
=\sum_{r\ge0}\frac{q_r}{2^{r+1}}
=\frac{2s}{2+s}=\frac2{4+\sqrt5}=\beta.
\]
For either \(U_N\) or \(\nu\), the total contribution from one odd-indexed chain lies in an interval of length at most \(L_i(N)\). Using
\[
\sum_{i\le N,\ i\text{ odd}}L_i(N)^2
=\sum_{k\ge1}(2k-1)\#\{i\text{ odd}:L_i(N)\ge k\}
\le N\sum_{k\ge1}\frac{2k-1}{2^{k-1}}=6N,
\]
Hoeffding's inequality implies, for all \(u>0\),
\[
\Pr\bigl(|S_N-\mathbb E S_N|\ge uN\bigr)
\le 2e^{-u^2N/3}.
\]
For \(\nu\), these probabilities are summable; Borel–Cantelli yields \(S_N/N\to\beta\) almost surely.

**6. A strict gap and exponential total-variation separation.** The first five terms of \(\alpha\) sum exactly to
\[
\sum_{k=1}^{5}\frac{b_k}{2^{k+1}a_k}=\frac{1667}{4992}>\frac13.
\]
Every remaining term is nonnegative, while \(\beta=2/(4+\sqrt5)<1/3\), so \(\delta=\alpha-\beta>0\). For all sufficiently large \(N\), the expectations of \(S_N/N\) under \(U_N\) and \(\nu\) lie within \(\delta/4\) of \(\alpha\) and \(\beta\), respectively. Let \(E_N=\{S_N/N>(\alpha+\beta)/2\}\). The preceding Hoeffding bound at \(u=\delta/4\) implies
\[
U_N(E_N)\ge1-2e^{-\delta^2N/48},\quad
\nu(E_N)\le2e^{-\delta^2N/48}.
\]
The difference of these probabilities is a lower bound for total-variation distance, proving the last assertion.

## Verification

The standalone `verify.py` uses independent exact enumeration of all finite admissible words for 18 horizons, checking their first two count moments against the independent-chain recurrence. It also checks 1,999 exact finite-chain squared-length bounds, five finite-length Perron-cylinder approximations, and high-precision truncated series. It reports \(\alpha\approx0.3665416620667312\), \(\sigma^2\approx0.1489360344549201\), and \(\beta\approx0.3207149131818564\). These are finite checks only; the proof of the infinite limiting claims is analytical.

The bounds on the omitted terms after index \(K\) are
\[
0\le\alpha-\sum_{k=1}^K\frac{b_k}{2^{k+1}a_k}
\le\frac{K+2}{2^{K+1}},
\]
and
\[
0\le\sigma^2-\sum_{k=1}^K\frac{\operatorname{Var}(W_k)}{2^{k+1}}
\le\frac{K^2+4K+6}{2^{K+3}}.
\]
They make the numerical values reproducible without any unproved infinite-computation assertion.

## Relationship to prior work

Fan, Liao and Ma established the independent dyadic-chain counting and box dimension of the multiplicative golden-mean system. Kenyon, Peres and Solomyak further analyzed its Hausdorff and Minkowski dimensions and established a variational principle for multiplicative subshifts. Their dimension formula and product-measure machinery are acknowledged as prior results, not innovations here. Peres and Solomyak further studied Hausdorff gauges and concentration for specially chosen infinite product measures; their Markov-chain calculations are closely related to the present proof.

The present claim distinguishes two different probability constructions: uniform finite-prefix measures and the infinite product of their **local** Perron limits. It gives their different digit densities, a quantified asymptotically maximal total-variation separation despite convergence of all fixed cylinders, and a central limit theorem with an explicit variance series for the finite-volume ensemble. None of those conclusions is asserted merely from the earlier dimension formulas. Historical priority beyond the inspected sources remains uncertain.

## Limitations

The results concern the binary multiplicative constraint, uniform finite-prefix sampling and its particular local-limit law. The theorem does not generalize automatically to all multiplicative subshifts, arbitrary interactions or alternate finite-volume boundary weights. The total-variation estimate holds only for sufficiently large \(N\), not with a specified minimum finite cutoff. Gaussian convergence is weak convergence, not a local limit theorem or a Berry–Esseen estimate. Direct finite enumeration does not prove the infinite asymptotics. 

## References

1. R. Kenyon, Y. Peres and B. Solomyak, *Hausdorff dimension for fractals invariant under the multiplicative integers*, arXiv:1102.5136 (first publicly submitted 2011-02-25), *Ergodic Theory and Dynamical Systems* **32** (2012), 1567–1584; https://arxiv.org/abs/1102.5136.
2. R. Kenyon, Y. Peres and B. Solomyak, *Hausdorff dimension of the multiplicative golden mean shift*, arXiv:1105.3441 (first publicly submitted 2011-05-17), *Comptes Rendus Mathématique* **349** (2011), 625–628; https://arxiv.org/abs/1105.3441.
3. Y. Peres and B. Solomyak, *The multiplicative golden mean shift has infinite Hausdorff measure*, arXiv:1201.5842 (first publicly submitted 2012-01-27); https://arxiv.org/abs/1201.5842.
4. W. Hoeffding, *Probability inequalities for sums of bounded random variables*, *Journal of the American Statistical Association* **58** (1963), 13–30.
5. A.-H. Fan, L. Liao and J. Ma, *Level sets of multiple ergodic averages*, arXiv:1105.3032 (first publicly submitted 2011-05-16); https://arxiv.org/abs/1105.3032.
