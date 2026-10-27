# Scientific review

## Correctness — PASS

The claim is the completed sixth-order Gauss–Legendre matrix functional calculus on every finite connected unweighted complete multipartite graph. Exact orthogonal projectors yield all entries for every part size and every nonnegative timestep. The two derivative identities for the scalar stability function and its divided difference have strictly signed, explicit polynomial numerators, proving both off-diagonal positivity and a single diagonal crossing. First-order stochastic dominance of the vertex spectral measures strictly orders the diagonal crossings by increasing part size. Rational matrix checks reproduce all transition-entry formulas and example signs but are not a proof for arbitrary graph size.

## Originality — PASS, subject to literature uncertainty

The closest primary literature concerns general SSP Runge–Kutta criteria, positivity-preserving graph-Laplacian integrators, and high-order Padé implementation. In particular, the 2001 Gottlieb–Shu–Tadmor article addresses general method-wide SSP restrictions; the 2021/2022 Blanes–Iserles–Macnamara study explicitly identifies higher-order diagonal Padé positivity as a challenge; and the 2021 Song–Eisenträger study gives precisely the sixth-order Padé numerator and denominator but concerns structural dynamics, stability, and efficiency rather than entrywise diffusion positivity. The inspected material contains no theorem implying that positive off-diagonal entries persist while the sharp diagonal threshold is controlled by the smallest multipartite class. Published mathematical records on fourth-order \([2/2]\) Padé concern a genuinely different stability map. Bibliographic indexing is not complete, so an independently rediscovered equivalent specialized result remains possible.

## Value — PASS

The result resolves a sharp, all-timestep positivity question for an unbounded heterogeneous graph family and standard sixth-order implicit method; it also proves a structurally informative one-parameter reduction: only graph order and the smallest part determine the cutoff. The universal off-diagonal sign and exact six-vertex contrast reveal why Euclidean spectral nonexpansivity alone does not guarantee a nonnegative numerical state. Higher-order Padé positivity was singled out as a challenge in the inspected primary literature. The theorem is not asserted to be a general method-wide positivity guarantee or a numerical accuracy theorem.

## Closest sources and limitations

The direct foundation is Gottlieb, Shu and Tadmor (SIAM Review 2001, DOI 10.1137/S003614450036757X); see also Conde et al. (arXiv:1702.04621), Blanes et al. (arXiv:2102.08242), and Song and Eisenträger (arXiv:2103.12282). Exact symbolic calculations and direct rational tests support the analytical identities. The proof does not extend to weighted, directed, nonlinear or non-complete-multipartite systems, and no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
