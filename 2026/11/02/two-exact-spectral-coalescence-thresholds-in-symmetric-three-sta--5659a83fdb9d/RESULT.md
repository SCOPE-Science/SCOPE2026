# Two exact spectral coalescence thresholds in symmetric three-state exchange

## Finding

A canonical three-state reversible spectral-diffusion model undergoes **two** distinct, exact transitions in the number of observable spectral peaks. With dimensionless exchange rate \(r=\kappa/\Delta\), there are three strict local maxima for \(0<r<r_-\), two for \(r_-\le r<r_+\), and one for \(r\ge r_+\). The transition values are the square roots of the two positive roots of

\[
81y^3-81y^2-5y+1=0.
\]

Numerically \(r_-\approx0.2954723830178\) and \(r_+\approx1.0235584351808\). Both transitions can be certified by real-root sign arguments for an explicitly factored derivative cubic, without relying on a plotted or discretely sampled spectrum. At \(r_-\) the zero-frequency point is a quartically flat minimum, while at \(r_+\) it is a quartically flat maximum.

## Assumptions and scope

Let \(X_t\in\{-1,0,+1\}\) be a continuous-time, stationary Markov chain with row generator

\[
Q=\kappa\begin{pmatrix}-1&1&0\\1&-2&1\\0&1&-1\end{pmatrix},\qquad \kappa>0.
\]

There is no direct transition between the extreme states. Symmetry implies the unique invariant law is \((1/3,1/3,1/3)\), **not** a degree-weighted random-walk distribution. Let the instantaneous frequency offset be \(\Delta X_t\), \(\Delta>0\). Define the stationary coherence and spectrum by

\[
C(t)=\mathbb E\left[\exp\left(-i\Delta\int_0^t X_s\,ds\right)\right],\qquad
S(\omega)=\frac1\pi\operatorname{Re}\int_0^\infty e^{-i\omega t}C(t)\,dt.
\]

The \(\pi\) here denotes the mathematical circle constant, not the invariant probability vector. There is no independent transverse-dephasing term, no static disorder, and no direct \(-1\leftrightarrow+1\) exchange. Local maxima are counted on the full real-frequency axis, including \(\omega=0\).

## Proof

**1. Convergence and resolvent.** Set \(F=\Delta\operatorname{diag}(-1,0,1)\). The Feynman–Kac formula gives \(C(t)=\frac13\mathbf1^\mathsf T e^{(Q-iF)t}\mathbf1\). The symmetric part of \(Q-iF\) is \(Q\), whose kernel consists of constant vectors. A constant vector is not an eigenvector of \(Q-iF\) when \(\Delta>0\). Thus each eigenvalue of \(Q-iF\) has strictly negative real part, so the integral converges absolutely and

\[
S(\omega)=\frac1{3\pi}\operatorname{Re}\!\left[\mathbf1^\mathsf T(i\omega I-Q+iF)^{-1}\mathbf1\right].
\]

Matrix adjugate evaluation, or direct solution of three linear equations, yields

\[
S(\omega)=\frac{2\Delta^2\kappa(\Delta^2+9\kappa^2+\omega^2)}{3\pi\left[\omega^2(\Delta^2+3\kappa^2-\omega^2)^2+4\kappa^2(2\omega^2-\Delta^2)^2\right]}.
\]

The denominator is strictly positive: both nonnegative summands cannot vanish simultaneously for \(\kappa,\Delta>0\). Consequently the density is even, smooth, strictly positive, decays like \(\omega^{-4}\), and is normalized by \(C(0)=1\) and Fourier inversion.

**2. Reduction to a cubic.** Put \(x=(\omega/\Delta)^2\ge0\), \(y=(\kappa/\Delta)^2>0\), and define

\[
N(x,y)=1+9y+x,\qquad
D(x,y)=x(1+3y-x)^2+4y(2x-1)^2.
\]

Apart from the positive factor \(2\kappa/(3\pi\Delta^2)\), the spectral density is \(N/D\). Differentiation gives

\[
\frac{\partial}{\partial x}\frac ND=-\frac{P(x,y)}{D(x,y)^2},
\]

where

\[
P(x,y)=2x^3+(1+37y)x^2+(180y^2-16y-4)x+81y^3-81y^2-5y+1.
\]

Let \(c(y)=P(0,y)=81y^3-81y^2-5y+1\). The signs \(c(0)>0\), \(c(1/5)<0\), \(c(2)>0\), together with Descartes' rule of signs, imply exactly two distinct positive roots, denoted \(0<y_-<1/5<y_+<2\). For a fully algebraic separation of the real roots of \(P\), its discriminant is

\[
\operatorname{disc}_xP=16(6y+1)^2(4913y^3+447y^2-21y+17)>0.
\]

