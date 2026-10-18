# Cyclicity threshold and even-power multiplicity for the classical Cesàro operator on Hardy spaces

## Finding
Let \(0<p<\infty\), and let \(C\) be the classical analytic Cesàro operator on \(H^p(\mathbb D)\), given by
\[
(Cf)(z)=\frac{1}{z}\int_0^z\frac{f(\zeta)}{1-\zeta}\,d\zeta,
\]
with the removable value at the origin. For every positive integer \(m\), **the power \(C^m\) is cyclic if and only if \(m\le2\)**. The constant function \(1\) is a cyclic vector for both \(C\) and \(C^2\). For \(m\ge3\), no vector is cyclic for \(C^m\), regardless of whether the Hardy space is Banach or quasi-Banach.

Define the cyclic multiplicity \(\mu(T)\) to be the smallest number of vectors whose combined polynomial orbits under \(T\) have dense linear span. For every positive integer \(k\),
\[
\boxed{\mu(C^{2k})=k.}
\]
For every odd \(m\ge3\), the additional quantitative bounds are
\[
\boxed{\left\lceil\frac{m}{2}\right\rceil\le\mu(C^m)\le m.}
\]
The exact multiplicities of odd powers greater than one are not asserted.

## Assumptions and scope
Throughout, Hardy spaces comprise complex holomorphic functions on the open disk, with
\[
\|f\|_{H^p}^p=\sup_{0<r<1}\frac1{2\pi}\int_0^{2\pi}|f(re^{i\theta})|^p\,d\theta<\infty.
\]
When \(0<p<1\), this is a quasi-norm and all closures are taken in its usual complete metric topology. A bounded operator is *cyclic* if one vector has dense linear span of its nonnegative powers. The operator \(C\) is bounded for the indicated range of \(p\), including the quasi-Banach regime [1]. Cyclic multiplicity concerns **linear spans**, not dense unscaled orbits (hypercyclicity). We treat all positive integer powers of this one operator, not general Cesàro-type matrices or the real-variable integral operator.

## Proof
### Step 1. A moment representation for powers when \(p\ge2\)
For \(p\ge2\), use the strongly continuous semigroup from [1, Section 3],
\[
(S_tf)(z)=\frac{e^{-t}}{1-(1-e^{-t})z}
 f\!\left(\frac{e^{-t}z}{1-(1-e^{-t})z}\right),\qquad t\ge0,
\]
which obeys \(\|S_t\|_{H^p\to H^p}\le e^{-t/p}\). Its generator \(A\) has \(-A^{-1}=C\); the Bochner integral identity \(C=\int_0^\infty S_t\,dt\) follows from the resolvent formula. Since \(S_sS_t=S_{s+t}\), Fubini and the volume of the \(m\)-simplex give, in operator norm,
\[
C^m=\frac1{(m-1)!}\int_0^\infty t^{m-1}S_t\,dt\quad(m\ge1).
\]
All integrals converge since \(\|S_t\|\le e^{-t/p}\).

