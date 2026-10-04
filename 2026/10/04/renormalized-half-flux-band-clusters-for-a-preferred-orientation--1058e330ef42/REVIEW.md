# Same-model scientific review

## Correctness
PASS. The claim uses the exact half-flux dispersion inequality from arXiv:2302.04601. Re-expansion in the scaled variable \(x=N_n(k-N_n)\) was reconstructed independently, the four limiting roots are simple, and the conversion from momentum to energy was checked explicitly. The accompanying verifier solves the exact edge equations and confirms the predicted \(N_n^{-4}\) residual scale for the displayed two-term energy expansions. The proof distinguishes the narrow local pair from the wide band family and limits the claim to a fixed energy window where that separation holds for large \(n\).

## Originality
PASS. The motivating paper states the asymptotic width of each narrow band and the gap between them, but not the four absolute translated edge locations, the local Hausdorff limit, or the asymmetric first corrections of those edges. Searches for the half-flux preferred-orientation square lattice, renormalized band edges, the interval pair \([-2\sqrt2,-2]\cup[2,2\sqrt2]\), and arXiv:2302.04601 edge offsets did not locate an equivalent statement. published-finding corpus searches likewise returned no matching finding. The closest retrieved mathematical-physics result concerned a mosaic almost-Mathieu no-point-spectrum window and does not imply the present local band-edge asymptotics.

## Value
PASS. The source emphasizes that the narrow bands shrink on the momentum scale and have asymptotically constant widths on the energy scale. Resolving the complete fixed-energy local profile identifies where those bands sit relative to the natural centers \((n\pi)^2\), not only how wide they are. The explicit edge corrections also quantify the left-right asymmetry at finite energy. This is a natural spectral refinement of the source's high-energy analysis rather than an arbitrary parameter slice.

Closest literature and limitations are detailed in `AUDIT.json` and `RESULT.md`. The finding is restricted to the half-flux case and does not assert an analogous local limit for general rational flux.

Same-model review: passed. Independent audit: not yet performed.
