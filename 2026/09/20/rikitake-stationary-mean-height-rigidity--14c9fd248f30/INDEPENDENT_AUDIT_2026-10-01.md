# Independent audit — 2026-10-01

## Record

**Rikitake stationary mean-height floor and sharp equality rigidity**

Final claim: For the classical Rikitake system with \(\mu>0\) and \(a\ge0\), every compactly supported invariant probability measure obeys exact stationary moment identities and the defect law \(m-z_+=\frac{\mu}{1+r^2}\int(y-rx)^2\,d\nu\), hence \(m\ge z_+\); for \(a>0\), equality holds exactly for mixtures of the two finite equilibria, yielding strict coordinate-excursion barriers for every other compact recurrent state and the corresponding bounded-orbit time-average floor.

Disposition: **PASSED**

## Correctness — PASS

Integrating four polynomial Lie derivatives gives \(\int xy=1\), \(\mu(U-V)=a\), and \(m=\mu U=a+\mu V\). The square-defect identity follows algebraically from \(r=\mu/z_+\). Equality forces the support onto \(y=rx\); invariance and tangency then force \(z=z_+\) and the two equilibrium points when \(a>0\). At \(a=0\) the plane \(x=y\) is invariant, explaining the exact boundary exception. Empirical-measure limits of bounded trajectories give the time-average corollary. No saved symbolic log is needed for these deductions.

## Originality — PASS

The inspected Rikitake literature covers global compactification, unbounded orbits, invariant planes, integrability, reversal geometry and chaotic dynamics. The Llibre–Messias primary description specifically treats the invariant-plane/global-flow structure, but the accessible material does not state the invariant-measure moment floor, square defect, or equality rigidity. An institutional full-text retrieval for that paper was still running during inspection, so no whole-document noncoverage claim is made. Resultary found the audited statement but no earlier equivalent Rikitake record.

Equivalent-formulation, broader-coverage, exact-database/table, and claim-versus-prior implication checks are recorded in the companion JSON audit. Source inspections distinguish material actually read from inaccessible full text.

## Scientific value — PASS

An exact invariant-measure balance with a sharp equality classification gives a parameter-explicit global constraint on every compact recurrent statistical state, not merely a numerical observation. The strict excursion consequences and sharp \(a=0\) transition make the result a motivated structural theorem for a classical dynamo model.

## Checked scientific sources

- J. Llibre and M. Messias, Global dynamics of the Rikitake system, Physica D 238 (2009), DOI:10.1016/j.physd.2008.10.011.
- A. E. Cook and P. H. Roberts, The Rikitake two-disc dynamo system, Math. Proc. Camb. Phil. Soc. 68 (1970), DOI:10.1017/S0305004100046338.
- J. Llibre and C. Valls, Darboux integrability and algebraic invariant surfaces for the Rikitake system, J. Math. Phys. 49 (2008), DOI:10.1063/1.2897983.
- Resultary semantic search for Rikitake invariant measures, stationary moments, mean-height floors, and periodic-orbit rigidity.

## Residual risks

- The full 1970 Cook–Roberts article was not inspected end-to-end. The authorized retrieval of the 2009 Llibre–Messias article had not completed during the audit, so a hidden equivalent time-average identity in those sources remains a concrete originality risk.

## Verification boundary

The audit reconstructed the mathematical argument from the record and performed fresh logical or algebraic checks where needed. Existing package logs were treated only as reproducibility evidence. No formal proof-assistant verification or expert attestation is asserted.
