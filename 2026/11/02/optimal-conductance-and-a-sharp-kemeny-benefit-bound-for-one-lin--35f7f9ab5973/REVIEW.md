# Scientific review

## Correctness — PASS

The statement uses the conductance-normalized discrete-time transition matrix and the standard eigenvalue convention for Kemeny's constant. The invariant antisymmetric mode, zero-mode multiplicities, and three-state quotient yield the exact rational identity; the special \(a=2\) quotient avoids an empty-class assumption. Differentiation of the normalized formula proves the unique positive optimizer and sign threshold; monotonicity in the part size reduces the global benefit bound to an exact quadratic inequality with an attained equality case. Exact rational matrix inversion independently checks 240 parameter triples. Boundary cases \(b=1\), \(t=0\), and \(a=2\) are included. Finite checks do not substitute for the analytic proof.

## Originality — PASS, with residual priority risk

Hu and Kirkland [1], Theorem 2.0.1, decisively cover the **unit-weight** specialization; this already-known special case is excluded from the new contribution. The same paper studies binary edge insertion in complete multipartite graphs and does not provide continuous edge-strength optimization. Altafini et al. [2] give general weighted perturbation machinery (a broader computational identity), but the inspected sections 2–4 do not give the explicit family-wide optimizer, sharp conductance threshold or graph-uniform \(1/6\) bound. Faught et al. [3] deal with 1-separable graphs. The new theorem is a continuous conductance-design classification and sharp cross-family optimization rather than a second assertion of the old binary edge formula. Relevant semantic-index searches found no explicit identical claim, but cannot establish priority, and a generic perturbation formula can be specialized by further algebra. This residual risk is disclosed.

## Value — PASS

A discrete choice to add a link and a continuous choice of its conductance give opposite recommendations on large balanced bicliques. The minimum is attained at a unique strength, while over-weighting can worsen the expected stationary-target hitting time. The sharp \(1/6\) bound holds simultaneously over every biclique size, every choice of a within-part pair and every new-link strength, with a natural equality family. These are global design facts not provided by the existing fixed-unit-edge classification or a generic numeric Kemeny update algorithm.

## Limits and closest literature

The closest coverage is Hu–Kirkland [1] for strength one, alongside general weighted Kemeny calculation in Altafini et al. [2]. There is no result here for multiple edges, unequal background conductances, other graph families, or independently verified publication priority. Exact computational checks are finite; all-size conclusions rest on the provided proof.

Self-review: passed. Independent audit: not yet performed.
