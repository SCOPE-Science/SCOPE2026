# Scientific review: sharp reciprocal-sine rank resonances

## Correctness — PASS

The theorem has a fully specified nonzero-coordinate domain, a forward-defined invariant subset, and explicit real nonzero parameters. Its algebraic core is the exact identity \(F_2=F_3\) when \(c=\pm b\). On the complement, the displayed Jacobian determinant has the nonzero leading coefficient \(2ab^3c^3(b^2-c^2)/3\) along large equal coordinates. The proof checks all eight orthants and invokes the standard zero-set property of real-analytic functions; thus it covers all parameter signs, not a finite numerical sample. Every invariant measure is forced onto the diagonal by invariance, and two elementary intermediate-value arguments produce infinitely many admissible fixed points. The standalone symbolic/numerical checker passed. No nonexistent infinite-simulation certificate is claimed.

## Originality — PASS, subject to identified literature limits

The closest primary source is Yan, Jiang, Huang and Ding (2021), DOI 10.3390/e23091221, equation (2) and Section 2; it defines the same three-dimensional map and numerically evaluates the dynamics, but its inspected full-text HTML has no global if-and-only-if Jacobian-rank theorem or stationary-support classification. The earlier Cao, Mao and Zhou (2020), DOI 10.1016/j.sigpro.2020.107457, already defines the entire two-dimensional \((y,z)\) subsystem: the basic equal-parameter diagonal symmetry follows immediately, and is **not** counted as a novel observation on its own. The complete three-dimensional rank alternative, one-step singularity of all stationary measures, and nonvacuous infinite fixed-point family form the reviewed claim. A 2023 related-work account, DOI 10.1049/ipr2.12651, does not strengthen the 2D formula to this theorem. Conceptual and semantic searches found no exact covering theorem; this is not a proof of global priority.

The 2020 author-hosted article was inspected through available searchable PDF text, including its original 2D defining formula and dynamics discussion; independent page-image retrieval failed. This partial-inspection limit, as well as unindexed treatments of the degenerate-parameter case, remains a genuine priority risk. Generic assertions for arbitrary analytic maps are also not confused with a classification specific to this map.

## Mathematical value — PASS

The natural issue is whether a map proposed to add a third dynamical coordinate retains three degrees of freedom for every formally allowed nonzero parameter triple. The theorem answers exactly which parameter surfaces cause instant global loss of one dimension, and proves that these surfaces are sharp, not merely sufficient. It translates that geometric obstruction into a restriction on **every** invariant statistical state and its transverse linear spectrum, while constructing infinitely many invariant point masses to show the singular phenomenon is substantive. The rank-almost-everywhere converse requires a nontrivial coupled determinant calculation; the result is broader than a negative numerical check or a normalization observation. It can inform parameter selection and interpretation of dynamics, but makes no claim of encryption security consequences.

## Limits and independent status

A full-rank derivative away from resonance does not establish three positive Lyapunov exponents, an absolutely continuous invariant measure, or robust transitivity; on resonance two positive exponents are not ruled out. The equation is undefined at zero coordinates. The 2020 precursor might contain an overlooked equivalent result, and equivalent unindexed literature remains possible. These limitations do not alter the proved rank/statistical conclusion.

Self-review: passed. Independent audit: not yet performed.
