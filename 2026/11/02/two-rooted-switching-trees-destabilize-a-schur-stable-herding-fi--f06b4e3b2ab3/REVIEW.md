# Independent mathematical audit

## correctness

PASS

With U=B e^T, the two frozen modes are block triangular with two copies of A on the diagonal. Independently checked the characteristic cubic and the Schur reduction: |c|=1/16, the reduced quadratic has leading coefficient 255 before dividing by 256, and the three strict quadratic conditions reduce to 135-16 beta>0, 272 beta>0 and 750-240 beta>0. Thus each frozen mode is Schur throughout 0<beta<25/8. Swapping the follower blocks gives K with block rows (U,A) and (A,0); P=K^2. Eliminating the identity block from I±K gives the four-dimensional determinants det(I-A^2±U). Exact rational-polynomial reconstruction gives beta(75-32 beta)/64 and beta(225-64 beta)/64 for I-K and I+K respectively. Their product at beta=3 is -6237/4096. On the full asserted open interval the product is negative, so the real monic characteristic polynomial of P has a real root greater than one. At beta=75/32 the product vanishes, the characteristic derivative in the multiplier is nonzero there, and the parameter derivative of det(I-P) is negative; this also checks a transverse crossing of a simple multiplier. An initial real eigenvector gives exponential two-step state growth. Nothing in this calculation certifies the schedule under endogenous predecessor selection.

## originality

PASS

The PAT equations and the single-filter Schur upper endpoint are already known, and so are Floquet methods and generic switching instability. The supported distinct claim is the exact positive-multiplier instability window and monodromy factorization for the two prescribed PAT trees, in particular the lower endpoint 75/32, not a new single-filter theorem or a counterexample to distance-selected herding.

## value

PASS

Two followers are the first setting in which these distinct rooted predecessor chains can alternate. The explicit open interval and simple unit multiplier show precisely how an unrestricted-history stability assertion can fail even under rootedness at every step, with a stationary leader and individually Schur filters. This is a useful model-specific obstruction, not merely an instance of generic switching instability chosen without motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
