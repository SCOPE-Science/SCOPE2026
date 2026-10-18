# Exact joint crossing and simple-chord laws for uniform chord diagrams

## Finding

Let \(M_n\) be a uniformly chosen perfect matching of \(2n\) cyclically ordered labeled endpoints, with \(n\ge2\). Let \(X_n\) count crossing pairs of matching chords and \(S_n\) count chords whose endpoints are cyclically consecutive, including the pair of endpoints \(\{2n,1\}\). Put \(Q_m(u)=\mathbb E[u^{X_m}]\), with \(Q_0=Q_1=1\), and define, for \(0\le k\le n\),

\[
a_{n,0}=1,\qquad a_{n,k}=\frac{k!\,\dfrac{2n}{2n-k}\binom{2n-k}{k}}{\prod_{j=0}^{k-1}(2n-2j-1)}\quad(k\ge1).
\]

**Theorem.** For every \(n\ge2\), \(0\le k\le n\), and any complex-valued function \(f\) on the possible crossing counts,

\[
\mathbb E[(S_n)_k f(X_n)] = a_{n,k}\,\mathbb E[f(X_{n-k})],
\qquad (s)_k=s(s-1)\cdots(s-k+1).
\]

Consequently, the full bivariate generating polynomial obeys

\[
\boxed{\ \mathbb E[u^{X_n}z^{S_n}]
=\sum_{k=0}^{n}\frac{a_{n,k}}{k!}(z-1)^k Q_{n-k}(u).\ }
\]

Writing \(\mu_n=n(n-1)/6\) and \(\sigma_n^2=n(n-1)(n+3)/45\), one has the exact finite-size formulas

\[
\mathbb E S_n=\frac{2n}{2n-1},\qquad
\operatorname{Var}(S_n)=\frac{4n(n-1)}{(2n-1)^2},\qquad
\operatorname{Cov}(X_n,S_n)=-\frac{2n(n-1)}{3(2n-1)},
\]
\[
\boxed{\ \operatorname{Corr}(X_n,S_n)=-\sqrt{\frac5{n+3}}.\ }
\]

In particular, although crossings and simple chords are negatively correlated at every finite size, they become **asymptotically independent** in the joint Gaussian–Poisson limit:

\[
\boxed{\ \left(\frac{X_n-\mu_n}{\sigma_n},S_n\right)
\xrightarrow{\ d\ }(Z,Y),\quad Z\sim N(0,1),\quad Y\sim\operatorname{Pois}(1),\quad Z\perp Y.\ }
\]

## Assumptions and scope

All \((2n-1)!!\) perfect matchings of the labeled cyclic endpoints are equally likely. Chords cross precisely when their four distinct endpoints alternate around the circle. A simple chord joins cyclically adjacent endpoints; the wrap-around adjacency is included. The parameter \(k\) ranges over integers from zero to \(n\). The factorial identity is exact and does not assume that \(f\) is a polynomial; its domain is finite. The joint weak limit is asserted only as \(n\to\infty\). Auxiliary random variables \(X_0\) and \(X_1\) are defined deterministically as zero. We never define a simple-chord count at \(n=1\), where the two-vertex cyclic adjacency would be degenerate.

## Proof

**1. Forced disjoint boundary chords.** Let \(\mathcal B_n\) denote the \(2n\) distinct edges in the labeled boundary cycle. Each \(e\in\mathcal B_n\) is an eligible simple chord. Expanding \((S_n)_k\) sums over ordered, pairwise vertex-disjoint \(k\)-tuples of boundary edges. The number of unordered \(k\)-edge matchings in the cycle \(C_{2n}\) equals

\[
 b_{n,k}=\frac{2n}{2n-k}\binom{2n-k}{k}\quad(0\le k\le n).
\]

For \(k=0\), this equals one. To establish the formula for positive \(k\), encode chosen boundary edges by occupied positions in a circular binary string of length \(2n\) having \(k\) ones, with no adjacent ones. Mark one selected position, cut immediately before it and record the \(k\) positive cyclic gaps; the gaps sum to \(2n\) and have size at least two. Their count is \(\binom{2n-k-1}{k-1}\). The first chosen position has \(2n\) possibilities while every subset is counted \(k\) times. Thus \(b_{n,k}=(2n/k)\binom{2n-k-1}{k-1}=\frac{2n}{2n-k}\binom{2n-k}{k}\).

Each fixed disjoint \(k\)-tuple occurs in the random matching with probability

\[
 d_{n,k}^{-1},\qquad d_{n,k}=\prod_{j=0}^{k-1}(2n-2j-1),
\]

because there remain exactly \((2n-2k-1)!!\) perfect matchings of the unused vertices. An individual boundary chord has no crossing with any chord. Deleting all \(k\) forced short chords leaves \(2(n-k)\) vertices whose induced cyclic order is the old cyclic order with gaps removed; a chord crossing is preserved by this deletion, including wrap-around. Conditional on the selected chords, the remaining matching is uniform. It therefore has crossing count distributed as \(X_{n-k}\). Summing the \(k! b_{n,k}\) ordered tuples proves the factorial identity, since \(a_{n,k}=k!b_{n,k}/d_{n,k}\). Expanding \(z^{S_n}=(1+(z-1))^{S_n}\) gives the bivariate polynomial identity without approximation.

