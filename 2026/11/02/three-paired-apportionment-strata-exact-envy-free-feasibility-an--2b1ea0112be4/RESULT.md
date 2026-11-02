# Three paired apportionment strata: exact envy-free feasibility and sharp lottery support

## Finding

Consider a quota-preserving, ex-ante proportional randomized apportionment of six parties, divided into three pairs having three **distinct** integer lower quotas. Within pair \(i\), label the parties \(H_i,L_i\) in nonincreasing order of their fractional quota residues \(h_i,\ell_i\). Suppose exactly three seats remain after assigning the lower quotas, so
\[
0\leq\ell_i<h_i<1,\qquad \sum_{i=1}^{3}(h_i+\ell_i)=3.
\]
Set \(S=\ell_1+\ell_2+\ell_3\). An ex-ante proportional, ex-post inversion-free lottery exists **if and only if**
\[
\boxed{S\leq1\quad\text{and}\quad \ell_i+1-h_i\leq S\ \text{for }i=1,2,3.}
\]
Here *inversion-free* means that in every realized allocation, the higher-residue party in each pair receives at least as many seats as its lower-residue partner. Because the within-pair residues are strictly different, this is exactly the absence of realized seat envy: no party with a strictly larger standard quota receives fewer seats. The cross-block pairs cannot have seat inversions because their integer lower quotas differ.

Whenever the inequalities hold, a lottery supported on **at most six** complete seat allocations suffices. This support bound is **sharp**: one valid six-party rational-quota instance requires six distinct realizations. In the symmetric subfamily \(h_i=p\) and \(\ell_i=1-p\) for all three pairs, with \(1/2<p<1\), an inversion-free proportional lottery exists exactly when \(p\geq2/3\).

## Assumptions and scope

Let \(F_1,F_2,F_3\) be distinct nonnegative integers. The six standard quotas are \(F_i+h_i\) and \(F_i+\ell_i\), and the chamber has exactly \(2(F_1+F_2+F_3)+3\) seats. A realized allocation rounds each standard quota down or up and uses exactly the available seats. Ex-ante proportionality requires the up-rounding probabilities of \(H_i,L_i\) to equal \(h_i,\ell_i\), respectively. Within every pair, residues are assumed strictly ordered. This avoids ambiguities about ties, where equal-quota parties may legitimately receive different seat counts without seat envy. All probabilities and quota residues are real, and the lower residue may equal zero. A party with an integral quota has zero up-rounding probability.

## Proof

**1. Enumeration of inversion-free outcomes.** Write \(U_i,V_i\in\{0,1\}\) for the up-rounding indicators of \(H_i,L_i\). The inversion-free requirement is \(U_i\geq V_i\). Thus each pair contributes either zero, one or two extra seats, with respective patterns \((0,0),(1,0),(1,1)\). Since \(\sum_i(U_i+V_i)=3\), the only possible count triples are \((1,1,1)\) and the six permutations of \((2,1,0)\). No other outcome meets both the cardinality constraint and the no-inversion requirement.

Denote the probability of \((1,1,1)\) by \(z\). For distinct \(i,j\in\{1,2,3\}\), denote by \(x_{ij}\) the probability of the count pattern with two extra seats in pair \(i\), none in pair \(j\), and one in the remaining pair. Ex-ante proportionality is equivalent to
\[
\sum_{j\ne i}x_{ij}=\ell_i,\qquad
\sum_{i\ne j}x_{ij}=1-h_j,\qquad x_{ij}\geq0,\qquad z=1-S.
\]
Indeed, the lower-residue party is selected only when its pair contributes two extras; the higher-residue party is omitted only when its pair contributes none. The two sets of transportation margins have the same total, since
\[
\sum_i(1-h_i)=3-\sum_i h_i=\sum_i\ell_i=S.
\]

**2. Necessary and sufficient inequalities.** Necessarily \(z=1-S\geq0\). In the off-diagonal transportation system, all mass sent by row \(i\) must enter one of the two columns different from \(i\). Their combined capacity is \(S-(1-h_i)\), so \(\ell_i\leq S-(1-h_i)\). These are exactly the claimed inequalities.

For sufficiency, consider the bipartite graph with three row vertices and three column vertices, with edge \((i,j)\) allowed just when \(i\ne j\). Give row \(i\) supply \(\ell_i\) and column \(j\) demand \(1-h_j\). The max-flow/min-cut condition for a nonnegative transportation matrix requires every subset of rows to have supply no greater than the total demand of its neighboring columns. A singleton row has precisely the two neighbors different from itself, yielding the three displayed inequalities. Every subset of at least two rows has **all three columns** as neighbors, and its supply is at most the total supply \(S\). Hence the listed inequalities suffice by the max-flow/min-cut theorem. Set \(z=1-S\) and use the resulting \(x_{ij}\) as the probabilities of the seven enumerated outcomes. The probabilities are nonnegative, sum to one, and give every party its exact marginal.

