# Independent Audit — 2026/09/19/bezout-simplex-stability-via-rogers-shephard--c2c66439c4b3

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `d9fbd2ad05c80a8042abb13cc1fdd796f88a7652`
- Disposition: **PASSED**

## Correctness

**PASS** — The quantitative bridge is correct. From K_v^s+[0,sv] subset K, the restricted Bezout bound and projection formula give a mixed-volume inequality; the (n-1)-dimensional Minkowski inequality then yields P_s<=c_v^{n-1}P(1-Ps/(nV(K)))^{n-1}. Integrating the layer-cake identity V(K)=int_0^ell P_s ds gives the sharp directional lower bound q>=lambda_n(c). Integrating the same estimate from t to ell bounds the covariogram, and polar integration over the difference body together with n B(n+1,n)=binom(2n,n)^{-1} gives the stated Rogers-Shephard deficit Psi_n(c). Böröczky's published stability theorem then directly yields the Banach-Mazur estimate. The small-epsilon expansion and the explicit coarse epsilon^{1/n} bound are algebraically consistent; independent numerical checks in dimensions 2, 3 and 5 satisfy the displayed coarse modulus.

## Originality

**PASS** — Langharst-Wang's September 2026 result resolves the exact constant-one Bezout characterization and reports longest-chord and relative-inradius characterizations, but its public statement does not give a quantitative stability theorem. Böröczky's 2005 theorem gives Rogers-Shephard near-equality stability but contains no Bezout hypothesis. The audited record supplies the missing quantitative bridge from the restricted chord-intersection Bezout tests to a Rogers-Shephard deficit and hence to Banach-Mazur proximity. Targeted searches for a Bezout-to-Rogers-Shephard stability estimate found no prior covering theorem.

## Scientific value

**PASS** — The result turns a qualitative simplex characterization into an explicit stability theorem using only the special tests already sufficient for exact characterization. It provides directional chord bounds, a difference-body deficit and a Banach-Mazur modulus, thereby making the recent theorem robust under approximate inequalities. Even with nonoptimal constants, this is a meaningful quantitative strengthening.

## Sources

- The Bézout inequality for mixed volumes characterizes simplices (Dylan Langharst; Shouda Wang): https://arxiv.org/abs/2609.20380 — Primary 2026 exact characterization; its abstract notes longest-chord and relative-inradius characterizations but not quantitative Banach-Mazur stability.
- The stability of the Rogers-Shephard inequality and of some related inequalities (Károly Böröczky Jr.): https://users.renyi.hu/~carlos/rogerstab.pdf — Provides the explicit Rogers-Shephard deficit-to-Banach-Mazur stability bound used as the final step.
- Bezout Inequality for Mixed Volumes (Ivan Soprunov; Artem Zvavitch): https://doi.org/10.1093/imrn/rnv390 — Original mixed-volume Bezout conjecture background.

## Limitations

- The exponent and constants are not claimed optimal; the Banach-Mazur coefficient inherited from Böröczky is extremely large.
- The stability theorem concerns the restricted chord-intersection tests; the relative-inradius corollary uses the stronger full two-body constant.
- No quantitative converse from simplex proximity back to the restricted Bezout defect is proved beyond the displayed contrapositive.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "beta_identity_checked": true,
  "coarse_modulus_numeric_checks": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence; no repository write was performed. Open-access and preprint sources were checked first. No current assigned record required Oxford Download.
