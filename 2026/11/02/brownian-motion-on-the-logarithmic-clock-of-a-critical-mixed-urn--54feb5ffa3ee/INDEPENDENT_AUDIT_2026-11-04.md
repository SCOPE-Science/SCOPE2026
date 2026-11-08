# Independent mathematical audit

## correctness

PASS

PASS: In the exact two-colour Bernoulli mixed replacement model, h=E[H]=mu/2 on 4bp=mu. Conditional urn drift E[Delta U|F]=hU/T, centered martingale difference zeta=H epsilon-hU/T has E[zeta^2|F]=q-h^2(U/T)^2. With T_n=mu n+O(sqrt(n)log n) almost surely, W_n=U_n/sqrt(n) obeys W_k-W_{k-1}=zeta_k/sqrt(k)+beta_k W_{k-1}, beta_k=sqrt((k-1)/k)(1+h/T_{k-1})-1=O(k^-2+k^-3/2 log k); summable beta W follows maximal Azuma/Gronwall. Hence W_n-S_n is a.s. bounded/convergent, S_n=sum zeta_k/sqrt(k), and predictable log-time bracket tends uniformly to q t, Lindeberg jumps O(1/sqrt(log N)). Martingale FCLT gives X_N(t)=>sqrt(q)B(t) in J1 including t=0. Finite exact source checker inspected and independent moment algebra checked; source log alone does not establish FCLT.

## originality

PASS

PASS, best-of-knowledge qualified: Shi-Yin-Miao's mixed urn theorem is in the strict 4bp>mu regime and does not state equality/log-clock. Fang already proves essentially the same Brownian logarithmic clock for critical elephant random walks, so time change and shape are prior. The Bernoulli mixture with random T_n requires explicit summable-denominator correction; an equivalent corollary of broad Janson generalized random-urn results remains substantial priority risk because full text was inaccessible. No novelty claim to the time-change principle itself.

## value

PASS

PASS: The exact critical surface of the recently posed mixed urn is an analytically meaningful missing phase boundary; its joint polynomial-time fluctuations and variance q min(s,t) distinguish an entire process limit from a marginal CLT. Extension to random-total Bernoulli replacements is a concrete issue requiring control, although technique and log clock have precedents.

The dated certificate retains the supplied scientific assessment, sources and limitations.
