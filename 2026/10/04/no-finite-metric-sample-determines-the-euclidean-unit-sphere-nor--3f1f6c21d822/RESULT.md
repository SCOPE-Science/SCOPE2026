# No finite metric sample determines the Euclidean unit sphere norm
## Finding
For every integer \(n\ge 2\), every nonempty finite set \(F\subset S_{{\ell_2^n}}\), and every \(\eta>0\), there is a norm \(p\) on \(\mathbb R^n\) for which
\[
\|z\|_2\le p(z)<(1+\eta)\|z\|_2\qquad(z\ne0),
\]
and such that \(p(x)=1\) for every \(x\in F\) and
\[
p(x-y)=\|x-y\|_2\qquad(x,y\in F).
\]
Nevertheless, \((\mathbb R^n,p)\) is not linearly isometric to \(\ell_2^n\). Hence no finite metric sample of a Euclidean unit sphere determines the ambient norm up to linear isometry, even among arbitrarily small Banach--Mazur perturbations of Euclidean space.

## Assumptions and scope
The scalar field is real, \(n\ge2\), and \(F\) is a finite nonempty subset of the Euclidean unit sphere. Distances on \(F\) are the restrictions of the ambient norms. The conclusion concerns exact preservation of all pairwise distances in \(F\), not approximate preservation. The perturbation parameter \(\eta>0\) is arbitrary.

## Proof
Put
\[
W=F\cup\{x-y:x,y\in F,\ x\ne y\}.
\]
This is a finite set of nonzero vectors. Because \(n\ge2\), finitely many one-dimensional subspaces cannot cover the Euclidean unit sphere. Choose \(u\in S_{{\ell_2^n}}\) that is not parallel to any member of \(W\). Therefore
\[
c=\max_{{w\in W}}\frac{{|\langle u,w\rangle|}}{{\|w\|_2}}<1.
\]
Choose \(a\) so that
\[
\max\{c,(1+\eta)^{{-1}}\}<a<1
\]
and define
\[
p(z)=\max\left\{\|z\|_2,\frac{{|\langle u,z\rangle|}}a\right\}.
\]
The maximum of two norms or seminorms with the Euclidean term present is a norm. Cauchy--Schwarz gives
\[
\|z\|_2\le p(z)\le a^{{-1}}\|z\|_2<(1+\eta)\|z\|_2
\]
for every nonzero \(z\).

For \(w\in W\), the definition of \(c\) and the inequality \(c<a\) give
\[
\frac{{|\langle u,w\rangle|}}a\le\frac ca\|w\|_2<\|w\|_2,
\]
so \(p(w)=\|w\|_2\). In particular, \(p(x)=1\) for every \(x\in F\), and for every \(x,y\in F\),
\[
p(x-y)=\|x-y\|_2.
\]
Thus the identity map on \(F\) is an exact isometry between the two restricted sphere metrics.

Finally,
\[
B_p=B_2^n\cap\{z:|\langle u,z\rangle|\le a\}.
\]
The supporting hyperplane \(\langle u,z\rangle=a\) cuts \(B_2^n\) in an \((n-1)\)-dimensional Euclidean ball of radius \(\sqrt{{1-a^2}}\), and similarly at \(\langle u,z\rangle=-a\). Since \(n\ge2\) and \(a<1\), these are nontrivial exposed faces containing line segments. Hence \(p\) is not strictly convex. The Euclidean norm is strictly convex, and strict convexity is preserved by linear isometry, so \((\mathbb R^n,p)\) is not linearly isometric to \(\ell_2^n\).

## Verification
The proof is symbolic and requires no numerical experiment. The only choice is a unit vector outside a finite union of lines, which exists in every real dimension at least two. The exact finite-distance identities are checked on the finite set \(W\), and the nonisometry is certified by the explicit positive-dimensional exposed faces of \(B_p\). The comparison \(p(z)<(1+\eta)\|z\|_2\) follows from the explicit choice \(a>(1+\eta)^{{-1}}\).

## Relationship to prior work
Nakamura and Tanaka prove that, for finite-dimensional real normed spaces, an isometry of the entire unit spheres with their ambient norm metrics forces the ambient spaces to be linearly isometric. Their theorem is genuinely global: the paper treats the full sphere and does not state a finite-sample substitute. The construction above gives an exact boundary statement: every finite Euclidean sphere sample, including all of its pairwise distances, survives in a non-Euclidean norm that can be chosen arbitrarily close to Euclidean.

Cabello Sánchez proves a different local-to-global statement for a prescribed surjective sphere isometry under strict-convexity and local-linearity hypotheses. That result assumes an isometry of the entire sphere and a relatively open region on which a prescribed map has extra structure. It neither supplies nor rules out the finite-sample renormings constructed here.

## Limitations
The finding does not address infinite samples, dense samples, stability from approximate sphere isometries, or the marked extension problem for a prescribed sphere isometry. It also does not claim an optimal relation between the perturbation size and the geometry of \(F\); the parameter \(a\) is chosen only to preserve the finitely many required directions exactly while making the ambient norm non-Euclidean.

## References
1. J. Nakamura and R. Tanaka, *Rigidity of Unit Spheres in Finite-Dimensional Real Normed Spaces*, arXiv:2609.31096v1, 25 September 2026. Primary MSC 46B04.
2. J. Cabello Sánchez, *A reflection on Tingley's problem and some applications*, arXiv:1810.02461v3; originally submitted 4 October 2018, Journal of Mathematical Analysis and Applications 476 (2019), 319--336.
