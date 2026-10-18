# Independent mathematical audit

## correctness

PASS

For alpha,theta,lambda>0 published S=(2^alpha-(2-v)^alpha)/(2^alpha-1), v=(lambda/(lambda+x))^theta. Taylor expansion at v=0 gives S=C_alpha v[1-(alpha-1)v/4+O(v^2)], C_alpha=alpha*2^(alpha-1)/(2^alpha-1)>0. Hence density ~C_alpha theta lambda^theta x^(-theta-1) and h~theta/x. Tail integration E X^q=q int x^(q-1)S dx gives finite moments iff 0<q<theta (near zero density finite). For truncated q=theta leading theta*C_alpha*lambda^theta logR, q>theta leading theta*C_alpha*lambda^theta R^(q-theta)/(q-theta), including subtraction of R^q S(R) in the integration-by-parts identity. Positive-t e^(tX) dominates the power density, hence MGF diverges on every right neighborhood of zero; negative-t Laplace transform finite. Analytic continuation of beta expressions is not a probabilistic moment. Independently checked leading and second expansion and inspected source script, not finite sampling as proof.

## originality

PASS

The source 2026 AIMS Mathematics article Kalt et al includes beta-formula moments and an MGF section, but does not impose the parameter-dependent convergence cutoff; its derivation uses r=-t and evaluates a Laplace-side integral, not an ordinary positive-t MGF. The classical Lomax power-tail and general alpha-power transforms are older. Originality is confined to correcting exactly the APIILx source interpretation with explicit constants, moment cutoff, critical/truncated rates, and MGF-domain correction; these precise combined source corrections were not located in Resultary or examined original paper.

## value

PASS

The new distribution is used for applications and moment-based statistical descriptions; knowing which mean, variance, higher moments and purported MGF genuinely exist is necessary for valid inference and interpretation. This source-specific correction has a substantive consequence (entire parameter regions have infinite mean/variance) beyond an incidental Taylor expansion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
