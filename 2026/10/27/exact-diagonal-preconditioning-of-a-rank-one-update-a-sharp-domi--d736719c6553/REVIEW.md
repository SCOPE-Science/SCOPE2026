# Mathematical review: exact rank-one diagonal preconditioning

## Correctness — PASS

The statement optimizes the generalized spectral ratio of \(A=I+uu^{\mathsf T}\) over **every** strictly positive diagonal \(P\), not merely over symmetric or equal-coordinate choices. For \(M\le S/2\), a closed-polygon Gram matrix \(H\succeq0\) has \(AH=H\) and diagonal \(u_i^2/S\). The same weighted trace occurs in upper and lower generalized-Rayleigh tests, proving \(\kappa(P)\ge1+S\). For a dominating coordinate, restriction to its span with the remaining part of \(u\) gives an unavoidable two-dimensional correlation bound; a diagonal matrix altering only that coordinate attains the bound because all remaining eigenvalues are one. The zero-vector, single-support and transition boundaries are handled explicitly. Actual supplementary checker output records 145 value/eigenvalue comparisons, 5,800 asymmetric competing scalings, 23 separate numerical optimizations, and three exact symbolic tests. All infinite quantifiers rest on the written proof, not sample coverage.

## Originality — PASS, with residual historical risk

Braatz and Morari (1994) establish a general condition-number-scaling framework, and Takapoui and Javadi (2016) discuss diagonal equilibration and its possible failure to improve conditioning. The general algorithms of Qu et al. (2022) can optimize such problems numerically. The new statement is an explicit dimension-independent optimum for **every** real rank-one vector, including the polygonal \(M\le S/2\) no-scaling criterion and an optimal one-coordinate factor when one squared coordinate dominates. Those conclusions are not explicitly established in the inspected full texts. The two-by-two balancing step is standard and is not itself claimed as novel. Full-text comparison with Kolotilina (2002), and Shapiro (1985), was not possible; specialized or implied prior coverage remains a genuine risk, and no absolute novelty claim is made.

## Mathematical value — PASS

A natural family of rank-one/spiked SPD Hessians arises in linear algebra and iterative linear solving. The theorem gives a closed-form global answer to a nonsymmetric, \(n\)-parameter diagonal condition-number-design problem, a structural test for when doing nothing is optimal, and a constructive single-entry optimum otherwise. The explicit \(u=(1/2,1,1,1)\) example shows that conventional Jacobi normalization can worsen the objective even when the identity is globally best. The result is useful as an exact test case and as a condition-number design principle; its significance does not depend on an unproved downstream runtime gain.

## Closest literature and limitations

- R. D. Braatz and M. Morari (1994), *Minimizing the Euclidean Condition Number*, full accessible paper. General formulation rather than the rank-one closed form.
- R. Takapoui and H. Javadi (2016), *Preconditioning via Diagonal Scaling*, arXiv:1610.03871v1, full HTML read. General equilibration and caution about conditioning.
- Z. Qu et al. (2022), *Optimal Diagonal Preconditioning*, arXiv:2209.00809, accessible full text read. General optimum via SDP, not this explicit formula.
- L. Yu. Kolotilina (2002), *Optimally Conditioned Block Matrices*, abstract available; full text unavailable for decisive specialized comparison.
- A. Shapiro (1985), *Optimal Block Diagonal \(\ell_2\)-Scaling of Matrices*, abstract consulted; specialized implications cannot be fully excluded.

The proof applies only to symmetric positive diagonal preconditioners for \(I+uu^{\mathsf T}\), and no optimizer uniqueness is asserted. Independent mathematical replication and independent literature audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
