# Sharp ninth-grid sixth moment and ninefold phase locking for four consecutive characters

## Finding

Let \(\zeta=e^{2\pi i/9}\) and, for arbitrary \(c=(c_0,c_1,c_2,c_3)\in\mathbb C^4\), put
\[
P_c(z)=c_0+c_1z+c_2z^2+c_3z^3,\qquad
\mathcal M_9(c)=\frac19\sum_{k=0}^{8}|P_c(\zeta^k)|^6.
\]
There is a unique positive root \(\rho\) of
\[
5\rho^5+20\rho^4+5\rho^3-30\rho-19=0,
\qquad \rho=1.15548281465957\ldots.
\]
The **sharp**, unrestricted nine-sample inequality is
\[
\boxed{\mathcal M_9(c)\le K_9^6\left(\sum_{j=0}^3|c_j|^2\right)^3},
\quad K_9^6=\frac{10\rho^6+30\rho^5+90\rho^4+60\rho^3+90\rho^2+11}{4(1+\rho^2)^3}
=9.22297799401694\ldots.
\]
All nonzero equality cases, and no others, are
\[
\boxed{c=\lambda(1,\rho\eta,\rho\eta^2,\eta^3),
\quad\lambda\in\mathbb C\setminus\{0\},\quad\eta^9=1.}
\]
Thus the complete projective equality set has **exactly nine points**. This is the first cyclic sampling order at which cubic convolution of the four consecutive frequencies acquires an alias, and it breaks the free continuous phase symmetry of the unaliased sixth-moment problem.

## Assumptions and scope

The group is precisely \(\mathbb Z/9\mathbb Z\), with normalized counting measure. The frequency set is \(\{0,1,2,3\}\) and the input normalization is coefficient \(\ell^2\) energy; no restrictions on the original complex coefficients are imposed. This result computes the sharp sixth-power norm and every extremizer at the first aliasing order. It does not compute constants for smaller cyclic orders or claim a new unaliased continuous-circle inequality.

## Proof

**1. A unique modular alias.** Expand \(P_c(z)^3=\sum_{j=0}^9 d_jz^j\), where \(d_0=c_0^3\), \(d_9=c_3^3\). Character orthogonality on the ninth roots gives the exact identity
\[
\mathcal M_9(c)=\sum_{j=0}^9|d_j|^2+2\operatorname{Re}(c_0^3\overline{c_3^3}).
\tag{1}
\]
Indeed only the degrees zero and nine collide modulo nine; all other degrees are distinct. Replacing each coefficient by its magnitude gives a termwise upper bound in the nine cyclic cubic-convolution bins, because the triangle inequality makes every bin no larger than its nonnegative-coefficient counterpart. Write the resulting magnitudes as \(a,b,c,d\ge0\).

**2. Root-mean-square reflection symmetrization.** Let \(S=a^2+b^2+c^2+d^2\), and define nonnegative aperiodic autocorrelations
\[
R_1=ab+bc+cd,\quad R_2=ac+bd,\quad R_3=ad.
\]
Coefficient extraction on the continuous circle, or direct expansion of \(\sum_{j=0}^9 d_j^2\), yields
\[
\sum_{j=0}^9d_j^2
=S^3+6S(R_1^2+R_2^2+R_3^2)+6R_1^2R_2+12R_1R_2R_3.
\tag{2}
\]
Combining (1) and (2) for real nonnegative coefficients adds exactly \(2R_3^3\) to the right side. Thus the sixth moment is coordinatewise nondecreasing in \(S,R_1,R_2,R_3\), and strictly increasing in \(R_3\) when \(S>0\).

Put
\[
A=\sqrt{\frac{a^2+d^2}{2}},\qquad B=\sqrt{\frac{b^2+c^2}{2}}.
\]
Cauchy–Schwarz and arithmetic–geometric mean give
\[
R_1=(ab+cd)+bc\le 2AB+B^2,\quad
R_2=ac+bd\le2AB,\quad R_3=ad\le A^2.
\tag{3}
\]
The reflected symmetric vector \((A,B,B,A)\) has these three upper bounds as its *exact* autocorrelations, and has the same \(S=2(A^2+B^2)\). Hence (2) together with the alias term proves that this symmetrization cannot decrease the normalized sixth moment. This is a global inequality, not an assumed shape of an optimizer.

