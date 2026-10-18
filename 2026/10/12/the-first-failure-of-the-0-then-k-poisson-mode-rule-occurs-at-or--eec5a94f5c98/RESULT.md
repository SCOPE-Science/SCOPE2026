# An exact certificate for the first order-fifteen Poisson modal departure

## Finding
Let \(N_1,\ldots,N_k\) be independent Poisson random variables of common real intensity \(\lambda>0\), and set \(X_{k,\lambda}=\sum_{j=1}^k jN_j\). For each integer \(2\le k\le15\), the smallest positive \(\lambda\) at which zero ceases to be the unique global mode is a single threshold \(\tau_k\). At \(\tau_k\) there are exactly two global modes:
\[
\operatorname*{arg\,max}_{n\ge0}\Pr(X_{k,\tau_k}=n)
=\begin{cases}\{0,k\},&2\le k\le14,\\\{0,25\},&k=15.\end{cases}
\]
Immediately below \(\tau_k\), zero is the unique mode; on a nonempty interval immediately above it, the indicated positive index is the unique mode. In particular
\[
\frac{250227}{10^6}<\tau_{15}<\frac{250228}{10^6}.
\]
All assertions concern **global** modes over the entire infinite nonnegative integer support and **all real** intensities in the relevant intervals, not a truncated numerical scan. No assertion is made for \(k\ge16\) or for later modal transitions.

**Priority distinction.** The order-fifteen switch to index 25 was already observed numerically, explicitly and approximately, by S. R. Mane in *Asymptotic results for the Poisson distribution of order k* (arXiv:2309.05190, 2023), and repeated in *First double mode of the Poisson distribution of order k* (arXiv:2309.09278, 2023). These prior computations correctly identify the same smallest exceptional order and competing index; they were explicitly described as numerical findings, with proof left open. The contribution here is **an exact, auditable rational certificate together with an analytic bound for every unexamined tail index**, proving the numerical finding and excluding any third tied mode for every order \(2\le k\le15\). The numerical observation itself is not claimed as new.

## Coefficients, thresholds, and exact brackets
Define
\[
a_{k,n}(\lambda)=[z^n]\exp\Bigl(\lambda\sum_{j=1}^kz^j\Bigr).
\]
Then \(\Pr(X_{k,\lambda}=n)=e^{-k\lambda}a_{k,n}(\lambda)\), \(a_{k,0}=1\), and
\[
na_{k,n}(\lambda)=\lambda\sum_{j=1}^{\min(k,n)}j\,a_{k,n-j}(\lambda).
\]
For \(n\ge1\) each \(a_{k,n}\) is a polynomial with nonnegative coefficients, positive for some nonconstant powers, and zero constant term; it is continuous and strictly increasing from zero to infinity on \(\lambda>0\). Thus each equation \(a_{k,n}(\lambda)=1\) has one and only one positive root.

For each \(k\), put \(j_k=k\) for \(k\le14\), and \(j_{15}=25\). The first transition is the unique positive root of \(a_{k,j_k}(\tau_k)=1\). Every root lies in the following strict rational bracket \((q_k-1)/10^6<\tau_k<q_k/10^6\):

| \(k\) | \(q_k\) | \(j_k\) |
|---:|---:|---:|
|2|732051|2|
|3|601680|3|
|4|520352|4|
|5|463330|5|
|6|420487|6|
|7|386782|7|
|8|359378|8|
|9|336537|9|
|10|317127|10|
|11|300374|11|
|12|285728|12|
|13|272786|13|
|14|261245|14|
|15|250228|25|

## Proof and verification
For each row, put \(L_k=(q_k-1)/10^6\) and \(B_k=q_k/10^6\). The included standalone standard-library Python program `verify.py` checks the rational recurrence directly in `fractions.Fraction`. It verifies exactly, for every \(2\le k\le15\),
\[
a_{k,j_k}(L_k)<1<a_{k,j_k}(B_k),\qquad
\max_{1\le n\le40k,\;n\ne j_k}a_{k,n}(B_k)<1,\qquad kB_k<4.
\]
Each comparison is between rational numbers, not rounded floating-point values. Independent exact-rational recomputation of all 14 sets of strict inequalities confirmed these assertions; for \(k=15\) the strongest alternate index at the upper endpoint is \(n=26\), with a positive gap of approximately \(0.000528\).

