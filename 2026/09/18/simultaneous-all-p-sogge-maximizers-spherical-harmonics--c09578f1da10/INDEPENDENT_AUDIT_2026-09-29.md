# Independent audit — Positive-density spherical harmonics simultaneously saturating all Sogge Lp branches

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/18/simultaneous-all-p-sogge-maximizers-spherical-harmonics--c09578f1da10`  
**Audited tree:** `ef8dd3a385bf2e10971ccd9ea5a06c9249b6e2e2`

## Disposition

**PASSED.** All three required axes pass. Publication may remain in the validated record set.

## Correctness

**PASS.** The two-subspace construction is sound. The zonal block supplies an orthonormal family with point peaks of order sqrt(N_k). Projecting the rotational tight frame of real Gaussian beams to its orthogonal complement leaves stable rank asymptotic to (1-rho)N_k; restricted invertibility selects rho N_k well-conditioned projected beams whenever rho<1/2. Orthogonalizing and mixing the two blocks preserves both a point peak and a nonzero Gaussian-beam pairing. Hölder duality gives the low-p Sogge lower branch, while the peak plus the standard gradient bound on a k^{-1} ball gives the high-p branch.

## Originality

**PASS.** Han's 2026 theorem supplies positive-density families, with density arbitrarily close to one, that achieve maximal Lp growth for each branch via the classical branch-specific concentration mechanisms. The searched literature did not state one common positive-density orthonormal family whose every member simultaneously carries both mechanisms and saturates every fixed p. The new content is therefore the mixed projected-frame construction, not the Sogge estimates, zonal/beam asymptotics, or restricted invertibility.

## Scientific Value

**PASS.** A common family simultaneously extremizing both sides of the critical Sogge exponent answers a structurally different question from branchwise existence and shows that the two classical concentration geometries can coexist at positive density. The rho<1/2 threshold is constructional rather than claimed optimal.

## Independent checks

- Verified z_i(x_i)=sqrt(N_k)(E_Z^{1/2})_ii and used lambda_min(E_Z)>=c0^2 to retain a uniform zonal peak after orthogonalization.
- Checked the projected frame identity integral P Q_R tensor P Q_R dR=P/N_k and the resulting stable-rank lower bound ~dim(V).
- Checked the restricted-invertibility parameter inequality can select M=floor(rho N_k) columns with a k-independent lower singular-value bound for every fixed rho<1/2.
- Verified q_i(x_i)=0 because q_i lies in U^perp while the reproducing zonal Z_{x_i} lies in U.
- Recomputed the Gaussian-beam dual exponent ||Q_i||_{p'}~k^{-sigma_n(p)} on the low branch and the peak-ball exponent k^{(n-1)/2}k^{-n/p}=k^{sigma_n(p)} on the high branch.

## Literature and prior-art boundary

- https://arxiv.org/abs/2609.14023 — Xiaolong Han (2026), positive-density maximal-Lp spherical harmonics; searched version does not state the mixed same-family all-branch theorem.
- https://arxiv.org/abs/1404.5016 — Han (2014), earlier positive-density low-p construction on the sphere.
- https://arxiv.org/abs/0911.1114 — Spielman and Srivastava, restricted invertibility input used to select the projected beam block.

## Limitations

- The theorem is only for round spheres and fixed densities rho<1/2; no optimality of 1/2 or full-basis result is established.
- Constants are allowed to depend on p, n and rho.
- The originality search found no exact simultaneous construction, but the argument is short enough that folklore overlap remains possible.

## Repository identity

The assigned source-tree SHA `ef8dd3a385bf2e10971ccd9ea5a06c9249b6e2e2` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
