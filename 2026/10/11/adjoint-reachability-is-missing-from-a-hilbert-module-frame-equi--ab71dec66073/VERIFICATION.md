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

Let
\[
\mathcal A=\mathbb C\oplus\mathbb C,\qquad
p=(1,0),\qquad
q=(0,1),
\]
and let
\[
\mathcal H=\mathcal A,\qquad
\mathcal K=\mathcal A p.
\]
With the source's left-module convention,
\[
\langle x,y\rangle_{\mathcal A}=xy^*.
\]

Define
\[
P(a)=pa.
\]
For \(k\in\mathcal K\),
\[
\langle Ph,k\rangle_{\mathcal A}
=
(ph)k^*
=
hk^*
=
\langle h,k\rangle_{\mathcal A},
\]
so \(P^*\) is the inclusion and
\[
P^*P=Q,\qquad Qh=ph.
\]

For every adjointable \(\mathcal A\)-linear
\[
T:\mathcal H\to\mathcal K,
\]
\[
TQh=T(ph)=pT(h)=T(h).
\]
Hence
\[
\langle T,P\rangle\langle P,T\rangle
=
TP^*PT^*
=
TQT^*
=
TT^*
=
\langle T,T\rangle.
\]
This verifies the Parseval operator-module frame identity exactly.

At
\[
q=(0,1)
\]
one has
\[
Pq=0,\qquad
\langle q,q\rangle_{\mathcal A}=q\ne0,
\]
so no positive scalar lower \(g\)-frame bound can hold.

Moreover, for \(k\in\mathcal K\),
\[
qT^*k=T^*(qk)=0,
\]
and therefore every \(R(T^*)\) lies in \(\mathcal A p\). This verifies the failure of the reachability step used in the source proof.

If \(e\in\mathcal K\) satisfies
\[
\langle e,e\rangle_{\mathcal A}=1_{\mathcal A},
\]
then for each \(y\in\mathcal H\),
\[
R_y(h)=\langle h,y\rangle_{\mathcal A}e
\]
has adjoint
\[
R_y^*k=\langle k,e\rangle_{\mathcal A}y
\]
and
\[
R_y^*e=y.
\]
Thus the additional unit-vector hypothesis supplies the missing representations required by the converse proof.

The preprint theorem and the published theorem were inspected in the actual source texts. No numerical approximation, finite search, or computational certificate is used.
