# Independent Audit — 2026/09/18/multiset-dimension-three-cylinders-mod-four--18703d594a7d

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `41a7b90bc64d2a6420ec06dd148565550a3c331f`
- Disposition: **PASSED**

## Correctness

**PASS** — The normalized-cycle collision calculation and cylinder lift criterion are correct. With all three landmarks in row zero, a cylinder code is s_a(x)+i(1,1,1), so two vertices can collide exactly when their normalized cycle codes h_a agree and the difference of minima can be canceled by a row offset of magnitude at most m-1. The piecewise-affine cycle analysis yields translation separation tau=a/2 for even a and tau=min(a,(L-a)/2) for odd a; maximizing over admissible a gives floor(L/3), attained by the submitted odd choices according to L mod 6. Thus n=2L>=6m and n=2 mod 4 imply tau>=m and a 3-vertex multiset-resolving set. The lower bound md>=3 follows from the standard facts that no connected graph has multiset dimension 2 and only paths have dimension 1. A fresh exhaustive check reproduced tau=floor(L/3) for all odd L below 80 and direct cylinder-code injectivity for m=3,...,14 over a band above n=6m.

## Originality

**PASS** — Marcelo-Tolentino-Garciano-Buot prove md(P_m square C_n)=3 under the stronger n>=8m+1 condition. The audited result gives an exact collision-capacity theorem for the antipodal boundary family and uses it to lower the coefficient to 6 on the infinite congruence class n=2 mod 4. The 2026 survey confirms that multiset dimension of graph products remains an active structural topic. The exact floor(L/3) capacity and the n>=6m congruence-family theorem are not statements of the 2025 source, and targeted searches found no earlier covering result.

## Scientific value

**PASS** — The theorem closes an infinite strip of cases left outside the best published 3-landmark sufficient range and explains the improved constant by an exact boundary-landmark capacity calculation rather than by isolated examples. The collision lemma is reusable for optimizing other cylindrical landmark configurations, while the result leaves clearly defined remaining congruence classes and the sub-6m region.

## Sources

- On multiset dimension of cylindrical graphs (R. M. Marcelo; M. A. C. Tolentino; A. D. Garciano; J. C. Buot): https://doi.org/10.61091/jcmcc126-15 — Open-access 2025 source; proves multiset dimension 3 for m>=3 and n>=8m+1.
- Multiset resolvability parameters in graphs: A survey with new results and open problems (Mohammad Farhan; Sandi Klavžar; Dorota Kuziak; Ismael G. Yero): https://arxiv.org/abs/2607.10311 — Current survey of multiset dimension and related graph-product/open problems.
- The multiset dimension of graphs (R. Simanjuntak; T. Vetrík; P. B. Mulia): https://arxiv.org/abs/1711.00225 — Foundational multiset-dimension results, including the dimension-one/two facts used for the lower bound.

## Limitations

- The theorem covers only n congruent to 2 mod 4 with n>=6m and m>=3.
- The coefficient 6 is sharp only for the analyzed antipodal boundary family, not for arbitrary 3-landmark configurations.
- It does not settle the other congruence classes or the region n<6m.
- The proof is analytic; finite computation is only an independent consistency check.

## Independent exact check

```json
{
  "implementation": "fresh cycle-code collision census and direct lifted-cylinder injectivity test",
  "cycle_range": "all odd 9<=L<80 using the theorem's optimal a",
  "cylinder_range": "3<=m<=14 and admissible n in [6m,6m+40)",
  "all_ok": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first; no needed source remained inaccessible, so Oxford Download was not required.
