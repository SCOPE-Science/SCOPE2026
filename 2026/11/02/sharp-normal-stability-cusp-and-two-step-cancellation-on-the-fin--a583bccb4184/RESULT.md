# Sharp normal-stability cusp and two-step cancellation on the finite incoherent Kuramoto manifold

## Finding
Consider the discrete-time globally coupled Kuramoto--Sakaguchi map with identical intrinsic frequencies,
\[
\theta_i^+=\theta_i+\omega+\frac K N\sum_{j=1}^N\sin(\theta_j-\theta_i-\alpha)\pmod{2\pi}.
\]
For every regular zero-first-harmonic configuration with \(\rho=|Z_2|<1\), the normal multipliers of its co-rotating fixed point are
\[
\lambda_\pm=1+\frac K2\left(c\pm\sqrt{\rho^2-\sin^2\alpha}\right),\quad c=\cos\alpha.
\]
Here the square root is taken in the complex plane when its argument is negative. The two transverse multipliers both lie strictly within the unit circle exactly if \(c<0\) and \(0<K<K_c\), where
\[
K_c=\begin{cases}
\dfrac{-4c}{1-\rho^2},&0\le\rho\le|\sin\alpha|,\\
\dfrac{4}{-c+\sqrt{\rho^2-\sin^2\alpha}},&|\sin\alpha|<\rho<1.
\end{cases}
\]
For every fixed lag with \(c<0\), this gain ceiling rises strictly up to \(\rho=|\sin\alpha|\) and then falls strictly; the maximum is \(4/(-c)\). All values of \(\rho\) are realizable for every even \(N\ge4\) by antipodally paired phases.

At the extremal geometry \(\alpha=2\pi/3\), \(\theta=(0,\pi/6,\pi,7\pi/6)\), the gain ceiling is \(8\); at gain \(K=4\), the transverse two-dimensional derivative is nonzero but its square is zero. Thus first-order transverse error vanishes after two iterates, although nonlinear error generally does not.

## Assumptions and scope
Fix an **even integer** \(N\ge4\), real common frequency \(\omega\), lag \(\alpha\in\mathbb R\), and gain \(K>0\). Write
\[
Z_1=N^{-1}\sum_j e^{i\theta_j},\qquad Z_2=N^{-1}\sum_j e^{2i\theta_j},\qquad\rho=|Z_2|.
\]
The zero-first-harmonic set \(\mathcal M=\{Z_1=0\}\) consists of fixed points after subtracting the uniform phase rotation. The regular stratum is \(\mathcal M_{\rm reg}=\{Z_1=0,\rho<1\}\). At \(\rho=1\), the differential of the two real constraints can lose rank, and no codimension-two assertion is made. Stability here means strict spectral contraction in the two directions normal to the regular stratum; all tangent eigenvalues equal one, so pointwise asymptotic stability is not asserted.

## Proof
**Step 1: invariant manifold.** The coupling sum equals \(N\operatorname{Im}(e^{-i(\theta_i+\alpha)}Z_1)\). Therefore it vanishes on \(\mathcal M\), and each state rotates by the same frequency \(\omega\). Co-rotation makes the state fixed; equivariance makes its derivative independent of this rotation.

**Step 2: rank-two Jacobian.** Set \(c_i=\cos\theta_i\), \(s_i=\sin\theta_i\), \(Q=[c\ s]\), and
\[
R_\alpha=\begin{pmatrix}\cos\alpha&\sin\alpha\\-\sin\alpha&\cos\alpha\end{pmatrix}.
\]
Direct differentiation at \(Z_1=0\) eliminates the diagonal mean-field term and yields
\[
J=I_N+\frac K N Q R_\alpha Q^{\mathsf T}.
\]
The Gram matrix \(G=N^{-1}Q^{\mathsf T}Q\) has trace \(1\) and determinant \((1-\rho^2)/4\); this follows by expressing \(\cos^2\theta\), \(\sin^2\theta\) and \(\sin\theta\cos\theta\) using \(Z_2\). When \(\rho<1\), \(G\) is positive definite, \(Q\) has rank two and the tangent space \(\ker Q^{\mathsf T}\) has dimension \(N-2\). On the \(Q\)-coordinate complement, the induced derivative is exactly \(L=I_2+K R_\alpha G\). Its trace and determinant are
\[
\operatorname{tr}L=2+Kc,\qquad \det L=1+Kc+\frac{K^2}{4}(1-\rho^2).
\]
The discriminant is \(K^2(\rho^2-\sin^2\alpha)\), proving the multipliers and the remaining \(N-2\) unit tangent multipliers.

**Step 3: sharp Schur region.** For a real monic quadratic with the two multipliers as roots, strict containment in the unit circle is equivalent to
\[
1-\det L>0,\quad 1-\operatorname{tr}L+\det L>0,\quad 1+\operatorname{tr}L+\det L>0.
\]
The middle term is \(K^2(1-\rho^2)/4>0\). The first term requires \(c<0\) and \(K<-4c/(1-\rho^2)\). When \(\rho<|\sin\alpha|\), the last term is strictly positive because the two multipliers are conjugate, and the determinant boundary is first. When \(\rho>|\sin\alpha|\), the multipliers are real and both move monotonically below one; the more negative one reaches \(-1\) at \(K=4/(-c+\sqrt{\rho^2-\sin^2\alpha})\). Equality of discriminant produces a double multiplier, and both formulas agree. At \(c\ge0\), strict Schur contraction is impossible, since \(\det L\ge1\).

