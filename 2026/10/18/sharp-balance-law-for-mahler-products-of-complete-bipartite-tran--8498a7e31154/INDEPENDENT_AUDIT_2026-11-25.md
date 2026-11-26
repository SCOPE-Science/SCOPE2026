# Independent mathematical audit

## correctness

PASS

The frozen mathematics checks, and the complete narrowed RESULT.md under repairs/4 has been rechecked. The primal lattice volume comes from h*(1), and the polar volume in anchored coordinates comes from the beta integral of p(p-1)r^(p-2)(2-r)^q (the anchored range CDF is p r^(p-1), and p=1 is a cube). Passing to the Euclidean zero-sum hyperplane gives reciprocal sqrt(N) factors, so its published normalized product is the same input to the repair. The baseline follows from binom(p-1,k)/(k+1)=binom(p,k+1)/p and Vandermonde. At fixed N the normalized adjacent difference has coefficient D_k, with zero baseline sum and a negative-to-positive sign pattern given by kN-p(q-1) for k<p. The endpoint coefficients D_0<0 and D_p>0 carry positive masses on both sides; their strictly separated weights s_p>s_0 prove strictness even when s_0=s_1. The repair makes this pairing justification explicit. Symmetry and transfers give precisely the stated maximizer and tied thin minima, with all splits thin for N<=5. The frozen fixed-p limit also checks by leading terms, but is not part of the distinct repaired claim. An independent rational reproduction checked 100 volume/normalization pairs through p,q<=10 and 169 fixed-order transfers through N=30, including R(3,3)=81/80 and the N=8 values. These are finite checks, not the proof. The attached verify.py was inspected, not executed; its exact rational tests and optional numerical hull tests are unchanged.

## originality

PASS

This PASS is for the narrowed fixed-order transfer theorem only. The frozen composite originality claim is not supported as stated: the distinct indexed f86fbac7ea01 demonstrably covers the polar-volume evaluation, normalized product, equality classification and fixed-part limit. Its monotonicity holds with one part fixed while the other grows, not under a transfer between parts at the same N. The strongest same-transfer comparison orders directional width, not the volume product. The repair removes standalone novelty claims for the covered results, treats them as inputs, and retains the explicit fixed-order signed-weight comparison and maximizer. The compared catalogue dates establish neither priority nor copying.

## value

PASS

The repaired statement is a strict extremal ordering over all bipartitions in each dimension, for a natural intrinsic product of primal and polar shapes. Keeping dimension fixed removes the change in normalization and pits two coordinatewise effects against one another; proving their net sign, and finding the unique maximizer and all ties, is useful beyond computing an isolated product value. It does not rank other graphs or claim a global Mahler extremum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
