# An exact overlap-optimal three-segment quadratic histopolation rule

## Finding
Let \(0<\varepsilon<1\). Recover a polynomial of degree at most two from the three interval means over \([-1,1]\), \([-1,1-\varepsilon]\), and \([-1+\varepsilon,1]\). The interpolation operator \(\Pi_\varepsilon:L^\infty([-1,1])\to\mathcal P_2\), measured in the essential-supremum norm on the input and uniform norm on the output, has the **exact** norm
\[
\|\Pi_\varepsilon\|=\max\left\{1+\frac{2(1-\varepsilon)^2}{2-\varepsilon},\ 1+\frac{2\varepsilon(3-\varepsilon)}{2-\varepsilon}\right\}.
\]
It has a **unique** minimum over \(0<\varepsilon<1\) at
\[
\varepsilon_* =\frac{5-\sqrt{17}}4,\qquad \min_\varepsilon\|\Pi_\varepsilon\|=\frac32(\sqrt{17}-3).
\]
For the *same three overlapping measurements*, the generalized segmental Lebesgue constant (the uniform-data-coefficient amplification) is
\[
\Lambda(\varepsilon)=1+\frac4{\varepsilon(1-\varepsilon)}.
\]
Consequently, \(\Lambda(\varepsilon)/\|\Pi_\varepsilon\|\to\infty\) at either endpoint of the admissible design interval. The generalized constant measures independently perturbed interval means, whereas the operator norm measures a common bounded perturbation of the underlying function; the distinction is essential.

## Assumptions and scope
Work in exact real arithmetic. Define \(I=[-1,1]\), \(S_0=I\), \(S_-=[-1,1-\varepsilon]\), and \(S_+=[-1+\varepsilon,1]\). For an interval \(S\), let \(M_S(f)=|S|^{-1}\int_S f(x)\,dx\). A bounded measurable real function is understood modulo almost-everywhere equality. The polynomial \(\Pi_\varepsilon f\in\mathcal P_2\) is defined by the three conditions \(M_{S_i}(\Pi_\varepsilon f)=M_{S_i}(f)\). All three intervals have positive length and nontrivial common overlap. The domain \(0<\varepsilon<1\) is necessary for uniqueness of the interpolation problem. No unbounded or independent errors in the three measured means are included in the operator-norm statement.

Define the three disjoint subintervals \(T_-=[-1,-1+\varepsilon]\), \(T_0=[-1+\varepsilon,1-\varepsilon]\), and \(T_+=[1-\varepsilon,1]\), with means \(m_-\), \(m_0\), and \(m_+\), respectively. Their boundary overlaps have measure zero. Put \(a=1-\varepsilon\) and \(d=1+a=2-\varepsilon\).

## Proof
**1. Unique quadratic reconstruction.** The three interval means of the basis \(1,x,x^2\) are respectively
\[
(1,0,1/3),\quad (1,-\varepsilon/2,(1-\varepsilon+\varepsilon^2)/3),\quad (1,\varepsilon/2,(1-\varepsilon+\varepsilon^2)/3).
\]
The determinant of this normalized measurement matrix, with rows ordered \(S_0,S_-,S_+\), is \(\varepsilon^2(1-\varepsilon)/3>0\). Writing \(M_0=M_{S_0}(f)\) and \(M_\pm=M_{S_\pm}(f)\), solution of the three equations gives
\[
(\Pi_\varepsilon f)(x)=M_0+\frac{M_+-M_-}{\varepsilon}x+
\frac{3}{\varepsilon(1-\varepsilon)}\left(M_0-\frac{M_-+M_+}{2}\right)\left(x^2-\frac13\right).
\]
The formula reproduces each polynomial of degree at most two and defines the unique interpolant for every \(f\in L^\infty(I)\).

**2. Disjoint-cell reduction.** Since \(S_-=T_-\cup T_0\), \(S_+=T_0\cup T_+\), and \(S_0=T_-\cup T_0\cup T_+\), substitution into the preceding display yields
\[
\Pi_\varepsilon f(x)=w_-(x)m_-+w_0(x)m_0+w_+(x)m_+,
\]
where
\[
w_\pm(x)=\frac{3x^2\pm2x-a^2}{2(1+a)},\qquad
w_0(x)=\frac{1+a+a^2-3x^2}{1+a}.
\]
The cell means can be independently assigned any values in \([-1,1]\) by choosing a bounded piecewise-constant function on \(T_-\), \(T_0\), and \(T_+\). Thus the exact induced norm is
\[
\|\Pi_\varepsilon\|=\max_{-1\le x\le1}\bigl(|w_-(x)|+|w_0(x)|+|w_+(x)|\bigr),
\]
with equality attained by cellwise signs at a maximizing point.

