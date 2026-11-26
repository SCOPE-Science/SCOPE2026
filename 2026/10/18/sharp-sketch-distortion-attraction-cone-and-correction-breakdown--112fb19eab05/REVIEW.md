# Independent mathematical audit

## correctness

PASS

/workspace/replay.py (sketch, Python 3 + SymPy) reconstructs the full projected vector equation, both bilinear identities and the homogeneous next vector. The shift makes the right side H-orthogonal to u; v spans that complement, so the correction is unique iff a−bt²≠0, and is inconsistent otherwise since t≠0 and the residual pairing is nonzero. For H in the distortion band, Hu lies in the disk of radius ε∥u∥ about u, hence its angle differs by at most arcsin ε. In the claimed cone a−bt²>0 by the diagonal bounds, and the maximal polar deviation leaves a positive first coordinate. The two-by-two tangent perturbation in the basis along and perpendicular to u has eigenvalues ±ε and attains the upper slope ratio; for t<0 conjugate by diag(1,−1) to reverse the slope. The resulting F(r)/r increases and is less than one exactly inside ρ, giving a geometric contraction from each starting slope even under arbitrary admissible stepwise changes. At t=0 the correction vanishes; the admissible diagonal metric makes ±ρ inconsistent and iterates finite exterior slopes by −t³/ρ², diverging in magnitude to the other direction. A fixed metric has leading coefficient −c/a, of sharp magnitude τ by the same angular argument, and ε=0 gives the exact cubic. No assumption of invertibility at either spectral shift is used; the conclusion is for this real two-dimensional exact restarted model, not a general eigensolver. Packaged rational tests were inspected, not executed.

## originality

PASS

The exact correction and the qualitative normal-matrix local quadratic versus cubic phenomenon are prior coverage, as is the ordinary unsketched two-mode cubic map on the cone interior. The distinct content is the exact attained envelope over the entire admissible Gram band, its maximal sketch-uniform basin including arbitrary changes of metric, and the explicit projected singularity. No inspected statement implies this joint quantitative classification, with residual uncertainty about historical weighted RQI literature.

## value

PASS

The smallest restarted spectral plane isolates metric distortion from multi-vector expansion. The exact worst-case one-step map and the sharp failure witness locate the boundary at which even a consistent exact projected solve can no longer be guaranteed. The extremizing metrics distinguish the sharp per-step and basin mechanisms, and the cone remains valid under every admissible sequence. This is useful quantitative sensitivity information without a claim about full unrestarted algorithms or sketch probabilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
