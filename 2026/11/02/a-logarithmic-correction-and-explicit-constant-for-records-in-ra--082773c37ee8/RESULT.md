# A logarithmic correction and explicit constant for records in random parking permutations

## Finding
Let \(R_n\) be the number of left-to-right maxima in the parking-order permutation produced by a uniformly sampled classical parking function with \(n\) cars. As \(n\to\infty\),
\[
\boxed{\mathbb E R_n=\sqrt{\frac{\pi n}{2}}+\frac12\log n+\frac{\gamma+\log2}{2}-\frac43+o(1),}
\]
where \(\gamma\) is Euler's constant and logarithms are natural. In particular, the previously known first-order square-root approximation misses a growing logarithmic term, while subtracting the displayed three terms leaves an error tending to zero.

## Assumptions and scope
For an integer \(n\ge1\), a preference vector \((a_1,\ldots,a_n)\in\{1,\ldots,n\}^n\) is a classical parking function if sequential arrivals numbered \(1,\ldots,n\), each taking the first vacant space at or after their preference, all park successfully. Sample uniformly from the \((n+1)^{n-1}\) successful preference vectors. Write \(\sigma_i\) for the number of the car occupying position \(i\) after parking. A left-to-right maximum is a position \(i\) with \(\sigma_i>\max_{j<i}\sigma_j\), using the empty maximum convention at \(i=1\). Let \(R_n\) be their count. The theorem is only about its expectation under this induced (nonuniform) law on permutations.

## Proof
**Step 1. Known finite identity.** The exact expectation is established in Theorem 16 and equation (85) of Pinsky [1]. Write \(N=n+1\), and for \(1\le k\le N-1\) let
\[
p_{N,k}=\prod_{j=1}^k\left(1-\frac jN\right).
\]
Reindexing equation (85), and combining its two summands, gives
\[
\mathbb E R_n=U_N+V_N,\qquad U_N=\sum_{k=1}^{N-1}p_{N,k},\quad V_N=\sum_{k=1}^{N-1}\frac{p_{N,k}}{k}.
\]
The original identity and its leading square-root asymptotic are prior work; only the finer asymptotic evaluation is claimed here.

**Step 2. The unweighted sum, including its constant.** Put \(\varepsilon=N^{-1/2}\), \(u=k\varepsilon\), and restrict initially to \(1\le k\le\sqrt N\log N\). Taylor expansion of the logarithm, with sums of the first two powers, gives uniformly on this range
\[
\log p_{N,k}=-\frac{u^2}{2}-\varepsilon\left(\frac u2+\frac{u^3}{6}\right)+O\left(\frac{1+(\log N)^4}{N}\right).
\]
Consequently, uniformly for such \(k\),
\[
p_{N,k}=e^{-u^2/2}\left[1-\varepsilon\left(\frac u2+\frac{u^3}{6}\right)\right]
+O\left(\frac{1+(\log N)^6}{N}\right).
\]
The error summed over this range is \(o(1)\). For larger \(k\), the bound \(0\le p_{N,k}\le\exp[-k(k+1)/(2N)]\) shows that the omitted tails, including the corresponding Gaussian tails, have sum \(o(1)\). Therefore
\[
U_N=\sum_{k\ge1}e^{-k^2/(2N)}-\frac1{\sqrt N}\sum_{k\ge1}e^{-k^2/(2N)}\left(\frac{k}{2\sqrt N}+\frac{k^3}{6N^{3/2}}\right)+o(1).
\]
The Gaussian mesh sum has the Euler--Maclaurin expansion
\[
\sum_{k\ge1}e^{-k^2/(2N)}=\sqrt{\frac{\pi N}{2}}-\frac12+o(1).
\]
The correction is a Riemann sum converging to
\[
\int_0^\infty e^{-u^2/2}\left(\frac u2+\frac{u^3}{6}\right)\,du=\frac12+\frac13=\frac56.
\]
Thus
\[
U_N=\sqrt{\frac{\pi N}{2}}-\frac43+o(1).
\]

**Step 3. The harmonic-weighted sum.** The same expansion and tail bounds imply
\[
V_N=\sum_{k\ge1}\frac{e^{-k^2/(2N)}}{k}+o(1).
\]
Here the Gaussian correction in Step 2 contributes only \(O(N^{-1/2})\) after the extra factor \(1/k\); the uniform remainder and the tails also tend to zero. Put \(M=\sqrt{2N}\) and \(m=\lfloor M\rfloor\). Subtracting \(H_m=\sum_{k=1}^m1/k\) and converting the remainder to a Riemann sum yields
\[
\sum_{k\ge1}\frac{e^{-(k/M)^2}}{k}-H_m
\longrightarrow\int_0^\infty\frac{e^{-u^2}-\mathbf1_{\{u\le1\}}}{u}\,du=-\frac\gamma2.
\]
For the last identity substitute \(t=u^2\) and use \(\Gamma(s)-1/s\to-\gamma\) as \(s\downarrow0\). Since \(H_m=\log M+\gamma+o(1)\),
\[
V_N=\frac12\log(2N)+\frac\gamma2+o(1).
\]

**Step 4. Combine.** Adding the previous two expressions, then using \(N=n+1\), changes \(\sqrt{\pi N/2}\) by \(o(1)\) and \(\log N\) by \(o(1)\). This gives the stated formula. \(\square\)

## Verification
A standalone pure-Python program, `verify.py`, independently enumerates all successful preference vectors for \(1\le n\le6\), checks both the source's original finite formula and the reindexed product formula using exact rational arithmetic, then evaluates the exact product sum numerically for \(n=1000,10000,100000,1000000\) and tests convergence toward the explicit constant. Run `python3 verify.py`. These finite tests corroborate, but do not substitute for, Steps 2--4.

## Relationship to prior work
Pinsky [1] introduced the induced distribution on permutations, established the exact mean formula and proved \(\mathbb E R_n\sim\sqrt{\pi n/2}\). The present formula is an additional refined asymptotic consequence of that exact expression; the finite identity and leading term are **not** new. In particular, the correction concerns record maxima of the *parking-order permutation*; it is not the usual lucky-car count (where a car parks at its originally preferred position), and it is not a statistic of the *preference vector* itself. The classical random-parking analyses of Diaconis--Hicks [2] and Bellin [3] concern different coordinate or preference observables. This asymptotic refinement was not located in the checked accessible texts; its absolute historical priority is not certified.

## Limitations
The formula is an asymptotic expected-value expansion, not a concentration bound, a distributional limit, or an extension to other parking rules. It relies on the previously published exact expectation and does not claim that identity as new. The \(o(1)\) remainder is proved but not optimized to an explicit rate. Equivalent expansions could appear in sources not accessible or not indexed; no independent review has been performed.

## References
[1] R. G. Pinsky, *The distribution on permutations induced by a random parking function*, arXiv:2404.11529 (first submitted 2024-04-17); *Electronic Journal of Combinatorics* **33** (2026), #P1.50, Theorem 16 and equation (85), https://doi.org/10.37236/13842.

[2] P. Diaconis and A. Hicks, *Probabilizing parking functions*, *Advances in Applied Mathematics* **89** (2017), 125--155, https://doi.org/10.1016/j.aam.2017.05.004.

[3] E. Bellin, *Asymptotic behaviour of the first positions of uniform parking functions*, *Journal of Applied Probability* **60** (2023), 1201--1218, https://doi.org/10.1017/jpr.2022.131.
