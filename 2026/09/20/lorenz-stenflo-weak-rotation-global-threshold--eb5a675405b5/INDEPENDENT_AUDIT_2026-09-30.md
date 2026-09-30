# Independent Audit — 2026-09-30

**Record:** `2026/09/20/lorenz-stenflo-weak-rotation-global-threshold--eb5a675405b5`  
**Title:** Exact weak-rotation global stability threshold for the Lorenz–Stenflo origin  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `c5a2838c0e1508bfe79ba045d054fa00b83c5614`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The global-threshold proof is correct. Under s=(sigma^2-k^2)/3 with 0<=k<sigma, the displayed storage matrix has determinant (sigma-k)^2(2sigma-k)/(3sigma^2(2sigma+k))>0 and positive leading entry. Independent symbolic expansion gives exactly M y^2-x y-dS/dt=psi^2/2. Adding the (y,z)-energy balance yields Vdot=-(1-rho M)y^2-beta z^2-(rho/2)psi^2, and 1/M=1+s/sigma^2. For rho<rho_c the zero-dissipation set reduces to the origin. At rho=rho_c, z=0 implies xy=0; a complete bounded invariant trajectory cannot have x nonzero on an interval, so x=0. The remaining equations plus invariance of x=0 leave no nonzero complete bounded trajectory (including the sigma=1 resonance, whose nonzero solution grows backward). LaSalle therefore closes the nonhyperbolic equality case. For rho>rho_c the linear characteristic polynomial has negative constant term and hence a positive real root. The frequency calculation also checks: Re H(i omega) is maximized at omega=0 exactly for s<=sigma^2/3.
- **Originality — PASS:** The static pitchfork threshold itself is prior and correctly credited. Accessible Lorenz–Stenflo literature located covers local pitchfork/Hopf analysis, boundedness and attractive sets, numerical dynamics, or controlled synchronization. The 2026 Naser–Abdel Aal–Gumah paper concerns nonautonomous extended Lorenz-84 and high-order Lorenz–Stenflo systems with time-varying parameters, not the classical autonomous four-dimensional theorem. No located source states the explicit positive-definite storage factorization, the weak-rotation global iff threshold, or global attraction at the nonhyperbolic pitchfork equality. On that evidence the theorem package passes originality to the best of the accessible literature.
- **Scientific value — PASS:** The theorem upgrades a known local bifurcation boundary to an exact nonlinear global stability boundary over a nontrivial parameter region and resolves the delicate equality case. The transfer-function calculation also identifies a structural reason for the weak-rotation cutoff, making the result informative beyond a single Lyapunov estimate.

## Independent findings
- Independent symbolic algebra gives zero residual for the storage factorization and reproduces the determinant exactly.
- The equality case does not rely on hyperbolicity: the largest complete bounded invariant subset of the zero-dissipation set is only the origin.
- The derivative of Re H(i omega) as a function of omega^2 has its maximum at zero exactly when s<=sigma^2/3; for stronger rotation the storage mechanism ceases to be passivity-sharp.
- The 2026 generalized/nonautonomous Lorenz paper is not a statement about the same autonomous classical four-dimensional parameter threshold.

## Independent checks
- Symbolically re-expanded the storage identity and determinant using an independent algebra system.
- Re-derived the marginal LaSalle invariant-set argument, including the sigma=1 possibility in the remaining y,v subsystem.
- Differentiated the exact real transfer function with respect to omega^2 to confirm the s<=sigma^2/3 cutoff.
- Searched current Lorenz–Stenflo global-stability literature and compared the accessible statements with the exact filed claim.

## Literature evidence
- https://doi.org/10.1142/S0218127410025466 — Xavier–Rech (2010), local bifurcation/pitchfork and numerical dynamics context; the static threshold is prior.
- https://doi.org/10.3390/math7060513 — Zhang–Xiao (2019), global boundedness and globally attractive sets, not the exact origin-convergence threshold.
- https://doi.org/10.1007/s40324-026-00429-8 — Naser–Abdel Aal–Gumah (2026), nonautonomous generalized extended Lorenz-84/high-order Lorenz–Stenflo systems; different model class.
- https://doi.org/10.1088/0031-8949/53/1/015 — Stenflo (1996), source of the classical four-dimensional model.

## Limitations
- The iff threshold is proved only for 0<s<=sigma^2/3; strong rotation is not classified.
- The theorem concerns the autonomous classical Lorenz–Stenflo system and not controlled, stochastic, fractional, or high-order variants.
- Post-pitchfork dynamics are not classified.

The assigned source tree remained unchanged from the inventory/source-tree-check interval through current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the exact tree audited is `c5a2838c0e1508bfe79ba045d054fa00b83c5614` and matches the assignment guard. GitHub was used only as read-only evidence; no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific audit contract.
