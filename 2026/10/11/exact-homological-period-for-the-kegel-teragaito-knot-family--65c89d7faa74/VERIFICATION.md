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

The proof was checked at the statement level against the family theorem and the exact Alexander-polynomial factorization. The 2026 source gives the family, hyperbolicity, L-space property, unique strong inversion, and primary MSC 57K10. The supporting Alexander source gives the exact factorization used in the proof.

For \(a=4n+5\) and \(b=4n+2\), the factor \(t^a+1\) has simple roots and division by \(t+1\) removes only \(-1\). The factor \(t^b+1\) has simple roots and, because \(b\equiv2\pmod4\), division by \(t^2+1\) removes exactly \(\pm i\). A common surviving root would satisfy \(z^a=z^b=-1\), hence \(z^3=1\), which is impossible. Therefore the characteristic polynomial is squarefree.

The first factor retains \(e^{\pi i/a}\), of exact order \(2a=8n+10\), and the second retains \(e^{\pi i/b}\), of exact order \(2b=8n+4\). Since the homological action is diagonalizable, its exact order is the least common multiple of those two integers. The arithmetic reduction uses
\[
\gcd(4n+5,4n+2)=\gcd(3,4n+2),
\]
which equals \(3\) precisely for \(n\equiv1\pmod3\).

A separate symbolic sanity replay for \(1\le n\le20\) verified that the two quotient polynomials are squarefree and coprime and that the least-common-multiple formula matches the stated residue split. That bounded replay is not used as evidence for the universal quantifier; the universal proof is the symbolic argument above.

The verification does not address higher nilpotent quotients, Johnson homomorphisms, or any relation between the strong inversion and a symmetry of the pseudo-Anosov representative.
