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

For the algebra \(e_1\cdot e_1=e_2\), write
\[
P=\begin{pmatrix}a&b\\c&d\end{pmatrix}
\]
with columns giving \(P(e_1)\) and \(P(e_2)\). Substitution into the averaging identities on the four ordered basis pairs gives
\[
b^2=0,\qquad ab=0,\qquad b(a-d)=0,\qquad a(a-d)=0.
\]
Thus over \(\mathbb C\), \(b=0\) and either \(a=0\) or \(d=a\). This is the complete operator set used in the proof.

The automorphism calculation is independent of that classification. Since \(e_2=e_1^2\), every automorphism has
\[
\phi(e_1)=\xi e_1+\nu e_2,\qquad \phi(e_2)=\xi^2e_2,
\]
with \(\xi\ne0\). Matrix conjugation then yields
\[
P_{a,c}\longmapsto P_{a,\xi c},
\qquad
Q_{c,d}\longmapsto Q_{\xi c-d\nu/\xi,d}.
\]
These formulas give the normalizations and stabilizers stated in the result.

The packaged `verify.py` uses exact rational arithmetic. It exhausts all matrices with entries in \(\{-2,-1,0,1,2\}\) and confirms that the averaging identity holds exactly when the displayed polynomial criterion holds on that grid. It then checks the candidate families, algebra automorphisms, conjugation formulas, and representative normalizations over additional exact parameter grids. The finite check is not used as a proof of the infinite statement.

Running `verify.py` produces `CHECK_OK`.
