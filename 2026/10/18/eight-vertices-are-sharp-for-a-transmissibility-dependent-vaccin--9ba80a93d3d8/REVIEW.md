# Independent mathematical audit

## correctness

PASS

For any unvaccinated x,y in a tree the unique path survives if v is deleted and its transmission probability is p^distance; sum over uniformly selected seeds yields E_v(p)=1+2F_v(p)/(n-1). If a candidate F_v coefficient vector has no larger partial sums than every competitor, summation by parts proves F_v(p)<=F_w(p) on [0,1]. Inspected original finite verifier enumerates all n^(n-2) labelled Prüfer trees for n=2..7 (18,248 total) and tests this sufficient exact prefix condition; an independently coded nonisomorphic-tree census found the corresponding common minimizer in all 24 unlabelled types. For edges (0,5),(0,1),(1,2),(2,3),(2,4),(5,6),(6,7), verified all eight deletion-polynomial coefficient vectors; among them only vertices 1 and 2 can minimize, with F2-F1=p(p^2+p^3-1), giving a unique switch at p≈0.754877666. Exhaustiveness is genuinely finite and the analytic inequalities cover all real p in (0,1).

## originality

PASS

Best-of-knowledge: prior exact small-graph epidemic analyses and immunization heuristics do not establish this precise all-trees-through-seven sharp eight-vertex crossover. Important subtlety: on a tree with a single seed, a continuous-time Markov SIR model with rate β and recovery ν has expected seed-target reachability p^distance at p=β/(β+ν); therefore the difference in dynamics alone cannot dismiss Holme’s n<=7 work, and that older census may already imply portions of the small-order case. The new eight-vertex witness and exact universal crossover remain not covered by the inspected sources.

## value

PASS

A sharp minimal tree-order threshold at which the optimal prophylactic vertex changes with transmissibility is a natural structural question for exact outbreak minimization; the finite lower-bound certificate and explicit analytic witness reveal where simple centrality targeting ceases to be robust. It is more than a parameter renaming or numerical heuristic: both necessity to order seven and a sharp order-eight counterexample are specified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
