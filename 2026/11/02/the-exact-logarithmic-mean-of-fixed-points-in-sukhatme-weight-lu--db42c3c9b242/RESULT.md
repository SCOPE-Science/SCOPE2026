# The exact logarithmic mean of fixed points in Sukhatme-weight Luce permutations

## Finding

Consider Luce sampling without replacement on \(\{1,\ldots,n\}\) with prescribed weights \(\theta_i=n-i+1\). Define the permutation by \(\sigma_n(i)=\) the position at which label \(i\) is drawn, and let \(F_n=\sum_{i=1}^n\mathbf 1\{\sigma_n(i)=i\}\). Then

\[
\boxed{\lim_{n\to\infty}\frac{\mathbb E F_n}{\log n}=\frac1e.}
\]

The coefficient concerns the unbounded diagonal fixed-point regime of the Sukhatme choice, not a smooth-permuton finite-mean regime.

## Assumptions and scope

For every integer \(n\ge2\), sequentially draw labels with probability proportional to their remaining positive weights \(\theta_i=n-i+1\). The random variable \(F_n\) counts fixed points of the **draw-rank permutation** (equivalently of its inverse, since fixed-point counts are inversion invariant). The logarithm is natural. The limit is along all integers \(n\to\infty\), with no additional parameters. The finite formula below is also valid for \(n=1\).

## Proof

**1. Exponential-race reduction.** Reverse labels so that the item of rate \(k\), \(1\le k\le n\), has the original label \(n-k+1\). Let \(T_k\sim\operatorname{Exp}(k)\) be independent. Their increasing order realizes the Luce draw order. The original label is fixed precisely when \(T_k\) has rank \(n-k+1\) in increasing order, equivalently when exactly \(k-1\) other clocks exceed \(T_k\). At each \(t>0\) introduce independent Bernoulli variables \(B_j(t)=\mathbf1\{T_j>t\}\) with probabilities \(p_j(t)=e^{-jt}\). Write \(S_n(t)=\sum_{j=1}^nB_j(t)\) and \(S_{-k}(t)=S_n(t)-B_k(t)\). Conditioning on \(T_k=t\) gives the exact, non-asymptotic formula

\[
\mathbb E F_n=\int_0^\infty G_n(t)\,dt,\qquad
G_n(t)=\sum_{k=1}^n k e^{-kt}\Pr\big(S_{-k}(t)=k-1\big).
\tag{1}
\]

**2. Uniform integrability in logarithmic time.** For any realized zero-one vector \((B_1,\dots,B_n)\) with sum \(S=s\), the equation \(S_{-k}=k-1\) holds for at most two values: \(k=s\) when \(s\ge1\) and \(B_s=1\), or \(k=s+1\) when \(s<n\) and \(B_{s+1}=0\). Thus

\[
G_n(t)=\mathbb E\!\left[S e^{-St}\mathbf1_{\{S\ge1,B_S=1\}}
+(S+1)e^{-(S+1)t}\mathbf1_{\{S<n,B_{S+1}=0\}}\right].
\tag{2}
\]

Since \(\mathbb E S=\sum_{j=1}^ne^{-jt}\le(e^t-1)^{-1}\le t^{-1}\), the bound \(G_n(t)\le2(\mathbb E S+1)\) yields

\[
0\le tG_n(t)\le4\qquad(0<t\le1).
\tag{3}
\]

Also \(G_n(t)\le2(n+1)\), so the contribution from \(0<t<n^{-1}\) is uniformly bounded. For \(t\ge1\), \(G_n(t)\le\sum_{k=1}^\infty k e^{-kt}=e^{-t}/(1-e^{-t})^2\), integrable on \([1,\infty)\). Both endpoint integrals are \(O(1)\), hence negligible relative to \(\log n\).

**3. Key local mass identity.** Suppose \(t=t_n\to0\) while \(nt_n\to\infty\). In this step suppress the arguments \(n,t\). Put \(m=\mathbb E S\) and \(v=\operatorname{Var}S\). Geometric series show

\[
tm\to1,\qquad tv\to\frac12,\qquad v\to\infty.
\tag{4}
\]

For any Bernoulli sum \(Y\) of variance \(V>0\), Fourier inversion and
\(\lvert\mathbb E e^{i\theta Y}\rvert\le\exp[-2V\sin^2(\theta/2)]\) imply the adjacent-mass bound

\[
\sup_{r\in\mathbb Z}\big|\Pr(Y=r)-\Pr(Y=r-1)\big|
\le\frac1{2\pi}\int_{-\pi}^\pi |\theta|e^{-2V\theta^2/\pi^2}\,d\theta
\le\frac\pi{4V}.
\tag{5}
\]

This applies uniformly to \(Y=S_{-k}\) because \(\operatorname{Var}S_{-k}=v-p_k(1-p_k)\ge v-1/4\). By conditioning on \(B_k\),

