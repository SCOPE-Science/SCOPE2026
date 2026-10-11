# Exact one-jump constant in the discrete reverse Hardy–BMO problem

## Finding
For a real sequence \(a=(a_j)_{j\ge1}\), write
\[
\Omega_d(a;[s,t])=\frac{1}{t-s+1}\sum_{j=s}^t|a_j-\overline a_{s,t}|,
\qquad \overline a_{s,t}=\frac{1}{t-s+1}\sum_{j=s}^t a_j,
\]
where \(1\le s\le t<\infty\) are integers, and let \(\|a\|_{\mathrm{BMO}_d}=\sup_{s\le t}\Omega_d(a;[s,t])\). Define \((Ca)_j=j^{-1}\sum_{i=1}^j a_i\). For each integer \(m\ge1\), put \(e^{(m)}_j=1\) for \(1\le j\le m\) and \(e^{(m)}_j=0\) otherwise.

**The discrete one-jump benchmark has an exact, attained, unique minimum:**
\[
\boxed{\inf_{m\ge1}\frac{\|Ce^{(m)}\|_{\mathrm{BMO}_d}}{\|e^{(m)}\|_{\mathrm{BMO}_d}}=\frac{3371}{6720},
\qquad\text{with equality exactly when }m=2.}
\]
Indeed, \(\|e^{(m)}\|_{\mathrm{BMO}_d}=1/2\) for every \(m\), and \(\|Ce^{(2)}\|_{\mathrm{BMO}_d}=3371/13440\), attained on the interval \([1,8]\). This evaluates the scalar benchmark \(\alpha_d\) defined in Section 5.1 of Caldera's 2026 paper. It does **not** establish Caldera's conjectured lower bound for every nonincreasing sequence.

## Assumptions and scope
Sequences are indexed by positive integers; intervals are arbitrary finite consecutive blocks, not only initial blocks. The seminorm uses the mean absolute deviation from the *arithmetic interval mean*, not median oscillation or quadratic variance. All assertions are exact over the rational numbers except two elementary rationally bounded logarithms. The minimization is over every positive integer jump location, with no finite-length cutoff in its statement.

## Proof
**1. Denominator.** Since \(0\le e^{(m)}_j\le1\), mean absolute deviation on any interval is at most \(1/2\). The interval \([1,2m]\) has equal numbers of ones and zeros, so \(\|e^{(m)}\|_{\mathrm{BMO}_d}=1/2\).

**2. Exact numerator for the two-jump-length indicator.** Write \(b=Ce^{(2)}\). Thus \(b_1=b_2=1\), and \(b_j=2/j\) for \(j\ge3\). If a block starts at \(s\ge4\), its entries lie in \([0,1/2]\); its mean absolute deviation is at most \(1/4\), by the elementary inequality \(\mathbb E|X-\mathbb EX|\le (\max X-\min X)/2\).

If a block starts at \(s\in\{1,2,3\}\) and ends at \(t\ge128\), its mean is at most \(2H_t/(t-2)\), where \(H_t=\sum_{j=1}^t1/j\). Nonnegativity gives
\[
\Omega_d(b;[s,t])\le\frac{4H_t}{t-2}\le\frac{4(1+\log t)}{t-2}
\le\frac{4(1+\log128)}{126}<\frac4{21}<\frac14.
\]
Here \((1+\log x)/(x-2)\) decreases for \(x>2\), and \(\log128<5\), as the first eight positive terms of the series for \(e^5\) already sum to more than \(128\).

Thus only \(s=1,2,3\), \(s\le t\le127\) can exceed \(1/4\). Direct rational arithmetic, exhaustively certified by `verify_discrete_bmo.py`, gives their respective maximum mean absolute deviations
\[
\begin{array}{c|ccc}s&1&2&3\\\hline
\max_{s\le t\le127}\Omega_d(b;[s,t])&3371/13440&76/375&1663/13440\\
\text{maximizing }t&8&6&10\end{array}.
\]
In particular the global supremum is \(3371/13440>1/4\). At \([1,8]\) the mean is \(621/1120\), which also directly gives the claimed rational oscillation.

