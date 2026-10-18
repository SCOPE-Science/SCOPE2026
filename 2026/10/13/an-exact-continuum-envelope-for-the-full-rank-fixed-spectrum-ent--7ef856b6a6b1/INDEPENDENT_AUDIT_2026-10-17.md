# Independent mathematical audit

## correctness

PASS

The exact continuum constraint in Camacho–de Vicente Eq. (39), after the full-rank Theorem 8 first-row reduction F12=F14=F13=0 and F11=1, gives for row two x=F22,y=F23,z=F24 the condition a²x+2a(1-a)y+(1-a)²z<=1/2 for every a in [0,1]. Writing u=1/2-x,v=1/2-z, copositivity of the homogeneous quadratic on nonnegative pairs is exactly u,v>=0 and y<=1/2+sqrt(uv), including boundary u=0 or v=0. The eigenvalue row equation then gives lambda2<=(1-lambda1)/2-lambda2*u-lambda4*v+lambda3*sqrt(uv). With r=sqrt(u),s=sqrt(v), for fixed s, optimal r=lambda3*s/(2lambda2) respects r<=1/sqrt2 because lambda3<=lambda2. Maximizing over s² in [0,1/2] gives (1-lambda1)/2+(1/2)(lambda3²/(4lambda2)-lambda4)_+. Under lambda3²<=4lambda2lambda4, the strict violation simplifies to lambda2>lambda3+lambda4; otherwise to lambda2/lambda3>(1+sqrt2)/2. Exact rational strict witness (63/100,1/5,3/20,1/50) yields upper bound 121/640 and gap 7/640; it is outside Theorem 8 regions A–C. Preconditions ensure the Bell target and MEMS are entangled. Independent rational optimization and boundary algebra passed; finite grid not mistaken for proof.

## originality

PASS

The full Camacho–de Vicente preprint provides the continuum constraints and the first-row elimination as prior art; Theorem 8 proves only three coarser analytic rank-four no-go sectors, and its numerical tests go beyond these sectors. The new closed-form max of the exact continuum row inequality yields a strictly larger analytically certified obstruction with a rational spectrum outside all three. The general two-qubit fixed-spectrum MEMS and rank-two no-go are also credited. Literature equivalence searches did not locate prior published optimization in the same parameters; this is best-of-knowledge, not a unique-priority proof.

## value

PASS

The source explicitly leaves a strict gap between its coarse analytic no-go areas and numerically infeasible full-rank spectra. This theorem replaces part of that gap with a sharp exact continuum-row necessary spectral inequality, a two-branch closed-form boundary, and an exact full-rank witness beyond all the published analytic sectors. The mathematical object and missing boundary are directly motivated, and the result is not a mere renaming of the numerical infeasibility observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
