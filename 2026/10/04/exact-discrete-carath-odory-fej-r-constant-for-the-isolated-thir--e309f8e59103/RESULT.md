# Exact discrete Carathéodory–Fejér constant for the isolated third harmonic
## Finding
For every integer \(N\ge 6\), define
\[
D_N=\sup\left\{\lambda\in\mathbb R:\exists c\in\mathbb R,\ 1+\lambda\cos(2\pi r/N)+c\cos(6\pi r/N)\ge0\ \text{for every }r\in\mathbb Z_N\right\}.
\]
Put \(a=\lfloor5N/12\rfloor\), \(b=\lceil5N/12\rceil\), \(v=\cos(2\pi a/N)\), and \(u=\cos(2\pi b/N)\). Then
\[
D_N=\frac{\tfrac34-(u^2+uv+v^2)}{uv(u+v)}.
\]
An extremizer is \(c=[4uv(u+v)]^{-1}\), for which, writing \(x=\cos(2\pi r/N)\),
\[
1+D_Nx+c(4x^3-3x)=\frac{(x-u)(x-v)(x+u+v)}{uv(u+v)}.
\]
When \(12\mid N\), this specializes to \(D_N=2/\sqrt3\).

## Assumptions and scope
The optimization is over real coefficients \(\lambda,c\), and nonnegativity is required only on the \(N\)-point cyclic grid. The harmonic support is exactly restricted to \(\{0,\pm1,\pm3\}\); allowing intermediate harmonics is a different optimization problem. The statement covers every \(N\ge6\), including meshes on which the third harmonic aliases modulo \(N\).

## Proof
Let \(T_3(x)=4x^3-3x\) and \(x_r=\cos(2\pi r/N)\). The continuous third-harmonic contact occurs at \(x_0=-\sqrt3/2=\cos(5\pi/6)\). By construction, \(u\le x_0\le v<0\), and no sampled cosine lies strictly between \(u\) and \(v\). For \(N=6\), \(u+v=-3/2\). For \(N=7\), \(u+v=-(\cos(\pi/7)+\cos(3\pi/7))<-1\): indeed \(\cos(\pi/7)>\sqrt3/2\), while concavity of cosine on \([0,\pi/2]\) gives \(\cos(3\pi/7)\ge1/7\). For \(N\ge8\), the lower bracketing angle is at least \(7\pi/12\), hence \(u+v\le-\sqrt3/2- (\sqrt6-\sqrt2)/4<-1\). Thus \(uv(u+v)<0\), and the third root \(-(u+v)\) lies to the right of \(1\).

Set
\[
K=\frac1{uv(u+v)},\qquad Q(x)=K(x-u)(x-v)(x+u+v).
\]
Expanding gives
\[
Q(x)=1+K\left(\frac34-u^2-uv-v^2\right)x+\frac K4T_3(x).
\]
Therefore the proposed coefficients are exactly the coefficient of \(x\) and \(c=K/4\). On \([-1,1]\), both \(K\) and \(x+u+v\) are negative, so the sign of \(Q(x)\) is the sign of \((x-u)(x-v)\). Since no grid value lies in \((u,v)\), \(Q(x_r)\ge0\) for every \(r\), proving feasibility.

For the matching upper bound first suppose \(12\nmid N\), so \(u<v\) and \(T_3(u)<0<T_3(v)\). Define
\[
\alpha=\frac{T_3(v)}{T_3(v)-T_3(u)},\qquad
\beta=\frac{-T_3(u)}{T_3(v)-T_3(u)}.
\]
Then \(\alpha,\beta>0\), \(\alpha+\beta=1\), and \(\alpha T_3(u)+\beta T_3(v)=0\). Every feasible polynomial \(q(x)=1+\lambda x+cT_3(x)\) therefore satisfies
\[
0\le \alpha q(u)+\beta q(v)=1+\lambda(\alpha u+\beta v).
\]
Because \(\alpha u+\beta v<0\),
\[
\lambda\le -\frac1{\alpha u+\beta v}
=-\frac{T_3(v)-T_3(u)}{uT_3(v)-vT_3(u)}
=\frac{\tfrac34-(u^2+uv+v^2)}{uv(u+v)},
\]
where the last identity follows by substituting \(T_3(t)=4t^3-3t\). This is attained by \(Q\).

If \(12\mid N\), then \(u=v=-\sqrt3/2\) is itself a sampled cosine and \(T_3(u)=0\). Feasibility at that one grid point gives \(0\le1+\lambda u\), hence \(\lambda\le2/\sqrt3\). The displayed factorized polynomial attains that value, completing the proof.

## Verification
The accompanying verifier evaluates the closed form and factorized polynomial for every \(6\le N\le5000\), checks the two-point dual certificate off the contact meshes, and independently solves the two-variable sampled linear program by active-constraint enumeration for every \(6\le N\le90\). These finite checks are corroborative; the proof above establishes the statement for all \(N\ge6\).

## Relationship to prior work
Kolountzakis and Révész introduced the continuous and discretized Carathéodory–Fejér quantities \(M(H)\) and \(M_m(H)\), including the inequality \(M_m(H)\ge M(H)\), but the inspected paper does not evaluate the support-restricted singleton case \(H=\{3\}\) on every finite mesh. Krenedits and Révész later established general equivalences and finite-to-continuous reductions for these extremal quantities, again without the closed form above in the inspected material. Ivanov studies a second discrete Fejér problem in which all intermediate harmonics up to a prescribed order may vary; that broader feasible class is not the same support restriction as \(\{0,\pm1,\pm3\}\).

## Limitations
The result is specific to one free nonconstant auxiliary harmonic, namely the isolated third harmonic, and to real even trigonometric polynomials on a uniform cyclic grid. It does not classify optimizers after additional harmonics are admitted. The literature comparison cannot rule out an equivalent formula hidden under different notation in specialized discrete Fejér or quadrature literature.

## References
1. M. N. Kolountzakis and Sz. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, arXiv:math/0302193v1 (2003).
2. I. Krenedits and Sz. Gy. Révész, *Carathéodory–Fejér type extremal problems on locally compact Abelian groups*, arXiv:1304.0071v5.
3. V. I. Ivanov, *Pointwise Turán problem for periodic positive definite functions*, DOI:10.21538/0134-4889-2018-24-4-156-175.