**Step 4: optimizing the geometry.** For fixed \(c<0\), the determinant boundary \(-4c/(1-\rho^2)\) increases strictly with \(\rho>0\), while the real-multiplier boundary \(4/(-c+\sqrt{\rho^2-\sin^2\alpha})\) decreases strictly above \(|\sin\alpha|\). Their shared value is \(4/(-c)\), the global maximum. When \(\sin\alpha=0\) and \(c<0\) (lag \(\pi\) modulo \(2\pi\)), this maximizer sits at the endpoint \(\rho=0\) rather than at an interior cusp. For every even \(N=2m\ge4\), select \(m\) phases \(\phi_j\) and their antipodes. Then \(Z_1=0\) and \(Z_2=m^{-1}\sum_{j=1}^m e^{2i\phi_j}\). The modulus varies continuously from zero (choose equally spaced doubled phases) to one (choose all doubled phases equal), so the intermediate-value theorem realizes each \(\rho\in[0,1)\) for every such \(N\). Explicitly for four phases, \((0,\phi,\pi,\pi+\phi)\) with \(\cos\phi=\rho\) has \(|Z_2|=\rho\).

**Step 5: exact two-step cancellation.** For \(\alpha=2\pi/3\), \(\phi=\pi/6\), the four-phase Gram matrix and lag rotation are
\[
G=\begin{pmatrix}7/8&\sqrt3/8\\\sqrt3/8&1/8\end{pmatrix},\qquad R_\alpha=\begin{pmatrix}-1/2&\sqrt3/2\\-\sqrt3/2&-1/2\end{pmatrix}.
\]
At \(K=4\),
\[
L=I_2+4R_\alpha G=\begin{pmatrix}0&0\\-2\sqrt3&0\end{pmatrix},\qquad L\ne0,\quad L^2=0.
\]
Its transverse multiplier pair is \((0,0)\), the exact non-semisimple cancellation. At \(K=8\) the multiplier pair is \((-1,-1)\), so the threshold is sharp.

## Verification
Run the standalone \(\texttt{check\_incoherent.py}\) script with Python 3, NumPy, and SymPy. It checks the exact symbolic Gram matrix, characteristic invariants, nonzero nilpotent transverse block, and gain-eight boundary. It also compares 750 independently constructed antipodal configurations against the full Jacobian spectrum and checks 120 strict-Schur parameter configurations on both sides of the computed gain ceiling. The maximum computed eigenvalue discrepancy was below \(1.2\times10^{-14}\). Two explicit nonlinear iterations from perturbed four-phase states also give strictly positive order-parameter residuals scaling quadratically with the perturbation, consistent with linear-only cancellation. These finite tests do not replace the all-parameter proof above.

## Relationship to prior work
Gade and Gupta (2026, arXiv:2609.22715v1) introduce and study a discrete-time Kuramoto model with phase lag, emphasizing continuum distributed-frequency stability and numerically investigated finite-size phenomena. Their accessible abstract does not assert the present all-lag, finite-identical-frequency second-harmonic normal spectrum, sharp gain cusp, or exact two-step derivative cancellation; their full text was not available for line-by-line comparison, leaving an explicit priority risk. Ashwin, Bick and Burylko (2016) discuss incoherent or antiphase configurations and their continuous-time phase-oscillator stability; the existence of such configurations and the general rank-two trigonometric reduction are not claimed as inventions here. Separate full-text published results concerning a quadrature unequal two-cluster return and a repulsive all-to-all parity effect do not classify the arbitrary-lag strict-Schur normal gain bound at zero first harmonic. The new asserted classification concerns the **discrete-time** strict-Schur gain boundary and its geometry optimization.

## Limitations
All results concern the first derivative at a regular zero-first-harmonic configuration, not global attraction or uniformly stable convergence across all of \(\mathcal M\). Tangential modes remain neutral. In particular, \(L^2=0\) is **linear** two-step cancellation, not finite-time extinction in the nonlinear map. On the boundary \(K=K_c\), a multiplier lies on the unit circle, and nonlinear boundary dynamics is not classified. The singular configurations \(\rho=1\), heterogeneous frequencies, non-global networks, and noisy models are excluded. Historical priority is provisional because the motivating paper's entire primary text was unavailable, though its public abstract and independently accessible related primary literature were compared.

## References
1. P. M. Gade and S. Gupta, *Discrete-time Kuramoto model with phase lag: Linear stability analysis and onset of synchronization*, arXiv:2609.22715v1, first submitted 2026-09-19, https://arxiv.org/abs/2609.22715.
2. P. Ashwin, C. Bick and O. Burylko, *Identical Phase Oscillator Networks: Bifurcations, Symmetry and Reversibility for Generalized Coupling*, *Frontiers in Applied Mathematics and Statistics* **2** (2016), article 7, https://doi.org/10.3389/fams.2016.00007.
3. *Sharp no-slip locking and logarithmic relaxation at quadrature phase lag*, available online 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-no-slip-locking-and-logarithmic-relaxation-at-quadrature-p--2becd3787aa1.
4. *Odd-even relaxation dichotomy for discrete repulsive all-to-all phase networks*, available online 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-odd-even-relaxation-dichotomy-for-discrete-repulsive-all-to-all--d8909b4a83b3.
