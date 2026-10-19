# A sharp dimension-nine MUB support law and an equal-probability balanced state

## Finding
Let \(K=\mathbb F_3[\iota]\), where \(\iota^2=-1\), and let \(\zeta=e^{2\pi i/3}\). For the standard set of ten mutually unbiased bases of \(\mathbb C^9\), consisting of the coordinate basis \(\mathcal B_\infty\) and, for every \(a\in K\), the basis
\[
\mathcal B_a=\bigl\{\phi_{a,b}:b\in K\bigr\},\qquad
\phi_{a,b}(x)=\frac13\zeta^{\operatorname{Tr}(ax^2+bx)},\quad x\in K,
\]
where \(\operatorname{Tr}(t)=t+t^3\in\mathbb F_3\), the **exact minimum total coordinate support** is
\[
\min_{0\ne f\in\mathbb C^K}\sum_{a\in K\cup\{\infty\}}\bigl|\operatorname{supp}_{\mathcal B_a}f\bigr|=50.
\]
An explicit normalized minimizer is
\[
\psi=\frac1{\sqrt5}\bigl(e_0-e_1-e_{-1}-e_{\iota}-e_{-\iota}\bigr).
\]
In **each** of the ten bases, \(\psi\) has exactly four zero coefficients and five nonzero coefficients of common squared modulus \(1/5\). Thus it is a MUB-balanced state in dimension \(9\equiv1\pmod4\), as well as a support minimizer. The conclusion concerns the displayed standard complete set; it does not classify other complete sets or all minimizers.

## Assumptions and scope
The finite field \(K=\mathbb F_3[\iota]\) is obtained from the irreducible polynomial \(X^2+1\) over \(\mathbb F_3\). Coordinates are indexed by its nine elements, with the usual Hermitian inner product on \(\mathbb C^K\). The symbol \(e_x\) denotes a coordinate vector. Support counts complex amplitudes that are exactly nonzero, not values above a numerical threshold. The standard ten bases are those defined above; all bases are normalized and mutually unbiased. No assumption is imposed on the competing nonzero state.

