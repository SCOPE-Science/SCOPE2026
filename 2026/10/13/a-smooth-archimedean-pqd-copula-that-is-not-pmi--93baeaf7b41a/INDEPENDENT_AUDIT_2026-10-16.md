# Independent mathematical audit

## correctness

PASS

On (0,1], φ(1)=0, φ(0+)=∞, φ'<0 and φ''>0 so the bivariate strict Archimedean copula exists. For f=φ+log t, f'(t)+tf''(t)=(t-1/2)²>=0; double integration gives f(uv)-f(u)-f(v)+f(1)>=0, implying φ(uv)>=φ(u)+φ(v) and hence C(u,v)>=uv globally. Differentiating implicit generator equation gives density c(u,v)=ell(u)ell(v)k(C)/ell(C)^3, with ell=-φ' and k=φ''. The fetched verification code performs exact Fraction root brackets using a bounded log-series remainder and monotone density enclosures: -0.019002196<Δc(1/4,1/4)<-0.019002192<0. Independent high precision direct evaluation gives approximately -0.019002193959, and independent symbolic first-order defect is -11/576. Reflected-density criterion of the original paper makes the C not PMI. Analytic PQD and exact PMI sign proof are separate and unrestricted on the unit square.

## originality

PASS

Fuchs-Tschimpke Conjecture 1 explicitly proposes equivalence PQD↔PMI in Archimedean class; their accessible full text develops PMI reflection criterion and non-Archimedean counterexamples but does not give this Archimedean generator. Their Markov-kernel total-positivity work is stronger in other dependence directions, not a refutation here. No prior same Archimedean obstruction found in searches; later/unindexed work is a priority risk.

## value

PASS

An explicit smooth strict Archimedean counterexample overturns a concrete published copula dependence conjecture, with a mathematically motivated reflection defect and a reproducible exact rational sign certificate; it is structurally informative rather than a mere parameter example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
