# Independent mathematical audit

## correctness

PASS

PASS. Git RESULT.md ddad38f57ac158799bd61944b64e5ee1f112931f and CHECK.py ee6ce8b5e541ccf613dc3f2362fadf06ab2c76d3 inspected. For nonzero ternary x, real l1 support functionals fix f_i=x_i where x_i !=0 and permit f_i in [-1,1] where x_i=0; therefore x perpendicular_B y iff abs(sum_{x_i!=0}x_i*y_i)<=sum_{x_i=0}abs(y_i). In iid ternary model probability rho/2 per sign, P(T=1)=rho^2/2, P(T=-1)=rho(2-rho)/2, P(T=0)=1-rho. Markov-Chernoff optimizing exp(u) gives theta(rho)=1-rho+rho*sqrt(rho(2-rho)); union of both signs and orientations has probability <=4theta^n. Condition on both samples nonzero (prob (1-(1-rho)^n)^2), treat repeated projective line as incompatible. Weighted clique-mass transfer (nonadjacent mass merger) proves incompatibility >=1/omega; hence omega_n >= (1-(1-rho)^n)^2/[4 theta^n]. Differentiating theta with t=1-rho, sqrt(1-t²) gives minimum t=1/sqrt2, theta=sqrt2-1/2. Ceiling and nth-root limit yield formula. Independently verified directed norm criterion against two half-step convex norm inequalities for ALL 64,676,6400 ordered ternary nonzero-vector pairs in n=2,3,4; checked optimizer rho~.292893 and exponential base~1.093836. Infinite dimension conclusion rests on analytic probabilistic proof, not pair enumeration.

## originality

PASS

PASS on bounded literature reading. The 2021 Arambasic-Guterman-Kuzma-Rajic-Zhilina full publicly presented Section 3 Example 3.7 provides 2^(n-1) mutual orthogonal directions in real/complex l_infty^n, not in l_1^n; it also proves universal linear lower bound and dimension-dependent upper bound. The 2024 Guterman-Kuzma-Singla-Zhilina primary article on orthodigraph recognition was materially read in HTML (Thm1.1 and Section1 context): it describes finite clique number/dimension classification, not this l1-specific exponential lower bound. Duality does not preserve two-sided BJ relation on primal projective lines, so the l_infty result is not a hidden l1 implication. Still, a 2022 survey chapter was only bibliographically accessible, and Resultary was unavailable.

## value

PASS

PASS. Exponential existence of mutual Birkhoff-James orthogonal projective directions in the canonical real l1^n spaces improves dramatically on universal linear-in-n examples; it distinguishes primal l1 from known dual l_infty constructions and establishes a concrete asymptotic invariant for the natural orthodigraph. The optimized ternary Chernoff construction and weighted graph clique argument are mathematically motivated. No claim to exact omega_n, optimal exponent, or explicit complete classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
