# Independent mathematical audit

## correctness

PASS

The assigned matrix boundary rows and interior five-point stencil reconstruct as M=12D+D²+e1*r^T+en*(Jr)^T. For d_j=u_j-u_(j-1), the two left defect Hermitian forms are (-2|d1|²+3Re d1*d2-Re d1*d3) and (-3|d1|²+6Re d1*d2-4Re d1*d3+Re d1*d4). Rank-two least eigenvalues give losses tau_BH=1+sqrt(14)/2 and tau_OS=(3+sqrt(62))/2; boundary edge sets overlap at most twice, giving 12-2tau=beta. Dirichlet eigenvalue lambda_n>0 then yields the stated accretivity bound for any complex u, and standard energy/resolvent identities prove the contraction estimates. The positive (2,4) off-diagonal of M yields a negative (2,4) heat-kernel entry to first order; mismatched (1,3) and (3,1) prevent positive diagonal symmetrization. Checked actual verify.py quadratic-form construction and independently enumerated n=5..9 integer vectors. No optimal beta claim or higher-order generality.

## originality

PASS

The original Feng–Gao–Shao paper addresses *the same two matrices* and their real positive eigenvalues. Positive eigenvalues do not imply positive symmetric part or Euclidean contraction (a 2x2 nonnormal upper triangular counterexample suffices), so its accessible advertised theorem is not a covering implication. Originality is best-of-knowledge because the full paper and historical Bramble–Hubbard/von Linde energy literature were inaccessible; no whole-document noncoverage judgment is made. The explicit rank-two energy certificates are independently reconstructed, not a cosmetic restatement of spectral location.

## value

PASS

Dimension-uniform explicit Euclidean accretivity for the actual nonsymmetric higher-order Dirichlet closures supplies a stability guarantee absent from mere spectral positivity, while the negative heat-kernel entry distinguishes norm dissipation from order preservation. This is a motivated structural numerical-analysis lemma, not a general claim about all fourth-order discretizations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
