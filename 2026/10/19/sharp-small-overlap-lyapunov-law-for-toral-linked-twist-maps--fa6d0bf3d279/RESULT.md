# Sharp small-overlap Lyapunov law for toral linked twist maps

## Finding
For the toral linked twist family defined below, the positive Lyapunov exponent per application of the full map has the **sharp thin-strip asymptotic**
\[\boxed{\lambda(p)=2p\log(1/p)+O(p)\qquad(p\downarrow0).}\]
In fact, every \(0<p<1\) satisfies the computable two-sided enclosure
\[
\frac{p}{2-p}\max\!\left\{\log\!\left(1+p^{-2}+\frac1{1+p}\right),\ 4\log(1/p)-2-\log(1+p)\right\}
\le\lambda(p)\le
\frac{2p}{2-p}\log(1+p^{-2}). \tag{1}
\]
In particular, the exponent vanishes in the narrow-overlap limit, although every fixed positive-width map has positive exponent.

## Assumptions and scope
Identify opposite edges of \([0,1]^2\) to form the two-torus \(\mathbb T^2\). For each \(p\in(0,1)\), define the horizontal and vertical strips
\[
P_p=\{(x,y):0\le y\le p\},\qquad Q_p=\{(x,y):0\le x\le p\},\quad R_p=P_p\cup Q_p,\quad S_p=P_p\cap Q_p.
\]
Define \(F_p:R_p\to R_p\) by \(F_p(x,y)=(x+y/p\pmod1,y)\) on \(P_p\), and identity off \(P_p\). Define \(G_p(x,y)=(x,y+x/p\pmod1)\) on \(Q_p\), and identity off \(Q_p\). The linked-twist map is \(H_p=G_p\circ F_p\). Branch-boundary conventions on the measure-zero boundaries do not affect the assertion. The map preserves Lebesgue area on \(R_p\) and is ergodic there (established for this family in the prior literature [1,2]). The positive exponent \(\lambda(p)\) is the almost-sure limit of \(n^{-1}\log\|D H_p^n\|\) in any matrix norm; the derivative is defined outside a null set of singular preimages. The claimed asymptotic does not assert uniformity in a point of the torus.

Let \(\mu_S\) be normalized area on the square \(S_p\). For typical \(z\in S_p\), let \(a(z)\in\mathbb N\) be the first return time to \(S_p\) under \(F_p\). Write \(F_S\) for that return map. Let \(b(z)\in\mathbb N\) be the first return time to \(S_p\) under \(G_p\), evaluated at \(F_S z\); denote the corresponding return map by \(G_S\). These are defined almost everywhere: each non-exceptional horizontal or vertical circle undergoes an irrational rotation.

## Proof
**1. Induced dynamics and mean return time.** A complete return under \(H_p\) first applies \(a\) horizontal twists, then \(b\) vertical twists, with the final horizontal twist and first vertical twist occurring in the same application of \(H_p\). Thus its return map on \(S_p\) is
\[
T=G_S\circ F_S,\qquad \tau=a+b-1.
\]
Each constituent first-return map preserves \(\mu_S\). On each typical horizontal circle, the \(F_p\) dynamics is an irrational rotation, and the segment of that circle inside \(S_p\) has relative length \(p\). Conditional Kac recurrence gives \(\mathbb E_{\mu_S}a=1/p\). By the reflected vertical argument and preservation under \(F_S\), \(\mathbb E_{\mu_S}b=1/p\). Consequently,
\[
\mathbb E_{\mu_S}\tau=2/p-1=(2-p)/p.\tag{2}
\]

**2. One-return derivative and cone.** Outside switching singularities,
\[
D T(z)=M_{a,b}:=
\begin{pmatrix}1&a/p\\b/p&1+ab/p^2\end{pmatrix},
\quad a,b\in\mathbb N. \tag{3}
\]
Work with the vector \(\ell^1\) norm and positive cone
\[
K_p=\{(u,v):u\ge0,\ v\ge u/p\}.
\]
For \((u,v)\in K_p\), the image \((u',v')=M_{a,b}(u,v)\) satisfies
\[
v'-u'/p=(b-1)u/p+\bigl(1+a(b-1)/p^2\bigr)v\ge0,
\]
so \(K_p\) is invariant. Since \(u+v\le(1+p)v\) and the second component of the image is at least \((ab/p^2)v\),
\[
\frac{\|M_{a,b}(u,v)\|_1}{\|(u,v)\|_1}\ge\frac{ab}{p^2(1+p)}.\tag{4}
\]
A second, uniformly positive lower bound follows from entrywise monotonicity \(M_{a,b}\ge M_{1,1}\). The column sums of \(M_{1,1}\) are \(1+1/p\) and \(1+1/p+1/p^2\). The larger column receives at least fraction \(1/(1+p)\) of the \(\ell^1\) mass of any vector in \(K_p\). Hence
\[
\frac{\|M_{a,b}(u,v)\|_1}{\|(u,v)\|_1}\ge
L(p):=1+p^{-2}+(1+p)^{-1}>1.\tag{5}
\]
The first application of \(M_{a,b}\) puts every nonzero positive vector in \(K_p\). Products of these strictly positive matrices can therefore be evaluated along a positive vector; their top operator growth exponent agrees with that vector's growth exponent because the vector \((1,1)\) bounds the matrix \(\ell^1\)-operator norm above and below within a factor \(2\). Equations (4)–(5), applied to every induced step, imply for the induced top exponent \(\lambda_S(p)\):
\[
\lambda_S(p)\ge \log L(p),\qquad
\lambda_S(p)\ge \mathbb E[\log a+\log b]+2\log(1/p)-\log(1+p).\tag{6}
\]

