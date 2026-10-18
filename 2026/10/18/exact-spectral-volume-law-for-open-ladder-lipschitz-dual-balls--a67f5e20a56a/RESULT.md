# Exact spectral volume law for open-ladder Lipschitz dual balls

## Finding

For every integer \(n\ge2\), let \(L_n=P_n\square K_2\) be the \(n\)-rung **open** ladder with unit-edge graph metric. The volume \(V_n\) of the unit ball of its real Lipschitz dual, measured in \((2n-1)\)-dimensional anchored-potential coordinates, has generating function

\[
\sum_{n\ge1}V_n z^{n-1}
=\frac{2\sin\sqrt{2z}}{\sqrt{2z}\bigl(\cos\sqrt{2z}-\sqrt{2z}\sin\sqrt{2z}\bigr)}.
\]

Here \(V_1=2\) is an auxiliary initial value corresponding to a single edge. Let \(\rho_j\) be the unique root of \(\cos\rho=\rho\sin\rho\) in \((j\pi,j\pi+\pi/2)\), for \(j=0,1,2,\ldots\). An absolutely convergent expression for each volume is

\[
V_n=\sum_{j=0}^{\infty}\frac4{\rho_j^2(\rho_j^2+2)}
\left(\frac2{\rho_j^2}\right)^{n-1}.
\]

In particular, \(V_{n-1}V_{n+1}>V_n^2\) for all \(n\ge2\), and the consecutive-volume ratios strictly increase to

\[
\frac2{\rho_0^2}=2.702067773756757248\ldots\,.
\]

Indeed, with \(C_0=4/[\rho_0^2(\rho_0^2+2)]\) and \(q=(\rho_0/\rho_1)^2=0.063074784784119386\ldots\),

\[
V_n=C_0\left(\frac2{\rho_0^2}\right)^{n-1}
\left(1+O(q^{n-1})\right),\qquad
C_0=1.972187085750126650\ldots\,.
\]

## Assumptions and scope

Vertices of \(L_n\) are \((i,a)\) with \(1\le i\le n\) and \(a\in\{0,1\}\). Unit-length edges join \((i,0)\) to \((i,1)\), and \((i,a)\) to \((i+1,a)\). There are no wraparound edges. Fix the real Lipschitz potential at \((1,0)\) to zero and put the usual Lebesgue measure on the remaining \(2n-1\) vertex coordinates. The unit Lipschitz ball consists of potentials satisfying \(|f(v)-f(w)|\le1\) on every graph edge; these constraints are equivalent to the full shortest-path Lipschitz condition. Volumes are in **anchored coordinates**, not the ambient zero-sum Euclidean metric.

## Proof

**1. Exact product kernel.** Write \(a_i=f(i,0)\), \(b_i=f(i,1)\), with \(a_1=0\), and change variables to rung slopes \(s_i=b_i-a_i\) and horizontal top slopes \(u_i=a_i-a_{i-1}\), \(2\le i\le n\). This triangular linear change of variables has absolute determinant one. The rung constraints become \(s_i\in[-1,1]\). For each pair of consecutive rung slopes, the two horizontal constraints are

\[
|u_i|\le1,\qquad |u_i+s_i-s_{i-1}|\le1.
\]

Their common interval has length \(2-|s_i-s_{i-1}|\); it is always nonnegative since \(|s_i-s_{i-1}|\le2\). Integration over independent top slopes proves

\[
V_n=\int_{[-1,1]^n}\prod_{i=2}^n
\bigl(2-|s_i-s_{i-1}|\bigr)\,ds_1\cdots ds_n.
\]

Define \(T:L^2[-1,1]\to L^2[-1,1]\) by \((Tf)(x)=\int_{-1}^1(2-|x-y|)f(y)\,dy\). The preceding identity is

\[
V_n=\langle \mathbf1,T^{n-1}\mathbf1\rangle,
\qquad n\ge1,
\]

including the auxiliary \(V_1=\langle\mathbf1,\mathbf1\rangle=2\).

**2. Resolvent and generating function.** For complex \(z\) sufficiently close to zero set \(u=(I-zT)^{-1}\mathbf1\). The kernel is continuous, so differentiating its integral equation twice gives \(u''=-2zu\). Reflection invariance makes \(u\) even. Put \(w=\sqrt{2z}\) (all expressions are analytic in \(z\) near zero), so \(u(x)=A\cos(wx)\). Since \((Tu)(1)=\int_{-1}^1u(y)\,dy\) for even \(u\), its boundary equation is

\[
A\cos w=1+z\frac{2A\sin w}{w},
\quad\text{thus}\quad
A=\frac1{\cos w-w\sin w}.
\]

Integrating \(u\) over \([-1,1]\) gives the generating function stated above. This determines every rational volume without computing high-dimensional polytope facets.

**3. Spectral expansion.** The identity

\[
2-|x-y|=\int_{\mathbb R}
\mathbf1_{[x-1,x+1]}(t)\mathbf1_{[y-1,y+1]}(t)\,dt
\]

