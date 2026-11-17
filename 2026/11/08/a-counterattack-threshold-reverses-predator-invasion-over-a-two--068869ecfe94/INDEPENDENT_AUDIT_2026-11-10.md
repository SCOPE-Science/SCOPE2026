# Independent mathematical audit

## correctness

PASS

For x_{t+1}=x+(11/5)x(1−x), the two-cycle x±=(21±√21)/22 satisfies f(x−)=x+, f(x+)=x−, with scalar product derivative 4/25<1. Full three-state Jacobian over the predator-free cycle is block upper-triangular, and its two-step eigenvalues are 4/25 and the eigenvalues of P=M(x+)M(x−), M(u)=[[1/5−Au,Cu],[1/4,1/5]]. Exact symbolic multiplication, independently recomputed, yields D=det(I−P)=−504 A²/605+504 A/1375+105 C²/1936+(21 A/242−273/550)C+576/625. On C0(A)=16(A+4/5)/5, D=−48(35A−2)/15125. With each M strictly positive in the prescribed A range, P positive, P22<1, and the non-Perron eigenvalue <P22<1, sign D uniquely detects whether ρ(P)<,=,>1. Substitution of (A,C)=(1/100,13/5) and (1/10,287/100) independently gives the stated opposite strict R_static and D signs. Neutral boundary asserts no nonlinear persistence; hyperbolic local cycle stability/invasion follows from Jacobian, not numerics.

## originality

PASS

The original model source treats fixed points and coexistence bifurcations but does not assert the Floquet product invasion criterion along this *predator-free* 2-cycle, its sharp rational counterattack crossing, or the two reversed witnesses. Prior general stage-specific invasion findings concern different equations and comparisons. The specific model threshold and both directions are best-of-knowledge original, with unindexed model-analysis risk.

## value

PASS

The exact crossing and two opposite rational witnesses show that a standard static predator reproduction benchmark can misclassify invasion in *both* directions under an attracting oscillating resident prey population. This resolves a motivated model-specific dynamical boundary using exact algebra and positive-matrix Floquet theory, rather than numerical examples alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