The last factor is positive since \(4913y^3\ge0\), and \(447y^2-21y+17>0\) for all real \(y\) by its negative quadratic discriminant. Hence \(P(\cdot,y)\) has three distinct real roots for every \(y>0\).

**3. Complete positive-root count.** Their sum is \(-(1+37y)/2<0\), their product is \(-c(y)/2\), and their pairwise-product sum is \((180y^2-16y-4)/2=2(5y-1)(9y+1)\). For \(0<y<y_-\), \(c(y)>0\) and this last sum is negative. There must be one negative root and two positive roots; three negative roots would give positive pairwise-product sum. Therefore the derivative in \(x>0\) has two zeros, corresponding to a positive-frequency local minimum followed by a positive-frequency local maximum; the center is another maximum. For \(y_-<y<y_+\), \(c(y)<0\), so the roots have positive product and negative sum: exactly two negative roots and one positive root. The center is a local minimum, and one symmetric pair of off-center maxima survives. Finally, \(y>y_+\) implies \(y>1/5\) and every coefficient of \(P\) is positive; thus no positive \(x\) root exists and the center is the only maximum.

At \(y=y_-\), \(P(0,y_-)=0\) and \(P_x(0,y_-)<0\), making \(\omega=0\) a quartically flat local **minimum** and leaving two strict off-center maxima. At \(y=y_+\), \(P(0,y_+)=0\) and \(P_x(0,y_+)>0\), making \(\omega=0\) a quartically flat **maximum** without off-center maxima. This proves the stated count at all boundaries.

## Verification

The accompanying standalone program `verify_tristate.py` reconstructs the complex resolvent and exact rational density, checks the derivative polynomial, its discriminant, and the threshold intervals symbolically, and compares 120 independently sampled complex-resolvent solutions to the closed form (maximum observed relative discrepancy below \(5\times10^{-15}\)). It also checks the positive-root patterns in nine rate regimes. Run `python verify_tristate.py` with Python, SymPy, NumPy and SciPy. The symbolic identities are exact; finite numerical tests do not prove the infinite-parameter statement, which is established by the real-root argument above.

## Relationship to prior work

The stochastic spectral-modulation framework is classical; Komijani and Coleman (arXiv:1604.05190, initially public April 18, 2016) discuss Kubo–Anderson line splitting and narrowing. Most importantly, Březina and collaborators (2022, DOI below) already give **general three-state NMR exchange resolvents and spectral formulas**. The rational expression here is an explicit special case and is **not** claimed to be novel. Their examined analysis of coalescence treats symmetric/asymmetric two-state exchange, and their consecutive three-state discussion treats a fast-process reduction; it does not state the present two exact thresholds or the global three/two/one maximum classification. Kovrigin (2012) investigates numerical three-state exchange regimes; the full text was not accessible for a decisive comparison, and could contain relevant graphical or implicit examples. The assessed contribution is only the exact all-rates peak-topology phase diagram and its two algebraic critical values. Existing general three-state formulas logically contain all the information needed to derive it, so priority against unexamined specializations remains a substantive risk.

## Limitations

The result concerns an ideal stationary, equal-population, equal-edge-rate, equally spaced three-state path with no intrinsic linewidth. Unequal exchange rates, a direct extreme-to-extreme jump, nonzero homogeneous broadening, nonstationary preparation, and experimental detection thresholds can change the visible peak pattern. A strict mathematical local maximum need not correspond to an experimentally resolvable line. This is neither a claim about independent bulk thermodynamic phases nor a claim that the general three-state resolvent is new.

## References

- Y. Komijani and P. Coleman, *Majorana approach to the stochastic theory of lineshapes*, initially public April 18, 2016, https://arxiv.org/abs/1604.05190.
- Březina and collaborators, *NMR lineshape analysis using analytical solutions of multi-state chemical exchange with applications to kinetics of host–guest systems*, *Scientific Reports* (2022), https://doi.org/10.1038/s41598-022-20136-4 ; open full text https://pmc.ncbi.nlm.nih.gov/articles/PMC9576801/.
- E. L. Kovrigin, *NMR line shapes and multi-state binding equilibria*, *Journal of Biomolecular NMR* 53 (2012), 257–270, https://doi.org/10.1007/s10858-012-9636-3 ; accessible abstract https://epublications.marquette.edu/chem_fac/221/.
- C. Feng, E. L. Kovrigin and C. B. Post, *NmrLineGuru: Standalone and User-Friendly GUIs for Fast 1D NMR Lineshape Simulation and Analysis of Multi-State Equilibrium Binding Models*, *Scientific Reports* (2019), https://doi.org/10.1038/s41598-019-52451-8.