**2. Covariance and correlation.** Counting boundary edges gives \(a_{n,1}=2n/(2n-1)\). There are \(2n(2n-3)\) ordered pairs of vertex-disjoint boundary edges, so \(a_{n,2}=2n/(2n-1)\) as well (valid at \(n=2\)). The cases \(k=1,2\), with \(f\equiv1\), give the asserted mean and variance of \(S_n\). For \(f(x)=x\) and \(k=1\), the identity gives \(\mathbb E[X_nS_n]=a_{n,1}\mu_{n-1}\). Since \(\mu_{n-1}-\mu_n=-(n-1)/3\), the covariance follows. The exact crossing mean and variance quoted in the statement are known and also independently checked for finite sizes below; substituting them yields the asserted correlation.

**3. Joint limit.** Write \(T_n=(X_n-\mu_n)/\sigma_n\). The established central limit theorem for \(X_n\) gives \(T_n\Rightarrow Z\sim N(0,1)\). For any fixed integer \(k\ge0\), we have \(a_{n,k}\to1\), \((\mu_{n-k}-\mu_n)/\sigma_n\to0\), and \(\sigma_{n-k}/\sigma_n\to1\). Applying the factorial identity with \(f(x)=\exp(it(x-\mu_n)/\sigma_n)\) therefore gives, for every real \(t\),

\[
\mathbb E[(S_n)_k e^{itT_n}]\longrightarrow e^{-t^2/2}.
\]

To justify summing these limits, observe that \(a_{n,k}=\mathbb E(S_n)_k\le2^k\). Indeed, after forcing an ordered \(k\)-tuple of disjoint boundary chords, at most \(2(n-k)\) edges of the original boundary cycle remain eligible on the \(2(n-k)\) residual vertices. Each is present in their uniform matching with probability \(1/(2(n-k)-1)\), so the expected number of eligible additions is at most \(2(n-k)/(2(n-k)-1)\le2\), for \(k<n\); this shows \(a_{n,k+1}\le2a_{n,k}\) and starts at \(a_{n,0}=1\).

For \(0\le z\le1\), Fourier–factorial expansion and this bound give

\[
\mathbb E[e^{itT_n}z^{S_n}]
=\sum_{k=0}^{n}\frac{(z-1)^k}{k!}\,\mathbb E[(S_n)_k e^{itT_n}]
\longrightarrow\exp(-t^2/2)\exp(z-1).
\]

Domination is by \(\sum_{k\ge0}2^k|z-1|^k/k!<\infty\). The limiting expression is precisely the joint Fourier/probability-generating transform of an independent standard normal and mean-one Poisson pair. Tightness follows from the marginal normal limit and \(\mathbb E S_n\le2\). Uniqueness of the transform proves joint weak convergence and independence.

## Verification

The attached standalone `verify.py` uses only the Python standard library. Execute `python verify.py`. It enumerates all labeled perfect matchings through \(n=6\) (including \(10{,}395\) matchings at \(n=6\)), calculates both statistics independently, and checks exact rational moments, all mixed factorial distributions at every \(0\le k\le n\), and the exact matching-count formula for disjoint boundary edges. These finite computations are corroboration and are not substituted for the general proof.

## Relationship to prior work

Paguyo [1], building on Flajolet–Noy [3], establishes a Gaussian limit and exact crossing mean and variance, and separately a Poisson approximation for simple chords. The main results and proofs in [1] do not assert their joint asymptotic independence or the finite-size mixed factorial transform. Acan [2] studies related simple-chord Poisson asymptotics and chord length counts. Cameron–Killpatrick [4] and Young [5] enumerate **linear** short chords \(\{i,i+1\}\), not the present wrap-around-inclusive circular statistic; their results concern the short-chord marginal, rather than its joint law with crossing count. The forced-boundary-chord deletion argument is a direct combinatorial refinement using the established model and classical crossing limit; it does not claim a new proof of the known marginal central limit theorem.

## Limitations

The joint convergence has no quantitative rate asserted here. Its proof invokes the established crossing-number central limit theorem, while proving the coupling identity and Gaussian–Poisson independence directly. The exact formula applies to uniform perfect matchings on labeled cyclic endpoints, not arbitrary nonuniform matchings or linear short-chord definitions. The originality comparison is based on the specifically inspected mathematical literature and searches; an equivalent older joint marked Touchard–Riordan identity might exist and independent historical-priority verification remains outstanding. No independent scientific audit has been performed.

## References

[1] J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, first publicly posted 2021-04-02; latest preprint version 2023-01-11. https://arxiv.org/abs/2104.01134

[2] H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489; Discrete Mathematics (2017). https://arxiv.org/abs/1501.01489

[3] P. Flajolet and M. Noy, *Analytic combinatorics of chord diagrams*, Formal Power Series and Algebraic Combinatorics (2000). https://algo.inria.fr/flajolet/Publications/FlNo00.pdf

[4] N. T. Cameron and K. Killpatrick, *Statistics on Linear Chord Diagrams*, Discrete Mathematics & Theoretical Computer Science 21:2 (2019). https://dmtcs.episciences.org/6038/pdf

[5] D. Young, *Linear k-Chord Diagrams*, arXiv:2004.06921 (2020). https://arxiv.org/abs/2004.06921
