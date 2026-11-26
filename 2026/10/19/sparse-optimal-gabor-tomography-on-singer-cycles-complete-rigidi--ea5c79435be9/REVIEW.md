# Independent mathematical audit

## correctness

PASS

The frozen assertion of exactly three distinct eigenvalue levels for all k≥2 is false at k=2. Indeed in Z₃ the support {0,1} is perfect, and the two nonidentity blocks have the same eigenvalue 3/4, of combined multiplicity 8; the identity eigenvalue is 3. Also, the equality characterization must be for attaining 1/k in the feasible branch, not for maximizing in the no-perfect-set branch, where every eligible window has margin zero. Corrected and re-audited files: /workspace/repairs/1/RESULT.md and /workspace/repairs/1/VERIFICATION.md; the latter preserves the original status block and corrects the description of the numerical tests. The necessary count |S−S|≤|S|(|S|−1)+1 forces uniqueness of each directed difference at capacity. On a perfect support every nonzero shift has one product term; the product over all distinct pairs and AM–GM give the maximum least pair modulus 1/k, with equality only for uniform weights. At zero shift character orthogonality gives the second modulus and the exact weighted nonvanishing condition. On normalized Weyl basis vectors the lifting columns are orthogonal characters of G×Ĝ scaled in modulus by |A|/√v, so squared singular values equal v|A|². The identity remains maximal; the trace-free bound separately uses Parseval to lower-bound its maximal zero-shift modulus by √(k−1)/k. A missing shift causes a nonidentity kernel direction, hence singularity also in the traceless sector. Moyal gives the SIC comparison; its excess over 7/8 is (k−4)²/(8k²). A projective line and its nontrivial Singer translates intersect in a single point, giving the claimed perfect supports; q=2^(3t+1) gives unbounded orders divisible by 7 and greater than 7 for t≥1. A direct independent lift SVD (not the frozen ambiguity-sum script) reproduced the two levels in v=3 and three in v=7. Replay: OPENBLAS_NUM_THREADS=1 python /workspace/independent_checks.py (NumPy/SciPy); finite checks do not certify the all-group proof.

## originality

PASS

For the corrected claim, the supported distinction is the sharp all-weights optimization and its equality cases, particularly the separate optimum for the trace-free lifting over the entire sparse class, in the arbitrary finite abelian setting. The support-count obstruction, flat-window overlaps, framework for the full spectral calculation, and Singer construction are prior; the SIC ratio is an evaluated implication of the known flat-window table and Moyal, not an independent priority claim. There is direct later-dated indexed maximin/rigidity overlap on the cyclic Singer subfamily, explicitly scoped below. The corrected verification does not promote the boundary case to a novelty claim.

## value

PASS

At the least possible sparsity in these orders, the new optimization classifies when sparse feasible designs are best-conditioned rather than merely giving one feasible construction. The traceless-sector optimum is separately informative for perturbations of fixed trace, and shows that the dominant nontrivial singular value cannot be traded against the least one to improve the ratio. The endpoint correction preserves both exact optima, and the known/evaluated SIC comparison helps interpret the least directional stability without claiming equiangularity. No general physical robustness or quantitative effect outside the sparse class is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