**3. All other jump locations.** For \(m=1\), the interval \([1,3]\) gives the ratio \(\|Ce^{(1)}\|/\|e^{(1)}\|\ge14/27>3371/6720\). Now suppose \(m\ge3\), set \(N=4m\), \(k=\lfloor5m/3\rfloor\), and \(h_j=\min(1,m/j)\). The mean of \(h_1,\ldots,h_N\) is \(\mu=(1+H_{4m}-H_m)/4\). Since the deviations sum to zero,
\[
\sum_{j=1}^N|h_j-\mu|\ge2\sum_{j=1}^{k}(h_j-\mu).
\]
Consequently,
\[
\frac{\|Ce^{(m)}\|_{\mathrm{BMO}_d}}{\|e^{(m)}\|_{\mathrm{BMO}_d}}
\ge L_m:=1+H_k-H_m-\frac{k}{4m}(1+H_{4m}-H_m).
\]
For the finite, explicitly bounded range \(3\le m\le199\), the standalone exact-rational certificate checks \(L_m\ge167723/332640>3371/6720\), with the smallest witness at \(m=3\). This is an exhaustive finite comparison, not an inference from numerical experiments.

For every \(m\ge200\), the integral comparison for harmonic numbers gives
\[
H_k-H_m\ge\log(k/m)-1/m,\quad H_{4m}-H_m\le\log4,
\quad 997/600\le k/m\le5/3.
\]
The rationally certified logarithm bounds \(\log(997/600)>507/1000\) and \(\log4<1387/1000\) imply
\[
L_m>1+\frac{507}{1000}-\frac1{200}
-\frac5{12}\left(1+\frac{1387}{1000}\right)
=\frac{6089}{12000}>\frac{3371}{6720}.
\]
For reproducibility, the logarithm bounds follow from the convergent positive series
\[\log\frac{1+y}{1-y}=2\sum_{j=0}^\infty\frac{y^{2j+1}}{2j+1},\quad0<y<1,\]
using the first two terms as a lower bound with \(y=397/1597\), and seven terms plus the geometric remainder \(2y^{15}/(15(1-y^2))\) as an upper bound with \(y=3/5\). The certificate verifies those inequalities with exact rational arithmetic. Every \(m\ne2\) is therefore strictly worse.

## Verification
Run `python3 verify_discrete_bmo.py` using Python 3's standard library. The program exactly enumerates all necessary short blocks for \(m=2\), all \(3\le m\le199\) for the explicitly proved lower witness, and verifies the two rational bounds that close the infinite tail. Its successful terminal message is `ONE_JUMP_DISCRETE_BMO_EXACT_CERTIFICATES_OK`. The proof independently establishes why these are the *only* finite cases requiring enumeration.

## Relationship to prior work
Caldera, arXiv:2608.08093v1 (first public August 8, 2026), proves a sharp reverse Hardy–BMO inequality for nonincreasing functions on the half-line. Section 5.1 (especially equations (74)–(75) and Conjecture 1) **defines** the discrete one-jump benchmark \(\alpha_d=\inf_{m\ge1}\|Ce^{(m)}\|_{\mathrm{BMO}_d}/\|e^{(m)}\|_{\mathrm{BMO}_d}\), obtains a nonsharp discrete global lower constant \(\alpha_0/8\), and conjectures that \(\alpha_d\) is the optimal constant over *all* nonincreasing sequences. It does not compute \(\alpha_d\) or identify the optimal jump location. The present result evaluates precisely that existing natural benchmark. Earlier work on the Cesàro-minus-identity operator in \(\ell^p\) addresses a different norm and operator; it does not imply this BMO numerical value.

## Limitations
No inequality with constant \(3371/6720\) is proved for arbitrary nonincreasing sequences; the discrete conjecture remains unresolved here. The only objects optimized are the one-jump sequences \(e^{(m)}\). The finite rational certificate is part of the proof of a global assertion because explicit analytic estimates dispose of all excluded indices and intervals; the certificate is not a substitute for those tail arguments. Novelty conclusions remain subject to discovery of independent, unindexed analyses of the same benchmark.

## References
1. A. Caldera, *The Sharp Reverse Hardy Inequality in BMO for Nonincreasing Functions*, arXiv:2608.08093v1, August 8, 2026, especially §5.1, equations (67)–(75). https://arxiv.org/html/2608.08093v1
2. A. Ben Said, S. Boza, J. Soria, *The norm of Hardy-Type oscillation operators in the discrete and continuous settings*, *Analysis and Applications*, first published November 18, 2025, DOI:10.1142/S0219530526500168.
3. A. Ben Said, S. Boza, J. Soria, *On sharp reverse Hardy-type inequalities for oscillation operators in the discrete and continuous settings*, *Rendiconti del Circolo Matematico di Palermo* 75 (2026), article 143, DOI:10.1007/s12215-026-01455-1.
