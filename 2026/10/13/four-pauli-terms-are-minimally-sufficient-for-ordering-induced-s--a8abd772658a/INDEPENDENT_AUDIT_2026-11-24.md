# Independent mathematical audit

## correctness

PASS

Use the operator norm and real a,b≠0. The distinct directions imply R is not ±I, so its positive eigenspace is nonzero (a nonscalar Hermitian Pauli is traceless). Both operators preserve the two sectors; on R=−1 the factors cancel and H vanishes. On R=+1 anticommutation gives the exact product cos(2bh)[cos(2ah)I−i sin(2ah)P]−i sin(2bh)Q. Independently, writing d=√(a²+b²), the exact evolution on that sector is cos(2dh)I−i sin(2dh)(aP+bQ)/d. Taylor subtraction yields (4iab/3)(2bP−aQ)h³+O(|h|⁴). The square of the self-adjoint Pauli combination is (a²+4b²)I; the reverse triangle inequality gives the claimed nonzero leading norm. Unitary telescoping gives O(|t|³/r²) for fixed t. In the quadratic product defect every anticommuting pair contributes a nonzero coefficient times its product, up to phase. Among at most three distinct directions two different unordered pairs must share a letter; equality of their products modulo phase would cancel that letter in the Pauli group modulo phases and identify the other two letters. Hence every nonzero contribution has a distinct Hilbert–Schmidt basis direction and there is no cancellation in any order. Replay is the two exact sector formulas above and the shared-letter test; the numerical artifact was inspected, not executed. No assertion about repeated or half-step factors, randomized order, or observable-restricted error is needed.

## originality

PASS

General BCH order conditions, sensitivity to ordering, and cancellations in error analysis or averaging are prior inputs. The distinct claim is the sharp four-versus-three threshold for a single deterministic full-step sweep on distinct Pauli terms, with an explicit family and nonzero local cubic norm coefficient. The strongest inspected sources did not supply this Pauli threshold or single-step construction.

## value

PASS

This resolves a natural resource question about using order as the only freedom in a single sweep: four distinct Pauli terms suffice and three cannot. The nonzero cubic coefficient separates actual order elevation from commuting exactness, and the effect requires neither extra stages nor averaging. This is a structural boundary, not a claim of a generic simulation advantage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
