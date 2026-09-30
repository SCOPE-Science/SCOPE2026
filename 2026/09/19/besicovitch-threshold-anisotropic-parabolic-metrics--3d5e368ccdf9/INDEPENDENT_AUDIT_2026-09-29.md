# Independent Audit — 2026/09/19/besicovitch-threshold-anisotropic-parabolic-metrics--3d5e368ccdf9

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `89e348058f5a0cb15a972b2e449661b577f0a1a1`
- Disposition: **PASSED**

## Correctness

**PASS** — The threshold proof is consistent. For p>=a>=2, q=p/a>=1 and the three geometric estimates used in the parabolic Besicovitch selection argument remain valid: the cone estimate forces geometric growth of the time coordinates, the bounded-space/large-time case is ruled out by convexity u^q-v^q>=u^{q-1}(u-v), and the bounded-time/large-space case uses p>=2 together with q<=p/2. The constants can be chosen from a and n only. Homogeneous volume growth r^{n+a} supplies the scale-bin packing step, so the standard greedy argument yields strong BCP uniformly in p>=a. For p<a, q<1; the explicit rapidly increasing family uses concavity to put the origin in every ball and the recursive spatial offset to keep every center outside every other ball, giving an infinite Besicovitch family and failure of weak BCP. The boundary p=a is correctly included in the positive regime.

## Originality

**PASS** — Dobronravov's September 2026 theorem gives the exact threshold p=2 for the standard parabolic anisotropy a=2. Le Donne-Rigot classify which graded groups admit some homogeneous distance with BCP but emphasize metric sensitivity; their theorem does not classify this explicit two-parameter distance family. Targeted searches for anisotropic/snowflaked product metrics and a p=a threshold did not locate a higher-anisotropy theorem. The audited result is thus a genuine extension of the very recent parabolic argument to all a>=2, with the additional uniform-in-p conclusion.

## Scientific value

**PASS** — The theorem identifies the exact interaction between the Lp exponent and anisotropic time snowflaking, showing that the covering transition tracks p=a rather than the fixed Euclidean value 2. It extends a newly solved parabolic covering problem to a natural higher-anisotropy family and supplies uniform constants in the positive range. This is useful for differentiation and geometric-measure arguments built on such anisotropic metrics.

## Sources

- Besicovitch's covering theorem in the parabolic metric (Nikita Dobronravov): https://arxiv.org/abs/2609.15560 — Primary 2026 source proving BCP for the a=2 metric exactly when p>=2.
- Besicovitch Covering Property on graded groups and applications to measure differentiation (Enrico Le Donne; Séverine Rigot): https://arxiv.org/abs/1512.04936 — General graded-group existence/classification background; it does not give the explicit p-versus-a threshold for this metric family.

## Limitations

- The proof and theorem are restricted to a>=2; the intermediate regime 1<a<2 is explicitly open.
- The max metric p=infinity is not covered and no optimal numerical Besicovitch constant is claimed.
- The positive proof adapts the recent a=2 selection geometry; originality is therefore in the exact higher-anisotropy classification, not the general Besicovitch method.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "positive_inequalities_checked": true,
  "negative_concavity_construction_checked": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence; no repository write was performed. Open-access and preprint sources were checked first. No current assigned record required Oxford Download.