### Step 2. The square is cyclic
Write \(q=p/(p-1)\). Suppose \(g\in H^q\) annihilates \(\{C^{2n}1:n\ge0\}\) under the standard Hardy duality pairing (linear in its first entry). Put
\[
F(t)=\langle S_t1,g\rangle=e^{-t}\overline{g(1-e^{-t})}.
\]
The semigroup estimate gives \(|F(t)|\le\|g\|_{H^q}e^{-t/p}\). From Step 1, for each \(n\ge1\),
\[
\int_0^\infty t^{2n-1}F(t)\,dt=0.
\]
The function \(G(z)=\int_0^\infty F(t)\sinh(zt)\,dt\) is analytic throughout the strip \(|\operatorname{Re}z|<1/p\). Every Taylor coefficient of \(G\) at the origin is zero, because they are the odd moments just displayed. Hence \(G\) vanishes on that strip. For every real \(y\),
\[
0=G(iy)=i\int_0^\infty F(t)\sin(yt)\,dt.
\]
The odd extension of \(F\) belongs to \(L^1(\mathbb R)\), and its Fourier transform is zero; Fourier uniqueness implies \(F=0\) almost everywhere. Continuity gives \(F(t)=0\) for all \(t\ge0\), hence \(g(1-e^{-t})=0\) for \(t>0\). The analytic identity theorem forces \(g=0\). Hahn–Banach proves
\[
\overline{\operatorname{span}}\{C^{2n}1:n\ge0\}=H^p\qquad(p\ge2).
\]
If \(0<p<2\), the continuous dense inclusion \(H^2\hookrightarrow H^p\) transfers this statement from \(H^2\); the polynomials are dense in every \(H^p\). Thus \(1\) is cyclic for \(C^2\) on all the stated spaces. The case \(C\) itself is Theorem 1.1 of [1] and also follows because all even powers are a subfamily of all powers.

### Step 3. Explicit, continuous adjoint eigenfunctionals
For any nonzero complex \(\lambda\) with \(\beta=1/\lambda\) satisfying \(\operatorname{Re}\beta>1+1/p\) and \(\beta\notin\{1,2,\ldots\}\), let
\[
a_0(\beta)=1,\qquad
 a_n(\beta)=\prod_{j=1}^{n}\left(1-\frac{\beta}{j}\right)
 =\frac{\Gamma(n+1-\beta)}{\Gamma(1-\beta)\Gamma(n+1)}.
\]
For this fixed \(\beta\), standard gamma-ratio asymptotics give \(|a_n(\beta)|=O((n+1)^{-\operatorname{Re}\beta})\). The Hardy point-evaluation bound and Cauchy's estimate at radius \(n/(n+1)\) give, for the coefficients \(f(z)=\sum_{n\ge0} f_nz^n\),
\[
|f_n|\le K_p(n+1)^{1/p}\|f\|_{H^p}\qquad(n\ge0).
\]
Consequently \(\Lambda_\lambda(f):=\sum_{n\ge0}a_n(\beta)f_n\) is a continuous complex-linear functional on \(H^p\), even for \(p<1\).

The elementary recurrence
\[
\lambda\bigl(a_n(\beta)-a_{n+1}(\beta)\bigr)
 =\frac{a_n(\beta)}{n+1}
\]
and \(a_n(\beta)\to0\) imply the exact identity
\[
\sum_{n=k}^\infty\frac{a_n(\beta)}{n+1}=\lambda a_k(\beta)
\qquad(k\ge0).
\]
On every polynomial, use the coefficient formula \((Cf)_n=(n+1)^{-1}\sum_{k=0}^{n}f_k\) to deduce \(\Lambda_\lambda(Cf)=\lambda\Lambda_\lambda(f)\). By boundedness of \(C\), of \(\Lambda_\lambda\), and density of polynomials, the identity extends to all \(H^p\):
\[
\boxed{\Lambda_\lambda\circ C=\lambda\Lambda_\lambda.}
\]
For distinct parameters \(\lambda_j\), the functionals are independent. Indeed the values \(a_n(1/\lambda_j)\) on \(1,z,\ldots,z^{r-1}\) are evaluations of degree-\(n\) polynomials with nonzero leading coefficients, and their determinant is a nonzero Vandermonde determinant in the distinct values \(1/\lambda_j\).

