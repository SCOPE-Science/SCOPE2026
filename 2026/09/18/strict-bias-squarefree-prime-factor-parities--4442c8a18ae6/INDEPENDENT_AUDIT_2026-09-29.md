# Independent Audit — Strict bias for squarefree prime-factor parity vectors

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `39bc805573ad1eb7d8d3dc9e8799ea9ce9a7102c`  
**Audited current source tree:** `39bc805573ad1eb7d8d3dc9e8799ea9ce9a7102c`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence; this file is a guarded publication-plan payload and is not claimed to be already present in the repository.

## Correctness — PASSED

PASS. Tang's Fourier decomposition gives pole order z_r=1-2r/m for each Hamming-weight layer. The submitted grouping z_{r+m/2}=z_r-1 exhausts all possible integer resonances because 1<=r<m/2. The Euler products F_j are linearly independent: coefficients at products of one selected prime in each chosen residue class form the Walsh–Hadamard character table. Thus H_1 cannot vanish identically for a!=b. After assigning each nonzero H_r its finite vanishing order nu_r at s=1, the effective exponents beta_r=z_r-nu_r are pairwise distinct, so exactly one fractional family leads. Tang's Selberg–Delange framework then gives a nonzero pairwise asymptotic; the integer-order 0 and -1 layers have all algebraic coefficients killed by reciprocal-Gamma zeros. The coordinatewise monotonicity follows because H_1(1) is a positive sum of Tang's weight-one constants.

## Originality — PASSED

PASS. Tang's September 2026 paper proves equidistribution and the two extremal binary comparisons but explicitly leaves pairwise sign stabilization for every two distinct parity vectors as its strict-bias conjecture. A current public open-problem index repeats that exact unresolved statement. The submitted resonance grouping plus Walsh–Hadamard noncancellation argument addresses the missing cancellation issue and yields the full pairwise theorem; targeted searches did not locate a prior solution.

## Scientific value — PASSED

PASS. The theorem resolves the motivating paper's full binary strict-bias conjecture, not merely an additional extremal case, and strengthens it by quantizing every leading logarithmic exponent and proving a Boolean-lattice monotonicity law. The proof introduces a clean structural way to control resonant Selberg–Delange layers.

## Independent checks

- Checked the Fourier-character linear-independence argument coefficient by coefficient using Dirichlet's theorem to choose primes in each reduced residue class.
- Checked that all possible pole-order resonances are exactly the pairs r and r+m/2 plus the integer layers 0 and -1.
- Verified beta_r cannot coincide for distinct r because 0<2|r-r'|/m<1 whereas nu_r-nu_r' is an integer.
- Checked the leading Selberg–Delange coefficient after a vanishing order nu and the reciprocal-Gamma cancellation for nonpositive integer pole orders.
- Compared the conclusion with Tang's abstract and the current public statement of the strict-bias open problem, which says only all-zero/all-one extremal comparisons are proved in the source.
- Verified the assigned record path is unchanged from the dispatcher source-check commit to current main and that both dated independent-audit marker files are absent.

## Limitations

- The proof imports Tang's analytic continuation, zero-free-region, and Selberg–Delange estimates rather than reproving them.
- The theorem is the binary l_i<=2 case and does not resolve analogous higher-modulus races.
- The source conjecture is very recent, so simultaneous unindexed work remains a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.16716
- https://www.emergentmind.com/open-problems/strict-bias-binary-congruence-conditions
- https://arxiv.org/abs/1806.01585
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/strict-bias-squarefree-prime-factor-parities--4442c8a18ae6

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
