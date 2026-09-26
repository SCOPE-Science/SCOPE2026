# Independent audit — 2026/09/09/079

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS, with a proof correction

The Borel example is exact: z and u(1) generate C₂×C₇ of order 14 inside SL(2,7), giving 24 base components (and 24 double-cover components of 28 vertices). For the displayed S_R, direct modular matrix checks give six distinct nonidentity trace-two elements plus −I; independently building the 336×336 Cayley adjacency matrix gives numerical extremal nontrivial eigenvalues 4.8872850069 and −4.6457513111. More decisively, I rebuilt the two integer matrices from the displayed generators and reran the original fraction-free elimination **from scratch**: 100A+489I is positive definite (minimum pivot 489), and 16430400I−3360000A+21436J is positive definite (minimum pivot 16451836). On 1⊥ the latter is 3360000(4.89I−A); thus −λ_min and λ₂ are each <4.89<2√6. The source's claim that a single Rayleigh quotient supplies an *upper* bound on λ₂ is mathematically false: it gives a lower bound by Courant–Fischer. The independent exact positive-definiteness certificate supplies the required upper proof. This error must not be propagated as a second proof.

## Originality — PASS

The interlacing existence results cited in the record do not exhibit this particular central-unipotent SL(2,7) set. The explicit seven generators, exact 336-dimensional spectrum certificate, and elementary disconnected counterexample make a bounded new classification observation within the admitted class. Priority beyond consulted primary interlacing sources is not guaranteed.

## Scientific value — PASS

A connected 7-regular bipartite Ramanujan Cayley double cover with a reproducible exact integer certificate directly refutes the proposed universal exclusion, while the Borel member shows a generating hypothesis is necessary. It does not classify other q or the whole class.

Sources: https://arxiv.org/abs/1304.4132 ; https://arxiv.org/abs/1506.02335 . Open preprints sufficed.
