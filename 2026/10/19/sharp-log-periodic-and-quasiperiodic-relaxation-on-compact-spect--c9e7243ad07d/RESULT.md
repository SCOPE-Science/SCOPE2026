# Sharp log-periodic and quasiperiodic relaxation on compact spectral source balls

## Finding
Let \(\alpha>0\) and \(b>1\). On \(\ell^2(\mathbb N_0)\), define the positive compact diagonal operator \(Q_b e_k=b^{-k}e_k\), its contraction \(T_b=\exp(-Q_b)\), and the compact spectral source ball \(\mathcal K_{b,\alpha}=Q_b^\alpha\{y:\|y\|_2\le1\}\). Set
\[
L_b=\frac{\alpha\log b}{b-1},\qquad
H_{b,\alpha}(t)=(L_b b^t)^\alpha\exp(-L_b b^t),\quad 0\le t\le1.
\]
The two endpoint values of \(H_{b,\alpha}\) agree, so it defines a continuous one-periodic function. For every integer \(n\ge\max\{1,L_b\}\), let \(k_b(n)=\lfloor\log_b(n/L_b)\rfloor\). The **exact** optimal uniform orbit error is
\[
E_{b,\alpha}(n):=\sup_{x\in\mathcal K_{b,\alpha}}\|T_b^n x\|_2
=b^{-\alpha k_b(n)}\exp(-n b^{-k_b(n)})
=n^{-\alpha}H_{b,\alpha}\bigl(\{\log_b(n/L_b)\}\bigr).
\]
In particular, writing \(m_b=L_b^\alpha e^{-L_b}\) and \(M_\alpha=\alpha^\alpha e^{-\alpha}\), the set of all subsequential limits of \(n^\alpha E_{b,\alpha}(n)\) is **exactly** \([m_b,M_\alpha]\), and \(0<m_b<M_\alpha\). Thus the sharp exponent \(\alpha\) is accompanied by a genuine nonconstant log-periodic amplitude; no single limiting normalized decay constant exists.

This result has a sharp two-scale extension. On \(\ell^2(\mathbb N_0)\oplus\ell^2(\mathbb N_0)\), set \(Q=Q_{b_1}\oplus Q_{b_2}\), \(T=e^{-Q}\), and \(\mathcal K=Q^\alpha\{y:\|y\|_2\le1\}\). If \(b_1,b_2>1\) and \(\log b_1/\log b_2\notin\mathbb Q\), then for every sufficiently large integer \(n\),
\[
n^\alpha\sup_{x\in\mathcal K}\|T^n x\|_2
=\max_{i=1,2}H_{b_i,\alpha}\bigl(\{\log_{b_i}(n/L_{b_i})\}\bigr),
\]
and the complete set of subsequential limits is **exactly**
\[
\boxed{\left[\max\{m_{b_1},m_{b_2}\},\ M_\alpha\right].}
\]
Adding an incommensurate geometric spectral ladder therefore lifts the sharp lower relaxation envelope without changing the upper envelope. For the natural choice \(\alpha=1\), \(b_1=2\), \(b_2=3/2\), the lower constant increases from \(\log2/2\approx0.3465735903\) to \(2\log(3/2)\exp(-2\log(3/2))\approx0.3604134294\), while the upper constant stays \(e^{-1}\approx0.3678794412\).

All the operators in the theorem are strongly stable, hence asymptotically expansive under the standard one-sided definition, but not strongly asymptotically expansive: each full-space operator norm \(\|T^n\|\) equals one. The compact source balls yield the quantified uniform convergence which is unavailable on the full unit ball.

## Assumptions and scope
The Hilbert space and all direct sums use the standard real or complex \(\ell^2\) norm. The index \(k\) runs through nonnegative integers and \(n\) through positive integers. Fractional parts take values in \([0,1)\); at a tie between adjacent optimal coordinates either optimizer gives the same exact error. The exponent \(\alpha\) and spectral ratios \(b,b_1,b_2\) are arbitrary fixed real parameters subject to the displayed restrictions. The two-ladder cluster-interval assertion assumes irrationality of \(\log b_1/\log b_2\); no such conclusion is asserted for rationally dependent spectral ratios without further analysis.

