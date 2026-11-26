# Independent mathematical audit

## correctness

PASS

For X=a+ts+t²r, Hasse–Taylor expansion gives output residue b and coordinates (u+αs,w+vs+βs²+αr). Jets of degrees 0, 1, 2 modulo (X−a)³ can be specified independently at each residue by CRT, since a−a′ is a unit. For q>2, 1,s,s² are independent as functions; for q=2 exactly the sum v+β remains after identifying s²=s. This gives q⁵ and 16 distinct local maps for a fixed b, respectively. The residue of an idempotent is a set retraction. On a fixed source residue α²=α. If α=1, u=0 and idempotence of translation of r forces the translation to vanish as a function. If α=0, idempotence forces the entire quadratic output g(s) to equal g(u), even in the binary case. So every occupied fiber is fixed fully or contributes one point; unused fibers choose independently among one map to each singleton and H_q to each full target. Choosing the active and full residues and their singleton values gives the rank polynomial and image-subset count; k+s(q²−1) gives the stated extrema and their coefficients. Independent direct ring multiplication and the span of monomial evaluation tables (`python3 review_checks/finite_checks.py 4`) give 1024 distinct binary functions, 35 images, and rank counts 8,16,32,8,1 at 1,2,4,5,8, verifying each fixed-image multiplicity without using the jet template as enumeration input.

## originality

PASS

The supported distinct result is the composition-idempotent image and rank enumeration and its binary multiplicity effect. Total polynomial-function counts on suitable rings already encode the numerical local-count exception; that local count alone is not new. The strongest inspected same-ring indexed results count unital algebra endomorphisms, and the broader near-ring theorem does not cover the arbitrary image subsets and multiplicities here.

## value

PASS

This is the first nilpotence length with a genuinely nonlinear local Hasse jet. An idempotent could superficially seem able to keep an intermediate-sized part of a residue fiber through the quadratic term when the linear coordinate collapses; the composition constraint rules it out. At the same time the nonlinear jet changes the retraction multiplicities, with a binary collision that affects the coefficients while leaving the admissible image sets unchanged. The complete exact image census for this natural chain-ring stage resolves both issues, not just the already-known count of all maps or an isolated binary example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
