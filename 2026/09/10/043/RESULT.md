# Impossibility of the published Evra-Kaufman certificate reaching h2 >= 0.08 at d=3

## Context
Target claimed h2^{cosys}(X_*;F2) >= 0.08 for the smallest connected 3-D LSV PGL4(F2((t))) quotient VIA the Evra-Kaufman Garland criterion with certified link gaps. Admission feasibility assumed EK Remark 3.4 closed forms could reach 0.08.

## Definitions
X any pure d=3 complex satisfying EK Thm 3.1 hypotheses with uniform proper-link coboundary parameter beta and degree bound Q; EK norm Def 2.1; Exp_b^0; container Gamma^1; Remark 3.4 constants C0=1/(3(d+2)2^{d+3}), C1=(d+2)2^{d+2}, bar-eps=(1/3)(beta/C1)^d, mu=(C0(beta/C1)^d)^{2^{d+1}}, eps=min{1/Q,mu}.

## Result
At d=3, C0=1/960, C1=160. Universal lemma: Exp_b^0(Y)<=2 for pure dim>=1 Y with >=2 vertices (minimum-weight singleton, Lemma 2.3 container identity), so admissible beta<=2. Hence eps_bar(beta)<=(1/3)(2/160)^3=1/1536000 approx 6.51e-07<0.08, mu(beta)<=((2/160)^3/960)^16=(1/491520000)^16<1e-139<0.08, eps<=mu<0.08. No certificate through published EK criterion can establish h2>=0.08 at d=3 for any admissible X including X_*.

## Proof / evidence
Transcription checked against EK HTML v3; singleton minimality/non-coboundary argument plus ||Gamma^1({v})||=2w(v); monotone substitution in exact Fraction arithmetic; replay output/artifacts/verify_cap.py gives VERIFY_OK.

## Limitations
Refutes only the method-specific conjunction (bound VIA published EK closed form). Bare h2(X_*;F2)>=0.08 by other routes (re-optimized EK constants, Garland-Oppenheim spectral, Dikstein-Dinur) not decided. No claim on H^2(X_*;F2) or true cosystole. 65-vertex link computation background only.

## Reproducibility
python3 output/artifacts/verify_cap.py (stdlib only) prints VERIFY_OK. Independently: (1/3)*(2/160)^3=1/1536000; ((2/160)^3/960)^16=(1/491520000)^16<1e-139.

## References
- https://arxiv.org/abs/1510.00839
- https://arxiv.org/html/1510.00839v3
- output/artifacts/verify_cap.py
