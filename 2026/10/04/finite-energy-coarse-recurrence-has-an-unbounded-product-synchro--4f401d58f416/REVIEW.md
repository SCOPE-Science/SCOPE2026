# Same-model review

## Correctness
PASS. Projection of a max-metric product chain gives factor chains with no larger \(\ell^p\) error, proving the universal lower bound. At \(p=\infty\), factor return chains can be concatenated to a common length without increasing the maximum step error, which proves the exact max formula.

For finite \(p\), the example was checked from the transition graph. Below the large distance \(D\), each factor has only exact moves and one admissible unit reset. Returning the distinguished point therefore forces a reset every \(L\) steps. In the \((L,M)\) product, a minimal common block has resets on the union of the multiples of \(L\) and \(M\), giving exactly \(M/g+L/g-1\) unit-error steps, where \(g=\gcd(L,M)\). Choosing \(D\) above the resulting \(\ell^p\) norm excludes cheaper paths with a large jump.

## Originality
PASS. The motivating 2025 coarse-chain paper defines the positive \(\varepsilon\)-\(\ell^p\) filtrations and circulation viewpoint but contains no product discussion. The closest earlier product paper proves zero-level results for ordinary and strong chain recurrence and explicitly notes the concatenation difficulty for strong chains. It does not state or imply the positive-threshold dichotomy, the exact synchronization count, or the unbounded finite-\(p\) amplification.

Residual risk: product properties of related pseudo-orbit filtrations may exist under different terminology. Searches for coarse/\(\varepsilon\)-chain recurrence products and \(\ell^p\)-chain products did not reveal an equivalent quantitative theorem.

## Value
PASS. The source motivates the positive filtration as a control/noise budget. Product systems are basic constructions, and the theorem identifies a qualitative change in how budgets compose: stepwise control obeys an exact max law, whereas every finite accumulated-energy norm can suffer an arbitrarily large synchronization penalty. The explicit finite examples isolate the mechanism and supply a sharp boundary at \(p=\infty\).

## Closest literature and limitations
Yokoyama supplies the new coarse-recurrence filtration and control interpretation. Wiseman supplies the nearest classical product comparison and the observation that strong-chain errors accumulate under concatenation. The present theorem works at positive coarse scale and gives an exact finite-state amplification law. It does not address the negative-error branch, arbitrary product metrics, or general formulas for all systems.

Same-model review: passed. Independent audit: not yet performed.
