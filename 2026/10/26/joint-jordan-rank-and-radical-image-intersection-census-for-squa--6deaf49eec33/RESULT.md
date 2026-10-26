# Joint Jordan-rank and radical-image intersection census for square-zero two-loop modules

## Finding

Let \(q\) be any prime power, let \(V=\mathbb F_q^n\) with \(n\geq 0\), and let \(A,B\in\operatorname{End}_{\mathbb F_q}(V)\) satisfy
\[
A^2=B^2=AB=BA=0.
\]
Put \(r=\operatorname{rank} A\), \(s=\operatorname{rank} B\), \(t=\dim(\operatorname{im}A\cap\operatorname{im}B)\), \(\ell=r+s-t\), and \(d=n-\ell\). The number \(N_{n,q}(r,s,t)\) of ordered pairs with these invariants is exactly
\[
\boxed{N_{n,q}(r,s,t)=
{n\brack\ell}_q{\ell\brack r}_q{r\brack t}_q
q^{(r-t)(s-t)}S_q(d,r)S_q(d,s).}
\]
Here the Gaussian binomial coefficient is \({a\brack b}_q=\prod_{i=0}^{b-1}(q^{a-i}-1)/(q^{b-i}-1)\), with \({a\brack0}_q=1\), and
\[
S_q(d,k)=\prod_{i=0}^{k-1}(q^d-q^i),\qquad S_q(d,0)=1.
\]
The count is positive precisely when \(r,s,t\) are integers satisfying \(0\le t\le\min(r,s)\), \(\ell\le n\), and \(d\ge\max(r,s)\); it is zero otherwise. These conditions include the sole zero-pair stratum \((r,s,t)=(0,0,0)\).

Each nonempty rank-triple stratum over an algebraic closure is smooth, geometrically irreducible, and rational, with dimension
\[
\boxed{r(n-r)+t(r-t)+(s-t)(n-s)+d(r+s).}
\]
The formula therefore supplies the exact finite-field point count and dimension of every image-intersection refinement of the pairwise annihilating square-zero representation variety of \(\mathbb F_q[u,v]/(u,v)^2\).

## Assumptions and scope

The transformations are arbitrary linear maps, not required to commute merely abstractly: all four length-two products are zero. They act on a **labeled** \(n\)-dimensional vector space; the count is not a number of similarity classes. The parameters are nonnegative integers, and the field may have any prime-power order. The intersection dimension \(t\) is intrinsic and simultaneously invariant under conjugation of both operators. Each operator has Jordan blocks of sizes at most two, with exactly \(r\), respectively \(s\), blocks of size two.

## Proof

Let \(U=\operatorname{im}A\) and \(W=\operatorname{im}B\), so \(\dim U=r\), \(\dim W=s\), \(\dim(U\cap W)=t\), and \(L=U+W\) has dimension \(\ell=r+s-t\). The four equations are **equivalent** to the requirements that both \(A\) and \(B\) vanish on \(L\). Indeed, their vanishing on \(U\) and \(W\) gives the four products, and the four equations imply both vanish on both images. Consequently, specifying the pair amounts to specifying the ordered pair of image spaces \((U,W)\), then independently specifying surjections
\[
\overline A:V/L\twoheadrightarrow U,
\qquad\overline B:V/L\twoheadrightarrow W.
\]
Each pair of such surjections lifts uniquely to a pair of operators with the required images and zero products. No choices are redundant.

To count the image spaces, first choose \(L\le V\) of dimension \(\ell\), in \({n\brack\ell}_q\) ways, then \(U\le L\) of dimension \(r\), in \({\ell\brack r}_q\) ways. Next choose \(T=U\cap W\le U\) of dimension \(t\), in \({r\brack t}_q\) ways. In \(L/T\), the subspace \(W/T\) must complement \(U/T\), which has dimension \(r-t\); each complement is the graph of a linear map from a fixed \((s-t)\)-dimensional complement to \(U/T\). Therefore exactly \(q^{(r-t)(s-t)}\) choices remain for \(W\).

