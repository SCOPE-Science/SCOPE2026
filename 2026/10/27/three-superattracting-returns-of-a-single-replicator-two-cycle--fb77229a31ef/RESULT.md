# Three superattracting returns of a single replicator two-cycle

## Finding

**Theorem (fixed-equilibrium reentrance of superattraction).** Consider the interval map
\[
f_{a,b}(x)=\frac{x}{x+(1-x)\exp(a(x-b))},\qquad 0\le x\le1,
\]
with intensity \(a>0\) and equilibrium parameter \(b\in(0,1)\). At the rational equilibrium \(b=12/25\), the **unique** nontrivial period-two orbit, followed continuously as \(a\) increases beyond its birth threshold \(a_0=625/78\), is superattracting at **at least three distinct finite values** of \(a\). There is also a nonempty open interval \(I\subset(0,1/2)\) containing \(12/25\) for which the same assertion holds for every \(b\in I\), with threshold \(a_0(b)=2/[b(1-b)]\).

The multiplier of that single orbit alternates in sign in the order positive, negative, positive, negative at four successively increasing intensities. In particular, its signed multiplier is not monotone in selection intensity, even though the period-two branch itself is unique. Each of the three zero-multiplier parameters supports a locally attracting, in fact superattracting, prime two-cycle. **No assertion that there are exactly three zeroes is made.**

## Assumptions and scope

All dynamics and parameter values are real. The phase interval is \([0,1]\). For the proof fix \(0<b<1/2\), let \(d\in(0,b)\), and put \(x=b-d\), \(y=b+d\). Define
\[
A_b(d)=\frac1d\log\frac{(b+d)(1-b+d)}{(b-d)(1-b-d)}.
\]
The formula is well-defined because \(0<x<y<1\). Its role is to parametrize the unique primitive two-cycle at intensity \(a=A_b(d)\). Write \(q(t)=t(1-t)\). The cycle multiplier is the derivative of \(f_{a,b}^2\) at either cycle point. A zero multiplier means that an iterate meets a critical point of the one-step map, and implies local superattraction.

The open interval of admissible equilibria is **existential** and obtained by continuity at explicit strict sign witnesses. The theorem is a certified existence and lower-bound result, not a complete classification of every parameter \(b\).

## Proof

**1. Exact parametrization and order.** Let \(h(t)=\log[(1-t)/t]\). Direct substitution yields
\[
h(f_{a,b}(t))-h(t)=a(t-b).
\]
If \(x,y\) are an interior primitive two-cycle, summing this identity shows \(x+y=2b\). Conversely, for any \(0<d<b<1/2\), the equation \(h(b-d)-h(b+d)=ad\) holds exactly at \(a=A_b(d)\); the identity for \(h\) proves \(f_{a,b}(b-d)=b+d\) and then \(f_{a,b}(b+d)=b-d\). Distinctness of the two points makes the cycle primitive.

The alternative representation
\[
A_b(d)=\frac2d\left[\operatorname{artanh}\left(\frac d b\right)+\operatorname{artanh}\left(\frac d{1-b}\right)\right]
\]
shows from the positive-coefficient series \(\operatorname{artanh}(z)/z=\sum_{j\ge0}z^{2j}/(2j+1)\) that \(A_b\) is **strictly increasing**. Moreover,
\[
\lim_{d\downarrow0}A_b(d)=\frac2{b(1-b)},\qquad
\lim_{d\uparrow b}A_b(d)=+\infty.
\]
Thus the above construction is the unique nontrivial two-cycle for every \(a>a_0(b)\), and its amplitudes \(d\) and intensities \(a\) have the same order.

