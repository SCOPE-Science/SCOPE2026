# Periodic separation dimension can increase under time iteration

## Finding
For the asymptotic periodic separation exponent \(\mathfrak s(T)\) of Kong--Wang--Yu, all positive integer iterates obey the one-sided inequality
\[
\mathfrak P^{s}(T^{q})\ge q^{-1}\mathfrak P^{s}(T),\qquad
\mathfrak s(T^{q})\ge\mathfrak s(T)
\]
for every integer \(q\ge2\), every \(s\ge0\), and every totally bounded metric dynamical system, with extended-real conventions. Despite this monotonicity, **for every such \(q\)** there is an explicit countable compact Euclidean planar system \((X_q,F_q)\), with \(F_q\) a homeomorphism, for which
\[
\mathfrak s(F_q)=0,\qquad \mathfrak s(F_q^{q})=1,
\qquad h_{\mathrm{top}}(F_q)=0.
\]
More precisely, its periodic contents satisfy
\[
\mathfrak P^{s}(F_q)=0\ (s>0),\qquad
\mathfrak P^{s}(F_q^q)=
\begin{cases}+\infty&0\le s<1,\\0&s\ge1.\end{cases}
\]
In particular, at the critical exponent \(s=1\), the iterated system has zero periodic content even though its separation dimension equals one.

