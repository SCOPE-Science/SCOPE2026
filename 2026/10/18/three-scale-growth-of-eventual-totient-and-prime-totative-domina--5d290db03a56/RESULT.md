# Three-scale growth of eventual totient and prime-totative dominance thresholds

## Finding
For each integer \(k\ge1\), let
\[N_k=\min\{N\ge2:\varphi(n)>k\pi(n)\text{ for every integer }n\ge N\}.\]
Write \(\omega(n)\) for the number of distinct prime factors and define
\[A(n)=\pi(n)-\omega(n),\qquad B(n)=\varphi(n)-\pi(n)+\omega(n).\]
Let \(M_k\) be the analogous least threshold such that \(B(n)>kA(n)\) for every \(n\ge M_k\). Then, with \(\gamma\) the Euler--Mascheroni constant,
\[\boxed{\log N_k=\mathrm e^\gamma k\bigl(\log k+\log\log k+\gamma+o(1)\bigr),}\]
\[\boxed{\log M_k=\mathrm e^\gamma k\bigl(\log k+\log\log k+\gamma+o(1)\bigr).}\]
The errors are \(o(k)\) in the logarithms of the thresholds; thus all three displayed scales \(k\log k\), \(k\log\log k\), and \(k\) have determined coefficients. Consequently \(\log M_{k-1}-\log N_k=o(k)\), but equality of the two integer thresholds is not asserted.

## Assumptions and scope
All logarithms are natural. The variable \(n\) ranges over positive integers, \(k\) tends to infinity through positive integers, and \(\pi(n)\), \(\varphi(n)\), \(\omega(n)\) are the standard prime-counting, Euler totient, and distinct-prime-factor functions. The existence and finiteness of the minima follow from the uniform lower bound proved below. No hypothesis such as the Riemann hypothesis is used.

## Proof
Put \(y=\log n\), \(L=\log y\), and \(c=\mathrm e^\gamma\). Define \(F(n)=\varphi(n)/\pi(n)\) for \(n\ge2\). We first prove two complementary asymptotic estimates, uniform for all sufficiently large integers in the first case and along primorials in the second:
\[F(n)\ge \frac{y}{cL}\bigl(1-O(L^{-2})\bigr),\tag{1}\]
\[F(P_t)=\frac{\log P_t}{c\log\log P_t}\bigl(1+o((\log\log P_t)^{-2})\bigr),\quad P_t=\prod_{j=1}^t p_j.\tag{2}\]
For (1), Rosser--Schoenfeld's explicit classical bound gives, for sufficiently large \(n\),
\[\frac n{\varphi(n)}\le c\log\log n+\frac{2.50637}{\log\log n}.\]
The prime number theorem with its classical quantitative remainder yields \(n/\pi(n)=y(1+O(y^{-1}))\). Combining these and expanding the reciprocal of \(cL+O(L^{-1})\) proves (1).

For (2), take the primorial \(P_t\), let \(z=p_t\), and note that \(\log P_t=\vartheta(z)\), the Chebyshev prime sum. The effective prime number theorem gives \(\vartheta(z)=z(1+O(\exp(-c_0\sqrt{\log z})))\) for some \(c_0>0\). The effective Mertens product estimate likewise gives
\[\prod_{p\le z}\left(1-\frac1p\right)=\frac{\mathrm e^{-\gamma}}{\log z}\bigl(1+O(\exp(-c_1\sqrt{\log z}))\bigr)\]
for some \(c_1>0\). Hence \(\log z=\log\log P_t+O(\exp(-c_2\sqrt{\log z}))\), and the prime number theorem at \(P_t\) gives (2). Every negative power of \(\log\log P_t\) dominates the displayed exponentially small error.

Next the two ratios relevant to the thresholds differ only by an additive unit and a negligible error. Indeed \(0\le\omega(n)\le y/\log2\), while \(\pi(n)\gg \mathrm e^y/y\); therefore, uniformly as \(n\to\infty\),
\[G(n):=\frac{B(n)}{A(n)}=F(n)-1+O(y^3\mathrm e^{-y})=F(n)-1+o(1).\tag{3}\]
Both denominators are positive for large \(n\). Thus (1)--(2) apply also to \(G(n)\) up to an additive error of \(-1+o(1)\).

