# Independent audit — 2026-09-29

Record: `2026/09/19/all-q-talagrand-cotype-compact-c0-separator--4b0e1a869da9`  
Assigned and audited source tree: `85de6d666900a8bb4c81a527d0981a551eb792e0`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `ab3dbed347ee0e04fac12a681d14b22cf1d5c7d0`  
Disposition: **passed**

## Correctness

**independently_supported**. The all-q extrapolation and compact gluing are correct. Wu's q=2 Walsh-Hadamard estimates imply the Rademacher lower bound for every q by testing the standard basis. For Gaussian cotype, ||a||_q<=||a||_2^(2/q)||a||_infinity^(1-2/q), the verified q=2 estimate, and the Gaussian norming-functional bound give C_q^g(U_n) of order (n/log n)^(1/q). Wu's matrix inequalities u_i<=alpha and sum u_i^2<=sqrt(n) alpha beta yield sum u_i^q<=alpha^(q-2)sum u_i^2 and hence the displayed (q,1)-summing bound. The latter is eventually smaller than the Gaussian scale uniformly in q after taking q-th powers, so the ratio grows at least as (log n)^(1/q). In the c0 direct sum, the inequality sum_i sup_k a_ik^q <= sum_k sum_i a_ik^q makes both positive ideals q-summable across weighted blocks, while restriction to one block forces unbounded Rademacher cotype. The block weights tend to zero, so the operator is a norm limit of finite-rank truncations and is compact.

## Originality

**supported_narrow_extension**. Wu's September 17, 2026 preprint explicitly announces and proves the counterexample at q=2. The public source does not state the fixed-q>2 interpolation, the explicit all-q (q,1) estimate, or the compact c0-subspace separator. Current searches found no public source covering those extensions. The direct-sum device and sequence-space interpolation are standard, so novelty is confined to recognizing and proving that Wu's concrete family separates the three quantities for every fixed finite q and to packaging this as a compact qualitative separator.

## Scientific value

**meaningful_strengthening**. The result shows that the negative phenomenon is not an endpoint artifact: every finite cotype exponent fails separately, with a quantitative logarithmic gap. The compact operator version is a useful operator-ideal separation adjacent to the positive Banach-lattice/C(K) theory.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/all-q-talagrand-cotype-compact-c0-separator--4b0e1a869da9
- https://arxiv.org/abs/2609.19731
- https://michel.talagrand.net/ULBSPRINGER.pdf
- https://arxiv.org/abs/math/9302206
- https://doi.org/10.1007/BF01231344
## Limitations

- The theorem treats real spaces and each fixed finite q separately.
- It does not determine the optimal finite-dimensional separation rate or produce one compact operator working simultaneously for all q.
- The c0-sum domain is only a closed subspace of c0; no Banach-lattice or complementability claim is made.
- The extension is mathematically short once Wu's q=2 estimates are available, and the priority window is only days wide.
