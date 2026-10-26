# Cauchy rigidity of fourth-order mode correlations under global resetting

## Finding
Consider \(m\ge 2\) independent Ornstein–Uhlenbeck coordinates between simultaneous Poisson resets to zero. Although all distinct coordinates have zero ordinary covariance in stationarity, their normalized connected fourth moments form an **exact Cauchy matrix**. The matrix admits an exact converse realization criterion, determines every damping-to-reset-rate ratio, and detects the number of distinct relaxation rates through its rank.

Precisely, for every \(i,j\in\{1,\ldots,m\}\), set \(M_i=\mathbb E[X_i^2]>0\) and
\[
F_{ij}:=\frac{\operatorname{cum}(X_i,X_i,X_j,X_j)}{(1+2\delta_{ij})M_iM_j}.
\]
Then, writing \(b_i=2\gamma_i/r\),
\[
\boxed{F_{ij}=\frac{1}{1+b_i+b_j},\qquad b_i>0.}
\]
In particular, the off-diagonal power correlations are determined by the single-mode excess kurtoses \(\kappa_i:=\mathbb E[X_i^4]/M_i^2-3=3F_{ii}\):
\[
\boxed{\frac{\operatorname{Cov}(X_i^2,X_j^2)}{M_iM_j}
=\frac{2\kappa_i\kappa_j}{3(\kappa_i+\kappa_j)}}\quad(i\ne j).
\]
Conversely, for arbitrary positive target values \(M_i\) and a real symmetric array \(F\), there exists **some** globally reset collection of independent positive-noise, positive-damping Ornstein–Uhlenbeck modes with these second moments and normalized fourth cumulants if and only if \(0<F_{ii}<1\) for each \(i\), and \(F_{ij}=2F_{ii}F_{jj}/(F_{ii}+F_{jj})\) for each \(i\ne j\). In every realization the ratios \(\gamma_i/r\) are uniquely determined, but the common time scale is not.

If all \(b_i\) are pairwise distinct, \(F\) is strictly totally positive when rows and columns are ordered by increasing \(b_i\), and
\[
\boxed{\det F=\frac{\prod_{1\le i<j\le m}(b_j-b_i)^2}{\prod_{i,j=1}^{m}(1+b_i+b_j)}>0.}
\]
With repeated values, \(\operatorname{rank}(F)\) is exactly the number of distinct \(b_i\). These conclusions apply without finite-size approximation to every finite selection of nonzero real Fourier modes of a periodically bounded Edwards–Wilkinson (EW) interface, with \(\gamma_i=\nu k_i^2\).

## Assumptions and scope
Let \(m\) be any integer at least two, \(r>0\), and \(\gamma_i,D_i>0\). Between resets let
\[
\mathrm dX_i(t)=-\gamma_iX_i(t)\,\mathrm dt+\sqrt{2D_i}\,\mathrm dW_i(t),
\]
where the \(W_i\) are independent standard real Brownian motions. One *common*, independent, rate-\(r\) Poisson clock instantaneously sends all coordinates to zero. Expectations are in the unique stationary law. For centered real variables, \(\operatorname{cum}(X_i,X_i,X_j,X_j)=\mathbb E[X_i^2X_j^2]-M_iM_j-2(\mathbb E[X_iX_j])^2\). The convention \(\delta_{ij}\) is the Kronecker delta, so the diagonal normalization divides the ordinary fourth cumulant by three.

For the EW specialization, consider \(\partial_t H=\nu\partial_x^2 H+\sqrt{2D}\,\xi\) on a periodic circle of length \(L>0\), reset everywhere to the flat height profile at rate \(r\). Remove the spatial mean and project onto any finite collection of distinct, real, \(L^2\)-orthonormal, nonzero sine/cosine Fourier modes with wave numbers \(k_i=2\pi n_i/L\), \(n_i\ne0\). Their amplitudes obey the stated independent OU equations, with \(\gamma_i=\nu k_i^2\) and \(D_i=D\). No limit in \(L\) or number of selected modes is needed. Conversely allowing arbitrary positive \(\gamma_i\) gives a broader collection of diagonal linear interface modes; not every such collection is the spectrum of one fixed periodic EW Laplacian.

