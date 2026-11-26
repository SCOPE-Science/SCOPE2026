# Independent mathematical audit

## correctness

PASS

Independently exhausted the cases by generating compositions of the entire participating profile over seven ballot types, then deleting each feasible unordered pair of types. The verifier computes whole-committee scores with exact doubled harmonic weights (0,2,3), compares supersets conditional on each winning singleton, and checks all Cartesian outcome comparisons separately from the frozen algorithm. The count of visited pairs agrees with the bijection between a remaining electorate and an independent multiset of two ballots, namely 28 binom(n+4,6). Every tested size from n=2 to 11 gives zero beneficial pairs (the optional empty remainder at n=2 also gives zero); n=12 gives six among 224224, with one canonical candidate-relabeling representative. Independently tracing that witness gives first-stage supports (5,5,5) after abstention and (7,5,6) before, and winner sets {AB,AC} and {AB}, respectively. The A ballot is indifferent and the AC ballot weakly gains in all outcomes and strictly in one. Each appended unanimous ballot contributes one identical first-round vote and one identical doubled second-round marginal to every applicable choice, so the example extends to all larger sizes. No voter coalition exists for n<2.

## originality

PASS

The same-rule Kelly literature covers different assertions: global PAV group participation, and sequential participation for single voters. The closest indexed census with all ties uses four candidates, three seats and one abstainer. The exact first two-voter failure at twelve total voters and its six-instance minimal orbit thus remain distinct in the inspected sources.

## value

PASS

Two seats are the natural low-size boundary at which known individual participation results prompt the joint-abstention question. Two abstainers and three candidates are the smallest nontrivial coalition and candidate-choice domains for this distinction. A sharp lower bound with a unique minimal orbit explains how a greedy all-ties choice correspondence breaks group participation even here, and the representative isolates exactly where Kelly weak-versus-strict comparisons enter. This is more useful than an isolated brute-force example without certified minimality or symmetry information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
