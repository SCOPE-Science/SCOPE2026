# Independent mathematical audit

## correctness

PASS

At normalized counting measure, convolution by D_m/N has both endpoint norms equal N^{-1} Σ_{j=0}^{N−1}|D_m(j/N)|; ℓ∞ phase alignment and ℓ1 normalized point mass attain Young bounds. The sine quotient R_m(x)=sin(mπx)/sin(πx) changes sign only at x=k/m, with sign (−1)^k on (k/m,(k+1)/m); b_k=floor(kN/m) partitions j=1..N. The j=0 term |D_m(0)|=m equals |R_m(1)|, making telescoping exact even on zero-aligned meshes and at m=N. For m odd, R_m=1+2Σ_{r≤(m−1)/2} cos(2rπx); for even, R_m=2Σ_{r≤m/2} cos((2r−1)πx). Their geometric progression sums give exactly the stated A_{m,N}(M), including M=0,N. F_m=|R_m| is periodic C^0, smooth at 0=1, and has derivative jump J_k=2mπ csc(πk/m) at k/m; distributional twice integration gives \hat F_m(n)=−(ΣJ_k e^{−2π i n k/m})/(4π²n²)+O_m(n^{-3}). Fourier aliasing and Σ_{ℓ≠0}e^{2πiℓt}/ℓ²=2π²B2({t}) yield the exact residue-class 1/N² correction and O_m(N^{-3}). Independent 65-digit high-precision checks matched 861 finite m≤N≤42 pairs to better than 2e−64 and tested 44 residue cases for 2≤m≤9 around N=750; such finite checks corroborate rather than prove the universal identities.

## originality

PASS

The all-m,N finite formula is not stated or implied by the inspected m=3/m=4 exact results or the concentration papers. The Bernoulli jump expansion is NOT independently novel: Berrut–Trummer 2022 Theorem 2 explicitly covers its general analytic mechanism, and elementary specialization yields the proposed coefficient. The originality judgment rests on the complete exact all-block finite norm evaluation and organized sampling law together, not on claiming a new Euler–Maclaurin principle. Residual risk: a classic finite cyclic Lebesgue-constant formula may already contain the all-m sign-block identity.

## value

PASS

Endpoint operator norms of Fourier partial-sum projections on cyclic groups are canonical discrete Lebesgue constants. The exact all-m,N expression removes absolute values and replaces N sample terms by O(m²) finite-trigonometric arithmetic for each m, including complete zero-aligned arithmetic edge cases; a researcher seeking precise amplification on finite cyclic grids can use this fact directly. The residue formula explicitly quantifies nonmonotone sampling error for every fixed block and reveals sign changes (including the known m=4 special case). Although the B2 jump law is a standard consequence of generalized Euler–Maclaurin and the proof uses elementary trig, the combined exact symbolic family is a naturally motivated invariant rather than a one-off tiny parameter calculation. No claims for nonconsecutive spectra, interior ℓp norms, or m-dependent uniform error bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