## Proof
**Step 1: regeneration and the stationary mixture.** Because resets occur at rate \(r>0\) independently of the Brownian drivers, stationarity can be constructed by starting at zero at the most recent reset. The elapsed age \(A\) is exponentially distributed with density \(r e^{-ra}\) for \(a\ge0\), independently of the Brownian increments since that reset. Conditional on \(A=a\), the \(X_i\) are independent centered Gaussians with variances
\[
V_i(a)=\frac{D_i}{\gamma_i}\bigl(1-e^{-2\gamma_i a}\bigr).
\]
The construction is stationary and unique: two copies coupled to the same clock and subsequent Brownian increments agree after the first joint reset. All fourth moments exist since \(V_i(a)\le D_i/\gamma_i\). In particular \(\mathbb E[X_iX_j]=0\) when \(i\ne j\).

**Step 2: connected fourth moments.** Let \(a_i=2\gamma_i\) and \(c_i=D_i/\gamma_i\). The exponential Laplace transform gives
\[
M_i=\mathbb E[V_i(A)]=c_i\frac{a_i}{r+a_i}=\frac{2D_i}{r+2\gamma_i}.
\]
For all \(i,j\),
\[
\operatorname{Cov}(V_i(A),V_j(A))
=c_ic_j\left(\frac{r}{r+a_i+a_j}
-\frac{r^2}{(r+a_i)(r+a_j)}\right)
=c_ic_j\frac{r a_i a_j}{(r+a_i+a_j)(r+a_i)(r+a_j)}.
\]
By conditional Gaussianity, the fourth cumulant for \(i\ne j\) is this covariance. For \(i=j\), \(\mathbb E[X_i^4]=3\mathbb E[V_i(A)^2]\), so the fourth cumulant is exactly three times the same covariance. Dividing by \((1+2\delta_{ij})M_iM_j\) yields \(F_{ij}=r/(r+a_i+a_j)\), proving the Cauchy law. Setting \(i=j\) yields \(\kappa_i=3r/(r+2a_i)\); elementary elimination of \(a_i/r\) proves the harmonic-mean cross-cumulant formula.

**Step 3: complete inverse range.** Necessarily \(F_{ii}=(1+2b_i)^{-1}\in(0,1)\) and \(b_i=(F_{ii}^{-1}-1)/2\). Therefore for \(i\ne j\), \(F_{ij}=(1+b_i+b_j)^{-1}=2F_{ii}F_{jj}/(F_{ii}+F_{jj})\). For sufficiency assume these relations, choose any \(r>0\), and define
\[
\gamma_i=\frac r4(F_{ii}^{-1}-1)>0,\qquad
D_i=\frac{M_i}{2}(r+2\gamma_i)>0.
\]
Then the OU-plus-common-reset model just constructed has the required \(M_i\) and \(F\). The ratios \(\gamma_i/r\) are forced by the diagonals. Multiplying simultaneously \(r,\gamma_i,D_i\) by the same positive factor changes physical time but not these stationary normalized moments, establishing the stated nonidentifiability of the absolute rate.

**Step 4: determinant, total positivity, and rank.** Apply the Cauchy determinant identity to \(F_{ij}=1/(u_i+v_j)\), with \(u_i=b_i\), \(v_j=1+b_j\). It gives the displayed determinant formula. The same identity holds for every square minor, with positive products of strictly increasing row and column parameter differences; hence every such minor is positive when the corresponding \(b_i\) are distinct and ordered. If some \(b_i\) coincide, their rows coincide, so the rank is at most the number of distinct values. The principal submatrix indexed by one representative of each value has positive determinant, giving the opposite inequality.

