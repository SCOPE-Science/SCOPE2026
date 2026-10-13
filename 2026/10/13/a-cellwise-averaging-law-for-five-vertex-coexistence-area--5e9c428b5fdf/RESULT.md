# A cellwise averaging law for five-vertex coexistence area
## Finding
Consider the genus-zero five-vertex model of Kenyon--Prause in the small-\(r\) regime, with positive periodic parameters \(\alpha_i\), \(1\le i\le m_1\), and \(\beta_j\), \(1\le j\le m_2\), satisfying \(\alpha_i\beta_j<1\) for every pair. Let \(\mathcal C\) be the coexistence subset of the slope triangle \(\mathcal N=\operatorname{conv}\{(0,0),(1,0),(0,1)\}\), bounded by \(s+t=1\) and the Kenyon--Prause coexistence curve. Define
\[
q_{ij}=(\alpha_i\beta_j)^2\in(0,1).
\]
Then the Euclidean area of the coexistence phase is
\[
\operatorname{Area}(\mathcal C)
=\frac1{m_1m_2}\sum_{i=1}^{m_1}\sum_{j=1}^{m_2}
\frac{1-q_{ij}^2+2q_{ij}\log q_{ij}}{2(1-q_{ij})^2}.
\]
Equivalently, since \(\operatorname{Area}(\mathcal N)=1/2\), the fraction of the slope polygon occupied by coexistence is the cellwise arithmetic mean
\[
\frac{\operatorname{Area}(\mathcal C)}{\operatorname{Area}(\mathcal N)}
=\frac1{m_1m_2}\sum_{i,j}
\frac{1-q_{ij}^2+2q_{ij}\log q_{ij}}{(1-q_{ij})^2}.
\]
Thus a nonlinear higher-period phase boundary has a global size invariant that decomposes exactly into the mean of the corresponding one-cell coexistence-area function.

## Assumptions and scope
The claim concerns precisely the small-\(r\) genus-zero family, meaning \(\alpha_i\beta_j<1\) for all \(i,j\). The source slope coordinates are used without rescaling. The result is an area identity for the phase region; it does not assert uniqueness of Gibbs states in its interior and does not extend here to mixed products crossing \(1\) or to the large-\(r\) regime.

Put \(a_i=\alpha_i^2\) and \(c_j=\beta_j^{-2}\). The small-\(r\) assumption is exactly \(a_i<c_j\) for every pair. Kenyon--Prause give the coexistence boundary, with \(R>0\), as
\[
s(R)=\frac1{m_1}\sum_i\frac{a_i}{R+a_i},
\qquad
t(R)=\frac1{m_2}\sum_j\frac{R}{R+c_j}.
\]
It connects \((1,0)\) to \((0,1)\).

## Proof
First, \(s(R)\) is strictly decreasing from \(1\) to \(0\). Moreover
\[
1-s(R)-t(R)
=\frac1{m_1m_2}\sum_{i,j}R\left(\frac1{R+a_i}-\frac1{R+c_j}\right)>0,
\]
because \(a_i<c_j\). Hence the source curve lies strictly below \(s+t=1\), so its enclosed coexistence area is
\[
\operatorname{Area}(\mathcal C)
=\int_0^1\bigl(1-s-T(s)\bigr)\,ds
=\frac12-\int_0^1T(s)\,ds,
\]
where \(T(s(R))=t(R)\).

Since
\[
-s'(R)=\frac1{m_1}\sum_i\frac{a_i}{(R+a_i)^2},
\]
changing variables from \(s\) to \(R\) gives
\[
\int_0^1T(s)\,ds
=-\int_0^\infty t(R)s'(R)\,dR
=\frac1{m_1m_2}\sum_{i,j}
\int_0^\infty
\frac{R}{R+c_j}\frac{a_i}{(R+a_i)^2}\,dR.
\]
For a fixed pair set \(q=a_i/c_j=(\alpha_i\beta_j)^2\) and \(R=a_i x\). The pair integral becomes
\[
I(q)=\int_0^\infty\frac{qx}{(1+qx)(1+x)^2}\,dx
=\frac{q}{q-1}-\frac{q\log q}{(q-1)^2}.
\]
The last equality follows by elementary partial fractions (or by differentiating an antiderivative and taking the two endpoint limits). Therefore
\[
\frac12-I(q)=
\frac{1-q^2+2q\log q}{2(1-q)^2}.
\]
Averaging this identity over \((i,j)\) proves the formula.

## Verification
The proof is analytic and uses only the published boundary parametrization plus elementary integration. The accompanying `verify.py` independently compares the closed formula with numerical quadrature of the published parametric boundary for several higher-period parameter sets satisfying \(\alpha_i\beta_j<1\). It also checks the one-cell specialization against the area obtained from the source's simply-periodic hyperbola. Numerical checks are corroborative and are not used as proof.

## Relationship to prior work
Kenyon and Prause derive the exact higher-period phase diagram and, in their Section 3.4, give the parametric coexistence boundary used above. Their Theorem 3.2 identifies this region as the zero-surface-tension coexistence phase, but they do not state its Euclidean area or a cellwise averaging law. The earlier simply-periodic work of de Gier, Kenyon, and Watson gives the one-weight coexistence boundary explicitly as a hyperbola. The formula above recovers the area of that hyperbolic region when \(m_1=m_2=1\), and shows that the higher-period area is exactly the arithmetic mean of those one-cell values. Aggarwal's ferroelectric six-vertex pure-state theorem treats existence and uniqueness relative to explicit hyperbolic forbidden regions, but it does not imply this staggered higher-period area decomposition.

## Limitations
The area is measured in the source slope coordinates and is not claimed to be invariant under arbitrary reparametrization of slope space. No statement is made about the probabilistic mixture inside the coexistence phase. The originality search cannot exclude an equivalent calculation hidden in weakly indexed literature or unpublished notes, although targeted searches of the exact formula, phase-area terminology, the primary source, and the closest predecessor found no covering result.

## References
1. R. Kenyon and I. Prause, *The genus-zero five-vertex model*, arXiv:2101.04195; Probability and Mathematical Physics 3 (2022), 707--729, DOI 10.2140/pmp.2022.3.707.
2. J. de Gier, R. Kenyon, and S. S. Watson, *Limit shapes for the asymmetric five vertex model*, arXiv:1812.11934; Communications in Mathematical Physics 385 (2021), 793--836, DOI 10.1007/s00220-021-04126-7.
3. A. Aggarwal, *Nonexistence and uniqueness for pure states of ferroelectric six-vertex models*, arXiv:2004.13272; Proceedings of the London Mathematical Society 124 (2022), 387--425, DOI 10.1112/plms.12430.
