# Independent Audit — A sharp ordinary-modulus median bound for two-summand expansive decompositions

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `3f8fdd207168a0637731245aacdf0fc4deb17cff`  
**Audited current source tree:** `3f8fdd207168a0637731245aacdf0fc4deb17cff`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path is unchanged from the dispatcher's source-check commit, so the audited tree equals the assigned source tree. GitHub was used only as read-only evidence. The UTC-dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. Let c=lambda_k(Q), E be the spectral subspace for eigenvalues lambda_k,...,lambda_d of Q=sum_j |X_j|, and F=E^perp. Under d>=m(k-1)+1, the intersection of the kernels of P_F|X_j||_E for j=1,...,m-1 is nonzero. For a unit x in that intersection, P_F Q P_E=0 forces the m-th leakage to vanish too, so every |X_j|x lies in E. With C_j=P_E|X_j||_E, one has 0<=C_j<=sum C_j=Q|_E<=cI and therefore C_j^2<=cC_j. Hence sum_j ||X_jx||^2<=c<Qx,x><=c^2. Expansivity gives 1<=||sum_j X_jx||^2<=m sum_j||X_jx||^2, proving c>=1/sqrt(m). For m=2 this gives the stated median bound. I independently evaluated the submitted 3x3 sharp family at t=10,100,1000; lambda_2(|A_t|+|B_t|) is approximately 0.740716, 0.710625, 0.707460 and converges to 1/sqrt(2), while the theorem supplies the matching lower bound. The direct-sum filler argument correctly propagates sharpness to all claimed odd dimensions and even dimensions >=6.

## Originality — PASSED

PASS, narrowly scoped. Bourin--Lee study triangle inequalities for the symmetric modulus and Zhang gives counterexamples/sharp inequalities in that line; Aouichaoui--Lee's September 2026 paper addresses related open matrix-analysis questions and exhibits loss of positive lower bounds for three ordinary-modulus summands. Targeted searches did not locate the submitted two-summand ordinary-modulus threshold lambda_n(|A|+|B|)>=1/sqrt(2), the general dimension-leakage criterion d>=m(k-1)+1, or the sharp families. Standard spectral-subspace arguments, compression inequalities, interlacing and direct sums are prior methods and receive no novelty credit.

## Scientific value — PASSED

PASS. The theorem gives a sharp positive median constant in the two-summand ordinary-modulus problem precisely where the recent three-summand construction shows that no positive constant can survive at the first critical dimension. The general d,m,k leakage criterion also explains the dimension threshold structurally. The unresolved 4x4 median case and lack of a universal sharpness statement for all (d,m,k) are appropriately left open.

## Independent checks

- Reconstructed the leakage-kernel dimension argument and verified every inequality in the proof.
- Numerically recomputed the 3x3 sharp family; lambda_2 tends to 1/sqrt(2) from above.
- Checked the 2x2 filler eigenvalues s+t and s-t and the direct-sum median counting for all claimed parity classes.
- Compared against public statements for Bourin--Lee arXiv:2602.19607, Zhang arXiv:2603.01046, and Aouichaoui--Lee arXiv:2609.20094; no covering two-summand theorem was located.
- Targeted searches for the exact 1/sqrt(2) median and d>=m(k-1)+1 formulas found no prior statement.
- Verified via GitHub compare that the assigned record path did not change from the dispatcher source-check commit to current main; the dated audit pair is absent and VERIFICATION.md retains blob SHA 31a3bb079c3be0cdcbee536377edadb1613bf629.

## Limitations

- The exact 4x4 two-summand median constant remains unresolved.
- The m^{-1/2} theorem is a sufficient dimension-regime result and is not claimed sharp for every admissible (d,m,k).
- Very recent matrix-analysis preprints leave some residual risk of simultaneous or differently phrased follow-up work.

## Evidence and references

- https://arxiv.org/abs/2609.20094
- https://arxiv.org/abs/2603.01046
- https://arxiv.org/abs/2602.19607
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/two-summand-expansive-modulus-median-bound--7e7587cf813c

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
