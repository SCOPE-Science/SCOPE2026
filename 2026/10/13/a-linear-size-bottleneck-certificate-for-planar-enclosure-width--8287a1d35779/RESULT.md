# A linear-size bottleneck certificate for planar enclosure width

## Finding

Let \(L,U\subset\mathbb R^2\) be finite sets and define the order enclosure
\[
E(L,U)=(L+\mathbb R^2_+)\cap(U-\mathbb R^2_+),
\qquad \mathbb R^2_+=[0,\infty)^2.
\]
The width of a nonempty enclosure is
\[
w(E)=\max_{\substack{\ell\in L,\;u\in U\\\ell\leq u}}
\min\{u_1-\ell_1,\;u_2-\ell_2\}.
\]
There is an exact deterministic algorithm that returns this width and an attaining pair \((\ell,u)\), or correctly reports that \(E\) is empty. For arbitrary finite inputs of cardinalities \(n\) and \(m\), it uses \(O((n+m)\log(n+m))\) comparisons and \(O(n+m)\) storage. Given the lower minimal front and upper maximal front already sorted by their first coordinates, it needs only \(O(n+m)\) time, and examines at most twice as many candidate pairs as there are lower-front vertices. Both algorithms work at zero width and with repeated input coordinates.

More precisely, list the fronts as
\[
L_* =\{(a_i,b_i):1\leq i\leq r\},\qquad
U_* =\{(c_j,d_j):1\leq j\leq s\}
\]
with increasing first coordinates. The respective second coordinates decrease strictly. Set
\[
\tau_i=a_i-b_i,\qquad\delta_j=c_j-d_j,\qquad
k_i=\min\{j:\delta_j\geq\tau_i\},
\]
where \(k_i=s+1\) if the last set is empty. Then the exact signed maximum over all input pairs is
\[
Q=\max_{1\leq i\leq r}\ \max_{j\in\{k_i-1,k_i\}\cap\{1,\ldots,s\}}
\min\{c_j-a_i,d_j-b_i\}.
\]
The enclosure is nonempty exactly when \(Q\geq0\), in which case \(w(E)=Q\). For either empty input set, the enclosure is empty. The indices \(k_i\) are nondecreasing and can all be found with one forward scan.

## Assumptions and scope

All coordinates are finite real numbers with exact order and arithmetic comparisons; dimensions are exactly two. The two input sets are finite and may be empty or contain duplicates, ties, dominated points, and incomparable points. The coordinatewise order \(\ell\leq u\) includes equality. An empty enclosure is reported separately rather than assigned a nonnegative width. The linear-time bound applies to inputs supplied as already sorted, undominated fronts; preprocessing arbitrary points requires sorting. No floating-point error guarantee is asserted.

## Proof

**1. The pairwise width identity.** Define width equivalently as
\[
\sup\{t\geq0:\exists z\in\mathbb R^2\text{ with }z,z+t(1,1)\in E(L,U)\}.
\]
If a feasible \((z,t)\) exists, membership of \(z\) in \(L+\mathbb R^2_+\) gives \(\ell\in L\) with \(\ell\leq z\), and membership of \(z+t(1,1)\) in \(U-\mathbb R^2_+\) gives \(u\in U\) with \(z+t(1,1)\leq u\). Therefore \(t\leq\min\{u_1-\ell_1,u_2-\ell_2\}\). Conversely, for any \(\ell\leq u\) choose \(z=\ell\) and any \(0\leq t\leq\min_j(u_j-\ell_j)\); both diagonal endpoints belong to the box \([\ell,u]\subseteq E\). Thus the width is the maximum over feasible pairs, and \(E\ne\varnothing\) exactly when some pair has nonnegative bottleneck score. Finiteness makes every nonempty maximum attained.

**2. Frontier reduction.** If \(\ell'\leq\ell\) in \(L\), then for every \(u\) the score associated with \((\ell',u)\) is no smaller than that of \((\ell,u)\). Likewise, if \(u'\geq u\) in \(U\), replacing \(u\) by \(u'\) cannot decrease the score. Repeatedly discarding dominated lower points and dominated upper points therefore preserves both the signed maximum and every feasibility conclusion. Sorting \(L\) by first then second coordinate in ascending order and retaining a point exactly when its second coordinate is smaller than all previously retained second coordinates produces \(L_*\). Sorting \(U\) in descending lexicographic order and retaining a point exactly when its second coordinate is larger than all previously retained coordinates produces \(U_*\), which is then reversed. These scans prove the asserted preprocessing bound and the strict antichain order properties.

**3. Two-candidate reduction.** Fix \((a_i,b_i)\). Since \(c_j\) increases and \(d_j\) decreases with \(j\), the first coordinate gap \(c_j-a_i\) increases while the second gap \(d_j-b_i\) decreases. The first is no larger than the second precisely when \(\delta_j\leq\tau_i\). Hence
\[
\min\{c_j-a_i,d_j-b_i\}=
\begin{cases}
c_j-a_i,&\delta_j<\tau_i,\\
d_j-b_i,&\delta_j\geq\tau_i,
\end{cases}
\]
where at equality the branches coincide. The score therefore increases strictly before \(k_i\) and decreases strictly from \(k_i\) onward. Its maximum occurs at one of the two bracketing indices \(k_i-1,k_i\) that actually exist. At a boundary crossing, one index suffices. No other upper point can improve that fixed lower point's bottleneck score.

