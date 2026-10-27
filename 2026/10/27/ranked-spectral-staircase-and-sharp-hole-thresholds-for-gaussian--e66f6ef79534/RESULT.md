# Ranked spectral staircase and sharp hole thresholds for Gaussian annuli

## Finding

Consider Gaussian time-frequency concentration in a concentric annulus of **fixed area**. For every positive integer \(N\), the maximizing rank-\(N\) Hermite-mode subspace passes through **every** consecutive block, one block at a time, as the central hole expands. Every switching radius is the unique positive zero of an explicit polynomial with one coefficient sign change. The switches are transverse, giving genuine corners in the rank-\(N\) concentration curve. Two sharp asymptotics locate the switches at high Hermite index and for large annular area.

Precisely, fix \(s>0\) and put
\[
\Omega_{a,s}=\{z\in\mathbb C:a<\pi|z|^2<a+s\},\qquad a\ge0.
\]
The set has Euclidean area \(s\). On the Gaussian Bargmann--Fock space let \(T_{a,s}\) be the positive localization/Toeplitz operator with symbol \(\mathbf 1_{\Omega_{a,s}}\), and let \(\Sigma_N(a,s)\) be the sum of its \(N\) largest eigenvalues, counted with multiplicity. Write
\[
H_{k,N}(u)=\sum_{j=k+1}^{k+N}\frac{u^j}{j!},
\qquad P_{k,N,s}(a)=e^sH_{k,N}(a)-H_{k,N}(a+s)
\]
for integers \(k\ge0\), \(N\ge1\). Then each \(P_{k,N,s}\) has exactly one positive root \(A_{k,N}(s)\), this root is simple, and
\[
0<A_{0,N}(s)<A_{1,N}(s)<\cdots\longrightarrow+\infty.
\]
Let \(e_j(z)=\sqrt{\pi^j/j!}\,z^j\) be the normalized Fock monomials. For \(a\) strictly between successive thresholds, the **unique** maximizing rank-\(N\) subspace is
\[
V_{k,N}=\operatorname{span}\{e_k,e_{k+1},\ldots,e_{k+N-1}\}
\quad\text{when}\quad A_{k-1,N}(s)<a<A_{k,N}(s),
\]
with \(A_{-1,N}(s):=0\), so the first interval is \(0\le a<A_{0,N}(s)\). At the switch \(a=A_{k,N}(s)\), all maximizing rank-\(N\) subspaces have the form
\[
\operatorname{span}\{e_{k+1},\ldots,e_{k+N-1}\}\oplus L,
\qquad L\subset\operatorname{span}\{e_k,e_{k+N}\},\quad\dim L=1.
\]
The first span is interpreted as \(\{0\}\) if \(N=1\). No other rank-boundary degeneracies occur. Thus
\[
\Sigma_N(a,s)=\sum_{j=k}^{k+N-1}\frac1{j!}\int_a^{a+s} e^{-t}t^j\,dt
\]
in the corresponding interval. At each threshold its right derivative minus its left derivative is strictly positive and is exactly
\[
\left[\partial_a\Sigma_N\right]_{A_{k,N}(s)+}
-\left[\partial_a\Sigma_N\right]_{A_{k,N}(s)-}
=e^{-A_{k,N}(s)-s}P'_{k,N,s}(A_{k,N}(s))>0.
\]

The switch thresholds obey the following **sharp two-regime laws**; the remainder constants may depend on fixed parameters:
\[
\boxed{\displaystyle
A_{k,N}(s)=k+\frac{N+1-s}{2}
+\frac1k\left(\frac{s^2}{12}-\frac{N^2-1}{24}\right)
+O_{s,N}(k^{-2})}\qquad(k\to\infty;\ s,N\text{ fixed}),
\]
and
\[
\boxed{\displaystyle
A_{k,N}(s)\sim
\left(\frac{(k+1)!}{(k+N)!}\right)^{1/(k+1)}
 s^{(k+N)/(k+1)}e^{-s/(k+1)}}
\qquad(s\to\infty;\ k,N\text{ fixed}).
\]
In particular, even an **exponentially small** centered hole can change the optimal rank-\(N\) concentration subspace of a large-area disk.

