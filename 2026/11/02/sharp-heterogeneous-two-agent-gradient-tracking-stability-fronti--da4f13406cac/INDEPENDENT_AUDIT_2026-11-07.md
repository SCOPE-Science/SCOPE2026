# Independent mathematical audit

## correctness

PASS

Deriving the 3x3 reduced dynamics from x+=W(x−αy), y+=Wy+H(x+−x) and the conserved tracker average gives the same cubic P(z) as the claimed reduced matrix. Exact Schur-Jury inequalities use P(1)=β(1−s)^2 and −P(−1)=2s(1−η²)β²−(s²+6s+1)β+2(1+s)^2. The proof establishes |c|<1 and J=1−b+ac−c²>0 before the smaller positive root; in the intermediate interval −P(−1)≤0, and beyond the larger root c<−1. Independent symbolic comparison with the true recurrence and sampled spectral radius on either side confirmed the formula. These tests do not certify all reals.

## originality

PASS

Wang et al. study exactly heterogeneous scalar-quadratic distributed gradient tracking and supply global sufficient certificates, tight in the complete-graph/homogeneous cases. The inspected abstract does not claim a two-agent heterogeneous sharp positive-disagreement Schur frontier; full paper was inaccessible. A standard Jury calculation is a tool, not itself the novel result.

## value

PASS

Exact stability at the first genuinely coupled two-agent curvature/mixing regime tests conservatism of general certificates and proves heterogeneity strictly lowers the admissible step length. This is a motivated optimization boundary with explicit counterexamples to homogeneous step tuning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