Fix an arbitrary \(\varepsilon>0\). For large positive integers \(k\) set
\[Y_{\pm}=ck\bigl(\log k+\log\log k+\gamma\pm\varepsilon\bigr).\]
Elementary logarithmic expansion gives
\[\log Y_{\pm}=\log k+\log\log k+\gamma+O\!\left(\frac{\log\log k}{\log k}\right)\]
and hence
\[\frac{Y_{\pm}}{c\log Y_{\pm}}=k\left(1\pm\frac{\varepsilon}{\log k}+O\!\left(\frac{\log\log k}{(\log k)^2}\right)\right).\tag{4}\]
The error in the lower bound (1) contributes only \(O(k/(\log k)^2)\), which is smaller than the definite \(\varepsilon k/\log k\) gap in (4). Moreover \(y/\log y\) is increasing when \(y>\mathrm e\), and the error bound in (1) is uniform. Consequently, for all sufficiently large \(k\), every integer \(n\ge\exp(Y_+)\) satisfies \(F(n)>k\) and, by (3), \(G(n)>k\). Thus
\[\log N_k\le Y_++o(1),\qquad\log M_k\le Y_++o(1).\tag{5}\]

For the matching lower bound, choose the least primorial \(P_t\) with \(\log P_t\ge Y_-\). Since consecutive logarithms of primorials differ by \(\log p_{t+1}=O(\log Y_-)\) by the prime number theorem, this choice has
\[\log P_t=Y_-+O(\log Y_-)=Y_-+o(k).\]
Using (2) and the minus case of (4), we obtain \(F(P_t)<k\) for large \(k\); equation (3) also yields \(G(P_t)<k\). Each inequality provides an actual failure of the corresponding strict eventual dominance. Thus \(N_k>P_t\) and \(M_k>P_t\), giving
\[\log N_k\ge Y_-,\qquad\log M_k\ge Y_-.\tag{6}\]
Since \(\varepsilon>0\) was arbitrary, (5)--(6) prove the two boxed asymptotics. Replacing \(k\) by \(k-1\) in the second formula changes the expansion by \(o(k)\), giving the final comparison.

## Verification
The result is an analytic theorem, not a finite enumeration. The proof isolates all three normalized scales and uses a uniform totient bound for the upper threshold brackets and explicit primorial failures for the lower brackets. A standalone standard-library numerical check evaluates the elementary inversion brackets only; it does not establish the infinite statement.

## Relationship to prior work
Fatehizadeh (2026) introduced the two exact eventual threshold sequences, computed their first values, established the general inequality \(M_k\le N_{k+1}\), and conjectured equality. A subsequent published determination extends the exact tables to \(N_7\) and \(N_8\). These finite evaluations and the conjectured equality concern individual integer thresholds; the present claim instead determines the sharp three-scale asymptotic location as the level \(k\) grows. Classical Landau/Mertens theory supplies the main extremal scale, but the coefficient of the \(k\)-term requires retaining a quantitatively small error before inverting the threshold relation.

## Limitations
The asymptotics do not determine exact values of \(N_k\) or \(M_k\), do not prove the conjecture \(M_k=N_{k+1}\), and do not control fluctuations finer than \(o(k)\) in their logarithms. The proof relies on classical quantitative prime number theory and the Rosser--Schoenfeld totient estimate. Priority over unindexed earlier deductions cannot be established by search alone.

## References
1. A. Fatehizadeh, *Prime and Nonprime Totatives: A Sharp Construction and Exact Thresholds*, arXiv:2609.13852v1 (first posted 12 September 2026), https://arxiv.org/abs/2609.13852.
2. J. B. Rosser and L. Schoenfeld, *Approximate formulas for some functions of prime numbers*, Illinois J. Math. 6 (1962), 64--94, https://doi.org/10.1215/ijm/1255631807.
3. F. Mertens, *Ein Beitrag zur analytischen Zahlentheorie*, J. reine angew. Math. 78 (1874), 46--62. Effective refinements follow from the classical prime number theorem with a zero-free-region error term.
4. *Exact seventh and eighth totient-prime thresholds*, public mathematical result (2026), publicly accessible mathematical result, 2026.
