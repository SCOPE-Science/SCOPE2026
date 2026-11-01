# Exact von Neumann–Jordan constant of Hilbert–hexagon tensor products

## Finding

Let \(H\) be any real Hilbert space of dimension at least two, and let \(G\) be the real affine-regular hexagonal Banach plane
\[
G=(\mathbb R^2,\|(a,b)\|_G=\max\{|a|,|b|,|a+b|\}).
\]
Write \(\widehat\otimes_\varepsilon\) and \(\widehat\otimes_\pi\) for the completed injective and projective tensor products. Define the classical von Neumann–Jordan constant of a real normed space \(X\) by
\[
C_{\mathrm{NJ}}(X)=\sup_{(x,y)\ne(0,0)}
\frac{\|x+y\|^2+\|x-y\|^2}{2(\|x\|^2+\|y\|^2)}.
\]
Then, without any separability or finiteness assumption on \(H\) beyond \(\dim H\ge 2\),
\[
\boxed{C_{\mathrm{NJ}}(H\widehat\otimes_\varepsilon G)
=C_{\mathrm{NJ}}(H\widehat\otimes_\pi G)
=1+\frac{\sqrt3}{2}.}
\]
The exact bound is attained already in the four-dimensional tensor product \(\ell_2^2(\mathbb R)\otimes G\). Consequently, enlarging the real Hilbert factor does not increase this constant.

## Assumptions and scope

All spaces, dualities, and tensor products here are **real**. Both canonical tensor norms have their usual definitions. The Hilbert space \(H\) may have arbitrary dimension, including infinite cardinal dimension. The assumption \(\dim H\ge2\) is essential for the specified orthogonal-vector sharpness witness; the one-dimensional tensor is just the hexagonal plane and is not addressed by the stated formula.

## Proof

**1. Reduction of the injective product to three Hilbert norms.** Every tensor in \(H\otimes G\) has a unique presentation \(u\otimes e_1+v\otimes e_2\), with \(u,v\in H\). The closed unit ball of \(G^*\) is the convex hull of
\[
\pm(1,0),\quad \pm(0,1),\quad\pm(1,1).
\]
Taking the supremum against \(B_{G^*}\) in the injective norm gives the exact isometric identification
\[
H\widehat\otimes_\varepsilon G\ \cong\ (H\oplus H,N),\qquad
N(u,v)=\max\{\|u\|,\|v\|,\|u+v\|\}.
\tag{1}
\]
Completeness follows because \(N\) is equivalent to the Hilbert direct-sum norm. The triple of evaluation vectors \((u,v,-u-v)\) sums to zero, and *every permutation* of this triple is induced by a linear isometry of \((H\oplus H,N)\). For example, interchanging the first two coordinates sends \((u,v)\) to \((v,u)\); interchanging the second and third sends it to \((u,-u-v)\). These transpositions generate all six permutations.

**2. A sharp simultaneous two-coordinate inequality.** Put
\[
 a=1-\frac1{\sqrt3},\quad c=\frac2{\sqrt3}-1,\quad
 D=2+\sqrt3,\quad B=1+\frac{\sqrt3}{2}.
\]
The numbers \(a,c\) are positive and \(2a+c=1\). Thus the quadratic form
\[
 E(u,v)=a(\|u\|^2+\|v\|^2)+c\|u+v\|^2
\]
satisfies \(E(u,v)\le N(u,v)^2\) for every pair. Relative to the real Hilbert inner product on \(H\oplus H\), it has the positive-definite coefficient matrix
\[
 P=\begin{pmatrix}a+c&c\\c&a+c\end{pmatrix},\qquad
 P^{-1}=\begin{pmatrix} B&-1/2\\-1/2&B\end{pmatrix}.
\tag{2}
\]
For arbitrary \(x=(u,v)\), \(y=(s,t)\), consider the linear map
\[
 \mathcal L(x,y)=(u+s,v-t)\in H\oplus_2H.
\]
In the squared Hilbert norm \(E(x)+E(y)\), the squared operator norm of \(\mathcal L\) is \(D\): if \(J=\operatorname{diag}(1,-1)\), the output covariance is exactly
\[
P^{-1}+JP^{-1}J=DI_2.
\tag{3}
\]
This is the elementary positive-operator inequality \(\mathcal L^*\mathcal L\le D\operatorname{diag}(P,P)\), with scalar blocks acting on \(H\). Consequently,
\[
\|u+s\|^2+\|v-t\|^2
\le D\,[E(x)+E(y)]
\le D\,[N(x)^2+N(y)^2].
\tag{4}
\]

**3. All maximizers are covered.** Write the three evaluation maps in (1) as \(F_1(u,v)=u\), \(F_2(u,v)=v\), and \(F_3(u,v)=-u-v\). Given \(x,y\), choose indices \(i,j\) at which the two maxima \(N(x+y)\) and \(N(x-y)\) are attained. If \(i=j\), the Hilbert parallelogram identity for \(F_i(x),F_i(y)\) yields
\[
N(x+y)^2+N(x-y)^2
=2\big(\|F_i(x)\|^2+\|F_i(y)\|^2\big)
\le2\,[N(x)^2+N(y)^2]\le D\,[N(x)^2+N(y)^2].
\]
If \(i\ne j\), apply a *common* permutation isometry from step 1 to \(x,y\), sending ordered indices \((i,j)\) to \((1,2)\). Under this isometry the selected maxima become \(\|u+s\|\) and \(\|v-t\|\), so (4) gives the same bound. In both cases
\[
N(x+y)^2+N(x-y)^2\le D(N(x)^2+N(y)^2).
\]
After division by \(2(N(x)^2+N(y)^2)\), this proves \(C_{\mathrm{NJ}}(H\widehat\otimes_\varepsilon G)\le D/2=B\) for every real Hilbert \(H\).

