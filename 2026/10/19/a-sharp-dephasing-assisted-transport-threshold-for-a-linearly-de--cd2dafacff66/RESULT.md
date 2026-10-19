# A sharp dephasing-assisted transport threshold for a linearly detuned three-site chain

## Finding

For the three-site single-excitation Lindblad chain with constant nearest-neighbor hopping, linear on-site detuning, uniform local dephasing, and irreversible trapping at the far endpoint, the **mean trapping time has at most one interior optimal dephasing rate**, and a sharp analytic detuning threshold determines whether that optimum exists.

Normalize the hopping amplitude to one. Fix the trap loss rate \(k>0\), a real adjacent-site detuning \(\delta\), and a uniform off-diagonal decoherence rate \(g\geq0\). Write \(y=\delta^2\). Define
\[
Q_k(y)=256y^3+(32k^2+512)y^2+(k^4+24k^2+288)y-12k^2.
\]
There is exactly one positive root \(y_c(k)\) of \(Q_k(y)=0\). The mean absorption time \(T_k(g,\delta)\) satisfies the following exact dichotomy:

1. If \(\delta^2\le y_c(k)\), then \(T_k(g,\delta)\) is strictly increasing on \((0,\infty)\). The unique minimum over \(g\ge0\) is the noise-free value at \(g=0\).
2. If \(\delta^2>y_c(k)\), there exists a **unique** \(g_*(k,\delta)>0\) at which \(T_k\) is globally minimized; it is strictly decreasing before this point and strictly increasing afterward.

In particular, no two distinct local noise-assisted transport optima occur anywhere in this complete three-site linear-gradient model. At \(k=1\), the threshold in the physical adjacent-site detuning magnitude is \(\sqrt{y_c(1)}=0.18984878489148868\ldots\). For fixed \(k>0\), the large-gradient optimum has the sharp expansion
\[
g_*(k,\delta)=|\delta|-\frac{k}{3}+O(|\delta|^{-1})
\qquad (|\delta|\to\infty).
\]

## Assumptions and scope

Use the three-dimensional Hilbert space with orthonormal site basis \(|1\rangle,|2\rangle,|3\rangle\). In units with hopping amplitude \(J=1\), let
\[
H_\delta=\begin{pmatrix}0&1&0\\1&\delta&1\\0&1&2\delta\end{pmatrix},
\qquad P_j=|j\rangle\langle j|.
\]
A particle starts at site \(1\), so \(\rho_0=P_1\). The unnormalized surviving density matrix evolves by
\[
\mathcal L_{k,g,\delta}(\rho)
=-i[H_\delta,\rho]
+g\left(\sum_{j=1}^3 P_j\rho P_j-\rho\right)
-\frac{k}{2}\{P_3,\rho\}.
\]
Our dephasing convention is that each off-diagonal matrix entry decays at bare rate \(g\) in the absence of Hamiltonian motion and trapping; other literature conventions can differ by factors of two or four. The irreversible absorption rate is \(k\,\rho_{33}(t)\). The initial-to-sink **mean absorption time**, not a continuously pumped steady-state current, is
\[
T_k(g,\delta)=\int_0^\infty\mathrm{tr}\big(e^{t\mathcal L_{k,g,\delta}}P_1\big)\,dt.
\]
Every \(k>0\), every \(\delta\in\mathbb R\), and every \(g\ge0\) are included. The formula remains finite when \(g=0\): the irreducible tridiagonal Hamiltonian has no eigenvector orthogonal to site \(3\), since its last and then middle row would force all coordinates to vanish. At positive dephasing, the only zero-loss invariant subspace is also trivial; hence the finite-dimensional trace-decreasing semigroup decays and the integral converges.

## Proof

