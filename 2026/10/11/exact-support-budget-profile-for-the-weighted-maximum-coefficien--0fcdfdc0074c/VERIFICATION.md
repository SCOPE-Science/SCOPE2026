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

The proof uses two exact published premises from arXiv:2610.01500v1. For every \(|\alpha|=m\),
\[
|a_\alpha|
\le
\left(\frac{m^m}{\alpha^\alpha}\right)^{1/p}\|P\|_p,
\]
and for every \(\|u\|_t\le1\),
\[
|u^\alpha|
\le
\left(\frac{\alpha^\alpha}{m^m}\right)^{1/t}.
\]
Their product gives the exact patternwise upper bound
\[
|a_\alpha u^\alpha|
\le
\left(\frac{m^m}{\alpha^\alpha}\right)^{1/p-1/t}\|P\|_p.
\]

If \(u^\alpha\neq0\) and \(\#\operatorname{supp}u\le s\), then \(\#\operatorname{supp}\alpha\le k=\min\{s,m\}\). For \(p<t\), minimizing \(\alpha^\alpha\) under this constraint uses exactly \(k\) positive parts: any part \(a\ge2\) can be split into \(a-1\) and \(1\), strictly decreasing the powered product. Among \(k\) parts, strict convexity of \(x\log x\) shows that any gap of at least two can be smoothed to reduce the product. Thus the unique exponent multiset at the minimum is
\[
\underbrace{q,\ldots,q}_{k-r\text{ times}},
\underbrace{q+1,\ldots,q+1}_{r\text{ times}},
\qquad m=kq+r.
\]
This gives
\[
\min\alpha^\alpha=q^{q(k-r)}(q+1)^{(q+1)r}.
\]

Sharpness is exact, not numerical. Taking the corresponding monomial \(P(z)=z^{\alpha^*}\) and its norming \(\ell_t\)-vector gives equality in both published premises simultaneously. When \(t\le p\), the pattern exponent is nonpositive and \(m^m/\alpha^\alpha\ge1\), while the pure power gives equality at constant \(1\).

Checks at the boundaries agree with the theorem: \(s=1\) gives \(1\); \(s\ge m\) gives the published unrestricted constant; \(p=t\) gives \(1\); and \(t=\infty\) is covered by \(1/\infty=0\).

No finite experiment, partial enumeration, or timeout is used to justify the all-dimensional statement. No converse or finite-exponent weighted Hardy--Littlewood theorem is claimed beyond the stated maximum endpoint.
