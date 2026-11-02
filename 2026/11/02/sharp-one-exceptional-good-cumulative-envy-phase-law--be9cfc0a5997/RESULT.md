# Sharp one-exceptional-good cumulative-envy phase law

## Finding

For every integer \(r\ge1\) and real \(H\ge1\), consider two agents with identical additive values for \(r\) distinct unit-valued goods and one distinct good of value \(H\). The planner knows the goods and chooses both their release order and their irrevocable recipients. Write \(\operatorname{OPT}_r(H)\) for the minimum sum of maximum pairwise envy after each of the \(r+1\) arrivals. Then
\[
\operatorname{OPT}_r(H)=
\begin{cases}
\dfrac{r-1}{2}+H,&r\text{ odd},\\[1mm]
\dfrac r2+\min\bigl\{H,\max\{1,2H-3\}\bigr\},&r\text{ even}.
\end{cases}
\]
Equivalently, for even \(r\) the correction to \(r/2\) is \(1\) for \(1\le H\le2\), \(2H-3\) for \(2\le H\le3\), and \(H\) for \(H\ge3\). The breakpoints \(2\) and \(3\) are independent of the number of unit goods.

The nondecreasing-value rule releasing all unit goods and then the exceptional good, always assigning to a currently lower-valued agent, has cost \(G_r(H)=\lfloor r/2\rfloor+H\). It is optimal whenever \(r\) is odd or \(H=1\) or \(H\ge3\). For even \(r\), its exact additive excess is
\[
G_r(H)-\operatorname{OPT}_r(H)=
\begin{cases}
H-1,&1\le H\le2,\\
3-H,&2\le H\le3,\\
0,&H\ge3.
\end{cases}
\]
Its maximum additive excess is exactly \(1\), at \(H=2\), for every positive even \(r\).

## Assumptions and scope

There are exactly two agents; all goods are indivisible and have the same strictly positive additive value for both agents. Exactly \(r\ge1\) goods have value \(1\), and a single exceptional good has value \(H\ge1\), potentially nonintegral. At each time step exactly one good is released and allocated irrevocably; both the order and recipient are freely chosen in advance. The objective is the unweighted sum, over all prefixes, of maximum pairwise envy. No transfers, discarded goods, heterogeneous preferences, capacity constraints, or discounted rounds are allowed.

Let \(D_0=0\) be the initial signed difference between agents' received total values. Assigning a good of value \(w_t\) changes it by \(D_t-D_{t-1}\in\{w_t,-w_t\}\). The maximum pairwise envy at time \(t\) equals \(c_t=|D_t|\), so the objective is \(C=\sum_{t=1}^{r+1}|D_t|\).

## Proof

**1. Edge bound.** For any step, the triangle inequality implies
\[
w_t=|D_t-D_{t-1}|\le |D_{t-1}|+|D_t|.
\]
If several step indices are of the same parity, their endpoint pairs are disjoint; summing their edge bounds therefore lower-bounds \(C\), since \(D_0=0\).

**2. Odd number of unit goods.** Write \(r=2m+1\). There are \(2m+2\) steps. Let \(h\) be the position of the exceptional good. Select all steps of the same parity as \(h\), a set of \(m+1\) pairwise endpoint-disjoint edges. Their weights sum to \(H+m\). Hence \(C\ge H+m\). Release the \(2m+1\) unit goods first, assigning successively to a lower-valued agent; their absolute gaps are \(1,0,1,0,\ldots,1\), totaling \(m+1\). Assign the final value-\(H\) good to the agent behind by one, leaving gap \(H-1\). The total equals \(m+H\), proving the odd case.

**3. Even number: exceptional step at an odd position.** Write \(r=2m\). There are \(2m+1\) steps. If \(h\) is odd, the \(m+1\) odd-indexed steps (including the exceptional one) have disjoint endpoint pairs and total weight \(H+m\). Thus \(C\ge H+m\).

**4. Even number: exceptional step at an even position.** Write \(h=2j\), where \(1\le j\le m\), and set \(k=h-1=2j-1\). Just before the exceptional step, the gap has odd integer magnitude \(d\ge1\), with \(d\le k\). For each \(1\le t\le k\), parity and the triangle inequality from \(D_t\) to \(D_k\) imply
\[
|D_t|\ge\max\bigl\{t\bmod2,\ d-(k-t)\bigr\}.
\]
For odd \(k\) and \(d\) the sum of these pointwise bounds is \((k+d^2)/2=j+(d^2-1)/2\). Thus the cost through step \(k\) is at least \(j+(d^2-1)/2\). This bound is also sharp for unit-only prefixes: alternate near zero for \(k-d\) steps and then walk \(d\) consecutive steps towards the terminal side.