## Assumptions and scope

The Fock Hilbert space consists of entire functions with finite norm
\[
\|F\|_{\mathcal F^2}^2=\int_{\mathbb C}|F(z)|^2 e^{-\pi|z|^2}\,dA(z).
\]
The operator \(T_{a,s}=P_{\mathcal F^2}\,\mathbf1_{\Omega_{a,s}}P_{\mathcal F^2}\) is defined on \(\mathcal F^2\) through the quadratic form \(\langle T_{a,s}F,F\rangle=\int_{\Omega_{a,s}}|F|^2e^{-\pi|z|^2}\,dA\). It is positive trace class, with trace \(s\). All the claims hold for every real \(s>0\), every \(a\ge0\), every integer \(N\ge1\), and every integer \(k\ge0\); the asymptotics have the fixed-parameter quantifiers explicitly specified above. Boundaries of the masks do not affect the operator. “Maximizing rank-\(N\) subspace” means a maximizer in the Ky Fan variational principle \(\operatorname{Tr}(QT_{a,s})\) over orthogonal rank-\(N\) projections \(Q\). By the Bargmann transform the same statement holds for Gaussian-window localization in the corresponding Hermite basis, with these normalizations.

## Proof

**1. Spectrum and discrete unimodality.** Radial integration makes the \(e_j\) an eigenbasis and gives the unsorted eigenvalues
\[
\mu_j(a,s)=\frac1{j!}\int_a^{a+s}t^je^{-t}\,dt
=e^{-a}\sum_{r=0}^{j}\frac{a^r}{r!}
-e^{-(a+s)}\sum_{r=0}^{j}\frac{(a+s)^r}{r!}.
\]
For \(a=0\) these decrease strictly with \(j\). For \(a>0\), adjacent differences are
\[
\mu_{j+1}-\mu_j
=\frac{e^{-a}a^{j+1}-e^{-(a+s)}(a+s)^{j+1}}{(j+1)!}.
\]
Their sign is the sign of \((j+1)\log(a/(a+s))+s\), so the sequence increases strictly and then decreases strictly, possibly with **one adjacent equality** at its mode. Consequently the \(N\) largest entries form a consecutive degree block, except for the choice between tied endpoints at a switching value. Every optimal rank-\(N\) subspace is determined by the entries at or above the \(N\)-th largest level.

**2. Unique crossing and transversality.** Let \(S_{k,N}=\mu_k+\cdots+\mu_{k+N-1}\). Its adjacent block difference is
\[
S_{k+1,N}-S_{k,N}=\mu_{k+N}-\mu_k
=e^{-(a+s)}P_{k,N,s}(a).
\]
For clarity, the coefficient of \(a^m\) in \(P_{k,N,s}\), for \(0\le m\le k+N\), equals
\[
\begin{cases}
-\displaystyle\frac1{m!}\sum_{r=k+1}^{k+N}\frac{s^{r-m}}{(r-m)!},&0\le m\le k,\\[2mm]
\displaystyle\frac1{m!}\left(e^s-\sum_{r=0}^{k+N-m}\frac{s^r}{r!}\right),&k+1\le m\le k+N.
\end{cases}
\]
All coefficients in the first row are negative, and all in the second are positive because \(s>0\). There is **exactly one sign change**. Descartes' rule of signs therefore bounds the total number of positive roots, counting multiplicity, by one. Since \(P_{k,N,s}(0)<0\) and the leading coefficient is \((e^s-1)/(k+N)!>0\), exactly one positive root exists. It is simple, and its crossing is from negative to positive, hence \(P'_{k,N,s}(A_{k,N})>0\).

