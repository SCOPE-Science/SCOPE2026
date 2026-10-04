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
The theorem was reconstructed from the definition of the cyclic subgroup graph, the semidirect-product law of a generalized dihedral group, and the exact comparison/product statements in the cited 2023 source.

Critical checks:
- for odd \(|A|=m\), every element of the coset \(At\) is an involution;
- the \(m\) involutions in \(At\) generate \(m\) distinct maximal cyclic subgroups of order \(2\);
- no new cyclic subgroup lies between two cyclic subgroups already contained in \(A\), so \(C(A)^*\) is preserved as the old part of the Hasse graph;
- therefore \(\varepsilon(\operatorname{Dih}(A))=\varepsilon(A)+m\);
- the cited theorem gives \(\varepsilon(A)\ge\varepsilon(C_m)\), with equality exactly for cyclic \(A\);
- the coprime product formula gives \(\varepsilon(C_{2m})=2\varepsilon(C_m)+\tau(m)\);
- for every odd prime power \(p^a\), \(\tau(p^a)+\varepsilon(C_{p^a})=2a+1\le p^a\), with equality only at \(p^a=3\);
- for coprime \(u,v>1\), the quantity \(f(r)=\tau(r)+\varepsilon(C_r)\) satisfies
  \[
  f(uv)=f(u)f(v)-\varepsilon(C_u)\varepsilon(C_v)<f(u)f(v),
  \]
  which yields \(f(m)\le m\), with equality only at \(m=3\).

`artifacts/verify.py` independently enumerates cyclic subgroups and Hasse edges for several cyclic and noncyclic odd abelian kernels, constructs the corresponding generalized dihedral groups, and checks the exact edge formula and comparison. It also checks the auxiliary cyclic inequality through a bounded odd range. The replay returns `VERIFY_OK`.

Finite computation is not used to establish the universal result.
