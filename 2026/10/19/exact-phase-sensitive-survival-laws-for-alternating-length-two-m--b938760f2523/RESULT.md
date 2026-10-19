# Exact phase-sensitive survival laws for alternating length-two Markov holes

## Finding

**Theorem (complete alternating-hole law).** Fix any integer \(k\ge 2\), and consider the expanding map \(T_k(x)=kx\bmod 1\) with Lebesgue initial distribution on \([0,1)\). At even observation times remove the length-two \(k\)-adic cylinder with digit word \(pq\); at odd observation times remove the cylinder with digit word \(rs\), where \(p,q,r,s\in\{0,\ldots,k-1\}\). Define the two temporal overlap indicators
\[
 d=\mathbf 1_{\{q=r\}},\qquad e=\mathbf 1_{\{p=s\}},\qquad U=k^2-2.
\]
Let \(S_n\) be the Lebesgue probability of avoiding all prescribed holes at times \(0,\ldots,n-1\). Put \(N_m=k^{2m+1}S_{2m}\) for integers \(m\ge0\), and \(G_{d,e}(z)=\sum_{m\ge0}N_m z^m\). Then \(G_{d,e}\) is determined *only* by \((d,e)\) and has the following exact four-case form:
\[
\begin{aligned}
G_{0,0}(z)&=\frac{k}{1-Uz+z^2},\\
G_{0,1}(z)&=\frac{k}{1-Uz-(k-1)z^2},\\
G_{1,0}(z)&=\frac{k+z}{1-Uz-(k-1)z^2},\\
G_{1,1}(z)&=\frac{k-(k-1)z}{1-(U+1)z+(k-1)^2z^2}.
\end{aligned}
\]
For every \(m\ge2\), there is a **strict, universal finite-horizon ordering**
\[
N_m^{0,0}<N_m^{0,1}<N_m^{1,0}<N_m^{1,1}.
\]
At \(m=1\), the first two values agree and the last two agree, with \(N_1^{0,0}=N_1^{0,1}=k^3-2k\) and \(N_1^{1,0}=N_1^{1,1}=k^3-2k+1\). The central inequality gives an exact *starting-phase effect*: interchanging the two holes exchanges \((0,1)\) and \((1,0)\), preserves their exponential escape rate, but strictly changes every positive even-horizon survival count. Indeed,
\[
\sum_{m\ge0}\bigl(N_m^{1,0}-N_m^{0,1}\bigr)z^m
=\frac{z}{1-Uz-(k-1)z^2}.
\]

The limit \(\gamma=-\lim_{n\to\infty}n^{-1}\log S_n\) exists for all word choices. It takes **exactly three values** as the hole pair varies:
\[
\begin{gathered}
\gamma_{0,0}=\log k-\tfrac12\log\lambda_0,\quad
\gamma_{0,1}=\gamma_{1,0}=\log k-\tfrac12\log\lambda_M,\quad
\gamma_{1,1}=\log k-\tfrac12\log\lambda_H,\\
\lambda_0=\frac{U+\sqrt{U^2-4}}2,\quad
\lambda_M=\frac{U+\sqrt{U^2+4(k-1)}}2,\quad
\lambda_H=\frac{U+1+\sqrt{(U+1)^2-4(k-1)^2}}2,\\
\lambda_0<\lambda_M<\lambda_H,\qquad
\gamma_{0,0}>\gamma_{0,1}=\gamma_{1,0}>\gamma_{1,1}.
\end{gathered}
\]
Among the \(k^4\) equally weighted ordered hole pairs, the fast, intermediate, and slow escape classes occur respectively \(k^2(k-1)^2\), \(2k^2(k-1)\), and \(k^2\) times. At the binary endpoint \(k=2\), the fastest class has the exceptional **exact polynomial prefactor**
\[
S_{2m}=\frac{m+1}{4^m}\quad(m\ge0),\qquad \gamma_{0,0}=\log 2,
\]
whereas every other case has a simple leading spectral root and an asymptotically constant exponential prefactor.

## Assumptions and scope

