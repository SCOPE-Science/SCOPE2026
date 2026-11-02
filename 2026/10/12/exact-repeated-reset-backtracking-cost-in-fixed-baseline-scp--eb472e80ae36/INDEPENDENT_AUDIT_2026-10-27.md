# Independent mathematical audit

## correctness

PASS

Reconstructed the trial subproblem and source line-search/stopping rules. With c(z)=z^2-R_c^2 and L_c=2, the surrogate constraint equals the original constraint exactly, hence it is inactive for all reached box-contained trials; q=indicator of the box is inactive by the explicit strict radius. For a nonzero outer z, the trial is (1-a/L_i)z and the descent test simplifies by algebra, dividing only by positive a^2 z^2/L_i^2, to 2L_i>=a+beta. The minimum i is exactly the displayed ceil-plus and equals Theorem 4 upper bound at the exact L=a. The accepted contraction q*=1-a/L*, |q*|<1, preserves the magnitude bound by induction. The source residual is |(a-L*)(z^{k+1}-z^k)|=a|a-L*|/L*|z^k|; the geometric sequence gives first stopping index K*. The q*=0/L*=a case terminates after first accepted outer step, treated separately. Thus total and rejected solves count (K*+1)(i*+1) and (K*+1)i*. For this scalar family starting later searches at L* accepts at first trial, saving exactly K*i* rejected solves; no global warm-start theorem asserted. The source KL gradient norm a|z| and objective gap a z^2/2 gives exponent 1/2 with constant sqrt(2a). Independent algebra and representative numerical boundary checks corroborate, not substitute for the all-parameter proof.

## originality

PASS

Best-of-knowledge: the closest published Lu--Wang source specifies a fixed-baseline search and bounds the per-outer accepted index, but the inspected Algorithm 1 and Theorems 4--5 do not determine an all-outer sharpness witness, exact repeated-rejection count through the first stopping index, or family-specific avoidable overhead. The exact algebra follows from basic quadratic descent calculations and should not be presented as a new general line-search principle; nonetheless the source-specific repeated attainment and complete cost identity were not established by an inspected stronger theorem. The adjacent published examples concern different recurrence/update mechanisms. Searches alone do not prove novelty.

## value

PASS

The natural gap is sharpness of an actual published inner-loop complexity index and the cumulative operational cost of fixed-baseline reset. The scalar quadratic is a motivated minimal exact witness because it attains the smoothness constant and reproduces the same curvature trial thresholds at every outer iteration; the exact all-run count (K*+1)i* shows per-outer worst-case rejection can recur rather than amortize. The gap between fixed reset and warm-start costs is K*i* and can be nontrivial when each constrained proximal solve is expensive. A small and elementary but source-specific sharpness/boundary result is mathematically useful for interpreting this scheme, without asserting a new general convergence theorem. The derivation is straightforward once the source algorithm is specialized; value is limited to diagnosing a real bound and implementation choice, not novelty of backtracking itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
