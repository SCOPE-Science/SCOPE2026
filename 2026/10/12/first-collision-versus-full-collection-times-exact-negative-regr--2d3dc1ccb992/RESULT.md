# First-collision versus full-collection times: exact negative regression and a Rayleigh covariance scale

## Finding
Let \(X_1,X_2,\ldots\) be independent uniform draws from \(\{1,\ldots,n\}\), where \(n\ge2\). Write \(B_n\) for the index of the first draw that repeats a previously observed type, and \(T_n\) for the first index at which all \(n\) types have appeared. These are measured on **the same draw sequence**.

Define \(S_{n,j}=\prod_{i=0}^{j-1}(1-i/n)\) for \(0\le j\le n\), with \(S_{n,0}=1\). The law of \(B_n\) and the conditional probability-generating functions of \(T_n\) are
\[
\begin{aligned}
 \mathbb P(B_n=b)&=S_{n,b-1}\frac{b-1}{n},&&2\le b\le n,\\
 \mathbb P(B_n=n+1)&=S_{n,n},\\
 \mathbb E[z^{T_n}\mid B_n=b]&=z^b\prod_{k=b-1}^{n-1}\frac{(n-k)z}{n-kz},&&2\le b\le n,\\
 \mathbb E[z^{T_n}\mid B_n=n+1]&=z^n.
\end{aligned}
\]
These identities determine the complete finite joint law of \((B_n,T_n)\); the empty product is one. For \(0\le u,z\le1\), the joint probability-generating function is the sum of \(u^b\mathbb P(B_n=b)\mathbb E[z^{T_n}\mid B_n=b]\) over \(2\le b\le n+1\).

The conditional distributions \(\mathcal L(T_n\mid B_n=b)\) are **strictly decreasing in first-order stochastic order** as \(b\) increases from \(2\) to \(n+1\). Their conditional means are
\[
 m_n(b)=\mathbb E[T_n\mid B_n=b]=
 \begin{cases}
 b+nH_{n-b+1},&2\le b\le n,\\
 n,&b=n+1,
 \end{cases}
\]
where \(H_j=\sum_{k=1}^{j}1/k\). In particular, for every \(n\ge2\),
\[
\boxed{\operatorname{Cov}(B_n,T_n)
=-\sum_{j=2}^{n} S_{n,j}\sum_{k=1}^{j-1}\frac{k}{n-k}<0.}
\]
Writing \(R\) for a Rayleigh random variable with \(\mathbb P(R>x)=e^{-x^2/2}\) for \(x\ge0\), one additionally has
\[
\begin{aligned}
 \left(\frac{B_n}{\sqrt n},\ m_n(B_n)-nH_n\right)&\ \xrightarrow{d}\ \left(R,1-\frac{R^2}{2}\right),\\
 \lim_{n\to\infty}\frac{\operatorname{Cov}(B_n,T_n)}{\sqrt n}&=-\sqrt{\frac\pi8},\\
 \lim_{n\to\infty} n\operatorname{Corr}(B_n,T_n)&=-\sqrt{\frac{3}{2\pi(4-\pi)}}.
\end{aligned}
\]
The regression correction converges in \(L^2\) to the indicated function of \(B_n/\sqrt n\): specifically \(m_n(B_n)-nH_n-[1-B_n^2/(2n)]\to0\) in \(L^2\).

## Assumptions and scope
All statements require uniformly distributed independent draws, finite integer \(n\ge2\), and first repetition/complete collection on one common infinite sample. The geometric law below counts the successful draw, so \(\mathbb P(G=k)=p(1-p)^{k-1}\) for \(k\ge1\). The convention \(B_n=n+1\) means the first \(n\) draws are pairwise different: then the sample is already complete at time \(n\), **before** its first repetition. The limiting results send \(n\to\infty\) through positive integers, without nonuniform weights or reset events.

## Proof
**Joint law and stochastic ordering.** Before its first repeated draw, the first \(b-1\) samples are all distinct. Thus the first-collision probabilities above follow by elementary sequential multiplication, including the separate event \(B_n=n+1\). For \(2\le b\le n\), exactly \(b-1\) types have been observed at time \(b\); the subsequent number of draws required to grow from \(k\) to \(k+1\) distinct types is independent geometric \(G_k\) with success probability \((n-k)/n\). Hence
\[
 T_n\mid(B_n=b)\ \overset d=\ b+\sum_{k=b-1}^{n-1}G_k.
\]
The probability-generating formula follows by multiplying \(\mathbb E[z^{G_k}]=(n-k)z/(n-kz)\). At \(b=n+1\) the coupon collection finishes at time \(n\), giving the exceptional \(z^n\) term. Use one common set of independent \(G_k\)'s for all conditional laws. For \(2\le b<n\), the coupled difference between successive conditional completion times is \(G_{b-1}-1\ge0\), and for \(b=n\) it is \(G_{n-1}\ge1\). Each comparison is strict with positive probability. Taking expectations yields the displayed \(m_n(b)\), and any increasing integrable function of \(T_n\) has nonincreasing conditional expectation given \(B_n=b\).

**Exact covariance.** The first success always takes one draw. Express the independent collection waiting times as \(T_n=1+\sum_{k=1}^{n-1}G_k\). The number of distinct coupons seen before a duplicate is the length of the initial run of unit waiting times, so
\[
 B_n=1+\sum_{j=1}^{n}\prod_{k=1}^{j-1}\mathbf{1}_{\{G_k=1\}}.
\]
For \(1\le k<j\), independence of the waiting times gives
\[
 \mathbb E\!\left[G_k\prod_{i<j}\mathbf{1}_{\{G_i=1\}}\right]=S_{n,j},\qquad
 \mathbb E[G_k]\,\mathbb P(G_i=1\text{ for all }i<j)=\frac{n}{n-k}S_{n,j}.
\]
For \(k\ge j\), the covariance vanishes by independence. Summing the negative differences proves the stated finite covariance identity and strict negativity. Here \(S_{n,j}\) is the probability that the first \(j\) samples are distinct. The strict conditional stochastic ordering independently implies \(\operatorname{Cov}(B_n,\phi(T_n))\le0\) for any increasing \(\phi\) with the requisite moments.

