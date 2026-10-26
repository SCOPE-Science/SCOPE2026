# Mathematical assessment

## Correctness — PASS

The completed stability function follows from the classical two-stage Radau IIA tableau. A distance-five pair has no off-diagonal matrix-power contribution before order five, and the stability function has fifth Taylor coefficient \(-1/108\); the resulting leading entry is negative. The large-timestep limit is the strictly positive stationary projector of the connected Laplacian. For unweighted paths up to six vertices, exhaustive exact polynomial coefficient certificates verify the safety boundary and identify the unique exceptional endpoint-entry type. The six-path quintic has exactly one positive root by Descartes' rule, with exact rational root isolation. All formulae are replayed using the enclosed program. The finite identities and the arbitrary-graph proof are distinct components.

## Originality — PASS, with limits

The primary archival positivity paper of Zappavigna, Colaneri, Kirkland and Shorten treats diagonal Padé approximation, counterexamples, and general sufficient positivity conditions, not the subdiagonal Radau stability function on paths. Available general method specifications determine the stability function but not the complete path-boundary and recovery theorem. Searches for the path-specific quintic, diameter-five obstruction, and equivalent distance-five transition kernels identified no stronger covering result. Other numerical-integrator and graph-geometry positivity findings do not imply this exact classification. This does not exclude unknown equivalent literature; priority has not been independently audited.

## Value — PASS

Entrywise nonnegativity is necessary to interpret numerical diffusion steps as stochastic transition matrices. The result exposes a structural obstruction that no smaller timestep can resolve on any positive-weight connected graph of diameter at least five, despite eventual recovery at large timesteps. The first minimal path witness is resolved exactly rather than numerically: one quintic completely determines its admissible timestep set. The finite threshold and all-graph extension together give a reusable benchmark for positivity-preserving numerical integration, rather than only a cheap sign check.

## Sources and limitations

The primary comparison is the openly accessible 2012 working paper *Essentially Negative News About Positive Systems* (Maynooth repository entry 3761), including its Padé definitions and the positivity analysis. The method definition was checked against Ketcheson's Radau IIA2 tableau and stability function. General arbitrary-graph positivity windows are not classified; the method's internal stages are not studied. Unrecognized equivalent prior publications remain a risk.

Self-review: passed. Independent audit: not yet performed.
