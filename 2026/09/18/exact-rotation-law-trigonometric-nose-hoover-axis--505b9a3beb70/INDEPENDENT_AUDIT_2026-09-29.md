# Independent Audit — Exact rotation law on the trigonometric Nosé–Hoover a=0 axis

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `16069d64c68725bef2f960fc81c407be02e9630d`  
**Audited current source tree:** `16069d64c68725bef2f960fc81c407be02e9630d`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assignment tree SHA. GitHub was used only as read-only evidence; this audit plan does not assert that any staged audit text is already published.

## Correctness — PASS

PASS. On a=0, H=cos x+cos y is conserved and the source identities T(h)=4K(sqrt(1-h^2/4)) and <cos y>_h=h/2 give Δz=bT(h)(1-h) exactly, hence rho_b(h)=b(1-h)/Omega(h). The zero-mean cohomological equation on each compact regular annulus has a smooth periodic solution, so the stated z-coordinate change gives an exact Kronecker normal form. The derivative of (1-h)/sqrt(cos^2 φ+(h^2/4)sin^2 φ) is strictly negative for 0<h<2, proving the positive-energy twist. Dense irrational linear flows plus continuity force every annular continuous first integral to be constant on each energy torus and therefore factor through H. The negative-energy symmetry and h=1 zero-drift case also check.

## Originality — PASS

PASS, NARROWLY. Szumiński–Llibre's September 2026 source supplies the local regular-domain first integrals, mechanical period, and energy-phase ingredients; those inputs and the standard rational/irrational Kronecker dichotomy are not new. The source's accessible statement does not give the global torus return map, the exact finite-b rotation classification, or the monodromy obstruction to a globally single-valued second continuous integral on a full regular annulus. The audited contribution is limited to that source-specific global synthesis and obstruction, not to general skew-product or torus-flow theory.

## Scientific value — PASS

PASS. The result resolves a genuine global-versus-local integrability issue in the motivating system: it converts branchwise first integrals into an exact torus rotation law, classifies periodic versus dense energy tori, and explains why the local elliptic primitive cannot globalize except at zero drift. This is a substantive clarification of the source model despite relying on standard dynamical-systems tools.

## Independent checks

- rederived conservation of H and the exact thermostat drift from the source period/average identities
- checked the cohomological equation and smooth annular coordinate change
- independently differentiated the positive-energy integral representation and confirmed strict monotonicity
- checked the dense-orbit continuity argument and the negative-energy symmetry
- compared the claimed global result against the source's accessible description of local regular-domain first integrals
- verified the current main directory tree exactly equals the assigned tree SHA

## Limitations

- The originality verdict is deliberately source-specific; standard Kronecker-flow, cohomological-equation, and rotation-number facts are not credited as new.
- The theorem excludes h=0 and the critical levels h=±2 and does not address persistence for a≠0.
- The literature comparison does not claim priority over unpublished or contemporaneous unindexed work.

## Evidence and references

- https://arxiv.org/abs/2609.19958
- https://arxiv.org/html/2609.19958v1
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/exact-rotation-law-trigonometric-nose-hoover-axis--505b9a3beb70

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