**Asymptotic regression profile.** The birthday survival law \(\mathbb P(B_n>j)=S_{n,j}\) for \(0\le j\le n\) and expansion of its logarithm imply \(B_n/\sqrt n\Rightarrow R\). The bound \(S_{n,j}\le\exp(-j(j-1)/(2n))\) yields convergence of every fixed positive moment. For \(2\le b\le n\), subtracting \(nH_n\) from the conditional mean gives the exact identity
\[
 m_n(b)-nH_n=1-\sum_{j=0}^{b-2}\frac{j}{n-j}.
\]
For \(b\le n/2\), the difference between this expression and \(1-b^2/(2n)\) is at most \(C(b/n+b^3/n^2)\). The moment bound makes this difference vanish in \(L^2\) at \(b=B_n\). For \(B_n>n/2\), the probability is exponentially small, while \(|m_n(B_n)-nH_n|=O(n\log n)\); this also covers the exceptional \(B_n=n+1\). We get the \(L^2\) regression approximation and joint weak limit.

By the tower property,
\[
 \frac{\operatorname{Cov}(B_n,T_n)}{\sqrt n}=
 \operatorname{Cov}\left(\frac{B_n}{\sqrt n},m_n(B_n)-nH_n\right)
 \longrightarrow-\tfrac12\operatorname{Cov}(R,R^2).
\]
The Rayleigh moments \(\mathbb ER=\sqrt{\pi/2}\), \(\mathbb ER^2=2\), and \(\mathbb ER^3=3\sqrt{\pi/2}\) give the constant \(-\sqrt{\pi/8}\). Also \(\operatorname{Var}(B_n)/n\to2-\pi/2\). Independence of the geometric waiting times yields
\[
 \operatorname{Var}(T_n)=n^2\sum_{j=1}^{n}\frac1{j^2}-nH_n,
\]
so \(\operatorname{Var}(T_n)/n^2\to\pi^2/6\). Division by the two standard deviations proves the correlation limit.

## Verification
Run `python3 verify.py` with Python 3.9 or newer; no external libraries are required. The program exhaustively enumerates \(\sum_{n=2}^7n^n=873611\) full length-\(n\) prefixes. For each prefix it identifies the first collision, uses a separately computed missing-coupon conditional expectation for the remaining cover time, and compares exact rational joint moments and conditional means with the theorem. There are 60 comparisons across six sizes. It independently checks the exact covariance series, prints finite exact values including \(-1/2\) at \(n=2\), and numerically tracks the scaled covariance through \(n=40000\). Its terminal success marker is `VERIFY_OK`. Enumeration is finite evidence only; the general claims are proved above.

## Relationship to prior work
Anceaume, Busnel and Sericola establish distributions and moments for the time to collect a prescribed number of distinct types, for more general weights and possible null coupons. This encompasses the marginal completion-time distribution, not the law of the first repeated type together with completion on a common draw sequence. The present conditional stochastic ordering and mixed covariance therefore do not follow from their stated marginal formula alone. Myers and Wilf study several coupon-collector variants and completion-time singleton counts. Flajolet, Gardy and Thimonier investigate birthday and collection times with a broad language-enumeration approach; their inspected main sections develop these as waiting-time constructions, and may allow indirect derivations of the finite joint identity. Holst's classical unified treatment of urn waiting problems could not be inspected in full. The priority assessment concerns the explicit negative conditional order and covariance asymptotics, not either classical marginal distribution or the elementary geometric decomposition in isolation.

## Limitations
The claim is restricted to iid uniform types. No assertion is made about analogous covariance signs under heterogeneous weights, coupon resets, or dependent sampling. The statement does not claim a new general coupon-collector framework, a multivariate limit of arbitrary occupancy statistics, or independent historical certification. Holst's 1986 unified urn paper remains an unresolved full-text priority risk; broader generating-function methods may implicitly produce some identities. Empirical verification through order seven is not a proof for all orders. The asymptotic correlation coefficient uses ordinary Pearson correlation, not asymptotic independence of the unscaled times.

## References
1. Emmanuelle Anceaume, Yann Busnel, Bruno Sericola, *New Results on a Generalized Coupon Collector Problem Using Markov Chains*, arXiv:1402.5245v1, 21 February 2014; *Journal of Applied Probability* 52 (2015), 405–418, DOI: 10.1239/jap/1437658606. Primary MSC 60C05.
2. Amy N. Myers and Herbert S. Wilf, *Some New Aspects of the Coupon Collector's Problem*, arXiv:math/0304229v1, 16 April 2003; *SIAM Journal on Discrete Mathematics* 17 (2003), 1–17.
3. Philippe Flajolet, Danièle Gardy, Loÿs Thimonier, *Birthday Paradox, Coupon Collectors, Caching Algorithms and Self-Organizing Search*, INRIA Research Report RR-0720 (1987), *Discrete Applied Mathematics* 39 (1992), 207–229.
4. Lars Holst, *On Birthday, Collectors', Occupancy and Other Classical Urn Problems*, *International Statistical Review* 54 (1986), 15–27, DOI: 10.2307/1403255. Full text not inspected.
5. Andrii Ilienko, *Limit Theorems in the Extended Coupon Collector's Problem*, *Modern Stochastics: Theory and Applications* (2026), DOI: 10.15559/26-VMSTA306; concerns completion times for different collections.
