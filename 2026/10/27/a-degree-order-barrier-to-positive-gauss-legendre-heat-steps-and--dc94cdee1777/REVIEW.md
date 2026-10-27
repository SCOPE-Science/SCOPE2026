# Scientific review

## Correctness — PASS

For any connected unweighted \(d\)-regular graph, the two adjacency trace identities imply \(\operatorname{tr}(AL^+)\ge(N-3d)/(2d)\). Equality at \(N=3d\) is impossible by the first and second nonconstant adjacency moments. A strictly positive edge entry of \(L^+\) follows from \(\operatorname{tr}(AL^+)=2\sum_{uv\in E}(L^+)_{uv}\). The exact Padé expansion then forces a negative completed edge transition for all sufficiently large steps. The closed formulas on \(C_3\square C_3\) follow from its three eigenspaces and are manifestly positive. All steps including equality boundaries and the \(h=0\) case were checked. Exact-rational matrix computations independently check selected cases; they are not substitutes for the proof.

## Originality — PASS, subject to residual source risks

The cited monotonicity literature establishes general SSP restrictions but not the claimed degree–order obstruction for all connected regular graphs. Accessible full text for explicit multistep SSP methods treats different integrators. Previously recorded special cases cover complete multipartite graphs, cycles, cubes, and strongly regular graphs; especially, the nine-vertex rook graph has already been classified and is **not separately novel**. Those family-specific results do not imply the general \(N\ge3d\) obstruction or exhaust the entire torus family. Queries also checked pseudoinverse-edge sign, cycle product, Padé, and graph positivity aliases. No stronger prior implication was found in inspected material, although no search can establish uniqueness. Some potentially relevant publisher full texts could not be inspected; they are explicitly listed as residual risks.

## Mathematical value — PASS

A fourth-order A-stable discretization is automatically spectrally contractive on graph diffusion, but entrywise positivity governs numerical preservation of probability and heat nonnegativity. The degree–order result supplies a broad and easily checkable structural no-go condition for this discrepancy and pins down an exact exception among an infinite, natural family of periodic grids. The positive-pseudoinverse-edge trace inequality provides a reusable mechanism, not merely another isolated example. The torus classification is complete and requires no numerical root solving.

## Evidence boundaries

The numeric regression spans seven test graphs and five steps each, not an exhaustive search. The unknown general sharpness of the order threshold and possible specialized historical prior formulations are not asserted resolved. The claim is about end-step entrywise nonnegativity, not internal-stage SSP.

Self-review: passed. Independent audit: not yet performed.
