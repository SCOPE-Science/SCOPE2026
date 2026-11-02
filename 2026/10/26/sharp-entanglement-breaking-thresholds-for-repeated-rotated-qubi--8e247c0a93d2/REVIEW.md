# Independent mathematical audit

## correctness

PASS

For Bloch D=diag(q,q,1), 0<q<1, a fixed qubit unitary induces R in SO(3). At n=1 the three singular values are 1,q,q. For n=2, the intersecting transverse planes W and R^{-1}W force one singular value q^2 of DRD; determinant q^4 fixes the product q^2 of the other two, giving nuclear norm >=q^2+2q with quarter-turn equality. For n>=3, det((DR)^n)=q^(2n) yields >=3q^(2n/3). The explicit Rodrigues rotation has prescribed diagonal trace coordinates, verified feasibility for 0<=1+2cos(2pi/n)<3, and characteristic roots u,u exp(+/-2pi i/n), u=q^(2/3). Because these roots are distinct, (DR)^n=u^n I. The known unital qubit Choi/PPT criterion ||B||_*<=1 yields exact inclusive EB thresholds q<=sqrt(2)-1 at n=2 and q<=3^(-3/(2n)) for n>=3; never at n=1. Independently reconstructed 15 numerical exact-power witnesses across q=.12,.45,.8 and depths 3,4,5,8,15; no sampling used as infinite proof.

## originality

PASS

A best-of-knowledge new exact all-depth trace-norm minimization and fixed-rotation depolarizing witness. The familiar unital-qubit EB nuclear-norm membership test and existing eventual-EB classifications are credited. The full text of the most relevant very recent eventual-EB paper was not accessible, so a stronger formula elsewhere remains a risk.

## value

PASS

The optimizer over identical reused rotations is a motivated control problem for a physically canonical anisotropic dephasing channel. Exact realization of a depolarizing power at every prescribed depth >=3 is structurally stronger than only bounding an EB index. It yields implementable depth/noise thresholds and demonstrates a qualitative two-step versus later-depth transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
