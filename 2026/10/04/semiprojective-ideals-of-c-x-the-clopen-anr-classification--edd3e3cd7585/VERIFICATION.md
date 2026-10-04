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

The final claim is: Let \(X\) be a compact metric space and let \(J\) be a closed lattice ideal of \(C(X)\). Then \(J\) is semiprojective if and only if either \(J=0\), or there is a nonempty clopen absolute neighbourhood retract \(U\subseteq X\) such that \(J=\{f\in C(X):f|_{X\setminus U}=0\}\). Equivalently, for closed \(F\subseteq X\), the ideal \(I_F=\{f\in C(X):f|_F=0\}\) is semiprojective exactly when \(X\setminus F=\varnothing\) or \(X\setminus F\) is a clopen absolute neighbourhood retract. If \(X\setminus F\) is not closed, then \(c_0\) is a contractive lattice retract of \(I_F\). In particular, for the middle-third Cantor set \(K\subset[0,1]\), \(I_K\) is not semiprojective.

The verification has three exact steps.

First, if \(U=X\setminus F\) is not closed, choose \(p\in\overline U\setminus U\) and \(x_n\in U\) converging geometrically to \(p\). The radii chosen in the proof force pairwise disjoint open neighborhoods whose closures lie in \(U\). Positive bumps \(h_n\) supported there satisfy \(h_n(x_n)=1\). For \(a\in c_0\), disjointness makes \(\sum_n a_nh_n\) uniformly convergent with norm exactly \(\|a\|_\infty\) and preserves absolute values. For \(f\in I_F\), continuity at \(p\in F\) gives \(f(x_n)\to0\). Thus synthesis and evaluation are contractive lattice homomorphisms whose composition is \(\operatorname{id}_{c_0}\).

Second, arXiv:2604.10624v1, Proposition 2.6 says that a contractive lattice retract of a semiprojective Banach lattice is semiprojective, while Corollary 5.8 says \(c_0\) is not semiprojective. Therefore every \(I_F\) with nonclosed support is non-semiprojective.

Third, if \(U\) is clopen, restriction and extension by zero give a lattice isometric isomorphism \(I_F\cong C(U)\). Theorem A of the same source says that for compact metric \(U\), \(C(U)\) is semiprojective exactly when \(U\) is an absolute neighbourhood retract. The zero ideal is semiprojective trivially.

The standard closed-ideal correspondence in \(C(X)\) is also checked directly: for a closed ideal \(J\), the common zero set \(F\) gives \(J\subseteq I_F\), and a finite positive lattice supremum plus clipping approximates every \(f\in I_F\) by members of \(J\).

No numerical computation, finite enumeration, or unproved limiting heuristic is used. The claim does not extend beyond compact metric \(X\) or beyond closed lattice ideals. No independent audit has been performed.
