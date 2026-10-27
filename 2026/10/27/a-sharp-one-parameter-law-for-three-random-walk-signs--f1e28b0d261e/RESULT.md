# A sharp one-parameter law for three random-walk signs

## Finding

Let \(Y_1,Y_2,Y_3\) be independent identically distributed, non-atomic and symmetric real increments, with \(T_j=Y_1+\cdots+Y_j\). Write \(A_j=|Y_j|\), and define the **dominant-jump probability**
\[
t=\mathbb P\{A_1>A_2+A_3\}.
\]
The complete law of the three signs \((\operatorname{sgn}T_1,\operatorname{sgn}T_2,\operatorname{sgn}T_3)\) is determined by this single parameter:

| Sign word | Exact probability |
|---|---|
| `+++`, `---` | \(5/16\) each |
| `++-`, `--+` | \(1/16\) each |
| `+-+`, `-+-` | \(1/16-t/8\) each |
| `+--`, `-++` | \(1/16+t/8\) each |

The **exact feasible range** is \(0\le t<1/3\). Every parameter in that half-open interval is realized by a symmetric absolutely continuous increment law. Thus the table is a sharp one-parameter classification, not a fixed-law identity.

For the ascent-descent walk of a uniform permutation on seven symbols, the signs at times \(1,3,5\) correspond to symmetric triangular increments, for which \(t=19/90\). Their joint word probabilities, in the order `+++`, `++-`, `+-+`, `+--`, `-++`, `-+-`, `--+`, `---`, are
\[
(225,45,26,64,64,26,45,225)/720.
\]
For an ordinary simple symmetric walk sampled at times \(1,3,5\), the probabilities in the same order are
\[
(10,2,1,3,3,1,2,10)/32.
\]
The total variation distance between these eight-point laws is exactly \(7/720\), even though both yield the same occupation-count vector \((5,3,3,5)/16\) for the number of positive signs.

## Assumptions and scope

The increments are real, independent, identically distributed, symmetric about zero and atomless; no moments are assumed. Consequently their nonzero signs are independent fair signs, independent of their iid strictly positive magnitudes. All three partial sums are nonzero almost surely. The sign words in the table refer to strict positivity/negativity. The application uses a uniform permutation, and ordinary simple symmetric random-walk steps are independent fair \(\pm1\) steps. The classification is at exactly three observation times; no full-process identity or universality at longer horizons is asserted.

## Proof

**One-parameter table.** Write \(Y_i=\varepsilon_i A_i\), where the \(\varepsilon_i\) are independent fair signs, independent of iid positive magnitudes \(A_i\). Let \(t=\mathbb P(A_1>A_2+A_3)\). By exchangeability, the same probability applies with any one of the three magnitudes distinguished. Continuous distributions eliminate equality ties.

The event that all three partial sums are positive can arise from four sign configurations of the increments. The corresponding magnitude conditions have respective probabilities \(1\), \(1-t\), \(1/2\), and \(t\). Thus
\[
\mathbb P(+++)={1+(1-t)+1/2+t\over8}=5/16.
\]
Also \(\mathbb P(T_1>0,T_2>0)=1/4+(1/8)=3/8\), because the `+-` increment case requires \(A_1>A_2\). Subtracting \(\mathbb P(+++)\) gives \(\mathbb P(++-)=1/16\).

For the alternating word `+-+`, the increment signs must be `+-+`, and the magnitude conditions are \(A_2>A_1\) and \(A_1+A_3>A_2\). Hence
\[
\mathbb P(+-+)={1/2-t\over8}=1/16-t/8.
\]
For `-++`, the first two increment signs are `-+` and \(A_2>A_1\). The third may be positive unconditionally, or negative if \(A_2>A_1+A_3\); thus
\[
\mathbb P(-++)={1/2+t\over8}=1/16+t/8.
\]
Global sign reversal supplies the remaining four words. This proves the exact table without a moment, a limit theorem, or numerical approximation.

**Sharp feasible range.** Since the events that each of three positive magnitudes exceeds the sum of the other two are mutually exclusive, \(3t\le1\). In fact \(3t<1\): some interval \((a,b)\) with \(0<a<b<2a\) has positive \(A\)-probability; when all three iid magnitudes lie there, none dominates. At the other end, any atomless law supported on a positive interval \((a,b)\) with \(b<2a\) has \(t=0\).

For attainability of every intermediate value, take \(A=e^{LZ}\) with \(Z\) uniform on \((0,1)\) and an independent fair sign, where \(L>0\). For \(L\le\log2\), the largest possible magnitude is smaller than the sum of the other two, so \(t(L)=0\). The map \(L\mapsto t(L)\) is continuous by dominated convergence and the zero probability of tie surfaces. As \(L\to\infty\), the gap between the largest and second-largest of three independent \(Z\)'s, multiplied by \(L\), exceeds \(\log2\) with probability tending to one. The largest magnitude then exceeds twice the second largest and so exceeds the sum of both smaller magnitudes. Consequently \(3t(L)\to1\). The intermediate-value theorem realizes each \(t\in[0,1/3)\) with an atomless symmetric density.

