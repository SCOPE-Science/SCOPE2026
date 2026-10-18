# Exact two-coordinate Khinchin phase transition for a two-radius Rademacher perturbation

## Finding
For \(0\le d<1\), let \(R_d\) take the two values \(1-d\) and \(1+d\) with probability \(1/2\) each, let \(\varepsilon\) be an independent fair random sign, and normalize
\[
X_d=\frac{\varepsilon R_d}{\sqrt{{1+d^2}}}.
\]
Then \(X_d\) is symmetric, has variance one, and has four nonzero atoms when \(0<d<1\).

For two iid copies \(X_{{d,1}},X_{{d,2}}\), consider
\[
K_d(a,b)=\mathbb E\left|aX_{{d,1}}+bX_{{d,2}}\right|,
\qquad a^2+b^2=1.
\]
There is a sharp transition at the unique root \(d_\ast\in(0,1)\) of
\[
d^3+4d^2+d-4=0,
\]
namely \(d_\ast=0.813606502648331\ldots\). Up to signs and permutation of the coefficients:

- for \(0\le d<d_\ast\), the unique minimizer is \(a=b=1/\sqrt2\);
- for \(d=d_\ast\), the equal-weight vector ties exactly with the vector whose ratio is \(b/a=(1-d)/(1+d)\);
- for \(d_\ast<d<1\), the unique minimizer has \(b/a=(1-d)/(1+d)\).

Thus a natural two-radius perturbation of the Rademacher law has an exact two-coordinate coefficient-minimizer phase transition.

## Assumptions and scope
The claim concerns exactly two iid summands, the \(L_1\) norm, and the normalized symmetric four-point law above. It does not claim the global minimizer among coefficient vectors of arbitrary dimension. The variance normalization is included to place the family in the standard sharp-Khinchin setting; multiplying the summand law by a positive scalar does not change which coefficient vector minimizes the expectation.

By symmetry of \(X_d\), signs of \(a,b\) are immaterial. By permutation symmetry, it suffices to take \(a\ge b\ge0\), write \(t=b/a\in[0,1]\), and hence \(a=(1+t^2)^{{-1/2}}\).

## Proof
Put \(l=1-d\), \(h=1+d\), and \(c=l/h=(1-d)/(1+d)\). Conditional on positive magnitudes \(R_1,R_2\), averaging over the two independent signs gives
\[
\mathbb E_{{\varepsilon_1,\varepsilon_2}}
\left|a\varepsilon_1R_1+b\varepsilon_2R_2\right|
=\max(aR_1,bR_2)
=a\max(R_1,tR_2).
\]
Therefore
\[
K_d(t)=\frac{1}{\sqrt{{1+d^2}}\sqrt{{1+t^2}}}
\mathbb E\max(R_1,tR_2).
\]

If \(0\le t\le c\), then \(tR_2\le R_1\) for every pair of possible magnitudes, so \(\mathbb E\max(R_1,tR_2)=\mathbb ER_1=1\). Hence
\[
K_d(t)=\frac{1}{\sqrt{{1+d^2}}\sqrt{{1+t^2}}},
\qquad 0\le t\le c,
\]
which is strictly decreasing in \(t\).

If \(c\le t\le1\), the maximum changes only in the case \(R_1=l,R_2=h\), which has probability \(1/4\). Thus
\[
\mathbb E\max(R_1,tR_2)
=1+\frac{th-l}{4}
=\frac{3+d+(1+d)t}{4}.
\]
Consequently
\[
K_d(t)=\frac{A+Bt}{\sqrt{{1+d^2}}\sqrt{{1+t^2}}},
\quad
A=\frac{3+d}{4},\qquad B=\frac{1+d}{4}.
\]
After multiplication by the positive factor \(\sqrt{{1+d^2}}(1+t^2)^{{3/2}}\), the derivative has sign
\[
B-At=\frac{1+d-(3+d)t}{4}.
\]
It is positive before \(t=(1+d)/(3+d)\) and negative after it. Hence the only interior critical point on this branch is a maximum. Since the first branch decreases, every global minimum is therefore at \(t=c\) or \(t=1\).

