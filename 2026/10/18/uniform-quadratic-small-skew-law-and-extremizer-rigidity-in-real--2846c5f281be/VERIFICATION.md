---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For unit x,y define C=∫x³y, E=∫xy³, D=∫x²y² and F=C−E. The pointwise polynomial identity ||x²−y²+√2xy||₂²=2+2√2F proves the sharp F≥−1/√2. The exact real quartic expansions and uniformly bounded fourth-root Taylor remainders give (||x+τy||₄+||τx−y||₄)/2=1+τF/2+τ²B+O(τ³), B=3D/2−3(C²+E²)/4. The identities for <R,xy> and <R,x²+y²> imply |B−9/16|≤4||R||₂. Completing the nonnegative defect quadratic gives the uniform lower 1−τ/(2√2)+9τ²/16−Kτ³ for all real L4 and any outer t≥1, using power-mean dominance over the arithmetic mean. On any two disjoint normalized supports, take x=af+bg,y=−bf+ag with a²=(√3+1)/(2√2),b²=(√3−1)/(2√2); both outputs have the identical fourth power 1−√2τ+3τ²+√2τ³+τ⁴, giving the uniform upper bound for every outer exponent including infinity. Equality in the square yields exactly two ratio levels r± and the specified y⁴-mass fractions. For O(τ³) near-optimal pairs the uncompleted quadratic forces ||R||₂=O(τ). Remainders are uniform via |C|,|E|,D≤1, τ≤1/8, and two-point power-mean comparison; no finite sampling substitutes for the analytic proof.

## originality

PASS

The exact all-small-skew L4 law for the previously uncontrolled outer exponents 1<=t<4, together with a square-defect rigidity statement for almost-minimizers, was not implied by the primary papers and complete relevant published results inspected. Xu–Liu Theorem 3.2 already proves matching exponent t=p=4; its balanced two-support optimizer, combined with monotonicity, in fact implies the whole t>=4 branch. These precovered cases are explicitly credited, rather than represented as original. The novel remaining assertion is an exact dimension-free lower expansion for t=1 and 1<t<4 and the quantified L2 stability that follows from a sharp antisymmetric-duality square identity. This is a best-of-knowledge priority assessment, not a claim of independently certified global novelty.

## value

PASS

The skew Schäffer infimum is a natural published Banach-space geometric invariant, and the cross-exponent regime 1<=t<4 is a specific mathematical gap after the matching-exponent theorem. Determining its dimension-free sharp two-term onset, including t=1, is not a relabeling of the t=4 formula: prior monotonicity has the incorrect direction for the essential lower bound. A sharp square identity, two-level classification of antisymmetric duality-map extremizers, and quantitative O(τ) stability for O(τ³) almost-minimizers give structurally useful information about this non-Hilbert geometry. The object and invariant are intrinsically motivated independently of any speculative application; no general/downstream theorem is needed for mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
