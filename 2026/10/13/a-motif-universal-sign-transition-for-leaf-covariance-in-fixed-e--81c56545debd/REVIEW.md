# Independent mathematical audit

## correctness

PASS

Let n>=h+1, N=C(n,2), B=C(n-1,2), and H be a fixed non-induced h-vertex e-edge graph with minimum degree >=2. In G(n,m), if a specified vertex has degree one then no copy of H uses it; the induced nonincident edge set is uniformly G(n-1,m-1). By exact factorial moments, E X_H=(n)_h/aut(H)*(m)_e/(N)_e, and conditional E X_H=(n-1)_h/aut(H)*(m-1)_e/(B)_e. Combining the sum of leaf indicators and the unconditional motif mean yields Cov(L,X_H)=E L E X_H[(n-h)/n*(N)_e/(B)_e*(1-e/m)-1] for e<=m<=B+1, with zero covariance outside that range. Let R=(n-h)/n*(N)_e/(B)_e. The bracket is strictly increasing with m; if R<=1 all nondegenerate covariances are negative, while if R>1 the exact real sign cutoff is eR/(R-1) (with feasibility intersections taken). For fixed h,e and m/n->c>0 the normalized coefficient tends to 2c*exp(-2c)*(2e-h-e/c); for H=K_3 the cutoff is strictly between n and n+1 for n>=5, with n=4 real cutoff 15/4. G(n,p) instead has Cov=-(h/n)E L E X_H, always nonpositive. An independent exhaustive calculation of all G(n,m) through n=6 for triangles exactly matched the proposed rational identity; unrestricted result follows from the conditional hypergeometric argument, not the enumeration.

## originality

PASS

Goldstein’s full 2013 article proves degree-count Gaussian approximations for G(n,p), not mixed leaf/motif covariance in G(n,m). Stark–Wormald’s full 2016/2021 work gives subgraph-cluster expansions and standard fixed-edge motif counts, but does not state the exact degree-one/motif covariance or its parameter-only sign transition. The conditional-moment identity uses classic counting and is not advertised as novel by itself; the claim is the complete sharp sign classification, including positive fixed-edge covariance for triangles above n edges versus always-negative binomial-model covariance. Inspected relevant original sources and searched natural aliases leaf count/degree-one, triangle covariance, G(n,m) factorial moments. Classical graph-statistics formulae could imply this with one conditional calculation; originality remains qualified rather than asserted absolutely.

## value

PASS

Degree-one counts measure pendant structure while H with min degree two measures cycles or dense motifs. Holding total edges fixed couples these statistics and produces a sharp positive/negative transition that is absent in G(n,p). The exact threshold depends only on motif vertices and edges, not detailed topology, and the triangle integer transition occurs precisely between m=n and m=n+1 for every n>=5. This is an interpretable, structurally universal covariance law for natural random-graph statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
