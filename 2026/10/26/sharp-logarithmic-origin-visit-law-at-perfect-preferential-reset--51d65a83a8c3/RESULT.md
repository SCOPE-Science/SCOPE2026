# Sharp logarithmic origin-visit law at perfect preferential resetting

## Finding
Fix a dimension \(d\ge1\) and an impurity relocation probability \(0<\xi_0<1\). Consider the nearest-neighbor monkey walk started at the origin of \(\mathbb Z^d\), which at each step relocates to a uniformly sampled earlier position with probability \(\xi_0\) when currently at the origin and with probability exactly one when currently away from the origin. With the remaining probability at the origin, it takes an independent symmetric nearest-neighbor step. Put \(p=1-\xi_0\), let \(W_n\) be its position after \(n\) transitions, and set
\[
C_n=\sum_{k=0}^{n}\mathbf1_{\{W_k=0\}},\qquad Q_n=\frac{n+1}{C_n}.
\]
Then there is an almost surely finite real random variable \(L\) such that
\[
\boxed{Q_n-p\log C_n\longrightarrow L\quad\text{almost surely}.}
\]
Equivalently,
\[
\boxed{Q_n-p\log(n+1)+p\log\log(n+1)
\longrightarrow L-p\log p\quad\text{almost surely}.}
\]
In particular,
\[
\boxed{\frac{C_n\log(n+1)}{n+1}\longrightarrow\frac1p\quad\text{almost surely}.}
\]
The logarithmic and logarithm-of-logarithm coefficients are independent of spatial dimension. The additive random offset is not claimed to have a known law or to be nondegenerate.

## Assumptions and scope
At time \(n\), the walker is at \(W_n\) and a relocation chooses an index uniformly from \(\{0,\ldots,n\}\), including the present index. Independent increments from the origin choose uniformly among the \(2d\) nearest neighbors, none equal to the origin. The process starts at \(W_0=0\); \(0<\xi_0<1\) is fixed; the away-from-origin relocation probability is exactly one. All limits are along positive integers \(n\to\infty\). This is a boundary-parameter result, not a uniform statement as the off-origin relocation probability approaches one.

## Proof
Write \(J_n=\mathbf1_{\{W_n=0\}}\), \(t=n+1\), \(C=C_n\), \(a_n=C_n/(n+1)\), and let \(\mathcal F_n\) be the natural past. Because a nonrelocation jump from the origin cannot return immediately to the origin, and because every step away from the origin is a uniform-history relocation,
\[
q_n:=\Pr(J_{n+1}=1\mid\mathcal F_n)
=\frac{C_n}{n+1}(1-pJ_n),\qquad C_{n+1}=C_n+J_{n+1}.\tag{1}
\]
This identity eliminates the spatial coordinates and is exact in every dimension.

**Step 1: the empirical origin fraction vanishes.** Taking conditional expectations in the count recursion gives
\[
\mathbb E(a_{n+1}-a_n\mid\mathcal F_n)
=-\frac{p a_nJ_n}{n+2}.\tag{2}
\]
Thus \((a_n)\) is a bounded nonnegative supermartingale, converging almost surely to some \(a_\infty\). The centered differences in (2) are bounded in absolute value by \(1/(n+2)\), so their martingale series converges almost surely. Summing (2) therefore shows that \(\sum_n a_nJ_n/(n+2)<\infty\) almost surely. On \(\{a_\infty>0\}\), however, \(C_n/(n+1)\to a_\infty\) and discrete summation by parts yields \(\sum_{k<n}J_k/(k+2)\sim a_\infty\log n\), contradicting that finiteness. Hence \(a_n\to0\) almost surely.

**Step 2: polynomial growth, then near-linear growth, of origin visits.** Put \(h(c)=\log(1+1/c)\). The increment \(\log C_{n+1}-\log C_n=J_{n+1}h(C_n)\) has predictable mean \(q_nh(C_n)\). Since \(c h(c)\ge\log2\) for every integer \(c\ge1\), and \(1-pJ_n\ge\xi_0\), the predictable mean is at least \(\xi_0\log2/(n+1)\). Its centered martingale difference has conditional variance at most
\[
q_nh(C_n)^2\le\frac1{(n+1)C_n}\le\frac1{n+1}.
\]
The series obtained by dividing these martingale differences by \(\log(n+3)\) has summable conditional variances. Martingale convergence and Kronecker's lemma show that the unweighted martingale is \(o(\log n)\) almost surely. Therefore \(\liminf\log C_n/\log n\ge\xi_0\log2>0\), implying that \(C_n\ge n^\eta\) eventually almost surely for some fixed \(\eta>0\).

Now \(c h(c)=1+O(1/c)\), so (1) gives
\[
q_n h(C_n)=\frac{1-pJ_n}{n+1}
+O\left(\frac1{(n+1)C_n}\right).
\]
The error series is absolutely convergent, and the logarithm martingale now has summable conditional variance \(\sum_n1/[(n+1)C_n]<\infty\); hence it converges almost surely. Consequently,
\[
\log C_n=\sum_{k=0}^{n-1}\frac{1-pJ_k}{k+1}+O_\omega(1).
\tag{3}
\]
Here \(O_\omega(1)\) means bounded almost surely, with a bound depending on the sample path. Since \(a_n=C_n/(n+1)\to0\), summation by parts gives \(\sum_{k<n}J_k/(k+1)=o(\log n)\). Applying this to (3) proves \(\log C_n/\log n\to1\), so in particular \(C_n\ge n^{3/4}\) eventually almost surely.

