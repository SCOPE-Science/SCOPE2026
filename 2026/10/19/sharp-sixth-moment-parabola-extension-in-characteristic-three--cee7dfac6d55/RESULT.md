# Sharp sixth-moment parabola extension in characteristic three

## Finding

For each integer \(n\ge1\), let \(q=3^n\) and fix any nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C\). Define the normalized parabolic extension map
\[
\mathcal E_q f(X,Y)=\frac1q\sum_{t\in\mathbb F_q}f(t)\psi(Xt+Yt^2),\qquad (X,Y)\in\mathbb F_q^2.
\]
For every complex-valued function \(f:\mathbb F_q\to\mathbb C\),
\[
\boxed{\ \sum_{X,Y\in\mathbb F_q}|\mathcal E_qf(X,Y)|^6
\le \left(1+\frac1q-\frac1{q^2}\right)
\left(\frac1q\sum_{t\in\mathbb F_q}|f(t)|^2\right)^3.\ }
\]
The coefficient is **sharp**, attained by each nonzero constant function and, more generally, by nonzero scalar multiples of every quadratic additive character \(t\mapsto\psi(At+Bt^2)\), for \(A,B\in\mathbb F_q\). Every nonzero maximizer has constant modulus. No complete characterization of its possible phases is asserted.

## Assumptions and scope

The field \(\mathbb F_q\) has characteristic exactly three, including every extension degree \(n\ge1\). Fourier-side sums are with **counting measure**; the coefficient-side squared norm is \(q^{-1}\sum|f|^2\). No special choice of nontrivial character is required. The zero input trivially gives equality, while the modulus statement concerns nonzero inputs. The proof is uniform in the field size, and no upper bound on \(n\) is imposed.

For shorthand set \(F=\sum_t|f(t)|^2\) and, for \((s,u)\in\mathbb F_q^2\),
\[
T(s,u)=\sum_{\substack{a+b+c=s\\ a^2+b^2+c^2=u}}f(a)f(b)f(c),
\qquad M=\sum_{s,u}|T(s,u)|^2.
\]
Character orthogonality yields \(\sum_{X,Y}|\mathcal E_qf(X,Y)|^6=q^{-4}M\), so the displayed inequality is equivalent to
\[
M\le\left(q+1-\frac1q\right)F^3.
\]

## Proof

**1. The generic fibers have constant cardinality.** Consider an ordered triple \((a,b,c)\) whose sum \(s=a+b+c\) is nonzero. Simultaneously translating its three entries by \(h\in\mathbb F_q\) preserves their sum in characteristic three, while its quadratic sum changes by \(2hs+3h^2=-hs\). Thus, as \(h\) ranges over the field, its quadratic sum traverses every value exactly once. For each fixed \(s\), the number of ordered triples summing to \(s\) is \(q^2\); these form \(q\) translation orbits, each with exactly one triple in every fiber \((s,u)\). Hence every fiber with \(s\ne0\) contains exactly \(q\) triples. Cauchy--Schwarz implies
\[
\sum_{s\ne0,u}|T(s,u)|^2
\le q\sum_{\substack{a,b,c\\a+b+c\ne0}}|f(a)f(b)f(c)|^2.
\]

**2. The exceptional fibers are arithmetic progressions.** Every triple summing to zero is uniquely of the form \((a-d,a,a+d)\), because the midpoint of its first and third entries is its second entry: in characteristic three, \((a-d)+a+(a+d)=0\). The associated quadratic sum is \(-d^2\). Put
\[
C_d=\sum_a f(a-d)f(a)f(a+d),\qquad
S_d=\sum_a|f(a-d)f(a)f(a+d)|^2.
\]
The map \(d\mapsto-d^2\) has one preimage at zero, two preimages at every nonzero negative square, and no preimages elsewhere. Moreover, \(C_{-d}=C_d\). Consequently,
\[
\sum_u|T(0,u)|^2=|C_0|^2+2\sum_{d\ne0}|C_d|^2,
\quad\sum_{a+b+c=0}|f(a)f(b)f(c)|^2=\sum_dS_d.
\]
Combining these identities with the generic-fiber estimate gives
\[
M\le q\left(F^3-\sum_dS_d\right)+|C_0|^2+2\sum_{d\ne0}|C_d|^2.
\]
Every \(C_d\) is a sum of \(q\) terms, so \(|C_d|^2\le qS_d\). Apply this bound to \(C_0\) and to one copy of each \(C_d\) with \(d\ne0\):
\[
\boxed{\ M\le qF^3+\sum_{d\ne0}|C_d|^2.\ }
\]

