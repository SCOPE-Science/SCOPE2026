# Independent mathematical audit

## correctness

PASS

Checked exact classical parking-function vertex maximization: h(G)=Σ_i G_i+Σ_{i<j}max(0,G_i,G_j); direct enumeration of all vertex layers for n=2..6 confirmed formula and opposite-direction width as S_n/R_n with kernel L(x,y)=max(0,x,y)-min(0,x,y). K_n=max(1,number of negative Gaussian coordinates), hence binomial layer fluctuations. Independently integrated the one-point Hoeffding projection f(x)=|x|Φ(|x|)+φ(|x|)+φ(0), obtaining μ=(1+√2)/√π and E f²−9μ²/8=(14π+12√3−30√2−21)/(24π)=0.017778933...; cross radial covariance E[(G²−1)f(G)]=μ/2. Degenerate U remainder has O(n²) second moment, negligible against n^(3/2), while chi-radius expansion contributes −μ/4(G²−1) to influence. Joint iid CLT and even influence vs centered odd sign indicator yield independent normal limits, the latter with variance 1/4. Exact mean follows from radial independence E S_n=E R_n E W_n. The finite numerical checks corroborate but do not prove the n→∞ theorem.

## originality

PASS

Joint second-order random Euclidean width/exposed-layer Gaussian CLT with exact variance is finer than the published polytope vertex descriptions, partial-permutohedron embeddings and first-order deterministic width laws. Generic Hoeffding CLTs give the method but not this exact identified kernel and radial correction.

## value

PASS

A precise second-order Gaussian law and independent exposed-vertex layer behavior for the canonical parking-function polytope are natural probabilistic convex-geometric invariants. The nontrivial exact covariance/radial cancellation and variance are not supplied by elementary vertex enumeration or first-order width scaling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
