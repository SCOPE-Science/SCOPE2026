# Disproof of the short prime-sum minor-arc sup bound at length N^{5/6}

## Context

Uniform minor-arc suppression of short prime exponential sums is the noise bottleneck for narrow-window ternary Goldbach–Waring theorems. The admitted target asked whether the short sum of length h(N)=N^{5/6} admits a power-saving uniform bound sup_{m(N)}|S_h| <= h N^{-1/150} on standard Dirichlet minor arcs with denominator threshold Q0=(log N)^A. Existing literature (Matomäki–Shao discorrelation for theta>2/3, Liu–Zhan and Kumchev short Weyl-sum estimates, Wooley Vinogradov mean-value inputs) gives only qualitative little-o or differently normalized upper bounds, with no explicit sup power saving recorded at this width and arc system. Both a proof and a large-value disproof were admitted as complete, original, valuable resolutions.

## Definitions

Fix an integer A>=1. Put Q0(N)=(log N)^A, h(N)=N^{5/6}, X(N)=N/3,
S_h(alpha;N)=sum_{|p-X|<=h}(log p) e(p alpha), T(N)=S_h(0;N).
Let M(N) be any standard major-arc system: disjoint neighborhoods of a/q with (a,q)=1, q<=Q0, each of half-width at most W(N)=(log N)^B/N for some fixed B. Let m(N)=T\M(N). The target asserts sup_{alpha in m(N)}|S_h(alpha;N)|<=h N^{-1/150} for all large N.

## Result

The target is false. In fact, for every fixed delta>0, sup_{m(N)}|S_h|>h N^{-delta} for all large N. More precisely, all large N admit a minor-arc point with |S_h|>=(1+o(1)) h/(log N)^A. Consequently any covering sixth-moment bound strong enough to imply the sup bound is false too.

## Proof / evidence

Let q=q(N) be a prime with Q0<q<=2Q0 (Bertrand's postulate). For large N, 2Q0<<X-h, so no prime in the short interval is divisible by q. With residue-class weights E_r=sum_{|p-X|<=h, p=r mod q} log p, this gives exact vanishing E_0=0 for all large N. For S(a/q)=sum_r E_r e(ar/q), character orthogonality gives exactly sum_{a mod q} S(a/q)=qE_0=0 with S(0/q)=T. Hence sum_{a!=0} S(a/q)=-T, and max_{a!=0}|S(a/q)|>=T/(q-1)>=T/(2Q0)=T/(2(log N)^A). Since q is prime, every a!=0 is coprime to q. The Huxley short-interval prime number theorem (theta=5/6>7/12) gives T=(1+o(1))2h, so the lower bound is (1+o(1)) h/(log N)^A; any positive-proportion lower bound T>=c h would suffice. Minor-arc membership: if a/q!=a'/q' with q'<=Q0<q, then |a/q-a'/q'|>=1/(qq')>1/(2Q0^2), while N/(2(log N)^{2A+B})->infinity, so for all large N every such a/q is farther than W(N) from every major-arc center, i.e. a/q in m(N). Hence the maximizer a* gives a minor-arc point with |S_h(a*/q)|>=T/(q-1). Finally R(N)=N^{1/150}/(2(log N)^A)->infinity (and likewise with any fixed delta in place of 1/150), so T/(q-1)>>hN^{-1/150} for all large N, contradicting the target. The ratio audit solves k log 10/150>log 2+A log(k log 10) in log-space: first decade with R>1 is k=505 (A=1), k=1062 (A=2), k=2916 (A=5), monotone thereafter.

## Limitations

Finite computations reach only N~1.2e5 where the asymptotic ratio still favors the target; the contradiction is asymptotic via the cited Huxley short-interval PNT for T~2h and the analytic ratio limit R(N)->infinity, not a finite-N counterexample (crossover decades are astronomically large: 10^505/10^1062/10^2916 for A=1/2/5). The equivalent sixth-moment covering form is refuted only insofar as it would imply the false sup bound; no direct sixth-moment computation is claimed.

## Reproducibility

`output/artifacts/verify_obstruction.py` (stdlib only) replays: exact Parseval sum_a|S(a/q)|^2=q sum_r E_r^2, exact sum_a S(a/q)=qE_0=0, E_0=0, max_{a!=0}|S(a/q)|>=T/(q-1), spacing-lemma spot checks at (N,q)=(60000,127),(120000,139), and the log-inequality crossover audit; it prints VERIFY_OK. Cited inputs: Bertrand's postulate (exact, elementary) and the Huxley short-interval PNT at theta=5/6 for T~2h (any component giving T>=c h suffices).

## References

- Kaisa Matomäki, Xuancheng Shao, Discorrelation between primes in short intervals and polynomial phases, arXiv:1902.04708.
- Bingrong Huang, Exponential sums over primes in short intervals (2015 survey), expsum2015.pdf.
- R. C. Vaughan / Kumchev, On Weyl sums over primes in short intervals.
- T. D. Wooley, Nested efficient congruencing and relatives of Vinogradov's mean value theorem.
- Kaisa Matomäki, Xuancheng Shao, Terence Tao, Joni Teräväinen, Higher uniformity of arithmetic functions in short intervals I, Forum Math. Pi 2023.
- Huxley, primes in short intervals (theta=5/6 input for T~2h).
