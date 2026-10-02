# Independent mathematical audit — 2026-10-01

## Final claim

Within the sharp Huang--Sukochev boundedness region for the Arazy divided-difference symbol associated with \(\lambda\in\ell^r\), the multiplier \(S_\Psi:S^q\to S^p\) is compact exactly when \(f(H_\lambda)=0\); if \(f(\lambda_i)\ne0\), its essential norm is at least \(|f(\lambda_i)/\lambda_i|\).

## Correctness — PASS

PASS. Necessity follows from a fixed-row matrix-unit sequence: for nonzero \(\lambda_i\), the divided-difference coefficient against \(\lambda_k\to0\) tends to \(f(\lambda_i)/\lambda_i\), so compact images cannot contain the resulting uniformly separated tail, and the same argument gives the essential-norm lower bound. For sufficiency, \(f(H_\lambda)=0\) kills every off-eigenspace block. Each nonzero repeated-eigenvalue block is finite because \(\lambda\in\ell^r\), while the zero block has derivative coefficient zero from the assumed derivative decay. The multiplier is therefore a block-diagonal pinching weighted by derivatives tending to zero; Schatten Hölder/inclusion estimates in the sharp exponent region make finite-block truncations converge in operator norm, including the quasi-Banach cases.

## Originality — PASS

PASS. Huang--Sukochev's full primary paper proves exactly the sharp boundedness region and its sharpness and extends boundedness to semifinite double operator integrals, but it does not state a compactness classification or essential-norm obstruction for the discrete divided-difference multiplier. Hladnik's earlier paper is genuinely relevant because it characterizes compact Schur multipliers on \(B(H)\) through a Haagerup tensor product; its abstract was inspected, but a verified full text could not be obtained in this run after the open and institutional-access attempts. That source is not obviously decisive for unequal Schatten-domain/range exponents, and the explicit fixed-row lower bound plus weighted spectral pinching are not stated in the available material. No stronger implication was found.

### Equivalent formulations

Compactness of the operator between Schatten ideals is stronger than membership of its values in compact operators.

### Broader coverage

Neither available result mechanically yields the discrete spectral iff criterion simultaneously for all sharp \(S^q\to S^p\) pairs.

### Exact database or table

The database search is supportive only; originality rests on theorem-level comparison.

### Claim versus prior implication

No decisive implication from either source to the audited unequal-ideal spectral classification was established.

## Scientific value — PASS

PASS. The theorem supplies the natural qualitative boundary immediately beyond a newly sharp boundedness theorem: boundedness has a full exponent region, while compactness collapses to the rigid spectral condition \(f(H_\lambda)=0\). The essential-norm obstruction and finite-block pinching argument are reusable for operator-ideal questions, so this is a motivated structural result rather than routine recomputation.

## Sources inspected

- **J. Huang and F. Sukochev, Arazy Conjecture Concerning Schur Multipliers** (arXiv:2609.17144): SHARP_BOUNDEDNESS_NOT_COMPACTNESS. The paper establishes boundedness and sharpness across the exponent region and related DOI estimates; it does not state the audited compactness iff or essential-norm formula.
- **Milan Hladnik, Compact Schur Multipliers** (doi:10.1090/S0002-9939-00-05708-7): PLAUSIBLE_BUT_NOT_DECISIVE_ACCESS_RISK. The available theorem scope is compact Schur multipliers on \(B(H)\); no available text connects it decisively to the audited all-\(p,q\) divided-difference spectral equivalence.

## Residual risks

- Hladnik's full paper was inaccessible in this run and is a genuine residual originality risk, although its available scope does not by itself decide the unequal-Schatten claim.
- Absolute novelty remains best-knowledge; a compactness theorem under different operator-ideal terminology could exist.

## Disposition

**passed**
