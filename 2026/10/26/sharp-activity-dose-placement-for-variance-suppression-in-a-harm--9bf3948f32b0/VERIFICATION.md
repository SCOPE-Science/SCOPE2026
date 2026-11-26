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

A flip at rate alpha/2 gives orientation correlation exp(-integral alpha) between two times. Extend the stationary baseline to negative times, set u=0 there, and represent X_T as the exponential convolution of the orientation. By symmetry its mean is zero. In the resulting covariance double integral over s<t<=T the integrand is 2v^2 exp(-2k(T-t)-(k+a)(t-s)) exp(-epsilon U(s,t)), where U is the integrated control from s to t. Expanding the last factor, integrating the linear term over s<=r<=t for a perturbation at r, yields exactly W(T-r), including the k=a limit. The zero-order integral is v^2/[k(k+a)]. Since 0<=U<=t-s and 0<=exp(-x)-1+x<=x^2/2 for x>=0, integrating the bound over T-t>=0 and t-s>=0 gives 0<=R<=v^2 epsilon^2/[k(k+a)^3], uniformly without assuming any smoothness of u. The difference-of-exponentials derivative has exactly one zero at the stated z_* and the resonant derivative has the sign of 1-2kz. For a threshold lambda whose superlevel set has length m, (W(T-s)-lambda)(u_star-u) is nonnegative everywhere and strictly positive where admissible controls differ off the level set. Thus the superlevel interval is the unique optimizer up to null sets. It first meets physical time zero at lag endpoints r_T,T and length m_c=T-r_T; it cannot touch physical time T for m<T because W(0)=0. Shrinking interior intervals contain the unique peak and their centers tend to T-z_*. The independent three-segment propagation matches the example: lag 0.4995912659, pulse [1.3649081504,1.6149081504], and variances 0.4996295196, 0.5036774237 and 0.5023481452 in the stated order.

## originality

PASS

The surviving contribution is model-specific: fixed stiffness, propulsion and baseline, bounded nonnegative extra tumbling of fixed integrated dose, and optimization of the terminal position variance at first order, including the lag and dose transition and the explicit uniform error. The basic trapped-particle equations, response theory and threshold allocation principle are not claimed as new. The closest inspected control studies and indexed pulse result differ in objective, control regime or dynamics and do not give this combination.

## value

PASS

At fixed added tumbling dose it is not enough to know that increased rate suppresses spread; the question is where to use that dose before a terminal measurement. The peak response occurs at a positive lag and the exact critical dose explains when front-loading loses to a delayed interior pulse. This supplies a usable schedule in a standard active-particle model, with a control-uniform variance error that makes the weak optimum informative for small positive amplitudes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
