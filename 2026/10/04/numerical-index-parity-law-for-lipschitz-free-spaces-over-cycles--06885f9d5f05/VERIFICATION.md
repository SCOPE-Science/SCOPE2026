---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof was checked at the level of definitions, quantifiers, quotient normalization, duality, extreme points, and the extremal operator.

1. **Cycle quotient model.** Edge increments identify \(\operatorname{Lip}_0(C_n)\) with the zero-sum hyperplane \(H_n\subset\ell_\infty^n\). An increment vector has Lipschitz norm equal to its maximum edge increment because shortest paths are sums of unit edges. The preannihilator of \(H_n\) is exactly \(\operatorname{span}\{\mathbf1\}\), so \(\mathcal F(C_n)\cong\ell_1^n/\operatorname{span}\{\mathbf1\}\).

2. **Extreme points.** The primal quotient ball is the convex hull of \(\pm q(e_i)\), and each is exposed. In the dual cube section, an extreme point has at most one coordinate not equal to \(\pm1\). Parity forces balanced all-sign vectors for even \(n\), and exactly one zero plus balanced signs for odd \(n\).

3. **Numerical-radius reduction.** For finite-dimensional polytopes, maximizing \(|x^*(Tx)|\) over norming pairs reduces first to an extreme point of the primal norming face and then to an extreme point of the dual norming face. This yields the coordinate formula used in the proof.

4. **Odd lower bound.** After shifting a representative by its median, the quotient norm is its \(\ell_1\)-mass. The only case in which a norming dual extreme must vanish at the prescribed coordinate is a unique zero median with exactly \((n-1)/2\) positive and \((n-1)/2\) negative coordinates. Moving the unique dual zero to a smallest-magnitude nonzero coordinate loses at most \(1/(n-1)\) of the norm.

5. **Sharp witness.** For odd \(n\), the cyclic shifts of \((0,1,\ldots,1,-1,\ldots,-1)/(n-1)\) each have quotient norm one and sum to zero, so they define a linear operator on the quotient. Every admissible extreme norming functional omits one nonzero coordinate, giving numerical radius exactly \((n-2)/(n-1)\).

The standalone script `verify_cycle_index.py` uses exact rational arithmetic. Its replay output is:

`WITNESS_OK n=6..10`

`LOWER_STRESS_OK n=7 coefficients={-1,0,1}`

The second line is an exhaustive finite stress test over all vectors in \(\{-1,0,1\}^7\) and all distinguished coordinates. These computations corroborate the formulas but do not prove the infinite family; the symbolic argument does.

The verification does not establish a complex-scalar analogue and does not eliminate the stated residual bibliographic risk.
