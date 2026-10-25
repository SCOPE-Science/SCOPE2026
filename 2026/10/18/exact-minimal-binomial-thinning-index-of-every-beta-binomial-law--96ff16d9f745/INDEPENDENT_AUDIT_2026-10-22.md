# Independent mathematical audit

## correctness

PASS

For all n>=1 and real a,b>0, the inverse PGF Q_alpha(z)=P_X(1-1/alpha+z/alpha) uniquely identifies an integer-valued latent Z supported on 0..n. Its q_k is binom(n,k)*alpha^{-n} E[W^k(alpha-W)^(n-k)]. Positivity is automatic for even n-k. For odd m, the Beta-Stein identity (vanishing endpoint terms for A,B>0), applied to (c-V)^(m-1), yields a nonnegative even-moment term and a size-biased Beta(A+1,B+1) term; induction at threshold L(A,B,m)=(A+m-1)/(A+B+m-1) succeeds. Size-bias W^k makes the threshold independent of k: alpha*=(a+n-1)/(a+b+n-1). q_{n-1} vanishes at alpha* and is strictly negative at every smaller positive alpha, giving sharpness. Q_alpha(1)=1 gives normalization including n=1. Independently rebuilt exact Fraction inverse/mass reconstruction and tested 28 rational (n,a,b) cases; this supports but does not prove real shape universality.

## originality

PASS

Kella & Löpker Theorem 19 (2022/2023) already gives an implicit root-maximization test for general binomial mixtures and Example 10 explicitly calculates uniform beta(1,1) case n/(n+1); both are recognized prior. No checked result evaluates the maximum for all real Beta(a,b) shapes or proves this common odd-moment threshold. Peyhardi and Jones concern generalized quasi-Pólya/convolution thinning rather than the fixed independent Bernoulli inverse scale. Inaccessible or older identity is residual priority risk.

## value

PASS

A natural beta-binomial exchangeable count family is completely classified by a simple rational minimum over a continuum of real shape parameters, avoiding an implicit polynomial root search and pinpointing a structural endpoint obstruction. Not merely the known uniform law or a plug-in reparametrization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