**Step 1: exact mean-time resolvent.** Integrating the nine real-linear matrix-unit equations, equivalently solving \(-\mathcal L^*(X)=I\) and evaluating \(\mathrm{tr}(XP_1)\), gives \(T=N/D\), where
\[
R=4g^3+4kg^2+(k^2+16y+8)g+2k,
\qquad D=2k(2g+k)R,
\]
\[
\begin{aligned}
N={}&24kg^5+(44k^2+48)g^4
 +(30k^3+120ky+120k)g^3\\
& +(9k^4+108k^2y+88k^2+192y+96)g^2\\
& +(k^5+26k^3y+24k^3+96ky^2+144ky+72k)g\\
& +k^4y+2k^4+16k^2y^2+32k^2y+12k^2.
\end{aligned}
\]
All factors of \(D\) are positive for the stated domain. The included executable regenerates this equality from the original nine-component Lindblad generator, rather than treating the rational expression as an unexplained ansatz. In particular, \(T\sim3g/2\) as \(g\to\infty\).

**Step 2: differentiate and isolate the threshold.** Let
\[
P(g;k,y)=(\partial_g N)D-N(\partial_g D),
\quad \partial_g T=P/D^2.
\]
The polynomial \(P\) has degree eight. Its constant, linear, and quadratic coefficients (in ascending powers of \(g\)) are
\[
\begin{aligned}
[g^0]P&=-2k^4 Q_k(y),\\
[g^1]P&=-8k^3 F_1(k,y),\\
[g^2]P&=2k^2 F_2(k,y),
\end{aligned}
\]
where
\[
\begin{aligned}
F_1={}&256y^3+(64k^2+640)y^2
 +(3k^4+28k^2+256)y-3k^4-36k^2,\\
F_2={}&-3072y^3-(256k^2+3072)y^2
 +(28k^4+416k^2-768)y+3k^6+144k^4+624k^2.
\end{aligned}
\]
Every coefficient \([g^j]P\) for \(3\le j\le8\) is a polynomial in \(k\) and \(y\) with **strictly positive coefficients** (verified by exact expansion in the included program). Two exact identities provide the sign control for the potentially nonpositive coefficients:
\[
F_1-3Q_k
=-512y^3-(32k^2+896)y^2-(44k^2+608)y-3k^4<0,
\]
\[
\begin{aligned}
F_2+12F_1={}&(512k^2+4608)y^2
 +(64k^4+752k^2+2304)y\\
&+3k^6+108k^4+192k^2>0.
\end{aligned}
\]
The derivative at zero noise is therefore exactly
\[
\left.\partial_g T_k(g,\delta)\right|_{g=0}
=-\frac{Q_k(y)}{8k^2}.
\]
Moreover \(Q_k\) is strictly increasing on \([0,\infty)\), begins at \(-12k^2\), and tends to \(+\infty\), proving existence and uniqueness of its positive root.

**Step 3: classify all stationary points, not only the initial slope.** If \(Q_k(y)\le0\), the first identity gives \(F_1<0\), and the second then gives \(F_2>0\). Hence all coefficients of \(P\) are nonnegative, with the coefficients of \(g,g^2,\ldots,g^8\) strictly positive. Thus \(P(g)>0\) for every \(g>0\), including at the threshold.

If \(Q_k(y)>0\), the constant coefficient of \(P\) is negative. When \(F_1<0\), the linear and quadratic coefficients are positive; when \(F_1\ge0\), the linear coefficient is nonpositive and the quadratic coefficient may have either sign. In both cases, after zero coefficients are discarded, the full coefficient sequence of \(P\) in ascending order has exactly **one** sign change: the coefficients of degrees \(3\) to \(8\) are all positive. Descartes' rule therefore gives at most one positive zero, counted with multiplicity. Since \(P(0)<0\) and its leading coefficient is positive, the intermediate value theorem gives exactly one positive, necessarily simple, zero. The derivative changes there from negative to positive. Together with \(T\to\infty\), this proves the sharp and global dichotomy.

