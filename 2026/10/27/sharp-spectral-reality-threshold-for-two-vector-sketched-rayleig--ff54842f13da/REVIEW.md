# Independent mathematical audit

## correctness

PASS

On the entire joint subspace the embedding gives ||G-I||<=epsilon and G11 positive definite. With R=YC the least-squares formula gives the perturbation G11^(-1)G12 C. For unit y let q=||G11^(-1)G12 y||; for q>0 project onto its normalized direction u and y. The bound gives (a-1)^2+a^2 q^2<=epsilon^2 with a=u^T G11 u, hence q<=epsilon/sqrt(1-epsilon^2); zero perturbation is immediate. For the sharp two-dimensional bound, let h=Delta/2 and write the additive real map on the complex plane as z times the argument plus w times its conjugate, in an eigenbasis of the centered symmetric Ritz matrix. Its real operator norm is |z|+|w| since a unit argument can align the two terms. The centered symmetric reference has conjugate-linear coefficient h (choose the eigenbasis order accordingly). If the pair is nonreal with imaginary part gamma>0, its discriminant identity gives |Im z|=sqrt(gamma^2+|h+w|^2). By the triangle inequality in R^2, sqrt(gamma^2+h^2)<=sqrt(gamma^2+|h+w|^2)+|w|<=||E||. This proves both reality at equality and the exact upper envelope. The frozen SPD witness has the required Schur complement and R=r times an isometry; its exact Gram square identity proves the full-space embedding and its normalized off-diagonal realizes E=delta J. The witness has a nonzero square-zero centered part at delta=h and the claimed conjugate pair above it. Exact replay for Delta=6,r=4 in reproductions/frozen_checks.py (argument 2) gives squared half-gaps 9,0,-175/9 at epsilon=0,3/5,4/5 respectively. This is a worst-case envelope over admissible inputs, not a characterization of whether a particular sketch above the threshold has real spectrum.

## originality

PASS

Credit the known nonsymmetric extraction and its qualitative pathology. The distinct supported contribution is the universal sharp imaginary-part envelope for arbitrary real whole-joint-subspace embeddings of two-vector extraction, conditional on both the full unsketched Ritz gap and residual norm. The 11/2 Resultary record has the same sharp transfer constant, critical reality transition, Gram construction and attaining eigenvalue formula after relabeling; it proves a strict real-and-simple threshold for general trial dimension. It does not prove a universal gap-dependent upper bound for the magnitude of nonreal parts in the two-vector class. This is a material overlap, not independent novelty for the threshold, and its catalogue date is not evidence of independent development or priority. Earlier records concern structurally restricted or differently parameterized problems. The envelope upper bound is a separate sharp perturbation optimization, not the stated normal-disk estimate or the exhibited witness alone.

## value

PASS

For the smallest subspace on which a real conjugate pair can occur, the result quantitatively controls the worst size of the imaginary part after reality fails, not merely whether failure can occur. Conditioning on the symmetric Ritz gap and the unsketched residual is natural for sketched eigensolvers; the attained gap-sensitive upper bound is strictly more informative than a generic perturbation norm disk and remains necessary even for positive-definite input. Exact-arithmetic worst-case scope is essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
