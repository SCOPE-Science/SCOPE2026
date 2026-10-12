# A Poisson second-difference law for component–indegree covariance in random mappings

## Finding

For a uniformly random self-map \(T_n:[n]\to[n]\), let \(C_n\) be the number of weakly connected components of its directed functional graph, and let \(D_{n,r}\) be the number of vertices of in-degree \(r\), for \(0\le r\le n\). Define the degree-count generating polynomial \(G_n(z)=\sum_{r=0}^{n}D_{n,r}z^r\). For every integer \(n\ge2\) and every complex \(z\), the covariance polynomial has the exact finite formula

\[
Q_n(z):=\operatorname{Cov}(C_n,G_n(z))
=n\sum_{k=1}^{n}\frac{a_{n,k}}{k}
\left(1+\frac{z-1}{n}\right)^{n-k}
\left[1+\frac{k(z-1)}n-\left(1+\frac{z-1}{n}\right)^k\right],
\qquad a_{n,k}:=\frac{(n)_k}{n^k}.
\]

As \(n\to\infty\), these polynomials converge uniformly on each compact subset of the complex plane:

\[
Q_n(z)\longrightarrow -\tfrac12(z-1)^2 e^{z-1}.
\]

Consequently, for every fixed integer \(r\ge0\),

\[
\lim_{n\to\infty}\operatorname{Cov}(C_n,D_{n,r})
=\frac{e^{-1}}{2r!}(-r^2+3r-1).
\]

The limit is positive precisely for \(r=1,2\), and negative for \(r=0\) and every \(r\ge3\). Therefore the corresponding signs hold for all sufficiently large \(n\) for each *fixed* \(r\), without any assertion of a threshold uniform in \(r\). This is one joint covariance-profile theorem; isolated special cases are not claimed as separate discoveries.

## Assumptions and scope

The \(n\) images \(T_n(1),\ldots,T_n(n)\) are independent and each uniform on \([n]=\{1,\ldots,n\}\). A directed edge points from each vertex to its image, including loops. In a finite functional digraph every weak component contains exactly one directed cycle, so \(C_n\) also counts its directed cycles (a fixed point is a cycle of length one). The in-degree includes loop edges. The symbol \((n)_k\) denotes the falling factorial \(n(n-1)\cdots(n-k+1)\). Covariances of complex polynomials are coefficientwise, namely \(\operatorname{Cov}(C_n,G_n(z))=\mathbb E[C_nG_n(z)]-\mathbb E[C_n]\mathbb E[G_n(z)]\); no conjugation is used. No limit with \(r\) increasing with \(n\) is asserted.

## Proof

**1. A one-cycle Palm calculation.** Let \(I_\gamma\) indicate the presence of one prescribed directed simple cycle \(\gamma\) on \(k\) distinct labeled vertices. Its probability is \(n^{-k}\), and the number of possible directed \(k\)-cycles is \((n)_k/k\). Thus \(C_n=\sum_\gamma I_\gamma\) and \(\mathbb E C_n=\sum_{k=1}^n a_{n,k}/k\). With \(u=(z-1)/n\), independence of all outgoing images gives

\[
\mathbb E G_n(z)=n(1+u)^n.
\]

Conditionally on \(I_\gamma=1\), the \(k\) vertices on the cycle each already receive one incoming edge, and the remaining \(n-k\) freely chosen outgoing images contribute an independent binomial \(\operatorname{Bin}(n-k,1/n)\) to the in-degree of each specified vertex. All other vertices have binomial \(\operatorname{Bin}(n-k,1/n)\) in-degree. Their *marginal* binomial generating functions suffice; independence among different vertices' in-degrees is not claimed. Hence

\[
\mathbb E[G_n(z)\mid I_\gamma=1]
=\bigl(kz+n-k\bigr)(1+u)^{n-k}
=n(1+ku)(1+u)^{n-k}.
\]

