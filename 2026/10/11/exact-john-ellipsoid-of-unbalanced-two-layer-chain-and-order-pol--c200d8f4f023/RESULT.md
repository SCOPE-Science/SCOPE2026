# Exact John ellipsoid of unbalanced two-layer chain and order polytopes

## Finding

Let \(a,b\) be **unequal positive integers** and \(d=a+b\). Consider the full-dimensional chain polytope of a complete height-two poset:
\[
P_{a,b}=\{(x,y)\in\mathbb R^{a+b}:x_i\ge0,\ y_j\ge0,\ x_i+y_j\le1\text{ for every }i,j\}.
\]
This is also the stable-set polytope of the complete bipartite graph \(K_{a,b}\). The associated order polytope with \(0\le x_i\le y_j\le1\) is its image under the Euclidean isometry \((x,y)\mapsto(x,\mathbf1_b-y)\).

Define
\[
\begin{aligned}
\delta&=\frac{b-a}{d}, & s&=\sqrt{\frac{2d-(d+1)\delta^2}{d-1}},\\
p&=\frac{s-\delta}{2}, &q&=\frac{s+\delta}{2}, &H&=1+p+q,\\
A&=\frac{b(1+p)}p, & B&=\frac{a(1+q)}q, & h&=\frac{ab}{dH},
\end{aligned}
\]
with \(J_{a,b}\) the all-ones matrix and
\[
K=\begin{pmatrix}AI_a&J_{a,b}\\J_{b,a}&BI_b\end{pmatrix}.
\]
The unique maximum-volume ellipsoid inscribed in \(P_{a,b}\) is
\[
E_{a,b}=\left\{z:(z-c)^{\mathsf T}\Sigma^{-1}(z-c)\le1\right\},\qquad
c=\frac1H(p\mathbf1_a,q\mathbf1_b),\qquad \Sigma=hK^{-1}.
\]
Every one of the \(a+b+ab\) defining facets contacts the ellipsoid at its own distinct point in the relative interior.

Writing
\[
\lambda_\pm=\frac{A+B\pm\sqrt{(A-B)^2+4ab}}2,
\]
the complete squared-semiaxis spectrum is \(h/A\) with multiplicity \(a-1\), \(h/B\) with multiplicity \(b-1\), and \(h/\lambda_+\), \(h/\lambda_-\) with multiplicity one each. Zero-multiplicity eigenspaces are absent. Its exact \(d\)-dimensional volume is
\[
\operatorname{vol}_d(E_{a,b})
=\frac{\pi^{d/2}}{\Gamma(1+d/2)}
\frac{h^{d/2}}{\sqrt{A^{a-1}B^{b-1}(AB-ab)}}.
\]

## Assumptions and scope

All statements use the standard Euclidean metric on the \(d\) coordinates. The integers satisfy \(a\ge1\), \(b\ge1\), \(a\ne b\). The matrix \(J_{a,b}\) has \(a\) rows and \(b\) columns. A shape matrix \(\Sigma\) defines the ellipsoid by \((z-c)^{\mathsf T}\Sigma^{-1}(z-c)\le1\), so its eigenvalues are squared semiaxes, not squared reciprocal semiaxes. No claims concern non-bipartite stable-set polytopes or arbitrary ranked posets. The balanced case was previously solved and is not claimed as a new contribution.

## Proof

**1. Positivity and two governing identities.** Since \(|\delta|<1\) and \(d\ge3\) for unequal positive integers,
\[
s^2-\delta^2=\frac{2d(1-\delta^2)}{d-1}>0.
\]
Therefore \(p,q>0\). The formulas directly give
\[
q-p=\frac{b-a}{d},\qquad d(p^2+q^2)-2pq=d.
\]
Equivalently the pair of identities
\[
\begin{aligned}
F_1&:=a+aq-bp+pq-dp^2=0,\\
F_2&:=b+bp-aq+pq-dq^2=0
\end{aligned}
\]
holds: their sum is \(d+2pq-d(p^2+q^2)=0\), while their difference is \(H[(a-b)+d(q-p)]=0\).

**2. Matrix positivity and inverse entries.** Set \(\Delta=AB-ab=abH/(pq)>0\). The matrix \(K\) has eigenvalue \(A>0\) on the \((a-1)\)-dimensional zero-sum subspace of the first block and eigenvalue \(B>0\) on the \((b-1)\)-dimensional zero-sum subspace of the second block. On the two-dimensional block-constant subspace its matrix in orthonormal block-mean coordinates is
\[
\begin{pmatrix}A&\sqrt{ab}\\\sqrt{ab}&B\end{pmatrix},
\]
which is positive definite because \(A,B,\Delta>0\). Hence \(\Sigma=hK^{-1}\) exists and is positive definite. Its relevant entries are
\[
(K^{-1})_{ii}=\frac{1+b/\Delta}{A}\quad(i\le a),\qquad
(K^{-1})_{a+j,a+j}=\frac{1+a/\Delta}{B}\quad(j\le b),
\]
and \((K^{-1})_{i,a+j}=-1/\Delta\) for every \(i,j\). By \(F_1=F_2=0\) these simplify to
\[
\Sigma_{ii}=\frac{p^2}{H^2},\qquad
\Sigma_{a+j,a+j}=\frac{q^2}{H^2},\qquad
\Sigma_{i,a+j}=-\frac{pq}{dH^2}.
\]

