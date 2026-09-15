# Six-level two-sided Ramanujan 2-lift tower from K8 (7-regular)

## Context

Degree 7 is the smallest degree not covered by the classical explicit Ramanujan constructions: Lubotzky–Phillips–Sarnak, Margulis, and Morgenstern require `d - 1` to be a prime power, and `6` is not one. Marcus–Spielman–Srivastava and followers give one-sided or bipartite control; the two-sided Bilu–Linial signing conjecture remains open. The admitted target asked for an infinite two-sided 7-regular Ramanujan tower by iterated 2-lifts from `K8`. That infinite claim is blocked. This record reports the strongest certified finite prefix obtained while pursuing it.

## Definitions

Let `G` be `d`-regular with adjacency eigenvalues `d = λ1 ≥ λ2 ≥ ... ≥ λn`. It is two-sided Ramanujan if `max(λ2, |λn|) ≤ 2√(d-1)`; for `d = 7` the bound is `2√6 ≈ 4.89897949`. An edge-signing `s : E(G) → {+1,-1}` defines a 2-lift `G̃` on `V × {0,1}`: a `+` edge lifts to parallel edges, a `−` edge lifts to crossed edges. Then `spec(G̃) = spec(G) ∪ spec(A_s)` where `A_s` is the signed adjacency matrix. Hence a Ramanujan `G` lifts to a Ramanujan `G̃` iff `ρ(A_s) ≤ 2√(d-1)`. The lift is connected iff the signing is unbalanced.

## Result

Starting from `G0 = K8` there is an explicit connected two-sided 7-regular Ramanujan tower `G0,...,G5` with `|V(Gi)| = 8·2^i` (8, 16, 32, 64, 128, 256). Each `G(i+1)` is a 2-lift of `Gi`, every `Gi` is connected and 7-regular, and every `Gi` is two-sided Ramanujan. Nontrivial spectral maxima are 1.0, 3.0, 3.62252, 3.87541, 4.24374, 4.53605, with margins to `2√6` of 3.899, 1.899, 1.276, 1.024, 0.655, 0.363. The first lift has exact new spectrum `{-3 (×3), -1, +1, +3 (×3)}`, i.e. signed characteristic polynomial `(x-3)^3 (x-1)(x+1)(x+3)^3` with spectral radius exactly 3.

## Proof / evidence

Machine certificate. `edges_Gi.json` fix each graph; `signing_G{i}_to_G{i+1}.json` fix each signing; `spectrum_Gi.txt` give full sorted spectra. Independent audit rebuilt every lift from `(base edges, signing)` by the Bilu–Linial recipe and confirmed exact edge-set equality at all five steps, 7-regularity, BFS connectivity, and spectra by dense symmetric eigensolvers; smallest margin 0.363 is far above roundoff (~1e-12). The `G0 → G1` signing was additionally verified with exact integer arithmetic (sympy characteristic polynomial), factoring exactly as `(x-3)^3(x-1)(x+1)(x+3)^3`. All graphs are non-bipartite, so `-7` is not forced. The verifier recipe is: rebuild lift, check degrees, BFS connectivity, edge-count lift relation, eigenvalues.

## Limitations

Finite tower only (six levels, `n ≤ 256`), not the infinite target. Signings were found by heuristic search (random sampling plus simulated annealing), which carries no guarantee for level 6+. Margins shrink monotonically to 0.363, suggesting a later obstruction is plausible. Spectra beyond `G1` rely on double-precision eigensolvers. Originality rests on literature and database checks described in the audit, not on an exhaustive manual review of all unpublished signings.

## Reproducibility

Artifacts: edge lists, signings, spectra, `chain_certificate.json`, and `verify_g1_exact.py` are packaged in `output/artifacts/`. Rebuild each lift from `(edges, signing)`, verify degrees, connectivity, lift edge counts, and run a dense symmetric eigensolver; verify the `G0 → G1` polynomial with exact integer arithmetic.

## References

Morgenstern, q+1-regular Ramanujan graphs (prime-power condition, excludes d=7); Marcus–Spielman–Srivastava / Cohen one-sided bipartite lifts; Bilu–Linial 2-lift spectrum-union mechanism; Mohanty–O'Donnell–Paredes explicit near-Ramanujan graphs (eps-approximate d=7 family; exact d=7 infinite family unknown); Zenodo dataset Ramanujan graphs degree 3–7 (7-regular census to 14 vertices).
