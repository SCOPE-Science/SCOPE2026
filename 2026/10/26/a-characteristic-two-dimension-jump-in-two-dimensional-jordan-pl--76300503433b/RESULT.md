# A characteristic-two dimension jump in two-dimensional Jordan-plane representations

## Finding

Let \(k\) be a field and let \(R_k=k\langle x,y\rangle/(xy-yx-y^2)\) be the Jordan plane. Define its **reduced** two-dimensional representation variety by the set of matrix pairs
\[
\mathcal J_2(k)=\{(X,Y)\in M_2(k)^2:XY-YX=Y^2\}.
\]
Geometric components below mean components after scalar extension to an algebraic closure of \(k\). The following gives the complete component structure, intersections, and finite-field point count, in every characteristic.

**(I) Characteristic different from two.** There are exactly two geometrically irreducible components, both of dimension \(4\):

* \(F=\{(X,0):X\in M_2(k)\}\), an affine \(4\)-space;
* \(C\), the Zariski closure of the irreducible locus \(Y\ne0\), \(Y^2=0\), and \(X\in kI+kY\), of dimension \(4\).

Their reduced intersection is
\[
C\cap F=\{(X,0): (\operatorname{tr}X)^2-4\det X=0\},
\]
an irreducible \(3\)-dimensional locus of matrices with repeated eigenvalue.

**(II) Characteristic two.** There are exactly two geometrically irreducible components of dimensions \(4\) and \(5\), so this reduced representation variety is **not equidimensional**. One component is the same affine space \(F\). The other is the irreducible hypersurface \(C\) in the six-dimensional linear subspace \(\operatorname{tr}X=\operatorname{tr}Y=0\), with coordinates
\[
X=\begin{pmatrix}u&v\\w&u\end{pmatrix},\qquad
Y=\begin{pmatrix}a&b\\c&a\end{pmatrix}
\]
and equation
\[
a^2+bc+vc+bw=0.
\]
Its reduced intersection with \(F\) is the affine \(3\)-space
\[
C\cap F=\{(X,0):\operatorname{tr}X=0\}.
\]
The singular locus of the hypersurface \(C\), considered with its reduced hypersurface structure, is precisely the affine line given by \(a=b=c=v=w=0\), with \(u\) free.

