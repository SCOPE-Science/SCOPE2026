# Barycentric subdivision and discrete conformal scaling

## Correctness

**PASS.** In the admissible range z=e^t>1/4, the scaled triangle has altitude squared z−1/4. The midpoint equations enforce equal scaling factors at all three original vertices, leaving a single consistency requirement from two centroid-to-midpoint edges: z=(z+2)/(4z−1). This becomes (2z+1)(z−1)=0, whose only admissible positive solution is z=1. At t=0 the subdivided metrics agree. This checks both the necessity and sufficiency directions, including the nondegenerate boundary.

## Relationship to prior mathematics

**Best-of-knowledge original.** The vertex-scaling relation follows Bobenko–Pinkall–Springborn (2015). Ulrich Bauer's 2015 subdivision problem names barycentric subdivision but asks an existence question rather than deriving this failure. Canonical Möbius Subdivision (Vaxman–Müller–Weber, 2018) uses a different Möbius-invariant operator and states simultaneous conformal-equivalence-preserving subdivision as future work. BPM (Rorberg–Vaxman–Ben-Chen, 2023) provides continuous interpolation, not the standard induced barycentric metric theorem. An unindexed elementary observation remains possible; the 2008 mesh-conformality source was not fully readable.

## Mathematical value

**PASS.** This exact counterexample rules out the standard Euclidean midpoint/centroid barycentric construction as a universal preserving rule. The complete single-ray classification is a motivated boundary result associated with a named subdivision question, not an exhaustive answer to that question.

## Scope

The result does not address alternative metric assignments, other subdivision schemes, or general existence of a conformality-preserving subdivision. Its stated one-triangle domain has boundary.
