---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

At the exact Padrol–Philippe normalization SP(A)=Σ_{i<j} [−(a_i−a_j)/2,(a_i−a_j)/2], the complex chord identity a_i−a_j=2i exp(πi(i+j)/n) sin(π(i−j)/n) partitions generators into n unoriented directions labelled i+j mod n, at angular gaps π/n. Each class contributes one opposite edge pair of length Σ|a_i−a_j|. For odd n=2m+1, multiplication by 2 acts transitively on the classes and Σ_{d=1}^m 2sin(πd/n)=cot(π/(2n)); the 2n-gon is equilateral and equiangular, hence regular. For even n=2m, the classes split into even and odd sums: total chord lengths 2cot(π/n) and 2csc(π/n). Alternating support numbers p,q obey q−p cos y=cos y and p−q cos y=1, solving p=(1+cos²y)/sin²y and q=2cos y/sin²y. Consecutive support-line intersections have the same radius, proving cyclicity; area=sum h_i L_i/2=n cos y(3+cos²y)/sin³y. Nonidentical alternating lengths imply exactly 2n metric symmetries for even n, versus 4n for regular odd case. Checked raw all-pair chord classes independently for n=3..44; tests supplement all-n trigonometric proof.

## originality

PASS

Full Padrol–Philippe source supplies sweep zonotope, normal fan and permutahedral shadows but does not provide metric regular-n-gon specialization in inspected sections. Older Gritzmann–Sturmfels shellotope source names the same construction, but full text was inaccessible; only abstract metadata was compared and its potential coverage remains an explicit risk. Semantically targeted searches for shellotope, pairwise-difference zonotope and even–odd edge orbit formulas gave no covering indexed theorem. The result requires nontrivial object-specific chord parity and exact edge/area computation beyond the general zonotope definition.

## value

PASS

Complete natural canonical-family metric classification of the planar pairwise-difference sweep construction: parity determines exact regularity, two edge orbits versus one, cyclicity, closed perimeter/area, and whether the Euclidean symmetry group doubles. The arithmetic orbit splitting of chord classes under rotation is a structural phenomenon not implicit in abstract normal-fan equivalence. This supplies precise reference examples for sweep-polytopal geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
