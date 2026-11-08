# Independent mathematical audit

## correctness

PASS

Reconstructed universal sufficiency: equality of magnitudes on |z|=1 cancels the top Fourier coefficient in the difference on |z|=r, leaving a real trigonometric polynomial degree <=d−1. Equality at any 2d−1 distinct inner samples makes that difference identically zero. Reflection identities for the rational quotient f/g on the two circles imply R(r²z)=R(z), so rational Laurent coefficients force constant unimodular R. Sharpness: for d>=3 and any 0<r<1 choose A²=(1-r^{2d})/(r²-r^{2d−2})>0, f=1+A z^{d−1}, g=A z+z^d: identical entire outer magnitudes, inner squared-modulus difference 2A r^{d−1}(1-r²)cos((d−1)t) with exactly 2d−2 zeros. d=2 separate f=1+i c z+z² and g=1−i c z+z² give -4 c r(1-r²)sin t, d=1 reciprocal pair shows zero samples insufficient. Independently evaluated all 2d−2 zeros at r=1/2 for d=3,4,5: maximum squared-intensity residual <9e-16. Finite checks are illustrative of the exact identities.

## originality

PASS

Pohl–Li–Boche 2017 Lemma 6 and Thm 7 already prove the sufficiency count 2d−1; this is explicitly acknowledged. The novelty under assessment is a uniform sharp matching necessity for all degrees and all inner radii using low-support reciprocal pairs, which is not in the relevant primary text inspected. The two-circle uniqueness theorem (Chalendar–Partington) is also prior.

## value

PASS

Completes the exact worst-case universal sampling complexity of a natural concentric-circle polynomial phase-retrieval design; gives adversarial sample configurations with sharp number of collisions. Explicit lower bounds are useful for measurement design even when the construction is elementary, and the claim does not assert collisions for each arbitrary smaller configuration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