**(III) Finite fields.** For every prime power \(q\), including nonprime fields,
\[
\#\mathcal J_2(\mathbb F_q)=
\begin{cases}
2q^4-q^2,&q\text{ odd},\\
q^5+q^4-q^3,&q\text{ even}.
\end{cases}
\]
For odd \(q\), the individual component counts are \(\#C=q^4+q^3-q^2\), \(\#F=q^4\), and \(\#(C\cap F)=q^3\); for even \(q\), they are \(\#C=q^5\), \(\#F=q^4\), and \(\#(C\cap F)=q^3\).

## Assumptions and scope

Here \(M_2(k)\) denotes all \(2\)-by-\(2\) matrices, not just invertible or traceless ones. Pairs \((X,Y)\) are **labelled** representations; no quotient by simultaneous conjugation is taken. Equations and components refer to the set-theoretically defined reduced algebraic variety; no assertion about the possibly nonreduced representation scheme is made. For a non-algebraically closed base field, component dimensions and irreducibility mean geometric statements after base change; finite-field counts count rational labelled pairs.

The first calendar-day-verified source for this question was publicly available on 2008-02-12 (Iyudu, arXiv:0802.1545v1). The positive-characteristic nonnilpotence possibility is already recognized in that literature and is not claimed as a new observation; the result here is the explicit characteristic-two component jump, geometry, and rank-free complete point count.

## Proof

### 1. Reduction by the centralizer

Let \(Y\) be nonscalar. Its minimal polynomial has degree two, so its matrix centralizer is exactly \(kI+kY\), of dimension two over \(k\). The trace pairing \((S,T)\mapsto\operatorname{tr}(ST)\) on \(M_2(k)\) is nondegenerate in **all** characteristics. Consequently, the equation \([X,Y]=Y^2\) is solvable precisely when \(Y^2\) pairs to zero with both \(I\) and \(Y\), that is,
\[
\operatorname{tr}(Y^2)=\operatorname{tr}(Y^3)=0.
\]
Whenever solvable, its solutions form one affine translate of \(kI+kY\), hence an affine plane. This observation also supplies a uniform finite-field fiber count of \(q^2\) over any admissible nonscalar \(Y\).

### 2. Characteristic different from two

Put \(t=\operatorname{tr}Y\) and \(d=\det Y\). Cayley–Hamilton gives
\[
\operatorname{tr}(Y^2)=t^2-2d,
\qquad
\operatorname{tr}(Y^3)=t^3-3td.
\]
If both vanish and the characteristic is not two, then \(d=t^2/2\), so
\[
0=t^3-3t(t^2/2)=-t^3/2.
\]
Since a field has no nonzero nilpotents, \(t=d=0\). By Cayley–Hamilton, \(Y^2=0\). Conversely, for every nonzero square-zero \(Y\), the defining equation is \([X,Y]=0\), so \(X=\alpha I+\beta Y\), uniquely. A nonzero square-zero two-dimensional matrix has rank one, and all such matrices form one geometrically irreducible \(\mathrm{GL}_2\)-orbit of dimension two. The affine centralizer fibers have dimension two, so the locus \(Y\ne0\) is geometrically irreducible of dimension four, with closure \(C\). The locus \(Y=0\) is the affine four-space \(F\). Since generic matrices \(X\) have distinct eigenvalues, \(F\not\subset C\); and since \(C\) contains nonzero \(Y\), \(C\not\subset F\). Thus they are precisely the two components.

Every \(X=\alpha I+\beta Y\) on \(Y\ne0\) has repeated eigenvalue. The repeated-eigenvalue equation is closed, hence imposes the stated discriminant equation on \(C\cap F\). Conversely, over an algebraic closure any matrix with repeated eigenvalue is \(X=\alpha I+N\) with \(N^2=0\): for \(N\ne0\) the pairs \((X,tN)\) with \(t\ne0\) lie in the nonzero-\(Y\) stratum and specialize to \((X,0)\); for \(N=0\) the same follows by first specializing nonzero nilpotent \(N\to0\). The discriminant locus is irreducible of dimension three (the affine family of scalar parts of nilpotents). This identifies the reduced intersection.

Over \(\mathbb F_q\) with \(q\) odd, there are exactly \(q^2-1\) nonzero square-zero two-by-two matrices (choose image/kernel line among \(q+1\) possibilities and a nonzero homomorphism of the one-dimensional quotient to that line, giving \((q+1)(q-1)\)). Each has \(q^2\) commuting matrices \(X\). The zero matrix \(Y\) has all \(q^4\) choices for \(X\), yielding \(q^4+(q^2-1)q^2=2q^4-q^2\). The repeated-eigenvalue intersection contains \(q\cdot q^2=q^3\) matrices \(X=\alpha I+N\), which also yields the claimed component count.

### 3. Characteristic two

Write \(X=\left(\begin{smallmatrix}u&v\\w&z\end{smallmatrix}\right)\) and \(Y=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\). In characteristic two, \(\operatorname{tr}(Y^2)=(\operatorname{tr}Y)^2\), so any solution forces \(d=a\). If \(Y=aI\) is scalar, then \([X,Y]=0\), so the defining equation forces \(a=0\). For a nonscalar trace-zero \(Y=\left(\begin{smallmatrix}a&b\\c&a\end{smallmatrix}\right)\), at least one of \(b,c\) is nonzero. The off-diagonal entries of \([X,Y]\) are \((u+z)b\) and \((u+z)c\), whereas \(Y^2=(a^2+bc)I\). Hence \(u=z\). The remaining diagonal equation is exactly
\[
vc+bw=a^2+bc,
\]
or the displayed hypersurface equation. Conversely that equation, together with \(\operatorname{tr}X=\operatorname{tr}Y=0\), implies the full matrix identity. If \(Y=0\), arbitrary \(X\) works. Therefore the entire reduced solution set is the union \(F\cup C\) of the two explicitly stated closed sets.

The hypersurface polynomial \(f=a^2+bc+vc+bw\) is geometrically irreducible. Over the algebraic closure, regard it as a polynomial of degree one in \(v\) with coefficients in \(k[a,b,c,w,u]\). Its leading coefficient \(c\) and constant coefficient \(a^2+bc+bw\) are relatively prime, since \(c\nmid a^2+bw\). Gauss's lemma implies irreducibility over this UFD. Hence \(C\) is an irreducible hypersurface of dimension five, while \(F\) is irreducible of dimension four; neither contains the other. Their intersection is obtained by setting \(a=b=c=0\) inside \(C\), with free \(u,v,w\), exactly the stated three-space. The partial derivatives of \(f\) in characteristic two are \(\partial_bf=c+w\), \(\partial_cf=b+v\), \(\partial_vf=c\), \(\partial_wf=b\), and \(\partial_af=0\); imposing their vanishing and \(f=0\) gives \(a=b=c=v=w=0\), so the singular locus is the asserted affine line.

For finite even \(q\), trace-zero nonscalar matrices \(Y\) number \(q^3-q\), because \(a,b,c\) are free and exactly the \(q\) choices \(b=c=0\) are scalar. For each nonscalar \(Y\), the equation is one nontrivial affine linear relation in \(v,w\), while \(u\) is free; there are therefore \(q^2\) matrices \(X\). At \(Y=0\), there are \(q^4\) unrestricted matrices \(X\). Thus the count is \(q^4+(q^3-q)q^2=q^5+q^4-q^3\). On \(C\), the \(q^3-q\) nonscalar trace-zero choices each give \(q^2\) choices of \(X\), while \(Y=0\) gives \(q^3\) trace-zero \(X\), totaling \(q^5\).

### 4. A nonnilpotent positive-characteristic witness

In characteristic two, set
\[
X=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
Y=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
Direct multiplication gives \(XY-YX=Y^2=I\), although \(Y\) is invertible. This illustrates why characteristic-zero nilpotent-stratum arguments cannot be transferred to characteristic two without additional hypotheses.

## Verification

The included standalone `verify.py` enumerates all \(2\)-by-\(2\) matrices over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\), explicitly computes both matrix products, checks \([X,Y]=Y^2\), and independently counts the two stated components and their intersection. It also checks the size of every fixed-\(Y\) fiber rather than testing just aggregate totals. The observed total counts were respectively \(40,153,1216,1225,4753\), all matching the proved formulas; the marker is `JORDAN_PLANE_MODULAR_2X2_OK`. The full-field statements follow from the proof, not from the finite checks. Run `python verify.py` with Python 3; no third-party packages are required.

## Relationship to prior work

Iyudu's 2005 MPIM preprint (MPIM 2005-20), 2008 Jordanian-algebra study (arXiv:0802.1545v1), and 2009 component note (arXiv:0903.3820) is foundational background on representation theory and already notes that nilpotence of the image of \(y\) fails without the characteristic-zero assumption. The 2012 preprint *Representation spaces of the Jordan plane* (arXiv:1209.0746v1; published 2014) proves an equidimensionality/component theorem for the characteristic-zero setting: its Section 2 explicitly assumes algebraically closed characteristic zero and the later component theorem uses that framework. This work does **not** challenge that correctly scoped theorem or claim novelty for the existence of nonnilpotent characteristic-two images. Instead, it explicitly calculates the reduced \(2\)-dimensional modular representation variety, its characteristic-two non-equidimensional component, singular line, and finite-field census, and contrasts it with the odd-characteristic geometry. Broad claims of unique publication priority are not made.

## Limitations

Only matrix size two is classified. This determines labelled rational points, not simultaneous-conjugacy orbits or moduli stacks. The theorem is set-theoretic/reduced; no assertion about nilpotent structure of the defining representation scheme or its deformation theory is implied. The classification in odd characteristic does not imply anything about all higher dimensions in positive characteristic. Independent mathematical audit has not been performed. A broader literature result not retrieved here might imply part of the enumeration; originality should therefore be interpreted relative to the inspected sources, not as a proof of absolute priority.

## References

1. N. Iyudu, *Representation theory of Jordanian algebra*, arXiv:0802.1545v1, first submitted 2008-02-12. https://arxiv.org/abs/0802.1545 .
2. N. Iyudu, *Classification of finite dimensional representations of one noncommutative quadratic algebra*, MPIM Preprint Series 2005 (20), publication day not verified. https://archive.mpim-bonn.mpg.de/id/eprint/1809/ .
3. N. Iyudu, *Irreducible components of the Jordan varieties*, arXiv:0903.3820, first publicly submitted 2009-03-23. https://arxiv.org/abs/0903.3820 .
4. N. K. Iyudu, *Representation spaces of the Jordan plane*, arXiv:1209.0746v1, first submitted 2012-09-04; *Communications in Algebra* **42** (2014), 3507–3540. https://arxiv.org/abs/1209.0746 .
