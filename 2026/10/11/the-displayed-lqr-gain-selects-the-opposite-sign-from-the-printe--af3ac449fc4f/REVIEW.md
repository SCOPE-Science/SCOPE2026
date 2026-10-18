# Independent mathematical audit

## correctness

PASS

Restricted precisely to Fu–Xu–Xiao's Section4 A, B=I4, Q=100I4, R=I4, and four-decimal displayed P=K, not unprinted simulation gains. Independent exact SymPy rational matrix arithmetic gives ||AᵀP+PA−P²+100I||max=1789/2000000=0.0008945, but printed-sign ||AᵀP+PA+P²−100I||max=5532161073/25000000=221.28644292. Independently reconstructed exact char polynomials for A−P and −(A+P). Each quartic has positive coefficients and positive Δ2,Δ3: 23744.94394709726 and 95105361.59314738 for A−P; 25060.094866157262 and 83523730.59155181 for −(A+P). Routh–Hurwitz proves A−P Hurwitz and A+P strictly anti-Hurwitz. Therefore literal printed negative K flips the sign of stabilization. It does not prove which feedback was used in unavailable nonlinear simulation code, nor that source plots are false. Inspected source exact Fraction and Faddeev–LeVerrier verifier blob 0490f0ef10ebd33b89148b61a1000e1dad01c9d5.

## originality

PASS

The source paper itself provides A and P and a contradictory gain formula, which is fully credited. The independently exact residual separation and Routh–Hurwitz confirmation of open-right-half-plane A+P are source-specific consequences not written in the source; a similar correction on a different oscillator would not imply these numbers. The contribution is a reproducibility/safety clarification, not a new LQR theorem. No separate public erratum for this exact matrix found in queried sources; priority risk remains.

## value

PASS

The source is a published control/synchronization calculation. The error is not a cosmetic minus sign: if a reader implements the source's printed K=−P in its own A−BK feedback formula, the reconstructed linear error dynamics has every eigenvalue in the unstable right half-plane rather than being Hurwitz. The exact four-dimensional certificate directly resolves reproducibility and potential control-system interpretation, a substantive motivation for an otherwise elementary sign check. It is not claimed as a new Riccati theorem or proof of actual hardware failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
