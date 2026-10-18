# Independent mathematical audit

## correctness

PASS

Both specified scalar randomized RK2 stage formulas solve to R(z,t)=(1+(1-t)z)/(1-tz). For z=-u+iv, u>0, s=|z|², exact identity |R|²-1=[-2u+(1-2t)s]/[1+2tu+t²s]. The stiff real-axis limit is g(t)=((1-t)/t)² (infinite at t=0). Independently expanded exact supporting identity g(t)-[1-8(t-1/2)+12(t-1/2)²]=(1-t)(2t-1)²(3t+1)/t²>=0, so ET=1/2 implies lim E|R|²>=1+12Var(T), with nondegenerate obstruction; a family with small probability mass at T=1 approaches coefficient 12 proving sharpness. For T=a with probability p and T=1 otherwise, the boundary p*=[a/(1-a)]² gives after positive denominator multiplication a strictly negative polynomial for every u>0 and s>=u²; affine mixing proves sufficiency, and the stiff limit p[(1-a)/a]² proves necessity for p>p*. Inspected coefficient-level package verifier; independent SymPy factorization matches identity. These are statements of strict expected squared contraction at every finite Re z<0, not nonlinear A-stability.

## originality

PASS

Same amplification map appears in Bochacik–Przybyłowicz’s uniform stage theorem, whose failure of global mean-square A-stability does not already imply the sharp distribution-free variance penalty or nontrivial exact biased two-atom stability frontier. Other implicit randomized tableaux and stochastic-theta SDE schemes are not logically equivalent.

## value

PASS

An exact impossibility theorem for preserving midpoint stage mean plus a constructive if-and-only-if design boundary quantify a genuine numerical-analysis stability trade-off for a natural family of randomized implicit RK2 discretizations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
