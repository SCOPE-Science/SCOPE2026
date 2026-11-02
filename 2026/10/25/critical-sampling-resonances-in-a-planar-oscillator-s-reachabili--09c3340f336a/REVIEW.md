# Independent mathematical audit

## correctness

PASS

Direct integration yields Bh=(sin(theta),1-cos(theta))/omega, Ah a rotation by theta=omega*h. The exact Gram matrix is r^2[[1,cos(theta)],[cos(theta),1]], r=2|sin(theta/2)|/omega. Diagonalizing gives both exact singular values and det(W)=4sin^2(theta/2)sin(theta)/omega^2; Taylor expansion at every positive m*pi proves the parity-specific asymptotics. Independent NumPy SVD tests checked 15 nonresonant instances and 36 detuning ratios (maximum singular-value deviation 8.9e-16). These numerical tests are corroborative, not the proof.

## originality

PASS

Best-of-knowledge comparison of actual final mathematical implications with primary sources and relevant published semantic records. Relevant predecessor results were credited; no inspected full-theorem statement covers the final claim, with explicit residual priority risks.

## value

PASS

The precise, parity-dependent inverse gain of the actual two-step zero-order-hold reachability matrix quantifies a meaningful sampling-design obstruction and distinguishes rank-one resonances from zero-input resonances. It is a motivated exact local conditioning result tied to an explicitly used tracking inverse, not a generic assertion that sampled controllability can fail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
