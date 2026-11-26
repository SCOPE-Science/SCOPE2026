# Independent mathematical audit

## correctness

PASS

Applying the two Taylor-normalized differential operators to (z−conj(w))^−2 independently gives P(s)=30b²s⁴+24bvs³+6(R−b)s²−4vs+1 with s=i/(z−conj(w)). The scalar maps onto Re(s)>0 and the prefactor cannot vanish. At b=0, the nonconstant quadratic has strictly negative discriminant and its conjugate pair has real part v/(3R); R=0 gives a constant. At v=0,b≠0, the quadratic in t² has both roots positive iff u²−b≥sqrt(10/3)|b|, in which case even repeated real t-roots are excluded; otherwise the even real quartic contributes two lower-half-plane roots. For bv≠0, zero at s=iy forces y²=−1/(6b) and R=−5b/6. Thus at fixed b, counts in the connected chamber(s) reaching the origin equal the even-quartic count of two; the fixed nonzero leading coefficient precludes escape to infinity along compact parameter paths. On the b<0,v<0 exterior the coefficients and strict Hurwitz minors have the required signs, with minors 24bv(6R−b) and −96bv²(6R+5b); reflection v→−v gives four in the opposite exterior. The explicit circle factorization removes the imaginary pair and the remaining quadratic has its two roots on the side determined by the sign of v. Independent replay: python3 /workspace/review-evidence/check_frozen_math.py 5 checks the derivatives, determinants, factorization and 16 rational parameter cases by exact rectangle root count with the imaginary-axis multiplicity subtracted. This is finite corroboration, not the parameter proof. Frozen VERIFICATION.md supplies analytic identities, not a previous independent or formal certification.

## originality

PASS

Credit the entire real-first-derivative slice to the exact indexed overlap, and the two-jet face and general kernel reduction separately. The supported distinct result is the complete real-b diagram allowing complex first coefficient, notably the nonreal crossing circle, inclusive boundary counts and four-root exterior; the inspected results do not decide these claims. Indexed path dates alone were not used to infer priority.

## value

PASS

The first consecutive extension beyond the value/first-derivative problem completes the zero-free locus for all complex first coefficients and real second coefficients. It resolves an actual root-count transition, including previously unaccounted four-root chambers and the exclusion of boundary roots, rather than merely writing the already available scalar polynomial. It makes no claim for complex second coefficients or other spaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
