# Sharp numerical radius of a three-point conditional-expectation commutator

## Finding
Let \(X=\ell_4^3(\mathbb R)\). On the uniform three-point probability space, let \(P\) and \(Q\) be conditional expectations associated respectively with the partitions \(\{\{1,2\},\{3\}\}\) and \(\{\{1\},\{2,3\}\}\):
\[
P(a,b,c)=((a+b)/2,(a+b)/2,c),\qquad
Q(a,b,c)=(a,(b+c)/2,(b+c)/2).
\]
For their commutator \(K=PQ-QP\), the **sharp real spatial numerical radius** is
\[
\boxed{v_X(K)=\frac{\sqrt{3\sqrt6}}{16}=0.1694253756768459\ldots .}
\]
Moreover, the complete set of nonzero maximizing vectors is specified explicitly below by one orbit under coordinate permutations and nonzero real scalar multiplication.

## Assumptions and scope
Everything in the theorem is **real**, finite-dimensional, and concerns the spatial numerical radius, not the absolute numerical radius and not the operator norm. The probability-normalized \(L_4\)-norm \((\sum_i|x_i|^4/3)^{1/4}\) differs from the sequence-space norm \((\sum_i|x_i|^4)^{1/4}\) by a common scalar; this change does not alter spatial numerical radius.

For a bounded real operator \(T\) on the strictly convex and smooth space \(X\), define
\[
v_X(T)=\sup\{|x^*(Tx)|:\|x\|_4=\|x^*\|_{4/3}=1,\ x^*(x)=1\}.
\]
The unique supporting functional at \(x\ne0\) gives the equivalent homogeneous formula
\[
v_X(T)=\sup_{x\ne0}\frac{|\sum_{i=1}^3x_i^3(Tx)_i|}{\sum_{i=1}^3x_i^4}.
\]
Direct composition gives
\[
K=\frac14\begin{pmatrix}0&-1&1\\1&0&-1\\-1&1&0\end{pmatrix}.
\]

## Proof
**1. Alternating quartic and centered invariants.** Write \(x=(a,b,c)\). Direct expansion yields the exact identity
\[
\sum_{i=1}^3x_i^3(Kx)_i
=-\frac14(a-b)(a-c)(b-c)(a+b+c).
\]
Put \(t=(a+b+c)/3\), \(y_i=x_i-t\), \(s=\sum_i y_i^2\), and \(q=\sum_i y_i^3\). Then \(\sum_i y_i=0\). If \(s=0\), the numerator is zero. Otherwise, homogeneity allows us to take \(s=1\), and replacing \(x\) by \(-x\) allows \(t\ge0\). A positive maximum requires \(t>0\).

Newton identities for a zero-sum triple give
\[
\sum_i y_i^4=\frac12,
\qquad
\sum_i(t+y_i)^4=\frac12+4tq+6t^2+3t^4.
\]
With \(\Delta=(y_1-y_2)(y_1-y_3)(y_2-y_3)\), the \(y_i\) are roots of the depressed cubic
\[
z^3-\frac z2-\frac q3=0,
\]
whose discriminant gives
\[
\Delta^2=\frac12-3q^2,
\qquad |q|\le\frac1{\sqrt6}.
\]
Conversely, **every** \(q\) in this closed interval corresponds to three real roots with sum zero and squared sum one (allowing repeated roots at the endpoints). Thus optimizing over \(q\) loses no configurations.

**2. Exact optimization over the cubic invariant.** Define
\[
A(t)=\frac12+6t^2+3t^4,
\quad B(t)=\frac{4t}{\sqrt6},
\quad u=-\sqrt6\,q\in[-1,1].
\]
The numerical-radius quotient becomes
\[
\frac{3t}{4\sqrt2}\frac{\sqrt{1-u^2}}{A(t)-B(t)u}.
\]
For \(t>0\),
\[
A(t)-B(t)\ge\frac12+6t^2-\frac{4t}{\sqrt6}\ge\frac7{18}>0.
\]
The logarithmic derivative in \(u\) has the sign of \(B-Au\). Therefore the unique maximizing parameter is \(u=B/A\in(0,1)\), with maximum
\[
F(t)=\frac{3t}{4\sqrt2\sqrt{A(t)^2-B(t)^2}}.
\]

