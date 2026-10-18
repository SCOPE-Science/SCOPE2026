# Scientific review

## Correctness — PASS

For every fixed positive nonuniform digit law, the finite sum from arXiv:2309.07366, Theorem 4.2, gives a deficit equal to the expectation of the positive overlap function \(\phi\). Strict convexity of the likelihood moment function places the Chernoff tilt uniquely inside \(0,1\), where it centers the tilted log-likelihood increment and gives positive variance. The exact tilted representation of the deficit and the refinement gain is then subjected to the appropriate nonarithmetic or maximal-lattice local limit theorem. Direct Riemann integrability follows from exponential tails. Strict Jensen concavity gives positivity of every gain and of every lattice prefactor. Integration by parts evaluates the universal coefficient as a beta function. A separate finite checker compares direct enumeration and multinomial coefficients, tests monotone arclength growth, and checks the beta integral by quadrature. The numerical checks are not used in lieu of proof. External local-limit results are invoked as standard theorems; they are not separately reproved.

## Originality — PASS on accessible evidence

Pfeffer, Smith and Severa, arXiv:2309.07366v2, Sections 4.2 and 5.1, establish the finite formula and the limiting value \(2\) and explicitly ask for a rigorous quantification of the gain from each refinement. Their work does not state the sharp \(\rho^n/\sqrt n\) scale or beta and lattice-phase prefactors. Stone (1965) proves a general nonlattice local limit theorem, not the arclength identification. Sason (2018) discusses general divergence representations but does not state this geometry-specific result. Semantic searches of public mathematical findings for unfair dice, singular Bernoulli distribution-function arclength, Chernoff-scale asymptotics, and lattice corrections returned no claim implying the theorem. Previously catalogued mathematical claims were checked for statement-level overlap and have different objects or invariants. Risks: unindexed asymptotics and relevant non-open literature might contain the specialized conclusion; the complete Stone article was not materially read here.

## Value — PASS

The primary 2023 paper identifies the incremental arclength as an open quantitative problem. This theorem gives the complete leading behavior for the entire fixed, fully supported, biased iid \(q\)-ary family, including both the nonarithmetic and arithmetic possibilities. It identifies a statistically meaningful rate (Chernoff information), a nontrivial \(n^{-1/2}\) penalty, and a genuinely necessary lattice-phase correction. It permits principled comparisons of the arclength obtained from successive digit refinements, rather than supplying only finite tables.

## Limitations and closest literature

The original 2023 result supplies the exact finite formula and limiting arclength; it does not solve the quantitative step-size problem. This proof depends on classical local limit theorems, full support, strict bias and independence. The result does not claim an explicit rate for the small-order remainders, a zero-weight extension, or independent external certification.

Self-review: passed. Independent audit: not yet performed.
