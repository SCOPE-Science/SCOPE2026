# Independent mathematical audit

## correctness

PASS

Read the source APAPC Algorithm 1 and derive the stated exact fixed-a proximal predictor, dual proximal update, and corrector for f=0, g(x)=mu||x||²/2, h(w)=lambda||w||²/2. Orthogonal singular vectors of K decouple independent 2x2 modes; unmatched null directions contract with r=(1+a gamma mu)^(-1) and d=(1+tau/(a lambda))^(-1). For each singular s, m=gamma tau s², the direct update gives trace r+d-dmr(1+r) and determinant rd(1-mr). Independently reconstructed updates for 144 rational cases. Strict quadratic Schur inequalities reduce to two automatically positive expressions (1-r)(1-d)+dmr and 1-rd+dmr², plus (1+r)(1+d)-dmr(1+2r)>0, equivalent to the stated threshold at the largest singular value. At equality p(-1)=0 and beyond the top mode has a root<-1; permitted scalar initializations witness nonconvergence/divergence. Averaged auxiliary iterates contract since 1-1/a<1. Rewriting in tau yields a precise all-finite-steps phase for gamma||K||²<=B/(a lambda), with B=(1+a gamma mu)(2+a gamma mu)/(3+a gamma mu). No nonzero smooth term, varying a, or nonlinear penalty is covered.

## originality

PASS

Best-of-knowledge new statement/implication after source-specific primary comparison and targeted published-record searches; residual priority and access risks are itemized below.

## value

PASS

A sharp necessary-and-sufficient dual-step stability boundary for a meaningful strictly curved APAPC benchmark exposes an all-finite-dual-steps regime that the source generic Lyapunov condition cannot certify. The exact singular-mode obstruction identifies a precise mechanism for failure at equality; this is useful beyond a routine restatement of a sufficient general-convex step restriction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