**4. Exact equality.** Choose orthonormal vectors \(h,k\in H\) and set
\[
\begin{aligned}
x&=(Bh-\tfrac12 k,\ -\tfrac12 h+Bk),\\
y&=(Bh+\tfrac12 k,\ -\tfrac12 h-Bk).
\end{aligned}
\tag{5}
\]
The three squared norms defining each of \(N(x)\) and \(N(y)\) all equal \(D\), because \(B^2+1/4=2(B-1/2)^2=D\). Their sum and difference satisfy
\[
 x+y=(2Bh,-h),\qquad x-y=(-k,2Bk),
\]
so \(N(x+y)=N(x-y)=2B\), since \(2B>1\) and \(2B>2B-1\). The corresponding quotient is
\[
\frac{(2B)^2+(2B)^2}{2(D+D)}=\frac{2B^2}{D}=B
\]
because \(D=2B\). This proves exact sharpness for every \(\dim H\ge2\).

**5. Projective tensor norm.** The hexagonal unit ball has the vertices \(\pm(1,0)\), \(\pm(0,1)\), \(\pm(1,-1)\). Its dual norm is therefore
\[
\|(s,t)\|_{G^*}=\max\{|s|,|t|,|s-t|\}.
\]
Canonical projective tensor duality and the Riesz representation theorem yield
\[
(H\widehat\otimes_\pi G)^*\cong\mathcal L(H,G^*)
\cong (H\oplus H,N_-),\quad
N_-(u,v)=\max\{\|u\|,\|v\|,\|u-v\|\}.
\]
The second isometry writes an operator as \(h\mapsto(\langle h,u\rangle,\langle h,v\rangle)\). The map \((u,v)\mapsto(u,-v)\) is a linear isometry from \(N_-\) to \(N\), proving that this dual has von Neumann–Jordan constant \(B\). Finally, for *every* Banach space \(X\), the parallelogram transform \((x,y)\mapsto(x+y,x-y)\) on \(X\oplus_2X\) has squared operator norm \(2C_{\mathrm{NJ}}(X)\). Its adjoint is the same transform on \(X^*\oplus_2X^*\), so equality of operator and adjoint norms gives \(C_{\mathrm{NJ}}(X)=C_{\mathrm{NJ}}(X^*)\). Thus the projective product also has constant \(B\). \(\square\)

## Verification

The supplied standard-library-only script `check.py` checks the identities (2)–(3), positivity and normalization of the convex coefficients, the precise norms of the equality pair (5), and the exact algebraic quotient in the quadratic field \(\mathbb Q(\sqrt3)\). It additionally executes 9,000 seeded finite-dimensional trials across real Hilbert dimensions two, three, and seven. Those trials are checks of the formulas, **not** evidence of the universal inequality, which is proved in steps 2–3.

Reproduce with `python3 check.py` in the directory containing these files. Expected result: `PASS: exact Q(sqrt(3)) identities and 9000 finite-dimensional norm inequalities`.

## Relationship to prior work

Zhang, Xu, Liu, and Li (2026), *Von Neumann–Jordan Constants in Banach Tensor Products*, arXiv:2609.37503v1, Example 3.12, introduce this exact \(G\) and establish **only** the strict statements \(C_{\mathrm{NJ}}(H\widehat\otimes_\varepsilon G)<2\) and \(C_{\mathrm{NJ}}(H\widehat\otimes_\pi G)<2\) for infinite-dimensional real Hilbert \(H\). Their Theorem 3.11 characterizes the maximal value through orthogonal contact and provides a nonsharp general lower estimate; neither states the exact constant \(1+\sqrt3/2\). The current result strengthens their qualitative example to a precise, attained value and also includes finite Hilbert dimensions at least two.

Nearby studies of von Neumann–Jordan constants on individual hexagonal or Radon planes treat a **different space** (one factor instead of its Hilbert tensor product), and computations for \(\ell_p\)-by-\(\ell_q\) tensors treat different factors. Neither set of statements implies the tensor equality here without an additional sharp operator-valued argument.

## Limitations

The result concerns the specific affine-regular hexagon and **real** Hilbert spaces of dimension at least two. It does not determine constants for arbitrary centrally symmetric polygons, complexifications, or non-Hilbert range spaces. An exhaustive worldwide publication-priority claim is not established; older operator-space formulations under different terminology could contain an equivalent calculation. The proof and checker are not a substitute for independent mathematical review.

## References

1. W. Zhang, Y. Xu, Q. Liu, Y. Li, *Von Neumann–Jordan Constants in Banach Tensor Products*, arXiv:2609.37503v1 (first posted 2026-09-27), Sections 2–3, especially Theorem 3.11 and Example 3.12. https://arxiv.org/html/2609.37503v1
2. H. Mizuguchi, *The von Neumann–Jordan and another constants in Radon planes*, Monatshefte für Mathematik **195** (2021), 307–322, DOI:10.1007/s00605-021-01540-w. Cited as contextual work on plane geometry, not as evidence concerning these tensor products.
