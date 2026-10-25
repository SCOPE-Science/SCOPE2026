# Exact phase-mismatch frontiers for low-correction Parareal with unitary propagators

## Finding

Let \(F,G\in\mathbb C^{d\times d}\), with \(d\ge1\), be **commuting unitary matrices**. On \(N\) equal time windows, initialize the standard Parareal scheme with consecutive coarse steps and perform exactly \(k\) correction sweeps. Write \(P_{N,k}\) for its completed-block map and \(\Delta=\|F-G\|_2\). For the first four nontrivial correction counts, the complete sharp one-block Euclidean contractivity classification is

\[
\begin{array}{c|c|c}
 k&\text{number of windows}&\|P_{N,k}\|_2\le1\ \text{if and only if}\\ \hline
 1&N\ge2&\Delta=0\\
 2&N\ge3&\Delta=0\\
 3&N\ge4&\displaystyle\Delta^2\le\frac{3}{(N-1)(N-2)}\\
 4&N\ge5&\displaystyle\Delta^2\le\frac{8}{(N-1)(N-3)}
\end{array}
\]

Every displayed boundary is attained and sharp. Thus the first two correction sweeps necessarily produce an expansive completed block for every nonidentical pair of commuting unitary propagators, whereas three corrections admit a nonzero phase-mismatch stability window. Four corrections enlarge that exact window. The same criterion characterizes boundedness under arbitrarily many repetitions of the *completed* block, since \(P_{N,k}\) is normal.

At \(N=5\), take \(G=1\) and \(F=3/4+i\sqrt7/4\) on \(\mathbb C\). Successive completed-block squared amplification factors for \(k=1,2,3,4,5\) are, respectively,
\[
11,\quad 16,\quad\frac72,\quad\frac{11}{16},\quad1.
\]
The fourth correction restores contraction even though all three preceding completed blocks expand. The fifth correction gives the exact fine solution.

## Assumptions and scope

All norms are Euclidean operator \(2\)-norms; unitary means \(F^*F=G^*G=I\); commuting means \(FG=GF\). The matrices represent one *coarse-window* fine propagator and one coarse propagator. The same pair is used on every window. The method is initialized by \(U^0_j=G^j x\), with \(U^k_0=x\) at every correction index, and
\[
U^{k+1}_{j+1}=G U^{k+1}_j+(F-G)U^k_j,
\qquad 0\le j<N.
\]
The completed-block map is \(U^k_N=P_{N,k}x\). For the classification, \(k\in\{1,2,3,4\}\) and \(N\ge k+1\). For \(k\ge N\), standard Parareal instead reproduces \(F^N\) exactly. The theorem concerns fixed-correction completed-block nonexpansivity, not nonexpansivity of all intermediate correction sweeps or monotonic convergence of the Parareal iteration.

## Proof

**1. Exact completed-block polynomial.** Induction in the window index and correction index gives, for \(0\le k\le N\),
\[
P_{N,k}=\sum_{j=0}^k{N\choose j}G^{N-j}(F-G)^j.
\]
Indeed, the coarse initialization supplies the term \(j=0\); the correction recurrence adds adjacent binomial coefficients by Pascal's identity, with the initial value fixed on each sweep. Since \(F\) and \(G\) commute, this is a genuine matrix polynomial.

**2. Reduction to one phase parameter.** Commuting unitaries admit a common orthonormal eigenbasis. On one eigenvector, let their eigenvalues be \(f,g\), with \(|f|=|g|=1\), and put \(z=f/g\), \(u=1-\operatorname{Re}z\in[0,2]\). The corresponding eigenvalue of \(P_{N,k}\) is \(g^N p_{N,k}(z)\), where
\[
p_{N,k}(z)=\sum_{j=0}^k{N\choose j}(z-1)^j.
\]
Consequently,
\[
\|P_{N,k}\|_2=\max_{\mathrm{modes}}|p_{N,k}(z)|,
\qquad
\Delta^2=\max_{\mathrm{modes}}|f-g|^2
=2\max_{\mathrm{modes}}u.
\]
The equalities rely on normality; no such conclusion is asserted for noncommuting or nonnormal propagators.

**3. Exact squared-amplification identities.** For \(k<N\), the coefficient of \(z^r\) in \(p_{N,k}\) is
\[
a_r=(-1)^{k-r}{N\choose r}{N-r-1\choose k-r},\qquad 0\le r\le k.
\]
This follows by expanding each \((z-1)^j\), using \({N\choose j}{j\choose r}={N\choose r}{N-r\choose j-r}\), and the finite alternating binomial identity. Since all \(a_r\) are real, for \(|z|=1\) and \(t=\operatorname{Re}z\),
\[
|p_{N,k}(z)|^2
=\sum_{r=0}^k a_r^2
 +2\sum_{0\le r<s\le k}a_ra_s T_{s-r}(t),
\]
where \(T_j\) is the degree-\(j\) Chebyshev polynomial. Substituting \(t=1-u\), with
\[
\begin{aligned}
T_1(1-u)&=1-u,\\
T_2(1-u)&=1-4u+2u^2,\\
T_3(1-u)&=1-9u+12u^2-4u^3,\\
T_4(1-u)&=1-16u+40u^2-32u^3+8u^4,
\end{aligned}
\]
and collecting equal powers yields the following **polynomial identities in \(N,u\)**, without approximation:
\[
\begin{aligned}
|p_{N,1}|^2-1&=2N(N-1)u,\\
|p_{N,2}|^2-1&=N(N-2)(N-1)^2u^2,\\
|p_{N,3}|^2-1&=\frac{N(N-3)(N-2)(N-1)}9u^2
  \left[2(N-1)(N-2)u-3\right],\\
|p_{N,4}|^2-1&=\frac{N(N-4)(N-3)(N-2)^2(N-1)}{36}u^3
  \left[(N-1)(N-3)u-4\right].
\end{aligned}
\]
The displayed formulae can also be verified mechanically by coefficient expansion, as implemented in the accompanying symbolic checker, but their derivation is elementary polynomial algebra and covers every integer \(N\) in the stated ranges.

