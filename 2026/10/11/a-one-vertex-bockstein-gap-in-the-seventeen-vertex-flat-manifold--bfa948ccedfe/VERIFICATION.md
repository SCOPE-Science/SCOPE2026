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

`verify.py` uses only the Python standard library and reads the included scientific certificates `integral_certificate.json` and `carrier_census.json`.

For integral \(H_2\), it checks an explicit primitive basis \(B\subset\ker\partial_2\) via
\[
\partial_2B=0,
\qquad
LB=I_{100},
\]
verifies \(\operatorname{rank}\partial_2=100\), forms \(H=L\partial_3\), and evaluates
\[
\det H=-2.
\]
Thus \(H_2(K;\mathbb Z)\cong\mathbb Z/2\).

For integral \(H_1\), it contracts the certified spanning tree and performs unimodular reduction of the facial relation matrix. The Smith data are
\[
1^{99},4,0,
\]
so \(H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/4\). Included free and mod-four cocycles are checked against all facial relations and against explicit generator cycles.

Over \(\mathbf F_2\), exact bit elimination gives a two-dimensional \(H_2\). For each nonzero class, the verifier computes the coefficient Bockstein by dividing the integral boundary of a \(0/1\) representative by two and evaluating the resulting \(1\)-cycle in the certified \(H_1\) coordinates. Exactly one nonzero class has zero Bockstein; the other two map to the order-two element of the \(\mathbb Z/4\) summand.

Every vertex subset of size at most eight is then exhaustively checked. The unique zero-Bockstein class has minimum support seven and exactly seven carriers. The other two classes have minimum support eight and carrier counts fifteen and twenty. The complete support lists are compared byte-for-byte at the data level with `carrier_census.json` after recomputation. Each seven-vertex carrier is independently verified to be an induced orientable closed surface with face vector \((7,21,14)\), hence a torus.

Exact successful output:

`VERIFY_OK f=17,117,200,100 H1_Z=Z+Z/4 H2_Z=Z/2 H2_F2_dim=2 bockstein=nonzero_classes_to_order2 integral_reduction_min_support=7 integral_reduction_carriers=7 all_integral_min_carriers_induced_tori=yes bockstein_min_supports=8,8 bockstein_carrier_counts=15,20 minimal_support_images_rank1=yes`
