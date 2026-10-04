# Same-model review

## Correctness
PASS. The five update increments from equation (3.1) telescope exactly: infection transfers from \(S\) to \(E\), progression transfers from \(E\) to \(I\), and recovery plus disease mortality split the same removal from \(I\) into \(R\) and \(D\). All denominators are positive for the stated domain. The disease-free boundary counterexample is exact by substitution. `verify.py` replays representative cases using exact rational arithmetic.

## Originality
PASS. The primary source was inspected at the formula level. It explicitly advertises unconditional positivity and prints the strict implication \(U^k\ge0\Rightarrow U^{k+1}>0\), but a search of its text did not locate the exact conservation law. Targeted published-finding corpus and web searches found broader structure-preserving numerical literature and unrelated epidemic results, not this exact scheme-specific correction and invariant. Residual risk remains because literature search cannot establish absolute novelty.

## Value
PASS. The distinction between nonnegative and strictly positive compartment states matters at invariant epidemic boundaries, especially the disease-free state. Exact conservation of \(S+E+I+R+D\) is also a natural, directly useful numerical invariant that can detect implementation errors independently of trajectory fitting quality.

## Closest literature and limitations
General nonstandard finite-difference epidemic schemes can preserve positivity and qualitative dynamics, but those results do not imply the exact telescoping identity of Liu–Tian equation (3.1). This finding does not challenge the paper's whole control framework; it corrects the stated strictness and records an unstated invariant of the forward step.

Same-model review: passed. Independent audit: not yet performed.
