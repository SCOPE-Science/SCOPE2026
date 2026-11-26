# Sharp degree-four realization of the pentagonal nonnegative Fourier Gram obstruction

## Finding

Let \(\theta=2\pi/5\), \(\varphi=(1+\sqrt5)/2\), and \(\eta=1/\varphi\). Suppose \(f\) is a real even trigonometric polynomial, pointwise nonnegative on the circle, with nonnegative Fourier coefficients, \(f(0)=1\), and \(f(2\theta)=0\).

**Sharp exclusion at small degree.** If \(f\) has Fourier degree at most three, then
\[
 f(\theta)\le \eta^2=\frac{3-\sqrt5}{2},
\]
with equality only for \(f(t)=((\cos t+\varphi/2)/(1+\varphi/2))^2\). In particular, for these degrees the matrix \((f((j-k)\theta))_{0\le j,k<5}\) is completely positive. It follows that the exact five-cycle zero-chord obstruction to complete positivity requires Fourier degree at least four. Equality in this degree threshold follows using the known degree-four polynomial of Kolountzakis and Révész [1, Example 3], normalized at zero. The quartic, its sampled matrix \(I+\eta A(C_5)\), and the unrestricted sample optimum \(\eta\) are supporting facts, not claims of originality here.

## Assumptions and scope

Write \(f(t)=a_0+2\sum_{j=1}^m a_j\cos jt\) with \(a_j\ge 0\), so that \(f\) is positive definite on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). A matrix is completely positive if it is a sum of real matrices \(vv^{\mathsf T}\) with \(v\) entrywise nonnegative. This is different from complete positivity of a linear map. A doubly nonnegative matrix is real symmetric, entrywise nonnegative, and positive semidefinite. The threshold is specific to real even polynomials, five equally spaced nodes, and the exact zero at \(4\pi/5\).

## Proof

### Sharp upper bound and uniqueness at degree at most three

