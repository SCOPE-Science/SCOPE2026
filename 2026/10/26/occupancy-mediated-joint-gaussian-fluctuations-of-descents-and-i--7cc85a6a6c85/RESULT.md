# Occupancy-mediated joint Gaussian fluctuations of descents and inversions in random-to-top shuffles

## Finding

For a random-to-top shuffle on \(n\) distinguishable cards, initially in increasing order, choose one of the \(n\) cards uniformly and move it to the top at each step, independently of earlier selections. Fix \(c>0\) and perform \(r_n=\lfloor cn\rfloor\) steps. Write \(D_n\) for the number of adjacent descents and \(I_n\) for the number of inversions of the resulting one-line deck. Then
\[
\left(\frac{D_n-na/2}{\sqrt n},\frac{I_n-n^2(2a-a^2)/4}{n^{3/2}}\right)\ \Longrightarrow\ \mathcal N_2(0,\Sigma_c),
\]
where \(a=1-e^{-c}\), \(\tau_c^2=e^{-c}-(1+c)e^{-2c}>0\), and
\[
\Sigma_c=\begin{pmatrix}
\frac a{12}+\frac{\tau_c^2}{4}&\frac{(1-a)\tau_c^2}{4}\\
\frac{(1-a)\tau_c^2}{4}&\frac{a-a^2+a^3/3}{12}+\frac{(1-a)^2\tau_c^2}{4}
\end{pmatrix}.
\]
In particular, the off-diagonal covariance is **strictly positive for every finite \(c>0\)**. The limiting Gaussian vector decomposes as
\[
(G_D+Z/2,\ G_I+(1-a)Z/2),
\]
with independent centered normals \(G_D,G_I,Z\) of variances \(a/12\), \((a-a^2+a^3/3)/12\), and \(\tau_c^2\), respectively. Thus the sole source of nonzero limiting descent–inversion covariance is fluctuation in the number of distinct cards moved, not the random ordering conditional on that number. The contrast
\[
\frac{I_n-n^2(2a-a^2)/4}{n^{3/2}}-(1-a)\frac{D_n-na/2}{\sqrt n}
\]
has a Gaussian limit independent of the coupon-occupancy fluctuation.

## Assumptions and scope

All random moves select card **labels**, not deck positions, uniformly with replacement. The value \(c\) is fixed in \((0,\infty)\); all limits are taken as the positive integer \(n\to\infty\). Descents are indices \(1\le i<n\) with the card at position \(i\) greater than that at \(i+1\). Inversions are pairs \(1\le i<j\le n\) where the former card is larger. This is joint weak convergence of two centered, differently scaled statistics, not a uniform-in-\(c\) bound, large-deviation principle, or finite-sample independence assertion. The primary classification is MSC2020 60F05.

## Proof

**1. Exact joint conditional construction.** Let \(K_n\) be the number of distinct labels selected during the \(r_n\) moves. Conditional on \(K_n=k\), the first \(k\) positions form a uniformly random ordered \(k\)-subset; the unselected labels follow in increasing order. This is Proposition 4.1 of Clay [1]. For an independent iid \(U_1,\dots,U_n\sim\operatorname{Unif}(0,1)\), sorting the last \(n-k\) ranked values into increasing order produces *both* statistics jointly as
\[
D_n\stackrel d=\sum_{i=1}^{K_n-1}\mathbf1\{U_i>U_{i+1}\}+B_{K_n,n},\qquad
I_n\stackrel d=\sum_{i=1}^{K_n}\sum_{j=i+1}^n\mathbf1\{U_i>U_j\},
\]
with \(B_{k,n}=\mathbf1\{k<n,\ U_k>\min_{j>k}U_j\}\in\{0,1\}\), using the *same* \(U\)-sample for both coordinates. Here \(K_n\) is independent of all \(U_i\). This common coupling, rather than two separate marginal identities, is essential.

