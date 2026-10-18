# Self-review

## Correctness — PASS
The bound follows from the exact rotation action on \(\mathbb F_2^5\): two constant configurations and six shift-orbits of length five. Reversibility preserves these orbit sizes and forces the temporal length at most \(30\). The bundled executable exhaustively evaluates all \(65{,}536\) functions on all \(32\) states, cross-checks reversibility through a distinct eight-orbit criterion, computes exact temporal cycles, and checks algebraic-normal-form degrees. The claimed maximum and counts follow from a complete finite enumeration, not partial experiments. The four witness integers are independently reinterpreted and verified. No assertion is made for other ring lengths.

## Originality — PASS, with priority risk
The 2026 motivating preprint's accessible abstract establishes the diagonal criterion and first nonlinear diameter, not a temporal maximal-cycle tally. The 2022 maximal-cycle work was materially read as full extracted author-posted text: its dynamical system uses pairs of orthogonal CA with width \(2n\), not the single five-site periodic map studied here. The 2026 combinatorial-design survey concerns Latin squares and orthogonality. A published four-variable Boolean Walsh census has broad coverage of local functions but not their induced cyclic dynamical periods. Targeted searches found no prior exact \(96\)-rule maximal-cycle census. The complete motivating manuscript could not be read, so equivalent results may exist and the search cannot establish uniqueness.

## Mathematical value — PASS
This determines the sharp achievable temporal orbit length and the exact number of rules attaining it at the **first diameter with nonlinear reversible examples** in a natural diagonal-CA construction, refining its mere invertibility test into a dynamical classification. The \(30\)-cycle visits 30 of 32 states and is an intrinsically meaningful maximal permutation orbit constrained by shift symmetry; \(92\) such rules are nonlinear. The count is a nontrivial exhaustive invariant and supplies explicit reproducible witnesses, without claiming cryptographic usefulness.

## Closest literature and limitations
Dennunzio–Gadouleau–Mariot, arXiv:2605.18875v1, accessible abstract only. Mariot, arXiv:2203.02726v1, author-posted full text inspected. Manzoni–Mariot–Menara, DOI:10.1016/j.dam.2025.10.014, accessible substantial web text inspected. Risk: inaccessible complete 2026 paper and possible other non-indexed exact enumerations. Scope is exactly five-site binary dynamics.

Self-review: passed. Independent audit: not yet performed.
