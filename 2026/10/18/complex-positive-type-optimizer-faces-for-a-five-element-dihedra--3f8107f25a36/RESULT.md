# Complex positive-type optimizer faces for a five-element dihedral neighborhood

## Finding
Let \(n\ge3\), let \(D_{2n}=\langle r,s:r^n=s^2=e,\ srs=r^{-1}\rangle\), and set \(\Omega=\{e,r,r^{-1},s,sr\}\). Among all complex-valued positive-definite functions \(f:D_{2n}\to\mathbb C\), supported in \(\Omega\) and normalized by \(f(e)=1\), consider the unnormalized mass \(M(f)=\sum_{g\in D_{2n}}f(g)\). Write
\[
Z_n=\{ |\cos(\pi k/n)|:0\le k<n\}.
\]

**Theorem (complete complex equality cases).** If \(3\nmid n\), let \(\alpha=\max\{z\in Z_n:z<1/2\}\) and \(\beta=\min\{z\in Z_n:z>1/2\}\). Then there is **exactly one** maximizing function, namely
\[
f(e)=1,\qquad f(r)=f(r^{-1})=u_*:=\frac1{2+4\alpha\beta},\qquad
f(s)=f(sr)=t_*:=\frac{\alpha+\beta}{1+2\alpha\beta},
\]
with all remaining values zero. Its mass is
\[
T_n=1+\frac{1+2(\alpha+\beta)}{1+2\alpha\beta}
=3+\frac{(1-2\alpha)(2\beta-1)}{1+2\alpha\beta}>3.
\]
If \(3\mid n\), then \(T_n=3\), and **all** maximizing functions form exactly the real line segment
\[
f(e)=1,\qquad f(r)=f(r^{-1})=u,\qquad
f(s)=f(sr)=1-u,
\]
where for \(n=3\) one has \(1/4\le u\le1\); for \(n\ge6\), with \(\alpha\) and \(\beta\) the nearest elements of \(Z_n\) strictly below and above \(1/2\), respectively,
\[
\frac1{2(1+\beta)}\le u\le\frac1{2(1+\alpha)}.
\]
In particular, none of the complex or reflection-asymmetric degrees of freedom survives at an optimum. The dimension of the optimizer face jumps from zero to one precisely when \(3\mid n\).

## Assumptions and scope
Positive-definite means \(\sum_{g,h}\overline{c_g}c_h f(g^{-1}h)\ge0\) for every complex family \((c_g)\). No assumption of reality, centrality, conjugation invariance, or nonnegative point values is made. Involutions force \(f(s),f(sr)\in\mathbb R\), and positive definiteness forces \(f(r^{-1})=\overline{f(r)}\). The claim concerns the entire complex positive-type optimizer set, not merely the scalar extremum or its symmetric witnesses. The mass is unnormalized counting mass.

## Proof
Write \(f(r)=u+iv\), \(f(s)=b\), and \(f(sr)=c\), with \(u,v,b,c\in\mathbb R\). The Fourier criterion for positive definiteness on a finite group tests the positive-semidefiniteness of \(\sum_g f(g)\rho(g)\) for every unitary irreducible representation. The standard two-dimensional dihedral blocks (including the reducible endpoint blocks, which aggregate all one-dimensional representations) have matrix
\[
\begin{pmatrix}
1+2u\cos\theta-2v\sin\theta & b+c e^{-i\theta}\\
b+c e^{i\theta} &1+2u\cos\theta+2v\sin\theta
\end{pmatrix},\qquad \theta=2\pi k/n,\quad 0\le k<n.
\]
Consequently the complete positive-type criterion is
\[
1+2u\cos\theta\ \ge\
\sqrt{4v^2\sin^2\theta+b^2+c^2+2bc\cos\theta}
\quad (0\le k<n). \tag{1}
\]
The automorphism \(r\mapsto r^{-1},\ s\mapsto sr\) preserves \(\Omega\), interchanges \(b,c\), and negates \(v\). Averaging a feasible function with its image preserves its mass, producing \(v=0,b=c=t\). Thus the scalar maximum reduces *without loss for its value* to
\[
q(z)=1-2u+4u z^2-2t z\ge0\quad(z\in Z_n),\qquad
M=1+2u+2t. \tag{2}
\]
For \(3\nmid n\), the nearest \(\alpha<1/2<\beta\) are consecutive sampled values. With \(u_*,t_*\) from the theorem,
\[
q(z)=4u_*(z-\alpha)(z-\beta)\ge0\quad(z\in Z_n),
\]
since no sampled value lies strictly between the roots. This proves attainability. For optimality, define the two strictly positive numbers
\[
\lambda=\frac{(2\beta-1)(1+\beta)}{(\beta-\alpha)(1+2\alpha\beta)},\qquad
\mu=\frac{(1-2\alpha)(1+\alpha)}{(\beta-\alpha)(1+2\alpha\beta)}.
\]
Direct expansion gives \(T_n-(1+2u+2t)=\lambda q(\alpha)+\mu q(\beta)\). Thus any symmetric maximizer has \(q(\alpha)=q(\beta)=0\); the two equations uniquely determine \((u,t)=(u_*,t_*)\).

