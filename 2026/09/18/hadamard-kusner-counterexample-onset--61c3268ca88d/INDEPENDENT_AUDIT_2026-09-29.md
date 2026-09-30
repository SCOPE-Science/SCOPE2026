# Independent Audit — Hadamard-order amplification and onset bounds for Kusner counterexamples

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `3ede89fc6e15be6b6b982ac941ec7be1281ba827`  
**Audited current source tree:** `3ede89fc6e15be6b6b982ac941ec7be1281ba827`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree is unchanged from the dispatcher-audited source tree. GitHub was used read-only as evidence; this audit file is staged by the ledger change-set and is not claimed to be already published.

## Correctness — PASSED

PASS. Xiong's pairwise distance count uses only Hadamard row orthogonality together with a normalized distinguished column, not the full Walsh group law. Replacing the Sylvester matrix of order m by an arbitrary real Hadamard H and using K_4⊗H therefore preserves the four pair types and the common distance after the same scalar equations. If m>1/Delta(p), continuity supplies the required a. The derivative expansion at p=4 gives c_4=sqrt(2) log(1+sqrt(2))-(7/4)log 2≈0.0334429143, so density of Hadamard orders yields the stated 8/c_4·epsilon^{-1} upper scale. The large-p expansion Delta(p)=2(log 2)^2/(3p)+O(p^{-2}) also checks. The Swanepoel stability inequality yields the stated lower scale near p=4.

## Originality — PASSED

PASS, narrowly scoped. Xiong's September 2026 construction explicitly selects a Sylvester/Walsh order m=2^k and proves existence for sufficiently large m. The asymptotic density of general Hadamard orders is classical, and Swanepoel--Villa previously exploited it in other equilateral-set regimes; those facts are not new. The submitted contribution is the verified transfer of Xiong's new p>4 construction to arbitrary Hadamard orders and the resulting explicit onset asymptotics/constants. Targeted searches did not locate that transfer in the source or contemporaneous follow-up work.

## Scientific value — PASSED

PASS. The theorem removes an artificial power-of-two sparsity from a newly discovered counterexample construction and converts its qualitative 'sufficiently large dimension' conclusion into explicit asymptotic onset bounds near p=4 and for large p. The bounds are not claimed optimal, but they materially quantify the transition.

## Independent checks

- Reconstructed the four pair types using an arbitrary normalized Hadamard matrix and K_4 tensoring.
- Numerically solved the construction at p=5, m=64 and checked all 512 points in dimension 510 have a common p-th-power distance to numerical precision.
- Recomputed c_4 and the near-p=4 Delta expansion numerically at several small epsilons.
- Recomputed the large-p limit p·Delta(p) and matched 2(log 2)^2/3.
- Checked the Hadamard-order density input and Swanepoel's p=4 stability inequality against the cited sources.
- Verified no file under this assigned record changed between the dispatcher source-check commit and current audited main.

## Limitations

- The near-p=4 upper and lower bounds retain a logarithmic gap.
- The constants describe this Hadamard-amplified construction and are not asserted to be optimal for the true minimum counterexample dimension.
- The motivating all-p>4 work is very recent, so simultaneous unindexed work is a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.14794
- https://doi.org/10.1007/s00454-013-9523-z
- https://doi.org/10.4153/CMB-2013-031-0
- https://arxiv.org/abs/2608.14013
- https://arxiv.org/abs/2606.03987
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/hadamard-kusner-counterexample-onset--61c3268ca88d

This change set updates only the independent-audit channel. Lean verification and expert attestation are preserved exactly as previously recorded.