**2. Exact derivative and boundary signs.** Elementary differentiation gives
\[
f_{a,b}'(t)=\frac{q(f_{a,b}(t))}{q(t)}[1-aq(t)].
\]
The \(q\)-factors cancel around a two-cycle, so its multiplier is the continuous function
\[
L_b(d)=\bigl[1-A_b(d)q(b-d)\bigr]
          \bigl[1-A_b(d)q(b+d)\bigr].
\]
As \(d\downarrow0\), both factors tend to \(-1\), giving \(\lim L_b(d)=+1\). As \(d\uparrow b\), the lower point \(b-d\to0\), and \(A_b(d)=O(\log[1/(b-d)])\); hence \(A_b(d)q(b-d)\to0\). Meanwhile \(b+d\to2b\in(0,1)\), so \(A_b(d)q(b+d)\to+\infty\). Consequently \(\lim_{d\uparrow b}L_b(d)=-\infty\).

**3. First rational sign certificate.** Take \(b_*=12/25\), \(d_1=2/5\). Then
\[
(x,y)=\left(\frac2{25},\frac{22}{25}\right),\quad
(q(x),q(y))=\left(\frac{46}{625},\frac{66}{625}\right),\quad
A_{b_*}(d_1)=\frac52\log\frac{253}{3}.
\]
The two derivative factors are therefore
\[
1-\frac{23}{125}\log\frac{253}{3},\qquad
1-\frac{33}{125}\log\frac{253}{3}.
\]
They have **opposite signs**. Indeed the elementary inequalities
\[
4<\log\frac{253}{3}<5
\]
follow from \(e<3\), hence \(e^4<81<253/3\), and from the truncated positive exponential series \(e^5>\sum_{j=0}^{5}5^j/j!=1097/12>253/3\). The first factor is greater than \(1-23\cdot5/125>0\); the second is less than \(1-33\cdot4/125<0\). Thus \(L_{b_*}(d_1)<0\).

**4. Second rational sign certificate.** Take \(d_2=23/50\), which satisfies \(d_1<d_2<b_*\). Direct exact arithmetic gives
\[
(x,y)=\left(\frac1{50},\frac{47}{50}\right),\quad
(q(x),q(y))=\left(\frac{49}{2500},\frac{141}{2500}\right),\quad
A_{b_*}(d_2)=\frac{50}{23}\log\frac{2303}{3}.
\]
Both derivative factors are **positive**, since
\[
\log\frac{2303}{3}<7,
\]
which follows from \(e^7>\sum_{j=0}^{8}7^j/j!=4605383/5760>2303/3\), and because
\[
1-\frac{141}{1150}\,7>0,
\qquad
1-\frac{49}{1150}\,7>0.
\]
Hence \(L_{b_*}(d_2)>0\).

**5. Three distinct superattracting intensities.** From Steps 2–4, the signs of \(L_{b_*}(d)\), sampled in increasing amplitude, follow
\[
+\quad (d\downarrow0),\qquad -\quad (d=d_1),\qquad
+\quad(d=d_2),\qquad-\quad(d\uparrow b_*).
\]
By continuity, at least one multiplier zero lies in each of the three mutually disjoint open intervals \((0,d_1)\), \((d_1,d_2)\), \((d_2,b_*)\). Strict increase of \(A_{b_*}\) sends them to three distinct and successively ordered intensities, all greater than the flip threshold. A zero multiplier of a primitive orbit is a superattracting two-cycle.

**6. Robustness in equilibrium asymmetry.** The values \(L_b(d_1)\) and \(L_b(d_2)\) depend continuously on \(b\) whenever \(d_2<b<1/2\). Both strict witness inequalities therefore persist on some open interval containing \(b_*\). The limiting signs at \(d\downarrow0\) and \(d\uparrow b\) in Step 2 hold for every such \(b\), and the preceding intermediate-value argument applies verbatim. This gives the asserted open family and completes the proof.

## Verification

