# Independent Audit — A growing block of traced Rankin--Cohen brackets is linearly independent

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `654bb12a49cc5c5e30871d3d6b921264884178d2`  
**Audited current source tree:** `654bb12a49cc5c5e30871d3d6b921264884178d2`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree is unchanged from the dispatcher-audited source tree. GitHub was used read-only as evidence; this audit file is staged by the ledger change-set and is not claimed to be already published.

## Correctness — PASSED

PASS. The submitted uniformization of Takloo-Bighash's explicit Fourier-coefficient estimate is consistent. With P=p_r=O_D(r log(2r)), the hypothesis r log(2r)=o(sqrt(ℓ)) gives P^2=o(ℓ); Stirling applied to the published coefficient error makes its logarithm dominated by -ℓ log(ℓ/P^2), which overwhelms the exp(O(r^2 log P)) determinant losses. The Vandermonde cofactor ratios are bounded by P^(2r), while the penultimate-prime contribution is exponentially smaller than the p_r^(ℓ-1) term because ℓ/(Pr log P)→∞. Restoring the coefficient errors via a telescoping determinant expansion and Hadamard bounds remains negligible. The exact cofactor identities in the artifact were independently checked algebraically.

## Originality — PASSED

PASS. Takloo-Bighash's 2026 theorem keeps the initial block length r fixed, while Kayath--Lane--Neifeld--Ni--Xue formulate a much larger conjectural independent family. The submitted result is a genuine quantitative intermediate theorem: r may tend to infinity subject to r log(2r)=o(sqrt(ℓ)). The audit does not treat the coefficient formula, the Petersson framework, or Vandermonde algebra as new; originality is in obtaining uniform control for a growing block.

## Scientific value — PASSED

PASS. A growing independent block gives a new quantitative lower bound for the explicit Rankin--Cohen family and advances the fixed-r result toward the conjectural linear-size regime. The range is far from optimal and does not improve every special-case nonvanishing count, but it is a nontrivial asymptotic strengthening rather than a finite computation.

## Independent checks

- Read the explicit coefficient bound in the open preprint and verified the dependence on e, p_j, and ℓ used in the uniform estimate.
- Re-derived the dominance of -ℓ log(ℓ/P^2) over r^2 log P under r log(2r)=o(sqrt(ℓ)).
- Re-derived the Vandermonde cofactor ratios and the exponential suppression of j<r prime terms.
- Checked the included exact determinant-identity script/output for r=2 through 8 as supplementary evidence.
- Compared the theorem with Takloo-Bighash's fixed-r statement and the Kayath--Lane--Neifeld--Ni--Xue basis conjecture.
- Verified no file under this assigned record changed between the dispatcher source-check commit and current audited main.

## Limitations

- The discriminant D is fixed; no growing-D uniformity is established.
- The condition r log(2r)=o(sqrt(ℓ)) is sufficient, not claimed optimal, and remains far below the conjectural linear-size block.
- For D=1, stronger counting lower bounds for nonvanishing eigenforms are known; the validated contribution is the growing explicit Rankin--Cohen block.

## Evidence and references

- https://arxiv.org/abs/2609.19649
- https://doi.org/10.4153/S0008414X25101697
- https://doi.org/10.1017/nmj.2026.10099
- https://doi.org/10.1090/proc/13572
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/growing-rankin-cohen-independence--b4aacb190052

This change set updates only the independent-audit channel. Lean verification and expert attestation are preserved exactly as previously recorded.
