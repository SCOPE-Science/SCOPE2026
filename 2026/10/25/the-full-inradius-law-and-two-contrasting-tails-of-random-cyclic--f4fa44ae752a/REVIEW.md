# Scientific review: incircle-radius distribution of random cyclic triangles

## Correctness — PASS

The proof states the normalized Dirichlet simplex measure \(8/\pi^2\), derives the standard identity \(R=4\sin X\sin Y\sin Z\), and integrates the permissible half-angle-difference interval exactly. The threshold roots \(a_-(t),a_+(t)\) follow from the inequality \(2s(1-s)>t\). The small-radius limit counts all three simplex vertices using explicit hyperbolic-sublevel areas, with the remaining edge strips lower order. The near-maximum limit follows from the positive-definite Hessian at the unique equilateral shape. The embedded checker verifies Cartesian geometry, quadrature normalization, known moment identities and numerical endpoint trends. Its finite samples do not certify an infinite limiting statement; the analytic proof does. The only boundary atoms are absent, since samples are almost surely nondegenerate.

## Originality — PASS relative to inspected evidence

The closest historical paper is Kórus (2020), DOI:10.33401/fujma.692916: the same circular sampling experiment and same inradius statistic, but its entire article gives **only the expectation and variance**, not an inradius CDF or thin/near-equilateral tail. Those two known moments are not presented as novel. Finch (2016), arXiv:1610.00510, defines the identical uniform-circle model but develops different triangle attributes. Labelle (2023), DOI:10.5206/mt.v3i4.17136, gives a full inradius law under uniform feasible side triples with **fixed perimeter**, which is not the measure used here. Madras–KC (2006) develops regular-polygon random triangles, chiefly perimeter and area; Rao (1976) supplies classical circular-spacings input. Relevant records covering random circumradius in bodies, octahedron projected inradius, and deterministic triangle roundness do not imply this inradius CDF. The equivalent formulation via Euler's identity \(OI^2=1-2R\) was included in the comparison, as were aliases and existing geometric records. Historical priority is provisional; an inaccessible 2006 publisher PDF and incomplete indexing leave a residual risk.

## Mathematical value — PASS

A natural complete law for the intrinsic thickness measure of a canonical random triangle is mathematically useful independently of its first two moments. The exact quadrature gives arbitrary threshold probabilities, and the two sharp tail coefficients explain why almost-degenerate incircles carry a logarithmic enhancement while almost-equilateral incircles are linearly rare. The two mechanisms are proved from different geometric strata of the angular simplex, not inferred from simulation or an arbitrary chosen cutoff.

## Limits of review

This is a self-review. No independent validation or historical-priority certification is claimed. The new contribution is limited to the full distribution and endpoint laws, for independent uniform circular points only.

Self-review: passed. Independent audit: not yet performed.
