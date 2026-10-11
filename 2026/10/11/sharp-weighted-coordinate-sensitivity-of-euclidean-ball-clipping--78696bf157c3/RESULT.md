# Sharp weighted coordinate sensitivity of Euclidean-ball clipping

## Finding
Let \(n\ge1\), let \(w_i>0\) for \(1\le i\le n\), and put
\[
R(x)=\frac{x}{\max\{1,\|x\|_2\}},\qquad
\|x\|_{\infty,w}=\max_{1\le i\le n}\frac{|x_i|}{w_i},\qquad
\|x\|_{1,w}=\sum_{i=1}^n w_i|x_i|.
\]
This is the Euclidean metric projection onto the closed unit ball, but the two norms used to measure input/output sensitivity need not be Euclidean. **The exact global Lipschitz constants coincide:**
\[
\boxed{\operatorname{Lip}_{\infty,w}(R)=\operatorname{Lip}_{1,w}(R)=\frac{1}{2}\left(1+\frac{\|w\|_2}{\min_{1\le i\le n}w_i}\right).}
\]
For \(n\ge2\), exterior limiting derivatives attaining the constant have precisely the normal directions specified in the next section. The smallest possible value over positive weights is \((1+\sqrt n)/2\); it is attained only when all weights are equal, up to common scaling.

## Assumptions and scope
All vectors are real. Every dimension \(n\) is a positive integer and every coordinate weight is strictly positive. We consider global Lipschitz quotients over all distinct points of \(\mathbb R^n\), not only points outside the ball. The weighted sum norm is dual to the weighted maximum norm under the usual bilinear pairing.

For \(n\ge2\), define \(m=\min_i w_i\). Fix any index \(i\) for which \(w_i=m\), and put
\[
t_i=\frac12\left(1-\frac{w_i}{\|w\|_2}\right).
\]
The normal directions of the maximal exterior boundary derivative are exactly those unit vectors \(u\) for which, for at least one such index \(i\),
\[
|u_i|=\sqrt{t_i},\qquad
|u_j|=\frac{w_j\sqrt{1-t_i}}{\bigl(\sum_{k\ne i}w_k^2\bigr)^{1/2}}\quad(j\ne i).
\]
Every coordinate sign can be chosen independently. The case \(n=1\) has global Lipschitz constant one by the interior identity map; no exterior direction is claimed to attain it.

## Proof
**1. Derivatives and a global bound.** Inside the open Euclidean unit ball, \(DR(x)=I\). At \(x=ru\), where \(r>1\) and \(\|u\|_2=1\), direct differentiation gives
\[
DR(ru)=\frac1r\bigl(I-uu^{\mathsf T}\bigr).
\]
Any straight segment meets the boundary of the Euclidean unit ball in at most two points, unless it lies in the sphere; a nontrivial straight segment cannot lie in a sphere. Thus the restriction of \(R\) to any straight segment is absolutely continuous and piecewise continuously differentiable. Integrating the derivatives, in any fixed norm \(N\), proves
\[
\operatorname{Lip}_N(R)\le\max\Bigl\{1,\sup_{\|u\|_2=1}\|I-uu^{\mathsf T}\|_{N\to N}\Bigr\}.
\]
Conversely, at any exterior point \(ru\), ordinary directional derivatives give a lower bound of \(r^{-1}\|I-uu^{\mathsf T}\|_{N\to N}\) for the global Lipschitz constant. Taking \(r\downarrow1\), and using the interior identity map, proves equality.

