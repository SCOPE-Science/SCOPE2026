# Independent mathematical audit

## correctness

PASS

In a welfare optimum every vertex must have at least one same-action neighbor: otherwise a unilateral flip creates strictly positive welfare on all its incident edges without losing any matched edge. Connectedness then leaves only unanimity for n=2,3, which is strict Nash. For n=4 a mixed optimum has two adjacent pairs choosing different actions. Their sum of matched-edge welfares is strictly below 4. On any graph the two unanimous welfares sum to 2|E|, so if the cross-cut has two or more edges, some unanimous profile has welfare at least 4. There must thus be one cross edge, forming a path. If the path preferences are (α,β,γ,δ) and its profile is aabb, comparison with all-a gives β+3γ+2δ<=2, and comparison with all-b gives 2α+3β+γ>=4. Since δ>0 and α<1, one has β+3γ<2<3β+γ, which forces β>1/2>γ. Each interior player strictly prefers its current matched edge to the alternative; leaves strictly match their only neighbors. The argument includes tied welfare maxima and uses the full continuum of open-interval types. Independent exact replay `python3 /workspace/branches/independent_checks.py 3` sums individual utilities in tenths and exhausts all 32 path profiles and all their individual reversals: unique optimum bbaaa has W=23/5, its third player's payoff rises from 2/5 to 3/5 by flipping, and the three Nash states are aaaaa, bbbaa, bbbbb with W=22/5, 9/2, 18/5, respectively. Thus 1/10 is an absolute unnormalized welfare gap, not a percentage. The frozen checker was inspected, not executed; its small graph grid is not needed in the continuum proof.

## originality

PASS

The utility and welfare model and the distinction between unconstrained welfare and best-equilibrium welfare are prior. The supported distinct contribution is the sharp connected-order threshold for every welfare maximizer to be a strict equilibrium and its exact P5 witness. The strongest inspected primary results give a polynomial welfare optimizer or complexity of optimizing over equilibria; they do not assert the universal n<=4 strictness property or the n=5 counterexample. The closest indexed records use anti-coordination or normalized costly stochastic coordination, different objectives or payoffs.

## value

PASS

The first failure of self-enforcing social optimality is a natural boundary in this canonical positive coordination game. The continuum proof explains why four vertices cannot suffice even with welfare ties, and the rational path example exhibits an exact welfare cost of requiring equilibrium without relying on a complicated graph or generic hardness construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