**2. Occupancy.** Classical uniform occupancy gives
\[
\frac{K_n-na}{\sqrt n}\Longrightarrow Z\sim N(0,\tau_c^2),\qquad
\mathbb EK_n=na+O(1),\quad \operatorname{Var}(K_n)=n\tau_c^2+O(1).
\]
The variance and central limit theorem follow from the occupancy count theorem (Weiss [2], as used in [1]). The order-one mean error holds for \(r_n=\lfloor cn\rfloor\). Positivity follows from \(e^c>1+c\).

**3. Deterministically truncated Gaussian pair.** Put \(k_n=\lfloor an\rfloor\). Define
\[
A_k=\sum_{i=1}^{k-1}\left(\mathbf1\{U_i>U_{i+1}\}-\tfrac12\right),\qquad
J_k=\sum_{i=1}^k\sum_{j=i+1}^n\left(\mathbf1\{U_i>U_j\}-\tfrac12\right).
\]
The first is a sum of bounded 1-dependent random variables, with exact variance \((k+1)/12\) for \(k\ge2\). The Hoeffding first-order projection of \(J_k\) is
\[
L_k=\sum_{t=1}^n w_{t,k}(U_t-\tfrac12),\quad
w_{t,k}=\begin{cases}n-2t+1&t\le k,\\-k&t>k.\end{cases}
\]
The remainder \(R_k=J_k-L_k\) is a sum of orthogonal canonical pair kernels
\[
h(u,v)=\mathbf1\{u>v\}-u+v-\tfrac12.
\]
Every such kernel has variance \(1/12\), and distinct pair kernels are orthogonal even when they share one index. Consequently \(\operatorname{Var}(R_k)\) equals \(k(2n-k-1)/24\), which is \(O(n^2)\); hence \(R_{k_n}/n^{3/2}\to0\) in \(L^2\).

A direct sum of squared weights yields
\[
\frac{\operatorname{Var}(L_{k_n})}{n^3}\longrightarrow
v_I(a)=\frac1{12}\left[\int_0^a(1-2x)^2\,dx+\int_a^1a^2\,dx\right]=\frac{a-a^2+a^3/3}{12}.
\]
For each \(i<k_n\), \(\operatorname{Cov}(\mathbf1\{U_i>U_{i+1}\}, U_i-1/2)=1/12\) and its covariance with \(U_{i+1}-1/2\) is \(-1/12\). Therefore
\[
\operatorname{Cov}(A_{k_n},L_{k_n})=\sum_{i=1}^{k_n-1}\frac{w_{i,k_n}-w_{i+1,k_n}}{12}=\frac{k_n-1}{6}=O(n),
\]
and this covariance divided by \(n^2\) vanishes. Every Cramér–Wold combination of \(A_{k_n}/\sqrt n\) and \(L_{k_n}/n^{3/2}\) is a sum of bounded, centered, 1-dependent triangular-array terms, each uniformly \(O(n^{-1/2})\). A standard independent-block proof applies: use blocks of length \(\lfloor n^{1/4}\rfloor\) separated by one discarded index; discarded terms have vanishing total variance, each retained block tends uniformly to zero in magnitude, and the retained independent blocks satisfy Lindeberg. Thus
\[
\left(A_{k_n}/\sqrt n,J_{k_n}/n^{3/2}\right)\Longrightarrow (G_D,G_I),
\]
where \(G_D,G_I\) are independent centered normals with variances \(a/12\) and \(v_I(a)\), respectively.