The two endpoint values are
\[
K_d(c)=\frac{1+d}{\sqrt2(1+d^2)},
\qquad
K_d(1)=\frac{1+d/2}{\sqrt{{2(1+d^2)}}}.
\]
Their squared comparison is exact:
\[
8(1+d^2)^2\bigl(K_d(1)^2-K_d(c)^2\bigr)
=d\bigl(d^3+4d^2+d-4\bigr).
\]
For \(d>0\), the cubic \(q(d)=d^3+4d^2+d-4\) is strictly increasing on \([0,1]\), because
\[
q'(d)=3d^2+8d+1>0.
\]
Moreover \(q(0)=-4\) and \(q(1)=2\), so it has exactly one root \(d_\ast\in(0,1)\). The three regimes and their uniqueness statements follow. At \(d=0\), the first branch extends to \(t=1\) and is strictly decreasing, so equal weights are again uniquely minimizing up to the stated symmetries.

## Verification
The proof reduces the entire two-coordinate sphere to the single ratio \(t\in[0,1]\), evaluates the expectation exactly on both branches, locates the sole interior critical point of the second branch, and compares the only possible global-minimum endpoints by an exact polynomial identity. A symbolic replay checks the derivative reduction, the endpoint-difference factorization, and the numerical location of the unique cubic root; the symbolic calculation is supplementary to the analytic proof.

Boundary behavior was included explicitly: \(d=0\) is the Rademacher law, while \(d\uparrow1\) makes the imbalanced minimizing ratio tend to zero. The claim deliberately excludes \(d=1\), where the law acquires an atom at zero and falls into a structurally different family already discussed in earlier Khinchin literature.

## Relationship to prior work
Eskenazis, Nayar, and Tkocz prove distributional stability of Szarek's sharp Khinchin inequality for laws close to Rademacher under the coefficient restriction \(\|a\|_\infty\le1/\sqrt2\). Their concluding Remark 2 explicitly identifies the complementary regime \(\|a\|_\infty>1/\sqrt2\) as a different problem not covered by their theorems. For two coordinates, the restricted region contains only the equal-weight point, so their result does not compare it against imbalanced two-coordinate vectors.

Their Remark 1 also points to known examples where a different coefficient vector wins, including a Rademacher-type law with a large atom at zero. Havrilla and Tkocz study symmetric discrete-uniform laws and this atom-at-zero phenomenon. The present family is different for \(0<d<1\): it is a symmetric four-point law with two nonzero radii, and the calculation supplies its entire two-coordinate minimizer phase diagram rather than only an example of changed extremizer.

Targeted database searches for two-radius Rademacher perturbations, symmetric four-point Khinchin minimizers, coefficient-ratio phase transitions, and the complementary Szarek coefficient regime did not locate a statement implying this classification. The closest indexed materials concern other Khinchin distributions or unrelated phase diagrams.

## Limitations
The theorem is two-dimensional and does not decide whether the displayed two-coordinate minimizer remains globally optimal when three or more coefficients are allowed. It treats only the equal-probability two-radius perturbation and only the first absolute moment. The originality assessment cannot exclude an elementary equivalent calculation hidden under different terminology in older Khinchin or random-series literature.

## References
1. A. Eskenazis, P. Nayar, T. Tkocz, “Distributional stability of the Szarek and Ball inequalities,” arXiv:2301.09380v1 (2023); *Mathematische Annalen* 389 (2024), 1161–1185, DOI 10.1007/s00208-023-02669-9.
2. A. Havrilla, T. Tkocz, “Sharp Khinchin-type inequalities for symmetric discrete uniform random variables,” arXiv:1912.13345v1 (2019); *Israel Journal of Mathematics* 246 (2021), 281–297.
3. S. Szarek, “On the best constant in the Khintchine inequality,” *Studia Mathematica* 58 (1976), 197–208.
