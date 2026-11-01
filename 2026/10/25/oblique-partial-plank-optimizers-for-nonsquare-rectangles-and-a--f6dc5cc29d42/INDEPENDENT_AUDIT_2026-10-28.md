# Independent mathematical audit

## correctness

PASS

The Bakaev–Polyanskii Theorem 12 first reduces the finite-plank union problem to one strip, and the central strip is optimal by the rectangle projection density being symmetric unimodal. For n=(u,v), U=au,V=bv,w=W/2, the uncovered-area profile is exactly 4ab-4w min(a/v,b/u) on plateau w<=|U-V|, and (U+V-w)^2/(uv) on tails. Reflections and swapping favor v>=u. With q=v/u>=1, derivative of H(q)=(a+bq-w sqrt(1+q²))/sqrt(q) is proportional to T_alpha(q)-t for T_alpha=q-alpha(q²-1)/sqrt(1+q²), t=a/b. The derivative of T_alpha has at most one turn and the admissible root q>t is unique, in tail regime since D/w=(q²-1)/(q²+1)<1; it is the global optimum. The exact rational example a=2,b=1,W=sqrt(10)/4, q=3, gives area53/16. Implicit differentiation gives q increasing with W, and T_{1/sqrt2}(1+h)=1+h³/8+O(h⁴) yields q-1~2(t-1)^(1/3), one-sided. Independent substitution checked example; 500 source numerical checks are supplementary, not all-real proof. Domain excludes a=b and W>=2b.

## originality

PASS

Best-of-knowledge: The cited general existence theorem and square symmetry boundary are insufficient to imply unique q>t, area formula for all a>b, or ε^(1/3) perturbation exponent; these require the explicit slice and scalar analysis. Broader convex-body result is used as a premise. The new geometric optimization supplies a complete nonsquare rectangular family and a local singular stability law.

## value

PASS

The partial-plank reduction poses a genuine exact optimization challenge for the first basic anisotropic convex body. The theorem classifies all optimal single-strip directions over an entire two-parameter family, proves strict obliqueness and monotonicity, and identifies a nonanalytic cubic-root symmetry-breaking limit; these are motivated geometric structure, not arbitrary isolated parameter evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
