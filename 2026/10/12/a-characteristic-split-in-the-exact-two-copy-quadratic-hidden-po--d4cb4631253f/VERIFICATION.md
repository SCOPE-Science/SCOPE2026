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

The analytic check uses the source's exact success expression for degree two,
\[
P_q=q^{-6}\sum_{(x,y)\in X_{\rm good}}\left(\sum_{(v,w):\eta^{x,y}_{v,w}>0}\sqrt{\eta^{x,y}_{v,w}}\right)^2.
\]
For every good \((x,y)\), the identity
\[
(x+y)w-v^2=xy(b-c)^2
\]
was re-derived directly.  The reconstruction formulas show that the fiber size is completely determined by whether the right-hand side is zero, a nonzero square, or a nonsquare in odd characteristic; in characteristic two the Frobenius square map is bijective.

`verify.py` independently enumerates representative fields.  It checks the odd-characteristic distribution over \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), \(\mathbb F_{11}\), \(\mathbb F_{13}\), and \(\mathbb F_9\), and verifies that every generic fiber is a singleton over \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_{16}\).  It then evaluates the closed formulas against the direct success sum.

The finite enumerations are not used as an infinite proof.  The claim is limited to the specified two-copy degree-two approximative measurement and does not establish optimality among measurements or algorithms.
