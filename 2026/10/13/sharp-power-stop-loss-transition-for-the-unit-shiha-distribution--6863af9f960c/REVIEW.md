# Independent mathematical audit

## correctness

PASS

For fixed positive omega and 0<eta1<eta2, the transformed CDF difference is a strictly positive scalar times u*g(u), g(u)=u(3-4 log u)-3. The derivative changes sign once before 1, and g is negative at 0+, positive at its interior maximum and zero at 1. This gives exactly one interior zero and H_q(u*)=u*. Integrating the density using the elementary log moment gives the moment gap k*z*(2-z)/[(1+z)(2+z)^2], z=s/omega. The stop-loss difference B is minus the integral of the powered CDF difference over [d,1]; its derivative is negative before the powered pivot and positive after it. B at the pivot is strictly negative, B(1)=0, and B(0) has the sign of 2*omega-r. This proves the stated strict interior comparisons, incomparability and unique subcritical root; the multiplicative factor k cancels from the root condition. Differentiating the proposed primitive verifies the log term and J(1)=0. Below 0 the stop-loss gap equals the mean difference; at and above 1 it vanishes. At r=2*omega the means are 1/3 and the variance (4+10q)/[45(1+3q)] decreases strictly over q>0, with the stated unattained limits and ratio. The independent bounded replay `python3 /workspace/review_replay.py 4` gives pivot 0.5768340041423086893096 and illustrative deductible 0.3150375457349501766499. The frozen checker was inspected, not executed; neither checker proves the all-parameter theorem.

## originality

PASS

The density, moments and qualitative quantile reversal are prior; classic one-crossing and integrated-tail principles are prior machinery. The supported distinct result is the full all-power stop-loss classification for the stated law, including the pair-independent positive deductible exactly in the subcritical regime and the mean-preserving order at the boundary. Available comparable statements do not establish that classification. This is not an absolute priority finding.

## value

PASS

An excess-loss premium depends on the whole upper tail, so a mean or a quantile table alone is not sufficient. The theorem tells when changing eta decreases premiums uniformly across deductibles, and when this fails, locates the unique preference reversal independently of the eta pair. The exact mean-preserving critical family is useful for comparing dispersion at matched means. This concerns fixed omega and model-based premiums, not real-data calibration or inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
