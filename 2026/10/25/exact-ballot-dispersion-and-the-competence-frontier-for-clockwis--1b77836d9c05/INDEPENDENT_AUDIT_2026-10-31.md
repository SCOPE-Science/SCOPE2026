# Independent mathematical audit

## correctness

PASS

The all-delegating event has probability r^n and contributes zero correct ballots, zero caster weight, and a lost strict majority; it is kept explicitly. For k≥1 casters, clockwise positive run lengths are a composition of n; marking a starting caster gives multiplicity n/k per ordered k-composition. Independent caster correctness signs give the stated exact coefficient-extraction PGF. For the dispersion, ∑W_j² counts ordered pairs whose ballots terminate at the same caster. For two distinct voters at clockwise distance d, the common-caster probability is r^d+r^(n-d)-2r^n; diagonal entries contribute 1-r^n. Summing yields the exact Q formula. With fixed 0<q<1, a union bound on runs length L=ceil(4 log n/|log r|) gives max W=O_P(log n). Truncated local squared weights have dependency range O(log n) and Var(n^-1 sum)=O(log^5 n/n); their mean tends to (2-q)/q. The conditional centered weighted-sign array therefore satisfies Lindeberg, giving S_n/√n⇒N(2c_D,(2-q)/q). The direct indicators average to independent Bernoulli with mean 1/2+(qc_D+(1-q)c_A)/√n, giving a second binomial CLT. Strict normal CDF monotonicity yields the frontier, including exact no-claim on its equality line. Independent rational brute enumeration of all indicator and caster-signal realizations for q,p=(1/2,1/2),(2/5,3/5),(3/4,5/7) and n=2..9 confirms 24 PGF and exact Q instances; asymptotics rely on the proven probabilistic estimates, not these finite checks.

## originality

PASS

General liquid-democracy truth tracking and influence-concentration results are established, but the inspected prior work uses random-target delegations, optimization over networks, or broad variance criteria rather than this unique one-direction deterministic-target cycle with exact all-delegating convention and matched local-alternative truth-tracking frontier. First-moment expected voting-power centrality results are not identical to the exact squared-weight moment or conditioned majority CLT. Earlier related fixed-guru cyclic delegation records have different rules; without their fully identified primary complete texts, possible stronger equivalent coverage remains a stated residual risk rather than an unsupported failure. The specific formulas and combined comparison survive those bounded searches.

## value

PASS

The cyclic delegation network is a minimal analytically tractable locality-constrained social-choice system. Its exact generating function and E∑W² measure how repeated ballots reuse the same noisy expert, and the limit derives a sharp, nontrivial information-versus-concentration competence threshold. The comparison can reverse depending on relative caster/noncaster skill, with the critical competence ratio explicit at q=1/2; the exact model boundary is mathematically motivated, not an arbitrary numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
