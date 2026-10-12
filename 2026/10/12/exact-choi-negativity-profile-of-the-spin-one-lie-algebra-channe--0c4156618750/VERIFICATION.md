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

The replay file `verify_choi_negativity.py` uses only Python's standard-library exact rational arithmetic.

It constructs the normalized Choi matrix directly from
\[
\mathcal E_p(|i\rangle\langle j|)
=(1-p)|i\rangle\langle j|
+\frac p2\left(\delta_{ij}I-|j\rangle\langle i|\right),
\]
performs the second-subsystem partial transpose, and checks coefficient-by-coefficient in the affine variable \(p\) that
\[
J_p^{T_2}=\frac{1-p}{3}F+\frac p6(I-3P_\Phi).
\]

It then verifies that
\[
\frac{I-F}{2},
\qquad
P_\Phi,
\qquad
\frac{I+F}{2}-P_\Phi
\]
are mutually orthogonal projectors of ranks \(3\), \(1\), and \(5\), and verifies the exact spectral reconstruction with eigenvalues
\[
\frac{3p-2}{6},
\qquad
\frac{1-2p}{3},
\qquad
\frac{2-p}{6}.
\]

Finally, it checks the piecewise negativity at rational points in every sign regime and the values
\[
\mathcal N(J_0)=1,
\quad
\mathcal N(J_{1/2})=\frac14,
\quad
\mathcal N(J_{2/3})=\frac19,
\quad
\mathcal N(J_1)=\frac13.
\]
The replay output is stored in `verification_output.txt` and begins with `VERIFY_OK`.

The finite rational test points do not establish the continuum theorem by themselves; the continuum claim follows from the exact projector decomposition and affine sign analysis.

No independent audit has been performed.
