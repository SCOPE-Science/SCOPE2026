# An isolated oscillatory Neumann mode without stationary instability in a public-goods reaction–diffusion system

## Finding
For the three-component public-goods population/resource reaction–diffusion equations of Zhao, Zhu, Zhang and Cooney, there exist **strictly positive rational reaction and diffusion parameters** for which a strictly positive spatially homogeneous coexistence state is linearly stable in the spatially uniform mode but unstable to **exactly one nonconstant Neumann spatial mode**. That mode has an exponentially growing nonreal complex-conjugate eigenvalue pair; every other spatial mode is strictly stable. Moreover, every modal characteristic polynomial has strictly positive coefficients at **every continuous squared wavenumber** \(q\ge 0\), so no stationary (real-eigenvalue) diffusion-driven instability can occur at any wavenumber. This gives an exact pure oscillatory diffusion-driven instability within the unbiased public-goods model, distinct from the stationary patterns obtained in the motivating paper's small-cooperator-diffusion regime.

## Assumptions and scope
On the interval \((0,\pi)\), use homogeneous Neumann conditions for all three fields and consider the **unbiased** system
\[
\begin{aligned}
 \partial_t u&=D_u\partial_{xx}u+u(r_u\phi-c-\gamma(u+v)-\mu_u),\\
 \partial_t v&=D_v\partial_{xx}v+v(r_v\phi-\gamma(u+v)-\mu_v),\\
 \partial_t\phi&=D_\phi\partial_{xx}\phi+cu-[\kappa(u+v)+\delta]\phi.
\end{aligned}
\]
The fields \(u,v,\phi\) are cooperator density, defector density and public-good concentration. All reaction and diffusion parameters below are strictly positive; the taxis coefficients are zero. Set
\[
\begin{gathered}
 D_u=1,\quad D_v=D_\phi=\frac1{10},\quad \gamma=\frac12,\quad \kappa=10,\quad \delta=\frac1{20},\\
 c=21,\quad r_u=\frac{431}{20},\quad r_v=\frac{541}{20},\quad \mu_u=\frac12,\quad \mu_v=27.
\end{gathered}
\]
All modes refer to the spectral linearization at the spatially uniform **positive** equilibrium
\[(u_*,v_*,\phi_*)=(1/20,1/20,1).\]
Linear growth does not assert a nonlinear time-periodic pattern. The primary assertion concerns exactly the stated parameter set; strict linear inequalities imply a neighborhood of parameters with the same single-mode instability.

## Proof
**Equilibrium.** Substitution of \((1/20,1/20,1)\) gives both per-capita growth rates zero:
\[
 \frac{431}{20}-21-\frac1{20}-\frac12=0,\qquad
 \frac{541}{20}-\frac1{20}-27=0.
\]
The resource balance is \(21/20=(1+1/20)\cdot1\), as required.

**Exact modal matrix.** For the Neumann eigenfunction \(\cos(kx)\), \(k=0,1,2,\dots\), write \(q=k^2\). The linearization is
\[
M(q)=\begin{pmatrix}
 -q-1/40 & -1/40 & 431/400\\
 -1/40 & -q/10-1/40 & 541/400\\
 11 & -10 & -q/10-21/20
\end{pmatrix}.
\]
The characteristic polynomial \(\det(zI-M(q))=z^3+a_1(q)z^2+a_2(q)z+a_3(q)\) has **exact** coefficients
\[
\begin{aligned}
 a_1(q)&=\frac{12q+11}{10},\\
 a_2(q)&=\frac{84q^2+475q+690}{400},\\
 a_3(q)&=\frac{80q^3+862q^2+98949q+1155}{8000}.
\end{aligned}
\]
Each coefficient is strictly positive for every \(q\ge0\). In particular \(p_q(z)>0\) for \(z\ge0\), which excludes nonnegative **real** eigenvalues at every wavenumber, not merely at Neumann frequencies.