Set \(x=\cos t\), \(c=\cos(2\theta)=-\varphi/2\), and \(d=\cos\theta=\eta/2\). A polynomial in the admissible class of degree at most three has the form \(f(t)=P(x)\). Its nonnegativity on \([-1,1]\) and its interior zero at \(c\) imply \(P'(c)=0\). Thus \(P(x)=(x-c)^2(A_0+Bx)\). The coefficient of \(\cos 3t\) is \(B/4\), so \(B\ge0\). Since \(d<1\) and \(P(1)=1\),
\[
 f(\theta)=\left(\frac{d-c}{1-c}\right)^2 \frac{A_0+Bd}{A_0+B}
 \le \left(\frac{d-c}{1-c}\right)^2=\eta^2.
\]
The inequality is strict if \(B>0\); if \(B=0\), normalization yields the displayed optimizer. The latter is a square and its constant, first-cosine, and second-cosine coefficients are positive by \(\cos^2t=(1+\cos 2t)/2\).

### Consequence for the five-point Gram matrix

Set \(q=f(\theta)\ge0\). The zero-chord sample is \(G_f=I+qA\) with \(A=A(C_5)\). For \(0\le q\le1/2\), the identity
\[
 I+qA=(1-2q)I+q\sum_{j=0}^4(e_j+e_{j+1})(e_j+e_{j+1})^{\mathsf T}
\]
with cyclic indices gives complete positivity, so the sharp bound \(\eta^2<1/2\) excludes the obstruction at degrees at most three.

For later use the classical Horn matrix \(H=J-2A\), with \(J\) all ones, is copositive. If \(v\ge0\) and two nonadjacent coordinates are positive, keeping their total fixed and putting it all at the vertex with the larger weighted sum of neighbors cannot decrease \(\sum_{\{i,j\}\in E(C_5)}v_i v_j\). Iterating leaves support on a clique, which has at most two vertices. Therefore the edge sum is at most \((\sum_i v_i)^2/4\), so \(v^{\mathsf T}Hv\ge0\). In particular \(\langle H,I+qA\rangle=5-10q<0\) for \(q>1/2\) rules out complete positivity. Also \(I+qA\) has an eigenvalue \(1-\varphi q\), so positive semidefiniteness implies \(q\le\eta\) at any degree.

### Attainment using the known quartic

In [1, Example 3, \(N=4\)], the polynomial
\[
 p_0(t)=1+\frac{4\cos t+\cos 4t}{5\cos(\pi/5)}
\]
is nonnegative, with \(p_0(0)=\sqrt5\) and \(p_0(2\theta)=0\). Its normalized version is
\[
 F(t)=\frac{p_0(t)}{p_0(0)}=\frac{5\varphi+8\cos t+2\cos4t}{5(\varphi+2)}.
\]
For a direct check of nonnegativity and the exact zero set, its numerator at \(x=\cos t\) factors as
\[
 16(x+\varphi/2)^2\left(x^2-\varphi x+(1+3\sqrt5)/8\right).
\]
The remaining quadratic has discriminant \(1-\sqrt5<0\), so the only zeros are \(t\equiv\pm2\theta\). The Fourier coefficients are nonnegative, and at \(\theta\) the two cosines agree and give \(F(\theta)=\eta\). The sample \(I+\eta A\) is the classical doubly nonnegative non-completely-positive pentagon matrix [2,3]; the Horn inequality above shows the separation since \(\eta>1/2\). Thus the degree threshold is sharp. This also recovers the already implied unrestricted sample optimum \(\eta\).

### Degree-preserving strict example (illustration)

If the zero-chord condition is relaxed, let \(L(t)=1+\cos2t\) and \(K_\delta=(F+\delta L)/(1+2\delta)\). For \(\delta>0\), the summands have disjoint zero sets (the zeros of \(L\) have \(\cos t=0\)), so \(K_\delta>0\). The positive Fourier coefficients at \(0,\pm1,\pm2,\pm4\) represent all residues modulo five, giving a positive definite five-point sample matrix. The Horn pairing is
\[
 \langle H,G_{K_\delta}\rangle=\frac{5[(2-\sqrt5)+\delta(2+\sqrt5)]}{1+2\delta},
\]
which is negative for \(0<\delta<9-4\sqrt5\). This follows from the diagonal and two chord values of \(L\), namely \(2,1+c,1+d\). The range certifies this witness and is not a complete-positivity transition theorem or a minimum-degree result without the chord constraint.

## Verification

The accompanying `verify.py` gives replayable SymPy checks for the radical identities, quartic factorization, sample values, and Horn pairing; it additionally checks the example \(\delta=1/100\) numerically. The degree bound and equality classification are proved above, not inferred from a finite check.

## Relationship to prior work and limitations

The contribution is the sharp degree-at-most-three bound and unique equality case under the exact chord-zero hypothesis, and hence the sharp bandwidth threshold when paired with the prior witness. Kolountzakis and Révész [1] obtain the quartic from a Turán problem, maximizing \(p(0)\) at fixed constant coefficient and sparse frequency support. Their \(N=4\) formula implies the degree-four attainment and, together with the pentagon eigenvalue bound, the unrestricted optimum here. It does not give the sharp bound among degrees at most three under the chord constraint. Their related pointwise estimates [4] optimize a Fourier coefficient with a specified support, not the chord-value ratio under an interior zero. The matrix obstruction and Horn separation are classical [2,3]. General positive-definite extension results, such as [5], address a different formulation; complete positivity of maps does not mean a real Gram factorization by nonnegative vectors. This comparison does not establish exhaustive historical priority for the degree-three inequality. No threshold for different nodes, without the exact chord condition, or for noneven kernels is asserted.

## References

1. M. N. Kolountzakis and S. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218v1, Example 3, p. 12. https://arxiv.org/abs/math/0312218
2. S. Burer, K. M. Anstreicher, and M. Dür, *The difference between 5 × 5 doubly nonnegative and completely positive matrices*, Linear Algebra Appl. **431** (2009), 1539–1552. https://doi.org/10.1016/j.laa.2009.05.021
3. G. Peyré, *Two notions of positivity, separated by a pentagon* (2026-07-04). https://www.gpeyre.com/blog/2026/07/04/doubly-nonnegative-completely-positive/
4. M. N. Kolountzakis and S. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, arXiv:math/0302193v1. https://arxiv.org/abs/math/0302193
5. S. S. Damase and J. E. Pascoe, *Complete Discrete Schoenberg-Delsarte theory for homogeneous spaces*, arXiv:2602.09010v1. https://arxiv.org/abs/2602.09010
