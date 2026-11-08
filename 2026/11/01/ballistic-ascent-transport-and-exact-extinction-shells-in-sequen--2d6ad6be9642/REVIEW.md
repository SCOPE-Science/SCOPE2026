# Independent mathematical audit

## correctness

PASS

For every n>=2, fixed left-to-right sequential closed-neighborhood (1,3) rule with unclipped endpoint persistence, the local recurrence y_i=(y_{i-1} OR x_{i+1}) if x_i=0, else (y_{i-1} AND x_{i+1}) is exact with y_0=x_(n+1)=0. Induction gives x_(i+1)=0=>y_i=0 and y_n=0; hence the complete set of 01 ascents shifts left exactly one index each sweep. Every nonzero ascent-free 1^a0^(n-a) configuration dies in one; a rightmost ascent j survives through the correct prior sweep and dies at exactly j+1. Counting rightmost ascent words gives n states at time1 and (n-t+1)*2^(t-2) at each t=2..n, all 2^n states accounted for; mean n-2+(n+2)/2^n and exact deficit probabilities (k+1)/2^(k+2) for k<=n-2. The residual mass at t=0,1 tends to zero, giving negative-binomial limit. Independent brute-force update with a separately written mutable-bit implementation reproduced the complete 2..13 state census: 16,380 starting states, including all ascents/time shells. Not a proof of infinite n.

## originality

PASS

The (1,3) bi-threshold and its Rule-178 alias are prior; Kuhlman et al. construct long cycles on cyclic/branched graphs, and Donoso-Leiva et al. analyze Rule 178 with sequential updates on periodic rings and existential update-order coverings. Their assertions do not imply the exact fixed ascending OPEN-path absorption-shell census. Related cycle-equivalence results concern eventual cycles and do not recover absorption depth. Resultary alternatives concern other cellular rules, domains and dynamical laws. Best-knowledge novelty is the path-specific exact finite-size and limiting law.

## value

PASS

The path is the canonical boundary-sensitive base graph contrasting known cycles and long periods at the SAME thresholds. A transport invariant of 01 domain walls yields a complete transient taxonomy, sharp maximal extinction n with exponentially many maximal states, and universal negative-binomial late-extinction deficit; this is structurally informative beyond a small-case enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
