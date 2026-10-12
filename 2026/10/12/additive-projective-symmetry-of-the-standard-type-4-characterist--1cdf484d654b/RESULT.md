# Additive projective symmetry of the standard type-(4) characteristic-two quartic
## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\), and consider
\[
C=V\!\left(y^{4}+xz^{3}+x^{3}z\right)\subset\mathbf P^{2}_{k}.
\]
This is the \(c=1\) member of the type-(4) pencil studied by Hilario--Stöhr. Its full group of projective \(k\)-automorphisms is
\[
\operatorname{Stab}_{\operatorname{PGL}_{3}(k)}(C)
 =\{T_{\lambda}:\lambda\in k\}\cong\mathbf G_a(k),
\]
with
\[
T_{\lambda}[x:y:z]=
\big[(1+\lambda^{4})x+\lambda^{4}z:\
y+(\lambda+\lambda^{2})(x+z):\
\lambda^{4}x+(1+\lambda^{4})z\big].
\]
The unique singular point is \(p=[1:0:1]\). Every \(T_{\lambda}\) fixes \(p\) and the strange point \([0:1:0]\), and the action on \(C_{\mathrm{sm}}\) is simply transitive. Thus this singular quartic is a projectively equivariant one-point compactification of the additive group.

## Assumptions and scope
The field \(k\) is algebraically closed of characteristic \(2\). “Projective automorphism” means an element of \(\operatorname{PGL}_{3}(k)\) preserving the displayed plane curve. The statement is about the group of \(k\)-points of the projective stabilizer; it does not assert that the stabilizer group scheme is reduced, and it does not classify abstract automorphisms of the singular curve that need not extend to \(\mathbf P^{2}\).

Hilario--Stöhr study the pencil
\[
y^{4}+xz^{3}+c x^{3}z=0.
\]
For \(c\neq0\), they describe the member as an integral rational quartic with one unibranch multiplicity-two singularity, and they show that it is strange and that each smooth tangent is a non-ordinary inflection tangent. The claim here specializes to \(c=1\) and determines the complete projective symmetry group of that member.

## Proof
Write
\[
F(x,y,z)=y^{4}+xz^{3}+x^{3}z.
\]
In characteristic \(2\),
\[
F_x=z(x+z)^{2},\qquad F_y=0,\qquad F_z=x(x+z)^{2}.
\]
If \(x=0\) or \(z=0\), the remaining nonzero partial derivative excludes singularity. Otherwise the two partials force \(x=z\), and then \(F=0\) forces \(y=0\). Hence the only singular point is
\[
p=[1:0:1].
\]

A normalization is
\[
\nu:\mathbf P^{1}\longrightarrow C,
\qquad
[u:v]\longmapsto
[u^{4}:uv(u+v)^{2}:v^{4}].
\]
Indeed, the defining equation vanishes because
\[
\big(uv(u+v)^{2}\big)^{4}=u^{4}v^{4}(u+v)^{8}
=u^{12}v^{4}+u^{4}v^{12}.
\]
On the chart \(u\neq0\), put \(t=v/u\), \(Y=y/x\), and \(Z=z/x\). Then
\[
Y=t(1+t)^{2},\qquad Z=t^{4},
\]
and in the function field
\[
t=\frac{Y(1+Z)}{1+Z+Y^{2}}.
\]
Thus \(\nu\) is birational, hence it is the normalization. The unique preimage of \(p\) is
\[
q=[1:1].
\]

Pulling hyperplanes back by \(\nu\) gives the three-dimensional linear series
\[
V=\langle u^{4},\ v^{4},\ uv(u+v)^{2}\rangle\subset H^{0}(\mathbf P^{1},\mathcal O(4)).
\]
Any projective automorphism of \(C\) lifts uniquely to an automorphism of the normalization, fixes \(q\), and preserves \(V\). Conversely, every element of \(\operatorname{PGL}_{2}(k)\) with those two properties induces a projective automorphism of the plane model.

