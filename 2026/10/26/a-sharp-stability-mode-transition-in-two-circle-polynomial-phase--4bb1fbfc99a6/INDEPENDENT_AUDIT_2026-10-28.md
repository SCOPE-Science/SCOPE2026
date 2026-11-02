# Independent mathematical audit

## correctness

PASS

For the specified real coefficient norm and two normalized circle L2 norms, the derivative at z^m splits exactly into one real constant Fourier mode and m complex 2-by-2 blocks B_j; complex conjugation of the low coefficient is a real isometry. Real Parseval gives the sqrt(2) block multiplier and multiplicity two, while det B_j=(rR)^(2m-j)(R^(2j)-r^(2j))>0 gives rank 4m+1 with only phase kernel. The determinant/singular-value product yields the h-linear coefficient 2j*r^(2m+j-1)/sqrt(1+r^(4j)). Ratios g_(j+1)/g_j strictly decrease, so the strictly log-concave sequence cannot minimize in the interior. The endpoint ratio m*r^(m-1)*sqrt((1+r^4)/(1+r^(4m))) increases strictly from 0 to m, giving the unique switch and the logarithmic degree asymptotic. Independently constructed six real sampled Jacobians and compared their 4m+1 singular values against all block formulas; tested 12 critical/end-index configurations. Fixed m,r and h-down-to-zero boundaries are explicit; this is neither global nonlinear phase retrieval nor a finite-separation switch theorem.

## originality

PASS

Best-of-knowledge PASS for the complete local intensity-Jacobian singular spectrum and its two-endpoint transition, not for phase uniqueness. Chalendar–Partington characterize qualitative uniqueness from two circles, and Freeman et al. give general stable phase retrieval principles. Neither inspected relevant theorem implies explicit normalized B_j singular values or the unique coalescence critical radius. No matching Resultary record surfaced; prior specialized polynomial Fourier-block conditioning is the main remaining priority risk.

## value

PASS

Local conditioning when two concentric intensity-measurement circles merge is mathematically intrinsic, but global uniqueness alone gives no sharp smallest singular direction. This theorem supplies the entire normalized derivative spectrum, proves exclusion of all interior Fourier modes and an exact one-parameter boundary between two very different destabilizing modes, with degree-dependent asymptotics. Those nontrivial structural statements motivate the spectral calculation independently of code or mere reproducibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
