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

For \(P_7=\operatorname{GAlex}(\Gamma,	heta)\) with \(\Gamma=Q_8	imes C_7\), the exact right-translation formula is
\[
S_y=R_{	heta(y)^{-1}y}	heta.
\]
The source proves that the displacement elements \(	heta(y)^{-1}y\) generate all of \(\Gamma\). Hence
\[
\operatorname{Inn}(P_7)=R_\Gammatimes\langle	hetaangle
\]
and has order \(56\cdot6=336\). Because the order-three and order-two pieces of \(	heta\) act on separate factors,
\[
\operatorname{Inn}(P_7)\cong T^*	imes D_{14}.
\]

The source's geometric orbit group has a lift \(f\) with \(f^6=-1\), so \(f\) has order \(12\). The split product \(T^*	imes D_{14}\) has no element of order \(12\), proving nonisomorphism.

The bundled exact verifier constructs the complete right-translation permutation group on all \(56\) elements and independently constructs the two order-\(336\) abstract groups. It prints:

`VERIFY_OK quandle_size=56 inn_order=336 displacement_order=56 identity_stabilizer=6 inn_order12=0 lambda_order=336 lambda_order12=112 f_order=12`

The enumeration is exhaustive over finite groups and is used as an independent check of the symbolic proof.

The independent-audit channel has not been performed.
