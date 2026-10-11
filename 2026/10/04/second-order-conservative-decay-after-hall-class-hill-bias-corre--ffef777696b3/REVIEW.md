# Independent mathematical audit

## correctness

PASS

The proof was reconstructed from the frozen package rather than accepted from its prior review. Under the exponential order-statistic representation, the exceedances above the kth exponential threshold are independent Exp(1), and the exact Hall increment is \(Y+\alpha\ell_z(Y)\). Integrating against Exp(1) gives \(m(z)=-\beta z/(1+\beta)+\beta z^2/(1+2\beta)+O(z^3)\). Since \(A=-\beta z\), the oracle correction cancels the linear term and leaves the positive quadratic term for either sign of \(c\). The chosen threshold window has \(r_n/\delta_n\to\infty\) and \(|z_n|r_n=o(\delta_n)\); order-statistic concentration is therefore superexponentially negligible on the \(k\delta_n^2\) scale. Centered Hall corrections are uniformly \(O(|z_n|)\), so Hoeffding likewise makes their \(\varepsilon\delta_n\) deviations negligible. What remains is the lower moderate deviation of a Gamma(k-1,1) average, whose rate is \(k\delta_n^2/2\). The missing 1/k mean term is negligible because \(k\delta_n^2\to\infty\).

## originality

PASS

Best-of-knowledge originality survives. Fresh semantic and web searches found the recent Gösgens--van Parys--Zwart paper as the uniquely close source and older Hill-bias literature, but no independently located statement of the sign-independent \(A^2\) residual combined with the \(kA^4\) one-sided exponent or target-decay threshold law. The accessible primary abstract confirms first-order second-order-bias and bias-corrected moderate-deviation coverage but does not state this residual regime. Full text of that very recent paper could not be obtained from arXiv/OA in this run, and the authorized institutional fallback was unavailable; under the owner rule this access limitation is retained as a material residual risk rather than treated as negative originality evidence.

## value

PASS

The result targets the precise reliability gap left after first-order bias cancellation in the motivating conservative tail-index problem. It identifies the next asymptotic safety scale, proves that the residual is conservative for both Hall signs, and converts that scale into a target-decay threshold law. This is a motivated probabilistic refinement, not a bare Taylor coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
