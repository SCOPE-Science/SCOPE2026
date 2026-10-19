# A size-ordered covariance reversal hierarchy for geometric components on the circle

## Finding

Fix an integer \(j\ge1\). Let \(C_{n,j}(r)\) be the number of \(j\)-vertex connected components, and \(K_n(r)\) the total number of connected components, of the one-dimensional binomial random geometric graph on the unit circle with connection radius \(r\). For each fixed \(t>0\), writing \(p=e^{-t}\),

\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(C_{n,j}(t/n),K_n(t/n))}{n}
=\Gamma_j(t):=p^2(1-p)^{j-2}\bigl[2-(j+1)p\bigr]\bigl[(1-p)-t^2p\bigr].
\]

For \(j=1\), cancel the common factor before evaluation: \(\Gamma_1(t)=2p^2[(1-p)-t^2p]\). The factor \((1-p)-t^2p\) is strictly positive for every \(t>0\). Thus isolated-vertex count has positive limiting covariance density with total components for all positive scales, while for every \(j\ge2\) the limiting covariance density changes sign **exactly once**, from negative to positive, at the explicitly ordered scale

\[
t_j=\log\bigl((j+1)/2\bigr).
\]

The sign statements concern the limiting density. At a fixed scale away from the critical value, the corresponding finite-sample covariance has that sign for all sufficiently large \(n\); no uniqueness of finite-sample zeros is asserted.

A second exact result is the threshold-independent conditional regression

\[
\mathbb E[C_{n,j}(r)\mid X=k]=
\frac{k(k-1)(n-k)_{\underline{j-1}}}{(n-1)_{\underline j}},\qquad k=0,\ldots,n,
\]

where \(X\) is the number of long circular spacings and \((m)_{\underline h}=m(m-1)\cdots(m-h+1)\). This regression is unimodal in the number of long spacings when \(j\ge2\), with the increasing/decreasing comparison governed by \(2n-(j+1)k-(j-1)\), whereas for \(j=1\) it is nondecreasing.

## Assumptions and scope

There are \(n\ge j+2\ge3\) independent points uniformly distributed by arc length on a circle of circumference one. Join two distinct points when their shorter circular arc length is at most \(r\), where \(0<r<1/2\). The almost-sure absence of ties makes weak versus strict distance inequalities immaterial. The asymptotic theorem keeps \(j\ge1\) and \(t>0\) fixed, takes \(r=t/n\) for sufficiently large \(n\), and is uniform for \(t\) in compact subsets of \((0,\infty)\) at each fixed \(j\). No assumption of independent circular gaps is made.

Order the sampled points cyclically and write their successive normalized gaps as \(S_1,\ldots,S_n\). These spacings have the exchangeable \(\operatorname{Dirichlet}(1,\ldots,1)\) law. Put \(B_i=\mathbf1\{S_i>r\}\) and \(X=\sum_iB_i\), with cyclic indices.

## Proof

**1. Components from long gaps.** If at least two gaps exceed \(r\), no geodesic edge can cross either one: either of the two circular routes between points on opposite sides of a separating gap traverses a gap longer than \(r\). Each string of consecutive short gaps connects its own vertices, and distinct strings are disconnected. If at most one gap is long, all other consecutive edges connect a spanning path, so the graph is connected. Therefore

\[
K_n(r)=\max(1,X),\qquad
C_{n,j}(r)=\sum_{i=1}^n B_iB_{i+j}\prod_{h=1}^{j-1}(1-B_{i+h}),\quad 1\le j\le n-2.
\]

For any specified \(h\) distinct gaps, the Dirichlet simplex-translation identity gives

\[
q_{h,n}(r):=\Pr(S_{i_1}>r,\ldots,S_{i_h}>r)=(1-hr)_+^{n-1},\qquad q_{0,n}=1.
\]

**2. Conditional regression.** Given \(X=k\), the binary indicator vector is uniform on all cyclic zero–one words with exactly \(k\) ones, by exchangeability. The probability of the pattern with two specified endpoint ones and \(j-1\) specified intervening zeros is

\[
\frac{(k)_{\underline2}(n-k)_{\underline{j-1}}}{(n)_{\underline{j+1}}}.
\]

Summing over \(n\) cyclic starting positions proves the stated regression. For positive adjacent values, the ratio of the regression at \(k+1\) to the one at \(k\) differs from one with the sign of \(2n-(j+1)k-(j-1)\). This proves the stated unimodal behavior.

**3. Exact finite-sample covariance.** For \(1\le j\le n-2\), set

\[
a_j=\sum_{\ell=0}^{j-1}(-1)^\ell\binom{j-1}{\ell}q_{\ell+2,n}(r),\qquad
b_j=\sum_{\ell=0}^{j-1}(-1)^\ell\binom{j-1}{\ell}q_{\ell+3,n}(r).
\]

Inclusion–exclusion over the required short gaps gives \(\mathbb E C_{n,j}=na_j\). Multiplying each pattern indicator by \(X\), the two mandatory long gaps contribute \(2a_j\), the \(j-1\) mandatory short gaps contribute zero, and the remaining \(n-j-1\) gaps each contribute \(b_j\). Hence

\[
\mathbb E[C_{n,j}X]=n\bigl[2a_j+(n-j-1)b_j\bigr],
\quad \mathbb E X=nq_{1,n}.
\]

