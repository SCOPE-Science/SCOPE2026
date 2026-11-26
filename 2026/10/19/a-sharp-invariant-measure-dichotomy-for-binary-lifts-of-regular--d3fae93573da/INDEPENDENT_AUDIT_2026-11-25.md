# Independent mathematical audit

## correctness

PASS

Applies to repairs/1/RESULT.md. The original assertion of only finitely many non-generating points is false. For each k choose phase i*p_k modulo p_(k+1) so that index -1 is the fill immediately preceding subblock i, obtaining either 0 or 1 while rho_k=0; both choices exist for q_k>=4. Compactness produces two base points with aligned phase zero and different symbols at -1, agreeing at all other coordinates. Lifts with the same x_0 agree on the nonnegative ray. Each of their common nonnegative shifts gives an indistinguishable pair for the tower partitions: the level-k start in the original lift is m-(m mod p_k)>=0 for shift m>=0. Their distinct embedded integer phases give infinitely many exceptions. The repair instead uses phase uniformity and cylinder windows enlarged to include the origin; the bad-phase mass for a difference window of length L is at most L/p_k. This proves measure determination and shows why no finite point-exception claim is needed. Even parity and the two consecutive odd fills give q_k-1 unchanged and one switched subblock start, with exact normalization by q_k. The replacement proves surjectivity of the compatible-vector description by weighted finite orbit segments with endpoint error at most 2||f||/p_k; clopenness preserves the projected masses. It also gives a direct minimality proof: every cylinder contains an atom from a noninteger-phase lift, and any full next-level block visits both level-k bases. The difference coordinate is multiplied by 1-2/q_k, whose negative logarithm is comparable to 1/q_k; compatibility gives either the unique balanced family or the affine segment parametrized by tP_k, with its extreme points precisely the ergodic measures. The original checker was inspected, not executed; it has three nested examples, not four, and is only finite incidence evidence. The repair is a complete corrected RESULT.md; no other mathematical support file depends on the false finiteness assertion.

## originality

PASS

Pass for the repaired exact two-regime classification and all-measure tower-mass simplex, not for the recursive construction, minimality, the summable non-unique direction by itself, or Bratteli theory. Same-construction prior work already implies the latter non-unique direction but its one-sided discrepancy bound cannot decide the divergent case or determine the measures. The concrete measure-determining partitions and explicit compatible family fill that gap.

## value

PASS

The repaired statement gives a sharp, simple sequence criterion, both regimes within a fixed established family, and a complete simplex with computable tower observables despite the same regular uniquely ergodic base mechanism. This goes beyond adding another existential non-unique lift. The result concerns this family only and does not claim new general symbolic dynamics machinery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