Let \(y=|D_h|\). The exceptional step gives \(y\ge|H-d|\). Define the nondecreasing function \(f(y)=y+|y-1|=\max\{1,2y-1\}\) for \(y\ge0\). Since the next good has unit value, \(|D_h|+|D_{h+1}|\ge f(y)\ge f(|H-d|)\). The remaining \(2(m-j)\) unit steps can be paired into \(m-j\) edges whose endpoint nodes are disjoint from those already charged; each such edge contributes at least \(1\). Therefore
\[
C\ge m+\frac{d^2-1}{2}+f(|H-d|).
\]
If \(d\ge3\), then \((d^2-1)/2\ge d\) and \(f(z)\ge z\) for all \(z\ge0\), yielding \(C\ge m+d+|H-d|\ge m+H\). If \(d=1\), the bound instead reads \(C\ge m+f(H-1)\). These two possibilities, together with step 3, give the universal lower bound
\[
C\ge m+\min\{H,f(H-1)\}.
\]

**5. Sharp constructions for even \(r\).** Releasing all \(2m\) unit goods alternately first leaves gap \(0\) at cost \(m\); releasing the exceptional good last adds \(H\), totaling \(m+H\). Alternatively, release \(2m-1\) unit goods in alternating fashion; their cumulative gap cost is \(m\) and their final gap is \(1\). Give the exceptional good to the lagging agent, leaving gap \(H-1\), and give the final unit good to the lagging agent, leaving gap \(|H-2|\). This costs
\[
m+(H-1)+|H-2|=m+f(H-1)=m+\max\{1,2H-3\}.
\]
Taking the better construction matches the lower bound. The piecewise formula follows by comparing \(H\) and \(f(H-1)\) on \(H\ge1\).

**6. Sorted greedy.** After \(r\) unit goods, lower-loaded assignment has gap \(0\) for even \(r\), gap \(1\) for odd \(r\), and accumulated cost \(\lceil r/2\rceil\). The final exceptional good contributes respectively \(H\) and \(H-1\). Hence \(G_r(H)=\lfloor r/2\rfloor+H\), and subtraction from the optimum proves the regret law.

## Verification

The standalone file `verify.py` independently minimizes cumulative absolute load differences by an exact integer dynamic program over the number of remaining unit goods, whether the exceptional good remains, and the signed load difference. For every rational \(H\) in a finite test grid, it compares the dynamic-programming optimum with the claimed closed form. It also enumerates every release position and recipient bitstring on smaller instances, independently checks the prefix bound for odd step counts, and computes the ascending greedy policy symbolically as in the proof.

Running `python3 verify.py` from the extracted package gave `VERIFY_OK rational_dp_cases=3186 rational_h_values=177 memo_states=700209 independently_enumerated_cases=48 terminal_prefix_cases=66`. These exhaustive finite checks corroborate, but do not replace, the proof for all real \(H\ge1\) and all positive integers \(r\).

## Relationship to prior work

Goldberg, Robinson, and Teh (2026) introduce the cumulative maximum-envy objective and its freely chosen sequencing variant, establish NP-completeness even with two identical agents, give a universal lower bound, and prove a \(3/2\) approximation for the ascending greedy sequencing algorithm. Their Appendix C.5 already gives the three-good instance \(\{1,1,2\}\) with greedy cost \(3\) and optimal cost \(2\). These facts are not presented as new. The present claim is the exact all-multiplicity, arbitrary-real-exceptional-value phase law and its continuous greedy-regret profile, rather than a new complexity bound or a repetition of the three-good example.

Dobler and Nöllenburg (2025) study minimizing absolute prefix sums when the multiset of signed numbers is specified in advance, including restrictions on the number of positive or negative entries. Their fixed-sign permutation problem is related to this signed-gap objective, but it does not permit choosing the sign of every good independently, so the specific optimal value here is not implied by their stated structural and complexity results. A complete priority claim about all unpublished mathematical work is not made.

## Limitations

The result requires two identically valuing agents, one exceptional good, freely chosen order, and unweighted per-round maximum envy. It does not determine optima for arbitrary multisets of several nonunit goods, fixed or adversarial arrival order, heterogeneous utilities, or discounting. The known \(H=2\) examples and general baseline results are explicitly excluded from originality. Alternative formulations in the broader signed-prefix-sum literature may pose residual priority risk; external independent validation is not supplied.

## References

Goldberg, P. W., Robinson, I., and Teh, N. (2026). *Minimizing Cumulative Envy in Allocating a Sequence of Items*. arXiv:2610.09843v1, first publicly submitted 2026-10-07. Sections 4–5 and Appendix C.5. https://arxiv.org/html/2610.09843v1

Dobler, A., and Nöllenburg, M. (2025). *On Minimizing Wiggle in Stacked Area Charts*. WADS 2025, LIPIcs 349, article 22, Section 3.2. https://doi.org/10.4230/LIPIcs.WADS.2025.22