**Step 4: asymptotic optimal rate.** Set \(x=|\delta|=\sqrt y\) and scale \(g=tx\). The leading homogeneous part of the exact derivative numerator is
\[
\frac{P(tx;k,x^2)}{384k^2x^8}
\longrightarrow t^2(t^2-1)(t^2+4)^2
\qquad(x\to\infty).
\]
For any fixed \(0<\epsilon<1\), this expression is negative at \(t=1-\epsilon\) and positive at \(t=1+\epsilon\); the unique positive root lies between these points for all large \(x\), so \(g_*/x\to1\). Writing \(g=x+a\) in the exact polynomial, the \(x^8\) coefficient cancels identically while the \(x^7\) coefficient is \(6400k^2(3a+k)\). Its simple zero, combined with the smooth implicit-function expansion near the simple scaled root \(t=1\), gives \(a=-k/3+O(x^{-1})\), as claimed.

## Verification

The standalone file `check_three_site.py` requires Python 3, SymPy, NumPy and SciPy. Running `python check_three_site.py` executes 83 assertions, including: exact verification of \(P\)'s low-order coefficients and the two strict sign identities; coefficientwise positivity for degrees \(3\) through \(8\); independent reconstruction of \(T\) from all nine matrix-unit Lindblad equations; forty-eight numerical evaluations using a separately implemented complex Kronecker superoperator; exact large-detuning coefficient checks; and sampled root counts as non-proof sanity checks. All 83 assertions passed. These computations supplement, but do not replace, the algebraic proof of the global sign and uniqueness claims.

For example, the formula yields \(T_1(1,1)=87/14=6.214285714285714\ldots\). Numerically solving \(Q_1(y_c)=0\) gives the critical detuning magnitude reported above.

## Relationship to prior work

Coates, Lovett, and Gauger (2021) study noise-assisted quantum transport in linearly detuned chains and characterize optimal noise rates primarily by pumped source–sink current and localization arguments; their analytic treatment does not supply the three-site, fixed-initial-site mean-first-absorption formula or the sharp all-parameter uniqueness classification here. This work uses the same broad physical ingredients but a distinct observable and exact finite chain. Their dephasing normalization differs and must not be identified directly with \(g\).

Coates, Lovett, and Gauger (2022) discuss multiple noise-optimal transport regimes (the 'twin peaks' phenomenon) on more complicated networks; the present theorem establishes an exact exclusion of two such optima in the specified minimal path geometry. Kassal and Aspuru-Guzik (2012) analyze trapping efficiency for several ordered small systems, including a three-site configuration, but use different preparation, energy landscape, and competing loss observables. Neither result implies the current uniform-gradient threshold. These comparisons concern explicit stated claims, not mere title matches.

## Limitations

This is a single-excitation Markovian Lindblad model with equal hopping strengths and an exact linear on-site energy ramp. It does not assert uniqueness for triangles, unequal couplings, added source/loss channels, correlated dephasing, or non-Markovian baths. The identified optimum minimizes **mean absorption time**; optimizing continuously driven stationary throughput can have different outcomes. At large finite detuning the optimum is asymptotic, not exactly \(|\delta|-k/3\). Published general Lindblad resolvent techniques can formally recover the finite-chain formula; the claim of mathematical novelty is the evaluated sharp threshold and sign-complete uniqueness proof, subject to independent priority evaluation. A historically relevant paper on topology-dependent Haken–Strobl trapping could not be materially inspected and leaves a specific priority risk.

## References

1. S. Coates, B. W. Lovett, E. M. Gauger, *Localisation determines the optimal noise rate for quantum transport*, arXiv:2106.12567 (first public 2021-06-23), https://arxiv.org/abs/2106.12567 .
2. S. Coates, B. W. Lovett, E. M. Gauger, *From Goldilocks to twin peaks: multiple optimal regimes for quantum transport in disordered networks*, arXiv:2210.11875 (first public 2022-10-21), https://arxiv.org/abs/2210.11875 .
3. I. Kassal, A. Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems*, arXiv:1201.5202 (2012), https://arxiv.org/abs/1201.5202 .
4. K. M. Gaab, C. J. Bardeen, *The effects of connectivity, coherence, and trapping on energy transfer in simple light-harvesting systems studied using the Haken-Strobl model with diagonal disorder*, J. Chem. Phys. (2004), https://doi.org/10.1063/1.1786922 ; abstract assessed, full text not available in this investigation.