**3. The only maximizing abscissae are needed at the center and endpoints.** By symmetry take \(0\le x\le1\). Put \(U=a^2\), \(V=1+a+a^2\), \(d=1+a\). Using \(|z-y|+|z+y|=2\max\{|z|,|y|\}\), the expression multiplied by \(d\) is
\[
F(x)=\max\bigl\{|3x^2-U|,2x\bigr\}+|V-3x^2|.
\]
The first branch, \(|z-U|+|V-z|\) with \(z=3x^2\in[0,3]\), is convex in \(z\) and is no larger than its larger endpoint value
\[
E_0=d+2U\quad\text{or}\quad E_1=6-d-2U.
\]
For the second branch \(2x+|V-3x^2|\), if \(3x^2\le V\), completing the square gives \(2x+V-3x^2\le V+1/3\). If \(a\ge1/\sqrt3\), then \(E_0-(V+1/3)=a^2-1/3\ge0\). Otherwise \(E_1-(V+1/3)=11/3-2a-3a^2>0\) for \(0<a<1/\sqrt3\). If \(3x^2\ge V\), the branch increases in \(x\), so is at most \(5-V\le E_1\), since \(E_1-(5-V)=1-U>0\). Therefore \(F(x)\le\max(E_0,E_1)\) for all \(x\), and equality occurs at \(x=0\) or \(|x|=1\). Division by \(d\) gives the asserted exact norm.

**4. Unique optimal truncation.** The center value \(E_0/d=1+2a^2/(1+a)\) is strictly increasing in \(a\in(0,1)\), whereas the endpoint value \(E_1/d=(5-a-2a^2)/(1+a)\) is strictly decreasing. They meet only when \(2a^2+a-2=0\). The unique admissible solution is \(a_*=(\sqrt{17}-1)/4\), yielding \(\varepsilon_*=1-a_*\) and \(E_0/d=E_1/d=3/(1+a_*)=\tfrac32(\sqrt{17}-3)\).

**5. Generalized Lebesgue constant.** In the original three *overlapping* means, the coefficient polynomials are
\[
c_0(x)=1+H(x),\quad c_-(x)=-x/\varepsilon-H(x)/2,\quad c_+(x)=x/\varepsilon-H(x)/2,\quad
H(x)=\frac{3(x^2-1/3)}{\varepsilon(1-\varepsilon)}.
\]
By the definition of the generalized Lebesgue constant, \(\Lambda=\max_x(|c_0|+|c_-|+|c_+|)\). Since \(|H(x)|\le2/[\varepsilon(1-\varepsilon)]\) and \(|c_-|+|c_+|=\max\{|H(x)|,2|x|/\varepsilon\}\le2/[\varepsilon(1-\varepsilon)]\), the sum is at most \(1+4/[\varepsilon(1-\varepsilon)]\). At \(x=1\) equality holds, since \(c_0>0\) and \(c_\pm<0\). This proves the exact formula and unbounded ratio, while the exact norm has finite limiting values \(2\) and \(5\) as \(\varepsilon\downarrow0\) and \(\varepsilon\uparrow1\), respectively.

## Verification
Execute `python3 verify.py` in the directory containing this document. The standard-library-only program checks exact polynomial reproduction, the linear transformation from overlapping to disjoint cell means, both norm and Lebesgue envelopes on a large rational grid, and exact piecewise-constant extremizers. A floating-point scan checks the separately proved optimal design. The verifier passed **414575 check groups**. These finite checks corroborate, but cannot replace, the preceding proof for every admissible real \(\varepsilon\) and input function.

## Relationship to prior work
Bruni Bruno and Erb (2023/2024), *Polynomial Interpolation of Function Averages on Interval Segments*, introduced the general segmental interpolation framework, the generalized Lebesgue constant, and the upper bound \(\|\Pi\|\le\Lambda\) (Theorem 4.1); they proved equality when the segments do not overlap and derived formulas for several special families. The present three-interval configuration is not the chain, common-left-endpoint, or uniform-arc-length arrangement analyzed there, and the published upper bound alone does not imply its exact shared-function norm or its unique optimal truncation. Their later *Fekete problem* (2024) optimizes determinants and analyzes generalized Lebesgue constants for different support families; the mock-Chebyshev histopolation paper (2024) treats other, principally non-overlapping designs. The exact quadratic overlap norm and the sharp minimax parameter are separate mathematical claims, subject to possible earlier equivalent formulations in specialized histopolation literature.

## Limitations
The theorem concerns degree-two reconstruction, these precisely specified overlapping intervals, exact integration, and common bounded function perturbations. It does not establish stability under independently corrupted mean measurements, under numerical cancellation in the displayed formula, at the singular endpoint designs \(\varepsilon\in\{0,1\}\), or for arbitrary higher-degree segment families. The generalized Lebesgue constant remains pertinent when mean data can be perturbed independently. Independent scientific validation and an exhaustive historical novelty certificate are not claimed.

## References
1. L. Bruni Bruno and W. Erb, *Polynomial Interpolation of Function Averages on Interval Segments*, arXiv:2309.00328, first submitted 2023-09-01; SIAM J. Numer. Anal. 62 (2024), 1759–1781. https://arxiv.org/abs/2309.00328 ; open original: https://www.research.unipd.it/retrieve/50caa65b-e7ec-4252-abcb-3e25c1f90836/2309.00328v1.pdf
2. L. Bruni Bruno and W. Erb, *The Fekete problem in segmental polynomial interpolation*, arXiv:2403.09378 (2024). https://arxiv.org/abs/2403.09378
3. L. Bruni Bruno, F. Dell'Accio, W. Erb, and F. Nudo, *Polynomial histopolation on mock-Chebyshev segments*, arXiv:2407.16825 (2024). https://arxiv.org/abs/2407.16825