## Assumptions and scope
Let \((X,d)\) be totally bounded and \(T:X\to X\) a map. A periodic orbit \(\mathcal O\) of cardinality \(N\ge2\) has minimal pairwise gap \(\eta(\mathcal O)=\min_{x\ne y\in\mathcal O}d(x,y)\). Set
\[
\mathfrak P_n^s(T)=\sup_{\mathcal O:\,\#\mathcal O\ge n}
\#\mathcal O\,\eta(\mathcal O)^s,
\quad \mathfrak P^s(T)=\lim_{n\to\infty}\mathfrak P_n^s(T).
\]
The supremum of the empty collection is zero; the limit exists, since the suprema decrease in \(n\). We take \(s\ge0\), interpreting \(\eta^0=1\) for a nontrivial orbit, and define
\[
\mathfrak s(T)=\sup\{s\ge0:\ \mathfrak P^s(T)>0\},
\]
with supremum of an empty subset of \([0,\infty)\) equal to zero. This agrees with the sequence-of-periodic-orbits formulation for the systems here and, for general systems, via selection of near-supremal orbits. No invariance of the metric or measure is assumed. The explicit example uses the Euclidean metric on \(\mathbb R^2\).

## Proof
**1. Passing to an iterate.** Fix \(q\ge2\). A period-\(N\) orbit of \(T\) splits under \(T^q\) into \(g=\gcd(N,q)\) distinct orbits, each of length \(N/g\). As each new orbit is a subset of the old one, its gap is no smaller. Since \(g\le q\), every \(T\)-orbit of size \(N\ge qn\) therefore supplies a \(T^q\)-orbit of size at least \(n\) and contribution at least \(q^{-1}N\eta(\mathcal O)^s\). Taking suprema gives
\[
\mathfrak P_n^s(T^q)\ge q^{-1}\mathfrak P_{qn}^s(T).
\]
The monotone limit gives the asserted content inequality, hence the dimension inequality.

**2. Euclidean construction.** Fix the same integer \(q\). For integers \(m\ge2\), write
\[
H_m=\sum_{k=1}^m\frac1k,\qquad r_m=H_m^{-1},\qquad
\varepsilon_m=\frac{2^{-m^2}}{100qm^2}.
\]
For \(0\le j<m\) and \(0\le h<q\), define
\[
z_{m,j,h}=\left(\frac{jr_m}{m},\ \frac1m+h\varepsilon_m\right)
\in\mathbb R^2,
\quad X_q=\{(0,0)\}\cup\{z_{m,j,h}:m\ge2,\,0\le j<m,\,0\le h<q\}.
\]
The vertical intervals for different \(m\) do not intersect: indeed
\[
(q-1)\varepsilon_m <\frac1{100m^2}<\frac1{m(m-1)}
\]
for \(m\ge2\), so the \(m\)-th shell lies in the half-open height interval \([1/m,1/(m-1))\). Every shell is finite, and \(r_m\to0\); hence the origin is the **only** accumulation point. Thus \(X_q\) is compact and countable.

Define \(F_q(0,0)=(0,0)\) and
\[
F_q(z_{m,j,h})=\begin{cases}
z_{m,j,h+1},&0\le h<q-1,\\
z_{m,(j+1)\bmod m,0},&h=q-1.
\end{cases}
\]
Each finite shell is one cyclic orbit of length \(qm\). The permutation and its inverse preserve the shell index. Since both send points from shells \(m\to\infty\) to points converging to the origin, both are continuous at the sole accumulation point; \(F_q\) is a homeomorphism.

**3. Exact orbit gaps.** Distinct points with different horizontal indices have Euclidean distance at least \(r_m/m\). When horizontal indices agree but vertical indices differ, their distance is at least \(\varepsilon_m\), attained by neighboring vertical levels. Since \(H_m\le m\) and
\[
\varepsilon_m<\frac1{m^2}\le\frac{r_m}{m},
\]
the unique period-\(qm\) orbit on shell \(m\) has exact gap \(\varepsilon_m\). Under \(F_q^q\), that shell splits into \(q\) period-\(m\) orbits indexed by \(h\); each consists of \(m\) equally spaced points on one horizontal line, with exact gap \(r_m/m\). Together with the fixed origin, these exhaust the periodic orbits of the respective maps.

**4. Critical exponent calculations.** For \(s>0\), direct substitution gives
\[
\mathfrak P^s(F_q)=\lim_{n\to\infty}\sup_{qm\ge n}
qm\,\varepsilon_m^s=0,
\]
because \(qm\,2^{-sm^2}(100qm^2)^{-s}\to0\). At \(s=0\) the periodic content is infinite, so \(\mathfrak s(F_q)=0\). For the iterate,
\[
\mathfrak P^s(F_q^q)=\lim_{n\to\infty}\sup_{m\ge n}
\frac{m^{1-s}}{H_m^s}.
\]
The elementary integral bounds \(\log(m+1)\le H_m\le1+\log m\) show that the summand tends to infinity when \(0\le s<1\), and tends to zero when \(s\ge1\). This proves the claimed content dichotomy and \(\mathfrak s(F_q^q)=1\).

**5. Entropy.** Given \(\delta>0\), choose \(m_0\) such that the union of all shells \(m\ge m_0\), together with the origin, has diameter less than \(\delta\). This union is invariant under every iterate of \(F_q\). Therefore every \((n,\delta)\)-separated subset of \(X_q\) has at most one point in this tail and at most the finite number of points in lower shells, independently of \(n\). Consequently \(h_{\mathrm{top}}(F_q)=0\).

## Verification
All geometric gap equalities and finite-shell orbit claims admit exact rational checking. The accompanying standalone \(\texttt{check.py}\), using only the Python standard library, tests \(q=2,\ldots,6\) and \(m=2,\ldots,12\), checks both minimal squared Euclidean gaps by exhaustive pair comparison and orbit-period enumeration, and verifies shell separation through \(m=30\). Its output is \(\texttt{PASS 420 exact rational diagnostics}\). The infinite content limits, compactness, monotonicity, and entropy conclusion follow from the written proof; the finite checks are not substitutes for those arguments.

## Relationship to prior work
Kong, Wang, and Yu introduced the separation exponent \(\mathfrak s\) and established its identification with Hausdorff dimension for strongly separated self-similar systems (arXiv:2609.16296v1). Their publicly accessible abstract and inspected initial preprint sections motivate the present question but do not furnish the claimed universal time-iterate inequality or the countable planar sharpness construction. The two statements are not implications of conjugacy comparisons: iteration changes the decomposition of periodic orbits while leaving the underlying metric unchanged. Independent published work on periodic separation of a \(\{\rho,\rho^2\}\) contraction pair concerns positive critical content for a self-similar system, rather than passage from \(T\) to \(T^q\). Dynamical-dimension results for finite-index subgroups and entropy under iteration concern different invariants.

## Limitations
The exhibited time-iterate jump is specifically \(0\) to \(1\) on a zero-entropy, countable compact Euclidean planar space. The theorem does not claim an upper bound on \(\mathfrak s(T^q)\) in terms of \(\mathfrak s(T)\), maximal jumps in arbitrary ambient dimension, or analogous behavior for expanding smooth maps. The original preprint's later sections were not accessible in full for comparison; independent literature verification remains desirable. 
## References
1. D. Kong, Z. Wang and D. Yu, *Asymptotic separation of periodic orbits and fractal dimension*, arXiv:2609.16296v1 (first public 2026-09-14), https://arxiv.org/abs/2609.16296.
2. *Positive critical periodic content for the {rho,rho-squared} contraction pair*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-positive-critical-periodic-content-for-the-rho-rho-2-contraction--f867b43e8ea4.
3. *Sharp finite-index restriction law for dynamical dimension*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-finite-index-restriction-law-for-dynamical-dimension--b7e316c9e024.
