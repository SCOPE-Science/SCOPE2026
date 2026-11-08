# Independent mathematical audit

## correctness

PASS

Checked independent-root-split recurrence with uniform K in [0,n-1] and singleton leaf base L_1=1, P_1=0. The exact GF for the mixed moment has A=(P(z)+zP’(z))/3+R(z), with [z^n]R=-(n+1)/9+2/(3n) for n>=2. Subtract means gives the covariance at every n; distribution polynomial F_n=v^(n-1)/n sum F_kF_(n-1-k) yields conditional numerator totals 0/80 at P<=10 and 1040/80 at P<=11 for L=3/4 (totals 2880/272), hence CDF crossing. Classical second moment formulas give Var(P)/n² ->7-2π²/3, Var(L)/n->2/45. Independent exact-fraction recurrence reproduced 49 nontrivial sizes and the n=7 crossing. Experiments do not replace the all-n generating-function proof.

## originality

PASS

Best-of-knowledge comparison of mathematical claims, implications, aliases and relevant primary texts; general tools are credited and historical priority is qualified. Holmgren–Janson 2014 treats fixed-size fringe-tree counts; a key-bearing leaf is a size-one fringe tree, but whole-tree internal path length has growing size toll and cannot be identified with a fixed fringe count. Resultary 6d69fbada9a9 concerns squared root imbalance rather than leaves.

## value

PASS

Leaf count is a natural branching/shape statistic; path length is expected search cost. An exact n-dependent negative covariance and a rigorously crossing conditional distribution distinguish weak negative dependence from stochastic monotonicity and quantify asymptotic decorrelation, a substantive question about two canonical BST functionals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