The finite prefix is sufficient because it is paired with an analytic **infinite-tail bound**. Let \(M\sim\operatorname{Poisson}(k\lambda)\). Conditional on \(M=m\), the order-k Poisson variable is the sum of \(m\) independent uniform variables on \(\{1,\ldots,k\}\). Thus for \(n>40k\), at \(\lambda=B_k\), the normalized coefficient obeys
\[
a_{k,n}(B_k)
\le\sum_{m\ge41}\frac{(kB_k)^m}{m!}
<\sum_{m\ge41}\frac{4^m}{m!}
\le\frac{2\cdot4^{41}}{41!}<1.
\]
The penultimate bound follows from the ratio of successive summands being at most \(4/42\); the final comparison is an exact integer inequality. Hence **every** competitor, including every index beyond \(40k\), is strictly below one at \(B_k\).

By monotonicity, all competitors other than \(j_k\) remain strictly below one for all \(0<\lambda\le B_k\). The target coefficient crosses one once at \(\tau_k\in(L_k,B_k)\). Since \(a_{k,0}=1\), this proves uniqueness of the zero mode below, exactly two modes \(0,j_k\) at, and uniqueness of the positive mode above the boundary up to \(B_k\). No finite enumeration is extrapolated without the proved tail estimate.

## Relationship to prior work
Philippou's 2014 note (arXiv:1312.7139) proves an initial mode-zero sufficient interval and solves order two. Georghiou, Philippou, and Saghafi (arXiv:1204.3186; Fibonacci Quarterly 2013) derive mode-location inequalities and results in low orders. Kwon and Philippou (Entropy 2023, DOI 10.3390/e25040699) prove modal regimes for orders three and four and formulate related questions. Those results do not prove the complete order-two-through-fifteen first-transition classification.

Most directly, Mane's 2023 paper arXiv:2309.05190 explicitly reports from **numerical calculations** that the first double mode is \(0,k\) through \(k=14\) but \(0,25\) at \(k=15\), around \(\lambda\approx0.25023\). His follow-up arXiv:2309.09278 discusses the same first double mode, proves several bounds and monotonicity results, and gives a numerical table implying \(\hat m_{15}=25\). It does **not** provide an exact rational global certificate, rigorous millionth brackets, or the simultaneous proof excluding third ties at these 14 boundaries. In fact it explicitly leaves open the general existence of triple modes. Therefore the reported mode index and exceptional order are **known numerical findings**, while their fully rigorous finite-order certification and tie exclusion are the narrower contribution here. A later or unindexed rigorous certificate could still supersede it.

## Limitations
The theorem concerns only first transitions for the fourteen orders \(k=2,\ldots,15\), not the full modality phase diagram, higher orders, or non-first triple modes. The program's finite inequalities are exact, but the infinite-support statement also requires the analytic Poisson tail bound and monotonicity argument printed above. The earlier 2023 numerical discovery must be credited; this finding does not independently discover the index 25 or the first exceptional order.

## References
1. S. R. Mane, *Asymptotic results for the Poisson distribution of order k*, arXiv:2309.05190 (2023), especially Section 4 and Figure 2.
2. S. R. Mane, *First double mode of the Poisson distribution of order k*, arXiv:2309.09278 (2023), especially Sections 4–6 and Tables 1–2.
3. Y. Kwon and A. N. Philippou, *The Modes of the Poisson Distribution of Order 3 and 4*, Entropy **25** (2023), 699, DOI: 10.3390/e25040699.
4. C. Georghiou, A. N. Philippou, and A. Saghafi, *On the modes of the Poisson distribution of order k*, Fibonacci Quarterly **51** (2013), 44–48, arXiv:1204.3186.
5. A. N. Philippou, *A note on the modes of the Poisson distribution of order k*, Fibonacci Quarterly **52** (2014), 203–205, arXiv:1312.7139.