**4. Necessity, sufficiency, and sharpness.** All prefactors involving \(N\) are positive for \(N\ge k+1\). When \(k=1\) or \(k=2\), a mode is nonexpansive only if \(u=0\), equivalently \(f=g\). For \(k=3\), every mode is nonexpansive precisely when \(u\le3/[2(N-1)(N-2)]\); for \(k=4\), precisely when \(u\le4/[(N-1)(N-3)]\). Apply \(\Delta^2=2\max u\) to obtain the theorem. At equality the corresponding mode has unit amplification; just above it, that mode has amplification strictly greater than one. Each threshold can be realized in dimension one with \(G=1\) and \(F=e^{i\theta}\) chosen so that \(1-\cos\theta\) equals the threshold. When a mode is expansive, repetition of the normal block map produces geometric growth along that eigenvector; when no mode is expansive, all repetitions have operator norm at most one.

**5. Exact illustration and phase-window scaling.** For the stated example, \(u=1/4\) and \(N=5\). Substituting into the four identities gives the displayed exact values; at \(k=N=5\), \(P_{5,5}=F^5\). If \(\theta\) denotes the principal relative eigenphase, the maximal nonexpansive phase mismatch for three and four corrections is respectively
\[
\theta_{N,3}=\arccos\left(1-\frac{3}{2(N-1)(N-2)}\right)
=\frac{\sqrt3}{N}+O(N^{-2}),
\]
\[
\theta_{N,4}=\arccos\left(1-\frac{4}{(N-1)(N-3)}\right)
=\frac{2\sqrt2}{N}+O(N^{-2}).
\]
These follow from \(1-\cos\theta=\theta^2/2+O(\theta^4)\). The exact windows make explicit the inverse-window-count scaling that is hidden by qualitative statements about phase accuracy.

## Verification

The independent recurrence implementation, exact algebraic boundary examples, generic symbolic factorization identities, and simultaneously diagonalized unitary-matrix tests are supplied in `verify.py`. Run `python verify.py` with Python 3, SymPy and NumPy. It prints a PASS count only after all assertions succeed. Symbolic identities with free integer parameter \(N\), together with the analytical argument above, establish the all-\(N\) conclusions; finite checks do not replace that proof.

## Relationship to prior work

Staff and Rønquist (2005) derive the underlying general Parareal binomial stability polynomial and study real modes analytically but general complex-mode stability by plots. Ruprecht (first public preprint 2017) analyzes discrete wave dispersion and shows that fine/coarse phase mismatch is central to Parareal's instability; its matrix and numerical analyses do not solve the present first-four-correction unit-modulus inequalities. Buvoli and Minion (2023) analyze exponential Runge–Kutta Parareal on nondiffusive systems through matrix stability functions and numerical regions; they do not derive these exact unitary phase-error cutoffs. Ariel, Nguyen and Tsai (2017) analyze weighted \(\theta\)-Parareal via an iteration-error bound and numerically mapped stability regions; this bounds a different quantity and does not imply the sharp unweighted completed-block cutoffs. Rosemeier, Haut and Wingate (2024) study multilevel Parareal with averaging and obtain error bounds, not the fixed-correction unitary classification. The generic binomial representation and the qualitative phase-instability phenomenon are prior work; the contribution assessed here is the **sharp solved norm frontier, its first restoration at three corrections, and its enlargement at four corrections**.

## Limitations

The result requires exact commuting unitary propagators and a common Euclidean inner product. Realistic coarse integrators may be dissipative, nonlinear, noncommuting, or nonnormal; the exact boundaries do not extend to those cases. Energy nonexpansivity of a completed block does not establish accuracy, computational speedup, energy monotonicity during individual correction sweeps, or a general stability threshold for five or more corrections. No claim is made concerning nonlinear equations, floating-point effects, or universal optimal correction counts.

## References

1. G. A. Staff and E. M. Rønquist, *Stability of the Parareal Algorithm*, in *Domain Decomposition Methods in Science and Engineering*, LNCS&E 40, 449–456 (2005), DOI: 10.1007/3-540-26825-1_46. Open manuscript: https://ddm.org/DD15/pdf/127.pdf.
2. D. Ruprecht, *Wave propagation characteristics of Parareal*, arXiv:1701.01359v1 (first public 2017-01-05); *Computing and Visualization in Science* 19, 1–17 (2018), DOI: 10.1007/s00791-018-0296-z. https://arxiv.org/abs/1701.01359.
3. T. Buvoli and M. L. Minion, *Exponential Runge-Kutta Parareal for Non-Diffusive Equations*, arXiv:2301.03764v1 (first public 2023-01-10). https://arxiv.org/abs/2301.03764.
4. J. Rosemeier, T. Haut and B. Wingate, *Multilevel Parareal Algorithm with Averaging for Oscillatory Problems*, *SIAM Journal on Scientific Computing* (2024), DOI: 10.1137/23M1547123. https://epubs.siam.org/doi/full/10.1137/23M1547123.
5. G. Ariel, H. Nguyen and R. Tsai, *\(\theta\)-parareal schemes*, arXiv:1704.06882v2 (2018; first preprint 2017). https://arxiv.org/abs/1704.06882.
