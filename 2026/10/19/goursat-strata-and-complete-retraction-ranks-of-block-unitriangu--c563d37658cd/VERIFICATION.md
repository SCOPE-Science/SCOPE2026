---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For field-linear multiplicative maps only, A^2=kz is invariant and F(v+sz)=Tv+(phi(v)+cs)z. Multiplicativity is B(Tv,Tw)=cB(v,w) for the ordered product B((u,w),(u',w'))=uw'; idempotence adds T^2=T, c^2=c and phi T+c phi=phi. If c=1 and v lies in ker T, the pairing equation in both orders puts v in the intersection of the two radicals of B. These radicals are complementary coordinate spaces, so T is invertible even though B is degenerate; idempotence forces T=I, then phi=0. For c=0 proper maps are exactly projections T onto subspaces S with B(S,S)=0 and lifts phi=eta T. For each S of dimension r there are q^r distinct graph images and q^(r(2n-r)) complementary kernels per image. For coordinate projection dimensions a,b, zero product says the projected spaces pair trivially; they have [n choose a]_q [n-a choose b]_q choices. Goursat kernels leave t-dimensional quotients matched by an isomorphism; their choices give [a choose t]_q[b choose t]_q|GL_t(q)| and r=a+b-t. This proves the complete map count including the identity. At r=n, t=0 and a+b=n; for rank one, counting nonzero (u,w) with uw=0 and dividing by q-1 gives the reported coefficient. The submitted checker was inspected but not run. A separately written bounded enumeration of all q^9 maps on the 3-dimensional algebra, testing the ordered multiplication on basis pairs and idempotence, gave rank-1 multiplicities 8,18,32 over q=2,3,4 (one zero and one identity each). Independently extending binary subspaces and testing zero products on bases gave dimensions 0 through 3 counts 1,35,77,16 at n=3. Direct enumeration of the 2^16 quotient matrices at q=n=2, retaining idempotent zero-product projections and counting graph functionals, gave ranks 0,1,2,5 with multiplicities 1,144,320,1. These replay procedures test bounded cases; the algebraic proof covers arbitrary q,n.

## originality

PASS

Best-of-knowledge pass for the complete retraction-map classification of this one-sided, degenerate pairing, not for the Gaussian–Goursat image census by itself. There is exact same-algebra coverage of proper image counts and very close coverage of the map-count formula for a different, nondegenerate multiplication; neither theorem as stated covers idempotent maps for the one-sided product. This is a narrow distinction, and the two matching ingredients should not be treated as independent discoveries.

## value

PASS

The map problem is natural for the basic noncommutative three-block nilpotent radical: classify all the direct multiplicative splittings and their ranks. The answer distinguishes associative retractions from Lie ones and excludes an entire interval of intermediate ranks, while giving a projection/kernel description of every proper retraction including all field extensions. This is more than recomputing a subspace table, although the complementary-kernel factor by itself is standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
