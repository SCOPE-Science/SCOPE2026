# An irreversible Rule-54/Rule-18 phase filtration in a normalized separable-field automaton

## Finding

The rank-one, nonlocal cellular automaton of Shi and Huang contains a natural invariant stripe sector which is governed not by a single local rule, but by an **irreversible switch between two classical elementary cellular automata**. The switch is selected by the largest local triple occupancy. The result applies simultaneously to all cyclic heights and all widths, for an interval of threshold parameters containing an explicit value on the fine-scan axis of the source model.

**Theorem.** Let \(H,W\ge3\) be integers, and let \(S=[s_-,s_+]\) and \(B=[b_-,b_+]\) be closed intervals with
\[
0<s_-\le\frac13\le s_+<\frac12,
\qquad
0<b_-\le\frac13,\quad \frac23\le b_+<1.
\]
Let \(\mathcal F_{S,B}\) be the normalized separable-field update defined below. The stripe subspace
\[
\mathcal Y=\{X\in\{0,1\}^{H\times W}: X(j,i)=y_j\text{ for some }y\in\{0,1\}^{H}\}
\]
is invariant, and its exact induced update \(G\) is
\[
G(y)=\begin{cases}
\operatorname{ECA}_{54}(y),&m(y)=3,\\
\operatorname{ECA}_{18}(y),&m(y)=2,\\
0,&m(y)\in\{0,1\},
\end{cases}
\qquad
m(y)=\max_j\big(y_{j-1}+y_j+y_{j+1}\big).
\]
The full cyclic orbit has a one-way filtration: once \(m\le2\) it can never again equal \(3\); if \(m\le1\), the next state is identically zero. Consequently a periodic orbit in the stripe sector is either entirely Rule 54, entirely Rule 18, or the all-zero fixed point.

