# Independent scientific audit — SCOPE-20260919-1615b82a083d

Audited at: 2026-10-01T13:18:12.002998Z

Disposition: **passed**

## Correctness — PASS

The normalization by a triangular change of q and a translation of p is valid. For normalized W=A(p)q+R(p) with degree A=d at least 2 and degree R below d, the total-degree filtration gives d deg(P)+deg(Q)=d+1 for an isotropy automorphism, forcing both generator images to have degree one. Unique factorization of the leading form forces the linear part to be diagonal; the missing \(p^{d-1}\) coefficient then forces zero translation, and the lower-degree comparison forces zero q-translation. The remaining coefficient conditions give exactly the stated finite cyclic group. Iterating ad_W on p raises polynomial degree by d-1 each time, proving non-local-finiteness. The constant and linear branches agree with the established normal forms.

## Originality — PASS

The recent primary source proves the isotropy criterion for locally finite derivations and explicitly leaves the arbitrary Weyl-algebra case open. Its normal-form theorem covers the constant and linear branches, not the non-locally-finite first-order family of degree at least two. Resultary search found the audited record itself but no earlier equivalent first-order cyclic-stabilizer theorem.

### Equivalent formulations

No equivalent theorem for the whole first-order-in-q stratum was located.

### Broader coverage

The primary theorem is strictly narrower on the nonlinear first-order branch, while the classical machinery is an ingredient rather than a dominating statement.

### Exact database or table

No natural database/table supplies this classification; the check is literature-oriented and found no prior exact entry.

### Claim versus prior implication

The nonlinear branch is not a corollary of the cited local-finiteness criterion; it requires the new filtered-degree stabilizer argument.

## Value — PASS

The first-order-in-q stratum is a natural infinite-dimensional boundary class for the newly posed isotropy criterion. The theorem resolves that whole stratum, including genuinely non-locally-finite derivations, and gives an exact cyclic stabilizer rather than merely boundedness.

## Sources inspected

- A Characterization of Local Nilpotence for Derivations of Ore Extensions — https://arxiv.org/abs/2609.19470v1. NOT_COVERING: The paper proves the criterion for nonzero locally finite derivations and explicitly asks the unrestricted Weyl-algebra question; it does not classify the degree-at-least-two first-order family.

## Checked sources

- https://arxiv.org/abs/2609.19470v1
- https://doi.org/10.24033/bsmf.1667
- https://doi.org/10.24033/bsmf.2010
- Resultary semantic search

## Residual risks

- Equivalent stabilizer computations may be implicit in older Weyl-algebra or polynomial-automorphism literature under different terminology.

## Limitations

- The theorem is restricted to q-degree at most one (and its Fourier-symmetric counterpart).
- It does not settle mixed elements of higher q-degree.
- Originality is best-of-knowledge with residual risk from older implicit stabilizer literature.
