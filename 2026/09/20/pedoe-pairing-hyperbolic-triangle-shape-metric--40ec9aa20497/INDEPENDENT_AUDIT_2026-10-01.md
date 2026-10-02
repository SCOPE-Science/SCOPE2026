# Independent scientific audit — SCOPE-20260920-40ec9aa20497

Audited at: 2026-10-01T20:13:40.771389Z

Disposition: **passed**

## Correctness — PASS

For Bookstein-normalized triangles \(0,1,z=x+iy\) and \(0,1,w=u+iv\), the side-square formulas and \(\Delta=y/2\), \(\Delta'=v/2\) give \(\mathcal P=2((x-u)^2+y^2+v^2)\). Dividing by \(16\Delta\Delta'=4yv\) gives exactly \(1+((x-u)^2+(y-v)^2)/(2yv)=\cosh d_{\mathbb H}(z,w)\). Independently, the squared-side bilinear form has the stated Lorentz signature, Heron's identity gives norm \(16\Delta^2\), and its polarization is the Pedoe pairing. The defect, equilateral radial identity, unlabeled minimization, and distances to the isosceles and right-angle geodesics then follow from standard hyperbolic formulas and rearrangement.

### Correctness sources

- assigned RESULT.md
- Pedoe 1941
- Perdomo-Plaza 2023 full HTML

### Correctness risks

- The unlabeled formula assumes the quotient over side correspondences/reflection exactly as stated; the labeled identity itself is independent of that quotient choice.

## Originality — PASS

The classical Neuberg-Pedoe literature supplies the two-triangle bilinear inequality, while Perdomo-Plaza explicitly develops Bookstein coordinates and the Poincaré hyperbolic metric on Euclidean triangle shape space. Targeted searches combining those terms did not locate the exact identity between them or the resulting side-length formulas for quotient and locus distances. The broad 1988 Mitrinović-Pečarić review remains a real residual risk because its full text could not be obtained despite open-access and authorized-access attempts, but no available metadata or search evidence indicates a Bookstein shape-space formulation.

### Equivalent formulations

No equivalent formulation was located in the searchable literature.

### Broader coverage

The two inspected frameworks are complementary rather than dominating: neither searchable source states the cross-identification that is the audited claim.

### Exact database or table

The claim is a structural metric identity rather than a numerical table entry.

### Claim versus prior implication

The calculation is elementary but the final statement is not a mere renaming: it identifies the classical two-triangle form as the Lorentz inner product of normalized shape vectors and turns the inequality defect into an exact intrinsic distance.

### Sources inspected

- Similarity Classes of the Longest-Edge Trisection of Triangles — https://doi.org/10.3390/axioms12100913. NOT_COVERING: It develops the hyperbolic shape metric but does not mention the Neuberg-Pedoe pairing or the audited identity.
- About the Neuberg-Pedoe and the Oppenheim inequalities — https://doi.org/10.1016/0022-247X(88)90242-9. INACCESSIBLE_PLAUSIBLE_SOURCE: The source remains a named originality risk, but the available material gives no evidence of the later Bookstein/Poincaré shape-space identity.
- An inequality connecting any two triangles — https://doi.org/10.2307/3606570. BACKGROUND: It supplies the inequality but not an intrinsic triangle-shape metric interpretation.

### Checked sources

- https://doi.org/10.2307/3606570
- https://doi.org/10.1016/0022-247X(88)90242-9
- https://doi.org/10.1016/j.amc.2013.06.075
- https://doi.org/10.3390/axioms12100913
- https://doi.org/10.21136/MB.2024.0111-23

### Residual risks

- The full 1988 Mitrinović-Pečarić review was inaccessible and could contain an equivalent Lorentzian reformulation.
- Because the main identity is algebraically short, an older equivalent statement may exist under different terminology.

## Value — PASS

The result gives a natural structural bridge between a classical two-triangle inequality and the intrinsic metric geometry of triangle similarity space. It upgrades a nonnegative defect into an exact distance identity and yields usable closed formulas for unlabeled distance and distances to equilateral, isosceles, and right-angle loci. The contribution is therefore more than a cosmetic substitution despite the short algebraic proof.

### Value sources

- Pedoe 1941
- Perdomo-Plaza 2023

### Value risks

- The mathematical value is interpretive/structural rather than a difficult new estimate; its novelty depends on the absence of an older equivalent formulation.

## Limitations

- The metric is the Poincaré/Bookstein metric, not Kendall's spherical/Procrustes shape metric.
- Only nondegenerate Euclidean triangles are included; degenerate shapes lie at the ideal boundary.
- The labeled identity uses a fixed side correspondence; the quotient formula handles relabeling and reflection.
- The inaccessible 1988 review remains a specific originality risk.
