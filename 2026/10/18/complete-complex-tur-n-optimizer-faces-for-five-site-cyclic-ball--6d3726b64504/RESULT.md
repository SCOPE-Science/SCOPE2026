# Complete complex Turán optimizer faces for five-site cyclic balls

## Finding
For every integer \(N\ge5\), write \(G=\mathbb Z/N\mathbb Z\) and \(\Omega=\{0,\pm1,\pm2\}\subseteq G\). Let \(\mathcal P_N\) be the convex set of complex positive-definite functions \(f:G\to\mathbb C\) with \(f(0)=1\) and \(\operatorname{supp}f\subseteq\Omega\). Here positive-definite means that the unnormalized Fourier transform \(\widehat f(j)=\sum_x f(x)e^{-2\pi ijx/N}\) is real and nonnegative at every frequency. Let \(\mathcal M_N\) be the face maximizing \(\sum_x f(x)=\widehat f(0)\).

The maximum itself is classical (see References), and is not asserted to be new. **The result here is the complete face of all possibly non-even, complex-valued maximizers.** If \(3\nmid N\), this face is a singleton, with \(f(1)=a\) and \(f(2)=b\) both real. Put
\[
 u=\max\{\cos(2\pi j/N):\cos(2\pi j/N)<-1/2\},\quad
 v=\min\{\cos(2\pi j/N):\cos(2\pi j/N)>-1/2\}.
\]
Then
\[
 a=-\frac{u+v}{1+2uv},\qquad b=\frac1{2+4uv},\qquad
 \max \widehat f(0)=\frac{(1-u)(1-v)}{1/2+uv}.
\]
If \(3\mid N\), the maximum is \(3\). Every maximizer has the uniquely parametrized form
\[
 f(1)=1-b+it,\qquad f(2)=b+it,\qquad b,t\in\mathbb R,
\]
with \(f(-x)=\overline{f(x)}\), and its parameter pair belongs to the following explicitly determined polygon. Define
\[
 \beta=2\pi/N,\quad C=\cos\beta,\quad S=\sin\beta,\quad
 u=\cos(2\pi/3+\beta),\quad v=\cos(2\pi/3-\beta),
\]
\[
 L=\frac1{2(1-u)},\quad R=\frac1{2(1-v)},\quad
 B=\frac{C}{1+2C},\quad T=\frac{S}{1+2C}.
\]
For \(N=6\), the optimizer face is the triangle with vertices \((R,0),(B,T),(B,-T)\). For every \(N\ge9\) divisible by three, it is **exactly** the four-vertex kite
\[
 \mathcal M_N\cong\operatorname{conv}\{(L,0),(R,0),(B,T),(B,-T)\}.
\]
In particular, there are exactly four extreme complex normalized optimizers for these orders (three for order six); nonreal optimizers occur precisely when \(3\mid N\). The vertices \((B,\pm T)\) have \(f(2)=e^{\pm i\beta}/(1+2\cos\beta)\).

## Assumptions and scope
All assertions concern complex positive-definite functions with normalized value \(1\) at the identity, supported **inside** the five-element ball; values at the other four sites are not required to be nonzero. Fourier transforms are unnormalized; the optimization objective is the unnormalized sum, not the Haar average. The group order satisfies \(N\ge5\), so the five residue classes are distinct. The parameterization uses the Hermitian identity \(f(-x)=\overline{f(x)}\), which follows from Fourier nonnegativity. The comparison with prior results is about the complex equality face, **not** the already known optimum value or the classical real-even coefficients.

## Proof
Write \(f(1)=a+is\) and \(f(2)=b+it\) for real \(a,b,s,t\). At \(\theta_j=2\pi j/N\), with \(x_j=\cos\theta_j\), one has
\[
 \widehat f(j)=1+2a x_j+2b(2x_j^2-1)+2s\sin\theta_j+2t\sin(2\theta_j).
\]
Symmetrization \(f(x)\mapsto(f(x)+f(-x))/2\) preserves positivity, normalization and objective, so the real-even part \(1+2a\cos\theta+2b\cos2\theta\) is an even optimizer.

**Orders not divisible by three.** The cosines \(u<-1/2<v\) are consecutive levels. Let \(Q(x)=(x-u)(x-v)/(1/2+uv)\). Its average over \(N\) roots of unity is \(1\), because \(N\ge5\), \(\langle x\rangle=0\), and \(\langle x^2\rangle=1/2\). It is nonnegative at all sampled cosines. Its coefficients give \(a,b\) in the finding. For an arbitrary feasible even polynomial \(P(x)=1+2ax+2b(2x^2-1)\), the explicit positive multipliers
\[
 \lambda_u=\frac{(1-v)(1+2v)}{(v-u)(1+2uv)},\qquad
 \lambda_v=\frac{(1-u)(-1-2u)}{(v-u)(1+2uv)}
\]
satisfy \(\lambda_u(u,2u^2-1)+\lambda_v(v,2v^2-1)=(-1,-1)\). The inequalities \(P(u),P(v)\ge0\) therefore imply \(P(1)\le1+\lambda_u+\lambda_v=Q(1)\). Both multipliers are strictly positive, so equality forces \(P(u)=P(v)=0\), determining \(a,b\) uniquely. For the original complex \(f\), averaging the Fourier values at positive and negative angles shows that the even part vanishes at both \(\pm\arccos u\) and \(\pm\arccos v\). Their odd parts must vanish there separately. Since neither sine vanishes, this means \(s+2ut=s+2vt=0\); hence \(s=t=0\). The complex optimizer is unique.