\[
\big|\Pr(S_{-k}=k-1)-\Pr(S=k-1)\big|
\le\frac{C}{v}
\tag{6}
\]

with a numerical constant \(C\), for all \(k\) and sufficiently small \(t\).

Fix \(M>0\), and let \(I_M=\{k\in\{1,\dots,n\}:|k-m|\le M\sqrt v\}\). Its cardinality is \(O(M\sqrt v)\). Summing (6) on \(I_M\) gives error \(O(M/\sqrt v)=o(1)\). Chebyshev yields

\[
\limsup_{n\to\infty}\sum_{k\notin I_M}\Pr(S=k-1)\le M^{-2}.
\tag{7}
\]

Moreover \(S_{-k}=k-1\) forces \(S\in\{k-1,k\}\), and for a fixed realization at most two indices \(k\) satisfy this event. Therefore

\[
\limsup_{n\to\infty}\sum_{k\notin I_M}
\Pr(S_{-k}=k-1)\le 2M^{-2}.
\tag{8}
\]

(The harmless integer shifts in (7)--(8) vanish compared with \(\sqrt v\).) Equations (6)--(8), followed by \(M\to\infty\), show that the local masses \(\Pr(S_{-k}=k-1)\) carry asymptotically total weight one, concentrated in \(I_M\).

For fixed \(M\), uniformly on \(I_M\), (4) implies

\[
tk\to1,\qquad t k e^{-kt}\to e^{-1},
\tag{9}
\]

since \(t\sqrt v=O(\sqrt t)\to0\). The global bound \(tk e^{-kt}\le e^{-1}\), combined with (6)--(9), proves the pointwise scaling lemma

\[
\boxed{t_nG_n(t_n)\to e^{-1}
\quad\text{whenever } t_n\to0,\ nt_n\to\infty.}
\tag{10}
\]

**4. Logarithmic integration.** Set \(t=n^{-u}\) for \(u\in[0,1]\). By the endpoint bounds, the change of variables and (3),

\[
\frac{\mathbb E F_n}{\log n}
=\int_0^1 n^{-u}G_n(n^{-u})\,du+o(1).
\]

At every \(u\in(0,1)\), we have \(t\to0\) and \(nt\to\infty\), so (10) gives pointwise convergence to \(e^{-1}\). The bound (3) supplies the integrable dominating constant four. Dominated convergence gives the claimed limit. \(\square\)

## Verification

The standalone Python 3 checker `verify.py` computes the exact expectation in two independent finite ways: enumeration of all weighted draw orders, and expansion/integration of the Bernoulli exceedance generating polynomial, for sizes \(1\) through \(7\). It also checks the pointwise Bernoulli-integrand identity (2) for sizes \(1\) through \(8\) at four distinct positive times, for **39 deterministic exact/analytic checks**. A separately seeded Monte Carlo experiment at larger sizes is a diagnostic, not part of the proof. The exact comparison and diagnostic output are included as `verification-output.txt`. The limit follows exclusively from the four proof steps above.

## Relationship to prior work

Borga, Chatterjee and Diaconis identify the Sukhatme fixed-point regime as singular and record the unresolved growth/distribution question in Section 5.2; their permuton local limits do not state an exact finite fixed-point mean or its logarithmic coefficient. Mukherjee's fixed-point Poisson theorem uses a strictly positive continuous limiting density and uniform local control, in contrast to this unbounded diagonal density and divergent mean. Paguyo's double-coset fixed-point approximation concerns a different conditional uniform-permutation model with distinct parameter assumptions. Borga and Dubach consider the longest increasing subsequence for Luce models, not the fixed-point mean. The present result proves only the leading expectation constant, rather than the full fixed-point distribution proposed as an open direction.

## Limitations

No variance asymptotic, concentration theorem, Poisson approximation, convergence in distribution, second-order additive constant or universality across other Luce weight families is proved. The coefficient is for the precise linear descending Sukhatme weights and draw-rank convention. Although targeted comparisons found no stronger covering statement, an unindexed historical identity for size-biased permutations could affect priority; absence of a search match is not an independence certificate.

## References

1. J. Borga, S. Chatterjee and P. Diaconis, *Permuton and local limits for the Luce model*, arXiv:2509.07729, submitted September 9, 2025, Section 5.2 (version 3, September 29, 2026), https://arxiv.org/html/2509.07729v3 .
2. S. Mukherjee, *Fixed points and cycle structure of random permutations*, arXiv:1509.04552, 2015/2016, Theorems 1.1 and 1.3, https://arxiv.org/html/1509.04552v3 .
3. J. E. Paguyo, *Fixed points, descents, and inversions in parabolic double cosets of the symmetric group*, arXiv:2112.07728, 2021/2023, Theorem 1.1, https://arxiv.org/html/2112.07728v2 .
4. J. Borga and V. Dubach, *The longest increasing subsequences of Luce permutations and permutons*, arXiv:2610.30382, posted October 21, 2026, https://arxiv.org/abs/2610.30382 .
