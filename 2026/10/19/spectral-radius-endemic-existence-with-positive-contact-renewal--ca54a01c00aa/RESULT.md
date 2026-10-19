# Spectral-radius endemic existence with positive contact renewal in adaptive SIS networks

## Finding

**Theorem.** In a finite strongly connected heterogeneous adaptive SIS network whose contact-creation responses remain strictly positive at every nonsaturated prevalence state, a disease-free reproduction number greater than one guarantees at least one strictly positive endemic equilibrium. Precisely, under the assumptions below,
\[
\mathcal R_0=\rho(D^{-1}M)>1\quad\Longrightarrow\quad
0<y_i^*<1\ \text{for every }i,
\]
with equilibrium edge densities \(0<z_{ij}^*\le1\) on every permitted transmission edge. No monotonicity, differentiability, or Lipschitz assumption on the contact-response functions is needed for the *equilibrium-existence* conclusion beyond continuity and positive creation in the interior.

The source paper proves existence when a minimum row/column sum exceeds one and explicitly conjectures existence at the weaker spectral-radius threshold. The theorem establishes that conjectured implication for the nondegenerate contact-renewal class specified here; it does not settle the source's unrestricted case allowing contact-creation rates to vanish at an interior prevalence state.

## Assumptions and scope

Fix an integer \(n\ge2\). For \(1\le i,j\le n\), let recovery rates \(\delta_i>0\), transmission strengths \(\beta_{ij}\ge0\), breaking rates \(\zeta_{ij}\ge0\), and creation rates \(\xi_{ij}>0\) on edges with \(\beta_{ij}>0\). The nonnegative matrix \(B=(\beta_{ij})\) is irreducible; that is, its directed transmission graph is strongly connected. Edges with \(\beta_{ij}=0\) are omitted from the contact equations and are mathematically irrelevant to infection dynamics.

On every permitted transmission edge, the functions \(f^{\mathrm{br}}_{ij},f^{\mathrm{cr}}_{ij}:[0,1]^3\to[0,\infty)\) are continuous, and
\[
f^{\mathrm{cr}}_{ij}(u,v,w)>0\qquad(0\le u,v,w<1).
\]
They may vary by edge and need not be monotone; their values at saturated states may be zero. For \(\bar y=n^{-1}\sum_i y_i\), consider the continuous-time model
\[
\dot y_i=-\delta_i y_i+(1-y_i)\sum_j\beta_{ij}y_jz_{ij},\qquad
\dot z_{ij}=-\zeta_{ij}z_{ij}f^{\mathrm{br}}_{ij}(y_i,y_j,\bar y)
+\xi_{ij}(1-z_{ij})f^{\mathrm{cr}}_{ij}(y_i,y_j,\bar y).
\]
The state ranges are \(0\le y_i,z_{ij}\le1\). Define the disease-free edge level and infection matrix by
\[
z_{ij}^{0}=\frac{\xi_{ij}f^{\mathrm{cr}}_{ij}(0,0,0)}
{\zeta_{ij}f^{\mathrm{br}}_{ij}(0,0,0)+\xi_{ij}f^{\mathrm{cr}}_{ij}(0,0,0)},\qquad
M_{ij}=\beta_{ij}z_{ij}^{0},\qquad D=\operatorname{diag}(\delta_i).
\]
The threshold \(\mathcal R_0=\rho(D^{-1}M)\) equals \(\rho(MD^{-1})\), since the two matrices are similar by conjugation with \(D\). A strictly positive endemic equilibrium means \(0<y_i^*<1\) for every community and valid stationary edge densities.

## Proof

**1. Eliminate the contact variables on a compact nonsaturated box.** Let \(b_i=\sum_j\beta_{ij}>0\), and put \(c_i=b_i/(\delta_i+b_i)<1\). Set \(K=\prod_i[0,c_i]\). Because each coordinate and the arithmetic mean lie below one on \(K\), every on-edge stationary contact density is uniquely defined and continuous there:
\[
Z_{ij}(y)=\frac{\xi_{ij}f^{\mathrm{cr}}_{ij}(y_i,y_j,\bar y)}
{\zeta_{ij}f^{\mathrm{br}}_{ij}(y_i,y_j,\bar y)+\xi_{ij}f^{\mathrm{cr}}_{ij}(y_i,y_j,\bar y)}\in(0,1].
\]
For \(y\in K\), write \(\Lambda_i(y)=\sum_j\beta_{ij}Z_{ij}(y)y_j\) and define
\[
T_i(y)=\frac{\Lambda_i(y)}{\delta_i+\Lambda_i(y)}.
\]
Since \(0\le\Lambda_i(y)\le b_i\), the continuous map \(T\) maps \(K\) into itself, and its nonzero fixed points correspond exactly to endemic equilibria of the original equations, with \(z_{ij}^*=Z_{ij}(y^*)\).

**2. Positively weighted repulsion from the disease-free fixed point.** Continuity of \(Z\) gives the one-sided first-order expansion as \(y\to0\) through \(K\):
\[
T(y)=Ay+o(\|y\|_1),\qquad A=D^{-1}M.
\]
This conclusion does not require derivatives of \(f^{\mathrm{br}}\) or \(f^{\mathrm{cr}}\): the continuity error \(Z(y)-Z(0)=o(1)\) is multiplied by \(y_j\). The matrix \(A\) is nonnegative and irreducible because all existing disease-free edge levels are strictly positive. Its Perron–Frobenius left eigenvector \(w\) can therefore be chosen coordinatewise positive and normalized by \(\sum_iw_i=1\), so \(w^{\mathsf T}A=\mathcal R_0w^{\mathsf T}\). Because \(w^{\mathsf T}y\ge(\min_iw_i)\|y\|_1\) for \(y\ge0\), the expansion and \(\mathcal R_0>1\) give numbers \(\eta>0\) and \(r_0>0\) such that
\[
w^{\mathsf T}T(y)\ge(1+\eta)w^{\mathsf T}y
\quad\text{whenever }y\in K,\ 0<\|y\|_1<r_0.
\]

