# Two quadric singular strata in a semisimple codimension-one Hessenberg fivefold
## Finding
Let \(V=\mathbb C^4\), let \(S=\operatorname{diag}(1,1,-1,-1)\), and let \(X=\operatorname{Hess}(S,(3,4,4,4))\) be the corresponding Hessenberg variety in the full flag variety. Write a flag as \(L\subset P\subset H\subset V\), with dimensions \(1,2,3\), and let \(E_+\) and \(E_-\) be the two-dimensional eigenspaces of \(S\).

Then
\[
\operatorname{Sing}(X)=\Sigma_+\sqcup\Sigma_-,
\]
where, for \(\lambda\in\{+1,-1\}\),
\[
\Sigma_\lambda=\left\{L\subset L\oplus M\subset L\oplus E_{-\lambda}:\ L\in\mathbb P(E_\lambda),\ M\in\mathbb P(E_{-\lambda})\right\}.
\]
Thus each singular component is a smooth quadric surface \(\Sigma_\lambda\cong\mathbb P^1\times\mathbb P^1\), and the two components are disjoint. At every point of either component, \(X\) is Zariski-locally isomorphic to
\[
\mathbb A^2\times\{py+qz=0\}\subset\mathbb A^6.
\]
In particular, the transverse singularity is the three-dimensional ordinary double point, \(\operatorname{Sing}(X)\) has codimension three in the fivefold \(X\), and \(X\) is normal.

## Assumptions and scope
Everything is over \(\mathbb C\). The Hessenberg function is exactly \(h=(3,4,4,4)\), the maximal proper Hessenberg function for \(n=4\), and \(S\) has eigenvalue multiplicities \(2+2\). No statement is made for other Hessenberg functions, other eigenvalue multiplicities, or higher rank.

For this Hessenberg function, the flag condition is only
\[
S L\subset H.
\]
The proof concerns the reduced algebraic variety. Reducedness for all codimension-one type-A Hessenberg schemes is known from Escobar--Precup--Shareshian, and the local equations below independently exhibit the reduced local structure in this example.

## Proof
Forget the intermediate plane. The natural projection from the full flag variety to the incidence variety of line--hyperplane pairs restricts to a projective-line bundle
\[
\pi:X\longrightarrow Y,
\]
where
\[
Y=\{(L,H):L\subset H,\ SL\subset H\}.
\]
Indeed, once \(L\subset H\) is fixed, the possible planes \(P\) are the lines in the two-dimensional quotient \(H/L\). Consequently, regularity of \(X\) at a point is equivalent to regularity of \(Y\) at its image, and locally \(X\) is the product of a neighborhood in \(Y\) with \(\mathbb A^1\).

Represent \(L\) by \([v]\in\mathbb P(V)\) and \(H\) by a covector \([\varphi]\in\mathbb P(V^*)\) with \(H=\ker\varphi\). Then \(Y\subset\mathbb P(V)\times\mathbb P(V^*)\) is the complete intersection
\[
\varphi(v)=0,\qquad \varphi(Sv)=0.
\]
The first equation is the smooth incidence divisor. A point of \(Y\) is singular precisely when the two differentials are linearly dependent. Thus, for some scalar \(\mu\),
\[
(S-\mu I)v=0,\qquad \varphi(S-\mu I)=0.
\]
The first equality comes from varying \(\varphi\), and the second from varying \(v\). Since the only eigenvalues of \(S\) are \(+1\) and \(-1\), singular points split into two disjoint sets indexed by \(\lambda\in\{+1,-1\}\). For a fixed \(\lambda\), one has \(v\in E_\lambda\), while \(\varphi\) is a left \(\lambda\)-eigenvector, equivalently it vanishes on \(E_{-\lambda}\). The incidence equation additionally says \(\varphi(v)=0\). Because \(E_\lambda\) is two-dimensional, for each line \(L=\mathbb Cv\subset E_\lambda\) there is a unique projective covector \([\varphi]\in\mathbb P(E_\lambda^*)\) annihilating \(L\). Hence each singular component of \(Y\) is a copy of \(\mathbb P^1\).