**Exact stability dichotomy.** The remaining cubic Routh–Hurwitz quantity is
\[
H(q):=a_1(q)a_2(q)-a_3(q)
=\frac{1936q^3+12386q^2-71939q+14025}{8000}.
\]
We have \(H(0)=561/320>0\), \(H(1)=-5449/1000<0\), and \(H(4)=48349/8000>0\). Its numerator has exactly two sign changes in descending coefficient order, hence by Descartes's rule of signs at most two positive roots counted with multiplicity. The two strict changes of sign across the intervals \((0,1)\) and \((1,4)\) provide at least two distinct positive roots. Therefore exactly two simple positive roots \(\alpha\in(0,1)\), \(\beta\in(1,4)\) exist, and
\[
H(q)\begin{cases}>0,&0\le q<\alpha\text{ or }q>\beta,\\<0,&\alpha<q<\beta.\end{cases}
\]
For positive \(a_1,a_2,a_3\), cubic Routh–Hurwitz gives strict Hurwitz stability exactly when \(H>0\). When \(H<0\), the real polynomial has exactly one negative real eigenvalue and an unstable nonreal conjugate pair. To see the latter without assuming a general stability classification: a polynomial with all positive coefficients cannot have a nonnegative real root, so its real root is negative. If all three real roots were negative it would be Hurwitz stable, contradicting \(H<0\); thus the other two roots are nonreal conjugates. Their real part cannot be zero off \(H=0\), and the Routh sign count gives two right-half-plane roots because the first column \((1,a_1,H/a_1,a_3)\) has two sign changes. At either root of \(H\), \(p_q(z)=(z+a_1)(z^2+a_2)\) and the pair is exactly imaginary. Both crossings are transverse since those roots of \(H\) are simple.

**Discrete-mode selection.** The Neumann squares are \(0,1,4,9,\ldots\). Only \(q=1\) lies in \((\alpha,\beta)\); \(q=0\) and \(q\ge4\) have \(H>0\). Therefore \(k=1\) alone carries a growing conjugate pair, giving exactly two real unstable dimensions. The stable tail includes every higher integer mode, not a truncated numerical sample. Numerical root approximations are \(\alpha\approx0.2022201\) and \(\beta\approx3.5347728\), used for illustration only.

The asserted persistence under small positive parameter perturbations follows from the strict inequalities at \(q=0,1\), bounded-mode spectral continuity, and the uniform stabilizing large-frequency negative diffusion diagonal (the diffusions stay bounded away from zero). No claim is made about nonlinear patterned attractors.

## Verification
The accompanying standalone program `verify_wave_publicgoods.py` implements rational exact polynomial arithmetic. Running `python verify_wave_publicgoods.py` checks all equilibrium balances, reconstructs \(\det(zI-M(q))\) from the matrix entries by finite symbolic polynomial multiplication, verifies the three coefficient formulas and \(H\), and checks the exact signs at \(q=0,1,4\). Its numerical root output is illustrative; the all-frequency conclusion is proved analytically by Descartes's rule plus the sign changes and cubic Routh–Hurwitz.

## Relationship to prior work
Zhao, Zhu, Zhang and Cooney (2026), Sect. 3.2.1, established the unbiased public-goods PDE and its cubic modal criteria. Their paper emphasizes stationary Turing instability at large defector diffusivity and small cooperator/public-good diffusivity; Sect. 3.2.3 explicitly identifies the search for oscillatory instabilities under other reaction and diffusion parameters as a problem for further study. The present exact positive-parameter construction meets that model-specific question and additionally establishes a complete one-mode instability census on \((0,\pi)\).

Piskovsky (2024/2025) proved necessary and sufficient **general three-species** conditions for stationary and oscillatory Turing instability. Those framework-level conditions are consistent with, but do not supply, the present specific constrained public-goods parameters, positivity/equilibrium verification, or complete discrete Neumann mode classification. The existence of oscillatory diffusion-driven instabilities in other three-species systems is established prior art; only this exact public-goods-model witness and its all-wavenumber spectral exclusion are proposed as the contribution. Similar finite-wavenumber wave-type constructions in distinct ecological or immunological systems do not imply this parameter-specific public-goods case.

## Limitations
This is a local **linear** stability theorem. It does not prove nonlinear periodic waves, sustained time oscillations, local Hopf bifurcation with a varying biochemical parameter, or long-time pattern selection. The rational parameters are an admissible mathematical regime, not an empirical calibration. Historical uniqueness is not proven; general multicomponent spectral methods and independently published constructions are related background. Open full-text comparisons were made for the motivating article and Piskovsky's general theorem, but literature coverage cannot be exhaustive.

## References
1. Y. Zhao, K. Zhu, Y. Zhang, D. B. Cooney, *Pattern Formation in a Spatial Public Goods Dilemma due to Diffusive or Directed Motion*, arXiv:2603.21025v1 (first posted March 22, 2026); *Bulletin of Mathematical Biology* **88** (2026), article 173. https://arxiv.org/abs/2603.21025 ; https://doi.org/10.1007/s11538-026-01733-0 .
2. V. Piskovsky, *Turing instabilities for three interacting species*, arXiv:2405.14682 (first posted May 23, 2024). https://arxiv.org/html/2405.14682v1 .
3. M. Villar-Sepulveda, A. Champneys, and A. Krause, *Designing reaction-cross-diffusion systems with Turing and wave instabilities* (2025); general construction literature, not a public-goods-specific witness. https://pmc.ncbi.nlm.nih.gov/articles/PMC12426155/ .
