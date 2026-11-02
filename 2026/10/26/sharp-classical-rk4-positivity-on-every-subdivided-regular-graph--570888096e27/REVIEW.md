# Independent mathematical audit

## correctness

PASS

For every finite connected simple d-regular graph (d>=2), with each edge once subdivided and unit weights, the exact completed classical RK4 step R_4(-hL) is entrywise nonnegative iff 0<=h<=2/(d+2). Reconstructed block incidence L=[[dI,-B],[-B^T,2I]] and all six off-diagonal pair types. Nonincident original/edge entry equals c*h^3*(1-(d+2)h/2)/6, with c>0 on an existing length-two base-graph path, giving a negative entry for EVERY h beyond the threshold. Incident pairs positive on range by F_d=1-x+x^2(a_d-b_dx), a_d-b_d=1/3, 0<=x<=1; original/original and edge/edge quadratic discriminants strictly negative, remaining off-diagonal types nonnegative. Diagonals positive because scalar R_4(-z)=(1-z/2)^2+z^2*((z-2)^2+2)/24>0. The sign-conjugate Perron eigenvector gives maximal Laplacian eigenvalue d+2; spectral contractivity extends to rho/(d+2), distinct from positivity. Independent exact rational matrix powers rechecked C4,C5,K4,K5 at threshold, before/after, row sums and witnesses. These finite examples corroborate, rather than prove, the general incidence identities.

## originality

PASS

Best-of-knowledge PASS: explicit exact graph-family positivity cutoff and nonreentrant negative witness are not shown by the inspected general SSP theory or distinct semigroup and Markov/rational schemes. Cycle and complete-bipartite specializations are not claimed as new. A structurally equivalent special-graph formula in less indexed numerical ODE literature remains plausible.

## value

PASS

Sharp nonreentrant timestep cutoff for a natural family of heat networks, independent of size and graph geometry; separates entrywise positivity from Euclidean contractivity and improves on forward Euler at d>=3. It is a meaningful numerical stability classification, not a mere polynomial rewrite.

The dated certificate retains the supplied scientific assessment, sources and limitations.
