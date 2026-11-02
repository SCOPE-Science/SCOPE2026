# Scientific review: threshold-work matching and cooling response

## Correctness — PASS

The claimed domain is finite-dimensional, nondegenerate, cyclic, unrestricted-unitary and two-projective-measurement. The critical reduction is exact: an arbitrary unistochastic transition matrix is doubly stochastic, a linear success functional attains its optimum at a permutation, and every permutation is an admissible unitary. For the nested threshold-eligibility graph, the Hall condition for a sorted winning source set is \(k_{s_t}\ge t\); the greedy algorithm produces coordinatewise-minimal feasible source indices. Strictly decreasing Gibbs weights make that source set uniquely optimal among winning sets, although the optimizing unitary need not be unique. The two-/three-level exclusion follows from explicit classifications of those greedy sets and monotonicity of the canonical mean energy. The four-level witness is exact, with a positive rational derivative \(17/160\) and a unique thermal peak. Gibbs passivity is established independently by majorization and summation by parts. These arguments prove the infinite families without extrapolating finite enumeration.

A standalone finite checker verifies 325 globally enumerated optimization instances at dimensions two through six with exact rational Gibbs weights. It checks the winning source sets of all optimal permutations as well as the four-level derivative, peak and negative mean in selected cases. The checker is corroboration, not an external certification or a substitute for the proof.

## Originality — PASS (qualified)

The closest 2026 primary paper, Cheng et al., arXiv:2610.30555, gives TPM statistics for a *two-stroke, thermally contacted* quantum Otto cycle (Sections II and IV, Appendix C). It does not present the all-unitary, same-Hamiltonian threshold-probability supremum or a minimum four-dimensional onset of a cooling-induced increase in the optimum. Cavina, Mari and Giovannetti, *Scientific Reports* **6** (2016), 29282, optimize probabilistic extraction over broader Jarzynski-compatible operation classes with quasi-static and thermalizing stages; their general bounds and attainability results do not assert this restricted spectrum-dependent matching formula. Their main argument and the multi-level Methods were examined. Relevant exact-term and synonymous statement searches in published mathematical records and accessible prior claims did not reveal an implication covering the combined theorem. The foundational use of Birkhoff decomposition, Hall matching, Gibbs passivity and canonical differentiation is not claimed as novel on its own.

The leading risk is an earlier optimal-tail or thermo-majorization theorem that implicitly contains the fixed-spectrum unitary answer. A zero-fluctuation quantum work reference was accessible only by its abstract, so it was not treated as a full-text negative comparison. The originality judgment is qualified; it does not establish absolute publication priority.

## Value — PASS

The quantity is a physically motivated, directly observable *maximum probability of delivering at least a specified work amount* in one cyclic stroke, not an arbitrary finite slice. The result gives its entire sharp spectrum-and-threshold law in all finite dimensions; identifies a temperature-independent optimal control; and proves the smallest Hilbert-space dimension at which cooling can initially improve this optimal stochastic extraction even though positive mean work remains impossible. The exact four-level onset resolves a qualitative design boundary, rather than merely recomputing a known table. The computational method needs only a spectrum ordering and a linear scan. The restriction to unrestricted cyclic unitaries means no claim about laboratory control complexity, dissipative engines or general quantum work measurements.

## Closest literature and residual limitations

- Cheng et al., *Probing quasiperiodic spectral accessibility with a finite-rate quantum Otto cycle*, arXiv:2610.30555 (first public 2026-10-22), main Sections II, IV and Appendix C: finite-rate Otto-cycle statistics, not same-spectrum one-stroke global optimization.
- Cavina, Mari and Giovannetti, *Optimal processes for probabilistic work extraction beyond the second law*, *Scientific Reports* **6**, 29282 (2016), full accessible main results and multi-level Methods: open/thermalizing protocols and Jarzynski bounds rather than an exact cyclic-unitary spectral matching envelope.
- Salvia and Giovannetti, *Zero-Fluctuation Quantum Work Extraction*, arXiv:2402.16964 (2024): abstract accessible; full text not inspected; potential broader overlap is a residual risk.

Independent mathematical and publication-priority audits remain to be performed.

Self-review: passed. Independent audit: not yet performed.