For \(3\mid n\), \(1/2\in Z_n\). From \(q(1/2)\ge0\) one gets \(t\le1-u\), hence \(M\le3\). At equality, \(t=1-u\) and
\[
q(z)=(2z-1)\bigl(2u(z+1)-1\bigr). \tag{3}
\]
The sign of the first factor changes only at \(z=1/2\). For \(n\ge6\), the two adjacent samples \(\alpha,\beta\) therefore give exactly the interval in the theorem, and that interval makes every sampled inequality hold. For \(n=3\), \(Z_3=\{1/2,1\}\); the sample at \(1\) gives \(u\ge1/4\), and the diagonal positivity at \(1/2\) gives \(u\le1\). These are all the constraints.

It remains to exclude nonsymmetric or genuinely complex maximizers. Let \(y=b+c\). The averaged optimizer is unique in the nondivisible case, or belongs to the displayed segment in the divisible case, so \(y>0\) except possibly at \(n=3,u=1\). At every active sample \(z=|\cos(\theta/2)|\in(0,1)\), the averaged feasibility constraint is saturated. The original inequality (1) can be rewritten as
\[
1+2u\cos\theta\ge
\sqrt{y^2z^2+(b-c)^2(1-z^2)+4v^2\sin^2\theta}\ge yz.
\]
Equality is forced by the active symmetric contact; since \(0<z<1\) and \(\sin\theta\ne0\), it implies \(b=c\) and \(v=0\). In the nondivisible case the contact at \(\beta\) is such a sample. In the divisible case \(z=1/2\) is such a sample, including \(n=3,u=1\), where \(y=0\) but the same sum-of-squares argument applies. Therefore the entire complex optimizer set is exactly as asserted.

## Verification
An accompanying standalone Python checker evaluates all irreducible-block eigenvalue inequalities on the full frequency range for \(3\le n\le120\), checks both endpoint and interior witnesses of the divisible-by-three optimizer intervals, verifies the positive two-contact dual multipliers, and independently enumerates vertices of the two-variable Fourier-positivity linear program. It reports 118 tested orders and 120 interval witnesses. These finite tests corroborate the symbolic proof; they do not substitute for the quantifiers over all \(n\).

## Relationship to prior work
The numerical theta value of the square of an even cycle is **not new**: Bachoc, Pêcher, and Thiéry (arXiv:1103.0444, first posted 2011-03-02) determine Lovász theta values for every power of a cycle. Indeed the undirected Cayley graph on \(D_{2n}\) with generators \(\{r,r^{-1},s,sr\}\) is isomorphic to the antiprism graph \(C_{2n}^2\) through the vertex map \(r^j\mapsto2j\), \(sr^j\mapsto2j-1\) modulo \(2n\). Consequently the scalar \(T_n\) is already covered by their theorem, even if its notation differs. The present theorem instead gives the *complete noncommutative, complex-valued positive-definite equality face*, including elimination of all nonsymmetric freedoms and the exact arithmetic zero-dimensional/one-dimensional transition. The inspected primary work constructs symmetric real optimizers and gives scalar formulas, but does not state this noncommutative equality-face classification. Standard finite-group Fourier positivity and the locally compact abelian Turán framework are used as background, not claimed as new.

## Limitations
Novelty is conditional on the inspected literature: an equivalent equality-case classification may be implicit in earlier semidefinite-program duality or the graph-theta literature. The result concerns this five-element generating neighborhood only; it does not classify all optimal semidefinite kernels on an antiprism graph, which need not be group-invariant. The checker is numerical; exact validity rests on the displayed Fourier blocks, polynomial identities, and positive dual multipliers. No independent mathematical audit has been performed.

## References
1. C. Bachoc, A. Pêcher, and A. Thiéry, *On the theta number of powers of cycle graphs*, arXiv:1103.0444 (first version 2011-03-02); *Combinatorica* **33** (2013), 297–317, DOI:10.1007/s00493-013-2950-x.
2. M. N. Kolountzakis and S. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, *Journal of the London Mathematical Society* **74** (2006), 475–496, DOI:10.1112/S0024610706023234.
3. Standard finite-group Fourier/Bochner criterion: positive type is equivalent to positivity of every irreducible Fourier matrix.
