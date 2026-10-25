# A sharp expertise-scale switch in optimal five-member majority committees

## Finding

**Theorem (scale law and first possible switch).** Consider a fixed group of independent, individually better-than-random binary decision makers. Partition them into equally sized odd-member committees. A committee decides by unweighted simple majority; its accuracy is the probability of the correct collective decision. Assign equal weight to the committees' accuracies. If every individual's excess skill over random guessing is multiplied by a common positive factor, the set of optimal allocations is independent of that factor for one- and three-member committees. For five-member committees, it need not be independent: there exist ten distinct positive skill levels and **exactly one** critical common scale at which the optimal split changes. In addition, for any finite number of five-member committees, the optimal sum of within-committee fifth-order skill products never decreases when the common scale increases.

Here is an explicit complete phase diagram. Index the ten people by \(1,\ldots,10\), with baseline skill profile
\[
(a_1,\ldots,a_{10})=(1,2,3,4,5,6,7,8,11,15),\qquad
p_i(s)=\frac12+s a_i,\quad 0<s<\frac1{30}.
\]
Each group of five is assigned to one of two equally weighted binary decisions. Among the \(126\) unordered partitions, write
\[
\begin{aligned}
\mathcal P_-&=\{\{1,2,4,9,10\},\{3,5,6,7,8\}\},\\
\mathcal P_+&=\{\{1,2,3,9,10\},\{4,5,6,7,8\}\},\\
s_*&=\frac{1}{30\sqrt3}.
\end{aligned}
\]
For \(0<s<s_*\), \(\mathcal P_-\) is the **unique** optimal unordered partition; for \(s_*<s<1/30\), \(\mathcal P_+\) is unique. At \(s=s_*\), precisely these two partitions tie. Thus the sharp first possible odd committee size for dependence of an optimal allocation on uniform skill amplification is five.

## Assumptions and scope

For each binary decision, individual correctness events are independent, with probability \(p_i(s)=1/2+s a_i\); all \(a_i\) are fixed and positive. A single expert is assigned to exactly one of the committees. Each committee makes one binary majority decision; there are no ties within an odd-sized committee. The planner maximizes the *sum*, equivalently the equal-weight mean, of the committee probabilities of reaching their correct decisions. Nothing requires correctness for different assigned proposals to be mutually independent. All comparisons concern **unordered** allocations, so exchanging committee labels does not create a new allocation. The exact witness assumes ten people, two five-person committees and \(0<s<1/30\). The general scale law and monotonicity statements apply to any partition into any finite number of five-person committees, with \(0<s<1/(2\max_i a_i)\).

For a vector \(v=(v_1,\ldots,v_k)\), denote by \(e_j(v)\) the degree-\(j\) elementary symmetric polynomial, and by \(e_1(v)=\sum v_i\) its sum. For a partition \(\mathcal P\) into five-person blocks, set
\[
A(\mathcal P)=\sum_{C\in\mathcal P}e_3((a_i)_{i\in C}),\qquad
B(\mathcal P)=\sum_{C\in\mathcal P}\prod_{i\in C}a_i.
\]

## Proof

**(1) The majority identity.** Write \(q_i=p_i-1/2\). By expanding the \(2^5\) correctness patterns with at least three correct votes, the probability of majority correctness for five independent voters equals
\[
G_5(q_1,\ldots,q_5)=\frac12+\frac38e_1(q)-\frac12e_3(q)+6e_5(q).
\]
The expression is separately affine in each \(q_i\). Symmetry of the rule and the identity \(G_5(-q)=1-G_5(q)\) eliminate all even-degree monomials. The remaining coefficients can be determined by evaluating the cases with respectively one, three or five varied coordinates; direct expansion yields \(3/8\), \(-1/2\), \(6\). This also follows from the 32-vertex exact interpolation check in the independent verifier. Similarly,
\[
G_3(q_1,q_2,q_3)=\frac12+\frac12e_1(q)-2e_3(q),
\qquad G_1(q)=\frac12+q.
\]
Consequently, the *sum* of the accuracies of all committees of size five has the exact form
\[
\frac Z2+\frac{3s}{8}\sum_{i=1}^{5Z}a_i
-\frac{s^3}{2}A(\mathcal P)+6s^5B(\mathcal P).
\]
For fixed \(s>0\), this is maximized precisely when
\[
Q_s(\mathcal P)=A(\mathcal P)-12s^2B(\mathcal P)
\]
is minimized. With three-person committees the only allocation-dependent term is \(-2s^3\sum_C\prod_{i\in C}a_i\), so the optimal partitions are scale-independent; one-person committees are also scale-independent.

**(2) General comparative statics for five-person committees.** Suppose \(s_1<s_2\), and \(\mathcal P_1\) and \(\mathcal P_2\) are optimal at those respective scales. Put \(\Delta A=A(\mathcal P_2)-A(\mathcal P_1)\), \(\Delta B=B(\mathcal P_2)-B(\mathcal P_1)\). Comparing the two objective values at both scales gives
\[
12s_1^2\Delta B\le\Delta A\le12s_2^2\Delta B.
\]
Because \(s_1<s_2\), these inequalities force \(\Delta B\ge0\), and hence \(\Delta A\ge0\). This holds for arbitrary choices of optimizers, including boundary ties. The minimum of finitely many affine functions of \(s^2\) is piecewise affine and concave, so only finitely many changes of optimal partition are possible unless two objective lines coincide identically.

