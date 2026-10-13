# The non-McCoy witness has a regular local model and a nonseparated power filtration

## Finding

Let \(k=\overline{\mathbb Q}\), \(A=k[x,y,z]\), and \(\mathfrak m=(x,y,z)\). In the function-ring construction of Tran and Nguyen, let \(X\subset k^3\setminus\{0\}\), \(\Omega=X\times\mathbb N\), \(D=k^{(\Omega)}\), let \(\iota:A\to k^\Omega\) repeat restriction to \(X\) along each infinite fiber, and put \(R=\iota(A)+D\). For the paper's witness
\[
I=(\iota(x),\iota(y),\iota(z))R,
\]
the entire power filtration is
\[
I^n=D+\iota(\mathfrak m^n)\qquad(n\ge1).
\]
Hence
\[
R/I^n\cong A/\mathfrak m^n,\qquad
\bigcap_{n\ge1}I^n=D\neq0.
\]
It follows that
\[
\operatorname{gr}_I(R)\cong k[x,y,z],
\qquad
\widehat R^{\,I}\cong k[[x,y,z]],
\]
with completion kernel exactly \(D\). In addition,
\[
R_I\cong A_{\mathfrak m}.
\]
Thus this globally pathological zero-divisor ideal has the same finite infinitesimal neighborhoods, associated graded ring, localization, and completion as the smooth origin of affine three-space, except that the \(I\)-adic topology on \(R\) is not separated.

## Assumptions and scope

The field, set \(X\), and ring \(R\) are exactly those in arXiv:2610.00116v1. The argument uses two source properties: \(X\) is Zariski dense in \(k^3\), and \(X\) avoids the origin. The source also proves
\[
I\subseteq Z(R),\qquad \operatorname{Ann}_R(I)=0.
\]
No Noetherian hypothesis on \(R\) is used. The statements here concern this specific witness ideal \(I\); they are not claimed for every maximal ideal of \(R\).

## Proof

First, \(\iota(A)\cap D=0\). Indeed, if \(\iota(f)\) has finite support and \(f(p)\neq0\) for some \(p\in X\), then \(\iota(f)\) is nonzero on the entire infinite fiber \(\{p\}\times\mathbb N\), a contradiction. Therefore \(f\) vanishes on \(X\), and Zariski density forces \(f=0\). Hence every element of \(R\) has a unique decomposition \(\iota(f)+d\) with \(f\in A\) and \(d\in D\).

Next, \(D\subseteq I\). For \(\omega=(p,j)\in\Omega\), at least one coordinate of \(p\) is nonzero because \(p\neq0\). If, for example, \(x(p)\neq0\), then for the coordinate idempotent \(\delta_\omega\in D\),
\[
\delta_\omega=\iota(x)\bigl(x(p)^{-1}\delta_\omega\bigr)\in I.
\]
The same argument uses \(\iota(y)\) or \(\iota(z)\) when necessary. Since the \(\delta_\omega\) span \(D\), this proves \(D\subseteq I\). Conversely, expanding the three generators against elements of \(R\) gives \(I\subseteq\iota(\mathfrak m)+D\), while \(\iota(\mathfrak m)\subseteq I\). Therefore
\[
I=D+\iota(\mathfrak m).
\]

The finite-support ideal is idempotent:
\[
D^2=D.
\]
For if \(d\in D\) has finite support \(F\), the characteristic function \(e_F\in D\) satisfies \(d=de_F\). Expanding powers of \(D+\iota(\mathfrak m)\) now gives, for every \(n\ge1\),
\[
I^n=D+\iota(\mathfrak m^n).
\]
The reverse inclusion is explicit: \(\iota(\mathfrak m^n)\subseteq I^n\) and \(D=D^n\subseteq I^n\).