**Step 5: common versus independent clocks.** Replace the shared reset clock by independent rate-\(r\) Poisson clocks, one for each mode, leaving all OU parameters unchanged. Every individual stationary mode has exactly the same law as before, and therefore the same \(M_i\) and \(\kappa_i\). But distinct modes are now independent, so \(\operatorname{Cov}(X_i^2,X_j^2)=0\) for \(i\ne j\). Under the common clock that covariance is strictly positive for every pair, by Step 2. Thus the cross-mode fourth moments detect global coordination despite identical one-mode statistics.

## Verification
The standalone `verify.py` checks the Laplace-moment construction, every element of \(F\), the harmonic-mean law, all square-minor signs, inverse reconstruction, and the Cauchy determinant against independent exact rational arithmetic for three finite parameter families. `verify_output.txt` gives the actual result. This arithmetic is supplementary; Steps 1–5 prove the statements for arbitrary finite \(m\) and all admissible real parameters. All formulae concern stationary distributional moments, not sample estimators or finite observational sequences.

## Relationship to prior work
Gupta, Majumdar, and Schehr (arXiv:1312.5954, initially public 2013-12-20) establish a whole-configuration renewal representation for resetting interfaces and derive one-point height laws. That representation is the starting principle for Step 1 and, in principle, contains joint statistics; the result here instead explicitly identifies a complete constrained **inverse range**, a Cauchy/total-positivity structure for connected modal fourth moments, relaxation-rate multiplicities, and the sharp common-clock versus separate-clock distinction. Rose, Touchette, Lesanovsky, and Garrahan (arXiv:1806.01298) give a general reset-generator spectral and stationary-state representation, without this fourth-cumulant inverse classification. Magoni, Carollo, Perfetto, and Lesanovsky (arXiv:2202.12655) exhibit reset-induced correlations in noninteracting *quantum spins*, not the Gaussian-interface Cauchy matrix or its inverse feasibility conditions. Nagar and Gupta (arXiv:2305.16955) review global versus local resetting and EW one-point statistics but do not give these pairwise modal covariance constraints.

The classical Cauchy determinant identity and Gaussian conditional fourth moments are standard mathematical ingredients, not new claims. The contribution is their exact combination into a falsifiable fourth-cumulant **realization and spectral-degeneracy theorem** for global resetting. A previously derived general configuration law remains a material priority risk: it formally entails all forward moments, even though the present converse criterion and strict rank/total-positivity structure are not stated there.

## Limitations
The converse realizes arbitrary positive diagonal OU rates, not arbitrary matrices as Fourier spectra of one fixed EW circle. The formulas assume independent Gaussian driving noises, zero resetting state, and a *single global Poisson clock*; correlated noise, non-Poisson renewal, partial resets, nonlinear KPZ dynamics, nonstationary data, and complex-amplitude power conventions are outside scope. If several modes share one decay rate (as sine and cosine partners do), the normalized Cauchy matrix is singular, although its entrywise formulas remain valid. A single stationary collection of moments determines only rate ratios, not the absolute clock speed. Explicitly identifying the inverse range is not a claim that all general full-distribution resetting representations were unknown, and the priority review remains non-independent.

## References
1. S. Gupta, S. N. Majumdar, and G. Schehr, “Fluctuating interfaces subject to stochastic resetting,” arXiv:1312.5954v1 (2013-12-20), https://arxiv.org/pdf/1312.5954 ; Phys. Rev. Lett. 112, 220601 (2014).
2. D. C. Rose, H. Touchette, I. Lesanovsky, and J. P. Garrahan, “Spectral properties of simple classical and quantum reset processes,” arXiv:1806.01298, https://arxiv.org/pdf/1806.01298 ; Phys. Rev. E 98, 022129 (2018).
3. M. Magoni, F. Carollo, G. Perfetto, and I. Lesanovsky, “Emergent quantum correlations and collective behavior in non-interacting quantum systems subject to stochastic resetting,” arXiv:2202.12655, https://arxiv.org/pdf/2202.12655 (2022).
4. A. Nagar and S. Gupta, “Stochastic resetting in interacting particle systems: A review,” arXiv:2305.16955v2, https://arxiv.org/html/2305.16955v2 (2023).
