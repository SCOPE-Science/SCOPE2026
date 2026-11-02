---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Let M be point-block incidence for any existing AD(n,mu). The design identities MM^T=kI+lambda J and M^T M=kI+mu(J_r-I_r) tensor J_n split real point and block spaces into v-1 corresponding singular directions with 2x2 B1, r-1 uncoupled parallel-class contrasts with scalar L=f0-n f2+(n-1)f4, and two constant directions with 2x2 B0. Total 2(v-1)+(r-1)+2=v+b dimensions, so PSD iff L>=0, B1>=0, B0>=0, including singular cases and arbitrary automorphism groups. For exponential f_j=z^j with w=z² and 0<w<1, direct determinant identities give L=(1-w)(1-(n-1)w), det B1=(1-w)^2(1-(k-1)w), and det B0=(1-w)/(n-1)*[(n-1)+beta w+gamma w²]. Positive diagonal pivots reduce PSD to w<=1/(k-1) and the quadratic inequality; a=0 separately yields the all-ones rank-one kernel. In AG(3,3), n=3,k=9,r=13, determinant factor 1-54w+416w² has roots (27±sqrt313)/416 both below 1/8, yielding exactly two positive-a disconnected PSD bands, with rank 40 at w=1/8 and 65 at the two quadratic boundaries. Independent symbolic algebra checked all determinant factors, inequalities, and root ordering; the singular-value proof handles all actual designs. The design's existence assumption is explicit, no universal (n,mu) existence assertion.

## originality

PASS

Ma 2016 explicitly derives spectral factorization and distance signature for affine-resolvable incidence graphs at the one specific radial weight f_d=d, supplying the essential design identities and singular-space structure. DeVille 2017/2020 treats arbitrary radial weights on distance-regular graphs and Cartesian products, where distance-class matrices commute, whereas these incidence graphs are biregular for r != k and their B1 distance-one and distance-two restrictions do not commute. This structural nonapplicability prevents a direct theorem specialization. The present exact all-parameter 5-weight PSD cone plus disconnected AG(3,3) exponential kernel interval is a motivated extension; the possibility of equivalent older coherent-config/block-matrix spectral computations remains explicit.

## value

PASS

The complete radial positive cone and its exact rank multiplicities are natural stability and covariance-kernel invariants of incidence geometries; disconnected admissible exponential bandwidths provide a structural counterexample to naïve monotonicity, with sharp radical endpoints and boundary rank changes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
