# Generic cusp and transverse double-branch germs of binary multiple-root loci

## Finding

**Theorem.** Work over \(\mathbb C\). For integers \(m\ge2\) and \(d\ge m+1\), define the reduced projective multiple-root locus
\[
\Delta_{m,d}=\{[F]\in\mathbb P(\operatorname{Sym}^{d}\mathbb C^{2}):\text{some linear factor of }F\text{ occurs at least }m\text{ times}\}.
\]
At every \([F]\) with exact root partition \((m+1,1^{d-m-1})\), the completed local ring has analytic form
\[
\widehat{\mathcal O}_{\Delta_{m,d},[F]}
\cong\mathbb C[[u_1,\ldots,u_{d-m},x,y]]/(y^{2}-x^{3}). \tag{1}
\]
Thus the generic merger of one multiplicity-\(m\) root with one simple root is **a transverse ordinary cusp**, independent of \(m\).

When \(d\ge 2m\), at every form with exact partition \((m,m,1^{d-2m})\), put \(q=d-2m+2\) and \(c=m-1\). Then
\[
\widehat{\mathcal O}_{\Delta_{m,d},[F]}
\cong \mathbb C[[u_1,\ldots,u_q,a_1,\ldots,a_c,b_1,\ldots,b_c]]/
(a_i b_j:1\le i,j\le c). \tag{2}
\]
These are two smooth analytic branches meeting transversely along the smooth stratum with both designated multiple roots. Their local Hilbert--Samuel multiplicity is \(2\); the completed local ring has
\[
\dim\mathcal O_{\Delta_{m,d},[F]}=q+c=d-m+1,\qquad
\operatorname{depth}\mathcal O_{\Delta_{m,d},[F]}=q+1=d-2m+3. \tag{3}
\]
For \(m=2\), the transverse crossing is a node; for \(m\ge3\) and \(d\ge2m\), the general two-multiple-root stratum is a **non-Cohen--Macaulay locus of exact depth defect \(m-2\)**. At its generic point the local ring has dimension \(m-1\) and depth \(1\), so \(\Delta_{m,d}\) fails Serre's \(S_2\) condition.

## Assumptions and scope

The variety is the *reduced scheme-theoretic image* of the classical multiplication morphism
\[
\mathbb P^1\times\mathbb P^{d-m}\longrightarrow\mathbb P^d,
\qquad ([L],[G])\longmapsto[L^mG].
\]
The statements hold at all closed complex points of the indicated **exact** multiplicity partitions (including when the number of remaining simple roots is zero). An exact partition requires all displayed simple roots to be mutually distinct and disjoint from the designated multiple roots. These local equations are not assertions about deeper collision strata or about the full global singular scheme. The normalization map and the set-theoretic singular support are classical; the theorem isolates the exact formal local rings and their depth consequences.

## Proof

**Analytic factorization lemma.** Let a monic polynomial \(F_0\) factor into monic pairwise coprime polynomials \(Q_1\cdots Q_r\). In a small complex-analytic neighborhood of \(F_0\), the multiplication map from the product of coefficient neighborhoods of the \(Q_i\) is a local analytic isomorphism. Indeed its differential identifies tangent coefficient vectors using the Chinese remainder theorem: a first-order product variation vanishes only when each variation is divisible by its corresponding factor, hence zero under the imposed degree bounds. The analytic inverse-function theorem applies. Equivalently, use Hensel factorization in complete local rings. In a projective chart with a nonzero leading coefficient, all forms can be taken monic after moving the finitely many roots away from infinity by a projective change of coordinates.

**The cusp stratum.** At a form with one root of multiplicity exactly \(m+1\) and all other roots simple, apply the factorization lemma to separate its degree-\(m+1\) root cluster from the monic simple-root factor of degree \(d-m-1\). The latter contributes \(d-m-1\) free smooth coefficient parameters. The cluster belongs to \(\Delta_{m,m+1}\) exactly when
\[
Q(z)=(z-t)^m(z-v_0).
\]
Set \(a=(mt+v_0)/(m+1)\) and \(v=v_0-t\); then \(t=a-v/(m+1)\) and \(v_0=a+mv/(m+1)\). Writing \(s=z-a\),
\[
Q(z)=\left(s+\frac{v}{m+1}\right)^m
\left(s-\frac{mv}{m+1}\right)
=s^{m+1}+\sum_{k=2}^{m+1}C_kv^ks^{m+1-k},
\]
where
\[
C_k=\frac{\binom m k-m\binom m{k-1}}{(m+1)^k},\quad
C_2=-\frac{m}{2(m+1)},\quad C_3=-\frac{m(m-1)}{3(m+1)^2}.
\]
(The convention \(\binom m{m+1}=0\) is used.) Both displayed coefficients are nonzero for \(m\ge2\). The coefficient of \(z^m\) recovers \(a\), and the remaining coefficients recover \(v^2\) and \(v^3\). Every \(v^k\), \(k\ge2\), is a polynomial in \(v^2\) and \(v^3\). Therefore the **reduced** coefficient image is exactly \(\mathbb C[a,v^2,v^3]\cong\mathbb C[a,x,y]/(y^2-x^3)\). Adding the smooth factor proves (1). Its transverse Jacobian ideal \((x^2,y)\) has colength \(2\) in the transverse local ring, while the cusp has multiplicity \(2\).

