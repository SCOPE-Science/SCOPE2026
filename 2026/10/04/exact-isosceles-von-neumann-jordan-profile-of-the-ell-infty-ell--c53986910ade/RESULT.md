# Exact isosceles von Neumann–Jordan profile of the \(\ell_\infty-\ell_1\) hexagonal plane
## Finding
Let \(X=\mathbb R^2\) with
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
Equivalently, \(N\) is the norm that equals the \(\ell_1\) norm when \(st\le0\) and the \(\ell_\infty\) norm when \(st\ge0\). For \(0\le\lambda\le1\), define
\[
C''_{\mathrm{NJ}}(\lambda,X)=\sup\left\{N(\lambda x+(1-\lambda)y)^2+\lambda(1-\lambda)N(x-y)^2:x,y\in S_X,\ N(x+y)=N(x-y)\right\}.
\]
Then
\[
C''_{\mathrm{NJ}}(\lambda,X)=1+\frac54m-2m^2,\qquad m=\min\{\lambda,1-\lambda\}.
\]
Equivalently,
\[
C''_{\mathrm{NJ}}(\lambda,X)=
\begin{cases}
1+\frac54\lambda-2\lambda^2,&0\le\lambda\le\frac12,\\
\frac14+\frac{11}{4}\lambda-2\lambda^2,&\frac12\le\lambda\le1.
\end{cases}
\]
Hence the profile has endpoint value \(1\) and maximum value \(9/8\) at \(\lambda=1/2\).

## Assumptions and scope
The space is real and two-dimensional. Isosceles orthogonality means \(x\perp_I y\) if and only if \(N(x+y)=N(x-y)\). The unit ball of \(N\) is the centrally symmetric hexagon with vertices
\[
(1,1),(0,1),(-1,0),(-1,-1),(0,-1),(1,0).
\]
The claim concerns only the parameterized constant displayed above, not other orthogonality constants with similar notation.

## Proof
Write
\[
N(z)=\max\{\varphi(z):\varphi\in\mathcal F\},\qquad
\mathcal F=\{\pm s,\pm t,\pm(s-t)\}.
\]
Parameterize each of the six unit-sphere edges affinely. For an ordered pair of edges containing \(x\) and \(y\), choose signed support forms \(\varphi_+,\varphi_-\in\mathcal F\) attaining \(N(x+y)\) and \(N(x-y)\). The conditions that these forms dominate all other signed support forms are linear inequalities in the two edge parameters, while isosceles orthogonality is the linear equality
\[
\varphi_+(x+y)=\varphi_-(x-y).
\]
Thus each nonempty support cell of isosceles-orthogonal pairs is a compact line segment. There are no feasible cells for which the equality is identically zero. On a fixed cell and for fixed \(\lambda\),
\[
(x,y)\longmapsto N(\lambda x+(1-\lambda)y)^2+\lambda(1-\lambda)N(x-y)^2
\]
is convex: the square of a norm is convex and the second summand is the square of an affine function on the cell. Therefore its maximum on each cell is attained at a cell endpoint.

Exact rational enumeration of all support cells yields 48 distinct endpoints. At those endpoints, resolving the three absolute support forms in the first norm gives only 12 distinct quadratic polynomials in \(\lambda\). Their coefficient triples \((a,b,c)\), representing \(a+b\lambda+c\lambda^2\), are
\[
\begin{aligned}
&(0,9/4,-5/4),(1/9,8/9,0),(1/9,20/9,-4/3),(1/4,3/4,0),\\
&(1/4,11/4,-2),(4/9,0,0),(4/9,16/9,-16/9),(1,-8/9,0),\\
&(1,-3/4,0),(1,1/4,-5/4),(1,4/9,-4/3),(1,5/4,-2).
\end{aligned}
\]
Exact comparison of these quadratics shows that \((1,5/4,-2)\) dominates all candidates on \([0,1/2]\), while \((1/4,11/4,-2)\) dominates all candidates on \([1/2,1]\).

Sharpness on the left branch is witnessed by
\[
x=(1,1/2),\qquad y=(0,1).
\]
Indeed, \(N(x)=N(y)=1\) and
\[
N(x+y)=N(x-y)=3/2.
\]
For \(0\le\lambda\le1/2\),
\[
N(\lambda x+(1-\lambda)y)=1-\lambda/2,
\]
so the defining expression equals
\[
(1-\lambda/2)^2+\frac94\lambda(1-\lambda)=1+\frac54\lambda-2\lambda^2.
\]
Swapping \(x\) and \(y\) replaces \(\lambda\) by \(1-\lambda\), proving sharpness on the right branch.

## Verification
The accompanying `verify.py` uses only exact rational arithmetic. It reconstructs the six edges, all signed support cells, the isosceles equality, every feasible cell endpoint, and all 12 candidate quadratics. It checks the two branch envelopes symbolically on their full intervals and checks the explicit maximizing pair. Running `python3 verify.py` returns `VERIFY_OK`, together with counts 48 and 12. No floating-point sampling is used to prove the continuum statement.

## Relationship to prior work
The current version of Wang et al., arXiv:2110.15741v2, introduces this parameterized isosceles restriction and, in Example 2.3, studies exactly the same \(\ell_\infty-\ell_1\) plane. It states \(C''_{\mathrm{NJ}}(\lambda,X)=1.2\) across the parameter range and includes intermediate constant outputs such as \(1.04\). The definition itself forces the endpoint values at \(\lambda=0\) and \(\lambda=1\) to be \(1\), so a parameter-independent value \(1.2\) cannot hold. The formula above supplies the complete corrected profile.

Ni et al., arXiv:2504.00826, study a different symmetric isosceles-orthogonality constant \(L_X(t)\) and recall an unparameterized constant attributed to Papini. Those definitions are not the parameterized unit-sphere constant treated here and do not imply the displayed profile.

## Limitations
The theorem is specific to this real hexagonal Banach plane. It does not determine \(C''_{\mathrm{NJ}}(\lambda,X)\) for arbitrary polygonal planes, sequence spaces, or general Banach spaces. The literature search cannot rule out an obscure independently derived correction under substantially different notation.

## References
1. Yuxin Wang, Qi Liu, Qian Li, Qichuan Ni, Zhijian Yang, Muhammad Sarfraz, and Yongjin Li, *Novel constants based on the generalization of Von Neumann-Jordan constant*, arXiv:2110.15741, first public version 29 October 2021; current v2, Example 2.3.
2. Qichuan Ni et al., *Symmetric form geometric constant related to isosceles orthogonality in Banach spaces*, arXiv:2504.00826, first public version 31 March 2025.