The cylinder for word \(pq\) is \(H_{pq}=[(kp+q)/k^2,(kp+q+1)/k^2)\), and similarly for \(rs\). The time-dependent hole equals \(H_{pq}\) at even times and \(H_{rs}\) at odd times. All probabilities use Lebesgue measure of initial points and regard entry into the current hole as escape *before* applying the next iterate. The half-open cylinder convention makes the symbolic identification precise up to the standard null set of points with two positional expansions. No mixing assumption is imposed on the surviving dynamics; the exceptional binary case is reducible. The result applies to every integer base and every ordered pair of length-two single-cylinder holes, including identical holes.

## Proof

**1. Exact path count.** The base-\(k\) digits of a Lebesgue-random point are independent uniform symbols. Let \(J\) be the \(k\times k\) all-ones matrix, let \(E_{ij}\) be the elementary matrix with one unit in row \(i\) and column \(j\), and set \(A=J-E_{pq}\), \(B=J-E_{rs}\). Allowed successive digit pairs at even and odd positions are precisely the unit entries of \(A\) and \(B\). Hence
\[
N_m=\boldsymbol1^{\mathsf T}(AB)^m\boldsymbol1,\qquad
S_{2m}=k^{-(2m+1)}N_m.
\]
The two-step matrix is
\[
AB=kJ-\boldsymbol1 e_s^{\mathsf T}-e_p\boldsymbol1^{\mathsf T}+d\,e_p e_s^{\mathsf T},
\]
where \(e_j\) is a coordinate unit vector. This preserves the two-dimensional span of \(\boldsymbol1\) and \(e_p\), which contains the right initial vector \(\boldsymbol1\). In the ordered basis \((\boldsymbol1,e_p)\), the restriction has matrix
\[
C=\begin{pmatrix}k&-1\\-1&d\end{pmatrix}
\begin{pmatrix}k&1\\1&e\end{pmatrix}.
\]
Its trace is \(t=k^2-2+de\) and determinant \(\Delta=(kd-1)(ke-1)\). Cayley–Hamilton on that invariant span proves for every \(m\ge0\):
\[
N_{m+2}=tN_{m+1}-\Delta N_m,\qquad
N_0=k,\quad N_1=k^3-2k+d.
\]
Consequently
\[
G_{d,e}(z)=\frac{k+d(1-ke)z}{1-(k^2-2+de)z+(kd-1)(ke-1)z^2}.
\]
Substitution of all four indicator pairs yields the displayed rational functions; no unexamined parameter case remains.

**2. Coefficientwise ordering.** Define
\[
D_0=1-Uz+z^2,\quad D_M=1-Uz-(k-1)z^2,\quad
D_H=1-(U+1)z+(k-1)^2z^2.
\]
Direct subtraction gives the exact identities
\[
G_{0,1}-G_{0,0}=\frac{k^2z^2}{D_0D_M},\qquad
G_{1,0}-G_{0,1}=\frac{z}{D_M},\qquad
G_{1,1}-G_{1,0}=\frac{(k-1)^2z^2}{D_MD_H}.
\]
Every coefficient in the power series of each reciprocal denominator is strictly positive: for \(D_0\), use its nonnegative real characteristic roots (double root \(1\) only when \(k=2\)); for \(D_M\), use its recurrence with positive coefficients \(U\) and \(k-1\); for \(D_H\), use its two positive real characteristic roots. Thus all differences have positive coefficients at their first possible degree and thereafter, giving the sharp ordering and the starting-phase formula.

**3. Escape spectrum and all time horizons.** The leading characteristic roots of \(D_0,D_M,D_H\) are \(\lambda_0,\lambda_M,\lambda_H\). For \(k\ge3\), \(AB\) has strictly positive entries (each is at least \(k-2\)); at \(k=2\), all noncritical cases have a simple dominating positive eigenvalue. The associated leading coefficient in \(N_m\) is positive, so \(m^{-1}\log N_m\) converges to the logarithm of that root. In the sole double-root case \(k=2,d=e=0\), one has \(G_{0,0}=2/(1-z)^2\), whence \(N_m=2(m+1)\) and the same logarithmic limit with root \(1\).

