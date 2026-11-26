# Independent mathematical audit

## correctness

PASS

For a fixed label-2 set S, positivity means that a vertex outside S costs w(v) if it has no neighbor in S and costs zero otherwise. On a crown every vertex on one shore is defended by two opposite 2s; with one opposite 2 only its match is undefended, and with none every vertex of that shore is undefended. Deleting a third 2 from a shore loses no defense across the shore and strictly lowers cost. The all-ones cost A+B is strictly beaten by doubling both vertices of the lightest matched pair because 2/n<1. A single 2 at a_i costs A+s with s=alpha_i+beta_i. If s<A, the matched pair costs 2s<A+s; if s>=A, the two-2 same-shore option costs A+P_A<A+s since P_A<A for n>=3. The other shore is symmetric. Evaluating the six remaining support types by the same defense rule gives every displayed term (an undefended match already in S is not charged twice). This argument handles arbitrary positive reals. `python3 /workspace/reviews/reproduce.py 5` exhausts ternary labelings at eight exact weight profiles including rationals; each of the six types wins uniquely on one of these, and direct optima per type agree with all six terms. The frozen checker was inspected, not executed. Its three named special cases do not on their own witness the two asymmetric types, which the new check does.

## originality

PASS

No applicable prior exact formula for arbitrary positive weights on crowns was found. The published complete-bipartite theorem differs in graph and value, while the prior unweighted exact same-graph census is only the constant-cost slice.

## value

PASS

Deleting a matching is a natural perturbation of a known exact weighted family, and the six cases quantify a real change: each can be uniquely optimal under positive weights. The proof reduces exponentially many ternary labelings to explicit bounded-size support templates for arbitrary order and arbitrary costs. The weighted information is not recoverable from the known scalar or unweighted census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
