# Scientific review

## Correctness
**PASS.** Exhaustive finite carry enumeration yields all \(18\) states and \(24\) edges for multiplier \(85\), and all \(3\) states for multiplier \(13\). The exact integer identity \((A_{85}^9-A_{85}^8-A_{85}^4-2A_{85}^2-I)\mathbf1=0\) on every reachable state proves the recurrence at all depths. Initial counts determine the rational series. Its factored denominator and positivity establish the common dominant growth constant; the published path-set dimension theorem completes the argument. The standalone integer verifier checks the full finite certificate and independent short prefixes.

## Originality
**PASS, with residual historical-priority risk.** Abram and Lagarias establish the general finite-automaton method and the same algebraic growth constant for multipliers \(13\) (their \(L_3\) family) and \(19\); neither result entails the specialized \(85\) recurrence or equality with \(13\) without an additional computation. Their sequel studies other infinite families, but only its abstract and bibliographic record were accessible for comparison. Specific search for the multiplier \(85\), equivalent ternary pattern \((10011)_3\), exact generating series, and matching eigenvalue returned no explicit matching theorem. This is not a proof of uniqueness, and further specialist tables may contain the numerical instance.

## Mathematical value
**PASS, narrowly.** Sparse ternary multiplier intersections are a natural test family for arithmetic sensitivity of fractal dimension. The \(18\)-state automaton for \(85\) has an unexpected ninth-order statewise recurrence and the same leading entropy as a distinct \(3\)-state automaton for \(13\). The exact recurrence specifies the entire prefix-complexity profile, while the equality shows that distinct arithmetic digit restrictions can have precisely the same dimension. Both facts make this finite case a reproducible structural benchmark, beyond a single numerical approximation.

## Sources and risks
The primary method and known examples are in Abram–Lagarias, arXiv:1308.3133, sections 2, 4 and 5, DOI:10.4171/JFG/11. The relevant sequel is Abram–Bolshakov–Lagarias, arXiv:1508.05967; full-text comparison was incomplete. Further undocumented calculations of multiplier \(85\) could affect historical priority. This is one exact specialized case, not a new general family theorem.

Self-review: passed. Independent audit: not yet performed.
