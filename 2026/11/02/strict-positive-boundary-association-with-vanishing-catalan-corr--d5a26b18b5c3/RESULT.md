# Strict positive boundary association with vanishing Catalan correlation in random 231-avoiding permutations

## Finding
Let \(\pi\) be uniform in \(\operatorname{Av}_n(231)\). Denote by \(X_n\) its maximal initial block of position-wise fixed points and by \(Y_n\) its maximal final block of position-wise fixed points. Their joint distribution exhibits strict positive quadrant dependence at every finite size, while the dependence is only of order \(n^{-2}\) asymptotically. More precisely, for every \(n\ge2\) and all \(0\le a,b\le n\),

\[
\Pr(X_n\ge a,Y_n\ge b)=\begin{cases}C_{n-a-b}/C_n,&a+b\le n,\\1/C_n,&a+b>n,\end{cases}
\]
where \(C_m=\binom{2m}{m}/(m+1)\) and \(C_0=1\). Each marginal tail is \(C_{n-a}/C_n\). All pairs of nontrivial upper-tail indicators have *strictly positive* covariance. Consequently, arbitrary nondecreasing transforms have nonnegative covariance, strictly positive when both transforms are strictly increasing. Yet the joint law converges to independent geometric variables with \(\Pr(G\ge a)=4^{-a}\), and

\[
\lim_{n\to\infty}n^2\operatorname{Cov}(X_n,Y_n)=\frac{8}{27}.
\]

## Assumptions and scope
A permutation avoids \(231\) if it has no indices \(i<j<k\) with \(\pi(j)>\pi(i)>\pi(k)\). The model is uniform among the \(C_n\) avoiders of length \(n\). The prefix statistic \(X_n\) is the largest integer \(a\in\{0,\ldots,n\}\) satisfying \(\pi(i)=i\) for \(1\le i\le a\). The suffix statistic \(Y_n\) is the largest \(b\) satisfying \(\pi(i)=i\) for \(n-b+1\le i\le n\). In particular both equal \(n\) for the identity permutation; this common rare atom is included in the formulas. All finite statements quantify over every integer \(n\ge2\) and every indicated admissible \(a,b\).

## Proof
**Exact tails.** The pattern \(231\) is indecomposable under the direct-sum operation: no proper initial subsequence of that three-term pattern uses precisely its smallest values. Hence the direct sum of any number of \(231\)-avoiders is another \(231\)-avoider. Requiring the first \(a\) positions to be \(1,\ldots,a\) and the last \(b\) positions to be \(n-b+1,\ldots,n\) leaves an arbitrary middle \(231\)-avoider of length \(n-a-b\), provided \(a+b\le n\). Deleting the specified fixed positions is a bijection, proving exactly \(C_{n-a-b}\) admissible permutations. When \(a+b>n\), the requirements cover every position and force the unique identity permutation. This also proves the marginal-tail identities by setting one threshold to zero.

**Strict finite dependence.** The successive Catalan ratios are
\[
r_m=\frac{C_m}{C_{m-1}}=\frac{2(2m-1)}{m+1}=4-\frac{6}{m+1},\qquad m\ge1,
\]
and are strictly increasing in \(m\). Thus \(C_m\) is strictly log-convex. For \(1\le a,b\) and \(a+b\le n\), repeated strict ratio comparison gives
\[
C_n C_{n-a-b}>C_{n-a}C_{n-b}.
\]
For \(a+b>n\), put \(u=n-a\) and \(v=n-b\), so \(u+v<n\). The standard Catalan convolution or direct injection of ordered pairs of avoiders shows \(C_uC_v\le C_{u+v}\); because \(n\ge2\) and \(u+v<n\), \(C_{u+v}<C_n\). Dividing the strict inequalities by \(C_n^2\) proves \(\operatorname{Cov}(\mathbf1_{\{X_n\ge a\}},\mathbf1_{\{Y_n\ge b\}})>0\) for *every* nonzero threshold pair. For nondecreasing \(f,g\), write \(f(x)=f(0)+\sum_{a=1}^n[f(a)-f(a-1)]\mathbf1_{\{x\ge a\}}\) and analogously for \(g\). Expanding covariance yields a nonnegative weighted sum, strictly positive if both functions are strictly increasing.

**Joint limit.** For every fixed \(a,b\ge0\), Catalan asymptotics \(C_m\sim4^m/(\sqrt\pi m^{3/2})\) imply
\[\Pr(X_n\ge a,Y_n\ge b)\longrightarrow4^{-(a+b)}.\]
These tails determine two independent integer-valued geometric variables with \(\Pr(G=k)=3/4^{k+1}\) for \(k\ge0\).

