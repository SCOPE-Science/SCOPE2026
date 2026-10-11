# Rank-sensitive finite probability models for Bessel Gram matrices
## Finding
Let \\(x_1,\\ldots,x_N\\) be a finite Bessel family with Bessel bound \\(1\\), and let
\\[
G=(\\langle x_j,x_k\\rangle)_{j,k=1}^N.
\\]
Write \\(r=\\operatorname{rank}G\\). If \\(r\\ge1\\), then in the complex case there is a probability space with at most \\(r^2\\) atoms and random variables \\(f_1,\\ldots,f_N\\) with \\(|f_j|\\le1\\) pointwise such that
\\[
G_{jk}=\\mathbb E[f_j\\overline{f_k}]
\\]
for every \\(1\\le j,k\\le N\\). In the real case, at most \\(r(r+1)/2\\) atoms suffice. For \\(G=0\\), one atom with all \\(f_j=0\\) gives the trivial realization.

Thus the finite simple-function realization supplied by the Bessel-sequence form of Grothendieck's theorem admits an intrinsic rank-sensitive support bound. In particular, when many vectors lie in a low-dimensional span, the number of probability atoms can be bounded independently of the number of vectors.

## Assumptions and scope
A finite family has Bessel bound \\(1\\) when
\\[
\\sum_{j=1}^N |\\langle h,x_j\\rangle|^2\\le \\|h\\|^2
\\]
for every vector \\(h\\) in the ambient Hilbert space. Equivalently, its Gram matrix is a positive semidefinite contraction: \\(0\\le G\\le I_N\\).

The claim is finite-dimensional and quantitative. It concerns the number of atoms in a probability representation of the Gram matrix. It does not assert that the bounds \\(r^2\\) or \\(r(r+1)/2\\) are always minimal, and it does not give a uniform finite-atom representation for an arbitrary infinite Bessel sequence.

## Proof
The recent Bessel-sequence Grothendieck theorem proves, in its finite complex form, that every Hermitian contraction \\(0\\le G\\le I_N\\) belongs to
\\[
\\operatorname{conv}\\{zz^*:z\\in\\mathbb D^N\\},
\\]
where \\(\\mathbb D\\) is the closed unit disk. Hence there are finitely many \\(z_s\\in\\mathbb D^N\\) and positive weights \\(p_s\\) with \\(\\sum_s p_s=1\\) such that
\\[
G=\\sum_s p_s z_s z_s^*.
\\]

Let \\(R=\\operatorname{Ran}G\\). For any \\(v\\in\\ker G\\), positivity gives
\\[
0=v^*Gv=\\sum_s p_s |z_s^*v|^2.
\\]
Every summand is nonnegative and every retained weight is positive, so \\(z_s^*v=0\\) for all \\(s\\). Thus every \\(z_s\\) lies in \\(R=(\\ker G)^\\perp\\). Consequently
\\[
G\\in\\operatorname{conv} S_R,
\\qquad
S_R=\\{zz^*:z\\in R\\cap\\mathbb D^N\\}.
\\]

The set \\(R\\cap\\mathbb D^N\\) is compact and convex, hence connected, and \\(z\\mapsto zz^*\\) is continuous. Therefore \\(S_R\\) is a compact connected subset of the real vector space of Hermitian operators supported on \\(R\\). That real vector space has dimension \\(r^2\\). The Fenchel--Hanner--Rådström refinement of Carathéodory's theorem says that every point in the convex hull of a connected subset of a real \\(d\\)-dimensional vector space is a convex combination of at most \\(d\\) points. Applying it with \\(d=r^2\\) gives
\\[
G=\\sum_{s=1}^m q_s w_s w_s^*,
\\qquad m\\le r^2,
\\]
with \\(w_s\\in R\\cap\\mathbb D^N\\), \\(q_s\\ge0\\), and \\(\\sum_s q_s=1\\).

Take a probability space with atoms \\(s\\) of masses \\(q_s\\), and define \\(f_j(s)=(w_s)_j\\). Then \\(|f_j(s)|\\le1\\) and the displayed Gram identity follows entrywise.

For real scalars, the same argument starts from the real convex representation with \\(w_s\\in[-1,1]^N\\). The symmetric operators supported on an \\(r\\)-dimensional real space form a real vector space of dimension \\(r(r+1)/2\\), so the same connected-set theorem yields the stated real bound.

## Verification
The proof was checked at each dimension-sensitive step. The kernel calculation forces every rank-one generator in any positive-weight convex representation of \\(G\\) into \\(\\operatorname{Ran}G\\); this is what replaces the ambient matrix dimension by the intrinsic rank. The connected set \\(S_R\\) is the continuous image of a convex compact set. The relevant ambient real dimensions are exactly \\(r^2\\) for Hermitian operators on \\(\\mathbb C^r\\) and \\(r(r+1)/2\\) for symmetric operators on \\(\\mathbb R^r\\). The classical connected-set refinement of Carathéodory then supplies the atom counts. No finite numerical experiment is used as evidence for the universal statement.

The edge case \\(r=0\\) was separated explicitly because a probability space must contain at least one atom. For \\(r\\ge1\\), the claimed bounds are positive integers.

## Relationship to prior work
Liehr, Taylor, and Yu prove the sharp Bessel-sequence representation with \\(L^\\infty\\)-bound \\(1\\). Their finite proof obtains a convex decomposition of the Gram matrix and then constructs simple functions from the finitely many convex-combination terms, but it does not state a rank-sensitive bound on the number of terms. The present observation combines their convex representation with the fact that every positive-weight generator is automatically supported on the range of \\(G\\), followed by the connected-set refinement of Carathéodory.

The classical Hanner--Rådström theorem is broader convex geometry: it reduces the Carathéodory number for connected sets from \\(d+1\\) to \\(d\\). It does not by itself identify the low-dimensional range-restricted generating set arising from a Bessel Gram matrix.

Targeted searches were also made under the aliases finite-support correlation representation, atomic Gram representation, rank-sensitive Carathéodory bound, polydisk rank-one decomposition, and finite simple-function Bessel representation. No statement implying the rank-dependent atom bounds was located. This search result is evidence about checked coverage, not a proof of novelty.

## Limitations
No minimality or sharpness claim is made for the atom counts. The connected-set theorem can in principle overestimate the number required for a particular Gram matrix. The result is for finite families; the countable theorem in the focal paper uses compactness of probability measures and is not converted here into a finite-support statement. A residual originality risk is that the same rank-sensitive compression may appear in older matrix-convexity, cubature, or bounded-correlation literature under different terminology.

## References
1. L. Liehr, M. A. Taylor, and P. Yu, *Grothendieck's theorem for Bessel sequences*, arXiv:2608.12280v1 (2026), especially the finite convex representation and simple-function construction.
2. O. Hanner and H. Rådström, *A generalization of a theorem of Fenchel*, Proc. Amer. Math. Soc. 2 (1951), 589--593, DOI:10.1090/S0002-9939-1951-0044142-0.
