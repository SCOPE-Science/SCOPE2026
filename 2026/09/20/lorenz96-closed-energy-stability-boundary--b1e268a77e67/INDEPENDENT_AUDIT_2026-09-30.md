# Independent Audit — 2026/09/20/lorenz96-closed-energy-stability-boundary--b1e268a77e67

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `8bf9352add83a918fc366f5b46ba57e74af72b66`
- Disposition: **PASSED**

## Correctness

**PASS** — The endpoint argument is correct. Centering at Fe gives ydot=G(y)+(FA-I)y and the exact energy identity (1/2)d||y||^2/dt=-y^T(I-FS)y, with S=(A+A^T)/2. Circulant diagonalization makes H=I-FS positive semidefinite exactly when max_k(Fr_k-1)<=0. At equality, polarization of x^TG(x)=0 at e gives e^TA=0 and e^TG(z)=-z^TAz. Since Ae=0, He=e; hence every y in ker H has e^Ty=0. For nonzero y in ker H, Hy=0 gives y^TAy=||y||^2/F and therefore d(e^Ty)/dt=-||y||^2/F !=0. Thus no nonzero trajectory can remain in the zero-dissipation set. The norm sublevel sets are compact and invariant, bounded solutions are global, and LaSalle yields convergence to zero. If some Fr_k-1>0, the linearization has an eigenvalue with positive real part, so the equilibrium is unstable. The finite-N beta_N formula for standard Lorenz-96 was independently checked numerically for 4<=N<=100.

## Originality

**PASS** — Kerin--Engler's Proposition 1 uses the same centered energy method but explicitly assumes strict inequalities F p_+<1 and F p_-<1; the available full-text excerpt confirms negative definiteness is the decisive step in their proof. The audited theorem adds the nonhyperbolic equality case via a second polarized identity and LaSalle, converting the prior strict sufficient condition into an exact closed local/global criterion. Targeted searches for marginal/endpoint Lorenz-96 energy stability did not locate this closure argument. The novelty claim is therefore narrow and leaves residual risk of an implicit folklore observation.

## Scientific value

**PASS** — Closing the marginal boundary is scientifically useful because it distinguishes a genuinely stable critical parameter from the first unstable parameter and rules out a hidden finite-amplitude recurrent set at the exact linear threshold for the whole homogeneous cyclic energy-preserving quadratic class. The result is modest in scope but exact and structurally reusable.

## Sources

- **On the Lorenz '96 Model and Some Generalizations** — John Kerin; Hans Engler. https://arxiv.org/abs/2005.07767 — Prior homogeneous energy-stability theorem; Proposition 1 uses strict inequalities and a negative-definite centered energy form.
- **Travelling waves and their bifurcations in the Lorenz-96 model** — D. L. van Kekem; A. E. Sterk. https://doi.org/10.1016/j.physd.2017.11.008 — Bifurcation/spectral background for the first Lorenz-96 instability; not a closed-boundary global stability theorem.

## Limitations

- The theorem assumes homogeneous forcing and damping, exact quadratic energy preservation, and cyclic equivariance.
- No quantitative convergence rate is proved at a marginal endpoint and no post-bifurcation dynamics are classified.
- The strict-interior theorem is prior work; originality is only the equality case and resulting exact criterion, with residual folklore risk.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "polarized_energy_identity_checked": true,
  "lasalle_invariant_set_checked": true,
  "standard_lorenz96_beta_formula_checked_N_4_to_100": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access and preprint sources were checked first; no decisive comparison remained inaccessible, so Oxford Download was not required.
