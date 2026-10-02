# Independent mathematical audit — 2026-10-01

## Final claim

The displayed rational function of type \((5,5)\) has no pole on \([-1,1]\) and approximates \(|x-1/2|\) there with uniform error at most \(0.00878494986604459<0.01\), hence \(E_{5,5}\le 0.01\).

## Correctness — PASS

Replaying the certificate from the printed rational coefficients with exact Fraction arithmetic gives minimum sampled denominator \(0.9946050566757593\) and, after the global derivative correction, the rigorous denominator lower bound \(0.9401355692097929>0\). On 2000 cells with the kink as a boundary, the largest exact endpoint error is \(0.00878086268557671\) and the largest second-derivative Taylor correction is \(0.00000408718046788004\), totaling \(0.00878494986604459<0.01\). This proves pole-freeness and the claimed uniform upper bound; no minimax optimality is asserted.

## Originality — PASS

Chebfun publicly treats the same shifted function \(f(x)=|x-0.5|\) and exhibits type \((8,8)\) and \((16,16)\) rational minimax examples, but it does not give the displayed type \((5,5)\) rational coefficients or a rigorous 0.01 certificate. Published-record search found later related finite-type approximation records with different functions/types but no covering result for this witness.

### Equivalent formulations

The statement is equivalently an explicit feasible point for the type-\((5,5)\) minimax problem with objective below 0.01; prior sources located do not supply this feasible point.

### Broader coverage

Higher-type numerical minimax examples and general theory do not mechanically imply the existence of this particular lower-type rigorous witness.

### Exact database or table

No exact external table row was located, leaving only the ordinary best-knowledge novelty risk.

### Claim versus prior implication

Existence of a strong type-\((8,8)\) approximant does not imply that type \((5,5)\) crosses the 0.01 threshold; the degree-restricted feasibility claim requires separate evidence.

## Scientific value — PASS

The function is an established rational-approximation benchmark, and type \((5,5)\) is a natural low-complexity level below the demonstrated type \((8,8)\) example. A fully rational certificate that a 1-percent uniform-error threshold is already attainable at this type is a reusable finite benchmark; it is explicitly limited to an upper bound and does not overclaim minimax optimality.

## Sources inspected

- **Nick Trefethen, Best approximation with the REMEZ command, Chebfun example** — https://www.chebfun.org/examples/approx/BestApprox.html. SAME_FUNCTION_HIGHER_TYPE_NOT_COVERING: It demonstrates higher types numerically but does not state or certify the audited type-\((5,5)\) threshold.
- **Published finite-type rational-approximation records** — https://github.com/Resultary/2026/tree/main/2026/9/14/SCOPE014. RELATED_DIFFERENT_TYPE_OR_FUNCTION: No related record supplies the same type-\((5,5)\) shifted-function certificate.

## Checked evidence

- Assigned RESULT.md, candidate_exact.json, and verify_certificate.py from the exact Git tree.
- Fresh exact rational replay of both denominator and second-derivative certificate stages.
- Same-function Chebfun benchmark and published-record semantic search.

## Residual risks

- The witness is only an upper certificate; no lower bound or minimax optimality is established.
- The archived verifier contains a historical output/artifacts path for candidate_exact.json, so the audit replayed the exact rational certificate independently from the committed coefficient file.

## Disposition

**passed**
