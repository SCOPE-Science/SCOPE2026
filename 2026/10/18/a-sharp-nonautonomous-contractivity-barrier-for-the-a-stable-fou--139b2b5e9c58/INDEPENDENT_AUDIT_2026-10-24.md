# Independent mathematical audit

## correctness

PASS

From the pinned nIRK4 tableau, with D=diag(a,2a/3,a/3,0), exact stage elimination gives det(I+AD)=(13a²+224a+1080)/1080>0 and R_var(a)=(1080−316a+36a²−2a³)/(1080+224a+13a²). The sign factor R−1=−a(2a²−23a+540)/Dnum (quadratic discriminant −3791), while R+1=−(2a³−49a²+92a−2160)/Dnum. Cubic derivative 2(a−1)(3a−46), extrema both negative, yields one positive crossing a*=24.426867812..., hence nonexpansivity iff a≤a*, and R_var(25)=−346/329, diverging magnitude as a→infty. The exact ODE flow is exp(−a/2). Independently reconstructed Gauss nodes/tableau from cardinal polynomials and its nine b_i Aij + b_j Aji = b_i b_j identities, proving energy decrement −2∑b_i lambda_i Y_i²<0 on this damping profile, with stage invertibility. Both autonomous functions equal diagonal [3/3] Padé; this does NOT imply variable-coefficient equality. Exact symbolic rederivation in independent_checks.py agreed. All-rate claims rely on algebra, not samples.

## originality

PASS

Inspected full arXiv HTML of Mizerová–Tvrdá 2404.16665v1, especially §3/§4 and Appendix A5: the exact A, b, c and autonomous stability function originate there; their experiments and A-stability claim are prior. The distinct parameter-dependent damping profile and exact noncontractivity frontier are not the same as autonomous A-stability and were not presented in the inspected primary account. Classical Gauss algebraic stability is credited. Resultary related published [2/2] Padé Markov positivity concerns stochastic endpoint positivity, not this nonautonomous scalar RK contractivity.

## value

PASS

A-stability alone is a common but invalid proxy for nonautonomous contractivity; the explicit sharp finite barrier for a published fourth-order tableau, with an exactly matched autonomous Padé function for a contractive comparator, is a useful numerical-analysis counterexample and reproducible benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