The source ball \(\mathcal K_{b,\alpha}\) is the image of the Hilbert unit ball under the compact operator \(Q_b^\alpha\). The quantity being optimized is the actual Hilbert norm of an orbit after \(n\) steps, not a Cesàro mean, a pointwise rate for a particular datum, or a time-integrated maximal-regularity norm. The claim includes no uniformity as \(b\downarrow1\) or \(\alpha\to0\).

## Proof
**1. Exact reduction to the eigenvalue sequence.** For \(x=Q_b^\alpha y\) and \(\|y\|_2\le1\), orthogonality gives
\[
\|T_b^n x\|_2^2=\sum_{k\ge0}b^{-2\alpha k}\exp(-2nb^{-k})|y_k|^2.
\]
Hence the supremum is the maximum of \(f_k=b^{-\alpha k}\exp(-nb^{-k})\), achieved by a unit basis vector multiplied by the spectral source weight. The maximum exists because \(f_k\to0\) as \(k\to\infty\). The adjacent ratio is
\[
\frac{f_{k+1}}{f_k}=b^{-\alpha}\exp\left(\frac{b-1}{b}\,n b^{-k}\right).
\]
It is at least one exactly when \(n b^{-k}\ge bL_b\). Since \(n b^{-k}\) is strictly decreasing in \(k\), the sequence \((f_k)\) rises and then falls, with at most one adjacent tie. For \(n\ge L_b\), the integer \(k_b(n)=\lfloor\log_b(n/L_b)\rfloor\) is nonnegative and satisfies
\[
L_b\le n b^{-k_b(n)}<bL_b.
\]
It therefore maximizes \(f_k\) globally. Writing \(t=\{\log_b(n/L_b)\}\) gives \(n b^{-k_b(n)}=L_b b^t\) and proves the exact formula.

**2. Exact phase range and single-scale cluster set.** Equality of endpoints follows from
\[
\frac{H_{b,\alpha}(1)}{H_{b,\alpha}(0)}=b^\alpha e^{-(b-1)L_b}=1.
\]
The inequalities \(\log b<b-1\) and \(\log b>1-1/b\), valid for \(b>1\), give \(L_b<\alpha<bL_b\). Differentiation yields
\[
H'_{b,\alpha}(t)=(\log b)(\alpha-L_b b^t)H_{b,\alpha}(t).
\]
Thus the unique interior maximum occurs at \(L_b b^t=\alpha\), with value \(M_\alpha\), and the equal endpoints are the minimum \(m_b\), strictly smaller than \(M_\alpha\). For any \(t\in[0,1)\), integers \(n_j\) nearest \(L_b b^{j+t}\) satisfy \(\log_b(n_j/L_b)-j\to t\) as \(j\to\infty\). For \(t=0\), convergence modulo one is sufficient because the endpoint values match. Every phase therefore occurs as a subsequential limit, and continuity plus the exact formula show that the cluster set is the full image \([m_b,M_\alpha]\).

**3. Two independent spectral scales.** The direct-sum norm is the larger of the two component norms, because the optimization is over a Hilbert unit ball. Applying Step 1 to each summand proves the exact two-scale identity. Let \(v=(1/\log b_1,1/\log b_2)\). Irrationality of \(\log b_1/\log b_2\) means that the continuous linear orbit \(t\mapsto tv\pmod{\mathbb Z^2}\) is dense on the two-torus, by the elementary Kronecker density theorem for a line of irrational slope. The translated orbit obtained by subtracting \((\log_{b_1}L_{b_1},\log_{b_2}L_{b_2})\) is also dense, and visits every open neighborhood at arbitrarily large positive times. If \(t_j\to\infty\) is a sequence realizing any prescribed torus phase, take \(n_j\) to be the nearest integer to \(e^{t_j}\). Then \(\log n_j-t_j\to0\), so the phase pair arising from these integers approaches the same target. The integer phase pairs are therefore dense in the two-torus at arbitrarily large indices.

The continuous function \((u_1,u_2)\mapsto\max\{H_{b_1,\alpha}(u_1),H_{b_2,\alpha}(u_2)\}\) on that connected torus has minimum \(\max\{m_{b_1},m_{b_2}\}\): choose both phases at their separate minima. Its maximum is \(M_\alpha\): choose either component at its maximum. Since the image of a connected compact space under a continuous real function is an interval, the torus image is the entire displayed interval. Integer phase density proves this is precisely the subsequential limit set, not merely an enclosing bound. For \(b_1=2\), \(b_2=3/2\), irrationality follows from unique prime factorization: no nonzero integers \(p,q\) solve \(2^p=(3/2)^q\).

