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

The claim is checked directly against the explicit probability inequalities of arXiv:2610.01555v1, Appendix C.4.

For \(d_n=2^n\) and
\[
b_n=\left\lfloor\frac{\log d_n}{4\log\log d_n}\right\rfloor,
\]
we have
\[
b_n\sim\frac{n\log2}{4\log n}.
\]
Hence
\[
\epsilon_n^2n/\log n\to\infty
\quad\Longleftrightarrow\quad
\epsilon_n^2b_n\to\infty.
\]

The published \(\tau=+1\) false-rejection bound is \(O((\epsilon_n^2b_n)^{-1})\), so it vanishes. The published alternative-hypothesis error bound is
\[
e^{-4}+\zeta_{d_n}
+\frac{32}{(d_n+1)\epsilon_n^2}
+\frac{128d_n}{(d_n-2)\epsilon_n^2b_n}.
\]
Here \(\zeta_{d_n}\to0\). The final term vanishes from \(\epsilon_n^2b_n\to\infty\). Also
\[
d_n\epsilon_n^2
=
(d_n/b_n)(\epsilon_n^2b_n)\to\infty,
\]
so the third term vanishes. Thus the base error is eventually at most \(1/3\).

The source's amplification uses independent repetitions and majority vote, giving \(O(\log(1/\delta))\) repetitions. Substitution into its base query count yields
\[
O\!\left(
\frac{2^n\log n}{\epsilon_n^2n}
\log\frac1\delta
\right).
\]
At fixed confidence, division by \(2^n\) leaves \(\log n/(\epsilon_n^2n)\to0\), proving the sub-\(2^n\) statement.

Finally, the source identity \(1-f_\tau=\Delta_\tau^2\) converts \(\epsilon_n=\Delta_n^2\) and gives the sufficient normalized Frobenius regime
\[
\Delta_n=\omega((\log n/n)^{1/4}).
\]

No finite computation, enumeration, or external certificate is used to prove the asymptotic claim. No optimality below this scale is asserted.
