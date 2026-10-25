# Independent mathematical audit

## correctness

PASS

For nonzero p,q>=0 with m>=3 and exactly one additive merge of coordinates 1 and 2, break into merged-part lengths a,b and remaining lengths r,s; d=inner merged pieces<=ab, e=outside inner product<=rs. Since merge norms M_pM_q>= original norms L_pL_q, the coefficient of e in O_before-O_after is nonnegative, justifying replacing e by rs for an upper bound; replacing d by ab also upper bounds. Angles alpha,beta of original split and alpha’,beta’ of merged split obey f(alpha)<=alpha’<=alpha, f(beta)<=beta’<=beta with f(x)=atan(tan(x)/sqrt 2). The decrease is bounded by cos(alpha-beta)-cos(alpha-f(beta))<=sin(beta)-sin f(beta); calculus of g(t)=t/sqrt(1+t²)-t/sqrt(2+t²) gives sole maximum K=(1-2^(-1/3))sqrt(2-2^(2/3))=0.1325141267187. Explicit p=(0,0,1), q=(1,1,sqrt(2s)), s=(2-2^(2/3))/(2^(2/3)-1) attains K; other coordinates zeros. Disjoint merged supports can increase O by 1. Schoener overlap cannot decrease by triangle inequality after unit-sum normalization. Independent integer-grid 3-bin checks and direct constant arithmetic corroborated; real-domain assertion is analytic.

## originality

PASS

Pianka 1973 invented the normalized cosine index; resolution sensitivity and compositional index alternatives are known in Hurlbert/Abrams and Pierotti et al. The scientific claim is a new one-merge dimension-independent sharp downward constant and explicit saturating example, not discovery of sensitivity. Pierotti et al. use compositional perturbations and subcomposition; no full-text theorem inspected applies to this cosine pooling map. Cross-disciplinary cosine-angle matrix-distortion literature could imply it and is the primary originality risk.

## value

PASS

Pooling diet or habitat-use bins is a standard resolution choice; the exact worst-case loss of a widely used ecological overlap coefficient is a natural calibration invariant. Sharp one-sided 0.1325 loss versus possible +1 rise, together with the Schoener monotonic contrast, quantifies practical index dependence on taxonomy without claiming competition dynamics or sampling interpretation. m>=3 and all other bins arbitrary make it a meaningful universal result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
