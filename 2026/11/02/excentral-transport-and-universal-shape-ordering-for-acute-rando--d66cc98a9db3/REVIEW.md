# Scientific review: excentral conditional shape transport

## Correctness — PASS

The sampling convention fixes a designated anchor among three independent uniform circle points before sorting the other two; this avoids the size bias that would arise from anchoring at the smallest absolute polar argument. The resulting three normalized angular gaps are exactly uniform on the positive angle simplex. By the inscribed-angle theorem they are the triangle angles divided by \(\pi\), up to a permutation. The acute region has the three vertices given by coordinate permutations of \((0,1/2,1/2)\); the excentral affine map has that exact image and two-dimensional Jacobian \(1/4\). It therefore transports the unconditional **entire** angle law to the acute-conditioned law. Its doubly stochastic matrix and centered scaling by \(-1/2\) prove weak majorization, strict majorization except equilateral, and exact quarter-scaling of centered angular variance. Trigonometric strict concavity checks support the area, perimeter and inradius assertions after common-circumradius normalization. All limits are for three independent, uniformly circular vertices; no finite numerical sample is being used to prove the continuous result.

Symbolic matrix calculation, 17,296 positive rational angle vectors and independent numerical conditional/rejection comparisons passed. Numerical evidence is supplemental; the affine and functional arguments close the proof.

## Originality — PASS, with residual historical risk

Wendel (1962) derives hemisphere coverage probabilities, which specialize to the known one-quarter acute-triangle event; probability alone does not identify an entire conditioned angle law. Akopyan–Edelsbrunner–Nikitenko (arXiv:2007.07783v1, pp. 4–6) explicitly recall that one-quarter event and study a different two-sphere point model; the inspected proof is not the excentral push-forward or a universal Schur-concave order. Edelman–Strang (2012, Sections 3 and 3.6) study Gaussian-vertex shape sampling and distinguish it from uniform angular sampling; those sampling laws cannot be silently identified. A later published record on center-containing triangles sampled from finite regular polygons covers first and second conditional area moments and their continuum limit, so those numbers are not claimed as original. Its indexed summary does not itself imply the majorization transport, but the complete publication was not accessible for comparison. Targeted published-record and open-literature searches for excentral random shapes, conditional uniform-angle laws, and stochastic area/perimeter dominance found no direct coverage; this is a bounded best-knowledge assessment, not proof of historical uniqueness.

## Value — PASS

The result replaces separate conditional integrations with a **single exact measure-preserving (after conditioning) shape coupling**: one draw generates both models, and one deterministic majorization relation orders *every* symmetric Schur-concave triangle-shape score at once. Area, perimeter and inradius are simultaneously and strictly improved; a natural continuous angular-deviation invariant satisfies a full-law exact quarter-scaling, not merely a mean identity. The theorem provides a direct rejection-free sampler for acute-triangle shape and clarifies why various natural geometric measures move together under a meaningful shape constraint. This structural conditional-distribution principle goes beyond reporting the textbook one-quarter probability or recomputing moments.

## Scope and priority limitations

The law concerns normalized angle-based geometry only; it does not couple the three original vertex locations. The three-point, circular, uniform sampling hypothesis is essential. The published finite-polygon record was inspected at indexed-summary level rather than in full, and broader historical angle-geometry literature may contain an equivalent identity. Historical originality cannot be certified by database partition or failed searches. No independent review has been carried out.

Self-review: passed. Independent audit: not yet performed.
