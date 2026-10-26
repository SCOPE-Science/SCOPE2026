# Sharp total-depth allocation maximizing the slowest multilayer internal-wave speed

## Finding
For an arbitrary integer \(N\ge2\), fix total fluid depth \(H>0\) and positive reduced gravities \(g'_j>0\) at the \(N-1\) interfaces. The strictly positive thicknesses \(h_1,\dots,h_N\) may vary subject only to \(\sum_{i=1}^{N}h_i=H\). Let \(c_{\mathrm{slow}}\) be the smallest of the \(N-1\) positive, linear, hydrostatic internal-wave phase speeds under a rigid lid. Define
\[
a_0=a_N=0,\qquad a_j=\frac{1}{g'_j}\ (1\le j<N),\qquad S=\sum_{j=1}^{N-1}a_j.
\]
**Theorem.** The sharp universal bound and its unique equality case are
\[
c_{\mathrm{slow}}(h)^2\le\frac{H}{4S},\qquad
h_i=h_i^*:=\frac{H(a_{i-1}+a_i)}{2S}\quad(1\le i\le N).
\]
Every other positive allocation has a strictly smaller slowest squared speed. At the unique optimizer, the slowest interface-displacement eigenvector is, up to nonzero scalar,
\[
\eta_j^*=(-1)^{j-1}a_j\qquad(1\le j<N).
\]
For three layers, \(h_2^*=H/2\); the other two depths split the remaining half in the ratio \(a_1:a_2\). The two positive baroclinic squared speeds at this allocation have ratio \(1:2\). For two layers, the result specializes to the familiar equal-depth allocation.

## Assumptions and scope
The model is an inviscid, incompressible, hydrostatic, **Boussinesq** stack of \(N\) immiscible uniform-density layers, without mean current or rotation, between fixed horizontal rigid lids. Each density jump appears only through a prescribed positive reduced gravity \(g'_j\); no other density dependence is retained in the Boussinesq approximation. The total depth and jumps are independently fixed while the layer depths vary. We consider linear long horizontal waves, equivalently the zero-wavenumber limit of their phase speeds, and exclude the barotropic surface mode by the rigid-lid condition. Layer thicknesses are strictly positive, and interface indices increase consistently through the stack.

Let \(\eta_j\) be the vertical displacement of interface \(j\), with \(\eta_0=\eta_N=0\). The linearized thickness conservation and momentum-jump equations for a traveling wave of positive phase speed \(c\) imply
\[
c^2\left(\frac{\eta_j-\eta_{j-1}}{h_j}-\frac{\eta_{j+1}-\eta_j}{h_{j+1}}\right)=g'_j\eta_j\qquad (1\le j<N).
\]
Equivalently, \(K(h)\eta=c^{-2}D\eta\), where \(D=\operatorname{diag}(g'_1,\dots,g'_{N-1})\) and \(K(h)\) is the positive definite Jacobi matrix with \(K_{jj}=h_j^{-1}+h_{j+1}^{-1}\) and \(K_{j,j+1}=K_{j+1,j}=-h_{j+1}^{-1}\). Hence
\[
c_{\mathrm{slow}}(h)^2=\lambda_{\max}\!\left(D^{-1/2}K(h)D^{-1/2}\right)^{-1}.
\]
All denominators are positive and all \(N-1\) internal speeds are real and positive.

## Proof
**1. A universal test displacement.** Set \(v_0=v_N=0\) and \(v_j=(-1)^{j-1}a_j\) for \(1\le j<N\). Since \(a_j>0\), the successive jumps obey
\[
|v_i-v_{i-1}|=a_{i-1}+a_i>0,\qquad
\sum_{i=1}^{N}|v_i-v_{i-1}|=2S.
\]
Also \(v^TDv=\sum_{j=1}^{N-1}g'_j a_j^2=S\). For every positive allocation, the Rayleigh principle and weighted Cauchy–Schwarz yield
\[
\begin{aligned}
\lambda_{\max}(D^{-1/2}KD^{-1/2})
&\ge\frac{v^TKv}{v^TDv}
=\frac{1}{S}\sum_{i=1}^{N}\frac{(v_i-v_{i-1})^2}{h_i}\\
&\ge\frac{1}{SH}\left(\sum_{i=1}^{N}|v_i-v_{i-1}|\right)^2
=\frac{4S}{H}.
\end{aligned}
\]
This gives \(c_{\mathrm{slow}}^2\le H/(4S)\). Cauchy–Schwarz is an equality only when \(h_i\) is proportional to the strictly positive quantity \(|v_i-v_{i-1}|=a_{i-1}+a_i\). The fixed total depth then forces the unique allocation \(h_i=h_i^*\). Consequently, every other allocation has a **strict** bound, provided that equality is achievable.

**2. Attainment and identity of the slowest mode.** For the proposed allocation,
\[
\frac{v_i-v_{i-1}}{h_i^*}=(-1)^{i-1}\frac{2S}{H}
\quad (1\le i\le N),
\]
where the last difference uses \(v_N=0\). Taking successive differences gives the exact eigenvalue equation
\[
K(h^*)v=\frac{4S}{H}Dv.
\]
To show this eigenvalue is **largest**, rather than merely some eigenvalue, set \(B=D^{-1/2}K(h^*)D^{-1/2}\) and \(J=\operatorname{diag}(1,-1,1,\ldots)\). The symmetric tridiagonal matrix \(JBJ\) has strictly positive diagonal entries and strictly positive nearest-neighbor off-diagonal entries. For \(N\ge3\), it is irreducible and entrywise nonnegative. The eigenvector \(JD^{1/2}v\) has strictly positive entries \(\sqrt{a_j}\), so the Perron–Frobenius theorem shows that the eigenvalue \(4S/H\) is the simple spectral maximum. For \(N=2\), the same assertion holds directly for the positive scalar matrix. Hence the upper speed bound is attained and the optimizer is unique.

**3. Three-layer spectral ratio.** For \(N=3\), the maximizing thicknesses are \((H a_1/(2S),H/2,H a_2/(2S))\). The trace of \(D^{-1/2}K(h^*)D^{-1/2}\) is \(6S/H\), whereas its largest eigenvalue is \(4S/H\). Its other eigenvalue is therefore \(2S/H\), and the corresponding squared speeds are \(H/(4S)\) and \(H/(2S)\), respectively. This proves the stated ratio without an assumption of equal density jumps.

## Verification
The standalone script `check_layers.py` constructs the tridiagonal matrix from the independent layer-gradient outer-product formula and computes its generalized eigenvalues. With deterministic seed `7302026`, it tests all integers \(2\le N\le17\), 200 randomly chosen positive gravities and depths per \(N\), and independently perturbed positive allocations. It passes 3,200 optimum-eigenvalue checks, 3,200 global-bound checks, 3,200 strict-uniqueness checks, 3,200 eigenvector-residual checks, 200 three-layer speed-ratio checks, and 200 two-layer consistency checks: **13,200 successful assertions**. These finite calculations corroborate the formulas; universal validity and exact equality conditions follow solely from the proof above. Reproduce with `python check_layers.py` using NumPy and SciPy.

## Relationship to prior work
The long-wave internal-mode spectral problem is classical. Shimizu (2011) gives a multilayer modal framework and orthogonality, including three-layer expressions, rather than an identified fixed-total-depth global maximizer of the slowest phase speed in the material available for examination. De Melo Viríssimo and Milewski (2019) derive and study three-layer rigid-lid shallow-water equations, their internal modes, and nonlinear simple waves; their accessible full manuscript was inspected and does not present the all-layer sharp allocation theorem. Earlier two-layer depth dependence is recovered as a boundary case, not claimed as new. The Rayleigh quotient, Cauchy–Schwarz, and Perron–Frobenius principles used here are established mathematical tools; the assessed contribution is their exact global allocation consequence for the entire multilayer physical family.

## Limitations
The conclusion is for the **smallest positive long-wave internal-mode speed** with a *fixed* total depth and *fixed* reduced gravities, not for the largest speed, mode averages, nonlinear wave amplitude, finite-wavelength dispersion, arbitrary shear, free-surface dynamics, rotational effects, or non-Boussinesq density contrasts. Changing interface buoyancy jumps together with thicknesses defines a different optimization problem. The 2011 primary source's complete publisher PDF was not accessible, so precise historical priority beyond the examined sections and abstracts requires additional review; absence from a search result does not certify novelty. The mathematical statement here needs no inaccessible lemma from that source because the finite spectral proof is self-contained.

## References
1. K. Shimizu, “A Theory of Vertical Modes in Multilayer Stratified Fluids,” *Journal of Physical Oceanography* 41 (2011), 1694–1707. DOI: https://doi.org/10.1175/2011JPO4546.1.
2. F. de Melo Viríssimo and P. A. Milewski, “Three-layer Flows in the Shallow Water Limit,” *Studies in Applied Mathematics* (2019). Lawful institutional author manuscript: https://nora.nerc.ac.uk/id/eprint/527073/1/2018-SAPM-deMeloVirissimoMilewskiREVISION.pdf.
