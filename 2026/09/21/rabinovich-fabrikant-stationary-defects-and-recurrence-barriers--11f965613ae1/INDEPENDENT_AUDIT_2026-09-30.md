# Independent audit — 2026-09-30

**Record:** `2026/09/21/rabinovich-fabrikant-stationary-defects-and-recurrence-barriers--11f965613ae1`  
**Audited source tree:** `7574302a47771f9c010a6cce811710c08c8a0c0d`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

## Correctness — PASS

PASS. I independently differentiated R=x^2+y^2 and W=R+4z and recovered R'=2γR+8xyz and W'=2γR-8αz. The sign of z is invariant. On z<0, W'>0 rules out compact invariant probability mass; on z=0, R'=2γR forces only the origin. On the positive component, applying invariance to cutoff antiderivatives with derivative φ(z)/z gives E[xy|z]=-α, which yields the conditional and global square-defect identities. Integrating W' gives γE[R]=4αE[z]. A cutoff log-R identity yields E[xyz/R]=-γ/4 and the second height-defect formula. For equality, x+y=0 almost surely; tangency gives z=x^2-1 and the remaining consistency polynomial, forcing x^2=1+γ/2=α and hence precisely the two stated equilibria. I independently rechecked the symbolic Lie derivatives and equality-manifold polynomial.

## Originality — PASS

PASS with a documented historical-language qualification. The open 1979 JETP paper introduces and qualitatively/numerically analyzes the model; it records the conservative energy x^2+y^2+4z and the invariant plane z=0. Modern papers located in the search emphasize numerical bifurcation/generalized-model dynamics. I found no statement of the conditional invariant-measure law E[xy|z]=-α, the exact stationary square defects, the equality classification, or the universal periodic-orbit barriers. Older Russian-language/model-specific literature remains a residual priority risk.

## Scientific value — PASS

PASS. The result upgrades familiar trajectory-level model identities into conditional stationary laws and sharp measure/periodic-orbit constraints with complete equality rigidity. These are analytic, parameter-exact restrictions that can constrain or falsify numerical claims about recurrent dynamics.

## Independent checks

- Recomputed the two polynomial Lie derivatives directly.
- Reconstructed the cutoff argument for the heightwise conditional expectation.
- Reconstructed the log-R cutoff and exact height-defect identity.
- Rechecked the equality-manifold tangency polynomial and special equilibria.
- Inspected the open 1979 JETP source at the pages containing the conservative energy and invariant z=0 plane.

## Literature evidence

- https://www.jetp.ras.ru/cgi-bin/dn/e_050_02_0311.pdf — Rabinovich and Fabrikant (1979), original model; open full text inspected for the conservative energy and invariant-plane context.
- https://doi.org/10.18500/0869-6632-2022-30-1-7-29 — Kuznetsov and Turukina (2022), generalized Rabinovich–Fabrikant dynamics; abstract/methods emphasize numerical study.
- https://www.mathnet.ru/ConfLogos/812/Abstr_book.pdf — Tsegel'nik (2016) conference abstract cited by the record as an analytical predecessor.

## Limitations

- Invariant-measure statements assume compact support and α,γ>0.
- The results are necessary recurrence/stationarity constraints, not existence or uniqueness theorems for attractors.
- Older Russian-language sources remain a residual originality risk.

The assigned record package was compared file-by-file against the current default-branch package for its research, review, verification, and listed artifact files; the inspected Git blobs are unchanged. No GitHub write was performed by this audit chat. The guarded change-set below only stages independent-audit evidence and the independent-audit channel of `VERIFICATION.md`.
