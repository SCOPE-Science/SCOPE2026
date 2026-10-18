# Sharp fourth-moment extension determined by maximal antipodal fibers of finite-field even maps

## Finding

Let \(F=\mathbb F_q\) have characteristic at least \(5\). Let \(r\ge1\), and let \(h:F\to F^r\) be an **even** map for which \(h(-t)=h(t)\) for every \(t\), and whose origin fiber is isolated:
\[
  h^{-1}(h(0))=\{0\}.
\]
The map need not be polynomial, injective on antipodal pairs, or have equally sized fibers. Define the frequency curve
\[
  \gamma_h(t)=(t,t^3,h(t))\in F^{r+2}
\]
and, for any nontrivial additive character \(\psi\) of \(F\), the Fourier synthesis operator
\[
  T_h f(\xi)=\sum_{t\in F}f(t)\psi\bigl(\xi\cdot\gamma_h(t)\bigr).
\]
Use the **counting** input norm \(\|f\|_2^2=\sum_t|f(t)|^2\) and the **probability** output norm \(\|T_hf\|_4^4=q^{-(r+2)}\sum_{\xi\in F^{r+2}}|T_hf(\xi)|^4\). Partition \(F^\times\) into antipodal classes \(\{t,-t\}\). For \(y\in h(F^\times)\), define
\[
  B_y=\bigl\{\{t,-t\}:h(t)=y\bigr\},\qquad n_y=|B_y|,\qquad M=\max_y n_y.
\]
Then the **sharp fourth power** of the Fourier extension norm is
\[
 \boxed{\|T_h\|_{\ell^2\to L^4}^{4}=\begin{cases}
    2-\dfrac1q,& M=1,\\
    3-\dfrac{3}{2M},&M\ge2.
 \end{cases}}
\]
Every equality case is determined. For \(M=1\), the nonzero maximizers are **exactly** those \(f\) with constant positive magnitude at **all** \(q\) inputs, with arbitrary phases. For \(M\ge2\), all nonzero maximizers are **exactly** the functions supported on one full fiber \(h^{-1}(y)\subset F^\times\) of maximal size \(2M\), with common positive magnitude at its \(2M\) points, and whose \(M\) pair products \(f(t)f(-t)\) are equal complex numbers. In this regime \(f(0)=0\), and all such functions attain the bound.

**Arithmetic monomial consequence.** For every integer \(m\ge1\), choose \(h(t)=t^{2m}\). Set \(d=\gcd(m,(q-1)/2)\). Then \(M=d\), and the norm is \(2-1/q\) when \(d=1\), and \(3-3/(2d)\) when \(d\ge2\). The second case has complete maximizing supports \(a\mu_{2d}\) (multiplicative cosets of the \(2d\)-th roots of unity) and the pair-product condition above. The values \(d\ge3\) give sharp resonance levels not visible in the quartic case \(m=2\); e.g. \(q=7,m=3\) gives \(5/2\), and \(q=17,m=4\) gives \(21/8\).

## Assumptions and scope

The characteristic restriction ensures \(2\) and \(3\) are nonzero in the field and antipodal pairs are distinct. Field order \(q\) may be a non-prime prime power. Every output coordinate ranges uniformly over the full dual affine space \(F^{r+2}\). The displayed norm is the fourth power of the operator norm, not the operator norm itself; the corresponding operator norm is its positive fourth root. The map \(h\) is allowed to take the same value on many distinct antipodal pairs; the origin-fiber hypothesis explicitly excludes \(h(t)=h(0)\) for nonzero \(t\). No assertion is made without this hypothesis. The normalization remains fixed throughout.

## Proof

**(1) Resolve every pair-sum collision.** Character orthogonality gives the exact fourth moment
\[
 Q(f)=\|T_hf\|_4^4=
 \sum_{u\in F^{r+2}}\left|\sum_{\gamma_h(a)+\gamma_h(b)=u}f(a)f(b)\right|^2.
\]
If \(a+b=c+d=s\ne0\) and \(a^3+b^3=c^3+d^3\), then the identity \(a^3+b^3=s^3-3sab\) forces \(ab=cd\). Therefore the two unordered pairs coincide as the roots of \(X^2-sX+ab\); the final \(h\)-coordinates add no new collisions. If \(s=0\), the pairs are \((t,-t)\) and their odd cubic coordinates vanish. Their even-map sums are \(2h(t)\); equality holds precisely when \(h(t)=h(u)\). By isolatedness of the origin fiber, the diagonal pair \((0,0)\) cannot collide with nonzero antipodal pairs. Thus the **only** exceptional additive fibers are the distinct antipodal pair classes sharing a nonzero value of \(h\).

**(2) Exact quartic identity.** Write \(S=\sum_t|f(t)|^2\), and choose one representative \(t\) for each unordered pair in \(B_y\). Let \(z_t=f(t)f(-t)\). The trivial unordered-pair coincidences contribute \(2S^2-\sum_t|f(t)|^4\). Two *distinct* antipodal unordered pairs in the same \(B_y\) produce four orderings per cross-convolution direction, so the exact identity is
\[
 \boxed{Q(f)=2S^2-\sum_t|f(t)|^4
 +4\sum_y\left(\left|\sum_{\{t,-t\}\in B_y}z_t\right|^2
  -\sum_{\{t,-t\}\in B_y}|z_t|^2\right).}
\]
The identity holds for all complex inputs, including zero coefficients and singleton blocks. Each exceptional collision occurs **exactly once** in the added correction.