**3. A perturbation excludes the zero fixed point.** Choose any \(a\) with \(0<a_i<c_i\). For \(0<\varepsilon<1\), the map \(T_{\varepsilon}(y)=(1-\varepsilon)T(y)+\varepsilon a\) continuously maps the compact convex box \(K\) into itself. Brouwer's fixed-point theorem gives \(y_{\varepsilon}\in K\) with \(y_{\varepsilon}=T_{\varepsilon}(y_{\varepsilon})\); indeed \(y_{\varepsilon,i}\ge\varepsilon a_i>0\). If a sequence \(\varepsilon_k\downarrow0\) had \(y_{\varepsilon_k}\to0\), for sufficiently large \(k\) the preceding inequality and \((1-\varepsilon_k)(1+\eta)>1\) would yield
\[
w^{\mathsf T}y_{\varepsilon_k}
=(1-\varepsilon_k)w^{\mathsf T}T(y_{\varepsilon_k})+\varepsilon_kw^{\mathsf T}a
>(w^{\mathsf T}y_{\varepsilon_k}),
\]
a contradiction. Compactness thus supplies a subsequence converging to a nonzero fixed point \(y^*=T(y^*)\).

**4. No proper coordinate face contains a nonzero fixed point.** If \(y_i^*=0\), the fixed-point equation forces \(\Lambda_i(y^*)=0\). For each \(j\) with \(\beta_{ij}>0\), positivity of \(Z_{ij}(y^*)\) forces \(y_j^*=0\). Propagating this implication along directed paths and using irreducibility gives \(y^*=0\), a contradiction. Therefore every coordinate is positive. Every coordinate is also bounded by \(c_i<1\), and the defined \(z_{ij}^*=Z_{ij}(y^*)\) makes every contact derivative zero. All infection derivatives vanish by the fixed-point identity. This completes the proof.

## Verification

The self-contained Python program `verify.py` uses exact rational arithmetic to check stationary infection/contact equations and supercritical thresholds for \(722\) explicitly constructed heterogeneous two-community equilibria. It reports \(7959\) passed exact assertions. These examples **illustrate** the theorem; the infinite family and all finite directed networks are handled by the analytical proof above.

In particular, choose two communities with \(\delta_1=\delta_2=\xi_{12}=\xi_{21}=\zeta_{12}=\zeta_{21}=1\), \(\beta_{11}=\beta_{22}=0\), \(\beta_{12}=42\), \(\beta_{21}=2/7\), \(f^{\mathrm{br}}_{ij}=y_i+y_j\), and \(f^{\mathrm{cr}}_{ij}=1\). Then
\[
\mathcal R_0=\sqrt{12}>1,\quad
(y_1^*,y_2^*)=(7/10,1/10),\quad
z_{12}^*=z_{21}^*=5/9.
\]
Direct substitution yields infection forces \(7/3\) and \(1/9\), respectively, and both contact derivatives vanish. Nevertheless the minimum row sum of the source's reproduction matrix is \(2/7<1\), so its Theorem 5 does not certify this example.

## Relationship to prior work

Achterberg, Sensi and Sottile introduce precisely these prevalence and edge-density equations. Their Theorem 5 provides endemic existence under a stronger minimum row/column-sum hypothesis, while their Conjecture 6 asks for the spectral-radius criterion. The fixed-point argument above supplies that criterion within the explicitly stated positive-renewal regime; it neither claims the epidemic model nor Brouwer's or Perron–Frobenius theorems as new.

Wang, Gracy, Ishii and Johansson study a discrete-time SIS model with a specific controlled infection multiplier. Wang and collaborators subsequently investigate a different continuous-time SIS feedback controller. Their endemic results for specialized controlled infection equations do not directly imply stationary existence for the present *independently evolving*, heterogeneous, edge-specific contact densities with merely continuous responses.

## Limitations

The contact-creation positivity hypothesis is substantive: the proof requires each stationary link response to remain positive throughout a nonsaturated box. If creation vanishes at interior prevalence states, the quotient defining \(Z_{ij}\) can be undefined or zero and the irreducibility propagation argument can fail. Thus the theorem is **not** an unrestricted proof of the source's Conjecture 6. It concerns equilibrium existence only; uniqueness, stability, convergence of trajectories, and models with other compartments are not established. Even within the allowed class, the result does not preclude multiple endemic equilibria or oscillatory solutions. The finite verification code is not a proof of arbitrary-network existence.

## References

1. M. A. Achterberg, M. Sensi and S. Sottile, *A minimal model for multigroup adaptive SIS epidemics*, arXiv:2407.17639 (first public version, July 24, 2024); *Chaos* 35, 033127 (2025), doi:10.1063/5.0246228. In particular equations (2)–(4), Theorem 5 and Conjecture 6.
2. Y. Wang, S. Gracy, H. Ishii and K. H. Johansson, *Suppressing the endemic equilibrium in SIS epidemics: A state dependent approach*, arXiv:2106.00122 (2021).
3. Y. Wang, S. Gracy, C. A. Uribe, H. Ishii and K. H. Johansson, *A State Feedback Controller for Mitigation of Continuous-Time Networked SIS Epidemics*, arXiv:2210.04169 (2022).
