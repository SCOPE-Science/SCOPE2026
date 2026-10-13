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
For
\[
\Lambda_\mu(k)
=
\left(
1+\frac{\mu k}{2(1+\mu)}
\right)e^{-\mu k},
\]
the PMF satisfies
\[
p_y=\Lambda_\mu(y)-\Lambda_\mu(y+1).
\]
Therefore
\[
\Pr(Y\ge k)=\Lambda_\mu(k).
\]

The corrected first two raw moments are
\[
\mathbb E[Y]
=
\frac{\phi}{1-\phi}
+
\frac{a\phi}{(1-\phi)^2},
\]
and
\[
\mathbb E[Y^2]
=
\frac{\phi(1+\phi)}{(1-\phi)^2}
+
\frac{a\phi(1+3\phi)}{(1-\phi)^3},
\]
where
\[
\phi=e^{-\mu},
\qquad
a=\frac{\mu}{2(1+\mu)}.
\]

The PGF is
\[
P(s)
=
1+(s-1)
\left[
\frac{\phi}{1-\phi s}
+
\frac{a\phi}{(1-\phi s)^2}
\right],
\]
so the MGF is finite exactly for
\[
t<\mu.
\]

The included checker compares direct PMF sums with the corrected closed forms, evaluates the source's displayed Eqs. (18), (21), and (22), reproduces selected Table 1 entries, and verifies the PMF tail ratio and MGF boundary.
