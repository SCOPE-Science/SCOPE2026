# Independent mathematical audit

## correctness

PASS

Under independent Poisson rates a for Y reset and b for all positions reset, the invariant generator gives EY²=2Λ²/a, EY⁴=24Λ⁴/a², EX²=4Λ²/(ab), H=Cov(X²,Y²)=40Λ⁴/(a²(a+b)), M=E(X_i²X_j²)=32Λ⁴(a+6b)/(a²b²(a+b)), V=M-(EX²)²=16Λ⁴(a+11b)/(a²b²(a+b)). The Markov ODE K’+bK=2H exp(-at), K(0)=V, gives exact integral K(t). Conditional common-environment Gaussian pairs give same-coordinate extra 2M exp(-bt) by Wick and no-reset probability; n-coordinate average adds 2M exp(-bt)/n. With h(t)=exp(bt)K(t), h’=2H exp((b-a)t)>0, yielding monotone R and threshold a<=b. Independent symbolic simplification confirmed the a>b rational formula and resonance a=b, while inspected checker separately verifies stationarity and 72 substitutions. Absolute time covariance decays; claimed memory is a relative asymptotic. Boundary parameters a,b,Λ=0 are excluded.

## originality

PASS

Best-of-knowledge PASS specific to two independent reset clocks and the exact cross-/self-coordinate lag covariance ratio. The closest full primary paper of Santra–Basu–Sabhapandit resets Brownian diffusivity and positions simultaneously with one common clock; a second paper studies a shared diffusivity without the two-clock reset law; ordinary resetting autocorrelation methods do not directly state this threshold.

## value

PASS

The model isolates experimentally interpretable separation between medium renewal and positional reset; the exact nontrivial threshold in normalized fourth-order lag memory and residual non-self-averaging are motivated model-specific stochastic invariants, with a repeated-rate critical form rather than a routine equality of rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