The accompanying `verify.py` uses only the Python standard library. It checks all rational fractions in the two witnesses, the exact finite Taylor bounds for exponentials, exact inequalities controlling the derivative factors, the signs of the cycle multiplier, numerical root brackets for three distinct superattraction intensities, and sample forward-map identities. Run `python3 verify.py`. In the tested environment it prints `VERIFY_OK exact_rational_witnesses=2 numerical_root_brackets=3 forward_cycle_checks=4` and gives approximate witness intensities \(10.381142138\), \(12.240124888\), \(25.984447188\). The numerical roots and forward calculations are **illustrative**; the assertion for all real parameters in the open interval follows from the exact inequalities and analytic proof, not finite computations. The source file checked is precisely the embedded `verify.py`.

## Relationship to prior work

Kryzhevich and Zhang (2026) analyze this replicator map in their study of statistical invariants, bifurcations and chaotic invariant sets. Their first-public 2026 work motivates a more detailed dynamical question but **does not establish** the three-zero fixed-equilibrium phenomenon. Kryzhevich, Zhang and Chmara (2024) and Kryzhevich, Avrutin and Söderbacka (2021) derive and analyze the two-cycle's existence, near-bifurcation stability and symmetric/asymmetric regimes. The cycle's uniqueness is prior knowledge and is **not claimed new** here.

Most importantly, Chotibut, Falniowski, Misiurewicz and Piliouras (2019/2020) already identify superstable curves of the very same multiplicative-weights map and numerically study their intersections, including period-two configurations (NeurIPS 2020 supplement, pp. 23–27, Figs. 6, 8, 9). Thus neither superattracting period-two orbits **nor intersecting critical-orbit parameter curves** are new phenomena. The specific new claim is the fully analytic **fixed-equilibrium three-distinct-intensity lower bound on an open set**, established through two rational sign certificates. The examined figures and approximate large-coupling curve conditions do not assert that fixed-equilibrium theorem; if a hidden exact consequence of an earlier published classification exists, its priority would supersede this one.

A published mathematical finding titled *Singular symmetry-breaking threshold for the period-two orbit of a replicator map* proves a **unique multiplier \(-1\) crossing** for sufficiently small asymmetry. That is a different assertion: the multiplier may cross zero repeatedly while remaining above \(-1\), so uniqueness at \(-1\) does not imply, contradict or dominate the three-zero claim. The present theorem does not assert an additional stability loss.

## Limitations

This is an existence theorem: it proves **at least** three zeros of the unique period-two multiplier for one rational equilibrium and an unspecified open neighborhood; it does not determine the exact number of zeros or the maximal equilibrium interval. The limiting-sign argument is specific to \(0<b<1/2\), with the reflected case obtainable by the familiar \(x\mapsto1-x\) symmetry, and does not classify all asymmetries. Other attractors may coexist. The root decimals are not certified values and are not necessary evidence. Literature priority may remain incomplete, especially for graphical or implicit superstable-curve analyses; independent scientific validation has not been performed.

## References

1. S. Kryzhevich and Y. Zhang, *Shift maps and statistical invariants for some dynamical systems*, arXiv:2603.20685v1, posted 2026-03-21, https://arxiv.org/abs/2603.20685.
2. T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, *The route to chaos in routing games: When is price of anarchy too optimistic?*, arXiv:1906.02486 (first posted 2019-06-06), NeurIPS 33 (2020). Full supplementary text: https://papers.neurips.cc/paper_files/paper/2020/file/0887f1a5b9970ad13f46b8c1485f7900-Supplemental.pdf.
3. S. Kryzhevich, Y. Zhang and M. Chmara, *Bifurcations and invariant sets for a family of replicator maps from evolutionary games*, arXiv:2412.16379v1 (2024-12-20), https://arxiv.org/abs/2412.16379.
4. S. Kryzhevich, V. Avrutin and G. Söderbacka, *Bistability in a one-dimensional model of a two-predators-one-prey population dynamics system*, arXiv:2108.06739, https://arxiv.org/abs/2108.06739.
5. *Singular symmetry-breaking threshold for the period-two orbit of a replicator map*, published mathematical result (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-singular-symmetry-breaking-threshold-for-the-period-two-orbit-of--fdee730ba349.
