# Scientific review

## Correctness — PASS

The result is established by a full analytical proof: coordinate-symbol averaging gives an optimizer with one weight per direction; the tensor factorization yields its exact eigenvalues; two necessary scalar inequalities give the sharp optimum. Uniqueness is stronger than symmetry reduction: every coordinate-singleton eigenspace saturates the top spectral bound in the averaged optimum, forcing the original (unaveraged) optimizer to have the same action there. On each coordinate fiber this fixes the complete-graph Laplacian and hence every edge weight. The exact finite checks (`verify.py`) corroborate these steps but are not substituted for the infinite-dimensional proof.

## Originality — PASS, with residual literature risk

The closest inspected primary comparison is Boyd–Diaconis–Parrilo–Xiao (arXiv:0709.0955, §§2–3.3): it includes symmetry reduction, Cartesian spectral facts and equal-alphabet Hamming optimum formulas. It does not explicitly state the mixed-alphabet formula or assert unrestricted optimizer rigidity in the inspected relevant parts. Boyd–Diaconis–Xiao (2004) gives the foundational general SDP method, not this all-edge uniqueness classification. Jafarizadeh (2026), §V-B and Hamming tables, concerns common alphabet \(q\) and adjacency-distance relations; no mixed-alphabet theorem was identified in the accessible relevant passages. The general techniques could permit a related derivation, and inaccessible or unindexed formulations remain a real risk; no exhaustive novelty certification is claimed.

## Value — PASS

The theorem resolves the entire unrestricted edge-allocation optimization, not just an averaged feasible construction. It gives a sharp arithmetic holding/no-holding boundary and a uniform SLEM for \(K_2^{\square(d-1)}\square K_q\) independent of arbitrarily large \(q\). The rigidity argument excludes hidden asymmetric optimizers and makes the weight prescription definitive for heterogeneous coordinate networks. These features address a natural fastest-mixing design problem rather than a narrow arbitrary parameter slice.

## Limits

The conclusion concerns symmetric row-stochastic time-homogeneous walks, not arbitrary nonreversible or nonuniform-stationary chains. The exact literature comparison is finite, and the proof should receive independent scrutiny before external reliance.

Self-review: passed. Independent audit: not yet performed.