## Proof
**1. The displayed system is a complete set of mutually unbiased bases.** For fixed \(a\), orthogonality follows from orthogonality of the additive characters \(x\mapsto\zeta^{\operatorname{Tr}(bx)}\). For distinct \(a,a'\), the squared absolute value of the transition sum
\[
G=\sum_{x\in K}\zeta^{\operatorname{Tr}((a-a')x^2+(b-b')x)}
\]
is \(9\): expand \(|G|^2\), substitute \(x=y+h\), and sum first over \(y\); the inner character sum vanishes unless \(h=0\), since \(2(a-a')\ne0\). Hence every cross-basis inner-product magnitude is \(1/3\).

**2. Universal lower bound.** Write \(P_{j,b}=|\phi_{j,b}\rangle\langle\phi_{j,b}|\) for the rank-one projections of any complete set \(\{\mathcal B_j\}_{j=1}^{10}\) of mutually unbiased bases in \(\mathbb C^9\), interpreting the coordinate basis similarly. For a normalized state \(f\), put \(\rho=|f\rangle\langle f|\) and \(p_{j,b}=\operatorname{Tr}(\rho P_{j,b})\). The nine-dimensional diagonal Hermitian operator space has an eight-dimensional traceless part \(D_j\); mutual unbiasedness makes the ten \(D_j\) pairwise orthogonal in Hilbert--Schmidt inner product. Their dimension sum is \(10\cdot8=80=9^2-1\), so together they exhaust the traceless Hermitian matrices. Orthogonally decomposing \(\rho-I/9\) gives
\[
\sum_{j=1}^{10}\sum_{b=1}^{9}\left(p_{j,b}-\frac19\right)^2
=\operatorname{Tr}\left(\rho-\frac I9\right)^2=\frac89,
\]
and therefore the complete-MUB second-moment identity
\[
\sum_{j,b}p_{j,b}^2=2.
\]
If \(s_j\) probabilities in basis \(j\) are nonzero, Cauchy--Schwarz and \(\sum_b p_{j,b}=1\) imply \(\sum_b p_{j,b}^2\ge1/s_j\). Applying Cauchy--Schwarz once more across the ten bases yields
\[
2\ge\sum_{j=1}^{10}\frac1{s_j}\ge\frac{100}{\sum_{j=1}^{10}s_j},
\]
so the total support cannot be smaller than \(50\). Equality requires five identical nonzero probabilities in every basis.

**3. The five-point state realizes equality.** The coordinate basis plainly has support five and every nonzero coordinate has squared modulus \(1/5\). For \(a,b\in K\) let
\[
T(a,b)=\sum_{x\in K}\sqrt5\,\psi(x)\,\zeta^{\operatorname{Tr}(ax^2+bx)}.
\]
Because \(\psi\) is real, \(\langle\phi_{a,b},\psi\rangle=\overline{T(a,b)}/(3\sqrt5)\). Define \(A=\operatorname{Tr}(a)\), \(U=\operatorname{Tr}(b)\), \(V=\operatorname{Tr}(\iota b)\), and \(H(0)=2\), \(H(1)=H(-1)=-1\). Since \((\pm1)^2=1\) and \((\pm\iota)^2=-1\), the sum is exactly
\[
T(a,b)=1-\zeta^A H(U)-\zeta^{-A}H(V).
\]
The map \(b=u+v\iota\mapsto(U,V)=(2u,-2v)\) is bijective on \(\mathbb F_3^2\). Consequently, for each fixed \(a\), the pair \((U,V)\) ranges once over all nine pairs.

When \(A=0\), this reduces to \(T=1-H(U)-H(V)\), which vanishes if and only if exactly one of \(U,V\) is zero. There are four such pairs. For the remaining five pairs, \(T\) equals \(3\) or \(-3\). When \(A\ne0\), \(\zeta^A+\zeta^{-A}=-1\) and the formula vanishes if and only if both \(U,V\) are nonzero. Again there are four such pairs, and in the remaining five cases \(T\in\{3,-3\zeta^A,-3\zeta^{-A}\}\). Thus in every finite basis there are four zeros and five coefficients of squared magnitude \(9/(9\cdot5)=1/5\). Summing ten support sizes of five gives \(50\), matching the lower bound. This proves the theorem and the equal-probability MUB-balanced property.

## Verification
The accompanying `verify_mub9.py` computes all \(9\times9=81\) quadratic-phase sums exactly in the integral basis \(1,\zeta\) of \(\mathbb Z[\zeta]\), with \(\zeta^2=-1-\zeta\). It checks that for each of the nine finite bases the squared integral norm of the phase sum has multiset \(\{0\text{ (four times)},9\text{ (five times)}\}\), and verifies the coordinate support and total \(50\). Its integer arithmetic is exact; the analytic argument above proves the universal lower bound independently of enumeration.

## Relationship to prior work
Fiorentino--Weigert [2] established complete-MUB support uncertainty bounds in **prime** dimensions and studied the cases through seven. Li [1] sharpened their problem to an exact theorem \(p^2-p+2\) and extremizer classification for prime \(p\ge5\); it does not cover the odd composite prime power \(9\). The lower bound \(50\) here follows from the previously known complete-MUB second-moment identity and is **not** itself claimed as new. The added content is an explicit state proving saturation at dimension nine and the exact five-equal-probabilities-per-basis conclusion. Amburg--Sharma--Sussman--Wootters [3] and Appleby--Bengtsson--Dang [4] constructed balanced states in odd prime powers congruent to three modulo four; [3] explicitly noted the existence question for dimensions congruent to one modulo four. The state here lies in that latter regime. No classification of balanced states is asserted.

## Limitations
The result is for the displayed standard ten bases over \(\mathbb F_9\). The universal second-moment argument is valid for every complete MUB set in dimension nine but does not prove every such set has a saturating state. There is no classification or count of all minimizers. The exact checker independently checks finite identities but does not replace the analytic proof of the lower bound. Earlier or differently named constructions of the same balanced state may exist, and historical priority cannot be conclusively established by database searches.

## References
1. Dongwei Li, Sharp Total-Support Uncertainty for the Standard Complete Set of Mutually Unbiased Bases, arXiv:2609.16030v2 (2026), first posted 2026-09-11, especially Sections 1 and 4.
2. Vincenzo Fiorentino and Stefan Weigert, Uncertainty relations for the support of quantum states, arXiv:2209.09817v2 (2023), Sections 2--5.
3. Ilya Amburg, Roshan Sharma, Daniel Sussman and William K. Wootters, States that look the same with respect to every basis in a mutually unbiased set, arXiv:1407.4074v3 (2015), Introduction.
4. D. M. Appleby, Ingemar Bengtsson and Hoan Bui Dang, Galois Unitaries, Mutually Unbiased Bases, and MUB-balanced states, arXiv:1409.7987v2 (2014), Sections 1, 9--12.
