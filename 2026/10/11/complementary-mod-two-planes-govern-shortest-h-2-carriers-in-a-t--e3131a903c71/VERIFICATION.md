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

`verify.py` embeds all \(90\) four-simplices and uses only the Python standard library.

It reconstructs
\[
f=(12,63,192,225,90).
\]
Unimodular reduction of
\[
\partial_2:C_2\to C_1
\]
has rank \(52\) and leaves a primitive rank-\(140\) integral cycle lattice. Expressing
\[
\partial_3:C_3\to\ker\partial_2
\]
in that basis and reducing again gives a primitive rank-\(136\) boundary lattice. Thus
\[
H_2(K;\mathbb Z)\cong\mathbb Z^4.
\]

All \(495\) four-vertex subsets are checked. Exactly \(153\) are induced tetrahedral boundaries rather than tetrahedra, and every one has a nonzero primitive integral coordinate vector.

Up to sign, the \(153\) integral coordinates form \(12\) classes: nine with multiplicity \(16\) and three with multiplicity \(3\).

With the displayed integral basis, reduction modulo two yields complementary planes
\[
U=\langle e_2+e_3,e_2+e_4\rangle,\qquad
W=\langle e_2+e_3+e_4,e_1+e_3\rangle.
\]
The verifier checks \(U\cap W=0\), all three nonzero \(U\)-classes have multiplicity \(3\), all three nonzero \(W\)-classes have multiplicity \(0\), and all nine mixed classes have multiplicity \(16\). It also checks that each represented mod-two class has a unique integral sign-class among the minimum carriers.

Exact successful output:

`VERIFY_OK f=12,63,192,225,90 H2_Z=Z^4 min_vertex_support=4 carriers4=153 all_primitive=yes integral_classes_up_to_sign=12 integral_multiplicities=16x9+3x3 mod2_carried_classes=12 mod2_missing_classes=3 planes=U+W_direct_sum=yes multiplicity_rule=U_nonzero:3|W_nonzero:0|mixed:16`