Represent such a normalization automorphism by
\[
g=\begin{pmatrix}a&b\\ c&d\end{pmatrix},
\qquad \Delta=ad+bc\neq0,
\]
where the plus sign occurs because the characteristic is \(2\). Fixing \(q=[1:1]\) is equivalent to
\[
a+b+c+d=0.
\]
The fourth powers \((au+bv)^{4}\) and \((cu+dv)^{4}\) automatically lie in \(\langle u^{4},v^{4}\rangle\). Expanding the third basis element after substitution, the coefficient of \(u^{2}v^{2}\) is
\[
\Delta(ab+cd).
\]
The difference between its \(u^{3}v\) and \(uv^{3}\) coefficients is divisible by \(a+b+c+d\), so it vanishes once \(q\) is fixed. Consequently preservation of \(V\) is equivalent to
\[
ab+cd=0.
\]
Using \(d=a+b+c\), this becomes
\[
(a+c)(b+c)=0.
\]
The branch \(a=c\) would force \(d=b\) and hence \(\Delta=0\), so it is impossible. Therefore
\[
b=c,\qquad d=a.
\]
After multiplying the matrix by a scalar, normalize \(a+b=1\) and write \(b=\lambda\). Every admissible normalization automorphism is therefore
\[
g_{\lambda}=
\begin{pmatrix}1+\lambda&\lambda\\ \lambda&1+\lambda\end{pmatrix}.
\]
Substitution into the three generators of \(V\) gives exactly the projective transformation \(T_{\lambda}\) displayed above. In particular, no additional projective automorphisms exist.

The group law is additive. Indeed,
\[
g_{\lambda}g_{\mu}=g_{\lambda+\mu},
\]
and the same identity holds for the induced \(T_{\lambda}\). For a direct geometric description, on \(\mathbf P^{1}\setminus\{q\}\) use
\[
r=\frac{v}{u+v}.
\]
Because \(g_{\lambda}\) fixes \(u+v\) and sends \(v\) to \(v+\lambda(u+v)\), it sends
\[
r\longmapsto r+\lambda.
\]
Hence the group acts simply transitively on \(\mathbf P^{1}\setminus\{q\}\), and therefore on \(C_{\mathrm{sm}}\).

## Verification
The accompanying `verification/verify.py` performs exact symbolic calculations over characteristic \(2\). It checks the normalization identity, the rational inverse identity, the partial derivatives, the coefficient condition \(\Delta(ab+cd)\), the reduction to the symmetric normalization matrices, the formula for \(T_{\lambda}\), preservation of \(F\), the additive group law, and the translation formula for \(r\). The calculation uses only symbolic polynomial identities; no finite-field enumeration is used to stand in for the algebraically closed-field statement.

## Relationship to prior work
Hilario--Stöhr classify the relevant regular genus-three curves and their universal fibrations, and in the type-(4) family they identify the geometric quartics as strange rational curves with one unibranch singularity and non-ordinary inflection tangents. Their paper also treats isomorphisms and automorphisms of the regular function fields over the original, generally imperfect, ground field. Those statements do not determine the projective stabilizer of the singular geometric member after passage to an algebraic closure: after that passage its normalization is \(\mathbf P^{1}\), and the question becomes which normalization automorphisms preserve the specific three-dimensional quartic linear series. The calculation above determines exactly that subgroup.

Searches for the exact quartic equation, its normalization, “projective stabilizer”, “automorphism group”, “additive group”, and “strange quartic” formulations found no prior statement identifying this full projective stabilizer or the simple transitivity of its action on the smooth locus. General literature on strange curves supplies tangent-line structure but does not imply the symmetry calculation.

## Limitations
The result concerns only the standard \(c=1\) member of the Hilario--Stöhr type-(4) pencil, equivalently any member explicitly carried to this plane model. It does not classify stabilizers of every parameter value in all five quartic families. It also does not determine possible infinitesimal nonreduced structure of the stabilizer group scheme, nor the full abstract automorphism group of the singular curve when automorphisms are not required to extend projectively.

## References
C. Hilario and K.-O. Stöhr, *Fibrations by plane projective rational quartic curves in characteristic two*, arXiv:2409.05464v1, first posted 2024-09-09. See Theorem 1.1 and Sections 4–5 for the type-(4) family and the pencil containing \(C\).

C. Hilario and K.-O. Stöhr, *Fibrations by plane quartic curves with a canonical moving singularity*, arXiv:2306.08579, for the predecessor classification and the distinction between automorphisms over the original ground field and geometry after base extension.
