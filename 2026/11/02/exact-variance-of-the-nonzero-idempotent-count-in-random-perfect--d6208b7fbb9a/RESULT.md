# Exact variance of the nonzero-idempotent count in random perfect evolution algebras

## Finding

Let \(n\ge 2\), let \(q\) be a prime power, and choose a matrix \(A\) uniformly from \(\operatorname{GL}_n(\mathbb F_q)\). Give \(\mathbb F_q^n\) the evolution-algebra multiplication \(e_i e_j=0\) for distinct \(i,j\), and \(e_j^2=\sum_i A_{ij}e_i\). Let \(N(A)\) be the number of **nonzero** elements satisfying \(x^2=x\) (zero is excluded). Put \(Q=q^n\).

Then \(\mathbb E N=1\), and the exact second factorial moment, hence the exact variance, is

\[
\operatorname{Var}N=\mathbb E[N(N-1)] =
\begin{cases}
1,&q\text{ even},\\[2mm]
1-\dfrac{(q-1)((2q-1)^n-2q^n+1)}{2(q^n-1)(q^n-q)},&q\text{ odd}.
\end{cases}
\]

For every odd \(q\) and \(n\ge2\), the variance is strictly between zero and one. At fixed \(n\), as odd \(q\to\infty\),
\[
1-\operatorname{Var}N=(2^{n-1}-1)q^{1-n}+O_n(q^{-n}).
\]

More precisely, if \(x,y\) are two distinct nonzero vectors, the simultaneous-idempotent probability is zero unless the vectors \(x,y\) and their coordinatewise squares \(x^{[2]},y^{[2]}\) are each linearly independent; when both pairs are independent, the probability is exactly \(1/[(Q-1)(Q-q)]\).

## Assumptions and scope

The probability distribution is on *labeled, ordered-natural-basis* perfect evolution algebras defined by uniformly chosen invertible structure matrices, **not** on isomorphism classes with equal weights. Coordinates are relative to the fixed natural basis. The theorem holds for every finite field, including extensions of prime fields; \(n\ge2\) avoids the denominator \(Q-q=0\) in dimension one. For \(n=1\) the nonzero-idempotent count is identically one and its variance is zero.

We write \(x^{[2]}=(x_1^2,\ldots,x_n^2)^{\mathsf T}\), and \(x^2=Ax^{[2]}\). The idempotent count is a finite nonnegative integer for each matrix.

## Proof

**Step 1 (one fixed idempotent).** For every nonzero \(x\in\mathbb F_q^n\), its coordinate square vector is nonzero. A uniformly random invertible linear map sends a fixed nonzero vector to each of the \(Q-1\) nonzero vectors with equal probability, so
\[
\mathbb P(Ax^{[2]}=x)=\frac1{Q-1}.
\]
Summing over \(Q-1\) choices proves \(\mathbb E N=1\).

**Step 2 (two distinct idempotents).** If \(y=t x\) with \(t\in\mathbb F_q^\times\), and both \(x,y\) are idempotents, then
\[
t x=Ay^{[2]}=t^2 A x^{[2]}=t^2x,
\]
forcing \(t=1\). Thus distinct nonzero idempotents cannot be proportional.

If \(x,y\) are independent but their squared vectors are dependent, invertibility of \(A\) prevents \(Ax^{[2]}=x\) and \(Ay^{[2]}=y\). If both ordered pairs are independent, transitivity of \(\operatorname{GL}_n(\mathbb F_q)\) on ordered independent pairs (with identical stabilizer sizes) shows that the probability of these two prescribed equations is
\[
\frac1{(Q-1)(Q-q)}.
\]
This proves the pairwise assertion.

**Step 3 (characteristic two).** Every finite field of characteristic two has a bijective Frobenius square map. Therefore \(x^{[2]}\) and \(y^{[2]}\) are proportional if and only if \(x\) and \(y\) are proportional: from \(y_i^2=c x_i^2\) take the unique square root \(t\) of \(c\) and conclude \(y_i=t x_i\) for every coordinate. Hence every ordered independent pair is admissible in Step 2. There are \((Q-1)(Q-q)\) of them, proving \(\mathbb E[N(N-1)]=1\).