### Step 4. Spectral folding forces multicyclicity
For each integer \(m\ge3\), rotate a regular \(m\)-gon of sufficiently small radius \(\varepsilon>0\) so that at least \(r=\lceil m/2\rceil\) distinct vertices \(\lambda_1,\ldots,\lambda_r\) have strictly positive real part. All of these vertices share one common \(m\)-th power \(\eta\). Taking \(\varepsilon\) small makes \(\operatorname{Re}(1/\lambda_j)>1+1/p\); the vertices can be chosen nonreal, so the integrality exclusion in Step 3 holds. Their \(r\) independent functionals satisfy
\[
\Lambda_{\lambda_j}\circ C^m=\eta\Lambda_{\lambda_j}\quad(1\le j\le r).
\]
Given fewer than \(r\) vectors, a nonzero linear combination of these functionals annihilates those vectors and hence all their iterates under \(C^m\). Their joint orbit therefore cannot be dense. Thus \(\mu(C^m)\ge r\); in particular \(C^m\) is not cyclic for any \(m\ge3\).

For every \(m\), Theorem 1.1 of [1] shows \(\mu(C^m)\le m\), since the joint \(C^m\)-orbits of \(1,C1,\ldots,C^{m-1}1\) contain all powers of \(C\) applied to \(1\). When \(m=2k\), Step 2 improves the upper bound: the joint \(C^{2k}\)-orbits of \(1,C^21,\ldots,C^{2k-2}1\) contain every even power of \(C\) applied to \(1\), and hence are dense. The lower and upper bounds both equal \(k\), proving \(\mu(C^{2k})=k\). The remaining odd-power bounds follow immediately.

## Verification
The nonstandard steps admit exact symbolic checks. The identity \(\lambda(a_n-a_{n+1})=a_n/(n+1)\) follows by direct substitution of \(\beta=1/\lambda\); telescoping gives the complete infinite adjoint eigenvector identity, not a finite truncation. The entire odd-moment sequence from \(C^{2n}\) is precisely the Taylor sequence of the hyperbolic-sine transform. Its strip analyticity follows from the explicit semigroup norm, and Fourier uniqueness has no discretization assumption. The Vandermonde determinant proves algebraic independence of the eigenfunctionals for every permitted \(p\), including \(p<1\). No finite computation is relied upon for an infinite-dimensional statement.

## Relationship to prior work
Belli, Gül, Ross, and Siskakis [1] prove the cyclicity of \(C\), identify \(1\) as cyclic for every \(0<p<\infty\), and establish the semigroup ingredients used here. Their Theorem 1.1 and Corollary 5.1 concern \(C\), not a classification of cyclicity or cyclic multiplicity of higher powers. The classical Kriete–Trutt subnormal model, discussed in [1,2], gives an alternative spectral perspective in the Hilbert case but does not itself state the uniform quasi-Banach/Hilbert power dichotomy or its sharp even-power multiplicity. Related real-variable Cesàro cyclicity results [3] concern operators on \(L^p(0,1)\), not on analytic Hardy spaces. We do not claim priority for the cyclicity of \(C\) or for any semigroup estimate appearing in [1].

## Limitations
The precise cyclic multiplicity of odd powers \(C^m\) for \(m\ge3\) is not determined: only the proved bounds are asserted. The argument does not classify all cyclic vectors for \(C\) or \(C^2\). This is an analytic same-paper extension for the classical operator and does not cover generalized Cesàro operators or other domains. The publication-priority comparison is bounded by searchable literature and the inspected primary sources; an unindexed equivalent formulation remains a risk. No independent audit has been performed.

## References
[1] A. Belli, U. Gül, W. T. Ross, A. G. Siskakis, *The Cesàro operator is cyclic on Hardy spaces*, arXiv:2609.15911v1 (first posted 2026-09-14), https://arxiv.org/html/2609.15911 .

[2] E. A. Gallardo-Gutiérrez, J. R. Partington, W. T. Ross, *Invariant subspaces of the Cesàro operator*, arXiv:2307.06923 (2023), https://arxiv.org/abs/2307.06923 .

[3] A. Belli, U. Gül, W. T. Ross, A. G. Siskakis, *Crescents and the Real Variable Cesàro Operator*, arXiv:2606.08600v1 (first posted 2026-06-07); *Integral Equations and Operator Theory* **98**, article 42 (2026), https://link.springer.com/article/10.1007/s00020-026-02865-7 .
