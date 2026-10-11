# Infinitesimal skew radii detect Hilbert geometry in uniformly smooth Banach spaces

## Finding
Let \(X\) be a nonzero real uniformly smooth Banach space, and let \(j(x)\in X^*\) be its unique norming functional at a unit vector \(x\): \(\|j(x)\|=j(x)(x)=1\). Define the normalized semi-inner-product asymmetry
\[
\kappa_X:=\frac12\sup_{x,y\in S_X}|j(x)(y)-j(y)(x)|,\qquad 0\le\kappa_X\le1.
\]
For a fixed finite \(1\le t<\infty\), set
\[
M_t(a,b)=\left(\frac{a^t+b^t}{2}\right)^{1/t},\quad
S_{X,t}(h)=\inf_{x,y\in S_X}M_t(\|x+hy\|,\|hx-y\|),\quad
J_t[h,X]=\sup_{x,y\in S_X}M_t(\|x+hy\|,\|hx-y\|).
\]
Write
\[
\rho_X(h)=\sup_{x,y\in S_X}\left[\frac{\|x+hy\|+\|x-hy\|}{2}-1\right].
\]
**Theorem.** For each finite \(t\), a constant \(C_t<\infty\), depending only on \(t\), exists such that for every \(0\le h\le1/4\),
\[
\left|S_{X,t}(h)-1+\kappa_Xh\right|\le2\rho_X(h)+C_th^2,
\qquad
\left|J_t[h,X]-1-\kappa_Xh\right|\le2\rho_X(h)+C_th^2.
\]
Since uniform smoothness means \(\rho_X(h)=o(h)\),
\[
S'_{X,t}(0+)=-\kappa_X,\qquad
\left.\frac{d^+}{dh}J_t[h,X]\right|_{h=0}=\kappa_X.
\]
Moreover, \(\kappa_X=0\) if and only if \(X\) is a real Hilbert space with its given norm. Thus every non-Hilbert uniformly smooth norm has a **strict negative/positive first-order skew-radius pair**, with the same coefficient for every finite outer exponent.

## Assumptions and scope
All spaces and dualities are real. Uniform smoothness is used, not merely pointwise smoothness, because both radii are extrema over the full unit-sphere product and require an error bound uniform in \(x,y\). No finite-dimensionality, reflexivity assumption separate from uniform smoothness, extremizer existence, or differentiability of the radii at positive parameters is assumed. The derivative notation is always the right derivative at \(h=0\). The exponent \(t=\infty\) is excluded from the two derivative identities.

## Proof
**Step 1: uniform first variations of the two norms.** For every \(x,y\in S_X\) and \(0\le h\le1/4\), the supporting-functional inequality and the definition of \(\rho_X\) give
\[
0\le\|x+hy\|-1-hj(x)(y)\le2\rho_X(h).
\]
The lower bound is \(\|x+hy\|\ge j(x)(x+hy)\). The upper bound follows by combining \(\|x+hy\|+\|x-hy\|\le2+2\rho_X(h)\) with \(\|x-hy\|\ge1-hj(x)(y)\). Apply the same estimate at the unit point \(-y\), using \(j(-y)=-j(y)\), to obtain
\[
0\le\|hx-y\|-1+hj(y)(x)\le2\rho_X(h).
\]
All four inequalities hold uniformly over unit pairs.

**Step 2: expansion of the finite power mean.** Because both arguments lie in \([1-h,1+h]\subset[3/4,5/4]\), the scalar function \((a,b)\mapsto M_t(a,b)\) has a bounded Hessian there for every fixed finite \(t\ge1\). Its differential at \((1,1)\) is \((u,v)\mapsto(u+v)/2\). Taylor's theorem therefore supplies a constant \(C_t\) (enlarged if needed) such that
\[
\left|M_t(1+u,1+v)-1-\frac{u+v}{2}\right|\le C_th^2
\quad (|u|,|v|\le h\le1/4).
\]
Inserting Step 1 yields the **uniform** bound
\[
\left|M_t(\|x+hy\|,\|hx-y\|)
-1-\frac h2\big(j(x)(y)-j(y)(x)\big)\right|
\le2\rho_X(h)+C_th^2.
\]
(The two nonnegative norm remainders each contribute at most \(2\rho_X(h)\), hence their half-sum is at most \(2\rho_X(h)\).)