**(3) A sharp single-block bound.** For one block of size \(n\), denote the squared magnitudes of a pair by \(x_i,y_i\ge0\), its total squared mass by \(s_i=x_i+y_i\), and its product magnitude by \(u_i=\sqrt{x_iy_i}\). Put \(W=\sum_i s_i\). The portion of the quartic expression after \(2S^2\) attributable to this block is bounded, by phase alignment, by
\[
 -\sum_i(x_i^2+y_i^2)+4\bigl((\sum_i u_i)^2-\sum_i u_i^2\bigr)
 =-\sum_i s_i^2-2\sum_i u_i^2+4(\sum_i u_i)^2.
\]
At fixed \(s_i\), \(0\le u_i\le s_i/2\). The right-hand side is nondecreasing in each \(u_i\), since its partial derivative is \(8\sum_j u_j-4u_i\ge0\). It is therefore maximized at \(u_i=s_i/2\), i.e. equal magnitudes within each pair. At that endpoint it equals \(W^2-\tfrac32\sum_i s_i^2\), which Cauchy–Schwarz bounds by
\[
 \boxed{\left(1-\frac3{2n}\right)W^2.}
\]
For \(n\ge2\) and \(W>0\), equality forces \(s_1=\cdots=s_n=W/n\), hence equal nonzero magnitudes on all \(2n\) points, and all pair products have a common argument. These conditions are sufficient. For singleton blocks the exact special-case contribution is simply \(-x_1^2-y_1^2\le-W^2/2\).

**(4) Global maximization.** If \(M=1\), there are no exceptional distinct-pair collisions; consequently \(Q(f)=2S^2-\sum_t|f(t)|^4\le(2-1/q)S^2\). Cauchy–Schwarz is sharp only for constant magnitudes on the complete field, and phases are unrestricted.

Suppose \(M\ge2\), and write \(\alpha=|f(0)|^2\), \(W_y=\sum_{t\in h^{-1}(y)}|f(t)|^2\). The coefficient \(1-3/(2n)\) increases with \(n\). The block bound gives
\[
 \begin{aligned}
 Q(f)&\le2S^2-\alpha^2+\sum_y\left(1-\frac3{2n_y}\right)W_y^2\\
 &\le2S^2-\alpha^2+\left(1-\frac3{2M}\right)\sum_y W_y^2\\
 &\le2S^2-\alpha^2+\left(1-\frac3{2M}\right)(S-\alpha)^2\\
 &\le\left(3-\frac3{2M}\right)S^2.
 \end{aligned}
\]
The positivity of \(1-3/(2M)\) is used in the third inequality. For \(S>0\), equality in the last step requires \(\alpha=0\); in the preceding strict convex mass inequality it requires only **one** nonzero \(W_y\); and in the first two steps it requires \(n_y=M\), equal point magnitudes and aligned pair products. Conversely, a maximally sized nonzero fiber with these exact coefficients attains equality. This proves both the norm and the complete equality classification.

**(5) Monomial fiber count.** The cyclic multiplicative group \(F^\times\) has order \(q-1\). Every nonzero fiber of the power map \(t\mapsto t^{2m}\) is a coset of its kernel, which has size \(\gcd(2m,q-1)=2\gcd(m,(q-1)/2)\). Modding out by sign leaves exactly \(d\) antipodal pairs in each nonzero fiber. The fiber above zero is \(\{0\}\), verifying the general hypotheses and the stated arithmetic formula.

## Verification

Run `python3 artifacts/verify.py` from this package. The script constructs the finite pair-sum fibers with exact finite-field arithmetic, compares the direct exact convolution fourth moment against the proved block identity on seeded Gaussian-integer inputs, and independently checks attainment and a strict phase-perturbation loss in the resonant cases. Cases include prime fields and explicit quadratic extensions, monomial exponents \(2m\) for several \(m\), and artificially specified even maps with unequal fiber sizes. The supplied `artifacts/verify_output.txt` records the actual result. These are finite checks; the arbitrary-field theorem follows from steps (1)–(5), not from exhaustive finite computation.

## Relationship to prior work

Sharp finite-field restriction and extension have been studied for parabolas, paraboloids, hyperbolic paraboloids and cones by González-Riquelme and Oliveira e Silva [1]. Their explicit surface results do not establish this arbitrary-even-fiber curve theorem. Earlier Mockenhaupt–Tao finite-field restriction theory [2] supplies the character-orthogonality framework. The previously published lacunary-curve calculation [3] proves the \(h(t)=t^4\) **special case**, and the sharp planar cubic-graph result [4] treats the opposite extreme in which all antipodal pairs collide with the origin, which **does not satisfy** the origin-isolation assumption here. The present statement supplies a new arbitrary even-map invariant, unequal fiber sizes, all possible higher resonance levels and all extremizers, rather than merely restating the quartic special case. The full-result comparisons are specific to these mathematical statements and do not certify absence of equivalent older formulations.

## Limitations

No assertion is made in characteristics two or three, for maps lacking the isolated-origin condition, or for other even moments such as the sixth moment. The norm depends on the *largest* antipodal fiber, but this fact does not imply stability under perturbations of the curve or bounds for noisy measurements. Finite verifier examples cannot establish all-field correctness or bibliographic priority. Some older additive-combinatorial work may state an equivalent universal fiber bound under different terminology; this remains a genuine residual originality risk. No independent mathematical audit has been performed.

## References

[1] C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, first publicly submitted 26 May 2024, https://arxiv.org/abs/2405.16647.

[2] G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, https://arxiv.org/abs/math/0204234.

[3] *Arithmetic resonance and sparse sharp extremizers on a lacunary finite-field curve*, publicly available mathematical result (specific quartic case), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-arithmetic-resonance-and-sparse-sharp-extremizers-on-a-lacunary--0c95b0b9fd4f.

[4] *Sharp cubic-graph Fourier extension and its inflection-point deficit*, publicly available mathematical result (cubic case), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-cubic-graph-fourier-extension-and-its-inflection-point-def--5a2b58c43575.