**3. Six-outcome support bound.** The six allowed transportation edges form a single bipartite six-cycle. If some edge has zero weight, the lottery already has at most five \((2,1,0)\)-outcomes and at most one \((1,1,1)\)-outcome, hence support at most six. If all six edge weights are positive, alternately add and subtract the same amount around that cycle. This preserves every row and column margin. Increase or decrease the amount until a nonnegative edge becomes zero; all weights remain nonnegative. Thus a feasible transportation table always exists with at most five positive edges. Including the common \((1,1,1)\) outcome proves the support bound.

**4. Sharpness with actual standard quotas.** Take three distinct lower quotas \((F_1,F_2,F_3)=(1,2,3)\), and within the corresponding pairs set
\[
(h_1,\ell_1)=\left(\frac{32}{40},\frac3{40}\right),\quad
(h_2,\ell_2)=\left(\frac{32}{40},\frac7{40}\right),\quad
(h_3,\ell_3)=\left(\frac{34}{40},\frac{12}{40}\right).
\]
For a fifteen-seat chamber, these are precisely the standard quotas derived from integer vote counts \((72,43,112,87,154,132)\), totaling \(600\). A feasible off-diagonal transportation table, in edge order \((12,13,21,23,31,32)\), has weights
\[
\frac1{40}(1,2,3,4,5,7).
\]
Its row sums are \((3,7,12)/40\) and column sums are \((8,8,6)/40\), as required. The \((1,1,1)\) outcome has the forced positive mass \(z=18/40\).

Every transportation table with these margins has the following *unique one-parameter form*:
\[
(x_{12},x_{13},x_{21},x_{23},x_{31},x_{32})
=\frac1{40}(1-t,2+t,3+t,4-t,5-t,7+t),\qquad -2\leq t\leq1.
\]
The form follows by solving the six margin equations (whose coefficient matrix has one-dimensional nullspace), and the interval is exactly the nonnegativity condition. At either endpoint precisely one of the six entries is zero; in its interior all six are positive. Thus every inversion-free proportional lottery gives positive mass to **at least five** of the six \((2,1,0)\) outcomes, and also to the mandatory \((1,1,1)\) outcome. Six realizations are necessary, proving sharpness.

**5. Symmetric threshold.** If all three pairs have \(h_i=p\) and \(\ell_i=1-p\), then \(S=3(1-p)\). Each singleton-cut inequality becomes \(2(1-p)\leq3(1-p)\), which always holds. The remaining requirement \(S\leq1\) is exactly \(p\geq2/3\).

## Verification

The accompanying `verify.py` uses the Python 3 standard library. It enumerates all twenty ways of assigning three extra seats to six parties and checks that precisely seven are inversion-free. It also enumerates every integer-grid weakly ordered residue profile with denominators from two through ten and total residue three, comparing the displayed cut inequalities with an independently implemented integral max-flow feasibility calculation for the fixed-priority inversion-free extension (including tied-residue test cases). The theorem itself claims equivalence to actual no-envy only for strictly ordered pairs. The script checks the rational sharp-support witness and its exact feasible one-dimensional interval. Run with `python3 verify.py` in the same directory. This finite verification is corroboration, **not** the proof for arbitrary real residues; the max-flow reduction and cycle argument above establish the general theorem.

## Relationship to prior work

La Commare, Tucker-Foltz and Verdugo (2026) introduce randomized apportionment envy and a general flow-based linear feasibility program for zero envy. Their formulation is the broader algorithmic starting point, and the seven admissible count patterns here are a specialization of their blockwise-prefix condition. The contribution proved here is an explicit closed-form feasibility region in the first three-pair, three-surplus-seat configuration **together with a sharp minimal lottery-support bound**, including a rational quota instance that forces that many outcomes. Neither a general LP feasibility test nor the mere existence of a flow supplies that explicit cut description and worst-case support lower bound as a stated result. The transportation cut criterion and cycle adjustment are established mathematical techniques, not claimed as new in isolation.

## Limitations

The result concerns precisely three *distinct* equal-floor pairs with strictly different within-pair residues, six parties, quota-respecting rounds and exactly three surplus seats. If two parties within a pair have tied quotas, the criterion still characterizes a fixed-priority inversion-free lottery, but may be unnecessarily restrictive for literal no-envy; no necessity claim is made there. It does not give a formula for minimum positive envy outside the feasible region, other block sizes, arbitrary party counts, or other proportionality axioms. The source's general LP solves a broader feasibility problem. The derivation is a structural finite-dimensional specialization with a sharp support-complexity result; it does not claim general-purpose algorithmic superiority. Priority risks include equivalent unstated applications of the original LP and earlier dependent-rounding or coupling literature. Independent expert validation has not been performed.

## References

- F. La Commare, J. Tucker-Foltz, and V. Verdugo, *Envy-Free Randomized Apportionment*, arXiv:2610.24217v1, first submitted 16 October 2026. https://arxiv.org/abs/2610.24217
- B. Doerr and M. Wahlström, *Randomized Rounding in the Presence of a Cardinality Constraint*, ALENEX 2009, DOI:10.1137/1.9781611972894.16. Related background on fixed-cardinality rounding, not the stated envy/six-support theorem.
