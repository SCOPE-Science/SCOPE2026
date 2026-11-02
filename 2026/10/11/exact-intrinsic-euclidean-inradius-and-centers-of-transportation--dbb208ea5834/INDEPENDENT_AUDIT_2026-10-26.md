# Independent mathematical audit

## correctness

PASS

For all integers m,n>=2 and strictly positive real margins of common total N, the strictly positive rank-one table r_i c_j/N proves the row/column affine hull has translation space L={H:H1=0,H^T1=0}. P_L(E_ij)=Q_ij=(e_i-1_m/m)(e_j-1_n/n)^T; direct orthogonality to row/column potentials and squared norm kappa²=(m-1)(n-1)/(mn) establish the intrinsic support-hyperplane clearance X_ij/kappa. For a ball B_L(X,rho) contained in all halfspaces X_ij>=0, necessarily rho<=X_ij/kappa for each (i,j), and these inequalities are jointly sufficient; this remains valid even when an individual coordinate inequality is redundant as a facet. Thus radius at X is min X_ij/kappa. If min X_ij>=t, row sums imply t<=min_i r_i/n and column sums t<=min_j c_j/m. Conversely residual margins r_i-nt,c_j-mt are nonnegative and equal-total; outer product Y_ij=r_i^prime c_j^prime/S for S>0, or Y=0 for S=0, yields feasible X=tJ+Y with floor t. At t=t*=min of those two bounds, all optimizing centers are exactly t*J+T(r-nt*1,c-mt*1), including forced-zero residual rows or columns. For dxd Birkhoff margins all one, t*=1/d, kappa=(d-1)/d, rho=1/(d-1) and residual set {0}, so unique center J/d. Independent check used exact rational projections for all i,j with 2<=m,n<=9 (1936 cases), and independent scipy.linprog max-inball LP for 200 positive-margin matrices with 2<=m,n<=6, validating exact formula (numerical LP tolerance). Separately exact counterexamples for d=3..8 locate Birkhoff boundary matrices at rho=1/(d-1), disproving the larger 2017 reported number. Finite tests corroborate, not replace, the all-parameter proof.

## originality

PASS

Qualified best-of-knowledge PASS after primary full-text mathematical implication comparisons and three targeted published-finding searches. Found explicit antecedent Collins et al. (2017) that names exactly the Birkhoff insphere but reports r=1/sqrt(d-1), false for d>=3; its chosen boundary B0=(J-I)/(d-1) is not nearest to uniform J/d. The correct Birkhoff special case is therefore not covered by that numerically conflicting statement. Bauschke–Singh–Wang establish an affine projector; Bouthat et al. calculate smallest enclosing balls; Blanchard–De Loera–Louveaux calculate combinatorial monotone paths. Published same-transportation Minkowski centers use a different asymmetry objective; partial assignment incenters exclude the Birkhoff endpoint. No independently verified prior theorem was found directly implying arbitrary positive-margin Frobenius inradius together with the full optimizing center locus. Residual priority risk persists for unindexed older operations-research work or exact formulas presented without inradius vocabulary. The discovery of the wrong earlier Birkhoff inradius expression merits explicit correction in any eventual scientific publication.

## value

PASS

Positive-margin transportation polytopes are a canonical matrix-feasibility/optimal-transport family, and the intrinsic Frobenius inball describes sharp uniform robustness of nonnegative feasible tables under perturbations respecting both sets of margins. The result determines that quantity for every positive real margin list and all m,n>=2 by a simple minimum-normalized-margin bottleneck, and classifies the entire (possibly positive-dimensional) optimizer set as one residual transportation polytope. The full center-locus description is nontrivial and directly useful for selecting robust feasible tables; no unrelated downstream theorem is required. The explicit Birkhoff specialization also resolves an erroneous numerical inradius in a 2017 primary convex-geometry study (whose choice of boundary point was not closest). The proof is elementary once the projected normals and complete support are recognized; that limits depth but does not turn this all-parameter natural exact classification into an arbitrary slice or merely a verifier output.

The dated certificate retains the supplied scientific assessment, sources and limitations.
