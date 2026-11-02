# Scientific review

## Correctness

**PASS.** For every positive radius and finite positive height, the projected disk-plus-segment area is exactly \(\pi r^2 x+2rh\sqrt{1-x^2}\) with \(x\) uniform on \([0,1]\). Beta integrals give the three raw moments. Normalizing by the mean yields the stated quadratic and cubic in \(y=h/(r+h)\). Every collision of the quadratic is a reflection \(y+z=s\), and the cubic secant quotient is strictly negative on such pairs by the explicit quartic \(f(\pi)<0\). The quartic's sign is proved with rational upper and lower bounds on \(\pi\). Endpoint cases and positivity hypotheses are stated. The standalone verifier independently checked analytic moments, reflected pairs, and directly projected polygonal rims.

## Originality

**PASS, subject to historical-priority uncertainty.** Finch (2012) calculates moments for random polytope shadows, not inverse recovery of cylinder dimensions. Kim–Yaskin–Zvavitch (2015) investigate distributional projection tomography for general convex bodies but do not prove the finite three-moment cylinder criterion. Agimelen and collaborators (2014) infer shape using chord-length distributions, a different invariant. A published same-cylinder area–perimeter *mixed*-moment calculation was inspected and contains the elementary forward shadow-area function, but not its third pure moment or the normalized-moment global inverse/collision classification. Other published finite-moment tomography results for orthotopes concern a different family. No inspected statement implies this exact theorem. Residual risk is an unlocated older stereological calculation of the same inverse criterion.

## Mathematical value

**PASS.** The natural observable is a dimensionless aspect ratio inferred from unlabeled silhouette areas. The mean alone fixes only surface area, the second moment becomes a two-branch shape parameter, and a specific third moment resolves that ambiguity for *all* positive aspect ratios. The explicit sharp bifurcation threshold and complete inverse of a two-parameter smooth convex-body family go beyond a single table value or elementary Cauchy mean-area restatement. No claim of broad statistical optimality is made.

## Closest sources and limitations

Finch, arXiv:1203.2464v1 (2012); Agimelen et al., arXiv:1408.4399v1 (2014); Kim, Yaskin and Zvavitch, arXiv:1512.07289v1 (2015). The proof applies only to one ideal right circular cylinder, Haar-uniform viewing planes, and its first three exact consecutive raw area moments. It does not address stability against noise, other measurement pairs, or arbitrary convex bodies. Independent historical-priority review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
