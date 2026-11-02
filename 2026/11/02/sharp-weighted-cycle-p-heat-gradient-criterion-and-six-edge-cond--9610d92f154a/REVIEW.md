# Review: sharp weighted-cycle \(p\)-heat gradient criterion

## Correctness — PASS

The claim and proof agree on finite cycles \(n\ge3\), all positive masses and conductances and \(1<p<\infty\), with metric edge lengths one. The signed edge-flow equation and the zero-sum condition jointly generate the four exact feasible-region maxima. Explicit normalized configurations attain each edge extremum; the finite-maximum Dini rule converts them into a sharp semigroup coefficient. Global well-posedness uses energy monotonicity and the maximum principle. For cycles of at least six vertices, summing the local rates and telescoping the mass-weighted conductance differences forces uniform conductance. For the pentagon example the monotone \(\ell_r\) profile has one subquadratic crossing. Rational and numerical checker diagnostics were replayed from the actual standalone file; they support, but do not prove, the universal formula.

## Originality — PASS (qualified)

Closest primary antecedents are Mugnolo (arXiv:1207.1996, nonlinear graph heat and vertex-norm contractivity), Hua–Mugnolo (arXiv:1410.1584, time regularity and extinction), and Münch–Wojciechowski (arXiv:1712.00875, general weighted *linear* graph heat Lipschitz decay). The latter covers the \(p=2\) method and is expressly prior art. An earlier unit-conductance cycle statement treats only homogeneous edges; the tree, multipartite, and product cases have different closure and adjacency constraints. The searched literature and published mathematical statements did not identify the all-exponent weighted-cycle coefficient. Unindexed equivalent nonlinear gradient theory remains a nonzero priority risk; database absence alone is not a novelty proof. Detailed implication comparisons, source material inspected and residual risks are in `AUDIT.json`.

## Mathematical value — PASS

The sharp coefficient solves the whole positive-weight continuous-parameter family rather than one sampled instance. Six vertices mark an exact mass-independent rigidity boundary, while five vertices permit a genuine nonlinear phase transition below \(p=2\). This is a motivated distinction between the evolution of individual edge gradients and vertex function norms. The evaluated derivative gives an immediately applicable smoothing/expansion test and quantitative decay when negative.

## Limitations

The result concerns one-input edge-Lipschitz contraction on unit metric edges, not two-input stability, edge-length-weighted Lipschitz norms, or infinite graphs. Strictly positive initial gradient decay coefficient need not remain attained for later times. Independent scientific audit is outstanding. The linear limit is not separately presented as novel.

Self-review: passed. Independent audit: not yet performed.
