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

The proof has two logically separate inputs.

First, the geometric input is the published one-step mutation criterion for well-formed weighted projective planes. For \(\mathbb P(1,a,b)\), the only possible strict height decrease is the mutation replacing \(b\), and it exists exactly when \(b\mid(a+1)^2\). Its new weight is \((a+1)^2/b\), so strict decrease is equivalent to \(b>a+1\). The published unique-minimal-weight tree property then converts this one-step criterion into height-minimality.

Second, the arithmetic count is exact: with \(n=a+1\), every exceptional pair corresponds to a divisor \(d\mid n^2\) with \(n<d\le N\). Pairing \(d\) with \(m=n^2/d\) gives \(md\) square and \(m<d\). Writing the common squarefree part as \(s\) gives the unique representation \(m=sv^2\), \(d=su^2\), and hence the binomial sum over \(1\le v<u\le\lfloor\sqrt{N/s}\rfloor\).

`verify.py` checks these equivalences with exact integer arithmetic. It compares direct mutation enumeration, the divisor formulation, and the squarefree formula for every \(2\le N<80\) and for \(N=100,200,500\). It also directly tests every allowed coordinate mutation for well-formed \(\mathbb P(1,a,b)\) with \(b<120\), confirming that the stated condition is exactly the condition for a strict height decrease.

The script's bounded checks do not prove the asymptotic. The infinite proof uses the displayed bijection together with the classical estimates
\[
\sum_{s\le N}\frac{\mu^2(s)}s=\frac6{\pi^2}\log N+O(1)
\]
and
\[
\sum_{m\le N}\varphi(m)=\frac3{\pi^2}N^2+O(N\log N).
\]
No independent audit has been performed.
