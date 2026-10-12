# Scientific review

## Correctness — PASS

The finite CTMC backward equations have a uniquely solvable transient block for every positive colonization rate. The four claimed rational solutions are reconstructed by exact elimination at 24 distinct positive integer rates; Cramer's-rule degree bounds turn this into an all-real-rate polynomial-identity certificate. Six differences are checked coefficientwise. All but one relevant comparison factor into polynomials with positive coefficients, and the sole varying sign is controlled by an eighth-degree polynomial with exactly one Descartes sign change and opposite exact values at 5 and 6. The claim does not depend on floating-point experimentation. The checker is a Python 3 standard-library script.

## Originality — PASS, with residual risk

Mountford et al. (arXiv:1203.2972) establish asymptotic contact-process extinction theory, not the finite four-patch single-site ordering. Barbillon et al. (arXiv:1404.4287), inspected in its full open-access text, use discrete-generation extinction-then-colonization and mainly fully occupied starts, rather than these continuous-time four-site single-source comparisons. Van de Bovenkamp and Van Mieghem (DOI:10.1103/PhysRevE.92.032806) provide general exact finite-state methodology and announced formulas for complete graphs and stars; that article's full text remained inaccessible. Its star result may anticipate a subset of our formulas, while its abstract does not supply the path comparison or unique switching polynomial. Previously unindexed exact small-network calculations remain possible; this review does not claim that failed searches prove novelty.

## Value — PASS

The initial introduction site is a genuine ecological decision variable, often distinct from background-network connectivity. The theorem classifies the complete fixed-size, fixed-edge comparison at the first tree order admitting two topologies and gives a qualitative colonization-dependent switch: weak colonization favors an internal source on a path over a peripheral star source; strong colonization reverses that conclusion. These are precise structural boundary conditions for rescue/reintroduction models, rather than an arbitrary isolated computed number. The result does not claim practical superiority outside the specified homogeneous four-patch model.

Self-review: passed. Independent audit: not yet performed.
