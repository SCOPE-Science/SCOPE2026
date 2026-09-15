# Threshold ternary Hamming graph H(3,3,2): classical number 7, quantum interval {5,6}, and a covariant no-go theorem

## Context

The admitted target asks for the exact finite-dimensional tensor-product quantum chromatic number `chi_q(H(n,q,d))` of the q-ary Hamming graph at threshold distance `d=(q-1)n/q`, known to lie in `[(q-1)n-q+2,(q-1)n]`. The smallest member is `H(3,3,2)`: vertex set `Z_3^3` (27 vertices), adjacent iff Hamming distance exactly 2, with target interval `[5,6]`. This record reports everything rigorously provable about that endpoint this pass, leaving the residual `5`-vs-`6` quantum decision open.

## Definitions

- `H(3,3,2)`: vertices `Z_3^3`, `x ~ y` iff `d_H(x,y)=2`. It is 12-regular with 162 edges and vertex-transitive.
- `chi`: classical chromatic number. `omega`, `alpha`: clique and independence numbers.
- `chi_q`: finite-dimensional tensor-product (synchronous, projective) quantum chromatic number, not `chi_qa`/`chi_qc`.

## Result

1. **Classical number.** `chi(H(3,3,2)) = 7`: 6-coloring is infeasible (exact branch-and-bound ILP) and an explicit proper 7-coloring exists (stored, machine-verified, zero conflicts).
2. **Quantum bounds.** `5 <= chi_q(H(3,3,2)) <= 6`: the Krawtchouk spectrum is exactly `{12^1, 0^6, (-3)^12, 3^8}`, so the Elphick-Wocjan quantum Hoffman bound gives `chi_q >= 1-12/(-3) = 5`; an explicit 6-outcome PVM in dimension 6 gives `chi_q <= 6`.
3. **Quantum advantage.** `chi_q <= 6 < 7 = chi`: strict separation on this named 27-vertex graph.
4. **Extremal structure.** `omega = alpha = 4`, with a 4-clique and a 4-independent-set witness, each proved optimal by exact ILP; exhaustive `C(27,5)` enumeration independently confirms no 5-clique and no 5-independent set.
5. **Covariant no-go.** No translation-covariant rank-1 5-coloring in dimension 5 exists for any choice of 5 characters. This eliminates the natural symmetric class only, not all 5-colorings. Symmetric level-1 NPA reduces to the Delsarte LP with optimum 5.4 (`27/5.4 = 5.0`), so level 1 provably cannot separate 5 from 6.

## Proof / evidence

- **Graph and spectrum:** direct enumeration gives 27 vertices and 162 edges; `K_2(x) = 4*C(3-x,2) - 2x(3-x) + C(x,2)` yields eigenvalues `12, 0, -3, 3` with the stated multiplicities; shell character sums `K(w)` over the 12-point weight-2 shell take values `12, 0, -3, +3` by weight `0, 1, 2, 3` (recomputed).
- **chi >= 7:** `alpha = 4` gives `chi >= 27/4 = 6.75`, i.e. `>= 7`; equivalently the exact 6-color ILP infeasibility certificate.
- **chi <= 7:** the stored coloring in `output/artifacts/coloring7.json` was rechecked edge-by-edge with zero conflicts.
- **chi_q >= 5:** quantum Hoffman bound from the exact spectrum above.
- **chi_q <= 6:** with `omega = e^{2pi i/3}`, `F` the 2x2 Fourier matrix, `U_a = diag(omega^a, omega^{2a}) F`, colors `(k,s)` in `[3]x[2]`, vectors `v^x_{k,s} = 3^{-1/2} sum_j omega^{jk} e_j otimes u_{x_j,s}` form a per-vertex orthonormal basis (Fourier orthogonality) and same-color edge overlaps equal `(1/3)[(3-d)-d/2] = 0` at `d = 2` since `diag(U_a^* U_b) = -1/2` for `a != b`; re-verified to ~3e-16.
- **omega = alpha = 4:** witnesses `{(0,0,1),(0,1,0),(1,0,0),(1,1,1)}` (clique) and `{(0,2,2),(1,2,2),(2,0,0),(2,0,1)}` (independent set), pairwise verified; optimality by exact CBC branch-and-bound ILP plus independent exhaustive 5-set enumeration.
- **No-go:** a covariant strategy gives row Fourier transforms vanishing on the weight-2 shell; summing rows forces `C(z) = sum_{j in J} chi_j(z)` to vanish there, and `0 = sum_z |C(z)|^2 = 60 + sum_{j!=k} K(j-k)` forces all 20 ordered differences to have `K = -3` (weight 2), i.e. `J` is a 5-clique in the graph itself, contradicting `omega = 4`. An exhaustive LP scan over all `C(26,4) = 14950` translation-inequivalent character 5-sets independently confirms infeasibility.
- **Non-proof evidence (excluded from claims):** Stiefel-manifold descents stall for complete 5-colorings while converging for 6-colorings, favoring `chi_q = 6` as conjecture only; a buggy L-BFGS variant was excluded.

## Limitations

The full infinite-family target (exact `chi_q` for all `q >= 3` and multiples `n` of `q`) is not proved; even for `H(3,3,2)` the residual `5`-vs-`6` decision remains open. The no-go covers only translation-covariant rank-1 dimension-5 strategies. ILP optimality rests on exact branch-and-bound runs rather than hand proofs.

## Reproducibility

Run `python3 output/artifacts/verify_all.py` (with `output/artifacts/` as working data; needs numpy/pulp/scipy for the ILP steps). Certificates: `output/artifacts/coloring7.json`, `output/artifacts/spectra.json`. The audit independently re-verified the graph size, coloring, spectrum, quantum construction overlaps, witnesses, character sums, and exhaustive 5-set optimality checks.

## References

- Cao, Feng, Huang, Yang, Zhang, On the quantum chromatic number of Hamming and generalized Hadamard graphs, arXiv:2510.14209 (threshold interval `[(q-1)n-q+2,(q-1)n]`; no `(3,3,2)` classical or no-go claim).
- Luo, Ning, Zhang, Quantum Chromatic Number of Subgraphs of Orthogonality Graphs and the Distance-2 Hamming Graph, arXiv:2512.01195 (binary distance-2 graphs; `chi_q(O_{3l,3}) = 3l`; different object).
- Cao, Feng, Tan, Quantum chromatic numbers of some graphs in Hamming schemes, arXiv:2412.09904 (binary/Hadamard families; no ternary threshold package).
