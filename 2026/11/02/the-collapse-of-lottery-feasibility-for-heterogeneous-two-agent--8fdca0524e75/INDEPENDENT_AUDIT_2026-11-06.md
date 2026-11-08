# Independent mathematical audit

## correctness

PASS

Every fPO allocation must assign type-(1,0) to cost-zero agent2 and type-(0,1) to cost-zero agent1, and any such allocation reaches minimum possible aggregate cost c. Shared assignment count x satisfies WEF precisely pc-qb<=x<=p(c+a). If a>0, agent2 necessarily holds a zero-cost chore; strong WEFX upon its removal enforces the lower bound in every lottery support, while ex-ante upper bound on E[x] ensures at least one support allocation meets upper bound; reverse for b>0. Hence point mass iff, and independent binomial choices yield 2^d sum C(c,x). Independent exhaustive small cases with a+b>=1, total chores≤6 and rational weights confirm criterion and count (728 cases); proof handles all nonnegative counts and p∈(0,1).

## originality

PASS

Best-of-knowledge original strong WEFX zero-cost removal collapse, exact unequal-weight instance-level feasibility interval, and labeled deterministic counts; existing deterministic WEFX+fPO existence, equal-weight lottery results, subsidy-based and WEF1T results address logically weaker/different outcomes.

## value

PASS

A natural best-of-both-worlds fair-division question in the first heterogeneous binary-cost domain; a one-sided chore can collapse randomization feasibility to an integer deterministic threshold and yields a sharp definition-sensitive boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
