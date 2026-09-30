# Independent audit — Sharp anisotropy threshold for mixed-power parabolic balls

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/anisotropic-parabolic-besicovitch-threshold--51dd101ca283`
**Audited tree:** `331cb08d488989777fbe477e964a15bb9f78c0a9`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

The p<kappa obstruction and p>=kappa covering argument check out. For sigma=p/kappa<1, the explicit rapidly separated centers use concavity twice to put the origin in every ball and force every pair of centers outside one another's balls. For sigma>=1, the near-ray spatial deficit is valid for all p>=1; combined with convexity in time it yields the mixed, vertical, and horizontal finiteness lemmas. Homogeneous doubling/packing, angular caps, separated radius buckets, and greedy coloring then give strong BCP. The endpoint p=kappa is covered because all positive-side inequalities remain valid at sigma=1.

### Independent checks

- Verified the negative construction algebra: concavity gives t_j^sigma+sigma(t_j+1)^(sigma-1) <= (t_j+1)^sigma, while (1-u)^sigma>1-u plus the recursive spatial gap gives d(z_i,z_j)>r_j>r_i for i<j.
- Re-derived the near-ray bound (a-1)^p-|u-v|^p >= 2^{-(p+2)} a^{p-1} b from the cosine cap and the elementary power difference inequality.
- Checked the mixed lemma in both exclusion directions: forward exclusion forces t_{j+1}>2t_j-1 and geometric growth; reverse exclusion plus convexity contradicts the resulting exponential decay of a_j/t_j^{1/kappa}.
- Checked the vertical and horizontal lemmas and the endpoint sigma=1; the remaining greedy selection uses only homogeneous doubling, fixed-annulus packing, finitely many angular caps, and separated radius buckets.

## Originality

PASS to the best of current searchable knowledge. Dobronravov arXiv:2609.15560 proves exactly the kappa=2 metric and threshold p=2. Itoh treats a different max-type parabolic metric, and Aimar–Forzani use a common-power anisotropic quasi-ball family rather than the mixed powers p and p/kappa here. Fresh searches through 2026-09-29 found no arbitrary-kappa statement with threshold p=kappa.

### Literature checked

- https://arxiv.org/abs/2609.15560 — Dobronravov, Besicovitch's covering theorem in the parabolic metric; theorem is the kappa=2 specialization d_p=(|dx|^p+|dt|^{p/2})^{1/p} with threshold p>=2.
- https://doi.org/10.32917/hmj/1544238028 — Itoh (2018), Besicovitch covering theorem for parabolic balls; related fixed square-root/max-type parabolic geometry.
- https://doi.org/10.2307/44154122 — Aimar–Forzani, On the Besicovitch Property for Parabolic Balls; common-power anisotropic quasi-balls, not the present mixed-power family.
- https://arxiv.org/abs/1512.04936 — Le Donne–Rigot, structural BCP existence on graded groups; does not classify this explicit distance family.

## Scientific value

The theorem converts the isolated parabolic threshold p=2 into a sharp anisotropy law and identifies the transition with convexity of the temporal exponent p/kappa. It supplies both a constructive weak-BCP failure family below threshold and a positive strong-BCP theorem above threshold, so the contribution is more than a cosmetic reparameterization.

## Limitations

- The proof gives existence of a finite strong-Besicovitch constant, not an optimal constant.
- Only one anisotropic time coordinate and finite p are treated; p=infinity, multiple anisotropy exponents, p<1, and kappa<1 remain outside scope.
- The closest source is extremely recent, so unindexed simultaneous generalizations remain a residual originality risk.

## Publication guard

This audit is scoped to the exact source-tree SHA above. The guarded change-set adds this independent-audit evidence pair and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
