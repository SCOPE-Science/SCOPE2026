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

The accepted claim is a symbolic consequence of the source's Jordan-block multiplicity formula, not a numerical experiment.

For every cone \(c\) and primitive index \(j\ge0\), a block contributed by the formula has size
\[
k=m_c-2j+1,
\qquad
m_c=d-\dim c.
\]
Thus \(k\le d+1\). Equality requires \(\dim c=0\) and \(j=0\). There is only one zero cone.

For the zero cone the source gives
\[
l^*_{\psi_0}(0;t)=1,
\]
so its only local degree is \(a=0\) with multiplicity one. The corresponding degree-zero primitive intersection-cohomology multiplicity is also one. Substituting these data into the published formula yields exactly
\[
J_{d+1,1}=1
\]
and
\[
J_{d+1,\lambda}=0
\quad\text{for}\quad
\lambda\ne1.
\]
No term can produce a larger block. Therefore the normalized nilpotent logarithm satisfies
\[
N_\infty^d\ne0,
\qquad
N_\infty^{d+1}=0.
\]

The source's nonsimplicial pure-sheaf formulation makes the multiplicities subdivision-independent. The 2024 predecessor was checked separately and is treated only as coverage of the narrower simplicial vertex-supported special case. No lower Jordan-block multiplicity, rational polarization, or extension datum is asserted.
