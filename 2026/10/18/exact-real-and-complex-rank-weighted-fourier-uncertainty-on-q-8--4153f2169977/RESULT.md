# Exact real and complex rank-weighted Fourier uncertainty on \(Q_8\)

## Finding
Let \(Q_8=\{\pm1,\pm i,\pm j,\pm k\}\), and for any nonzero complex function \(f\) on \(Q_8\) define
\[
\sigma(f)=\sum_{\pi\in\widehat{Q_8}}(\dim\pi)\,\operatorname{rank}\widehat f(\pi),
\qquad \widehat f(\pi)=\sum_{g\in Q_8}f(g)\pi(g)^*.
\]
For \(\mathbb K\) equal to \(\mathbb C\) or \(\mathbb R\), let
\[
\Theta_{\mathbb K}(t)=\min\{\sigma(f):f:Q_8\to\mathbb K,\ |\operatorname{supp}f|=t\},\qquad 1\le t\le8.
\]
The **entire exact-support rank-weighted uncertainty profiles** are
\[
\boxed{(\Theta_{\mathbb C}(1),\ldots,\Theta_{\mathbb C}(8))=(8,4,4,2,3,2,3,1)}
\]
and
\[
\boxed{(\Theta_{\mathbb R}(1),\ldots,\Theta_{\mathbb R}(8))=(8,4,6,2,5,3,5,1).}
\]
In particular, the real and complex optima differ at exactly \(t\in\{3,5,6,7\}\). The split is forced by the isotropic complex quadric governing the unique two-dimensional Fourier block: over real coefficients that block can never have rank one.

## Assumptions and scope
Signals are arbitrary, not required positive or of constant modulus. The support is **exact** (all indicated nonzero entries are required). Matrix rank is complex rank, including for real-valued signals. The normalization of the Fourier transform is deliberately unnormalized; replacing it by a nonzero common factor does not change any rank. These results concern functions **on the finite nonabelian group** \(Q_8\), not quaternion-valued functions on a Euclidean space.

For the transversal \(T=(1,i,j,k)\) of the center, write
\[
 u_c=f(c)+f(-c),\qquad v_c=f(c)-f(-c),\qquad
 f(\pm c)=\tfrac12(u_c\pm v_c).
\]
Use the fixed coordinate order \((1,i,j,k)\) for both vectors.

## Proof
**1. Fourier block decomposition.** Four one-dimensional irreducible representations of \(Q_8\) factor through \(Q_8/\{\pm1\}\simeq\mathbb F_2^2\). Their Fourier coefficients are exactly the four ordinary Walsh transforms of \(u\):
\[
  W(u)=(u_1+\alpha u_i+\beta u_j+\alpha\beta u_k)_{\alpha,\beta\in\{1,-1\}}.
\]
Let \(a(u)\) be the number of nonzero entries of \(W(u)\).

The remaining irreducible representation has dimension two. Choose
\[
 A=\begin{pmatrix}\mathrm i&0\\0&-\mathrm i\end{pmatrix},\quad
 B=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad C=AB,
\]
for the matrices representing \(i,j,k\), respectively. Since their adjoints are their negatives, the unnormalized two-dimensional Fourier block is
\[
 M(v)=v_1I_2-v_i A-v_j B-v_k C,
 \qquad \det M(v)=v_1^2+v_i^2+v_j^2+v_k^2.
\]
Consequently, with \(r(v)=\operatorname{rank}M(v)\),
\[
\sigma(f)=a(u)+2r(v),\quad
r(v)=\begin{cases}0,&v=0;\\1,&v\ne0\ \text{and}\ \sum_c v_c^2=0;\\2,&\sum_c v_c^2\ne0.\end{cases}
\]
For real \(v\ne0\), the sum of squares is positive, so \(r(v)=2\); for complex \(v\), nonzero isotropic vectors do exist (e.g. \((1,\mathrm i,0,0)\)).

**2. Exact support constraints.** If \(u=0\), the support of \(f\) is even, since every nonzero \(v_c\) yields both \(c\) and \(-c\). The same is true if \(v=0\). If \(a(u)=1\), the inverse Walsh transform forces \(u\) to be a nonzero scalar multiple of a character and hence all four coordinates of \(u\) are nonzero. Then the support of \(f\) is at least four. If \(a(u)=2\), writing \(u\) as a sum of two distinct characters shows that its coordinate support has size either two or four, never three: the ratio of the two characters takes \(1\) and \(-1\) on two coordinates each. If \(u\) has support one, all four Walsh coefficients are nonzero. Therefore, for \(v=0\), the minimum possible \(a(u)\) at spatial supports \(t=2,4,6,8\) is respectively \(4,2,3,1\).

**3. Sharp complex lower bounds.** The general rank-weighted uncertainty inequality for an eight-element group gives \(t\sigma(f)\ge8\), hence the lower bounds \(8,4,3,2,2,2,2,1\) for \(t=1,\ldots,8\). A putative \(\sigma(f)=3\) at \(t=3\) would require either \((a,r)=(3,0)\) or \((a,r)=(1,1)\); the first has even support and the second at least four supported points. A putative \(\sigma(f)=2\) at either \(t=5\) or \(t=7\) would require \((a,r)=(2,0)\) or \((0,1)\), both of even spatial support. This proves the claimed complex lower profile.

