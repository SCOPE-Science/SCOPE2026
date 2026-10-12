# Witt-type jumps in local derivations of three-dimensional nilpotent associative algebras

## Finding

Let \(K\) be a field of characteristic different from \(2\), and let \(d\in K^\times\). Define the three-dimensional, commutative, associative, nilpotent algebra \(A_d\) with basis \(e_1,e_2,z\) and multiplication
\[
e_1^2=z,\qquad e_2^2=d z,
\]
all other basis products being zero. In particular, \(A_d^2=Kz=\operatorname{Ann}(A_d)\) and \(A_d^3=0\). Write
\[
J_d=\begin{pmatrix}0&-d\\1&0\end{pmatrix},
\qquad J_d^2=-dI.
\]

Every derivation of \(A_d\), in the displayed basis and column convention, is uniquely
\[
D(a,b,u,v)=
\begin{pmatrix}
a&-db&0\\
b&a&0\\
u&v&2a
\end{pmatrix},\qquad a,b,u,v\in K.
\]
Thus \(\dim_K\operatorname{Der}(A_d)=4\).

A **local derivation** means a *linear* map \(\Delta:A_d\to A_d\) such that, for every \(w\in A_d\), there is some derivation \(D_w\) with \(\Delta(w)=D_w(w)\). Its complete classification is the following Witt-type dichotomy.

* If \(-d\notin(K^\times)^2\), then **every** matrix
  \[
  \Delta=\begin{pmatrix}
  r&s&0\\t&h&0\\u&v&c
  \end{pmatrix},\qquad r,s,t,h,u,v,c\in K,
  \]
  is a local derivation, and these are all of them. Hence \(\dim_K\operatorname{LDer}(A_d)=7\).
* If \(-d\in(K^\times)^2\), then the local derivations are **exactly**
  \[
  \Delta=\begin{pmatrix}
  a&-db&0\\b&a&0\\u&v&c
  \end{pmatrix},\qquad a,b,u,v,c\in K,
  \]
  so \(\dim_K\operatorname{LDer}(A_d)=5\).

Despite this jump, **every linear 2-local derivation is an ordinary derivation**: if a linear \(\Delta\) is locally represented by one derivation on each prescribed *pair* of elements, then \(\Delta\) is one of the four-parameter matrices \(D(a,b,u,v)\). This does *not* assert the same of nonlinear 2-local derivations: explicit nonlinear examples exist.

Consequently, over any odd finite field \(\mathbf F_q\),
\[
\#\operatorname{Der}(A_d)=q^4,
\qquad
\#\operatorname{LDer}(A_d)=
\begin{cases}
q^7,&-d\text{ nonsquare},\\
q^5,&-d\text{ square},
\end{cases}
\qquad
\#\operatorname{Lin2LDer}(A_d)=q^4.
\]

The Witt jump has a scalar-extension consequence. If \(-d\) is nonsquare in \(K\), the linear map
\[
\Delta(e_1)=e_1,\qquad\Delta(e_2)=0,\qquad\Delta(z)=0
\]
is local over \(K\), but ceases to be local over the quadratic splitting extension \(K(\sqrt{-d})\). Thus the local-derivation property need **not** survive separable extension of scalars.

## Assumptions and scope

The starting literature is Abdurasulov–Ayupov–Yusupov, *Local and 2-local derivations on filiform associative algebras*, first posted on 24 May 2023 (arXiv:2305.15339v1; the openly readable v2 is dated 26 June 2023). Its first listed MSC is **17A32**. In the paper's Theorem 2.8, the three-dimensional complex algebra \(\mathcal A_2\) has \(e_1e_2=e_2e_1=e_3\); Theorem 4.1 and its adjacent dimension table give derivation dimension \(4\) and local-derivation dimension \(5\). This is precisely the **split** case of the quadratic-bilinear family above. The result here determines the missing nonsplit arithmetic behavior, the fate of local maps under scalar extension, and the linear 2-local boundary. Its claims are not about arbitrary nondegenerate bilinear forms of higher dimension.

The condition \(-d\in(K^\times)^2\) is equivalent to isotropy of the nondegenerate binary quadratic form
\[
Q_d(x,y)=x^2+d y^2.
\]
No algebraic-closedness, infinitude, or characteristic-zero hypothesis is used.

## Proof