Linearity of covariance across \(I_\gamma\), followed by summation over all labeled cycles, yields the exact displayed formula. In particular, the bracket \(1+ku-(1+u)^k\) is divisible by \(u^2\), proving the exact identities \(Q_n(1)=Q_n'(1)=0\). These also follow from the deterministic conservation laws \(\sum_r D_{n,r}=n\) and \(\sum_r rD_{n,r}=n\).

**2. Gaussian cycle-length cutoff.** For \(1\le k\le n\),

\[
0<a_{n,k}=\prod_{j=0}^{k-1}\left(1-\frac jn\right)
\le \exp\!\left(-\frac{k(k-1)}{2n}\right).
\]

For every fixed \(t>0\), \(a_{n,\lfloor t\sqrt n\rfloor}\to e^{-t^2/2}\). Consequently, Gaussian domination and a Riemann-sum limit give

\[
\frac1n\sum_{k=1}^n a_{n,k}(k-1)
\longrightarrow\int_0^\infty t e^{-t^2/2}\,dt=1,
\qquad \sum_{k=1}^n a_{n,k}k^2=O(n^{3/2}).
\]

The second bound follows, for example, by comparing the Gaussian tail with a corresponding integral after \(k/\sqrt n\) rescaling. No simulated cutoff is used in this argument.

**3. A uniform analytic expansion.** Fix any compact set of complex \(z\)-values. Writing \(w=z-1\), the binomial theorem supplies, uniformly for \(1\le k\le n\),

\[
1+\frac{kw}{n}-\left(1+\frac wn\right)^k
=-\binom{k}{2}\frac{w^2}{n^2}
+O\!\left(\frac{k^3}{n^3}\right),
\]

where the implied constant depends only on the compact set. The factors \((1+w/n)^{n-k}\) are uniformly bounded. After multiplication by \(n a_{n,k}/k\) and summation, the total remainder is at most a compact-dependent constant times \(n^{-2}\sum_k a_{n,k}k^2=O(n^{-1/2})\). Therefore

\[
Q_n(z)=-\frac{w^2}{2n}\sum_{k=1}^n
 a_{n,k}(k-1)\left(1+\frac wn\right)^{n-k}+O(n^{-1/2}).
\]

For \(k=O(\sqrt n)\), the last exponential factor converges uniformly to \(e^w\). The Gaussian bound on \(a_{n,k}\), with the preceding Riemann sum, controls the contribution of larger \(k\). Thus \(Q_n(z)\to -\tfrac12w^2e^w\) uniformly on every compact set.

**4. Coefficient limit and its signs.** Because the convergence is locally uniform for entire polynomials, Cauchy's coefficient formula permits fixed-degree coefficient extraction:

\[
[z^r]Q_n(z)\longrightarrow
-\tfrac12[z^r](z-1)^2e^{z-1}
=\frac{e^{-1}}{2r!}(-r^2+3r-1).
\]

The two real zeros of the final numerator are \((3-\sqrt5)/2\) and \((3+\sqrt5)/2\). Its integer sign is therefore positive only at \(r=1,2\), completing the proof.

## Verification

The companion standalone script `verification.py` independently enumerates every one of the \(n^n\) self-maps for \(2\le n\le7\) (873,611 maps total). It computes component counts directly from visited trajectories and tabulates in-degree counts, without using the cycle-Palm formula in the enumeration stage. It compares each exact rational covariance with the coefficient formula obtained from the analytic identity: all 33 degree-class comparisons passed. It additionally verifies the two deterministic conservation identities at each tested size (12 checks) and evaluates numerical convergence diagnostics for \(n=100,500,2000\). Run from the directory containing the script with `python3 verification.py`. The numerical diagnostics are finite corroboration only; compact-uniform convergence and all fixed-degree sign conclusions were proved above.

## Relationship to prior work

Random mapping component counts, cyclic points, and in-degree structures have substantial prior literature. Hansen and Jaworski's *A new random mapping model* (2006 preprint, subsequently *Random mappings with exchangeable in-degrees*) computes the distribution of cyclic vertices and components in exchangeable-in-degree models; their local-properties companion analyzes predecessor structure. Flajolet and Odlyzko previously developed a broad generating-function framework for random mapping statistics, and Kupka gave exact marginal component-count moments. Hansen and Jaworski also studied structural transitions with constrained in-degrees in 2014. None of the fully inspected relevant treatments explicitly states the joint component-count/entire immediate-in-degree covariance polynomial or the compact-uniform Poisson second-difference limit here; these conclusions are *not* claimed to be inaccessible to their methods. The in-degree-zero negative covariance is already obtainable indirectly from earlier cyclic-core/deletion relations and is included only as a member of the full profile; neither that special-case sign nor marginal component formulas alone are a novelty claim.

## Limitations

The theorem concerns independent uniform mappings only and gives asymptotic signs for each fixed degree class, not an all-size sign theorem or a uniform-in-degree estimate. It establishes covariance limits, not joint convergence in distribution, conditional independence, or a central limit theorem. Prior methods may imply parts of the result implicitly; in particular, the broad earlier Flajolet–Odlyzko chapter could not be fully inspected. No exhaustive historical priority claim or independent validation is made. The scientific assertion depends on the analytic derivation; exact bounded enumeration does not prove its asymptotic statements.

## References

1. J. C. Hansen and J. Jaworski, *A new random mapping model*, arXiv:math/0603529v1 (first public preprint, 22 March 2006); revised journal title *Random mappings with exchangeable in-degrees*, *Random Structures & Algorithms* 33 (2008), 105–126, DOI:10.1002/rsa.20187.
2. J. C. Hansen and J. Jaworski, *Local properties of random mappings with exchangeable in-degrees*, *Advances in Applied Probability* 40 (2008), 183–205, DOI:10.1239/aap/1208358892.
3. J. C. Hansen and J. Jaworski, *Structural transition in random mappings*, *Electronic Journal of Combinatorics* 21(1) (2014), P1.18, DOI:10.37236/3572.
4. P. Flajolet and A. M. Odlyzko, *Random mapping statistics*, *Advances in Cryptology—EUROCRYPT '89*, LNCS 434 (1990), 329–354, DOI:10.1007/3-540-46885-4_34.
5. J. Kupka, *The distribution and moments of the number of components of a random function*, *Journal of Applied Probability* 27 (1990), 202–207, DOI:10.2307/3214607.
6. M. Drmota and M. Soria, *Images and preimages in random mappings*, *SIAM Journal on Discrete Mathematics* 10 (1997), 246–269, DOI:10.1137/S0895480194268421.