**Step 4 (odd characteristic: projective square collisions).** For a nonzero vector \(x\), let \(s\) be the number of its nonzero coordinates. There are \(\binom ns(q-1)^s\) such vectors. To count nonzero \(y\) with \(y^{[2]}\in\mathbb F_q^\times x^{[2]}\), observe that a proportionality factor must be a nonzero square. Write it as \(t^2\). Every nonzero coordinate of \(y\) is then \(\pm t x_i\), independently, and each zero coordinate stays zero. Dividing by the double representation \((t,\varepsilon_i)\sim(-t,-\varepsilon_i)\), we obtain exactly
\[
(q-1)2^{s-1}
\]
choices for \(y\). Among them, exactly \(q-1\) are scalar multiples of \(x\). The number \(B\) of ordered independent \((x,y)\) whose squared vectors are dependent is therefore
\[
\begin{aligned}
B&=\sum_{s=1}^{n}\binom ns(q-1)^s\big((q-1)2^{s-1}-(q-1)\big)\\
&=\frac{q-1}{2}\big((2q-1)^n-2q^n+1\big).
\end{aligned}
\]
Of all \((Q-1)(Q-q)\) ordered independent pairs, exactly \(B\) must be removed. Step 2 gives
\[
\mathbb E[N(N-1)]=1-\frac{B}{(Q-1)(Q-q)},
\]
which is the stated odd-characteristic formula.

**Step 5 (variance, strictness, asymptotic).** Since \(\mathbb E N=1\),
\[
\operatorname{Var}N=\mathbb E[N^2]-1=\mathbb E[N(N-1)].
\]
For odd \(q\), \(B>0\) because a vector with support at least two produces nonproportional square-colliding vectors (e.g. changing one coordinate sign). Also \(B<(Q-1)(Q-q)\), since \((e_1,e_2)\) is an admissible ordered pair. Hence the variance is strictly between zero and one. Finally expanding the displayed formula in powers of \(1/q\), for fixed \(n\ge2\), gives the stated leading deficit \((2^{n-1}-1)q^{1-n}\) with remainder \(O_n(q^{-n})\). This finishes the proof.

## Verification

The standalone \(\texttt{verify\_moments.py}\) exhaustively enumerates every invertible structure matrix over the chosen finite fields and determines the nonzero idempotents directly from \(A x^{[2]}=x\), without using the pair-counting proof. It checks both the mean and exact second factorial moment, using rational arithmetic.

Tested examples include \((q,n)=(2,2),(3,2),(5,2),(7,2),(2,3),(3,3),(2,4),(4,2),(9,2),(4,3)\), with \(\mathbb F_4\) and \(\mathbb F_9\) implemented using irreducible quadratic polynomials. All checks passed and the program ended with \(\texttt{VERIFY\_OK}\).

For example the observed exact variances are \(5/6\) for \((q,n)=(3,2)\), \(13/15\) for \((5,2)\), \(23/26\) for \((3,3)\), and \(41/45\) for \((9,2)\). Every tested even-characteristic example has variance one. These experiments are independent corroboration; the proof is uniform in \(q,n\).

Run with Python 3: \(\texttt{python3 verify\_moments.py}\). No third-party packages are needed.

## Relationship to prior work

Kaygorodov, Martín González and Viruel (arXiv:2610.22248v1, posted 15 October 2026) prove in Remark 23 that the **first** moment for uniformly random invertible structure matrices equals one; their Question 22 and Conjecture 2 motivate the study of the idempotent-count distribution and its putative permutation-fixed-point limit. They do not state the second factorial moment in the inspected Remark 23 and conjecture discussions. The result above makes that next moment exact and identifies the finite-field characteristic dependence, without asserting the limiting distribution.

Wei and Zou (arXiv:2310.12368v1, 2023) enumerate **isomorphism classes** of perfect evolution algebras via a monomial group action on structure matrices. Their full-text introduction and counting development concern orbit counts, not the uniformly matrix-weighted nonzero-idempotent second moment. Neither orbit counts nor the already-known mean imply the formula in this note.

## Limitations

This theorem does not determine the full distribution of \(N\), its higher factorial moments, the probability of no nonzero idempotent, or analogous statistics for sampling isomorphism classes uniformly. The finite checks are not substitutes for the arbitrary-field-size argument. Historical-priority uncertainty remains for differently phrased finite-field quadratic-map moment calculations.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first posted 2026-10-15), especially Remark 23, Question 22, and Conjecture 2. https://arxiv.org/abs/2610.22248
2. Y. Wei, Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, Linear Algebra Appl. 675 (2023), 142–178; arXiv:2310.12368v1. https://arxiv.org/abs/2310.12368