**3. Global one-variable optimization.** Set \(r=t^2\ge0\) and \(A(r)=\tfrac12+6r+3r^2\). Then
\[
F(\sqrt r)^2=\frac{9r}{32\bigl(A(r)^2-\frac83r\bigr)}.
\]
Its derivative for positive \(r\) has the same sign as
\[
A(r)\bigl(A(r)-2rA'(r)\bigr)
=A(r)\left(\frac12-6r-9r^2\right).
\]
Consequently it increases and then decreases, with its **unique** maximum at
\[
r_0=\frac{\sqrt6-2}{6}.
\]
The endpoint limits \(r\downarrow0\) and \(r\to\infty\) both give zero. Exact substitution gives
\[
F(\sqrt{r_0})^2=\frac{3\sqrt6}{256}.
\]
Taking the positive square root proves the claimed value.

**4. All maximizing vectors.** Let
\[
t_0=\sqrt{\frac{\sqrt6-2}{6}},
\qquad q_0=-\frac{t_0}{\sqrt6-1}.
\]
Let \(y_1,y_2,y_3\) be the three real roots of \(z^3-z/2-q_0/3=0\), in any order. Since \(|q_0|<1/\sqrt6\), the roots are distinct. All nonzero norming vectors are exactly
\[
\left\{\lambda\bigl(t_0+y_{\sigma(1)},\ t_0+y_{\sigma(2)},\ t_0+y_{\sigma(3)}\bigr):
\lambda\in\mathbb R\setminus\{0\},\ \sigma\in S_3\right\}.
\]
Indeed, equality at the two successive strict maxima forces \(r=r_0\) and \(q=q_0\) after the stated scaling and sign normalization. Conversely all displayed vectors attain equality, as absolute Vandermonde products are permutation-invariant.

## Verification
The accompanying standard-library script `verification.py` checks, using exact rational polynomial arithmetic, the alternating-quartic factorization and the cubic discriminant identity. It numerically reconstructs the three extremal roots and all their permutations, checks the sharp expression to floating-point precision, and compares against 60,000 deterministically sampled nonzero vectors. It reports `EXACT_POLYNOMIAL_IDENTITIES_OK` and `NUMERICAL_SPOT_CHECKS_OK`. The proof of the global inequality is analytic in the preceding section; random sampling is a diagnostic only.

## Relationship to prior work
Martín, Merí and Popov study numerical and absolute numerical radii in real and complex \(L_p\)-spaces, including the numerical radius of the two-coordinate skew rotation and general estimates for numerical indices. Their two-coordinate rotation formula concerns a different operator and does not determine this three-coordinate commutator. Chica, Martín and Merí analyze rank-one operators, whereas this commutator has rank two. Kim, Lee and Martín establish a qualitative Bishop–Phelps–Bollobás property for numerical-radius attainment, not an exact value for this operator. The present computation resolves a specific sharp three-point noncommuting-expectation example; it does **not** determine numerical indices or numerical radii of arbitrary commutators. In the real Hilbert case \(\ell_2^3\), the same matrix has numerical radius zero by skew symmetry, making the nonzero \(\ell_4\) value a quantified departure from Hilbert geometry.

## Limitations
The theorem is restricted to real \(\ell_4^3\), the two specified conditional expectations and their commutator. No assertion is made for complex scalars, unequal atom probabilities, other powers, or arbitrary finite partitions. The analytical argument proves the exact value and all equality cases; it is not a computer-assisted exhaustive search. Searchable-publication comparisons cannot rule out unindexed historical statements. Independent verification has not been performed.

## References
1. M. Martín, J. Merí, M. Popov, *On the numerical radius of operators in Lebesgue spaces*, arXiv:1011.4785v1 (public 2010-11-22), https://arxiv.org/abs/1011.4785 ; author-hosted full text https://www.ugr.es/~mmartins/Curriculum/Papers/pre-MarMerPop(2).pdf .
2. M. Chica, M. Martín, J. Merí, *Numerical radius of rank-1 operators on Banach spaces*, Quarterly Journal of Mathematics 65 (2014), 89–100, https://doi.org/10.1093/qmath/has050 ; author-deposited text https://www.researchgate.net/publication/261062614_NUMERICAL_RADIUS_OF_RANK-1_OPERATORS_ON_BANACH_SPACES .
3. S. K. Kim, H. J. Lee, M. Martín, *On the Bishop–Phelps–Bollobás Property for Numerical Radius*, Abstract and Applied Analysis (2014), article 479208, https://doi.org/10.1155/2014/479208 .