**1. Derivations.** Put \(V=Ke_1\oplus Ke_2\) and identify \(A_d=V\oplus Kz\). The product of \(v,w\in V\) is \(B_d(v,w)z\), where \(B_d\) has Gram matrix \(\operatorname{diag}(1,d)\). Since \(A_d^2=Kz\), every derivation has
\[
D(v)=Mv+\phi(v)z,\qquad D(z)=cz
\]
with \(M\in\operatorname{End}(V)\) and \(\phi\in V^*\). The Leibniz rule on \(V\times V\) is exactly
\[
M^{\mathsf T}\operatorname{diag}(1,d)+\operatorname{diag}(1,d)M
=c\operatorname{diag}(1,d).
\]
Comparing entries (using \(2\ne0\)) gives
\[
M=aI+bJ_d,\qquad c=2a,
\]
with arbitrary \(a,b\). Conversely these formulas satisfy the Leibniz rule on all basis pairs, proving the displayed derivation classification.

**2. Reduction of locality.** Because each derivation carries \(z\) to a multiple of \(z\), a linear local derivation necessarily has block form
\[
\Delta(v+tz)=Nv+\psi(v)z+t\gamma z,
\]
for \(N\in\operatorname{End}(V)\), \(\psi\in V^*\), \(\gamma\in K\). The only possible obstruction to locality is
\[
Nv\in\operatorname{span}_K\{v,J_dv\}\qquad\text{for every }v\in V.
\tag{1}
\]
Indeed, necessity follows by comparing the \(V\)-components of \(\Delta(v)\) and \(D_v(v)\). For sufficiency, if \(v\ne0\), choose \(a,b\) with \((aI+bJ_d)v=Nv\), and then choose \(\phi\in V^*\) with
\[
\phi(v)=\psi(v)+t(\gamma-2a).
\]
Such a functional exists because \(v\ne0\), and the corresponding derivation agrees with \(\Delta\) at \(v+tz\). For a pure element \(tz\), choose \(a=\gamma/2\). This proves (1) is necessary and sufficient.

**3. The quadratic-form dichotomy.** In the basis \(e_1,e_2\),
\[
\det(v,J_dv)=Q_d(v).
\]
If \(-d\) is nonsquare, \(Q_d(v)\ne0\) for every \(v\ne0\). Hence \(v,J_dv\) span all of \(V\), and (1) places no constraint on \(N\). The seven coefficients \(r,s,t,h,u,v,c\) above are free.

If \(-d\) is square, \(J_d\) has two distinct eigenvalues \(\pm\sqrt{-d}\). Its two eigenlines are exactly the nonzero isotropic directions of \(Q_d\). On an eigenline, the span in (1) is that same line; therefore \(N\) must preserve both eigenlines. Conversely every endomorphism preserving both is diagonal in their common eigenbasis, hence lies in \(KI+KJ_d\), and satisfies (1). This gives the five-parameter family. The dimensions follow because all parameter expressions are injective.

