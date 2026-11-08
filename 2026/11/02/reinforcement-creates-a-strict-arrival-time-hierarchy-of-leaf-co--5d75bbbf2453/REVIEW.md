# Independent mathematical audit

## correctness

PASS

The exact affine total parent weight is s_m=(1+alpha)m-alpha. With X=1{parent(m+1)=root}, Y=L_{m+1}-L_m, the root is nonleaf after time 2 and XY=X; E[X|T_m]=(1+alpha D_m)/s_m, E[Y|T_m]=1-L_m/s_m. These identities give E[L_m]=s_m/(alpha+2), r_{m+1}=r_m(1+alpha/s_m), and C_{m+1}=(1+(alpha-1)/s_m)C_m+r_m/((alpha+2)s_m). Direct induction solves C_n=[r_n-(1+alpha)h_n]/(alpha+2). Conditioning a fixed birth indicator through later leaf increments gives w_{j,n}=q_{j,n}[alpha C_{j-1}+r_{j-1}/(alpha+2)]/s_{j-1}. The algebraic difference is precisely q_{j+1,n}alpha(alpha+1)h_{j-1}/[(alpha+2)s_{j-1}s_j], positive for alpha>0 and zero for alpha=0; direct sum recovers C_n. Gamma product asymptotics hold for fixed alpha>0, with exact alpha=1 binomial expression. Independently enumerated every increasing parent history n=3..7 for alpha=0,1/2,1,2, verifying formulas, gaps and equality boundary with rational arithmetic. The universal statement follows from conditional recurrences, not the finite experiment.

## originality

PASS

Previously published uniform-attachment equal-share covariance is exactly the alpha=0 special case and is credited. Janson–Kuba–Panholzer and Mahmoud–Smythe–Szymański study affine/plane recursive trees and leaf or degree marginals. The strict all-alpha>0 age ordering of individual root-attachment versus total-leaf covariances, explicit gap and combined global covariance were not identified as consequences of the inspected marginal results; this is bounded best-of-knowledge, not priority certification.

## value

PASS

The root-degree/leaf-count dependence is natural in preferential attachment, and individual arrival epochs provide a substantive fine-grained decomposition. The exact strict phase boundary between alpha=0 equal contributions and every alpha>0 later-arrival dominance, plus closed finite-n gradients and fixed-alpha covariance growth, is a motivated structural law not implied by marginal expectations or an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