For such a singular pair, \(H=\ker\varphi=L\oplus E_{-\lambda}\). The fiber of \(\pi\) consists of planes
\[
P=L\oplus M,\qquad M\in\mathbb P(E_{-\lambda}).
\]
Therefore the two components of \(\operatorname{Sing}(X)\) are exactly
\[
\Sigma_\lambda\cong\mathbb P(E_\lambda)\times\mathbb P(E_{-\lambda})\cong\mathbb P^1\times\mathbb P^1.
\]

It remains to determine the local analytic type. Consider a point in the \(+1\)-component and choose eigenbases so that its line is represented by \(e_1\) and its covector by \(e_2^*\). On the projective chart
\[
v=(1,x,y,z),\qquad \varphi=(u,1,p,q),
\]
the two defining equations of \(Y\) are
\[
u+x+py+qz=0,\qquad u+x-py-qz=0.
\]
Replacing these by their half-sum and half-difference gives
\[
u+x=0,\qquad py+qz=0.
\]
After eliminating \(u\), this chart is
\[
\mathbb A^1_x\times\{py+qz=0\}\subset\mathbb A^1\times\mathbb A^4.
\]
The quadratic form \(py+qz\) is nondegenerate, so its hypersurface is the three-dimensional ordinary double point. Since \(X\to Y\) is locally a product with \(\mathbb A^1\), the local model in \(X\) is \(\mathbb A^2\times\{py+qz=0\}\). The same argument applies to the \(-1\)-component.

The local model is smooth away from the two surfaces and normal at every point: the ordinary double point is a normal hypersurface, and products with affine space preserve normality. This proves the stated singular locus, transverse type, codimension, and normality.

## Verification
The accompanying `artifacts/verify.py` checks the local equations symbolically. It reconstructs the incidence equations on the chosen eigenbasis chart, verifies that their half-sum and half-difference are \(u+x\) and \(py+qz\), and checks that the Hessian of the latter quadratic form has full rank four and determinant one.

The script also rewrites the patch polynomial from Insko--Precup Example 5.5,
\[
pas-pr-qs,
\]
by the invertible triangular substitution \(r=r'+as\) into
\[
-pr'-qs,
\]
which is the same nondegenerate quadric normal form. Finally it counts eight torus-fixed singular flags, four on each quadric surface, matching the fixed-point count in the source. These computations verify the local algebra and compatibility with the published patch; the global singular-locus proof is the incidence argument above.

## Relationship to prior work
Insko and Precup introduced this exact \(S\) and Hessenberg function in Example 5.5 of *The singular locus of semisimple Hessenberg varieties*. They exhibit one patch equation, show a chosen torus-fixed point is singular, and report that computations at all torus-fixed points yield one irreducible component and eight singular torus-fixed points. They do not identify the full positive-dimensional singular locus or classify the local type along it.

Escobar, Precup, and Shareshian later study all codimension-one type-A Hessenberg varieties. Their general theorem gives only a containment for the singular locus in the semisimple case, with equality asserted for nilpotent operators, and they prove all such schemes are reduced. Their irreducibility criterion also implies that the present \(2+2\) semisimple case is irreducible. The exact two-quadric singular locus and uniform transverse ordinary-double-point model above are not consequences stated in that work.

A 2024 thesis by Mike Cummings gives a partial positive answer to the Insko--Precup radicality conjecture for semisimple patch ideals. Its accessible abstract concerns radicality rather than a global singular-locus classification; the full thesis text was not accessible during this comparison, so an equivalent local calculation under different terminology remains a residual literature risk.

## Limitations
The result is specific to the five-dimensional variety \(\operatorname{Hess}(\operatorname{diag}(1,1,-1,-1),(3,4,4,4))\). It does not classify singular loci for arbitrary semisimple codimension-one Hessenberg varieties, does not construct a resolution, and does not compute global birational invariants beyond normality. The literature search cannot exclude an equivalent calculation hidden in an inaccessible thesis or differently indexed source.

## References
1. E. Insko and M. Precup, *The singular locus of semisimple Hessenberg varieties*, arXiv:1709.05423v1, 2017. https://arxiv.org/abs/1709.05423
2. L. Escobar, M. Precup, and J. Shareshian, *Hessenberg varieties of codimension one in the flag variety*, arXiv:2208.06299v1, 2022; Canadian Mathematical Bulletin, 2026. https://arxiv.org/abs/2208.06299
3. M. Cummings, *Gröbner Geometry for Hessenberg Varieties*, Master's thesis, McMaster University, 2024. Abstract available from the author's research page.