**4. Monotone merge and costs.** Along \(L_*\), \(a_i\) increases and \(b_i\) decreases, so \(\tau_i\) increases. Along \(U_*\), \(\delta_j\) increases. The crossing index \(k_i\) is consequently nondecreasing. A pointer over the ordered upper front makes at most \(s\) forward moves, while each of the \(r\) lower points causes at most two constant-cost score evaluations. This proves the linear sweep and the size bound for the candidate certificate. The maximal candidate's original coordinate pair is an exact witness if its score is nonnegative; if the maximum score is negative, the enclosure is empty by step 1.

Both sides of the bracket can be essential. With \(L=\{(0,0)\}\) and \(U=\{(5,6),(10,0)\}\), the predecessor has score \(5\) and the successor has score \(0\). With \(U=\{(0,10),(9,1)\}\), the predecessor instead has score \(0\) and the successor score \(1\).

## Verification

The standalone `verify_width.py` implements the two front scans and the monotone merge, compares them with direct all-pairs enumeration, and checks that each claimed witness is feasible and attains the returned score. Running `python3 verify_width.py` with only Python's standard library returned:

```text
VERIFY_OK 16900 exhaustive subset pairs, 96000 random integer pairs, 1500 rational pairs
```

The exhaustive cases range over all subsets of cardinality at most three of the nine-point integer grid with coordinates in \(\{-1,0,1\}\). Random tests include duplicated points and order ties; rational tests use exact `Fraction` arithmetic. The formal proof in the preceding section, not those finite tests, establishes the claim for all finite real inputs.

## Relationship to prior work

Eichfelder and Hoff (first publicly posted September 5, 2025) use enclosure width to assess approximations of multiobjective optimal sets and give the bottleneck pair formula in their equations (3.3)–(3.5), drawing on the 2021 work of Eichfelder, Kirst, Meng, and Stein. The 2025 paper's Proposition 3.2 also allows replacing bounding sets by their minimal and maximal sets. These are **known premises**, not claimed as new.

The additional result here is a planar candidate-sparsification theorem: for *each* lower-front vertex only the two upper-front vertices bracketing one scalar diagonal difference can be optimal, and those brackets move monotonically as the lower front is scanned. This produces a certified exact linear-time evaluation from sorted fronts, rather than the quadratic all-pairs evaluation of the published width formula. Other enclosure algorithms use this width as a stopping criterion; the present result supplies a dimension-specific computational primitive, not a new convergence theorem. The published papers and related algorithms inspected did not state this exact candidate-reduction and merge complexity, but unindexed implementations or equivalent results remain a possible prior-art risk.

## Limitations

The result is for finite, planar point sets and exact input arithmetic. It neither proves a linear-time method in three or more objective dimensions nor avoids the sorting cost for arbitrary inputs. It gives no guarantee about convergence, practical wall-clock speed for a complete optimization solver, or the validity of a bounding enclosure for a particular optimization problem. The theory does not establish uniqueness of optimal witnesses, and a failed literature search is not proof of absolute novelty.

## References

1. G. Eichfelder and D. Hoff, *Properties of Enclosures in Multiobjective Optimization*, first posted 2025-09-05, revised 2026, *EURO Journal on Computational Optimization* 14 (2026), 100127, DOI: 10.1016/j.ejco.2026.100127. Original public posting: https://optimization-online.org/2025/09/properties-of-enclosures-in-multiobjective-optimization/ ; openly available manuscript: https://optimization-online.org/wp-content/uploads/2025/09/Properties_of_Enclosures_in_Multiobjective_Optimization-1.pdf . Relevant: Proposition 3.2 and equations (3.3)–(3.5).
2. G. Eichfelder, P. Kirst, L. Meng, O. Stein, *A general branch-and-bound framework for continuous global multiobjective optimization*, *Journal of Global Optimization* 80 (2021), 195–227, DOI: 10.1007/s10898-020-00984-y. Relevant: Lemmas 3.2–3.3 and width-based stopping rules. https://link.springer.com/article/10.1007/s10898-020-00984-y .
3. G. Eichfelder, M. Link, S. Volkwein, L. Warnow, *An adaptive relaxation-refinement scheme for multi-objective mixed-integer nonconvex optimization*, *Mathematical Programming Computation* (2025), DOI: 10.1007/s12532-025-00299-7. Relevant: enclosure-width tolerance as a termination objective. https://link.springer.com/article/10.1007/s12532-025-00299-7 .
4. *Using dual relaxations in multiobjective mixed-integer convex quadratic programming*, *Journal of Global Optimization* (2024), DOI: 10.1007/s10898-024-01440-x. Relevant: explicit pairwise bottleneck expression for finite bound sets. https://doi.org/10.1007/s10898-024-01440-x .
