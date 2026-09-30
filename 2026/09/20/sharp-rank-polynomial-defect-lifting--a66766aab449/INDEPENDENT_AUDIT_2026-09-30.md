# Independent audit — 2026-09-30

**Record:** `2026/09/20/sharp-rank-polynomial-defect-lifting--a66766aab449`  
**Audited source tree:** `e7bee9dd64346cb8ad0f55cd6b41e2c63358e1b0`  
**Disposition:** passed

## Correctness — PASS

PASS. Let M=Ran p(T). Since M is T-invariant and dim M=r, an annihilator q of T|M with degree at most r gives (qp)(T)=0 and hence deg m_T<=d+r. With X=M⊕Y, T has upper-triangular blocks [[A,B],[0,D]] and p(D)=0; replacing the M-block by any root lambda of p produces S=diag(lambda I_M,D), so F=T-S has range contained in M and rank at most r. The same block proof works for any closed complemented M without finite-dimensionality. For arbitrary S with p(S)=0, the noncommutative telescoping formula expresses p(T) as a sum of d operators factoring through F=T-S, giving rank p(T)<=d rank F. The scalar-block example proves the upper constant one for each fixed p, and cyclic-versus-nilpotent d-blocks prove the universal lower factor 1/d. I found no missing commutativity assumption in the telescoping step.

## Originality — PASS

PASS. Barnes (1985) already proves the qualitative finite-rank lifting: if p(T) has finite-dimensional range, some finite-rank J makes p(T-J)=0. The inspected primary text does not impose Ran J⊆Ran p(T), does not give rank J<=rank p(T), and does not state the d+r minimal-polynomial bound or two-sided rank-distance estimate. Kramar's later abstract concerns the reverse direction, finite-rank perturbations of algebraic operators. On the sources inspected, the defect-range localization and sharp quantitative constants are genuine additions. Poorly indexed operator-ideal literature remains the ordinary residual risk.

## Scientific value — PASS

PASS. The localized correction is stronger than mere existence because it identifies the exact defect subspace supporting the repair; the sharp rank-distance bounds quantify how much perturbation is necessary and sufficient, and the complemented-range extension isolates the mechanism beyond the finite-rank case.

## Independent checks

- Reconstructed the invariant-range block decomposition and the complemented-range extension.
- Re-expanded p(T)-p(S) term-by-term and checked the rank accounting.
- Verified the scalar example for the sharp upper constant and the cyclic/nilpotent direct-sum example for the lower factor.

## Literature evidence

- https://doi.org/10.2140/pjm.1985.117.219 — Barnes (1985), open-access primary source; Corollary 11 gives qualitative finite-rank lifting.
- https://doi.org/10.4064/cm134-1-6 — Álvarez (2014), polynomially finite-rank linear relations and Riesz--Schauder/Fredholm structure.
- https://acta.bibl.u-szeged.hu/16425/ — Kramar (2012), abstract-level evidence on finite-rank perturbations of algebraic operators.

## Limitations

- The algebraic statement is over complex Banach spaces, using existence of a root of p.
- The lower factor 1/d is sharp uniformly over degree-d polynomials, not claimed for every fixed polynomial.
- Originality remains qualified against poorly indexed operator-ideal literature.

No GitHub write was performed by the audit chat. This file is staged by the guarded `scope-audit-change-set-v1` plan only.