**4. Sharp real lower bounds.** The general product inequality already gives the lower bounds at \(t=1,2,4,8\). For odd \(t\) the vanishing of either \(u\) or \(v\) is impossible. Thus real \(v\ne0\) has \(r=2\) and nonzero \(u\) has \(a\ge1\). At \(t=5,7\) this yields \(\sigma\ge5\). At \(t=3\), \(a=1\) is impossible because it forces at least four supported points, so \(\sigma\ge6\). Finally, at \(t=6\), if \(v\ne0\), the real block has rank two and \(\sigma\ge4\). If \(v=0\), exactly three coordinates of \(u\) are supported, so the two-character support lemma gives \(a\ge3\). Therefore \(\sigma\ge3\) at \(t=6\).

**5. Sharpness for all sixteen entries.** Every row in the following tables specifies exact vectors \((u,v)\) in the above fixed coordinate order; recover \(f(\pm c)=(u_c\pm v_c)/2\). Direct substitution into the formulas of Step 1 gives the stated spatial supports and weighted spectral supports. A zero tuple means \((0,0,0,0)\).

| \(t\) | Complex \(u\) | Complex \(v\) | \((a,r)\) |
| ---: | --- | --- | --- |
| 1 | \((1,0,0,0)\) | \((1,0,0,0)\) | \((4,2)\) |
| 2 | \((1,0,0,0)\) | \((0,0,0,0)\) | \((4,0)\) |
| 3 | \((1,1,0,0)\) | \((1,\mathrm i,0,0)\) | \((2,1)\) |
| 4 | \((0,0,0,0)\) | \((1,\mathrm i,0,0)\) | \((0,1)\) |
| 5 | \((1,1,1,1)\) | \((1,1,1,\mathrm i\sqrt3)\) | \((1,1)\) |
| 6 | \((0,0,0,0)\) | \((1,1,\mathrm i\sqrt2,0)\) | \((0,1)\) |
| 7 | \((1,1,1,1)\) | \((1,\mathrm i,0,0)\) | \((1,1)\) |
| 8 | \((1,1,1,1)\) | \((0,0,0,0)\) | \((1,0)\) |

| \(t\) | Real \(u\) | Real \(v\) | \((a,r)\) |
| ---: | --- | --- | --- |
| 1 | \((1,0,0,0)\) | \((1,0,0,0)\) | \((4,2)\) |
| 2 | \((1,0,0,0)\) | \((0,0,0,0)\) | \((4,0)\) |
| 3 | \((1,1,0,0)\) | \((1,0,0,0)\) | \((2,2)\) |
| 4 | \((1,1,0,0)\) | \((0,0,0,0)\) | \((2,0)\) |
| 5 | \((1,1,1,1)\) | \((1,1,1,0)\) | \((1,2)\) |
| 6 | \((1,1,2,0)\) | \((0,0,0,0)\) | \((3,0)\) |
| 7 | \((1,1,1,1)\) | \((1,0,0,0)\) | \((1,2)\) |
| 8 | \((1,1,1,1)\) | \((0,0,0,0)\) | \((1,0)\) |

This completes both lower and upper bounds.

## Verification
Run `python checker.py` in the same directory with SymPy installed. The script verifies the quaternion relations, symbolically calculates the four-square determinant of the nonabelian Fourier block, verifies each of the sixteen explicit witnesses with exact algebraic arithmetic, and checks the elementary two-character Walsh-support identity. The universal lower bounds follow from the preceding proof, not from enumeration or numerical testing.

## Relationship to prior work
Alagic and Russell's compact-group uncertainty principle (arXiv:math/0608702) establishes the general inequality \(t\sigma(f)\ge8\) when applied here but does not give the exact-support table or its real/complex distinction. Their Fourier-support measure is precisely the rank-weighted measure used above. The earlier result *Exact two-spike rank-support law on arbitrary finite groups* determines our \(t=2\) entry, which is therefore not claimed as a new isolated fact; it does not determine any stratum \(t\ge3\). The published *Support-pattern incidence refinement of the order-eight Fourier uncertainty diagram* treats the **abelian cyclic group** \(\mathbb Z_8\) (whose irreducibles all have dimension one), not \(Q_8\) with its two-dimensional block. Neither the existing general estimate nor these closest exact tables imply the displayed dual profiles. The central-character splitting and isotropic/anisotropic determinant explain the extra constraints and attainability.

## Limitations
The classification is for a single natural group of order eight and rank-weighted Fourier support; it is not an exact diagram for all nonabelian groups, not a count of support-position pairs, and not the unweighted number of nonzero irreducible blocks. The proof does not classify every minimizing function up to group symmetries. The absence of a matching result from searches is not a proof of publication priority; an equivalent calculation under unindexed group-algebra terminology is a residual risk. Some older papers on nonabelian uncertainty were available only as abstracts and might contain specialized examples.

## References
1. G. Alagic and A. Russell, *Uncertainty Principles for Compact Groups*, arXiv:math/0608702v1 (first publicly posted 2006-08-28); revised v2 (2008), Theorem 2 and Section 3.2. https://arxiv.org/abs/math/0608702
2. *Exact two-spike rank-support law on arbitrary finite groups*, publicly available complete result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-two-spike-rank-support-law-on-arbitrary-finite-groups--29d4924b2b7c
3. *Support-pattern incidence refinement of the order-eight Fourier uncertainty diagram*, publicly available complete result for \(\mathbb Z_8\), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-support-pattern-incidence-refinement-of-the-order-eight-fourier--78caf4d7929b
4. A. Russell and I. E. Shparlinski, *Classical and Quantum Function Reconstruction via Character Evaluation*, J. Complexity 20 (2004), 404–422, DOI 10.1016/j.jco.2003.08.019 (abstract consulted).