The probability of no long gap is

\[
P_{0,n}=\sum_{h=0}^n(-1)^h\binom nh q_{h,n}.
\]

Since \(K_n=X+\mathbf1\{X=0\}\), and \(C_{n,j}\mathbf1\{X=0\}=0\), the **exact all-radius formula** is

\[
\operatorname{Cov}(C_{n,j},K_n)
=n\bigl[2a_j+(n-j-1)b_j-nq_{1,n}a_j-a_jP_{0,n}\bigr].
\]

**4. Thermodynamic covariance density.** For each fixed integer \(h\ge0\), with \(r=t/n\), \(p=e^{-t}\), and fixed \(t>0\),

\[
q_{h,n}(t/n)=p^h\left[1+\frac{ht-h^2t^2/2}{n}+O(n^{-2})\right].
\]

For each fixed \(h\), subtracting the product of single-gap probabilities gives

\[
n\bigl(q_{h+1,n}-q_{1,n}q_{h,n}\bigr)\longrightarrow-h t^2p^{h+1}.
\]

The exact covariance with \(X\), divided by \(n\), can be rearranged as

\[
2a_j-(j+1)b_j+n\bigl(b_j-q_{1,n}a_j\bigr).
\]

Using the finite binomial sums for \(a_j,b_j\) and the preceding expansions yields

\[
\Gamma_j(t)=p^2(1-p)^{j-2}\bigl[2-(j+1)p\bigr]\bigl[(1-p)-t^2p\bigr].
\]

To replace \(X\) with \(K_n\), note that

\[
\frac{\operatorname{Var}(X)}n\longrightarrow p(1-p)-t^2p^2.
\]

Since \(\mathbb EX/n\to p>0\), Chebyshev's inequality gives \(P_{0,n}=\Pr(X=0)=O(n^{-1})\), hence \(a_jP_{0,n}\to0\). This proves the covariance limit, including the circular connected-graph correction.

**5. Sign and uniqueness in the limit.** For every \(t>0\),

\[
e^t-1-t^2>0:
\]

indeed its derivative is \(e^t-2t>0\), since \(e^t/t\ge e>2\) for \(t>0\), and its value at zero is zero. Thus \((1-p)-t^2p>0\). For \(j\ge2\), all other factors except \(2-(j+1)e^{-t}\) are positive. That factor increases strictly from \(1-j<0\) to \(2>0\), crossing zero exactly at \(t_j=\log((j+1)/2)\). For \(j=1\), the cancellation yields a strictly positive expression. These observations complete the proof.

## Verification

A standalone standard-library script, `verify.py`, provides 12,124 independent finite checks: 416 exact conditional-combinatorial identities, 540 exact rational mixed-moment checks using a separately enumerated gap-exceedance law, 10,944 finite periodic-point configurations compared with direct geodesic graph breadth-first search, and 224 numerical limiting-formula comparisons/threshold checks. It prints `PASS; verification groups (416, 540, 10944, 224) total 12124` when executed by `python verify.py`.

The computational tests are finite corroboration. The proof of the unrestricted domain and limiting sign theorem is the symbolic Dirichlet/gap-indicator argument above, not the numerical experiments or timeout-based inference.

## Relationship to prior work

Decreusefond and Ferraz [1, §4.2] determine the distribution of total cluster count on a Poisson-populated circle. This differs both in sampling model (random Poisson point total rather than fixed \(n\)) and in observable (total clusters alone rather than covariance against the size-\(j\) count). Schulte and Yukich [2, §3.2(a), Theorem 3.5] treat joint normal approximation for vectors of fixed-size component counts in Poisson-input random geometric graphs. Their general convergence theorem does not give the evaluated fixed-sample circle covariance-density function or its ordered logarithmic sign thresholds. Penrose [3] is a broad foundational component-count reference, and Zhao–Yağan–Gligor [4] concerns a different one-dimensional connectivity/isolated-point boundary regime. These are implication comparisons, not claims that generic covariance methods are inapplicable.

## Limitations

The sign switch is proved **once for the limiting covariance density** at fixed \(j\); no assertion about the number of zeros for a fixed \(n\), nor about joint growth of \(j\) with \(n\), is made. At the critical thermodynamic radius the normalized covariance tends to zero without determining its finite-sample sign. Earlier generic random-geometric graph moment formulae might imply the evaluated density after additional derivation. A complete external historical-priority audit is not part of this mathematical proof; the accessible abstract of Penrose [3] does not support a whole-book exclusion claim.

## References

[1] L. Decreusefond and E. Ferraz, *On the One Dimensional Poisson Random Geometric Graph*, arXiv:1008.5140 (2010-08-30), *Journal of Probability and Statistics* (2011), DOI 10.1155/2011/350382. Full primary article, §4.2.

[2] M. Schulte and J. E. Yukich, *Rates of multivariate normal approximation for statistics in geometric probability*, *Annals of Applied Probability* (2023), DOI 10.1214/22-AAP1822, §3.2(a), Theorem 3.5.

[3] M. Penrose, *Random Geometric Graphs*, Oxford University Press (2003), Chapter 13 (accessible chapter synopsis).

[4] J. Zhao, O. Yağan and V. Gligor, *A curious gap in one-dimensional geometric random graphs between connectivity and absence of isolated node*, arXiv:1502.00404 (2015), abstract.
