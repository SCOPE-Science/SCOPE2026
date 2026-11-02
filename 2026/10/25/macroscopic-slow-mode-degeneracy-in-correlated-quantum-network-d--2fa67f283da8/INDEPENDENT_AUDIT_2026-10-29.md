# Independent mathematical audit

## correctness

PASS

For even N=2m, define u all ones, s balanced ±1, S=uu^T-I, Q=ss^T-I and exchange jumps Vij=|i><j|+|j><i|. Their independent-edge dissipator D=Σ D[Vij] has HS-orthogonal spaces scalar eigenvalue 0, symmetric zero-diagonal eigval -(N-2), traceless diagonal and skew zero-diagonal eigval -N. The coherent -i[Jxi S,.] has zero HS-real part; bD[Q] is nonpositive quadratic form, so every nonstationary eigenoperator has Re λ <= -a(N-2), a=J² Δt ξ(1-ξ)(1-κ²)>0. Equality requires X transpose-symmetric, diagonal zero, [Q,X]=0 (for κ>0) and [S,X]=0 (transposition parity in eigenvalue equation), or Xs∈Cs and Xu∈Cu; the entire boundary eigenvalue is exactly -a(N-2). HS contraction on traceless part excludes nontrivial Jordan chains at boundary, hence semisimple. Constant-row-sum linear constraints give dim C(N-2,2) for N>=6 and 0<κ<1, exception N4 dim 3; at κ=0 only Xu constraint, dim C(N-1,2). Independently built full N²×N² Liouvillian matrices at N4,N6 and κ=0,.45 and reproduced gap and multiplicities. Finite spectrum checks are diagnostic; analytic symmetric/s skew decomposition and incidence ranks prove all even N. Inspected RESULT.md blob 74db5c7..., artifacts/verify.py 262c9c7... and status files. Statement concerns leading-order continuous-time generator, not exact finite switching channel.

## originality

PASS

Nourmandipour–Mancini's October 2026 preprint is an extremely close primary source, describing this random-network ensemble and one explicit slow eigenoperator/rate. The new claim is the full eigenspace dimension, precise boundary uniqueness and four-site exception for 0<κ<1. Original full manuscript could not be accessed (arXiv PDF/OA attempts unavailable and authorized Oxford returned vpn_disconnected); only its publicly available abstract plus mathematical source attribution were compared, so a plausible precise prior coverage remains a material best-of-knowledge risk. The inspected related Farooq–Mancini work treats a different random-network model.

## value

PASS

The mode multiplicity grows quadratically, so correlation changes the entire slow relaxation geometry rather than merely shifting one decay rate. An explicit closed dimension C(N-2,2), an N=4 exception and a singular κ=0 multiplicity jump give a useful natural structural classification of dissipative network dynamics beyond a single already-known slow eigenoperator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
