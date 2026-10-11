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

Let
\\[
s_n=\\varsigma_{\\mu,n},
\\qquad
a_n=a_{\\mu,n},
\\qquad
b_n=b_{\\mu,n}.
\\]
The inspected primary theorem gives
\\[
b_n(1+s_n)=1
\\]
and
\\[
a_n^2
=
\\frac{(1+s_n)(\\mu^2-s_n^2)}{s_n}.
\\]
Therefore
\\[
1-b_n=\\frac{s_n}{1+s_n}
\\]
and multiplication yields the exact relation
\\[
a_n^2(1-b_n)=\\mu^2-s_n^2.
\\]
Since
\\[
s_n=\\frac{1-b_n}{b_n},
\\]
this is equivalently
\\[
a_n^2(1-b_n)
+
\\left(\\frac{1-b_n}{b_n}\\right)^2
=
\\mu^2.
\\]

The source proves
\\[
b_n\\to1,
\\]
so \\(s_n\\to0\\). The stationarity equation then gives
\\[
s_n=O(a_n^{-2}),
\\]
and consequently
\\[
1-b_n
=
\\frac{\\mu^2}{a_n^2}
+
O(a_n^{-6}).
\\]

The classical fixed-order cylinder zero asymptotic gives
\\[
c_{\\mu,n}=\\pi n+O(1).
\\]
Since
\\[
c_{\\mu,n}<a_n<c_{\\mu,n+1},
\\]
one has
\\[
a_n=\\pi n+O(1).
\\]
Thus
\\[
a_n^{-2}
=
(\\pi^2n^2)^{-1}+O(n^{-3}),
\\]
and hence
\\[
1-b_n
=
\\frac{\\mu^2}{\\pi^2n^2}+O(n^{-3}).
\\]

All limits are for fixed \\(\\mu>0\\) and fixed \\(\\alpha\\in[0,\\pi)\\). No numerical computation or finite enumeration is used.