**The two-multiple-root stratum.** Suppose \(d\ge2m\) and \(F_0\) has exactly two distinct roots of multiplicity \(m\), with every other root simple. Separate two disjoint monic degree-\(m\) clusters and the remaining monic degree-\(d-2m\) factor by the factorization lemma. The latter contributes \(d-2m\) smooth parameters. In a sufficiently small neighborhood a root of multiplicity at least \(m\) must occur in one of the two clusters; the remaining factor has only simple roots. Thus the reduced image germ is the union
\[
\{Q_1=(z-t)^m\}\times\mathbb A^{m}
\quad\cup\quad
\mathbb A^{m}\times\{Q_2=(z-v)^m\},
\]
with the residual smooth parameters suppressed. The \(m\)-fold-power curve inside the affine space of monic degree-\(m\) polynomials is smooth: the coefficient of \(z^{m-1}\) equals \(-mt\) and gives a nonsingular local parameter. Analytically straighten this smooth curve in each independent coefficient block; each leaves \(c=m-1\) normal coordinates. The ideal of the union is the intersection of the two disjoint-block coordinate ideals, equal to their product \((a_i b_j)\). Its free coordinates comprise \(q=(d-2m)+2\), proving (2).

**Depth.** Set \(A=\mathbb C[[u,a]]\), \(B=\mathbb C[[u,b]]\), and \(C=\mathbb C[[u]]\) with \(q\) variables \(u\) and \(c\) variables in either of the blocks \(a,b\). The transverse-union ring \(R\) satisfies the exact sequence
\[
0\longrightarrow R\longrightarrow A\oplus B\longrightarrow C\longrightarrow0,
\]
where the last arrow is the difference of the two restrictions obtained by setting normal variables to zero. Both \(A,B\) are regular of dimension \(q+c\), whereas \(C\) is regular of dimension \(q\). The depth lemma (or the local-cohomology long exact sequence) gives \(\operatorname{depth}R=q+1\) for \(c\ge2\); for \(c=1\) the same equality follows because \(R\) is the hypersurface \((a_1b_1)\). The dimension is \(q+c\). Because the two irreducible branches are smooth of multiplicity one and meet in a proper lower-dimensional locus, their union has local multiplicity \(2\). Localizing at the generic point of the intersection deletes the \(u\)-directions; the resulting local ring has dimension \(c\) and depth \(1\). For \(c\ge2\) it violates \(S_2\). The depth defect at a closed general point is \(c-1=m-2\), completing the proof.

## Verification

The accompanying exact checker `checks/verify_multiple_root_germs.py` requires SymPy, with `checks/requirements.txt` describing the dependency. It reproduces coefficient identities for \(2\le m\le12\), verifies ambient tangent-space intersection dimensions for \(2\le m\le8\) and \(2m\le d\le 2m+3\), and checks the Hilbert functions of the squarefree two-block union for \(1\le c\le7\). Run `python checks/verify_multiple_root_germs.py` in a Python environment with the declared dependency. `checks/check_output.txt` contains an actual run's output. These computations do **not** establish the unbounded claims; the analytic factorization and exact-sequence proofs above do.

## Relationship to prior work

Chipalkatti, *On equations defining coincident root loci* (arXiv:math/0110224, first posted 2001-10-19), §5, established the scheme-theoretic normalization framework and a combinatorial classification of the **set-theoretic** singular locus; it does not give the two completed local-ring formulas (1)--(2) or their depth calculation. Kurmann, *Some remarks about equations defining coincident root loci* (arXiv:1108.4532, first posted 2011-08-23), §2, refines the singular-support analysis through normalization fibers and tangent maps, referring qualitatively to nodal-type and cusp-like phenomena. The present statement sharpens that language to the exact ordinary cusp and transverse union of two \((m-1)\)-normal-block smooth branches, with the resulting failure of Cohen--Macaulayness and \(S_2\). The familiar discriminant case \(m=2\) is classical and is included for comparison, not claimed as new. The precise overlap risk from earlier Hilbert-function/defining-ideal literature is acknowledged in the review.

## Limitations

The theorem concerns exact generic collision partitions and formal/complex-analytic neighborhoods. It does not classify deeper root collisions, every component of a nonreduced Jacobian singular scheme, global graded minimal resolutions, or all Cohen--Macaulay parameter regimes. Full-text comparison with Weyman's *On the Hilbert Functions of Multiplicity Ideals* (1993) could not be completed and remains an originality risk. The displayed singular-support criterion is established prior work. No independent external mathematical audit has been performed.

## References

1. J. V. Chipalkatti, *On equations defining coincident root loci*, arXiv:math/0110224 (2001), §§4--6; Journal of Algebra 267 (2003), 246--271. https://arxiv.org/abs/math/0110224
2. S. Kurmann, *Some remarks about equations defining coincident root loci*, arXiv:1108.4532 (2011), §§1--3; Journal of Algebra 352 (2012), 223--231. https://arxiv.org/abs/1108.4532
3. J. Weyman, *On the Hilbert functions of multiplicity ideals*, Journal of Algebra 161 (1993), 358--369. DOI:10.1006/jabr.1993.1224. Full text not reviewed.
4. Brambilla--Staglianò, *CoincidentRootLoci*, Macaulay2 documentation, `singularLocus(CoincidentRootLocus)` (set-theoretic singular-stratum functionality).