**2. Weighted maximum norm.** The matrix \(A(u)=I-uu^{\mathsf T}\) has diagonal entries \(1-u_i^2\ge0\). Its exact weighted maximum-norm operator norm is the maximum weighted absolute row sum:
\[
\|A(u)\|_{\infty,w\to\infty,w}
=\max_i\left(1-u_i^2+\frac{|u_i|}{w_i}\sum_{j\ne i}w_j|u_j|\right).
\]
Write \(W_i=(\sum_{j\ne i}w_j^2)^{1/2}>0\), and \(t=u_i^2\in[0,1]\). Cauchy--Schwarz gives
\[
1-u_i^2+\frac{|u_i|}{w_i}\sum_{j\ne i}w_j|u_j|
\le 1-t+\frac{W_i}{w_i}\sqrt{t(1-t)}.
\]
For every \(t\in[0,1]\), equality in this inequality is realizable by choosing \(|u_j|=w_j\sqrt{1-t}/W_i\) for all \(j\ne i\). The elementary two-dimensional eigenvalue identity
\[
\max_{0\le t\le1}\left(1-t+a\sqrt{t(1-t)}\right)
=\frac{1+\sqrt{1+a^2}}{2}\quad(a\ge0)
\]
then yields, with \(a=W_i/w_i\),
\[
\max_{\|u\|_2=1}\bigl(1-u_i^2+|u_i|w_i^{-1}\textstyle\sum_{j\ne i}w_j|u_j|\bigr)
=\frac12\left(1+\frac{\|w\|_2}{w_i}\right).
\]
Interchanging the finite maxima over \(u\) and \(i\) gives the asserted closed formula. For \(n\ge2\), \(W_i>0\), so the scalar maximizer is unique and has \(t=(1-w_i/\|w\|_2)/2\). Equality conditions in Cauchy--Schwarz and the row maximum give exactly all maximizing normal directions stated above.

**3. Dual weighted sum norm.** Under the usual pairing, \(\|\cdot\|_{1,w}\) is the dual norm of \(\|\cdot\|_{\infty,w}\). For any real matrix \(A\), duality gives \(\|A\|_{1,w\to1,w}=\|A^{\mathsf T}\|_{\infty,w\to\infty,w}\). Since \(A(u)=A(u)^{\mathsf T}\), the same sharp derivative supremum, and hence the same global Lipschitz constant, holds for the weighted sum norm. For \(n=1\), direct scalar clipping has Lipschitz constant one, matching the formula.

**4. Weight minimax and dimensions.** Since \(w_i\ge m\), \(\|w\|_2/m\ge\sqrt n\), with equality if and only if every \(w_i=m\). Rescaling all weights by a common factor does not change the formula. Hence equal weights uniquely minimize the constant up to scale. For example, the unweighted four-dimensional constant equals \(3/2\), while weights \((1,2,2,2)\) yield \((1+\sqrt{13})/2\). The expression diverges if one weight approaches zero while another stays fixed.

## Verification
The accompanying standalone program `verify.py` implements the clipping map, both weighted matrix operator norms, the explicit maximizing boundary normal, and first differences in maximizing directions. It uses only Python's standard library. Run with `python3 verify.py`; the checks cover dimensions \(2\) through \(12\) and randomized strictly positive weights. This is a finite numerical corroboration, not the proof for all dimensions or real parameters: the proof is the preceding analytic calculation.

## Relationship to prior work
Goebel (2003) explicitly uses radial projection onto a norm ball and quotes a universal Lipschitz bound two for the norm generating that ball. That is different from taking **Euclidean** projection while measuring errors using **another, anisotropically weighted** norm: the latter sharp bound can exceed two. Su, Yu, and Fei-Fei (2012) describe Euclidean-ball rescaling and algorithms for Euclidean projection onto other constraint balls, but do not establish this cross-norm Lipschitz invariant. Classical linear orthogonal-projection norm estimates concern the derivative matrix; by themselves, none of the inspected cited statements supplies the global sharp nonlinear weighted projection formula and equality normal classification. Historical equivalence through projection-constant theory remains an acknowledged possibility.

## Limitations
The result is finite-dimensional and real, and concerns the Euclidean ball centered at the origin with strictly positive coordinate weights. It does not characterize projections onto arbitrary convex bodies, arbitrary norms, or complex coordinate geometries. The cited literature was checked for directly implying the theorem; absence of a located equivalent is not a proof of historical novelty. The extremal boundary statement concerns limiting derivatives, not a claim that the global Lipschitz quotient is attained at two distinct points.

## References
1. Kazimierz Goebel, *On the problem of retracting balls onto their boundary*, Abstract and Applied Analysis 2003, 101--110. DOI: 10.1155/S1085337503204103. First published 30 January 2003. Section 2, equations (2.1)--(2.3), discusses the radial projection.
2. Hao Su, Adams Wei Yu, and Li Fei-Fei, *Efficient Euclidean Projections onto the Intersection of Norm Balls*, ICML 2012, arXiv:1206.4638 (first preprint June 2012). Sections 2--5 concern computation of metric projections, not their cross-norm sharp modulus.
