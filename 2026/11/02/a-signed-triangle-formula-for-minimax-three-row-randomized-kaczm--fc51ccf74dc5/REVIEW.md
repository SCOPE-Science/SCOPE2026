# Review of the signed-triangle minimax sampling theorem

**Correctness — PASS.** Invertibility makes the one-step Kaczmarz probability optimization exactly a trace-minimal diagonal PSD majorant problem. The proof constructs optimal complementary primal/dual certificates in each of three sign/reciprocal-triangle regimes and establishes uniqueness. The exact rational test suite reported 7,362 assertions, including 553 admissible Gram triples and every phase. The proof, not the finite tests, carries the universal claim.

**Originality — PASS, with residual risk.** Strohmer–Vershynin's convergence theorem, Dai–Soltanalian–Pelckmans's general probability SDP, the Pukelsheim–Torsney experimental-design equivalence theorem, and Saunderson and coauthors' trace-minimization/elliptope duality are all prior art. The corresponding original mathematical results and Agaskar–Wang–Lu's exact MSE paper were inspected. They do not state the complete explicit three-row sign/triangle formula and exact \(2/5\) transition in the material inspected. A specialized elliptope or optimal-design source not surfaced by the searches might cover some or all of this formula; novelty is not conclusively certified.

**Mathematical value — PASS.** The result is a complete analytic optimal-sampler classification for all real invertible three-row unit-norm systems, not a special graph or arbitrary parameter slice. The nontrivial switch between a one-dimensional and two-dimensional least-eigenvalue space and the explicit corner in a natural Gram family show useful structural information unavailable from the generic numerical SDP alone.

**Limitations.** One-step fixed iid expected-error minimax only; not exact multi-step mean-square optimality, adaptive row selection or arbitrary rectangular matrices. Finite computational checks are not an infinite proof; specialized historical coverage and independent expert validation remain unresolved.

Self-review: passed. Independent audit: not yet performed.
