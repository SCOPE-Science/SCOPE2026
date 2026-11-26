# Independent mathematical audit

## correctness

PASS

For r_j=H_{j+1}/H_j, positivity forces R>max r_j and fixes each P_j=log(R/r_j) for j=0,1,2. Equating cH_0 reconstructed at the first two parasitoid updates gives exactly the displayed F=0. Either admissible root gives a positive c and P_0 and regenerates the observations, so the elimination loses no conditions. Writing L=log 2 and b=sqrt 2, the two trajectories give P_1=L/2 and 3L/2 and then P_2=L(1-1/b) and 2L(1-1/(2b)), respectively. These imply H_1=1, H_2=b and H_3=b exp(L/b) for both. At r_0=1 and r_1=b, differentiating each quotient at equality with common value K gives the derivative difference (1-K)(1/(R-1)-1/(R-b)). Since K=L at 2 and 2L at 4, the roots are simple with opposite signs. The implicit-function theorem gives locally unique branches in disjoint admissible neighborhoods; reconstruction and the invertible H_0-plus-ratios chart give openness in four real host coordinates. Nonconstancy persists because r_1 is bounded away from 1. The common r_2 cancels from the difference in P_3, leaving Lb and fifth-census log ratio L(1-b). This proves neither an exact count of all roots nor general five-census recovery. Independent bounded check: 65-digit forward iteration, centered inverse derivatives and fifth ratio agreed (/workspace/review_checks.py, aliases); the supplied script was inspected but not executed and its finite perturbations are not the openness proof.

## originality

PASS

The distinct claim is regular two-branch inversion failure for a finite exact host-only output in the fixed-searching-coefficient map. The closest checked indexed result concerns forced trajectories with model parameters fixed. General identification methods and knowledge of the forward model are not evidence of the finite inverse result. Full-text access to several plausible classical sources was limited; the decision is bounded by that evidence.

## value

PASS

The three host ratios match the number of positive unknowns after fixing the searching coefficient. Two regular inverse branches on an open set give a concrete obstruction to global recovery that parameter counting, equilibrium examples, and generic local arguments would miss. This pinpoints what four exact host observations cannot ensure, without claiming noise performance or a general result at five observations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
