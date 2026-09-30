# Independent Audit — 2026/09/19/entropy-gauge-corner-obstruction-elcd--8cb75d085d2d

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `9e5bf1b2a9be5344d33b7ff2334dde897d53419f`
- Disposition: **PASSED**

## Correctness

**PASS** — The convex-analysis and entropy-gauge objections are correct. For eta0=-rho/(gamma-1) log(p/rho^gamma), the Hessian has positive determinant 1/((gamma-1)p^2) and positive leading entry, so eta0 is strictly convex; convexity does not imply a minimum occurs at rectangle corners. Because partial_p eta0<0, the continuous rectangle minimum lies on p=p_+, and solving partial_rho eta0=0 gives rho*=e^-1 p_+^(1/gamma), clipped to the density interval. The stated Bregman-type excess formula follows by direct subtraction. For gamma=1.4 on [0.2,0.6]x[0.5,1], I independently obtain eta(e^-1,1)=-1.2875780441 versus -1.1266065387 at the best listed corner. Adding c rho is an equivalent entropy-pair gauge because it adds c times mass conservation and leaves the Hessian unchanged. The minimizer shifts to exp[-1-(gamma-1)c/gamma]p_+^(1/gamma), and candidate rankings with unequal densities are affine in c. The example threshold c*=-1.6173434213 and the branch flip at c=-2 reproduce exactly. Dividing eta by rho removes this mass-affine ambiguity up to an additive constant.

## Originality

**PASS** — The general facts that Euler admits families of convex entropies and that specific entropy has an arbitrary reference constant are classical; they are not claimed as new. Chu-Herty-Kurganov's September 2026 ELCD paper is the new target: its public description explicitly selects a state that locally minimizes entropy. The audited record gives a source-specific mathematical correction—an exact continuous minimizer missed by a corner-only argument—and shows that absolute entropy-density ranking is not invariant under the standard mass-affine entropy gauge. Targeted searches for a published correction using this corner-minimization or gauge-obstruction argument found no pre-record statement.

## Scientific value

**PASS** — The result identifies two conceptually distinct defects in the justification of a new numerical-state selector: the geometric minimization claim is false, and the selected branch can depend on an arbitrary entropy reference while the Euler equations and entropy inequality are unchanged. This does not show the ELCD schemes are unstable or inaccurate, but it materially changes how their interface-state criterion should be interpreted and suggests a simple gauge-invariant diagnostic.

## Sources

- Entropy-Based Local Characteristic Decomposition (Shaoshuai Chu; Michael Herty; Alexander Kurganov): https://arxiv.org/abs/2609.19838 — Primary September 2026 source; public abstract states that ELCD selects a nearby state that locally minimizes entropy.
- Convex Entropies and Hyperbolicity for General Euler Equations (Ami Harten; Peter D. Lax; C. David Levermore; William J. Morokoff): https://doi.org/10.1137/S0036142997316700 — Classical source for the generalized Euler entropy family rho f(sigma); supports that the entropy representative is not unique.
- A Minimum Entropy Principle in the Gas Dynamics Equations (Eitan Tadmor): https://ntrs.nasa.gov/citations/19860020949 — Classical specific-entropy minimum-principle background, distinct from the source's absolute entropy-density selector.

## Limitations

- The result is a correction/invariance analysis, not a convergence, stability, or accuracy failure theorem for the published numerical schemes.
- A fixed entropy normalization still makes the four-candidate algorithm well-defined as a heuristic.
- The proposed eta/rho ranking is gauge invariant but is not validated here as a superior numerical replacement.

## Independent checks

```json
{
  "gamma": 1.4,
  "rectangle_example": {
    "rho_star": 0.36787944117144233,
    "eta_star": -1.2875780441000482,
    "best_corner_eta": -1.1266065387038704
  },
  "gauge_example": {
    "eta_rho025_c0": -1.2130075659799044,
    "eta_rho1_c0": 0.0,
    "eta_rho025_cminus2": -1.7130075659799044,
    "eta_rho1_cminus2": -2.0,
    "switch_c": -1.6173434213065392
  },
  "proof_reconstructed": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. The dated independent-audit pair was verified absent before staging this change set, and `VERIFICATION.md` was read at blob `31a3bb079c3be0cdcbee536377edadb1613bf629`. GitHub was used only as read-only evidence; no repository write was performed. Open-access/preprint sources were checked first. No decisive comparison required Oxford Download in this run.
