# Independent mathematical audit

## correctness

PASS

For 0<q<1 and exact cap Lambda>1, with a=(Lambda-1)/2, constrained two-residual minimization is projection onto t in [-a,1+a]. While errors positive and decreasing, failure to cancel selects t=-a, yielding v0=1,v1=q,v(n+1)=q((1+a)v(n)-a v(n-1)); the first nonpositive hypothetical v is exactly the first zero actual iterate. Characteristic discriminant vanishes at a_-=(1-s)/(1+s), a_+=(1+s)/(1-s), s=sqrt(1-q). At/below a_- both positive modes preserve positivity, double-root boundary v_n=(1+ns)(1-s)^n>0; above, complex-root oscillation, unstable repeated-root coefficient, or negative dominant coefficient force a first nonpositive v. Thus terminate iff a>a_-, equivalently Lambda>(3-s)/(1+s). At a=1, v_n=q^(n/2)cos(n arccos sqrt q) and first zero index ceil(pi/(2 arccos sqrt q)); threshold tends to Lambda=3 as q->1, establishing sharp universal cap. No finite data substitutes for all-n root/phase proof.

## originality

PASS

Best-of-knowledge PASS: published capped windowed Anderson results prove convergence/rate estimates, not this exact one-dimensional finite-termination frontier or stopping index. Uncapped scalar termination is known, so novelty is specifically the sharp cap-dependent classification.

## value

PASS

The exact finite-versus-asymptotic dichotomy for a standard safeguarded online AA(1) algorithm and the smallest uniformly terminating cap distinguish a mathematically important dynamical property not determined by general asymptotic acceleration-rate theorems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