The inequalities \(\lambda_0<\lambda_M\) follow since \(D_0\) and \(D_M\) share trace \(U\) but the second polynomial has strictly smaller constant product. Moreover \(\lambda_M>U\ge k(k-1)\). Writing \(P_H(X)=X^2-(U+1)X+(k-1)^2\), the relation \(\lambda_M^2=U\lambda_M+(k-1)\) implies
\[
P_H(\lambda_M)=k(k-1)-\lambda_M<0,
\]
so \(\lambda_H>\lambda_M\). Finally, after \(2m\) visits, the next forbidden two-digit word deletes at most one of the \(k\) equally likely continuations. Hence
\[
\frac{k-1}{k}S_{2m}\le S_{2m+1}\le S_{2m}.
\]
Both parity subsequences therefore have the same per-iterate exponential rate, giving the stated \(\gamma\).

**4. Number of configurations.** The conditions \(q=r\) and \(p=s\) are independent for a uniformly selected quadruple of digits. There are \(k^2\), \(k^2(k-1)\), \(k^2(k-1)\), and \(k^2(k-1)^2\) configurations with \((d,e)=(1,1),(1,0),(0,1),(0,0)\), respectively. Grouping by the three spectral values gives the distribution.

## Verification

Run `python3 verify.py`. The standalone standard-library checker exhaustively compares the exact recurrence with integer transition-matrix counts for every ordered hole pair and bases \(2\) through \(6\), independently enumerates finite digit strings for representative cases and all binary pairs, confirms the strict finite-horizon ordering, checks the starting-phase difference, and tests the binary double-root law. Successful output is `VERIFY_OK`. These finite checks corroborate but are not substituted for the general proof above.

## Relationship to prior work

Livorati, Georgiou, Dettmann and Leonel study time-periodically moving holes in the doubling map, reporting numerical Ulam escape rates and overlap-based analytical approximations. Their moving boundaries are sinusoidal, not the arbitrary ordered pair of exact Markov cylinders considered here; their formulas do not provide this complete four-type finite-time law or the binary polynomial prefactor. Georgiou, Dettmann and Altmann give exact spectral and periodic-orbit methods for *static* Markov holes. Cheriyath and Agarwal derive generating-function and escape-rate methods for shift spaces with a *fixed* union of forbidden-word cylinders. The present time-alternating experiment is different from forbidding both words at every time: for example, static exclusion of both binary words \(00\) and \(11\) leaves only two alternating sequences, whereas alternating the two holes has \(2(m+1)\) allowed length-\(2m+1\) words. Generic transfer-matrix methodology motivates the proof, but the all-base three-rate classification, strict phase-sensitive finite-horizon hierarchy, and endpoint correction require the explicit rank-two calculation above.

## Limitations

The holes have exactly one forbidden word of length two in each temporal phase and the underlying map is a full integer-branch expansion; the theorem makes no claim for arbitrary hole shapes, longer words, nonuniform digit measures, or nonperiodic schedules. The comparisons described above do not rule out unlocated equivalent formulations in the wider symbolic-dynamics literature. The proof establishes exact ensemble survival probabilities and rates, not a universal conditional invariant measure or an escape law for every deterministic initial point. No independent audit has been performed.

## References

1. A. L. P. Livorati, O. Georgiou, C. P. Dettmann and E. D. Leonel, “Escape through a time-dependent hole in the doubling map,” *Physical Review E* 89 (2014), 052913. First arXiv posting 2013-12-25, arXiv:1312.7030. DOI: 10.1103/PhysRevE.89.052913. Full text: https://people.maths.bris.ac.uk/~macpd/brazil/pre14.pdf.
2. O. Georgiou, C. P. Dettmann and E. G. Altmann, “Faster than expected escape for a class of fully chaotic maps,” *Chaos* 22 (2012), 043115. DOI: 10.1063/1.4766723. Full text: https://people.maths.bris.ac.uk/~macpd/georgiou/avesc.pdf.
3. H. Cheriyath and N. Agarwal, “Subshifts of Finite Type with a Hole,” *Journal of the Australian Mathematical Society* 115 (2023), 73–98 (published online 2022). First arXiv posting 2019-05-28, arXiv:1905.11767. Full text: https://arxiv.org/pdf/1905.11767.
