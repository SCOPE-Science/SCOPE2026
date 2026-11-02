# Rank-one Nijenhuis spectra of free two-step nilpotent Lie algebras

## Finding
Let \(k=\mathbb F_q\) be any finite field, let \(n\geq2\), and set \(c=\binom n2\) and \(m=n+c\). Let \(L=V\oplus\bigwedge^2V\), with \(\dim V=n\), have the free class-two Lie bracket \([v+z,w+t]=v\wedge w\). A nonzero rank-one endomorphism is written \(N_{u,\phi}(x)=\phi(x)u\), where \(0\neq u\in L\) and \(0\neq\phi\in L^*\).

The Nijenhuis identity
\[
[Nx,Ny]=N\bigl([Nx,y]+[x,Ny]-N[x,y]\bigr)
\]
holds **if and only if** either

1. \(\phi(\bigwedge^2V)=0\); or
2. \(\phi(\bigwedge^2V)\neq0\), \(\phi(u)=0\), and \(\phi([u,L])=0\).

These cases are disjoint. In the second case \(N^2=0\), while the first includes both square-zero and non-square-zero maps. The total number of nonzero rank-one Nijenhuis maps is
\[
\boxed{
\mathcal N_{n,q}=\frac{(q^m-1)(q^n-1)+q^n(q^c-1)(q^{c-1}-1)+(q^n-1)q^{m-1}(q^{c-n+1}-1)}{q-1}.}
\]
The three displayed numerator terms count, respectively, the first case, the second case with central image, and the second case with noncentral image. The corresponding counts are the terms divided individually by \(q-1\). The number of Nijenhuis rank-one maps with \(N^2\neq0\) is precisely
\[
(q^n-1)q^{m-1}.
\]
The second case is empty for \(n=2\), appears for every \(n\ge3\), and comprises an asymptotic proportion tending to \(1\) among all nonzero rank-one Nijenhuis maps as \(n\to\infty\) with \(q\) fixed.

## Assumptions and scope
All fields are finite fields of any characteristic, including characteristic two and nonprime finite fields. The bracket is alternating: in characteristic two, the formula \(v\wedge w\) remains valid. \(\bigwedge^2V\) is central and equals \([L,L]\). The assertion counts **distinct linear operators**, not factorizations \((u,\phi)\) and not automorphism-conjugacy classes. It addresses only nonzero rank-one operators, not the complete Nijenhuis variety.

## Proof
For \(u,\phi\neq0\) put \(\lambda=\phi(u)\) and \(\psi(x)=\phi([u,x])\). Since \([u,u]=0\), substituting \(Nx=\phi(x)u\) into the Nijenhuis torsion gives the equivalent scalar identity
\[
\phi(x)\psi(y)-\phi(y)\psi(x)=\lambda\phi([x,y])\quad\text{for all }x,y\in L.
\tag{1}
\]
If \(\phi\) annihilates \(Z=\bigwedge^2V\), then both sides vanish identically. Suppose instead that \(\phi|_Z\neq0\). The projection \(\ker\phi\to V\) is surjective: for any prescribed \(v\in V\), choose a central correction to make \(\phi(v+z)=0\). Since the bracket of \(V\) spans \(Z\), there exist \(x,y\in\ker\phi\) with \(\phi([x,y])\neq0\). Equation (1) therefore forces \(\lambda=0\). For \(z\in Z\) with \(\phi(z)\neq0\), take \(x=z\) in (1); because \(\psi(z)=0\), this gives \(\psi(y)=0\) for every \(y\). Conversely, \(\lambda=\psi=0\) makes (1) true. This proves the classification over every field.

Write \(u=v+z\) and \(\phi=(\phi_V,\phi_Z)\) under the direct sums. In the second case the conditions are precisely
\[
\phi_Z\neq0,\qquad \phi_Z(v\wedge V)=0,\qquad
\phi_V(v)+\phi_Z(z)=0.
\tag{2}
\]
If \(v=0\), the vector \(z\) must be nonzero. For each of \(q^c-1\) choices of \(\phi_Z\), exactly \(q^{c-1}-1\) nonzero \(z\)'s satisfy its zero condition, and \(\phi_V\) is arbitrary among \(q^n\) choices. Thus the central-image number of nonzero pairs \((u,\phi)\) is \(q^n(q^c-1)(q^{c-1}-1)\).