**3. Strictly ordered switches.** At \(a=A_{k,N}\) we have \(\mu_k=\mu_{k+N}\). Discrete unimodality forces \(\mu_{k+1}>\mu_{k+N+1}\). Indeed \(\mu_{k+1}\) is strictly above the common endpoint level when \(N>1\), while \(\mu_{k+N+1}\) is strictly below it; for \(N=1\) the tied pair is the unique plateau and the following entry is strictly smaller. Thus
\[
S_{k+2,N}-S_{k+1,N}=\mu_{k+N+1}-\mu_{k+1}<0
\]
at \(a=A_{k,N}\). By the unique-crossing result, \(A_{k+1,N}>A_{k,N}\). Also \(A_{k,N}\to\infty\): on every bounded range \(0\le a\le B\), the adjacent differences \(\mu_{j+1}-\mu_j\) are negative for all \(j+1>B+s\); a crossing \(\mu_k=\mu_{k+N}\) is then impossible at sufficiently large \(k\).

Since \(S_{j+1,N}-S_{j,N}\) is positive above \(A_{j,N}\) and negative below it, the strict ordering of the roots proves that \(S_{k,N}\) is uniquely maximal on the open interval \((A_{k-1,N},A_{k,N})\), and at \(A_{k,N}\) exactly \(S_{k,N}\) and \(S_{k+1,N}\) maximize. Discrete unimodality then gives precisely the rank-\(N\) eigenspaces stated above. The Ky Fan formula follows from the variational principle. The derivative jump equals \(\partial_a(S_{k+1,N}-S_{k,N})\), yielding the displayed positive expression.

**4. Fixed rank, large-area exponential threshold.** Fix \(k,N\), and write \(A=A_{k,N}(s)\). For each fixed \(\varepsilon>0\), as \(s\to\infty\),
\[
e^s H_{k,N}(\varepsilon)\gg H_{k,N}(\varepsilon+s).
\]
The uniqueness and sign of the crossing imply \(0<A<\varepsilon\) for sufficiently large \(s\), hence \(A\to0\). Since \(H_{k,N}(A)\sim A^{k+1}/(k+1)!\) and \(H_{k,N}(A+s)\sim s^{k+N}/(k+N)!\), the exact identity \(e^s H_{k,N}(A)=H_{k,N}(A+s)\) gives the sharp exponential formula, including its constant.

**5. High-index switch expansion.** Fix \(s,N\), and define the exact factorial geometric mean
\[
\rho_{k,N}=\left(\frac{(k+N)!}{k!}\right)^{1/N}
=k+\frac{N+1}{2}-\frac{N^2-1}{24k}+O_N(k^{-2}).
\]
Put \(p_k(t)=e^{-t}t^k/k!\). Since \(p_{k+N}(t)=p_k(t)(t/\rho_{k,N})^N\), the crossing equation is equivalent to
\[
0=\int_a^{a+s}p_k(t)\left[\left(\frac{t}{\rho_{k,N}}\right)^N-1\right]dt.
\]
Write \(a=\rho_{k,N}-s/2+d\) and \(x=t-\rho_{k,N}\). Uniformly on each bounded \(x\)-interval,
\[
\begin{aligned}
\frac{p_k(\rho_{k,N}+x)}{p_k(\rho_{k,N})}
&=1-\frac{(N+1)x+x^2}{2k}+O_{s,N}(k^{-2}),\\
\left(1+\frac{x}{\rho_{k,N}}\right)^N-1
&=\frac{Nx}{k}+\frac{-N(N+1)x/2+N(N-1)x^2/2}{k^2}
+O_{s,N}(k^{-3}).
\end{aligned}
\]
Multiplication gives
\[
\frac{p_k(\rho_{k,N}+x)}{p_k(\rho_{k,N})}
\left[\left(1+\frac{x}{\rho_{k,N}}\right)^N-1\right]
=\frac{Nx}{k}-\frac{N\bigl((N+1)x/2+x^2+x^3/2\bigr)}{k^2}
+O_{s,N}(k^{-3}).
\]
The integral is taken over \(d-s/2<x<d+s/2\). Its leading term locates the unique root at \(d=O_{s,N}(k^{-1})\); integrating once more, using \(\int_{-s/2}^{s/2}x^2dx=s^3/12\), gives
\[
0=\frac{Nsd}{k}-\frac{Ns^3}{12k^2}+O_{s,N}(k^{-3}),
\qquad d=\frac{s^2}{12k}+O_{s,N}(k^{-2}).
\]
Substituting the expansion of \(\rho_{k,N}\) proves the high-index formula. The localization of the root and all remainders are uniform for \(x\) in a fixed compact interval because \(s,N\) are fixed; opposite signs of the first approximation at \(d=\pm\delta\) for any fixed \(\delta>0\) first place the root in this range.