**Step 3: inverse-fraction martingale.** Define \(Q_n=(n+1)/C_n\). The two possible values of \(Q_{n+1}-Q_n\) give the *exact* conditional drift
\[
\mathbb E(Q_{n+1}-Q_n\mid\mathcal F_n)
=\frac{pJ_n}{C_n}+r_n,
\qquad
r_n=\frac{(1-pJ_n)(n+1-C_n)}{(n+1)C_n(C_n+1)}.
\tag{4}
\]
In particular \(0\le r_n\le C_n^{-2}\), so \(\sum_n r_n<\infty\) almost surely by the growth bound in Step 2. The centered increment in (4) has conditional variance bounded by
\[
\frac{4(n+1)}{C_n^3},
\]
which is summable almost surely because \(C_n\ge n^{3/4}\) eventually. The martingale differences therefore have an almost surely convergent sum. Thus, for a finite random \(R\),
\[
Q_n-p\sum_{k=0}^{n-1}\frac{J_k}{C_k}\longrightarrow R.
\tag{5}
\]

**Step 4: harmonic telescoping and the second-order correction.** Since \(C_0=J_0=1\) and \(C_n\) increases exactly at times with \(J_n=1\), the following identity holds for every path:
\[
\sum_{k=0}^{n-1}\frac{J_k}{C_k}
=H_{C_n}-\frac{J_n}{C_n},\qquad H_m=\sum_{j=1}^m\frac1j.
\tag{6}
\]
Step 2 shows \(C_n\to\infty\). Since \(H_m-\log m\to\gamma\) and \(J_n/C_n\to0\), combining (5) and (6) proves \(Q_n-p\log C_n\to L\). Finally \(C_n=(n+1)/Q_n\), so
\[
Q_n+p\log Q_n-p\log(n+1)\to L.\tag{7}
\]
The first limit together with \(\log C_n\sim\log n\) shows \(Q_n\sim p\log n\). Hence \(\log Q_n=\log\log(n+1)+\log p+o(1)\). Substitution in (7) yields the asserted almost-sure logarithm-of-logarithm correction and the leading count law.

## Verification
The standalone Python standard-library file `verify.py` checks the one-step conditional identities in (1), (2), and (4), the conditional variance envelope in Step 3, and an exact finite-state rational recursion for the joint law of \((C_n,J_n)\). Its completed execution returned `EXACT_IDENTITIES_OK 27224` and `EXACT_DISTRIBUTIONS_OK 1521`, followed by a seeded illustrative path. These finite calculations are consistency checks only; the infinite almost-sure conclusions follow from Steps 1–4, not from enumeration or simulation. Run `python3 verify.py` in a Python 3 environment.

## Relationship to prior work
Armfield and Mailler (2026, arXiv:2610.21864) study the same impurity monkey walk and prove localization when the off-origin relocation parameter lies in a sufficiently high **open** interval below one. Their Theorem 1.1 does not include the endpoint with off-origin relocation probability one and does not supply the inverse origin-frequency asymptotic. Boyer, Falcón-Cortés, Giuggioli and Majumdar (2019, arXiv:1902.00817) analyze the model's localization physics and already identify, via a stationary self-consistency calculation, disappearance of origin mass and nearest-neighbor concentration as the relocation parameter *approaches* one. These qualitative endpoint-profile insights are prior work and are not claimed here. Their Section 4 does not establish the pathwise coefficient, harmonic renormalization, or logarithm-of-logarithm term at the exact endpoint. Mailler and Uribe Bravo (2018, arXiv:1810.02735) study position-independent preferential relocation; its regenerative random-tree CLT does not directly give a site-dependent impurity origin-count law. The contribution here is a sharp almost-sure *finite-time visit-frequency* expansion at the singular exact endpoint.

## Limitations
The theorem is restricted to \(0<\xi_0<1\), initialization at the impurity, and off-origin relocation probability exactly one. It does not establish uniformity as that parameter approaches one from below, the law of \(L\), nondegeneracy of \(L\), or fluctuations around the random offset. Earlier physical self-consistency equations identify qualitative related phenomena, and a more general unlocated reinforcement theorem might imply the expansion. No independent mathematical audit has been performed.

## References
1. W. Armfield and C. Mailler, *Localisation of the monkey walk with an “impurity” at the origin*, arXiv:2610.21864, first posted 15 October 2026, https://arxiv.org/abs/2610.21864.
2. D. Boyer, A. Falcón-Cortés, L. Giuggioli, and S. N. Majumdar, *Anderson-like localization transition of random walks with resetting*, J. Stat. Mech. (2019) 053204; arXiv:1902.00817, https://arxiv.org/abs/1902.00817.
3. C. Mailler and G. Uribe Bravo, *Random walks with preferential relocations and fading memory: a study through random recursive trees*, arXiv:1810.02735, https://arxiv.org/abs/1810.02735.
