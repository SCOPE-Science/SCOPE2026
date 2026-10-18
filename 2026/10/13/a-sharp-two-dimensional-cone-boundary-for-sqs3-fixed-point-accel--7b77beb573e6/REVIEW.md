# Independent mathematical audit

## correctness

PASS

For 2x2 A=I-J=[[a,-c],[-c,d]] symmetric positive definite with c>0, (I-sA)^2 has diagonal terms positive and offdiagonal sc(2-s(a+d)); hence it maps R_+² into itself iff 0<=s<=2/(a+d). With SqS3 s=||Ax||/||A²x||, positive x arbitrarily close to the Perron eigenvector may generate a signed subdominant mode when J has nonzero second eigenvalue. Exact witness J=[[1/2,1/4],[1/4,1/2]], x=(11/10,9/10), s=4sqrt(19729)/181, final J(I-sA)^2x has second coordinate (3769-27sqrt(19729))/3620<0. Independently rederived radical by exact algebra; never inferred all A from finite witnesses.

## originality

PASS

Best-of-knowledge original exact orthant feasibility frontier and positive-input counterexample for raw unsafeguarded SqS3. Varadhan–Roland provide the step formula and generic safeguard/globalization; their full accessible pages discuss parameter failures but do not derive the 2D fixed-s matrix entry condition s<=2/tr A or the radical positive-input witness. The result is not claimed for safeguarded methods.

## value

PASS

Sharp feasibility barrier for a commonly used fixed-point accelerator, with a robust tiny two-dimensional counterexample under a strictly positive contractive base map. It motivates step safeguarding and distinguishes feasible base iteration from feasible extrapolation. Does not criticize or override safeguarded gSqS3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
