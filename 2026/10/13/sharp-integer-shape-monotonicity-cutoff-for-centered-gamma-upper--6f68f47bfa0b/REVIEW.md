# Independent mathematical audit

## correctness

PASS

For n>=1 and c>-1/3, Gamma(n,1)-n survival equals P(Poisson(n+c)<=n-1). Subtracting adjacent Poisson CDFs gives positive factor exp(-(n+c))(n+c)^n/n! times [1-I_n(c)], I_n(c)=integral_0^1 exp(-s)(1+s/(n+c))^n ds. The density-ratio calculation proves every adjacent increment strictly increasing in c on (-1,0]. First difference equals exp(-(2+c))(3+c-e), forcing c>=e-3. At c=e-3, first increment is zero, n=2 has 1-I_2=(2+2e-e^2)/(e(e-1)^2)>0, and n>=3 follows from h_n(s)=n log(1+s/(n-d))-s, d=3-e, the uniform Hoeffding range bound R<=(1-d)^2/[2(n-d)] and explicit negative mean/log-moment bound; checked the inequality chain and constants, yielding all later increments strictly positive. n+c>0 everywhere; equality, scale and strictly/non-strictly boundaries consistent. Independent 65-digit quadrature of increments n=1,2,3,4,5,10,25,100,500 corroborates but is not infinite proof.

## originality

PASS

Best-of-knowledge PASS: prior Pinelis theorem classifies real-shape monotonicity and proves eventual positivity of unit differences, not their uniform sharp integer-subsequence cutoff e-3; Sun-Hu-Sun concerns mean threshold. Integer rather than real shape is a distinct natural Erlang hypothesis; no searched source gives an implication of the precise n=1 equality plus all n>=2 strictness.

## value

PASS

Erlang waiting times are naturally indexed by integer stage count. Their centered upper tails acquire a sharp negative-shift monotonicity interval where the continuous-shape Gamma family lacks global monotonicity. The exact transition e-3 and equality classification are a potentially useful quantitative structural boundary, not a routine shift of the c=0 theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
