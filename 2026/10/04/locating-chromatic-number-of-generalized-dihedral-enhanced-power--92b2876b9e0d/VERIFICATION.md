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
The universal statement is proved symbolically from the generalized-dihedral multiplication law and the locating-coloring definition.

Critical checks:
- every element of the nontrivial coset has order \(2\) and is adjacent only to the identity in the enhanced power graph;
- a nonidentity kernel element is a leaf exactly when it belongs to \(T(A)\);
- the set \(At\cup T(A)\) is therefore a false-twin class of size \(|A|+|T(A)|\);
- the identity is universal, giving the lower bound \(|A|+|T(A)|+1\);
- the constructed coloring uses exactly that many colors and distinguishes each repeated-color leaf/nonleaf pair by a nonidentity neighbor of the kernel vertex;
- outside the \(2\)-group case every involution lies with an odd-order element in a cyclic subgroup of order greater than \(2\);
- for an abelian \(2\)-group, \(T(A)=A[2]\setminus2A\), giving \(|T(A)|=2^r-2^s\).

`artifacts/verify.py` independently constructs the groups and enhanced power graphs for twelve cyclic and noncyclic kernels, enumerates cyclic subgroups, verifies the false-twin class, constructs the claimed coloring, computes all color codes, and checks the invariant-factor formula. It returns `VERIFY_OK`.

Finite enumeration is not used to establish the universal theorem.