The same statements hold with rows and columns interchanged. For the concrete thresholds \(S=[1/18,7/18]\), \(B=[1/3,8/9]\), height \(H=13\), any width \(W\ge3\), and seed \(y=\texttt{\#.\#\#\#........}\) (the literal 13-symbol word `#.###........`), the orbit has primitive period exactly \(169\) and stays in the Rule-54 region in all its phases. This last cycle is an explicit realization in the two-dimensional normalized automaton of period behavior known earlier for the standalone one-dimensional Rule 54.

## Assumptions and scope

The finite lattice is the torus \(\mathbb Z/H\mathbb Z\times\mathbb Z/W\mathbb Z\). Let \(X(j,i)\in\{0,1\}\), define row and column totals
\[
r_j=\sum_iX(j,i),\qquad c_i=\sum_jX(j,i),
\]
and their three-neighbor blurs \(R_j=r_{j-1}+r_j+r_{j+1}\), \(C_i=c_{i-1}+c_i+c_{i+1}\). The field is \(N(j,i)=R_jC_i\). If \(N_{\max}=\max_{j,i}N(j,i)>0\), write \(q(j,i)=N(j,i)/N_{\max}\). Alive sites survive precisely when \(q\in S\), and dead sites are born precisely when \(q\in B\). The all-dead state is fixed by convention. These are the source model's synchronous updates with closed thresholds and periodic indexing.

Define ECA Rule 54 by the local output \(1\) for neighborhoods \(101,100,010,001\), and output \(0\) otherwise; define Rule 18 by output \(1\) for \(100,001\) and \(0\) otherwise. We use the standard cyclic application of these local rules, not their infinite-lattice extensions. The theorem is restricted to stripe initial data, but the stripes are evolved using the **original two-dimensional** operator, not an altered model. Non-stripe perturbations are not classified.

## Proof

**1. Exact cancellation and invariance.** For any nonzero stripe state \(X(j,i)=y_j\), put \(M=\sum_jy_j>0\) and \(t_j=y_{j-1}+y_j+y_{j+1}\). Every column occupancy equals \(M\), hence every blurred column sum is \(C_i=3M\). The row sums are \(r_j=Wy_j\), so \(R_j=Wt_j\). Consequently
\[
N(j,i)=3WMt_j,\qquad N_{\max}=3WMm(y),\qquad q(j,i)=\frac{t_j}{m(y)}.
\]
The normalized field is constant within every row, so a synchronous update leaves every row constant. This proves the invariant embedding and, crucially, shows that its dynamics are independent of \(W\). The zero seed stays zero by convention.

**2. Truth-table reduction.** If \(m(y)=3\), the only possible positive normalized field values are \(1/3,2/3,1\). A live central site has \(t_j\ge1\) and survives precisely when \(t_j=1\), namely in neighborhood \(010\). A dead central site has \(t_j\le2\), and is born precisely when \(t_j\in\{1,2\}\), namely neighborhoods \(001,100,101\). Therefore the output-one neighborhoods are \(101,100,010,001\), exactly Rule 54.

If \(m(y)=2\), the possible values are \(0,1/2,1\). No live cell survives since \(s_+<1/2\). Dead sites are born exactly at \(1/2\), for neighborhoods \(001,100\), giving Rule 18. If \(m(y)=1\), the possible values are \(0,1\), neither of which lies in \(S\) or \(B\), so the next configuration is zero. The case \(m=0\) is the zero state. This proves the exact piecewise formula in every admissible parameter choice, including equality at \(1/3\) and \(2/3\).

**3. One-way filtration.** Suppose \(z=\operatorname{ECA}_{18}(y)\). We claim \(z\) contains no cyclic occurrence of \(111\). If \(z_j=z_{j+1}=1\), the Rule-18 definition forces \(y_j=y_{j+1}=0\), \(y_{j-1}=1\) and \(y_{j+2}=1\). Hence \(z_{j+2}=0\), since its center \(y_{j+2}\) is alive and Rule 18 only creates a one on a dead center. Therefore \(m(z)\le2\). A state with \(m\le1\) maps to zero, and zero is fixed. It follows that the sets \(\{m\le2\}\) and \(\{m\le1\}\cup\{0\}\) are forward invariant, while a transition out of \(\{m=3\}\) cannot reverse. A periodic orbit cannot cross such a one-way boundary and return, yielding the asserted trichotomy.

**4. Period-169 realization.** At \(S=[1/18,7/18]\), \(B=[1/3,8/9]\) the hypotheses hold. Starting from the literal cyclic word `#.###........` of length \(13\), the standalone exact checker generates all \(169\) consecutive words under the original normalized update, verifies that they are pairwise distinct, verifies the presence of \(111\) at every step, and verifies that step \(169\) returns exactly to the initial word. It independently compares the full two-dimensional field update with the stripe update for widths \(3\) and \(5\). The analytical width-independence established in step 1 then supplies the result for every integer \(W\ge3\). No conclusion about global maximum period at height \(13\) is claimed.

## Verification

The embedded standard-library program `verify.py` performs exact rational arithmetic. Running `python3 verify.py` prints `VERIFY_OK assertions=7161 orbit_period=169 rule_regimes=(54,18,0)` and exits only if all assertions pass. Its 7,161 checks include exhaustive one-step comparisons for every cyclic word of lengths \(3\) through \(9\) for four threshold choices, independent implementations of the full two-dimensional outer-product rule, the no-\(111\) implication at the Rule-18 stage, a direct 169-state orbit certificate, and all small-height cycle regime checks. The infinite-height filtration is proved in steps 1–3, not extrapolated from these finite tests. The period-169 claim itself is a finite exact assertion verified by explicitly checking all 169 states.

## Relationship to prior work

Shi and Huang [1] introduced this exact rank-one normalized model and numerically observed stripes, distinct cyclic regimes and unusually long transients. Their August 2026 version v2 states that analytic lower-dimensional reductions of the row/column dynamics would help explain these patterns (discussion, pp. 8–10); it does not give the present local-rule switching classification or its irreversible orbit filtration. Their definitions and scan thresholds are treated as prior work.

Rule 54 and its complex periodic orbit structure are classical. Martínez, Adamatzky and McIntosh [2] explicitly give its truth table, investigate 13-cell cycles and exhibit a 169-cycle (Section 4 and Figure 15). We do not claim to have discovered the rule or its standalone period. The new comparison is **implication across models**: knowing the rule's cycles alone does not show that the globally normalized, two-dimensional Shi–Huang automaton contains the rule as an exact, invariant subsystem, and neither source establishes the full conditional Rule-54/Rule-18/zero transition and one-way boundary. Rule 18 itself is also a standard ECA [3]. The reduction is a deliberately constrained but exact analytic complement to the source's high-dimensional simulations.

## Limitations

No claim is made about generic initial conditions, transverse stability of the stripe sector, global classification of the full two-dimensional phase diagram, or a universal period-169 lower bound for other dimensions. The 169-cycle is a transfer of a **known** one-dimensional periodic phenomenon, not a novel standalone Rule-54 cycle. Literature equivalences beyond the sources inspected remain a priority risk; a negative search alone does not establish novelty. The result is conditional on the exact closed threshold inequalities and the original all-zero convention. Independent scientific validation has not been performed.

## References

[1] X. Shi and M. Huang, *Dynamics in a Low-Rank Separable Field Cellular Automaton*, arXiv:2606.08983v2 (4 August 2026), first public v1 on 8 June 2026. https://arxiv.org/abs/2606.08983v2 and https://arxiv.org/pdf/2606.08983v2.

[2] G. J. Martínez, A. Adamatzky and H. V. McIntosh, *Complete Characterization of Structure of Rule 54*, *Complex Systems* **23** (2014), 259–293, doi:10.25088/ComplexSystems.23.3.259; https://www.complex-systems.com/abstracts/v23_i03_a04/.

[3] S. Wolfram, *Statistical Mechanics of Cellular Automata*, *Reviews of Modern Physics* **55** (1983), 601–644; standard ECA numbering also summarized at https://mathworld.wolfram.com/ElementaryCellularAutomaton.html.
