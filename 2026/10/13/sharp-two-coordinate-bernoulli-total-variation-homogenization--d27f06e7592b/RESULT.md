# Sharp two-coordinate Bernoulli total-variation homogenization

## Finding
For probability vectors \(p=(p_1,p_2)\) and \(q=(q_1,q_2)\) in \([0,1]^2\), write \(P=\mathrm{Ber}(p_1)\otimes\mathrm{Ber}(p_2)\), \(Q=\mathrm{Ber}(q_1)\otimes\mathrm{Ber}(q_2)\), \(\bar p=(p_1+p_2)/2\), and \(\bar q=(q_1+q_2)/2\). Put \(d=|p_1+p_2-q_1-q_2|\) and \(t=(p_1+p_2+q_1+q_2)/2\). For all such vectors,
\[
\operatorname{TV}(P,Q)\ge\frac{d}{2-|1-t|}\ge \frac89\operatorname{TV}\bigl(\mathrm{Ber}(\bar p)^{\otimes2},\mathrm{Ber}(\bar q)^{\otimes2}\bigr).
\]
The denominator lies in \([1,2]\). The uniform factor \(8/9\) is optimal: no larger factor holds for all \(p,q\). The first inequality gives an additional dependence on the pooled mean \(t\); it is not asserted to be the optimal bound at each fixed \(t\).

## Assumptions and scope
A Bernoulli law \(\mathrm{Ber}(u)\) puts probability \(u\) at one and \(1-u\) at zero. Products refer to independent coordinates, and total variation on a finite set is half the sum of the absolute probability-mass differences. Every coordinate lies in the closed interval \([0,1]\), including endpoints; the result holds without coordinatewise ordering of \(p\) and \(q\). The comparison concerns the labeled product laws on \(\{0,1\}^2\), not only their pushforward sums. If \(d=0\), both asserted lower bounds are zero, because \(\bar p=\bar q\).

## Proof
**Exact homogenized distance.** Let \(x,y\in[0,1]\), with \(x\ge y\). The probability differences between two copies of \(\mathrm{Ber}(x)\) and two copies of \(\mathrm{Ber}(y)\), at the ordered atoms \(00,01,10,11\), are
\[
-(x-y)(2-x-y),\quad (x-y)(1-x-y),\quad(x-y)(1-x-y),\quad(x-y)(x+y).
\]
Consequently,
\[
\operatorname{TV}\bigl(\mathrm{Ber}(x)^{\otimes2},\mathrm{Ber}(y)^{\otimes2}\bigr)
=|x-y|\bigl(1+|1-x-y|\bigr).
\]
Taking \(x=\max(\bar p,\bar q)\) and \(y=\min(\bar p,\bar q)\) yields
\[
\operatorname{TV}\bigl(\mathrm{Ber}(\bar p)^{\otimes2},\mathrm{Ber}(\bar q)^{\otimes2}\bigr)
=\frac{d}{2}\bigl(1+|1-t|\bigr).
\]

**Mass-sensitive lower bound.** Swapping \(P,Q\) does not affect either total variation or \(d,t\). Simultaneously replacing all Bernoulli outcomes by their complements in both products preserves their total variation and \(d\), and sends \(t\) to \(2-t\). Hence, whenever \(d>0\), we may arrange \(t\in[1,2]\) and \((p_1-q_1)+(p_2-q_2)=d>0\).

Set \(a=p_1-q_1\), \(b=p_2-q_2\), \(u=(p_1+q_1)/2\) and \(v=(p_2+q_2)/2\). Then \(a+b=d\), \(u+v=t\), and \(u,v\in[0,1]\). Since marginalization is a Markov kernel, the variation of the product laws dominates each marginal variation:
\[
\operatorname{TV}(P,Q)\ge\max\{|a|,|b|\}.
\]
The variation also dominates the difference of probabilities of any particular event. Applied to the joint-success event \(\{11\}\), this gives
\[
\operatorname{TV}(P,Q)\ge |p_1p_2-q_1q_2|=|va+ub|.
\]
If either \(a<0\) or \(b<0\), the other exceeds \(d\), so \(\operatorname{TV}(P,Q)\ge d\ge d/(3-t)\), because \(1\le t\le2\).

