# Independent mathematical audit

## correctness

PASS

Automorphism averaging preserves every rim-edge lower bound and convex spectral norm, proving existence of a globally optimal invariant chain. Fourier decomposition reduces spectral radius to three absolute affine eigenvalues. The proof balances the rim endpoints q0=2(1-p)/(a+b), proves the negative radial branch never binds (including boundary m=4), minimizes over p<=min(1/m,1-2tau), and derives switches tau1, tau2, tau3 and parity-dependent fourth regime. Independently solved corresponding 3-variable LP using SciPy HiGHS for 6 rim sizes and 9 threshold samples (54 comparisons), matched analytic SLEM; source verifier has 1833 floating and 48 rational LP cases, but proof is universal.

## originality

PASS

Boyd et al. already derived wheel spectrum and unconstrained optimum, so those components are NOT new. The new per-edge rim floor tau changes feasible set and yields all-parameter four-phase SLEM with explicit kernels. Published price-constraint wheel optimizations have distinct objective and parameter; no dominating coverage located.

## value

PASS

Minimum local rim exploration under fastest contraction is a naturally motivated robustness tradeoff; exact sharp phase diagram and constrained kernels for all finite wheel sizes are useful independent spectral design facts. Odd m alone has terminal zero-holding regime, distinguishing parity and feasibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