**3. A sharp correlation estimate.** For each \(d\ne0\), Cauchy--Schwarz with the central factor \(f(a)\) yields
\[
|C_d|^2\le F\sum_a|f(a-d)|^2|f(a+d)|^2.
\]
The map \((a,d)\mapsto(a-d,a+d)\) is a bijection from the pairs with \(d\ne0\) onto all ordered pairs of *distinct* field elements: its determinant is \(2=-1\ne0\). It follows that
\[
\sum_{d\ne0}|C_d|^2\le
F\sum_{x\ne y}|f(x)|^2|f(y)|^2
=F\left(F^2-\sum_t|f(t)|^4\right).
\]
Since \(\sum_t|f(t)|^4\ge F^2/q\) by Cauchy--Schwarz,
\[
M\le qF^3+F^3-F\sum_t|f(t)|^4
\le\left(q+1-\frac1q\right)F^3.
\]
Character orthogonality and the precise measure normalization in the assumptions complete the asserted inequality. If a nonzero function saturates it, then equality holds in the final Cauchy--Schwarz inequality, forcing \(|f(t)|\) to be independent of \(t\).

**4. Sharpness and explicit equality examples.** For \(f\equiv1\), every fiber with \(s\ne0\) has value \(q\). The exceptional fibers have values \(q\) at \((0,0)\), \(2q\) at the \((q-1)/2\) points \((0,u)\) for which \(-u\) is a nonzero square, and zero elsewhere. Hence
\[
M(\mathbf1)=q(q-1)q^2+q^2+\frac{q-1}{2}(2q)^2=q^4+q^3-q^2,
\]
so \(M(\mathbf1)/(qF^3)=1+q^{-1}-q^{-2}\) exactly. For a quadratic additive character, the product \(f(a)f(b)f(c)\) is constant on each fiber because it depends only on \(a+b+c\) and \(a^2+b^2+c^2\). Such characters therefore have the same sixth moment and norm as the constant input (up to scalar), proving the final assertion.

## Verification

Run the bundled standard-library-only script `python verify.py` in the same directory. It builds the fields \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\) by explicit polynomial quotients; exhaustively enumerates all triple fibers; checks the exact constant moment and four successive inequalities on sixty nonconstant complex inputs in each field; and verifies two exact equality witnesses per field. The checked output is in `verify_output.txt`. These finitely many tests support reproducibility but **are not** a substitute for the proof over arbitrary \(3\)-power fields.

## Relationship to prior work

González-Riquelme and Oliveira e Silva [1, Theorem 1.3] prove the same sharp coefficient and constant-modulus necessity for the parabola under the explicit assumption that the characteristic exceeds three. Their §6 analyzes the cases \(q\equiv1,2\pmod3\); the characteristic-three branch of the triple convolution is different and is **outside** that theorem. The present proof closes precisely this excluded characteristic, using its special translation-invariant triple sums and arithmetic-progressions-on-the-zero-sum-fiber structure.

Previously established localized results [2, 3] do not imply the claim for all \(q=3^n\): [2] gives only the local second variation at constants, explicitly withholding any global inequality; [3] gives a sharp three-frequency bound and the global case \(q=3\), while expressly not treating unrestricted functions for \(q>3\). The new all-input statement for \(q\ge9\) is stronger in a different direction than either. The 2025 moment-curve endpoint paper [4] concerns the degree-dependent exponent, which for the planar degree-two curve is \(L^2\)-to-\(L^4\), not the sixth moment treated here.

## Limitations

The result is restricted to characteristic three. It proves the sharp operator norm and the necessary constant-modulus property of nonzero extremizers, but does not classify all their phases or give quantitative stability. The fact that the bound matches the coefficient in [1] for other characteristics does not by itself prove a universal proof covering arbitrary prime-power characteristics; the argument here depends essentially on \(3=0\). Searches of identified prior results and primary sources support novelty, but cannot exclude every unindexed or unpublished equivalent inequality. Independent audit remains outstanding.

## References

1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, first public version dated 2024-05-26, Theorem 1.3 and §6, https://arxiv.org/html/2405.16647v2.
2. *Exact local sixth-moment stability of the parabola in characteristic three*, publicly indexed result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-local-sixth-moment-stability-of-the-parabola-in-characteri--158763dab4f3/RESULT.md.
3. *Sharp sixth Fourier moments for three parabolic modes in every odd characteristic*, publicly indexed result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-sixth-fourier-moments-for-three-parabolic-modes-in-every-o--52302cf3414e/RESULT.md.
4. C. Biswas, E. Carneiro, T. C. Flock, D. Oliveira e Silva, B. Stovall, and J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields*, arXiv:2508.08377v1, https://arxiv.org/abs/2508.08377.