Otherwise \(a,b\ge0\), and with \(z=a/d\in[0,1]\), \(h=\max\{z,1-z\}\), the marginal bound is \(\operatorname{TV}(P,Q)/d\ge h\). The joint-success event gives a second estimate. Indeed,
\[
\begin{aligned}
\frac{p_1p_2-q_1q_2}{d}
&=vz+u(1-z)\\
&=1-(1-v)z-(1-u)(1-z)\\
&\ge1-\bigl((1-v)+(1-u)\bigr)h\\
&=1-(2-t)h,
\end{aligned}
\]
where the inequality uses \(1-u,1-v\ge0\) and \(z,1-z\le h\). Thus
\[
\frac{\operatorname{TV}(P,Q)}d\ge\max\{h,1-(2-t)h\}\ge\frac1{3-t}.
\]
For the final inequality, either \(h\ge1/(3-t)\) or \(h<1/(3-t)\), in which case \(1-(2-t)h\ge1-(2-t)/(3-t)=1/(3-t)\). This works also at \(t=2\), where \(2-t=0\). Undoing the complement symmetry, \(3-t=2-|1-t|\) for the reduced parameter, proving the first displayed inequality for all inputs.

**Optimal constant.** Write \(w=|1-t|\in[0,1]\). The exact homogenized formula and the first bound imply, for \(d>0\),
\[
\frac{\operatorname{TV}(P,Q)}{\operatorname{TV}(\mathrm{Ber}(\bar p)^{\otimes2},\mathrm{Ber}(\bar q)^{\otimes2})}
\ge\frac{2}{(2-w)(1+w)}\ge\frac89,
\]
using \((2-w)(1+w)=9/4-(w-1/2)^2\le9/4\). The statement is immediate for \(d=0\).

For sharpness, use the example already identified by Kontorovich: for \(0<\varepsilon\le1/2\), choose
\[
p=(1-2\varepsilon,1/2),\qquad q=(1,1/2+\varepsilon).
\]
Directly evaluating the four atoms gives \(\operatorname{TV}(P,Q)=2\varepsilon\); here \(d=3\varepsilon\), \(t=(3-\varepsilon)/2\), and
\[
\operatorname{TV}\bigl(\mathrm{Ber}(\bar p)^{\otimes2},\mathrm{Ber}(\bar q)^{\otimes2}\bigr)
=\frac{9\varepsilon-3\varepsilon^2}{4}.
\]
The ratio is \(8/(9-3\varepsilon)\), which tends to \(8/9\) as \(\varepsilon\downarrow0\). Thus \(8/9\) is the best uniform factor; the extremal sequence is credited to the existing work, while the new contribution is the matching universal lower bound in the two-coordinate case.

## Verification
The independent-coordinate event and marginal inequalities above give a proof for the complete continuum of parameters, including boundary cases. The included executable `check_two_site.py` independently computes both distances exactly on rational grids of mesh \(1/2,1/4,1/8,1/12\), verifying \(35{,}828\) ordered parameter quadruples. It checks the stronger mass-dependent lower bound and the uniform \(8/9\) bound, and evaluates four exact rational sharpness examples. Run `python3 check_two_site.py` with Python 3's standard library. These finite checks are supplementary and are not a substitute for the universal proof.

## Relationship to prior work
Aryeh Kontorovich's *TV homogenization inequalities* (arXiv:2601.04079, first posted January 7, 2026), Theorem 1.5 and its subsequent open-problem remark, establishes a positive constant for every dimension, presents the same two-site asymptotic upper-bound example, and explicitly conjectures that the best constant is \(8/9\). It does not establish the matching lower bound at two sites. Kontorovich's later *A homogenization principle for total variation* (arXiv:2604.03882, first posted April 4, 2026), Theorem 4, extends a positive constant to arbitrary measures but does not identify the conjecturally sharp factor. The present theorem establishes the optimal conjectured factor only when there are exactly two Bernoulli coordinates; the mass-sensitive lower bound is a supplementary finite-dimensional refinement. Hoeffding's classical fixed-mean convex-order principle compares convex expectations of Bernoulli sums, not the two-product total-variation ratio.

## Limitations
No conclusion is asserted for three or more coordinates, arbitrary multi-state factors, or the conjectured dimension-independent optimal constant. The sharpness example was already known and is not claimed as a new construction. The mass-sensitive inequality is not asserted sharp for every fixed pooled mean. Searches and primary-source comparison reduce, but cannot eliminate, the risk of earlier equivalent formulations. No independent mathematical audit has been performed.

## References
1. A. Kontorovich, *TV homogenization inequalities*, arXiv:2601.04079, first posted 2026-01-07; relevant portions: Theorem 1.5 and remarks/open problems; https://arxiv.org/abs/2601.04079 ; full text: https://arxiv.org/pdf/2601.04079 .
2. A. Kontorovich, *A homogenization principle for total variation*, arXiv:2604.03882, first posted 2026-04-04; relevant portions: Theorem 4 and introduction; https://arxiv.org/abs/2604.03882 ; full text: https://arxiv.org/pdf/2604.03882 .
3. W. Hoeffding, *On the distribution of the number of successes in independent trials*, Ann. Math. Statist. 27 (1956), 713–721. Referenced for the distinct classical fixed-mean comparison, not as a source of the sharp TV bound.
