# Independent mathematical audit

## correctness

PASS

Conjugating the generalized pencil by the inverse square roots gives the stated equations. With Cz=0 in scaled coordinates the first and third equations give x*Ãx=λ(||x||²+||z||²); x=0 would force z=0 by injectivity of the scaled B transpose. Hence 0<λ<b strictly. If λ<a, eliminating x and using the inverse Loewner order gives λ≥β/(b−λ), equivalently λ(b−λ)≥β. The discriminant and lower-root cases follow only on λ<a, and the complementary branch λ≥a yields the clipping. When the root r exists, r=β/(b−r)≥β/b, which also gives the weaker universally clipped bound. To verify the full asserted attainment regime r≤a, take A=diag(a,b,b), B with rows √β e2^T and √β e3^T, C=(0,1), identity approximating blocks and any positive E; y=0,z=e1,x=−√β e2/(b−r) is an eigenvector at r by r(b−r)=β, even at r=a. In the proposed unbounded family, s²=3+6t² gives Bx=(2t²−s²/3)e1=−e1 and (A−I)x=−B^T z, so λ=1 for all t≥1. The Gram entries are 3+7t²,100t²,100t²; the first is the minimum and β/b diverges, with diagonal blocks fixed and all ranks and positivity requirements satisfied. Independent rational spot checks give β/b=10/7 and 850/7 at t=1 and t=11. These examples also satisfy the source paper's spectral-straddling normalization and avoid both diagonal spectra at λ=1.

## originality

PASS

The inspected original paper states the lower bound that the exact family violates; the clipped replacement is not its result. Closely related quadratic and cubic enclosures concern different matrix pencils, preconditioners or kernel conditions. Credit the repair of the specific spectral assertion, the unbounded fixed-spectrum failure and lower-root attainment, not the standard energy identity or inversion inequality in isolation.

## value

PASS

The claimed lower enclosure of a concrete preconditioned branch can be wrong by an arbitrarily large factor even with diagonal spectra unchanged. Pinpointing the resolvent error and replacing the false inequality with a bound valid under the actual hypotheses is useful for interpreting those spectra. Attainability makes the quadratic portion meaningful, not merely a loose rescue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
