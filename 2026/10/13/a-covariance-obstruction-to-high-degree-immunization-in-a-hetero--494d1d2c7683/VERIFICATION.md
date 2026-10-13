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
The threshold comparison is analytic.

With
\[
w_k=\phi(k)f_k'(0),
\qquad
D=(\mu+\gamma)\langle k\rangle,
\]
a profile of mean \(\bar\sigma\) has
\[
\mathcal R_0^{\mathrm{prof}}
=
\frac{\langle w\rangle-\langle\sigma w\rangle}{D},
\]
while uniform coverage of the same mean has
\[
\mathcal R_0^{\mathrm U}
=
\frac{(1-\bar\sigma)\langle w\rangle}{D}.
\]
Thus
\[
\mathcal R_0^{\mathrm{prof}}-\mathcal R_0^{\mathrm U}
=-\frac{\operatorname{Cov}_P(\sigma,w)}{D}.
\]

The bundled checker uses exact rational arithmetic for the witness and verifies
\[
\mathcal R_0=\frac54,
\qquad
\operatorname{Cov}_P(\sigma,w)=-\frac3{40},
\qquad
\mathcal R_0^{\mathrm U}=\frac{15}{16},
\qquad
\mathcal R_0^{\mathrm T}=\frac98.
\]
It also checks
\[
\mathcal R_0^{\mathrm T}-\mathcal R_0^{\mathrm U}=\frac3{16}
=-\frac{-3/40}{2/5}.
\]

The derivatives of the chosen infection-rate functions are explicit rational functions with the required signs for every nonnegative infection pressure, so no finite experiment is used as a substitute for the general hypothesis check.