**4. Linear 2-local rigidity.** Let \(\Delta\) be linear and 2-local. In particular it is local, so write it in the block form of Step 2. A derivation witnessing \(\Delta\) simultaneously on \(e_1\) and \(e_2\) has \(V\)-block \(N\); hence \(N=aI+bJ_d\) for some \(a,b\). Now choose a derivation \(D'\) witnessing \(\Delta\) at the *pair* \(e_1\) and \(e_1+z\). Subtracting these two equalities forces
\[
D'(z)=\Delta(z)=\gamma z.
\]
The \(V\)-component of \(D'(e_1)\) is \(Ne_1\). Since \(e_1,J_de_1\) are a basis, the coefficients of the \(V\)-block of \(D'\) are uniquely \(a,b\). Therefore \(\gamma=2a\). The central terms \(\psi(e_1),\psi(e_2)\) are unrestricted, and the resulting map is precisely the derivation \(D(a,b,\psi(e_1),\psi(e_2))\). The converse is immediate.

For clarity, nonlinear 2-local derivations still exist. Define \(f:V\to K\) by
\[
f(xe_1+ye_2)=
\begin{cases}
x,&y=0,\\
0,&y\ne0.
\end{cases}
\]
This function is homogeneous of degree one but not additive. The map \(\Theta(v+tz)=f(v)z\) is not linear. Given any pair of vectors in \(V\), homogeneity allows a single linear functional \(\phi\) to interpolate \(f\) at both (if independent, prescribe the two values; if dependent, use homogeneity). The central-valued derivation \(D(v)=\phi(v)z,\ D(z)=0\) then witnesses both values. Thus \(\Theta\) is a genuinely nonlinear 2-local derivation, consistent with the source's general existence results.

**5. Arithmetic and base change.** Over \(\mathbf F_q\), a \(k\)-dimensional vector space of linear maps has \(q^k\) elements; apply Steps 1–4 to obtain the count. If \(-d\) is nonsquare over \(K\), the displayed diagonal map has \(N=\operatorname{diag}(1,0)\) and is local by Step 3. Over the splitting extension \(L=K(\sqrt{-d})\), both eigenlines of \(J_d\) exist, and \(N\) fails to preserve them (its eigenlines are the coordinate axes). By (1), the scalar-extended map is not local. Since \(\operatorname{char}K\ne2\), this quadratic extension is separable.

## Verification

The standalone `artifacts/verify.py` symbolically reconstructs the product and the four-parameter derivation formulas, proves the determinant identity, and checks the Leibniz rule on all basis pairs. It enumerates all \(q^4\) possible \(V\)-blocks \(N\) over \(\mathbf F_3,\mathbf F_5,\mathbf F_7,\mathbf F_{11}\), for every \(d\ne0\), and directly tests the pointwise evaluation-span condition (1), obtaining exactly the predicted split/nonsplit counts. In addition it checks **every** candidate \(3\times3\) linear map preserving \(Kz\) over \(\mathbf F_3\) against the actual pointwise sets attained by all derivations, independently confirming that there are \(2187\) local maps in the anisotropic case and \(243\) in the split case, with \(81\) derivations in either case. The checker returns `VERIFY_OK`.

Finite-field computations are confirmatory; the proof for all eligible fields is Steps 1–5.

## Relationship to prior work

Abdurasulov–Ayupov–Yusupov's Theorem 4.1 and dimension table explicitly give \(4\) derivations' **dimension** and local-derivation dimension \(5\) for their three-dimensional complex algebra \(\mathcal A_2\). That algebra is the split binary-form case, so the split branch over an algebraically closed field is **prior coverage**, not claimed as new. The new finding is the exact arbitrary-field Witt dichotomy, including the seven-dimensional anisotropic locus, the failure of local derivations to descend/ascend naively under scalar extension, and the rigidity of *linear* 2-local derivations. Anisotropic local maps do not become local over the algebraic closure, which explains why the source's complex classification cannot imply the nonsplit claim.

The source's Theorem 4.3 constructs nonlinear 2-local derivations on complex three-dimensional nilpotent associative algebras. The explicit nonlinear witness above is included only to delimit the **linear** assertion; the existence of nonlinear witnesses is not offered as independent novelty.

Searches for quadratic-form and Witt formulations of local derivations, anisotropic finite-field local derivations, algebraic reflexive hulls of conformal orthogonal operators, exact finite-field counts, and equivalent three-dimensional nilpotent multiplication tables found no source stating the nonsplit branch or the base-change failure. A later journal edition of the same paper has the same abstract but was not compared line by line against its openly available full preprint; this remains an explicit literature risk. Search failure does not establish absolute originality.

## Limitations

The theorem concerns three-dimensional associative algebras with one-dimensional annihilator and a nondegenerate **symmetric** binary multiplication form; it does not classify higher-dimensional algebras, degenerate forms, or arbitrary nonsymmetric bilinear forms. Characteristic \(2\) is excluded. The finite-field result counts **linear** local maps and **linear** 2-local maps; it does not count all nonlinear 2-local maps. Prior work already covers the split complex case; the originality claim is the nonsplit arithmetic and scalar-extension boundary.

## References

1. K. Abdurasulov, Sh. Ayupov, B. Yusupov, “Local and 2-local derivations on filiform associative algebras,” arXiv:2305.15339v1 (24 May 2023), v2 (26 June 2023); later *Journal of Algebra and Its Applications* 24 (2025), 2550242, DOI `10.1142/S0219498825502421`.
2. Sh. Ayupov, K. Kudaybergenov, B. Omirov, “Local and 2-local derivations and automorphisms on simple Leibniz algebras,” *Bulletin of the Malaysian Mathematical Sciences Society* 43 (2020), 2199–2234, DOI `10.1007/s40840-019-00799-5`. (Context for nonlinear 2-local interpolation constructions.)
