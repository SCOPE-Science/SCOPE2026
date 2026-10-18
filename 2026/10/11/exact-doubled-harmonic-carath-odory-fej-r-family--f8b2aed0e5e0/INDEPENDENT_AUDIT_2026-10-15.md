# Independent mathematical audit

## correctness

PASS

The support is continuous circle, real even, constant term 1. Evaluating any feasible 1+a cos(t)+b cos(mt)+c cos(2mt) at t=pi and t=pi-2pi/(3m) cancels b,c after weighting 1+2, so a<=3/(1+2u), u=cos(2pi/(3m)). In the construction, after t=pi-phi and y=cos(m phi), one has cos((arccos y)/m)>=cos(phi) for phi in [0,pi], so P>=R(y)-g(y) where g(y)=A cos(arccos(y)/m) and R(y)=1-C+B y+2C y². Exact coefficient identities B+C=A-1 and B-2C=q force R(1)=g(1), R(-1/2)=g(-1/2) and R'(-1/2)=g'(-1/2). For alpha=1/m in (0,1), every nonconstant coefficient of the hypergeometric expansion of cos(alpha arccos y) in (1-y)/2 is negative; applying three y-derivatives gives third_derivative_g(y)>0 on (-1,1), including one-sided continuous endpoints. Therefore the quadratic Hermite remainder g-R=(third_derivative_g(xi)/6)(y-1)(y+1/2)^2<=0, proving circle nonnegativity. Equality in the dual bound forces vanishing at both contacts and zero derivative at the interior contact, giving unique B,C by two independent linear equations. Independently checked cancellation, contacts and positivity across 20,001 points for m=2,3,4,7,13,35; sampling corroborates but cannot prove the all-m Hermite argument.

## originality

PASS

The full infinite m>=2 doubled-harmonic family and unique Hermite-contact extremizer survive mathematical implication comparison; m=2 is covered prior and explicitly excluded as standalone novelty. No identified general reduction computes the family closed form.

## value

PASS

A natural sparse positive-definite extremal family is solved for every m with a sharp analytic closed form and a unique extremizer. The dual two-contact certificate and Hermite majorization give a reusable structural method and a sharp coefficient for infinitely many distinct supports, a motivated extension beyond prior isolated m=2 and qualitative augmentation. Neither a textbook coefficient exercise nor a random finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