## Verification

The accompanying standalone checker `check_spectral_staircase.py` uses only the Python standard library. It tests, using exact rational arithmetic, the binomial coefficients underlying the crossing polynomial over 735 parameter/index cases; it additionally checks 224 eigenvalue-order and crossing instances and 18 high-index/large-area asymptotic instances. The observed result was `CHECK_OK: 735 exact coefficients, 224 spectral tests, 18 asymptotic tests`. Exact finite tests establish the displayed test identities for those cases only. Existence, simplicity, full ordering for all \(k,N,s\), and both infinite asymptotic regimes are established by the preceding proof, not inferred from tests.

For an independent small-parameter check, \(N=1\) admits the exact solution
\[
A_{k,1}(s)=\frac{s}{\exp(s/(k+1))-1}.
\]
Its \(k=0\) instance is a previously published annular equality radius, **not a newly claimed discovery**. Its large-\(k\) and large-\(s\) expansions agree with both general formulas.

## Relationship to prior work

The exact Fock eigenbasis and moment-integral representation for radial symbols are classical; see Grudsky--Vasilevski (2002) and the references of Nicola--Riccardi--Tilli (2025). Nicola--Riccardi--Tilli explicitly observed that the index-to-ordered-eigenvalue correspondence depends on the radial set and determined the annulus with the first pair of equal eigenvalues. In the present notation their inner-area constant is **exactly** \(A_{0,1}(s)=s/(e^s-1)\). Their paper optimizes the second eigenvalue over radial sets and proves a fixed-area Ky Fan inequality for radial sets, but does not provide the full all-rank annular mode-order staircase or the two switching-radius asymptotics. Abreu (2026) proved the global fixed-area Ky Fan isoperimetric inequality, extending the radial result. The present theorem instead resolves the spectral-projector selection problem **within every fixed-area annular deformation**; it neither improves nor challenges the global isoperimetric bound.

The claimed contribution is restricted to the combined all-rank ordered-switch theorem and its sharp two-regime location laws. The monomial diagonalization, Poisson/gamma formulas, the simple first-pair annulus, and basic Ky Fan variational principle are acknowledged prior facts. Unindexed descriptions of annular spectral switching may exist.

## Limitations

All formulas concern concentric annuli with the Gaussian Fock weight in **one complex dimension**. They do not classify nonradial masks, other windows, higher-dimensional phase spaces, or arbitrary radial unions of annuli. The asymptotics fix \(s,N\) while \(k\to\infty\), or fix \(k,N\) while \(s\to\infty\); they make no assertion uniform when both diverge. Threshold multiplicity concerns only the rank-\(N\) selection boundary, and the derivative-jump positivity does not imply convexity or monotonicity of the full concentration curve. Historical-priority comparisons cannot rule out equivalent unindexed annular spectral-order calculations.

## References

1. L. D. Abreu, *The isoperimetric inequality for the Ky Fan norm*, arXiv:2607.28376 (first public version 30 July 2026). https://arxiv.org/abs/2607.28376
2. F. Nicola, F. Riccardi, P. Tilli, *The Faber-Krahn inequality for partial sums of eigenvalues of Toeplitz operators*, arXiv:2503.07069 (first public version 10 March 2025). Especially the introduction, Theorems 1.3/1.5, and Section 4. https://arxiv.org/abs/2503.07069
3. S. M. Grudsky and N. L. Vasilevski, *Toeplitz operators on the Fock space: Radial component effects*, Integral Equations Operator Theory **44** (2002), 10--37, DOI:10.1007/BF01197858. https://doi.org/10.1007/BF01197858