**3. All facet tangencies.** Put \(u=p/H\), \(v=q/H\), \(w=1/H\). The respective outward facet normals and their slacks at \(c\) are \(-e_i\) with slack \(u\), \(-e_{a+j}\) with slack \(v\), and \(e_i+e_{a+j}\) with slack \(w\). Their squared support functions on the centered ellipsoid are respectively
\[
\Sigma_{ii}=u^2,\quad \Sigma_{a+j,a+j}=v^2,\quad
\Sigma_{ii}+\Sigma_{a+j,a+j}+2\Sigma_{i,a+j}
=\frac{p^2+q^2-2pq/d}{H^2}=w^2.
\]
Thus \(E_{a,b}\subseteq P_{a,b}\), with equality of support against each defining facet. An ellipsoid has a unique support point for each nonzero outward normal; because these facet normals are pairwise nonproportional, the \(a+b+ab\) points are distinct, and none belongs to another facet. Consequently every contact lies in the relative interior of its facet.

**4. A complete positive John certificate.** Write \(\gamma=d/(abH)>0\). Give each first-block nonnegativity facet weight \(\gamma bp\), each second-block nonnegativity facet weight \(\gamma aq\), and each cross facet weight \(\gamma\). For each listed outward normal \(n_f\) and slack \(r_f\in\{u,v,w\}\), direct summation gives
\[
\sum_f\omega_f\frac{n_f}{r_f}=0,\qquad
\sum_f\omega_f\frac{n_fn_f^{\mathsf T}}{r_f^2}
=\gamma H^2K=\Sigma^{-1}.
\]
Indeed, the first vector identity cancels each coordinate with its \(b\) or \(a\) incident cross facets. For the matrix identity, the upper diagonal block contributes \(\gamma H^2b(1+1/p)I_a=\gamma H^2 A I_a\), similarly for the lower block, and every cross entry equals \(\gamma H^2\). All weights are strictly positive. The affine transformation \(z\mapsto\Sigma^{-1/2}(z-c)\) sends the proposed ellipsoid to the unit ball and its contact points to vectors \(\Sigma^{1/2}n_f/r_f\), which satisfy the zero-first-moment and identity-second-moment conditions of John's theorem. Therefore the unit ball is the unique maximum-volume inscribed ellipsoid of the transformed polytope; undoing the transformation proves the asserted global optimality and uniqueness without assuming any symmetry of a competitor.

**5. Spectrum, determinant, and the order-polytope variant.** The decomposition in step 2 gives the eigenvalues \(A\) with multiplicity \(a-1\), \(B\) with multiplicity \(b-1\), and \(\lambda_\pm\) once each for \(K\), so
\[
\det K=A^{a-1}B^{b-1}(AB-ab).
\]
Scaling by \(h\), taking the square root of \(\det\Sigma\), and multiplying by the unit-ball volume yields the stated formula. Reflecting the second coordinate block is an orthogonal isometry between the chain polytope and the corresponding two-rank order polytope, so it transfers the ellipsoid and its optimality.

## Verification

The accompanying standalone program `verify_john_biclique.py` uses floating-point linear algebra over \(169\) pairs of block sizes from \(1\) through \(13\), checking \(10{,}647\) facet contact equations, the two John moment identities, positive definiteness, the spectrum, and the determinant. It also uses exact rational Gaussian elimination for twelve star cases \((a,b)=(1,b)\) with \(1\le b\le12\), checking \(168\) exact facet equations and John moment identities. All checks passed. The finite tests are corroborating examples, not a proof for infinitely many pairs; the proof above is algebraic.

To reproduce: install Python 3 and NumPy, then execute `python3 verify_john_biclique.py` in the directory containing that file. For the source equations, all displayed expressions can be checked by replacing \(q-p=(b-a)/d\) and \(d(p^2+q^2)-2pq=d\); no external certificate is required.

## Relationship to prior work

Ahmad, Fourier, and Joswig introduce and study the maximal ranked posets \(P_\tau\), including the natural unequal two-rank instance, and prove \(f\)-vector statements for chain-order polytopes. Their paper supplies the structural motivation and definitions; its main results concern faces and do not assert a maximum-volume ellipsoid. Mori's related paper analyzes triangular faces, not metric ellipsoids. General John's theorem characterizes optimal ellipsoids via contact points; the new contribution here is the evaluated two-parameter radical solution and **all-facet** certificate. A previously recorded result settles the balanced case \(a=b\) separately. This statement expressly excludes that already-covered case; the unbalanced parameter family does not follow from the balanced symmetry reduction, since the two coordinate blocks then have different sizes and distinct internal spectral subspaces. Searches did not find a published identical formula, but this is not proof of worldwide priority.

## Limitations

Only the unbalanced, complete, height-two family is classified. No assertion is made about general height, missing cross-comparabilities, non-bipartite graphs, affine-inequivalent coordinate metrics, or uniqueness of the finding in the full literature. An equivalent formula could occur under free-sum-of-cubes, optimal-design, or invariant-matrix terminology. The numerical checks are finite; independent audit has not been performed.

## References

1. Ibrahim Ahmad, Ghislain Fourier, Michael Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626 (first publicly posted 2023-09-04). https://arxiv.org/abs/2309.01626
2. Aki Mori, *Triangular faces of the order and chain polytope of a maximal ranked poset*, arXiv:2404.00263 (first publicly posted 2024-03-30). https://arxiv.org/abs/2404.00263
3. Peter M. Gruber, Franz E. Schuster, *An arithmetic proof of John's ellipsoid theorem*, arXiv:1207.7246. https://arxiv.org/abs/1207.7246
