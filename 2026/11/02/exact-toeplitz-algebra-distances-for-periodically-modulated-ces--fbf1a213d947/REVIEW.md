# Scientific review: periodic Cesàro row modulations

## Correctness (C): PASS

The claim concerns complex period-\(m\) diagonal row weights acting on the ordinary discrete Cesàro matrix over \(\ell^2\), for every finite \(m\ge1\). Its proof has six indispensable links: (i) bounded partial sums of any zero-mean periodic sequence yield \(O((1+L)^{-2})\) cancellation in the Cesàro Gram-kernel tail and hence a Hilbert–Schmidt error; (ii) the sharp Hardy estimate and weakly null logarithmic extremizers show \(\|C\|_{\mathrm{ess}}=2\); (iii) shift conjugation in the Calkin algebra rotates the period and fixes \(\pi(C)\); (iv) the positive finite-orbit average of squared distances gives the lower bound \(2\sqrt v\); (v) finite-rank output-row corrections of \(\mu C\) give the matching **distance infimum**, using Sang's established \(C\in\mathfrak T\); (vi) the cyclic first difference yields the exact essential commutator norm. The proof covers zero weights, nonreal phases, period one, and nonminimal periods. No unjustified attainment of the distance minimum is asserted.

Supplementary `verify.py` executed successfully on finite covariance identities, centering identities and kernel-tail inequalities. Its outputs are consistency checks, not substitutes for the operator-theoretic proof.

## Originality (O): PASS with residual risk

The motivating source, Sang (arXiv:2608.25740, entire available HTML; Theorem 1.1 and sections 1–5), proves the **unmodulated** Cesàro operator lies in the full Toeplitz algebra, but does not determine any quantitative distance for periodically modulated rows. Bellavita–Stylogiannis (arXiv:2409.10014, definition of essential shift commutant and Theorem 10) study integral-operator essential Toeplitzness, not the exact periodic diagonal-weight obstruction. Nikpour (DOI:10.21136/CMJ.2018.0391-17, Theorem 2.6, PDF pp. 475–477) gives a distance to *vanishing strongly asymptotic Toeplitz operators*: our rows already belong to that larger vanishing class, whereas their distance to the C*-Toeplitz algebra can be positive. published-finding corpus claim-level searches for periodic Cesàro row weighting, Calkin shift orbits and Toeplitz-algebra distances returned nearby but non-implication-equivalent objects. The accessible local research records likewise have no claim about this periodic multiplier family.

This does **not** establish absolute publication priority. The residual risk is a broader, unindexed periodic-operator-algebra distance theorem subsuming this case, or an earlier result framed as an essential fixed-point approximation problem. The claim is not represented as independently certified.

## Mathematical value (V): PASS

The 2026 Toeplitz membership breakthrough naturally raises the stability question under structured row perturbations. A qualitative answer (nonconstant periods leave the algebra) does not quantify the boundary. This theorem gives the exact operator-norm distance to both the full Toeplitz algebra and the larger essential shift commutant for every complex finite period; importantly, the invariant is the **period variance**, not the row maximum. It also determines the full essential-norm and shift-commutator profiles and provides explicit asymptotically optimal algebra elements. The connection between periodic cancellation, positive orbit averaging and a difficult ambient membership result is more than a change of notation or a finite table calculation. The theorem is specialized, but applies uniformly to arbitrary period length and complex weights. Broader almost-periodic weights and identification of all actual minimizers are not settled.

Self-review: passed. Independent audit: not yet performed.
