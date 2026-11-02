# Independent mathematical audit

## correctness

PASS

For real symmetric A,B negative semidefinite, direct multiplication of the published PartRosExp2 formula gives LML^{-1}=exp(Y)(I-X/2)^{-1}(I+X/2). Both factors are Euclidean contractions, and equality occurs only on ker A intersect ker B, proving exact weighted power and rho<1 criterion. The fixed-B two-state family has M_t/t -> [[0,0],[1/8,0]], hence ||M_t||_2/t ->1/8 while rho(M_t)<1 for each t. At t=16 its characteristic polynomial and eigenvalues (1±sqrt57)/12 follow exactly. The reverse PartExpRos2 update is bounded by 3+h||B||_2 for fixed B using ||L^{-1}X||<=2 and ||phi_1(Y)||<=1. I independently reconstructed exact symbolic witness identities and the asymptotic limit, distinct from the assigned 450 random checks. Finite tests are not substituted for matrix proof.

## originality

PASS

Qualified best-of-knowledge PASS: Dallerit et al. introduces the methods and scalar A-stability and Achleitner et al. the generic contraction theory, but the inspected published scheme and results do not establish the combined noncommuting weighted contraction, strict common-kernel condition, fixed-B unbounded physical endpoint gain and reversed-order stiffness bound. Generic similarity phenomena are explicitly prior; mathematical implication rather than title resemblance was compared.

## value

PASS

The numerical stability of second-order partitioned integrators with noncommuting dissipative stiff components is a natural algorithm-selection problem. A sharp explicit Euclidean transient obstruction despite dissipative total generator and a norm-safe reversal identify an actionable operator-ordering boundary, beyond scalar A-stability. The exact weighted metric and all-dimensional kernel classification are structural rather than a routine parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
