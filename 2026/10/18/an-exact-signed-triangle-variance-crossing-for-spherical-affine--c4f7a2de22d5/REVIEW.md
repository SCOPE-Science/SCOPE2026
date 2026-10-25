# Independent mathematical audit

## correctness

PASS

For edges with conditional p+delta<X_i,X_j>, spherical E[X_iX_i^T]=I/d gives E[Z_triangle]=delta³/d², E[Z_triangle²]=s³+c³delta³/d², s=p(1−p),c=1−2p; all monomials of one/two unpaired dot products vanish. Distinct triangles sharing exactly one edge have covariance s delta^4/d³−delta^6/d^4; one-vertex-sharing covariances vanish by conditional rotational symmetry. Ordered shared-edge pairs number 12*C(n,4), so Var(T)=C(n,3)[s³+c³delta³/d²−delta^6/d^4]+12*C(n,4)[s delta^4/d³−delta^6/d^4]. Subtract Var_ER=C(n,3)s³ to obtain difference C(n,3)delta³/d^4*Phi_n with Phi_n=c³d²+3(n−3)s delta d−(3n−8)delta³, strictly increasing slope 3delta(sd−delta²)>0. At p=3/4,delta=1/8,d=2, exact Phi6=−25/256 and Phi7=19/512. Independent rational enumeration of latent ±coordinate axes in d=2 for n=3,4 reproduced E and Var exactly (n3 var27391/4194304; n4 var6865/262144). This discrete latent comparison matches the required moment tensors for the checked low-degree observables, not an infinite or all-n proof.

## originality

PASS

The general-kernel signed-triangle detection literature, notably Huang–Li Proposition 2.1, identifies mean and bounds variance by n^3+n^4*tau_4 and its proof gives general overlap/covariance forms. Here the complete finite-n polynomial with its negative-to-positive variance reversal for the explicit affine kernel is isolated and simplified. Best-of-knowledge passes the new finite-n sign classification, but the general covariance identity is sufficiently close to leave a serious reduction/prior-implication risk.

## value

PASS

An exact finite-sample signed-triangle noise comparison is motivated by geometric-graph detection and calibrates which graph size reduces versus increases null-comparison variability. The monotone crossing is a real parameter boundary with concrete rational witness n=6 to7, not merely an upper bound or a small numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