Define
\[
\pi:R\longrightarrow A,\qquad \pi(\iota(f)+d)=f.
\]
The uniqueness above makes \(\pi\) a surjective ring homomorphism with kernel \(D\). For every \(n\ge1\), the composite \(R\to A\to A/\mathfrak m^n\) has kernel
\[
D+\iota(\mathfrak m^n)=I^n,
\]
so
\[
R/I^n\cong A/\mathfrak m^n.
\]
If \(r=\iota(f)+d\) lies in every \(I^n\), then \(f\in\bigcap_{n\ge1}\mathfrak m^n=0\): a nonzero polynomial has monomials of some finite least total degree. Thus \(r=d\in D\), and conversely \(D\subseteq I^n\) for all \(n\). Hence
\[
\bigcap_{n\ge1}I^n=D.
\]

Passing to successive quotients gives
\[
I^n/I^{n+1}\cong\mathfrak m^n/\mathfrak m^{n+1},
\]
compatibly with multiplication. Therefore
\[
\operatorname{gr}_I(R)\cong\operatorname{gr}_{\mathfrak m}(A)\cong k[x,y,z]
\]
with the standard grading. Taking inverse limits yields
\[
\widehat R^{\,I}
=\varprojlim_n R/I^n
\cong\varprojlim_n A/\mathfrak m^n
\cong k[[x,y,z]].
\]
The kernel of \(R\to\widehat R^{\,I}\) is the intersection of the \(I^n\), hence exactly \(D\).

Finally, \(R/I\cong A/\mathfrak m\cong k\), so \(I\) is maximal. To localize, let \(d\in D\) and choose the finite-support idempotent \(e_F\) that equals \(1\) on \(\operatorname{supp}(d)\). Then \((1-e_F)d=0\), while \(1-e_F\notin I\) because its image in \(R/I\cong k\) is \(1\). Thus \(D_I=0\). Since \(R/D\cong A\) and \(I/D\) corresponds to \(\mathfrak m\),
\[
R_I\cong (R/D)_{I/D}\cong A_{\mathfrak m}.
\]

## Verification

Every implication in the finding is proved symbolically above. The critical points are: the infinite fibers force \(\iota(A)\cap D=0\); puncturedness of \(X\) forces every coordinate idempotent into \(I\); finite support gives \(D^2=D\); and the polynomial degree filtration gives \(\bigcap_n\mathfrak m^n=0\). These four facts determine the powers, quotients, completion kernel, and localization without an exhaustive computation.

As consistency checks, the graded pieces satisfy
\[
\dim_k I^n/I^{n+1}=\binom{n+2}{2}\qquad(n\ge0),
\]
exactly as for the regular local ring \(A_{\mathfrak m}\). The source's statements \(I\subseteq Z(R)\) and \(\operatorname{Ann}_R(I)=0\) remain global statements; after localization the finite-support annihilators are killed.

## Relationship to prior work

Tran and Nguyen construct \(R\) and prove that \(I\) is a three-generated ideal contained in the zero-divisors with zero annihilator, establishing failure of \((A_3)\). Their paper does not describe powers of \(I\), the \(I\)-adic intersection, the associated graded ring, the completion, or the localization \(R_I\). Full-text inspection found no completion statement and no ideal-power analysis; its occurrence of localization is inside the geometric proof used to build \(X\), not a localization of the final ring.

The present result isolates the finite-support ideal \(D\) as the exact persistent tail of the \(I\)-adic filtration. It shows that all finite \(I\)-adic neighborhoods and the localization are regular polynomial models even though \(I\) globally consists entirely of zero-divisors and has zero annihilator.

## Limitations

The conclusion is specific to the Tran--Nguyen witness at the missing origin. It does not classify the power filtrations of the other maximal ideals of \(R\). The argument establishes an isomorphism of rings for the localization and completion; it does not assert that the global ring \(R\) is Noetherian or \(I\)-adically separated. In fact the equality \(\bigcap_{n\ge1}I^n=D\neq0\) proves nonseparatedness.

## References

V.-H. Tran and T. M. Nguyen, *A Reduced Non-McCoy Ring with the Annihilator Condition and \((A_2)\)*, arXiv:2610.00116v1, first version dated 2026-09-09.