If \(v\neq0\), its wedge map \(V\to Z\), \(w\mapsto v\wedge w\), has kernel exactly \(kv\), hence rank \(n-1\). Consequently the space of \(\phi_Z\) annihilating its image has dimension \(c-n+1\), giving \(q^{c-n+1}-1\) nonzero choices. There are \(q^n-1\) choices of \(v\), \(q^n\) choices of \(\phi_V\), and, because \(\phi_Z\neq0\), precisely \(q^{c-1}\) solutions \(z\) of the last equation in (2). This contributes \((q^n-1)q^{m-1}(q^{c-n+1}-1)\) pairs.

In the first case, \(\phi_V\) has \(q^n-1\) nonzero choices, \(u\) has \(q^m-1\) choices, and \(\phi_Z=0\). Every nonzero rank-one operator has exactly \(q-1\) factorizations \((tu,t^{-1}\phi)\), so dividing each disjoint pair count by \(q-1\) proves the formula. Since \(N^2=\lambda N\) and the trace of \(N\) is \(\lambda\), a non-square-zero map occurs exactly when \(\phi_Z=0\) and \(\phi_V(v)\neq0\). Its number is \((q^n-1)(q^n-q^{n-1})q^c/(q-1)=(q^n-1)q^{m-1}\).

For \(n=2\), \(c=1\) makes both non-character contributions zero. For \(n\ge3\), taking \(u=e_1\) and \(\phi\) supported on \(e_2\wedge e_3\) gives a noncentral-image Nijenhuis map not annihilating \([L,L]\). For fixed \(q\), the ratio of the noncentral non-character count to the character count is
\[
\frac{q^{m-1}(q^{c-n+1}-1)}{q^m-1}\sim q^{c-n}\quad(n\to\infty),
\]
which diverges. Hence the non-character fraction tends to one, proving the final assertion.

## Verification
A standalone finite-field checker is included as `verification/verify.py` and runs with Python 3.10+ and NumPy. It evaluates the tensor identity (1) for every nonzero factor pair in five prime-field configurations, verifies the predicted non-character and non-square-zero counts, and independently evaluates the original operator Nijenhuis identity for all rank-one factors over \(\mathbb F_4\) with two generators. The exhaustive configurations are \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3),(2,4)\), totaling \(554023\) tested factor pairs. The completion marker is `NIJENHUIS_RANK_ONE_FREE_CLASS_TWO_OK 6 554023`. These finite checks corroborate, but do not replace, the argument for all dimensions and finite fields.

## Relationship to prior work
Liu–Sheng–Zhou–Bai (arXiv:1601.02356v1, first posted 2016-01-11) develops Nijenhuis operators and their deformation interpretation, including the ordinary Lie-algebra case. It does not give the rank-one finite-field classification or its exact free-two-step counts. Farinati–Jancsa (arXiv:1607.00300v1) studies Lie **bialgebra cobrackets** on two-step nilpotent graph algebras, including free two-step examples; this is a different type of map and condition. Zhikhareva (arXiv:2410.10536v1), Example 2, includes a general central-image, square-zero construction, which overlaps part of our central-image case; its main classification concerns **regular semisimple** operators on real and complex three-dimensional algebras, not rank-one operators across finite fields and free-two-step dimensions. The present classification and enumeration explicitly include noncentral-image maps not factoring through the abelianization, which are not implied by those constructions. No exhaustive historical-priority certification is claimed.

## Limitations
The theorem is a rank-one census, not a classification of higher-rank Nijenhuis maps, their full variety or automorphism-conjugacy orbits. The affine/algebraic scheme structure of the rank-one solution locus is not determined. The asymptotic statement holds for fixed \(q\) and increasing generator dimension. Priority remains subject to unpublished or unindexed equivalent rank-one classifications. No independent external mathematical audit has been performed.

## References
1. J. Liu, Y. Sheng, Y. Zhou, C. Bai, *Nijenhuis operators on \(n\)-Lie algebras*, arXiv:1601.02356v1 (2016-01-11), https://arxiv.org/abs/1601.02356.
2. M. A. Farinati, A. P. Jancsa, *Lie bialgebra structures on 2-step nilpotent graph algebras*, arXiv:1607.00300v1 (2016-07-01), https://arxiv.org/abs/1607.00300.
3. E. S. Zhikhareva, *Three-dimensional Lie algebras admitting regular semisimple algebraic Nijenhuis operators*, arXiv:2410.10536v1 (2024-10-14), https://arxiv.org/abs/2410.10536.
