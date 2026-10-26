# Scientific assessment: resource-ancestry extinction bounds

## Correctness — PASS

The generator of Głuchowski–Menz [1, Section 1] makes source-labeled birth intensity exactly \(\theta/m\) times consumption of the same resource component because \(K\) is symmetric. The positive resource decomposition [1, equation (5)] limits the initial source to mass \(\mu_0(\mathbb R^d)\) and every corpse source to mass \(m\). Independent Poisson clocks in the accumulated-consumption coordinates produce a pathwise offspring upper envelope with independent Poisson(\(\theta\)) potential families, even though actual consumption depends on the interacting spatial history. Particle lifetime independence and the occupation identity give \(\tau_0\le S\). Classical Poisson offspring generating functions and independent exponential lifetimes then give the displayed subcritical exponential moment and critical \(t^{-1/2}\) upper bound. Verification checks: 52 numerical identities, independently evaluated Borel-series checks, and direct critical inequality tests. Computational tests are only corroboration; the proof is analytical.

## Originality — PASS, with residual priority risk

The closest identified paper is Głuchowski and Menz, arXiv:2610.21476v1, whose full model definition, theorem, extinction proof, and resource decomposition were inspected. Their theorem proves almost-sure extinction at \(\theta\le1\) via a supermartingale, but does not provide an extinction-time tail bound or this marked-resource Poisson forest. Borel, Dwass and standard Galton–Watson theory already give the offspring generating function and its singularity once an envelope is established; no originality is claimed for those formulas alone. The general Poisson-Galton–Watson integrability work of Hu–Sun (arXiv:2607.16833) addresses branching forests, not a spatial resource process coupled to a forest. General time-change or domination theorems may provide an equivalent method; comprehensive priority checking requires independent research. Searches compared both the exact model and broader implied results, and no covering statement was located.

## Mathematical value — PASS

The 2026 motivating work identifies the sharp extinction threshold but does not quantify extinction-time tails. For the same unmodified model, the result supplies a structural birth-charge ancestry coupling and quantitative, dimension- and kernel-uniform bounds in *both* the subcritical and critical regimes, with explicit permissible exponent and an explicit polynomial rate. This yields finite-time probabilities not inferable from the paper's qualitative almost-sure extinction statement. The square-root critical upper bound is intentionally one-sided and the subcritical exponent need not be optimal.

## Literature comparison and limits

Closest: Głuchowski–Menz, arXiv:2610.21476v1, full HTML read. Related: classical Poisson–Galton–Watson total progeny (Borel/Dwass); Hu–Sun arXiv:2607.16833, introduction and total-progeny formulation; Garcia (2016), Poisson projections/time-change abstract. Residual priority risk is an unlocated general resource-consumption/marked branching-envelope theorem. The result does not assert sharp physical-system decay rates, matching lower bounds, or applicability to an externally replenished resource model.

Self-review: passed. Independent audit: not yet performed.