**Step 3: pass to both extrema.** Put \(D(x,y)=j(x)(y)-j(y)(x)\). It satisfies \(D(y,x)=-D(x,y)\). Therefore
\[
\inf_{x,y\in S_X}D(x,y)=-2\kappa_X,\qquad
\sup_{x,y\in S_X}D(x,y)=2\kappa_X.
\]
Taking the infimum and supremum in the uniform estimate from Step 2 proves both error bounds. Uniform smoothness gives \(\rho_X(h)/h\to0\), which proves the derivative formulas without any assumption that extremal pairs exist.

**Step 4: Hilbert rigidity.** In a Hilbert norm, \(j(x)(y)=\langle x,y\rangle\) for unit points, so \(\kappa_X=0\). Conversely suppose \(\kappa_X=0\). For \(u\ne0\) define
\[
B(u,v)=\|u\|\,j(u/\|u\|)(v),\qquad B(0,v)=0.
\]
For each fixed \(u\), \(B(u,\cdot)\) is linear. Symmetry of \(j(x)(y)\) on all unit pairs implies \(B(u,v)=B(v,u)\) for arbitrary \(u,v\). Symmetry makes \(B(\cdot,v)\) linear as well. Finally \(B(u,u)=\|u\|^2\), so \(B\) is a positive-definite symmetric bilinear form inducing the given norm. Thus \(X\) is Hilbert.

## Verification
Every analytic estimate above is uniform over \(S_X\times S_X\); no finite search or numerical fit is used to establish an infinite-dimensional statement. As a direct non-Hilbert witness, in real \(\ell_4^2\) take \(x=(1,0)\) and \(y=(1/2,(15/16)^{1/4})\). Both are unit vectors, and \(j(x)(y)-j(y)(x)=1/2-1/8=3/8\); hence \(\kappa_{\ell_4^2}\ge3/16>0\). This illustrates, but does not claim to calculate, the optimal coefficient for that space.

The finite-exponent boundary is genuine: on a real Hilbert space of dimension at least two, the known exact maximum-mean formula gives \(J_\infty[h,H]=1+h\), whose right derivative is \(1\), even though \(\kappa_H=0\). This does not contradict the theorem because the scalar maximum is not differentiable at equal arguments. For the infimal maximum-mean functional on the same Hilbert space, \(S_{H,\infty}(h)=\sqrt{1+h^2}\).

## Relationship to prior work
Xu and Liu [1] introduced the infimal skew Schäffer power-mean radius, proved basic parameter bounds and exact Hilbert and \(L^p\) formulas (with the outer exponent set equal to \(p\) in their \(L^p\) theorem). Rao and collaborators [2] introduced the corresponding supremal skew James invariant. Neither inspected main-result statement identifies a simultaneous first-variation coefficient for all finite outer exponents on arbitrary uniformly smooth spaces, or the resulting Hilbert-characterization property. The Lumer–Giles semi-inner product and its relationship to norming functionals are classical [3]; the new assertion is their exact identification with the two skew-radius derivatives and the uniform modulus-of-smoothness error estimate. Exact planar derivatives for particular nonsmooth norms do not imply the present theorem, and this theorem does not compute those nonsmooth cases.

## Limitations
The result does not cover arbitrary nonsmooth norms, where norming functionals can be multivalued; does not assert that the extrema are attained; and does not provide an exact value of \(\kappa_X\) for every non-Hilbert space. The outer exponent \(t=\infty\) cannot be included unchanged. Classical semi-inner-product symmetry is acknowledged as a pre-existing ingredient, not a newly discovered theorem. Further equivalent formulations could exist in unindexed geometric-constant literature.

## References
[1] Y. Xu and Q. Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1 (2 October 2026), https://arxiv.org/abs/2610.03050 .

[2] Z. Rao and collaborators, *The skew James type constant in Banach spaces*, arXiv:2504.00827v1 (2025), https://arxiv.org/abs/2504.00827 .

[3] T. Kobos and P. Wójcik, *On Non-linear Mappings Preserving the Semi-inner Product*, Results in Mathematics 78 (2023), article 214, DOI:10.1007/s00025-023-01993-5. This is a modern reference for the classical Lumer–Giles representation of a smooth norm by its norming functionals.
