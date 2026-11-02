# Scientific review: finite BALFI incidence classification

## Correctness — PASS

The theorem has a complete proof valid for every integer \(m\ge1\). The BALFI equations reduce independently at every Boolean input-atom incidence to either three allowed local states (atom inside the argument) or two (atom outside). The \(\mathrm{ciw}\) and classical-negation restrictions leave the stated numbers of states; their intersection is unique. An isomorphism of the expanded algebras is precisely an atom permutation preserving the two operators, so Burnside applies to the induced incidence action. The complement of the argument identifies the inside and outside permutation sets. Each power of a permutation fixes exactly \(f(\tau)2^{c(\tau)-1}\) inside incidences; this establishes the nonstandard orbit formula. The rigidity estimate uses a valid fixed-incidence bound and the union bound. Binomiality is for the explicitly stated uniform labelled product measure. There is no reliance on extrapolating finite computations to general \(m\).

The standalone checker directly enumerates and verifies the complete finite tables for \(m\le2\) and independently verifies orbit calculations for \(m\le5\). All checks passed. Boundary conditions \(m=1\), the exceptional empty outside/inside restrictions, and the uniqueness of the \(\mathrm{ciw}\)-classical intersection are treated explicitly.

## Originality — PASS within inspected evidence

The 2020 BALFI paper establishes the defining algebraic equations and exhibits possible unary operations on a four-element Boolean reduct (Example 2.17); Proposition 3.4 identifies the \(\mathrm{ciw}\) identity. Its relevant full-text sections were read. It does not supply the arbitrary-atom two-color normal form, the three parameterized isomorphism-count formulas, or the asymptotic automorphism bound. The 2026 study establishes finite-model property and various axiomatic subvarieties but does not report such a census. Its relevant definition, finite-model, and extension sections were inspected. General Pólya/Burnside theory supplies a method, not the object-specific reduction and explicit action enumeration. Nearby published finite Boolean-algebra operator counts impose different operator equations.

Priority limitation: the 2020 four-element example does imply local special cases of the count, and the incidence normal form is a direct algebraic deduction; these are not represented as independent new semantic axioms. A logically equivalent global enumeration could exist in algebraic-enumeration literature using different terminology. No claim of exhaustive bibliographical uniqueness is made.

## Value — PASS

The algebraic semantics of a self-extensional paraconsistent logic is the natural collection of BALFI structures, so the distribution, identification up to isomorphism, and relation to the standard recovery extension are mathematically motivated, rather than arbitrary Boolean table counts. The theorem classifies *all* finite expansions on every finite Boolean reduct; distinguishes recoverable consistency and classical-negation strata; and gives the asymptotic symmetry behavior of each stratum. These formulas permit duplicate-free finite-model enumeration and quantify how rare classical collapse and the recovery axiom are among unconstrained finite models. The almost-sure triviality of automorphisms is a structural consequence beyond the raw labelled count. This is not a complexity improvement or a new decidability theorem, and none is claimed.

## Sources and residual risks

Primary sources were the full-text HTML of Carnielli–Coniglio–Fuenmayor (arXiv:2003.09522; Definition 2.10, Example 2.17, Proposition 3.4), and Coniglio–Mallea (arXiv:2608.28443; Definition 2.5 and finite-model/extension discussions). Their own algebraic axioms were used without modification. The most serious residual risk is prior equivalence in a differently named variety of unary Boolean-algebra expansions. The proof does not address infinite reducts or additional consistency propagation axioms.

Self-review: passed. Independent audit: not yet performed.
