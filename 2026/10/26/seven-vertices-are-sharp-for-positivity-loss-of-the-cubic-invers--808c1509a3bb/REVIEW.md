# Scientific review of the sharp seven-vertex Padé positivity barrier

## Correctness — PASS
The domain is precise: finite simple connected unweighted undirected graphs and the third-order inverse-Taylor heat matrix. For all positive timesteps, the denominator polynomial is positive on the nonnegative Laplacian spectrum, so all denominators are strictly positive. The verified cofactor identity reduces every off-diagonal sign to a polynomial sign; the exhaustive independent-of-atlas permutation-orbit enumeration covers all connected graph classes on two through six vertices (1, 2, 6, 21, 112 classes). Exact rational arithmetic verifies all 1,933 required cofactors, with at most a \((1+h)^{32}\) positive multiplier, and verifies the seven-path witness. The supplied checker was executed successfully. Spectral contractivity and mass preservation follow separately from the functional calculus and the zero row sums of the Laplacian. No finite timestep sample substitutes for the continuum positivity proof.

## Originality — PASS with residual literature risk
Closest inspected primary works: Gottlieb, Shu and Tadmor (2001), full text, concern general SSP time-stepping conditions; Blanes, Iserles and Macnamara (2022), full text, construct different positive graph-Laplacian integration mechanisms. The closest historical title explicitly mentioning positivity-preserving Padé approximations is Masood and Yousuf (2010), but only its abstract was available; this creates a residual risk and no whole-document noncoverage conclusion is drawn. The nearest accessible historical results concern distinct rational stability functions (the \([0/2]\) inverse-Taylor step, \([2/2]\) Gauss Padé, and two-stage Radau IIA), which do not imply the present exact graph cutoff. The claim is confined to the exact \([0/3]\) order cutoff and its rational reentry witness; method-level novelty is not asserted.

## Mathematical value — PASS
The first dimension of failure is a natural sharp invariant for a high-order heat timestep: spectral contractivity and conservation alone are insufficient to ensure positivity. The outcome supplies a complete, exact minimum-order barrier for every simple connected unweighted graph, not merely for one graph family. The unique difficult six-vertex cofactor requiring a degree-32 positivity multiplier illustrates why this is more than a direct Taylor-sign check, and the seven-path exhibits a nonmonotone positivity window. This gives a meaningful diagnostic when selecting a diffusion integrator for small state spaces, while leaving the full large-order classification open.

## Limits and provenance
No classification of weighted, directed, or larger graphs is claimed; historical Padé literature remains a risk. The reviewed evidence is the mathematics and replayable code contained in this package. This is not an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