shows that \(T\) is positive semidefinite. It is compact and self-adjoint. If \(Tf=0\), the second-derivative identity \((Tf)''=-2f\) gives \(f=0\), hence its eigenvalues are strictly positive. For an even eigenfunction \(f(x)=\cos(\rho x)\), the equation \(Tf=\lambda f\) yields \(\lambda=2/\rho^2\). Evaluating it at \(x=1\) gives \(\cos\rho=\rho\sin\rho\), equivalently \(\tan\rho=1/\rho\). Monotonicity of tangent and reciprocal on each interval \((j\pi,j\pi+\pi/2)\) produces exactly one \(\rho_j\). Odd eigenfunctions have zero inner product with \(\mathbf1\), so they contribute nothing to the volumes. The squared coefficient of the normalized even eigenfunction is

\[
\frac{\bigl(\int_{-1}^1\cos(\rho_jx)\,dx\bigr)^2}
{\int_{-1}^1\cos^2(\rho_jx)\,dx}
=\frac4{\rho_j^2(\rho_j^2+2)}.
\]

The spectral theorem now gives the absolutely convergent series. In particular, its coefficient sum equals \(V_1=2\).

**4. Strict log-convexity and sharp growth.** Every term in the spectral representation has strictly positive weight and the distinct bases \(\lambda_j=2/\rho_j^2>0\). The strict Cauchy–Schwarz inequality applied to \(\{\sqrt{c_j}\lambda_j^{(n-2)/2}\}\) and \(\{\sqrt{c_j}\lambda_j^{n/2}\}\) gives \(V_{n-1}V_{n+1}>V_n^2\) for \(n\ge2\). Hence ratios increase strictly. Since \(\lambda_0>\lambda_1>\cdots>0\), and \(\sum_jc_j=2<\infty\),

\[
0<\sum_{j\ge1}c_j\lambda_j^{n-1}
\le\biggl(\sum_{j\ge1}c_j\biggr)\lambda_1^{n-1}.
\]

Dividing by \(c_0\lambda_0^{n-1}\) proves the stated geometric error bound, ratio limit, and sharp leading constant.

## Verification

The independent script `verify_ladder_volumes.py` calculates the coefficients of the proposed trigonometric generating function in exact rational arithmetic and separately counts all integer-valued anchored Lipschitz potentials on the graph dilated by each integer \(k\). Total unimodularity of the graph-edge incidence constraints makes the potential polytope integral. Its Ehrhart polynomial has degree \(d=2n-1\), so its leading coefficient, recovered by the full \(d\)-th finite difference divided by \(d!\), equals volume. Both calculations agree **exactly for every \(n=2,3,4,5,6,7\)**, i.e., dimensions \(3,5,7,9,11,13\). This finite verification corroborates, and does not replace, the analytical proof.

For orientation,

\[
V_1=2,\quad V_2=\frac{16}3,\quad V_3=\frac{72}5,\quad
V_4=\frac{12256}{315},\quad V_5=\frac{298048}{2835},\quad
V_6=\frac{14764672}{51975},\quad V_7=\frac{933546368}{1216215}.
\]

To reproduce: `python verify_ladder_volumes.py` (Python standard library only).

## Relationship to prior work

Aliaga (2021, arXiv:2102.01219) supplies a relevant functional-analytic treatment of extreme points in Lipschitz-free spaces. Ostrovska and Ostrovskii (2021, arXiv:2112.02689) describe finite transportation-cost spaces through graph edges and cycles. Alexander, Fradelizi, García-Lirola, and Zvavitch (2019, arXiv:1911.10642) study finite-metric volume products and the equilateral baseline. D'Alì, Delucchi, and Michałek (2019, arXiv:1910.05193), especially Proposition 4.37 and their symmetric-edge volume discussion, connect graph polytopes with polar lattice points but do not state the open-ladder polar continuous-volume sequence or its spectral growth. The triangular-kernel eigenvalue problem is classical; its spectrum alone is not asserted to be new. The proposed contribution is the identified **open-ladder metric volume**, its complete closed generating/spectral representation, and resulting strict volume-ratio law. These comparisons do not imply an exhaustive novelty guarantee.

## Limitations

The statement concerns unit-edge open ladders and a fixed anchored-coordinate volume normalization; it does not assert intrinsic Euclidean volume or results for circular ladders, weighted ladders, or general grid strips. The asymptotic is for \(n\to\infty\), and the numerical approximations are illustrative only. An equivalent derivation in literature not uncovered by the documented comparisons may exist. The proof and small-dimensional computations have not undergone independent scientific audit.

## References

- Ramón J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219, first posted 2021-02-01, primary MSC 46B20. https://arxiv.org/abs/2102.01219
- Sofiya Ostrovska and Mikhail Ostrovskii, *Isometric structure of transportation cost spaces on finite metric spaces*, arXiv:2112.02689, 2021. https://arxiv.org/abs/2112.02689
- Matthew Alexander and collaborators, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642. https://arxiv.org/abs/1911.10642
- Alessio D'Alì, Emanuele Delucchi, Mateusz Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, 2019. https://arxiv.org/abs/1910.05193