**4. Replace fixed index by occupancy.** For every integer \(k\), let \(\mu_n(k)=k(2n-k-1)/4\); this is exactly the conditional mean of the inversion sum. Since \(K_n-k_n=O_p(\sqrt n)\) and is independent of the uniforms, the 1-dependent variance bound for a shifted descent-index interval yields
\[
(A_{K_n}-A_{k_n})/\sqrt n\to0\quad\text{in }L^2.
\]
For the inversions, the projection coefficients differ only at \(|K_n-k_n|\) changed leading indices and by a constant \(|K_n-k_n|\) on the remaining tail. Orthogonality of the canonical pair remainders consequently bounds
\[
\mathbb E[(J_{K_n}-J_{k_n})^2]\le C\big(n^2\mathbb E|K_n-k_n|+n\mathbb E(K_n-k_n)^2\big)=O(n^{5/2}),
\]
so \((J_{K_n}-J_{k_n})/n^{3/2}\to0\) in \(L^2\). Taylor's identity for \(\mu_n\) gives
\[
\frac{\mu_n(K_n)-n^2(2a-a^2)/4}{n^{3/2}}=\frac{1-a}{2}\frac{K_n-na}{\sqrt n}+o_p(1).
\]
The descent mean is \((K_n-1)/2\) plus the bounded boundary indicator, so its corresponding leading occupancy term is \((K_n-na)/(2\sqrt n)\). Since \(K_n\) is independent of the uniforms for each \(n\), the Gaussian pair in step 3 and the occupancy limit are jointly independent. Slutsky's theorem establishes the three-independent-normal decomposition and the displayed covariance matrix.

## Verification

The standalone standard-library-first script `verify.py` enumerates the exact joint conditional distributions for \(3\le n\le7\), checks conditional means, variances and covariance, verifies the Hoeffding projection variance formula, and compares the exact shuffle-history law against the occupancy-mixture law for \(3\le n\le5\), \(1\le r\le4\). When SymPy is installed it also checks that the two covariance-matrix diagonal entries reduce identically to the respective univariate formulas in [1]. Run `python verify.py` from the extracted package directory. It reports 202 successful exact algebraic, coupling and moment checks in the available environment. These finite checks corroborate the algebra; the all-\(n\) theorem follows from the proof, not enumeration.

## Relationship to prior work

Clay [1], public since March 9, 2026, proves the two separate critical-regime Gaussian limits and the common conditional-prefix construction, but does not state their joint distribution or calculate their limiting covariance. Dörr and Heiny [3] prove joint Gaussian/extreme-value results for **uniform** permutations; those correspond to the fully mixed, zero-occupancy-fluctuation regime and do not entail a positive cross-covariance for an intermediate number of random-to-top moves. Işlak [4] studies descents and inversions under **riffle** shuffles, a different transition kernel. The result here identifies the complete joint Gaussian law at every fixed finite positive shuffle density and explicitly separates permutation-order noise from occupancy noise. The known marginal variances in [1] match the diagonal entries above; they do not alone imply the off-diagonal entry.

## Limitations

The result concerns uniform random-to-top moves from the identity, fixed \(c>0\), and Gaussian weak convergence only. It does not show conditional independence at finite size: that assertion is false in general. It does not yield a joint local limit theorem, total-variation convergence for discrete statistics, convergence-rate bound, uniformity near \(c=0\) or \(c=\infty\), or a theorem for biased move-to-front chains. The proof is a mathematical derivation; code checks only finite cases. Older general multivariate shuffle results might provide another route to the same asymptotic law, although the inspected sources do not state it for this chain.

## References

[1] Alexander Clay, *On the statistics of random-to-top shuffles*, arXiv:2603.09008v1, first submitted March 9, 2026. https://arxiv.org/html/2603.09008v1

[2] I. Weiss, *Limiting distributions in some occupancy problems*, *Annals of Mathematical Statistics* **29** (1958), 878–884 (occupancy central limit theorem, cited and used in [1]).

[3] Philip Dörr and Johannes Heiny, *Joint extremes of inversions and descents of random permutations*, arXiv:2309.17314v2. https://arxiv.org/html/2309.17314v2

[4] Ümit Işlak, *Descent-inversion statistics in riffle shuffles*, arXiv:1303.2387. https://arxiv.org/abs/1303.2387