**3. Short-return estimate valid at every width.** For any integer \(j\ge1\), if \((x,y)\) is uniformly distributed on \(S_p\), the number \(t=y/p\) is uniform on \([0,1]\). Thus \((x+j t)\pmod1\) is uniform on the unit circle conditional on \(x\), and
\[
\mu_S\{F_p^j z\in S_p\}=p.
\]
A union bound gives \(\mu_S\{a\le N\}\le Np\) for every integer \(N\ge1\). For every \(t\ge0\), therefore,
\[
\mu_S\{pa<e^{-t}\}\le e^{-t}.
\]
Integration of the negative logarithmic tail proves
\[
\mathbb E[\log(pa)]\ge -\int_0^\infty e^{-t}\,dt=-1,
\qquad\mathbb E\log a\ge \log(1/p)-1.\tag{7}
\]
The vertical-first-return variable \(b\) has the same marginal law as \(a\), because \(F_S\) preserves \(\mu_S\) and the vertical problem is the coordinate reflection of the horizontal problem. Substituting (7) into (6) yields
\[
\lambda_S(p)\ge
\max\{\log L(p),\ 4\log(1/p)-2-\log(1+p)\}.\tag{8}
\]

**4. Upper bound without a return-time partition.** Decompose \(M_{a,b}\) into its elementary horizontal and vertical shear matrices. Their operator \(\ell^1\) norms give
\[
\|M_{a,b}\|_1\le(1+a/p)(1+b/p).
\]
Subadditivity, preservation of \(\mu_S\), and Jensen's inequality now give
\[
\lambda_S(p)\le\mathbb E\log(1+a/p)+\mathbb E\log(1+b/p)
\le 2\log(1+p^{-2}),\tag{9}
\]
using \(\mathbb E a=\mathbb E b=1/p\).

**5. Return-time normalization and asymptotics.** Since the full map and the induced map are ergodic, the return-time average (2) and the standard induced Lyapunov identity give
\[
\lambda(p)=\frac{\lambda_S(p)}{\mathbb E\tau}=\frac{p}{2-p}\lambda_S(p).\tag{10}
\]
For completeness, the identity follows by evaluating the derivative product on successive return times; integrability of \(\tau\) makes the remaining unfinished excursion negligible per original iterate, since every individual original-time shear has bounded derivative for fixed \(p\). Combining (8)–(10) proves (1). As \(p\downarrow0\), the second lower branch of (1) equals \(2p\log(1/p)-p+O(p^2\log(1/p))\); the upper bound equals \(2p\log(1/p)+O(p^2\log(1/p))\). This establishes the stated \(O(p)\) enclosure with sharp leading coefficient \(2\).

## Verification
The cone algebra, short-return union bound, conditional Kac normalization, Jensen estimate, and asymptotic expansion constitute the infinite-parameter proof. The accompanying `verify.py` independently checks the matrix inequalities on exact rational samples and validates that the two explicit bounds bracket a deterministic numerical Lyapunov calculation at representative widths. Finite computations are supplementary; they do not establish the universal theorem.

## Relationship to prior work
Wright, Niesen and Sturman [1] introduced the same parameterized linked-twist family, its return matrix \(M_{a,b}\), and the Kac factor \((2-p)/p\). Their stated computable Lyapunov bounds (Theorem 2) apply only above the positive root of \(p^3+p-1=0\), approximately \(0.682\). They do not determine the limit \(p\downarrow0\) or the coefficient \(2\). The present proof instead combines a universal arithmetic short-return bound with coarse cone inequalities, dispensing with the small-width return partition. Springham and Sturman [2] established polynomial correlation decay for linked twist maps and considered arbitrary annulus widths; their Lyapunov discussion establishes hyperbolicity without the asymptotic coefficient claimed here.

## Limitations
The theorem is for equal strip widths and one positive full twist in each direction. It asserts the Lebesgue-typical exponent, not every individual orbit's exponent, and it does not identify the \(O(p)\) constant or higher-order expansion. Ergodicity and existence of the almost-sure Lyapunov exponent rely on established theorems for this family; no independent proof of ergodicity is given. Other historical sources on quantitative thin-annulus limits could contain implicit antecedents; the present comparison does not claim exhaustive priority verification.

## References
[1] P. Wright, J. Niesen and R. Sturman, *Rigorous bounds on Lyapunov exponents of linked twist maps*, Nonlinearity 36 (2023), 1699–1715, doi:10.1088/1361-6544/acb397. First public source verified 2023-02-06; open version: https://eprints.whiterose.ac.uk/id/eprint/196140/7/Wright_2023_Nonlinearity_36_1699.pdf.

[2] J. Springham and R. Sturman, *Polynomial decay of correlations in linked-twist maps*, Ergodic Theory Dynam. Systems 34 (2014), 1724–1746, doi:10.1017/etds.2013.8; arXiv:1212.0889v1 (2012-12-04).
