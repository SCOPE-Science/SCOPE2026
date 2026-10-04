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

The theorem is proved analytically; the finite checker is only a replay aid.

For a cyclically ordered quadruple with positive gap counts \(a,b,c,d\), the diagonal pair-sum exceeds the two side-pair sums by
\[
8R\cos\!\left(\frac{A-C}{2}\right)\sin\!\left(\frac B2\right)\sin\!\left(\frac D2\right)
\]
and
\[
8R\cos\!\left(\frac{B-D}{2}\right)\sin\!\left(\frac A2\right)\sin\!\left(\frac C2\right),
\]
respectively. Therefore the quartet contribution is half the smaller of these two differences.

Writing \(p=a+c\), \(q=n-p\), and \(h=\pi/(2n)\), balancing the integer splits gives the upper bound
\[
U_n(p)=
4R\cos(\varepsilon_q h)
\sin\!\left(\left\lfloor\frac p2\right\rfloor h\right)
\sin\!\left(\left\lceil\frac p2\right\rceil h\right).
\]
The consecutive-step identities
\[
\cos h\,\sin((m+1)h)-\sin(mh)=\sin h\,\cos((m+1)h)
\]
and
\[
\sin((m+1)h)-\cos h\,\sin(mh)=\sin h\,\cos(mh)
\]
show that \(U_n(p)\) increases strictly until \(p=\lfloor n/2\rfloor\). Balanced gap patterns at that endpoint attain the bound, yielding the four residue-class formulas.

The embedded `verify.py` was replayed from its actual package path before packaging. It enumerates every four-subset for every \(4\le n\le60\), compares the brute-force maximum with the closed formula, and checks the balanced witness. Its output was:

`VERIFY_OK n=4..60`

Finite enumeration is not used as evidence for the all-\(n\) step. No numerical tolerance enters the symbolic proof.