**Orders divisible by three.** The Fourier inequalities at \(j=N/3\) and \(2N/3\) imply \(a+b\le1\), so the objective is at most \(3\). Equality is attained by \(a=2/3,b=1/3,s=t=0\), whose Fourier polynomial is \((1+2\cos\theta)^2/3\). For any maximizing \(f\), both these Fourier samples have nonnegative sum zero and must individually vanish. Their sine terms force \(s=t\). Substituting \(a=1-b\) and \(s=t\) gives the factorization
\[
 \widehat f(\theta)=(1+2\cos\theta)\bigl(1-2b(1-\cos\theta)+2t\sin\theta\bigr).
\]
By symmetry \(t\mapsto-t\), take \(t\ge0\). Put \(\theta_j\in(0,\pi]\). For angles \(\theta_j>2\pi/3\), positivity at both signs is equivalent to
\[
 b\ge\frac1{2(1-\cos\theta_j)}+t\cot(\theta_j/2).
\]
Both terms decrease as \(\theta_j\) grows; thus the unique strongest lower bound is at \(\theta_u=2\pi/3+\beta\). For \(\theta_j<2\pi/3\), positivity at both signs is equivalent to
\[
 b\le\frac1{2(1-\cos\theta_j)}-t\cot(\theta_j/2).
\]
For \(N\ge9\), the right side decreases in \(\theta_j\) whenever \(0\le t\le1/(2\sqrt3)\): its derivative has the sign of \(2t\sin(\theta_j/2)-\cos(\theta_j/2)\). Therefore its strongest upper bound is at \(\theta_v=2\pi/3-\beta\). The intersection of these two bounds has \(t=T=\sin\beta/(1+2\cos\beta)\) and \(b=B=\cos\beta/(1+2\cos\beta)\) by elementary sine addition; for \(N\ge9\), \(T<1/(2\sqrt3)\), so the preceding monotonicity applies **throughout the feasible region**. At \(t=0\) the endpoints are \(L,R\), giving precisely the announced kite. For \(N=6\), there is only one positive-angle sample on each side of \(2\pi/3\): \(\theta_u=\pi\), \(\theta_v=\pi/3\). Their two inequalities give the triangle, as \(L=B=1/4\). Reflection supplies the \(t\le0\) half in every case.

## Verification
The independent-of-formula finite checker `check.py` uses direct Fourier evaluation, independent two-dimensional half-plane intersection enumeration in the divisible-by-three case, and direct enumeration of even feasible LP vertices in the other cases. It completed checks for every \(N\) from \(5\) through \(300\); these finite computations corroborate the formulas but the preceding argument proves all \(N\ge5\). Run `python check.py` using Python 3, without external packages.

## Relationship to prior work
Gorbachev and Manoshina (2002), Theorem 5 and their discrete linear-programming equivalence, already determine the **optimal numerical value and an even real extremizer** for degree-two support at the relevant nonmultiples of three. Those numerical formulas are not original here. Their problem and its proof explicitly restrict to **even functions**, and do not classify the nonsymmetric complex equality face, its number of extreme points, or its vertices. Kolountzakis and Révész (2003) show that real-part symmetrization preserves Turán constants, but this does not identify all nonsymmetric equality cases. Other published discrete Fejér extremal results address coefficients or different support sets, rather than this face. The new feature is the complete real-two-dimensional complex optimizer geometry, including the triangle-versus-kite resonance.

## Limitations
The theorem concerns only the radius-two interval support; extending the optimizer-face classification to larger supports is not proved. The known scalar Turán constant is prior work. A hidden equivalent equality-face classification in less-accessible Russian or discrete-positive-definite literature remains a publication-priority risk. The finite checker is corroborative, not a substitute for the unrestricted proof.

## References
1. D. V. Gorbachev and A. S. Manoshina, *Turan Extremum Problem for Periodic Function with Small Support*, arXiv:math/0211291v1 (19 November 2002), particularly Theorems 2 and 5, https://arxiv.org/pdf/math/0211291.
2. M. N. Kolountzakis and Sz. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218v1 (10 December 2003), https://arxiv.org/pdf/math/0312218.
3. V. I. Ivanov, *Pointwise Turán problem for periodic positive definite functions*, Trudy Inst. Math. Mekh. 24(4) (2018), 156–175, https://geodesic.mathdoc.fr/item/TIMM_2018_24_4_a12/ (related objectives; only abstract checked).