**4. Dynamical distinction.** Each eigenvalue of \(T_b\) lies strictly between zero and one. Dominated convergence of \(\sum |x_k|^2\exp(-2nb^{-k})\) gives \(T_b^nx\to0\) for every \(x\). The same holds for a finite direct sum. On the other hand, eigenvalues tend to one, so \(\|T_b^n\|=\|T^n\|=1\) for every \(n\). Every vector of norm at most a fixed radius has a bounded orbit, but convergence is not uniform over that ball. These are respectively the one-sided asymptotic-expansivity and failure-of-strong-asymptotic-expansivity conditions. Steps 1–3 give the exact restoration of uniform convergence on each compact source ball and show the exponent \(\alpha\) cannot be increased, since \(m_b>0\).

## Verification
All infinite-dimensional assertions are proved in Steps 1–4. The standalone standard-library program `verify.py` independently checks the adjacent-coordinate optimum, the normalized identity and its sharp bounds for seven parameter pairs, numerical approximations to prescribed phases, and two-scale bounds. The recorded run passed 2,440 finite assertions. These tests corroborate formula handling but do not prove the density theorem or the infinite-dimensional supremum independently of the proof. Reproduce with `python3 verify.py` from the extracted file set.

## Relationship to prior work
Bag, Mandal and Das (arXiv:2610.01196v1, Sections 3–4) define asymptotic and strong asymptotic expansivity and exhibit qualitative nonuniform convergence, including diagonal operators. Their claims do not specify compact spectral source sets, optimize their orbit-decay error, or compute an exact one- or two-scale cluster interval. The spectral-theorem reduction of an operator norm to a supremum over eigenvalues is classical and is **not** claimed as new; the contributions here are its exact sharp discrete-scale optimization and the arithmetic description of all normalized limit points for one and two incommensurable geometric spectral ladders.

Rozendaal, Seifert and Stahn study optimal decay bounds for operator semigroups using resolvent growth and normality, notably Theorems 1.1 and 4.4, but these results do not state the source-ball, geometric spectral phase profile above. Related records on normal-operator spectral criteria and scalar asymptotic-expansivity failure sets describe qualitative stable/unstable classes rather than decay envelopes. A published geometric-spectral maximal-regularity computation studies an \(L^1\)-in-time convolution norm in increasing finite dimensions, not the present \(\|e^{-nQ}Q^\alpha\|\) for a compact generator. These comparisons are of mathematical claims, not a proof of absolute priority; equivalent formulas in broader literature may exist.

## Limitations
The exact envelope requires pure geometric spectral ladders and a Hilbert spectral source ball; it is not asserted for arbitrary irregular eigenvalue sequences, nonnormal operators, unweighted Hilbert-unit-ball decay, or arbitrary source norms. The two-scale interval requires rational independence of the logarithms. The logarithmic modulations are a limiting behavior as the integer orbit index tends to infinity, not claims about periodic or quasiperiodic individual trajectories. The finite verifier is illustrative rather than exhaustive of the infinite-dimensional proof. No independent mathematical audit has been performed.

## References
1. P. Bag, P. N. Mandal and P. K. Das, *Asymptotic Expansive and Hyperbolic Linear Operators*, arXiv:2610.01196v1, publicly submitted 1 October 2026, primary MSC2020 37B05. https://arxiv.org/html/2610.01196v1
2. J. Rozendaal, D. Seifert and R. Stahn, *Optimal rates of decay for operator semigroups on Hilbert spaces*, arXiv:1709.08895v3. https://arxiv.org/html/1709.08895v3
3. *Boundary spectral projection criterion for asymptotic expansivity of normal operators*, published mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-boundary-spectral-projection-criterion-for-asymptotic-expansivit--0138cc6da4e0
4. *Universality of scalar asymptotic-expansivity phase diagrams for normal dynamics*, published mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universality-of-scalar-asymptotic-expansivity-phase-diagrams-for--7f4d4e5a239b
5. *Sharp spectral-spacing constants for finite-dimensional endpoint maximal regularity*, published mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-spectral-spacing-constants-for-finite-dimensional-endpoint--696f083028ce
