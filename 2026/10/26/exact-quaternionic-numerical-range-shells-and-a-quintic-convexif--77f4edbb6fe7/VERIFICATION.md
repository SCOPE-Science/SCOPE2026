---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Use right unit-quaternion multiplication to make the first vector coordinate u real and nonnegative (the zero case is allowed). For the other coordinate q, put t=u^2-|q|^2 and p=2u q in real coordinates; the whole sphere t^2+|p|^2=1 is attained, including t=-1. The Hermitian off-diagonal part contributes x=2cu Re(jq)=-cp_2. The i coefficient of conjugate(q) i q is 2(q_0^2+q_1^2)-|q|^2, giving |v|^2=(d+st)^2/4+ab(p_0^2+p_1^2). Since p_3 is invisible, its square fills any sphere slack: at fixed x the feasible (t,p_0,p_1) form the closed radius-R ball with R=sqrt(1-x^2/c^2). Its connected image gives an interval. Minimizing takes p_0=p_1=0 and clips the lower endpoint at zero; maximizing takes p_0^2+p_1^2=R^2-t^2 and then t=R by convexity of the resulting quadratic and d>=0. The endpoints are L=max(0,d-sR)/2 and U=(d+sR)/2, valid also at x=±c and d=0. Quaternionic conjugation fills all imaginary directions. Concavity of U and the convex hull of each outer sphere establish the proposed convex hull. The missing section has volume 4 pi L^3/3; symmetry, the factor 1/8 from cubing L and x=c cos(theta) give the prefactor pi c s^3/3. The stated elementary antiderivative expression vanishes at zero and its derivative 3r^2+2-(r^2+2)sqrt(1-r^2)-3r arcsin(r) equals the differentiated integral. Rescaling sin(theta)=rt gives I(r)=r^5(1/20+O(r^2)); the positive integral and its monotone integrand verify strict increase of the normalized profile and the sharp coefficient pi c/(60 s^2) multiplying d^5. The zero deficit occurs exactly at d=0.

## originality

PASS

Credit the general upper-bild representation and the earlier yes/no convexity criterion. The supported distinct contribution is the exact four-dimensional convexification deficit for this family, including its normalized profile and sharp quintic onset, not a new general numerical-range representation or a new convexity criterion. No verified equivalent coverage of the quantitative result was established in the bounded search.

## value

PASS

A full-range convexity criterion is qualitative. The four-volume quantifies how much nonconvexity remains in a natural two-level family as skew anisotropy breaks the convex case. Its quintic law distinguishes the simultaneous collapse of the two cap widths and the radial cavities and gives a sharp coefficient, not just a nonconvex example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
