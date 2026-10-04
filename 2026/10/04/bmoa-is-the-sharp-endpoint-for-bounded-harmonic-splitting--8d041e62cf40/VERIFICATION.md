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
\[
F\in L^\infty(\mathbb T)
\]
be the radial boundary function of the bounded harmonic map
\[
f=h+\overline g,
\qquad
g(0)=0.
\]
Writing
\[
h(z)=a_0+\sum_{n\ge1}a_nz^n,
\qquad
g(z)=\sum_{n\ge1}b_nz^n,
\]
gives
\[
F(e^{it})
=
a_0+\sum_{n\ge1}a_ne^{int}
+\sum_{n\ge1}\overline{b_n}e^{-int}.
\]
Hence
\[
P_+F=h^*,
\qquad
P_+\overline F-\overline{a_0}=g^*.
\]

The classical endpoint estimate
\[
P_+:L^\infty(\mathbb T)\to\mathrm{BMO}(\mathbb T)
\]
therefore places both boundary functions in analytic BMO, with norms controlled by
\[
\|F\|_\infty\le\|f\|_\infty.
\]
The standard derivative-Carleson characterization then gives the stated interior estimate.

For sharpness, the inspected primary theorem constructs, for every
\[
0<k<1,
\]
a bounded globally one-to-one harmonic mapping satisfying
\[
|g'|\le k|h'|
\]
with unbounded \(h\). The corresponding maximal dilatation is at most
\[
(1+k)/(1-k).
\]
Given \(K>1\), take
\[
k=(K-1)/(K+1).
\]
If \(g\) were bounded, boundedness of \(f\) would force
\[
h=f-\overline g
\]
to be bounded, contradiction. Thus both components are unbounded, while the first part places both in \(\mathrm{BMOA}\).

No numerical experiment, finite truncation, or unproved endpoint limiting argument is used.
