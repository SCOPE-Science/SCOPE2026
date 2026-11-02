# Reentrant endpoint positivity for a palindromic Euler splitting of two-state Markov generators

## Finding

For \(a,b>0\), split a two-state continuous-time Markov generator into its one-way components
\[
 A=\begin{pmatrix}-a&a\\0&0\end{pmatrix},\qquad
 B=\begin{pmatrix}0&0\\b&-b\end{pmatrix}.
\]
Consider the **palindromic product of three forward-Euler factors**
\[
 P_h=(I+hA/2)(I+hB)(I+hA/2),\qquad h\ge0.
\]
Although its factors need not be nonnegative, \(P_h\) preserves every probability row vector **if and only if**
\[
 0\le h\le\frac{2}{a},\qquad bh\left(1-\frac{ah}{2}\right)\le1.
\]
For \(b\le2a\) the positivity set is exactly \([0,2/a]\). For \(b>2a\) it consists of two disjoint closed intervals,
\[
 [0,h_-]\cup[h_+,2/a],\qquad
 h_\pm=\frac{1\pm\sqrt{1-2a/b}}{a}.
\]
The open interval \((h_-,h_+)\) fails positivity: the bottom-right entry is negative. Thus positivity can be lost and restored as the positive timestep increases. Both branches are exact, including equality endpoints.

## Assumptions and scope

The rates \(a,b\) are arbitrary strictly positive real numbers and \(h\ge0\). Probability distributions are row vectors. Every row of \(A\), \(B\), and hence the first-order product generator, sums to zero. For each fixed \(h\), \(P_h\) is therefore row-sum-one. It maps *every* nonnegative probability row vector to another precisely when all four entries are nonnegative. Only the **one-step composed endpoint** is asserted to be positive; the intermediate factors or intermediate stages are not assumed positive. The palindromic use of forward Euler is a first-order approximation to the unsplit flow and must not be confused with the second-order Strang splitting of exact subflows.

## Proof

Define \(x=ah/2\) and \(y=bh\). The two factors become
\[
 E=\begin{pmatrix}1-x&x\\0&1\end{pmatrix},\qquad
 F=\begin{pmatrix}1&0\\y&1-y\end{pmatrix}.
\]
Direct multiplication gives the **exact factorization**
\[
 EFE=\begin{pmatrix}
 (1-x)(1-x+xy)&x[2-x-y(1-x)]\\
 y(1-x)&1-y(1-x)
 \end{pmatrix}. \tag{1}
\]
The matrix is row-sum-one. Since \(y>0\) when \(h>0\), its bottom-left entry can be nonnegative only if \(x\le1\). Thus \(h\le2/a\) is necessary for \(h>0\); \(h=0\) is trivially positive. If \(0\le x\le1\), the upper-left entry of (1) is nonnegative. Nonnegativity of the bottom-right entry is equivalent to \(y(1-x)\le1\). Under this inequality, the upper-right entry obeys
\[
 x[2-x-y(1-x)]\ge x(1-x)\ge0.
\]
All four entries are therefore nonnegative exactly when \(x\le1\) and \(y(1-x)\le1\), proving the first equivalence.

On \([0,2/a]\), the concave quadratic \(g(h)=bh(1-ah/2)\) has its unique maximum at \(h=1/a\), with \(g(1/a)=b/(2a)\). For \(b\le2a\) the criterion is met everywhere. For \(b>2a\), the two solutions of \(g(h)=1\) are the stated \(h_-<h_+\), and concavity gives precisely the two positive intervals and the intervening negative interval. This proves both sharp boundaries without extrapolation from numerical experiments.

For instance, \(a=1,b=4\) yields \(h_-=1-1/\sqrt2\) and \(h_+=1+1/\sqrt2\). At \(h=1/2\), the bottom-right entry is \(-1/2\), whereas at \(h=19/10\), all entries are nonnegative even though the bottom-right entry of the middle factor \(I+hB\) is \(-33/5\). At the upper endpoint \(h=2/a\), formula (1) gives
\[
 P_{2/a}=\begin{pmatrix}0&1\\0&1\end{pmatrix},
\]
independent of \(b\). In contrast, the exact flow \(e^{h(A+B)}\) has positive entries and retains its nondegenerate stationary distribution \((b/(a+b),a/(a+b))\). Hence endpoint positivity alone is not an accuracy guarantee.

## Verification

The standalone script `verify.py` symbolically multiplies the matrices and verifies (1). It tests 6,006 timestep-rate triples across contrasting ratios, comparing the exact sign criterion against all four directly evaluated entries. Run `python verify.py` after installing `sympy`. The finite checks corroborate the algebra; the proof above, not the grid, establishes the universal all-real-parameter claim.

## Relationship to prior work

Bréhier, Cohen and Ulander (2023) analyze positivity-preserving Lie–Trotter integration of stochastic heat equations with exact positive subflows; their scheme and its unconditional subflow positivity are distinct from the present **forward-Euler substeps that can individually lose positivity**. Blanes, Casas and Murua (2024) survey positivity-preserving splitting with matrix exponentials and preservation of mass and positivity, not the explicit product (1). Published examples of nonmonotone positivity in rational approximations to Markov semigroups are conceptually related, but concern different one-step maps and do not imply the two-parameter formula here. The basic matrix multiplication is elementary; the claim is the exact global reentrant endpoint-positivity classification for this natural composed scheme, not a general statement about all splitting methods.

## Limitations

The result is restricted to two-state one-way generator components and the displayed three-factor forward-Euler composition. It is not an unconditional CFL rule for higher dimensions, arbitrary splittings, second-order Strang integration, or stochastic heat equations. The large-timestep positive branch can be highly inaccurate: at \(h=2/a\), the endpoint map is absorbing despite an irreducible underlying chain. No convergence advantage or improved physical simulation accuracy is claimed. Separate published literature may contain an equivalent two-state special case; independently checking priority remains necessary.

## References

1. C.-E. Bréhier, D. Cohen and J. Ulander, *Positivity-preserving schemes for some nonlinear stochastic PDEs*, arXiv:2304.11064v1 (first public 2023-04-21), https://arxiv.org/abs/2304.11064 . Sections 1 and 3.
2. S. Blanes, F. Casas and A. Murua, *Splitting methods for differential equations*, arXiv:2401.01722 (2024), https://arxiv.org/abs/2401.01722 . Section 9.2.1.
3. Related published result: *Eight-state barrier for Markov positivity of the [2/2] Padé map*, https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab . Distinct rational integrator and eight-state model.
4. Related published result: *Two-state immunity and three-state sharpness for endpoint positivity of SSP-SDIRK2(2)*, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-two-state-immunity-and-three-state-sharpness-for-endpoint-positi--46bf11cc19c7 . Distinct implicit Runge–Kutta map.