For any vector spaces of dimensions \(d\) and \(k\), the number of surjective linear maps from the former to the latter is \(S_q(d,k)=\prod_{i=0}^{k-1}(q^d-q^i)\), obtained by counting linearly independent coordinate functionals. Hence the two maps provide the two final factors, proving the count. Existence requires and, by the same construction, follows from \(d\ge\max(r,s)\); otherwise no surjections exist.

For the geometric assertion, the base parameterizing pairs \((U,W)\) with fixed dimensions and intersection is a smooth rational incidence stratum. One may choose \(U\) in a Grassmannian, choose \(T\) inside \(U\), and then choose \(W/T\) as a complement in an appropriate quotient. This exhibits the base as a relative Grassmannian followed by an affine bundle, of dimension
\[
r(n-r)+t(r-t)+(s-t)(n-s).
\]
Above this base the two surjections form the open full-rank subset of the vector bundle \(\operatorname{Hom}(V/L,U)\oplus\operatorname{Hom}(V/L,W)\), whose fiber dimension is \(d(r+s)\). The total is smooth, geometrically irreducible and rational, and its dimension is as stated. The argument works over any field for the geometric properties after base change.

## Verification

The standalone file `verify_rank_triples.py` independently enumerates all matrices over prime fields, tests the four products literally, computes image rank and intersection dimension by Gaussian elimination, and compares every nonzero coefficient with the formula. Verified cases include \((n,q)=(1,2),(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)\). For example, over \(\mathbb F_2\) at \(n=4\) there are \(316\) square-zero matrices, \(8296\) qualifying ordered pairs and \(10\) nonempty rank-triple strata. These finite computations are checks, not the proof for arbitrary \(n\) or nonprime fields.

## Relationship to prior work

Schröer, *Varieties of pairs of nilpotent matrices annihilating each other* (preprint 2002; published 2004), studies irreducible components of varieties with \(AB=BA=A^a=B^b=0\), including the square-zero specialization. Oblak, *Jordan forms for mutually annihilating nilpotent pairs* (2006), characterizes feasible pairs of Jordan types. Bondarenko–Gerasimova–Sergeichuk, *Pairs of mutually annihilating operators* (2008/2009), gives simultaneous canonical forms. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity* (2021/2022), enumerates all pairs with \(AB=BA=0\), and pairs of mutually annihilating nilpotents in aggregate. Those results concern geometry, existence, canonical form, or coarser counting; the present statement gives a specified finite-field cardinality and a smooth rational geometric stratum for every **triple** of individual square-zero ranks and image-intersection dimension. A pre-existing reformulation through a detailed module/orbit enumeration remains a bibliographic risk.

## Limitations

The theorem counts labeled ordered pairs rather than simultaneous-similarity classes. It does not enumerate rank profiles for products of three or more generators, higher nilpotency indices, or the full scheme structure. It does not assert a new classification of indecomposable modules or irreducible components of the full square-zero-pair variety. The available comparison is not a proof of historical uniqueness. Geometric smoothness refers to the rank-triple locally closed strata as reduced varieties, not to a potentially nonreduced ambient representation scheme.

## References

1. J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293, preprint first posted 19 November 2002; Commentarii Mathematici Helvetici 79 (2004), 396–426. https://arxiv.org/abs/math/0211293
2. P. Oblak, *Jordan forms for mutually annihilating nilpotent pairs*, arXiv:math/0612300, 12 December 2006. https://arxiv.org/abs/math/0612300
3. V. M. Bondarenko, T. G. Gerasimova and V. V. Sergeichuk, *Pairs of mutually annihilating operators*, arXiv:0812.2155, 11 December 2008; Linear Algebra and its Applications 430 (2009), 86–105. https://arxiv.org/abs/0812.2155
4. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566, 29 October 2021; Journal of Algebra (2023). https://arxiv.org/abs/2110.15566