**Permutation application.** Let \(U_1,\ldots,U_7\) be iid uniform on \((0,1)\). Their relative ranks form a uniform permutation. Define the ascent-descent walk \(S_k=\sum_{j=1}^k(1-2\mathbf 1\{U_j>U_{j+1}\})\). Set \(V_1=U_1\) and \(V_j=\{U_j-U_{j-1}\}\) for \(j\ge2\), with braces denoting fractional part. The torus-coordinate change is triangular with determinant one, hence \(V_1,\ldots,V_7\) are iid uniform. Counting integral carries gives
\[
S_k=k-2\left\lfloor\sum_{i=1}^{k+1}V_i\right\rfloor.
\]
For \(r=1,2,3\), the odd integer \(S_{2r-1}\) is positive exactly when \(\sum_{i=1}^{2r}V_i<r\). Therefore its sign is the sign of the partial sum \(T_r=\sum_{j=1}^{r}Y_j\), where \(Y_j=1-V_{2j-1}-V_{2j}\) are iid with triangular density \(f_Y(y)=1-|y|\) for \(|y|<1\).

The magnitude \(A=|Y|\) has density \(2(1-a)\) on \((0,1)\). Conditioning on the other two magnitudes and integrating the tail \(\mathbb P(A>x)=(1-x)^2\) gives
\[
\begin{aligned}
t&=4\int_{b,c\ge0;\,b+c<1}(1-b)(1-c)(1-b-c)^2\,dc\,db\\
 &=4\left({1\over3}\int_0^1b(1-b)^4\,db+{1\over4}\int_0^1(1-b)^5\,db\right)\\
 &=4\left({1\over90}+{1\over24}\right)=19/90.
\end{aligned}
\]
Substitution in the universal word table gives the claimed rational probabilities. A five-step simple symmetric walk has the displayed \(32\)-path word table by direct finite enumeration. Exactly four entries differ, each by \(7/1440\); hence the total variation distance is \(7/720\). Summing words according to their number of positive signs yields the identical occupation-count laws \((5,3,3,5)/16\).

## Verification

The included standalone script `verify_three_signs.py` uses only standard-library exact rational arithmetic. It verifies the evaluated dominance integral, the full eight-word table against exhaustive enumeration of all \(6!=720\) relative orders relevant to the permutation sign triple, the comparison with all \(2^5=32\) simple-walk prefixes, the exact total variation distance, and normalization/feasibility for six rational parameter choices. On the packaged script the actual output was:

`PASS: triangular dominance 19/90; 720 permutation cases; 32 walk cases; TV 7/720; 6 family checks`

The universal table and sharp feasible continuum rely on the analytic argument above, not on these finite checks.

## Relationship to prior work

Tang's 2026 permutation occupation-time theorem (arXiv:2609.25102v1) identifies an iid symmetric triangular-increment representation and proves a discrete arcsine **marginal** for the number of positive odd-time positions. That representation implies the particular permutation sign law once its joint probabilities are computed, so the triangular numerical specialization is not asserted as independently novel. The contribution here is instead the **complete, sharp feasible family of all three-time sign-word laws for arbitrary atomless symmetric iid increments**, identifying the unique nonuniversal parameter and its entire attainable range; this classification is neither the marginal arcsine theorem nor its immediate special case.

Fang and collaborators' 2021 paper, first available as arXiv:2001.08857, studies permutation-generated occupation statistics and an even-horizon discrete-arcsine conjecture, without stating the present sharp three-word classification. Classical Sparre Andersen persistence gives only certain aggregate sign probabilities. The related published four-step limited-independence persistence result concerns dependent signs and a different fourth-order interaction, rather than iid magnitudes and three partial sums.

## Limitations

The classification is confined to three partial-sum signs, and it does not classify arbitrary longer sign words. The permutation example is a consequence of the previously known coordinate representation and is included to demonstrate a concrete failure of pathwise universality, not as a separate novelty claim. A broader classical sign-combinatorics formulation may already encode the three-word table under other terminology; one historical work on signs of symmetrically distributed sums was identifiable only at abstract level and remains a literature-priority risk. No independent scientific audit has been performed.

## References

- W. Tang, arXiv:2609.25102v1, first submitted 2026-09-20, on the discrete arcsine occupation law for a permutation-generated walk; mathematical proof inspected at https://arxiv.org/abs/2609.25102 .
- X. Fang, H. L. Gan, S. Holmes, H. Huang, E. Peköz, A. Röllin, and W. Tang, *Arcsine laws for random walks generated from random permutations with applications to genomics*, Journal of Applied Probability 58 (2021), 851–867; open preprint arXiv:2001.08857, initially posted 2020-01-24.
- E. Sparre Andersen, *On sums of symmetrically dependent random variables*, Scandinavian Actuarial Journal (1953), pp. 123–138; general historical context, abstract inspected only.