**3. The one-variable exact extremum.** For \(A>0\), write \(t=B/A\). The positive symmetric vector has cubic-convolution coefficients, in ascending order,
\[
(1,3t,3t^2+3t,t^3+6t^2+3,3t^3+3t^2+6t,
3t^3+3t^2+6t,t^3+6t^2+3,3t^2+3t,3t,1)
\]
after factoring out \(A^3\). Identifying the two endpoint coefficients modulo nine, its normalized sixth moment is
\[
F_9(t)=\frac{10t^6+30t^5+90t^4+60t^3+90t^2+11}{4(1+t^2)^3}.
\]
Direct differentiation yields
\[
F_9'(t)=-\frac{3t(5t^5+20t^4+5t^3-30t-19)}{2(1+t^2)^4}.
\tag{4}
\]
The quintic in (4) has exactly one change of coefficient sign when written in descending powers, so by Descartes' rule of signs it has at most one positive root. It is negative at zero and positive for sufficiently large \(t\), hence has exactly one positive root \(\rho\). Thus \(F_9\) increases until \(\rho\) and decreases thereafter. The boundary values are \(F_9(0)=11/4\) and \(\lim_{t\to\infty}F_9(t)=5/2\), both smaller than \(F_9(1)=291/32\). Therefore \(\rho\) gives the unique optimal positive magnitude ratio.

**4. Equality and phase locking.** At the optimal ratio \(A,B>0\). The expression (2) plus \(2R_3^3\) is strictly increasing in each positive autocorrelation. Equality in the reflected bound forces \(ad=A^2\), whence \(a=d=A\); then equality in the second bound of (3) forces \(b=c=B\). No asymmetric magnitude optimizer exists. All four original coefficients are therefore nonzero.

In the complex coefficientwise triangle inequality, equality at the ordinary cubic coefficient of degree two forces \(\arg c_0+\arg c_2\equiv2\arg c_1\pmod{2\pi}\). Equality at degree three then forces \(\arg c_3\equiv3\arg c_1-2\arg c_0\pmod{2\pi}\). Consequently every equality phase has the affine form \(c_j=\lambda a_j\eta^j\) for \((a_0,a_1,a_2,a_3)=(1,\rho,\rho,1)\), with \(|\eta|=1\). The sole ninth-period alias requires the phases of \(c_0^3\) and \(c_3^3\) to align, equivalently \(\eta^9=1\). Conversely all nine such choices align every ninth-cyclic cubic-convolution bin and attain \(F_9(\rho)\). They are distinct modulo nonzero common scaling. This completes the proof.

## Verification

The independent standard-library `check.py` recomputes the exact cubic-convolution alias and autocorrelation identity for all \(4^4=256\) small nonnegative integer coefficient vectors, checks the rational polynomial derivative by exact integer arithmetic, locates \(\rho\) by bisection, and numerically evaluates each of the nine extremizers by direct ninth-root sampling. The stored output is `check_output.txt`. The finite tests provide reproducible consistency checks; all universal statements and uniqueness claims rest on (1)–(4) and the equality analysis.

## Relationship to prior work

The full primary result *Sharp sixth-moment Fourier norm via four-term even-moment symmetrization* solves the **continuous-circle** problem with exactly the same four frequencies. Its optimal ratio is the root of a *different* quintic, \(t^5+4t^4+t^3-6t-4=0\), and its entire projective equality set is a circle; its assumptions explicitly exclude discrete sampling grids. The present cyclic-order-nine alias adds \(2(ad)^3\), changes the quintic and the sharp norm, and forces precisely nine phases. Thus the continuous theorem supplies the symmetrization method but neither states nor implies the ninth-grid sharp constant and discrete equality classification without a new finite-torsion calculation.

The published *A universal four-mode fourth-moment constant and the sharp seven-point sampling threshold* handles the same four frequencies on finite groups, but at the **fourth**, not sixth, moment, and its period threshold is seven rather than nine. The published *Sharp sixth moments and the order-seven transition for three-character progressions* handles three, rather than four, frequencies. The 2020 primary work by Doktorski proves broad trigonometric Nikol'skii-type estimates, not this sharp finite-dimensional nine-grid algebraic constant or equality count. These comparisons are by hypotheses and logical implication rather than titles. No exhaustive priority assertion is made.

## Limitations

No formula is asserted for sampling periods below nine or for exponents other than six. The sharp norm is given by a uniquely specified algebraic root; decimals are only approximations. The existence of older unindexed tables for low-dimensional cyclic trigonometric norms has not been excluded. 

## References

1. L. R. Ya. Doktorski, *Nikol'skii–Type Inequalities for Trigonometric Polynomials for Lorentz–Zygmund Spaces*, first publicly published 2020-02-03, DOI:10.1155/2020/6853723, https://onlinelibrary.wiley.com/doi/10.1155/2020/6853723 .
2. *Sharp sixth-moment Fourier norm via four-term even-moment symmetrization*, published mathematical result (2026-10-11), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-sixth-moment-fourier-norm-via-four-term-even-moment-symmet--f3e238ebf219/RESULT.md .
3. *A universal four-mode fourth-moment constant and the sharp seven-point sampling threshold*, published mathematical result (2026-10-11), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-a-universal-four-mode-fourth-moment-constant-and-the-sharp-seven--92de3bb230cd/RESULT.md .
4. *Sharp sixth moments and the order-seven transition for three-character progressions*, published mathematical result (2026-10-11), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-sixth-moments-and-the-order-seven-transition-for-three-cha--1a8e79d7e85a/RESULT.md .
