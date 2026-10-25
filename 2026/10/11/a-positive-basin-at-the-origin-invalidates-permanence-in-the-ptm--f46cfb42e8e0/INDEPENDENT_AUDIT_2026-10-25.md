# Independent mathematical audit

## correctness

PASS

For the printed discrete update T=(rho1 H tanh P, rho2 H(1-tanh P), alpha0 G+alpha H+(1-alpha)P), direct differentiation at zero gives DT(0)=[[0,0,0],[rho2,0,0],[alpha,1-alpha,alpha0]], hence multipliers 0,0,alpha0 strictly inside the unit disk for 0<alpha0<1. T is C1, so the origin is locally attracting. Independently at (rho1,rho2,alpha,alpha0)=(2,1,1/2,1/2), for strictly positive V=3H+P+G<1/16, tanh P<P<1/16 gives Hprime<=H/8, Pprime<=H, Gprime=(G+H+P)/2; therefore Vprime<=15H/8+P/2+G/2<=(3/4)V. The positive cone is invariant (tanh P in (0,1), alpha0>0), so this open positive set has V_n<=(3/4)^n V_0 and all coordinates tend to zero, contradicting Theorem 1’s universal strictly positive permanence liminf. For shared H0,P0 the G difference is alpha0^n deltaG0, because the first two equations contain no G.

## originality

PASS

Best-of-knowledge source-specific correction: the exact publisher primary article states permanence for all positive solutions under rho1>1, 0<rho2<=rho1, 0<alpha0<1 but Model (9) has a locally attracting origin and an explicit strictly positive basin inside those hypotheses. Its proof’s liminf>=1 is therefore false. Material inspection of its Model (9), difference-field Jacobian, and Theorem 1, together with the 2024 same-author-family Table 2, found no correction or equivalent positive-basin result. Broader two-dimensional refuge models do not imply this printed 3D contradiction. Resultary matches the assigned public self-record, excluded as independent priority; other hits concern distinct models. Targeted erratum, exact-title/DOI and alias searches found no separate same-system correction, but absence of hits is not a novelty proof.

## value

PASS

Permanence is a substantive invariant for ecological/discrete population models: the original paper asserts a common positive asymptotic lower bound on every positive solution. This result invalidates that quantified conclusion inside the paper’s own parameter domain, with an open invariant positive basin and exact geometric convergence rather than an isolated orbit or superficial sign check. The passive third-coordinate identity also shows why varying PTM coefficients cannot rescue persistence of the first two populations in the printed model. Its significance is a precise correction to a central published theorem, not a claim of a globally classified basin or a new general local-stability theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
