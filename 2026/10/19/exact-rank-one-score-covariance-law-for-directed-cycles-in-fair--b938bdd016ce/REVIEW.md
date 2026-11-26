# Independent mathematical audit

## correctness

PASS

A direct replay conditions on each candidate cycle indicator being one. A vertex off the cycle retains its Bin(m,1/2) degree law; a vertex on the cycle has one incident win and one incident loss fixed, with its other m-2 edges still fair and independent, so has degree 1+S with S~Bin(m-2,1/2). There are (n) falling ell divided by ell candidate oriented cycles (rotation only), each present with probability 2^{-ell}. Summing their covariances gives (n) falling ell /2^ell times [E f(1+S)-E f(D)]. The identity d(m-d)p_m(d)=m(m-1)p_{m-2}(d-1)/4 converts this to (1), including ell=n. The scalar multiplier is positive for every ell; the covariance with H0 is nonzero since m>=2 and D(m-D)=0 at D=0 but has positive mean. Thus the cross-covariance rank is exactly one, and residual orthogonality is only linear, not independence. The degree-class covariance follows from 4d(m-d)-m(m-1)=m-(2d-m)^2; its equality roots are integers exactly for square m, by parity. For the threshold let T_j=P(S>=j). Because D has the law of S plus an independent Bin(2,1/2), the expectation difference is (2T_{k-1}-T_k-T_{k-2})/4, equal to (p_{m-2}(k-1)-p_{m-2}(k-2))/4. The ratio of successive masses in the interior is (m-k)/(k-1), giving the cutoff 2k=n, with the endpoint signs from one mass vanishing. At n=3, two cyclic and six transitive orientations give Cov(C3,H0)=-3/16 and threshold covariances +3/16,-3/16, consistent with the formulas. The source file verification/check_cycles.py was found inside the nested directory and inspected, not executed. Its stated checks are finite (all orientations through n=6 and a bounded sign test); the all-length formulas follow from the exact conditioning argument, not those finite checks.

## originality

PASS

The triangle specialization is explicitly covered by the earlier October 12 indexed result; the four-cycle specialization also follows from the October 18 indexed orthogonal decomposition, as shown below. The supported distinct claim is the single exact all-length formula for the mixed score covariances, including lengths at least five and their exact degree/threshold signs and residuals. A later November 2 record matches the full score covariance and projection and implies threshold signs; that is documentary overlap, not antecedent coverage. The earlier published results examined concern different moment, extremal or deterministic quantities and do not establish the full claim in the inspected statements.

## value

PASS

The all-length law collapses the linear dependence between the full cycle-count vector and the full additive score profile to one direction, including up to Hamiltonian cycles. The exact finite-size degree and threshold signs give the direction of dependence and its zero boundary for each length, beyond known triangle and four-cycle cases. This is an exact joint invariant for two naturally used diagnostics, not just a marginal moment or finite recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
