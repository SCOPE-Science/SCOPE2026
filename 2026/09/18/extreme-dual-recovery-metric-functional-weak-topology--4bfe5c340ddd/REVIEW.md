# Review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

The general T1 statement follows directly from internal metric functionals. For distinct x and y, the internal functional h_y differs by exactly d(x,y) between those two points, so a basic neighborhood with threshold smaller than d(x,y) contains x and excludes y. Swapping the points gives the reverse separation. This is compatible with the motivating paper's non-Hausdorff example, so no stronger general separation claim is being made.

For a real normed space, the topology comparison was checked in both directions under the stated hypothesis. Gutiérrez--Nevanlinna prove that every metric functional on a normed space is convex, and metric functionals are 1-Lipschitz. Thus every sublevel set is norm-closed and convex, hence weakly closed by Hahn--Banach separation. Every metric functional is therefore weakly lower semicontinuous, and every basic metric-functional open set is weakly open. This establishes tau_diamond subset tau_w without boundedness or completeness assumptions.

For the reverse inclusion under the extreme-span hypothesis, Walsh's Corollary 3.5 identifies extreme points of the dual unit ball with singleton Busemann points, hence with metric functionals. Central symmetry gives both e and -e as metric functionals. Since the new topology makes every metric functional lower semicontinuous, e and -e are both lower semicontinuous, which makes e continuous. Finite linear combinations remain continuous. If the extreme points algebraically span X*, all weak coordinate functionals are therefore tau_diamond-continuous, so tau_w subset tau_diamond.

The two advertised corollaries were checked separately. Strict convexity of X* makes every dual unit vector extreme. In finite dimension, Krein--Milman places the dual unit ball in the closed convex hull of its extreme points, while their linear span is automatically closed; hence the extreme points span all of X*. The C[0,1] strictness statement uses the unbounded tau_diamond-convergent sequence from the 2026 preprint together with the standard boundedness of weakly convergent sequences in Banach spaces.

## Originality

The full five-page version of Gutiérrez--Nevanlinna's arXiv:2609.19368 was inspected. It defines the topology, proves the metric-topology comparison, lower semicontinuity of metric functionals, equivalence with d-weak convergence for nets, a non-Hausdorff example, and Hausdorffness on normed spaces. It does not state a comparison theorem with the classical weak topology, a T1 theorem for arbitrary metric spaces, or an extreme-span equality criterion.

The earlier Gutiérrez--Nevanlinna paper arXiv:2506.04154 / DOI 10.4171/ZAA/1828 was inspected at its convexity result and proofs of the bounded-sequence and strictly-convex-dual statements. It already uses Walsh's Corollary 3.5 and proves that, for sequences, strict convexity of the dual forces d-weak convergence to imply ordinary weak convergence. That sequence-level statement is prior art and is not claimed as new. The new claim is the topology-level comparison, the arbitrary-net equality under the algebraic extreme-span condition, its finite-dimensional arbitrary-norm consequence, and the general T1 separation result.

Walsh's 2018 paper was inspected at Corollary 3.5, which identifies singleton Busemann points with extreme points of the dual unit ball. Kell's 2014 co-convex topology was checked as a distinct prior weak-topology construction that agrees with the classical weak topology on Banach spaces.

Targeted searches covered the exact and synonymous formulations metric-functional topology versus weak topology, d-weak nets with strictly convex dual, extreme dual points generating the weak topology, finite-dimensional metric-functional weak topology, and T1 separation for the new topology. No prior source stating the combined theorem or the extreme-span criterion was found. No matching SCOPE record was found by searches for metric functionals, d-weak convergence, the motivating authors, or strictly convex dual weak topology.

No inaccessible paper was identified whose title or available metadata specifically indicates the same theorem. Because the motivating topology preprint was submitted on 16 September 2026, unindexed or unpublished parallel work remains a residual risk.

## Value

The result gives the first direct placement of the newly introduced metric-functional topology inside a standard functional-analytic topology and identifies broad classes where the new construction recovers the classical weak topology exactly. Equality is a topological statement, so it controls arbitrary nets rather than only bounded sequences. The algebraic extreme-span condition cleanly unifies finite-dimensional spaces and spaces with strictly convex dual, while the C[0,1] construction proves that the comparison is genuinely nontrivial. The T1 theorem also gives the sharp general separation level in view of the known non-Hausdorff example.

## Limitations

The extreme-span condition is only sufficient and is not claimed necessary. The result does not characterize all normed spaces on which tau_diamond equals the weak topology, nor the full continuous linear dual of the metric-functional topology. It does not strengthen the general separation axiom beyond T1, which would be false. The motivating preprint is extremely recent, so parallel work may not yet be indexed.
