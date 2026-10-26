# Cusp-collision trichotomy in the characteristic-three cyclic trigonal quintic

## Finding
For the coefficientwise characteristic-three plane-quintic model of the cyclic \((3,5)\) trigonal family, the finite cusps form a complete three-step collision pattern. The generic basket has four cusps of value semigroup \(\langle2,3\rangle\); on the coefficient hypersurface \(a_1=a_4a_2\) it becomes one cusp of semigroup \(\langle3,4\rangle\) plus one of semigroup \(\langle2,3\rangle\); on its further sublocus \(a_2=-a_4^3\) it becomes a single cusp of semigroup \(\langle3,5\rangle\). The infinity cusp always has semigroup \(\langle2,5\rangle\). The normalization is \(\mathbb P^1\); over any finite field of characteristic three containing the coefficients, the point count is \(q^n+1\) over every \(\mathbb F_{q^n}\).

## Assumptions and scope
Work over an algebraically closed perfect field \(k\) of characteristic \(3\). Let
\[
F(x)=x^5+a_4x^4+a_3x^3+a_2x^2+a_1x+a_0
\]
be squarefree; this is the natural smooth-parameter locus for the characteristic-zero cyclic trigonal family. Denote the quintic in \(\mathbb P^2\) by
\[
X_F:\quad Y^3Z^2=X^5+a_4X^4Z+a_3X^3Z^2+a_2X^2Z^3+a_1XZ^4+a_0Z^5.
\]
The value semigroup of a branch means the positive orders attained by nonzero elements of its completed local ring inside \(k[[u]]\); the delta invariant is the normalization quotient length.

## Proof
**Normalization and integrality.** Choose unique cube roots \(b_i^3=a_i\) and put \(G(u)=u^5+b_4u^4+b_3u^3+b_2u^2+b_1u+b_0\). The morphism \(\mathbb P^1\to\mathbb P^2\) given in homogeneous source coordinates \([S:T]\) by
\[
[S:T]\longmapsto[S^3T^2:G_h(S,T):T^5]
\]
is base-point free and lands on \(X_F\), because \(G_h(S,T)^3=F_h(S^3,T^3)\). The affine function fields satisfy \(k(t^3,G(t))=k(t)\): the extension \(k(t)/k(t^3)\) has degree three, while \(G(t)\notin k(t^3)\), because its leading term has degree five. Thus this morphism is finite, birational, and the normalization. It also shows geometric integrality.

**Singular support.** In the affine chart \(Z=1\), the partial derivative with respect to \(y\) of \(y^3-F(x)\) vanishes identically, whereas its \(x\)-derivative is \(-F'(x)\). Thus the finite singular support consists precisely of critical points of \(F\), with one point over each root because cubing is bijective on \(k\). On \(Z=0\) the equation forces \(X=0\), giving the unique point \([0:1:0]\).

**Critical-point multiplicities.** Direct differentiation gives
\[
F'(x)=2x^4+a_4x^3+2a_2x+a_1,\qquad F''(x)=2(x^3+a_2).
\]
Since \(F''\) has one root \(r\), counted three times, with \(r^3=-a_2\), a repeated root of \(F'\) must be \(r\). Evaluating gives \(F'(r)=a_1-a_4a_2\). If this is nonzero, \(F'\) has four distinct roots. If it vanishes, the exact identity
\[
F'(x)=2(x-r)^3(x-a_4)
\]
holds. Accordingly its roots have multiplicities \((3,1)\) when \(r\ne a_4\), and \((4)\) when \(r=a_4\), equivalently \(a_2=-a_4^3\). There are no other multiplicity patterns.

**Local branch types.** At a finite singularity write \(t=t_0+u\). The normalization expansion is \(x-x_0=u^3\) and \(y-y_0=G(t_0+u)-G(t_0)\), with
\[
G'(t)^3=F'(t^3).
\]
If the critical root has multiplicity \(1\), the second coordinate begins in degree \(2\), so the semigroup is \(\langle2,3\rangle\), of delta \(1\). If the multiplicity is \(3\), subtracting a scalar multiple of \(x-x_0\) leaves first term of degree \(4\), giving semigroup \(\langle3,4\rangle\), of delta \(3\). If multiplicity is \(4\), the analogous first term has degree \(5\), giving semigroup \(\langle3,5\rangle\), of delta \(4\). In each case the two displayed coprime leading orders generate the full value semigroup of this one-Puiseux-pair plane branch. At infinity use \(s=T/S\) as parameter; in the chart \(Y=1\) the coordinates have initial orders \(2\) and \(5\), giving semigroup \(\langle2,5\rangle\) and delta \(2\). Therefore the total delta is \(4+2=6\), equal to the arithmetic genus of the plane quintic; the classification is complete.

**Arithmetic.** When all coefficients lie in \(\mathbb F_q\), cube-root coefficients also lie there. The normalization morphism is bijective on \(\mathbb F_{q^n}\)-points for every \(n\): over an affine point there is exactly one \(t\) with \(t^3=x\), and the only point at infinity has one rational preimage. Hence \(\#X_F(\mathbb F_{q^n})=q^n+1\). Summing the logarithmic zeta series gives \(Z(X_F/\mathbb F_q,T)=1/((1-T)(1-qT))\).

## Verification
Run `python cyclic_quintic_char3_checker.py` using Python 3. It tests the three strata using squarefree explicit witnesses \(x^5+x^3+x+1\), \(x^5+x^4+2\), and \(x^5+1\), exact derivative-gcd patterns, the coefficient trichotomy across all \(3^5\) monic quintics over \(\mathbb F_3\), and counts over \(\mathbb F_3\) and \(\mathbb F_9\). Finite checks corroborate the identities but do not prove the universal assertions, which follow from the argument above.

## Relationship to prior work
Baldwin, Eilbeck, Gibbons and Ônishi investigate complex abelian and sigma functions of precisely this cyclic trigonal genus-four family; that construction and the generic genus are prior work. The characteristic-three inseparability is elementary and is not claimed as a standalone novelty. The focused contribution is the coefficient-exact full three-stratum cusp collision, branch semigroups, total delta, and resulting exact model-specific arithmetic. Standard plane-branch techniques for delta and semigroups are also prior knowledge. Literature overlap cannot be excluded; no claim of independent verification is made.

## Limitations
The theorem concerns the displayed **plane quintic model** over characteristic three and its normalization, not regular or semistable reduction of an integral arithmetic family, its stable special fibre, or the Jacobian specialization. The classification assumes \(F\) squarefree. Its arithmetic statement requires all coefficients in the finite field. The proof does not determine the full infinitesimal Jacobian scheme at infinity. Historical literature may contain equivalent computations.

## References
Baldwin, Eilbeck, Gibbons, Ônishi, *Abelian Functions for Cyclic Trigonal Curves of Genus Four* (2006), arXiv:math/0612654, https://arxiv.org/abs/math/0612654.

Cassou-Noguès and Płoski, *Invariants of plane curve singularities and Newton diagrams* (2012), arXiv:1207.1600, https://arxiv.org/abs/1207.1600 (general singularity methods; not a source of the specific trichotomy).
