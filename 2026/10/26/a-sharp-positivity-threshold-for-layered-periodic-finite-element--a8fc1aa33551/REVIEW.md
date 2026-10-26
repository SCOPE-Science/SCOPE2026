# Scientific review

## Correctness — PASS
The stated necessary-and-sufficient property is proved for every even \(N=2m\ge6\), without extrapolation from finite experiments. The proof explicitly constructs the Schur complement, derives two propagator blocks, and exhibits a negative coefficient below the cutoff in both the same-sign and mixed-sign regimes. The positivity conclusion above the cutoff follows from the Stieltjes inverse and nonnegative consistent mass. The four-node exception is given by exact rational matrix inversion. The exact-arithmetic script successfully checked 116 finite parameter/time combinations, but the general proof is analytic. A possible practical implementation risk is orientation of the block shift, addressed by the explicit convention and exact tests.

## Originality — PASS, with residual source-access risk
Relevant earlier literature establishes *sufficient* lower time-step constraints for consistent-mass schemes and documents small-step positivity failures, but no inspected statement derives the exact alternating-diffusivity necessary-and-sufficient criterion for every \(m\ge3\), including the mixed-sign inverse regime. The closest earlier theorem, Li–Huang, is an implication from a Stieltjes coefficient matrix to a positive propagator; the converse is false for the included four-node example and requires the nontrivial resolvent argument for \(m\ge3\). Schatz–Thomée–Wahlbin's time-stepping criteria likewise are not an all-size alternating-diffusivity equivalence. A relevant 2015 paper's full text remained inaccessible; available abstract emphasizes Dirichlet heat schemes, but could conceal an unexpected special-case theorem. This risk prevents any claim of exhaustive priority and merits independent checking.

## Mathematical value — PASS
Consistent finite-element mass matrices generate negative couplings at small positive steps, whereas implicit diffusion can restore the discrete maximum principle. For a layered medium with two natural diffusivities, an exact transition identifies the operational step-size boundary and demonstrates surprising insensitivity to contrast and lattice size. Unlike an arbitrary finite table, the theorem covers infinitely many meshes and parameter values and exposes the exceptional four-node geometry.

## Scope and limitations
This is a one-dimensional uniform periodic alternating-coefficient classification for nodal positivity. No implication is claimed for graded meshes, arbitrary coefficients, more general equations or independent validation. The most relevant inaccessible full text is Chatzipantelidis–Horváth–Thomée (2015), DOI 10.1515/cmam-2015-0018.

Self-review: passed. Independent audit: not yet performed.
