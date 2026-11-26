# Independent mathematical audit

## correctness

PASS

In a closed rank-at-most-one sentence, each quantifier matrix has only its own possible free variable; above those quantifiers, splitting disjunction on the singleton empty assignment reduces to ordinary disjunction by the empty-team property. In the matrix, a support-preserving induced restriction preserves quantifier-free satisfaction on any retained subteam and is downward closed, so a true universal persists. An existential is equivalent to the existence of a satisfying singleton by downward closure, and singleton matrix truth depends only on its colour. This proves the necessary order property, up to isomorphism. For the converse, U_{t,k} recognizes n_t<=k because its non-t disjunct cannot receive t and each constancy disjunct can receive at most one t-assignment; if there are at most k, the required split exists. U_{t,0} is literal colour exclusion. Guards select the exact support, and in the positive multiplicity orthant, Dickson's lemma gives a finite antichain of minimal exclusions, each avoided by a disjunction of the upper bounds n_t<=b_t−1. Empty and full fibres, and the empty class, are covered by this construction. In pure equality, the exact one-variable team capacities are zero/infinite for false/true literals, one for constancy, and infinite for dependence with a nonempty determining tuple (only x can occur). Conjunction takes min, splitting disjunction adds; overlap never raises the bound, and a disjoint split realizes it. Every finite capacity is bounded by the number of constancy occurrences by induction. Existentials have constant truth across nonempty sets, and the outer min/max of cutoffs must select a universal cutoff k if the whole spectrum is {1,...,k}. The k-fold constancy split attains that cost. The checker was inspected, not run; in its synthesis check it selects the support in code, so that specific test checks the obstruction formula on an already selected fibre, not a direct evaluation of the written existential guard. The general proof covers the guard independently.

## originality

PASS

The exact rank-one classification on finite unary structures, the associated formula construction, and the sharp pure-set occurrence bound survive the comparison. Downward closure, the expressive behavior of constancy over teams, and the finite-basis lemma are ingredients, not themselves new results. The closest catalog normal form is for a different logic and a different preservation order; general dependence-logic normal forms and games do not supply this combination of finite-domain expressiveness and syntax-sensitive cost.

## value

PASS

This gives a complete answer at the first nontrivial quantifier rank for a natural finite-structure class. The exact support-fibre invariant identifies what positive multiplicity information can and cannot be expressed, with finite formula synthesis and a sharp separation between quantifier rank and atom cost. It is more informative than showing unbounded finite thresholds alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
