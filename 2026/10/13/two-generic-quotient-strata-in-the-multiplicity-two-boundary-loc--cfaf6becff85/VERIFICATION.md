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

The initiating source was checked at Theorem 2.16, Definition 5.7, Proposition 5.8, and Proposition 5.9. These give \(\dim\mathcal R(-1,1,1)=3\), the resolution
\[
0\to\mathcal O_{\mathbf P^3}(-2)\to\mathcal O_{\mathbf P^3}(-1)^{\oplus3}\to F\to0,
\]
the quotient condition \(P_Q(t)=2t\), and the fact that \(\mathcal C(-1,1,1,2)\) is an unresolved part of the non-reflexive boundary.

For a smooth conic \(C\simeq\mathbf P^1\) in a plane avoiding the common zero of the three linear forms, restriction gives
\[
0\to\mathcal O_{\mathbf P^1}(-4)\to\mathcal O_{\mathbf P^1}(-2)^{\oplus3}\to F|_C\to0.
\]
The three quadratic entries form a basis of \(H^0(\mathbf P^1,\mathcal O(2))\). The quotient has degree \(-2\) and no global section, so the splitting theorem forces \(F|_C\simeq\mathcal O(-1)^{\oplus2}\). Hence the quotient-map space to the unique degree-\(-1\) line bundle is \(\mathbf P^1\), giving dimension \(3+8+1=12\).

For a line \(L\) avoiding the common zero, the three restricted linear forms span \(H^0(L,\mathcal O_L(1))\), so after basis change the presentation is \((x,y,0)\). Therefore
\[
F|_L\simeq\mathcal O_L\oplus\mathcal O_L(-1),
\]
and \(\operatorname{Hom}(F,\mathcal O_L(-1))\) is one-dimensional. For two disjoint lines, the two nonzero component maps are unique up to the two independent target scalars, so a fixed hull and fixed unordered line pair determine one kernel. The dimension is \(3+8=11\).

The supporting full text arXiv:1702.06553v1 was checked at Section 4.1 and Proposition 18: \(\mathcal T(2)\) has exactly two irreducible \(8\)-dimensional components, represented generically by the smooth-conic and disjoint-line-pair quotient types used above.

For every constructed kernel, slope stability follows from inclusion into the slope-stable hull with the same rank and first Chern class. Riemann--Roch gives \(\operatorname{ch}(Q)=2H^2-4H^3\), and subtraction from the hull Chern character gives \((c_1,c_2,c_3)=(-1,3,7)\). Thus the constructed points lie in the stated boundary locus.

No exhaustive classification of special incidence strata or of all irreducible components of \(\mathcal C(-1,1,1,2)\) is claimed.
