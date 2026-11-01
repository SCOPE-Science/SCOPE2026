# Independent mathematical audit

## correctness

PASS

PASS: Reconstructed the three exhaustive merger types with probabilities b(b-1)/[k(k-1)], 2b(k-b)/[k(k-1)], (k-b)(k-b-1)/[k(k-1)]. The independent Exp(binomial(k,2)) waiting interval adds b times its length to E, and two-singleton merging adds one cherry. First moments f=b(b-1)/[3(k-1)] and g=2b/k and total-covariance induction give K(b,k)=-2b(b-1)(3k-2b-2)/[9k(k-1)(k-2)]. k=3,b=3 is exceptional, yielding zero, while k=3,b=2 yields -2/9. k>=4 successors cannot have b=3,k=3; the induction is therefore valid. Taking b=k=n>=4 yields -2/9, with n=2,3 separately zero. Independent exact joint-moment recursion reconstructed 1,125 partial states up to k=46 including boundaries; finite verification supplements the symbolic recurrence, not the all-n proof. Clock normalization is essential.

## originality

PASS

PASS, best of knowledge: Janson-Kersting develop the external/singleton coalescent machinery, Wu-Choi the cherry/pitchfork topology, and Alimpiev-Rosenberg a compendium of metric coalescent covariances; the inspected statements do not yield an evaluated mixed cherry-count versus total external-length covariance -2/9 or the partial-state rational kernel. General merger recurrences make it calculable but do not explicitly imply the closed evaluated identity without additional derivation. Priority may overlap unindexed mixed-moment calculations.

## value

PASS

PASS: This exact cross-covariance measures dependence between a natural topological tree statistic (cherries) and a natural metric statistic (total pendant length). The size-independent -2/9 and strictly negative partial-state kernel explain an asymptotically vanishing correlation despite a persistent covariance and form a useful structural finite-size identity, not a marginal-moment restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