**Sharp covariance decay.** For \(a,b\ge1\), put \(p_a=C_{n-a}/C_n\) and \(\Delta_{a,b}=\Pr(X_n\ge a,Y_n\ge b)-p_ap_b\). The tail-sum identity gives
\[\operatorname{Cov}(X_n,Y_n)=\sum_{a=1}^n\sum_{b=1}^n\Delta_{a,b}.\]
When \(a+b\le n\), let \(r_m=C_m/C_{m-1}\). Then an exact telescoping identity is
\[
\log\frac{C_{n-a-b}C_n}{C_{n-a}C_{n-b}}=\sum_{i=0}^{a-1}\sum_{j=0}^{b-1}\big(\log r_{n-i-j}-\log r_{n-i-j-1}\big).
\]
Since \(r_m=4-6/(m+1)\), uniformly for \(1\le a,b\le K\log n\) with fixed \(K>0\), the right side equals \(3ab/(2n^2)+O(ab(a+b+1)/n^3)\). Also \(p_a=4^{-a}(1+O(a/n))\) uniformly on that range. It follows that
\[
\Delta_{a,b}=4^{-(a+b)}\left(\frac{3ab}{2n^2}+O\left(\frac{ab(a+b+1)}{n^3}\right)\right).
\]
The error sums absolutely: \(\sum_{a,b\ge1}ab(a+b+1)4^{-(a+b)}<\infty\). To justify discarding larger thresholds, elementary upper/lower Catalan bounds give \(p_a\le K_0(n+1)^{3/2}4^{-a}\) for a universal \(K_0\). Because every \(\Delta_{a,b}>0\) and \(\Delta_{a,b}\le p_a\), the total contribution of indices with \(a>A\) or \(b>A\) is at most \(2n\sum_{a>A}p_a\le K_1n(n+1)^{3/2}4^{-A}\). Take \(A=\lceil10\log_4n\rceil\) for large \(n\): this is \(o(n^{-2})\). Consequently
\[
\lim_{n\to\infty}n^2\operatorname{Cov}(X_n,Y_n)=\frac32\left(\sum_{a\ge1}a4^{-a}\right)^2=\frac32\left(\frac49\right)^2=\frac8{27}.
\]
The proof establishes a rate only for this covariance, not total-variation independence.

## Verification
A standalone Python 3 script `check.py` independently enumerates all \(231\)-avoiders of lengths \(2\) through \(8\) from permutations, reconstructs the two boundary statistics and checks each exact tail, strict tail covariance and the covariance tail-sum identity with rational arithmetic. It checks 490 assertions across 2054 avoiders. It additionally computes exact Catalan-sum covariances at sizes \(40,100,200,400\), whose rescaled values approach \(8/27\). Finite checks are corroboration; the unrestricted conclusion follows from the proof above. Run: `python check.py` in an environment with Python 3 standard library.

## Relationship to prior work
Albert, Bouvel, Féray and Noy (2022 preprint, published 2024) prove a logical limit law for uniform \(231\)-avoiders and explicitly note that permutation fixed points are not expressible in their two-orders first-order logic. Their main theorem therefore does not entail the finite joint fixed-prefix/fixed-suffix law or its second-order asymptotic covariance. Hoffman, Rizzolo and Slivken (2015) analyze the empirical fixed-point distribution through Brownian excursion, including bulk scaling; this is a different object and asymptotic regime from fixed identity runs at the extreme boundary. Classical Catalan enumeration and direct-sum closure are used here as known tools, not claimed as new. Earlier Catalan enumerations may implicitly contain the exact tail counts; the additional strict quadrant-association theorem and sharp \(n^{-2}\) correlation scale are the proposed contribution.

## Limitations
The model is restricted to uniform \(231\)-avoiders. The boundary lengths are counts of *consecutive fixed identity positions*, not the total number of fixed points or arbitrary increasing runs. The limit law concerns fixed finite boundary indices. Historical priority of equivalent tail-correlation statements is not independently settled. An independent mathematical audit has not been performed.

## References
1. M. Albert, M. Bouvel, V. Féray, M. Noy, *A logical limit law for 231-avoiding permutations*, arXiv:2210.05537, first publicly posted October 11, 2022; Discrete Mathematics & Theoretical Computer Science 26 (2024). https://arxiv.org/abs/2210.05537
2. C. Hoffman, D. Rizzolo, E. Slivken, *Pattern-avoiding permutations and Brownian excursion, Part II: Fixed points*, arXiv:1506.04174 (2015). https://arxiv.org/abs/1506.04174
3. M. Albert, M. Bouvel, *A general theory of Wilf-equivalence for Catalan structures*, arXiv:1407.8261 (2014). https://arxiv.org/abs/1407.8261
