# Independent mathematical audit

## correctness

PASS

For V uniform [μ−ε,μ+ε], delays a=(μ+ε)−1,b=(μ−ε)−1, observation [b,T] with T>2/μ, rewrite unhalved cost under t=s−V−1. Each t has eligibility J=[a,b]∩[b−t,T−t], density q(t), and conditional delay mean m(t). Completing the conditional square proves exact H(u)−H(u*)=κ²∫q(t)(proxy(t)−m(t))²dt for affine demand c+κs. Separate left strip t∈[0,b−a], middle, and right strip t∈[T−b,T−a], nonoverlapping for small ε. With normalized strip coordinate y=μ² t/ε (or shifted), q and m biases converge uniformly, giving each raw strip ∫(y/2)(1−y/2)² dy=1/6 and each clipped strip 1/12. Middle delay bias O(ε²) integrated over bounded horizon adds O(ε⁴). Hence raw cost=κ² ε³/(3μ⁶)+O(ε⁴), clipped=κ² ε³/(6μ⁶)+O(ε⁴); variance ε²/3 so order is variance^(3/2). Independently checked strip integrals by rational arithmetic and finite-width direct conditional quadrature for μ=1,2 and ε=.04,.02,.01; normalized ratios tend 1/3 and 1/6. No finite data used in place of the uniform asymptotic proof.

## originality

PASS

Göttlich–Schillinger introduce the uncertain-velocity transport setting, exact conditional-expectation optimizer and a higher-order mean-speed bound over an INTERIOR time window. The present result quantifies both actual boundary strips and two exact asymptotic constants over the entire observation horizon, including an explicitly defined projected-delay proxy not ascribed to the prior authors. Prior work on stochastic demand and chance constraints does not directly cover this velocity-induced boundary. Closest 2026 paper full text unavailable under current access (Oxford VPN disconnected); original abstract and scientific claims were examined, a substantive residual-priority risk. Best-of-knowledge PASS, not certified priority.

## value

PASS

The natural boundary of an actually observed transport horizon changes the approximation order from the interior O(Var(V)^2) to sharp Θ(Var(V)^(3/2)); the positive coefficient quantifies a real practical limitation of mean-speed controls, while clipped-delay correction halves but does not remove the loss. Precise assumptions and contrast with interior guarantee are explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
