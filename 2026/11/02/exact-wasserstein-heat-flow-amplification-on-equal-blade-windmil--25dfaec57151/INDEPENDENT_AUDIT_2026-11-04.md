# Independent mathematical audit

## correctness

PASS

The Laplacian decomposes into constants, block-average contrasts with eigenvalue 1, within-block contrasts with eigenvalue m+1, and a radial hub eigenvalue rm+1, accounting for all 1+rm dimensions including m=1. The evolved signed hub-minus-leaf distribution is explicit; for any other leaf in the chosen blade its signed mass is nonpositive because rz-(r-1)-z^r<=0 for z=e^-mt in [0,1]. All positive mass lies at hub and other blades, and all negative mass in chosen blade, producing a transport of cost C(t) using distances 1 and 2. A 1-Lipschitz potential 0/1/2 for chosen blade/hub/other blades attains the exact dual lower bound. Every graph edge is either hub-leaf or within-blade; a within-blade difference decays e^{-(m+1)t}, no larger than C(t). Thus exact global W1 norm follows for arbitrary input measures. Derivative of two-exponential expression proves unique maximum if m(r-2)>1 and strict contraction otherwise; graph spectral gap 1. Independent graph-built Q, scipy expm and LP W1 for r=2..5,m=1..3 and four times yielded 48 independent correct hub-edge and within-blade comparisons. This is a general all-integer/time proof plus finite corroboration.

## originality

PASS

Kooij 2019 Theorem 8 gives Laplacian eigenvalues on generalized windmills, explicitly credited; it does not study W1 heat transport operator norms. Münch–Wojciechowski provides the general equivalence between curvature and heat Lipschitz behavior, but no exact windmill all-time formula or phase transition. Degree-normalized Lin–Lu–Yau curvature on friendship graphs uses a different operator. The exact full semigroup norm and sharp threshold survive comparison.

## value

PASS

This exact graph-family W1 norm has transient >1 amplification in finite, reversible, spectrally-gapped networks; the sharp r,m phase classification and explicit peak provide a natural transport counterexample/benchmark for curvature and mixing theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
