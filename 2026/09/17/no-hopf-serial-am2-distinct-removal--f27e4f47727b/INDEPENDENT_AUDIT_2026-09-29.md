# Independent audit — 2026-09-29

**Record:** `2026/09/17/no-hopf-serial-am2-distinct-removal--f27e4f47727b`  
**Audited source tree:** `7277181471fa26b1947edd1bfbf234e62af5a2eb`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026@253a0fe5d0217455660a277f9adb940030e567ad`  
**Disposition:** PASSED

## Correctness

PASS. The serial feed-forward architecture makes the full Jacobian block lower triangular, so its spectrum is the union of four 2x2 diagonal-block spectra. For a positive-biomass first-reactor block, the equilibrium relation mu=alpha D gives tr=-D-k mu' x and det=k alpha D mu' x; thus det>0 forces tr<0, while tr=0 forces det<0. For a positive-biomass second-reactor block, the equilibrium balance gives r=x0/x in [0,1], delta=alpha D r and q=-k mu' x, hence tr=q-D-delta and det=D(delta-alpha q). I independently rederived these identities. If det>0 then q<Dr and tr<-D(1-r+alpha r)<=-alpha D<0; if tr=0 then det=alpha D^2((1-alpha)r-1)<=-alpha^2 D^2<0. Zero-biomass blocks are triangular with real eigenvalues. Therefore no diagonal block, and hence no equilibrium Jacobian, can have a nonzero purely imaginary pair. The claimed redundancy det>0 => tr<0 for the second-reactor stability block follows immediately.

## Originality

PASS, qualified. The source preprint explicitly retains a separate trace condition for the relevant coexistence equilibria and lists Hopf/limit-cycle identification as open. Searches for the exact serial-AM2 model and determinant/trace identity found no prior no-Hopf theorem. Earlier equal-removal or structurally different chemostat models do not supply this source-specific second-reactor identity. The ingredients are elementary; originality lies in closing the stated open local-stability/Hopf case for this eight-dimensional cascade.

## Scientific value

PASS. The theorem removes a spurious stability condition and rules out an entire local bifurcation mechanism across all equilibria of the stated model, directly simplifying the source paper's coexistence classification. It also sharply delimits what remains open: global periodic-orbit mechanisms are not excluded.

## Evidence and literature

- https://arxiv.org/abs/2604.18903 — T. Hmidhi and R. Fekih-Salem, AM2 model with a series configuration of interconnected chemostats and distinct removal rates; source model, trace condition, and open Hopf/limit-cycle discussion.
- https://doi.org/10.1007/s11538-025-01475-5 — Hmidhi, Fekih-Salem and Harmand, earlier serial-AM2 analysis with equal-removal setting; contextual prior work.
- https://doi.org/10.1137/18M1171801 — Fekih-Salem and Sari, chemostat with aggregated biomass and distinct removal rates; nearby but structurally different dynamics.

## Limitations

- The result is local: it excludes ordinary Hopf bifurcation from equilibria but not periodic orbits born in global bifurcations or other nonlocal mechanisms.
- The argument relies on the feed-forward block-triangular serial-AM2 structure and does not automatically extend to feedback, delay, flocculation, mutualism, or predator-prey variants.

## Audit conclusion

All three audit axes pass. No substantive research-file correction is required. This audit changes only the independent-audit verification channel and does not alter Lean or expert-attestation channels.
