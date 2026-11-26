# Independent mathematical audit

## correctness

PASS

Reconstructed the qubit minimum-error SDP with priors 1/4 and strict feasibility. With dual variable H=((1+s)I+c·σ)/8, domination of each weighted state is exactly s≥||c−(t+TRv_j)||, and tr H=(1+s)/4. Thus the objective is a Euclidean enclosing radius, independent of t for every R. The tetrahedral mean and second moment give the mean squared distance from c as ||T||²_F/3+||t−c||², a lower bound on the enclosing radius squared. A proper eigenframe makes the four squared distances at t equal to that bound. Conversely equality forces c=t and all four squared norms equal; orthogonality of the three nonconstant coordinate-pair sign columns on the four vertices forces each off-diagonal Gram entry to vanish. This also covers singular and degenerate T. If T=0, all rotations attain and every Gram matrix is zero; if the eigenvalues are distinct, the three ordered eigenaxes have 3!×4 proper sign choices. At an attaining frame the advertised effects are positive, sum to I by the zero mean, and give the dual value by direct trace multiplication; division by zero is avoided using I/4 for T=0. As a concrete strict case, T=diag(1,0,0) has radius 2/3 when a vertex is oriented along the channel axis (the projections are 1 and −1/3), versus 1/√3 at a Gram-diagonal orientation. The included verification/verify.py was inspected but not executed; its documented finite tests cannot establish the continuous minimum or the necessity statement.

## originality

PASS

The supported distinct claim is the arbitrary affine-channel minimum over common tetrahedral rotations and its exact Gram-diagonal equality criterion. Fixed-ensemble discrimination, common-translation invariance, tetrahedral tight frames and the isotropic case are already covered. No examined stronger claim mechanically implies the anisotropic minimization and equality classification.

## value

PASS

The formula gives a sharp worst-orientation receiver-performance invariant for a standard four-state signal family without numerical orientation or measurement optimization. The exact eigenframe criterion and usable attaining measurement matter alongside the scalar, including for anisotropic, nonunital and rank-deficient channels. This value is specific to the worst-orientation question, not a claim about best encoding fidelity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
