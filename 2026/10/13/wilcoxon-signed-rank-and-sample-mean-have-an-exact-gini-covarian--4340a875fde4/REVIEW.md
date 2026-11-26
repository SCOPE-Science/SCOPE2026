# Independent mathematical audit

## correctness

PASS

Independent derivation: write X_i=S_i A_i with A_i=|X_i| and independent fair signs S_i conditional on the magnitudes. The conditional signed-rank mean is constant and its conditional variance is sum r²/4, giving n(n+1)(2n+1)/24. The conditional covariance with the mean is (1/(2n)) sum r A_(r). With no ties, sum r A_(r) equals sum A_i plus the sum over unordered pairs of max(A_i,A_j). The identity max(|x|,|y|)=(|x+y|+|x-y|)/2 and symmetry give expected pair maximum Δ. Thus the unconditional covariance is μ_1/2+(n−1)Δ/4 without using the Walsh representation. The frozen Walsh proof agrees: a diagonal pair contributes E|X|/2 and each off-diagonal pair contributes E|X-X'|/2 before division by n. Atomlessness and independence give the required no-tie conditions, and the second moment guarantees finite covariance. At n=1 only the diagonal survives. Normalizing by σ²/n and the rank variance gives the displayed general, Gaussian and uniform correlations and the limit. The 3/π comparison is numeric equality with the Gaussian efficiency, not an asserted efficiency theorem for all laws. The bundled finite checker was inspected, not executed; these analytic identities apply to all n and do not rely on its checks.

## originality

PASS

The signed-rank null variance, the Walsh identity and Gaussian Pitman efficiency are not new. The accepted distinct statement is the exact finite-n mixed covariance of the signed rank and sample mean, with its law-dependent Gini coefficient and exact diagonal correction. The inspected references and catalogue results do not state or directly supply that mixed identity. The conclusion is bounded by the reported access limitations.

## value

PASS

For two standard location statistics, the exact dependence on the same sample is a useful quantity when comparing or combining them. The finite formula identifies the population quantity controlling that dependence, including the small-n correction and limiting contrast between Gaussian and uniform parents. This interpretation is distinct from a null marginal table or a rederivation of Gaussian efficiency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
