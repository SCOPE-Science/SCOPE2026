# Independent mathematical audit

## correctness

PASS

A uniform recursive tree is constructed with independent uniform earlier-parent choices. For fixed birth indices 2<=i<j<=n, the event that i has unique child j and no other descendants has exactly (i-1)(n-3)! parent sequences among (n-1)!, giving probability (i-1)/((n-1)(n-2)). Deleting the pair yields a uniform independent (n-2)-vertex recursive tree and a uniform earlier parent A among its first i-1 labels, with depth-sum law P_n|E_{i,j} =_d P_{n-2}+2D_A+3 independent of j. Summing over j gives the probability (i-1)(n-i)/((n-1)(n-2)), conditional mean and covariance with total path length exactly factor times [2(H_{i-1}-H_{n-2})+(n-2)/(n-1)]. The bracket increases by 2/i and crosses from negative at i=2 to positive at i=n-1 for n>=4; harmonic asymptotics yield alpha(1-alpha)(1+2log alpha) with root exp(-1/2). Independent exhaustive rational enumeration for n=3,...,8 corroborates all indexed covariances; only the deletion coupling proves arbitrary n.

## originality

PASS

Holmgren and Janson (2014) Theorems 1.4 and 1.15 describe aggregate fringe-subtree counts and their covariances, not a fixed birth-index two-vertex indicator paired with total root-path length. Feng et al. (2008) also study aggregate subtree-size phases; Fuchs/Hwang/Neininger address profiles. Resultary publication on forcing root attachment versus total path length concerns a different event and no two-vertex fringe deletion law. An aggregate covariance cannot recover opposing age-indexed contributions, so the additional exact conditional distribution and single sign switch are not merely rephrased. Specialist marked-fringe mixed moments might nevertheless predate this result.

## value

PASS

Birth index is natural in recursively grown trees, and conditioning on one local fringe cherry changes the global depth profile in opposite directions depending on arrival age. The exact conditional deletion coupling, finite sign threshold and macroscopic e^-1/2 crossover reveal localized contributions invisible to known aggregate statistics; useful for analyses of age-resolved fringe behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