**(3) Exact ten-person phase diagram.** Enumerate every five-element subset containing person \(1\), and pair it with its complement. This lists each unordered partition exactly once because exactly one committee contains person \(1\). The number is \(\binom95=\binom94=126\). For the two named partitions, direct integer arithmetic gives
\[
\begin{array}{c|cc}
 &A&B\\\hline
\mathcal P_-&3346&6360\\
\mathcal P_+&3352&7710
\end{array}.
\]
Therefore
\[
Q_s(\mathcal P_+)-Q_s(\mathcal P_-)=6-16200s^2,
\]
so their unique crossing in the permitted parameter interval is \(s_*^2=1/2700\).

It remains to exclude all other partitions **for the entire continuum** of admissible scales, rather than at sample scales. The following finite, exact certificate does so. At \(u=s^2=0\), compare all other partitions to \(\mathcal P_-\); at \(u=1/2700\), compare them to the tied candidates; and at \(u=1/900\), compare to \(\mathcal P_+\). Exhaustively evaluating the \(126\) partitions with the elementary-symmetric integer formula gives the following **minimum differences** among the other \(124\) partitions:
\[
\begin{array}{c|ccc}
u&0&1/2700&1/900\\\hline
\min_{\mathcal P\notin\{\mathcal P_-,\mathcal P_+\}}
\bigl(Q_{\sqrt u}(\mathcal P)-\min\{Q_{\sqrt u}(\mathcal P_-),Q_{\sqrt u}(\mathcal P_+)\}\bigr)
&36&112/3&52
\end{array}.
\]
The expressions \(Q_s(\mathcal P)\) are affine in \(u=s^2\). Since \(\mathcal P_-\) is the better candidate on \([0,1/2700]\) and \(\mathcal P_+\) is better on \([1/2700,1/900]\), strict positivity of the other-partition differences at both endpoints of each interval implies strict positivity throughout that interval. The exact verifier enumerates all 126 candidates and recomputes all six displayed integer coefficients and all three margins without floating-point arithmetic. Thus no other allocation is optimal at any admissible scale, proving the stated phase diagram and uniqueness.

## Verification

The companion `verify.py` implements the 126-case proof certificate using only the Python standard library and exact rational arithmetic. It separately checks majority correctness by direct summation over all \(2^5\) vote outcomes for both sample scales \(s=1/60\) and \(s=1/32\), and verifies the analytic multilinear majority identity at all \(2^5\) interpolation vertices. Its associated `certificate.json` records: \(126\) unordered partitions, \(40\) interpolation checks, \(252\) direct five-person probability comparisons, exact coefficient pairs \((3346,6360)\) and \((3352,7710)\), and the strict exclusion margins \(36,112/3,52\). Run `python verify.py` and compare the output to `certificate.json`.

## Relationship to prior work

Ben-Yashar and Danziger (2011) study symmetric versus asymmetric optimal compositions of two odd-member simple-majority committees, and exhibit five-member asymmetric superiority under duplicated expert abilities. Their specific assumptions, examples and theorems do not provide an exact *uniform-skill-scaling phase diagram for ten distinct abilities*, nor the general monotone \(B\)-statistic proved above. Ben-Yashar and Danziger (2014) derive the exact triple-product criterion for three-member majority committees, which yields the scale-independence baseline here. Ben-Yashar and Danziger (2016) solve the *unanimity* rather than majority decision-rule objective. The new result does **not** claim to originate majority-rule correctness polynomials, the three-person product criterion, or the observation that five-person compositions may be asymmetric. It isolates and exactly proves a specific comparative-statics phenomenon for five-person majority committees, sharpening the distinction with three-person committees.

## Limitations

The exact phase diagram concerns one distinct ten-skill profile and homogeneous amplification of the excess-correctness probabilities; the general monotonicity statement is restricted to five-person blocks. It is not a characterization of all possible five-person partitions for arbitrary skills, nor a bound on the maximal number of changes for general larger committees. Expertise levels are known, independent within a question, stable across questions, and informative \((p_i>1/2)\); strategic voting, correlated signals, unequal committee stakes, and information acquisition are outside scope. This result is not independently audited. Literature search cannot establish absolute novelty; a previously unnoticed five-committee scale classification remains a residual bibliographic risk.

## References

1. R. Ben-Yashar and L. Danziger, *Symmetric and Asymmetric Committees*, IZA Discussion Paper 5782 (June 2011), accessible full text: https://docs.iza.org/dp5782.pdf; journal DOI 10.1016/j.jmateco.2011.06.001.
2. R. Ben-Yashar and L. Danziger, *On the Optimal Composition of Committees*, IZA Discussion Paper 7963 (February 2014), accessible full text: https://docs.iza.org/dp7963.pdf; journal DOI 10.1007/s00355-014-0805-z (published online February 19, 2014).
3. R. Ben-Yashar and L. Danziger, *The Unanimity Rule and Extremely Asymmetric Committees*, IZA Discussion Paper 9875 (April 2016), accessible full text: https://docs.iza.org/dp9875.pdf.
