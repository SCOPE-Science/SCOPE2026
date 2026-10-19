# The one-exception law for resistance-diameter-optimal spider trees under power-law conductance costs

## Finding
Let a spider tree have \(k\ge3\) nonempty arms, all attached at a single hub. Give every edge \(e\) an independent strictly positive conductance \(w_e\) and a fixed positive price coefficient \(c_e\). For every exponent \(\alpha>0\) and every budget \(B>0\), minimize the resistance diameter
\[
\mathcal D(w)=\max_{u,v}R_{\mathrm{eff}}(u,v),
\qquad \sum_e c_e w_e^\alpha=B.
\]
The optimum exists and is **unique over all independently chosen edge conductances**, including for \(0<\alpha<1\), when the cost as a function of conductance is concave.

For arm \(i\), define its price aggregate
\[
S_i=\sum_{e\in E_i}c_e^{1/(\alpha+1)},\qquad
C_i=S_i^{\alpha+1},\qquad C=\sum_{i=1}^k C_i.
\]
There are exactly two regimes.

**Balanced regime**: If \(2\max_i C_i\le C\), define \(F=2^\alpha C\) and \(\rho_i=1/2\) for every arm.

**Single-dominant-arm regime**: If \(2C_j>C\) for one index \(j\), necessarily unique, put
\[
U=C_j^{1/(\alpha+1)},\qquad
V=(C-C_j)^{1/(\alpha+1)},\qquad
F=(U+V)^{\alpha+1},
\]
and set \(\rho_j=U/(U+V)\) and \(\rho_i=V/(U+V)\) for all \(i\ne j\).

In either regime, the exact optimal resistance diameter, total resistance from the hub to each arm leaf, and every optimal individual conductance are respectively
\[
\boxed{\mathcal D_*=(F/B)^{1/\alpha}},\qquad
\boxed{R_i^*=\rho_i\mathcal D_*},\qquad
\boxed{w_e^*=\frac{S_i}{R_i^*}\,c_e^{-1/(\alpha+1)}}
\quad(e\in E_i).
\]
Thus **at most one arm has a different optimal hub-to-leaf resistance**, even when every individual edge price is different. The support boundary is the sharp price-aggregate equality \(C_j=\sum_{i\ne j}C_i\); at equality the balanced solution is still uniquely optimal.

For unit-price edges and arm lengths \((3,2,2)\), the exponent alone crosses a nontrivial transition at
\[
\boxed{\alpha_c=\frac{\log2}{\log(3/2)}-1=0.709511\ldots}.
\]
For \(0<\alpha\le\alpha_c\) all three optimal radial resistances agree; for \(\alpha>\alpha_c\) the three-edge arm has strictly larger optimal resistance, and the two other radii still agree. For any unit-price spider with a **unique longest arm**, the same comparison is monotone in \(\alpha\): a unique positive transition exists precisely when the sum of all other arm lengths exceeds the longest length; if the sum is at most that length, the longest arm dominates for every \(\alpha>0\).

## Assumptions and scope
The tree is finite and simple, with a single central vertex incident to \(k\ge3\) internally disjoint paths, each having at least one edge. The edge prices \(c_e\), exponent \(\alpha\), and budget \(B\) are strictly positive real numbers. The optimization is over every individual edge conductance, not just arm-constant choices. As a tree, it must retain all positive-conductance edges to have finite resistance diameter. Resistance is defined by the electrical unit-current law; for a tree it equals the sum of reciprocal conductances along the unique path. The largest pairwise effective resistance is taken over **all vertices**, not just selected terminals.

## Proof
**1. Reduction to leaf radii.** Define \(r_e=1/w_e>0\) and the hub-to-leaf resistance \(R_i=\sum_{e\in E_i}r_e\). Every same-arm vertex pair has effective resistance at most \(R_i\); any cross-arm vertex pair has resistance at most \(R_i+R_j\), and equality is attained by the two corresponding leaves. Therefore
\[
\mathcal D(w)=\max_{1\le i<j\le k}(R_i+R_j).
\]
Because at least two arms are nonempty, these cross-arm leaf distances dominate all within-arm distances.

**2. Unrestricted optimal allocation inside each arm.** For prescribed \(R_i>0\), the expenditure on arm \(i\) is
\[
\sum_{e\in E_i}c_e r_e^{-\alpha}\quad\text{subject to}\quad
\sum_{e\in E_i}r_e=R_i.
\]
Every summand has strictly positive second derivative \(\alpha(\alpha+1)c_er_e^{-\alpha-2}\), so this constrained problem has one minimizer. Its Lagrange equation \(-\alpha c_e r_e^{-\alpha-1}=\lambda\) gives
\[
r_e=\frac{R_i}{S_i}c_e^{1/(\alpha+1)},
\qquad
\min\sum_{e\in E_i}c_e r_e^{-\alpha}=\frac{C_i}{R_i^\alpha}.
\]
In particular, the stated per-edge solution is the **unique** cheapest way of realizing each vector of arm radii. No assumption about within-arm symmetry was made.

**3. A normalized strictly convex minimax problem.** Fix a proposed diameter \(d>0\) and write \(R_i=d\rho_i\). The minimum total expenditure possible at diameter at most \(d\) equals \(d^{-\alpha}F\), where
\[
F=\min_{\rho_i>0,\ \rho_i+\rho_j\le1\ (i<j)}
\sum_{i=1}^k\frac{C_i}{\rho_i^\alpha}.
\]
This is a strictly convex objective on a convex polytope, with divergence at every coordinate-zero boundary. Hence a minimizing radius vector exists and is unique. Because the objective strictly decreases in each coordinate, at least one pairwise constraint is tight.

If all \(\rho_i\le1/2\), replacing them all by \(1/2\) preserves every constraint and strictly decreases the objective unless they already all equal \(1/2\). The balanced candidate has cost \(F_{\mathrm{bal}}=2^\alpha C\).

Otherwise one coordinate \(\rho_j=t>1/2\) is the unique largest. All others obey \(\rho_i\le1-t\) from their constraint with \(j\). At fixed \(t\), setting **every** other coordinate to \(1-t\) is feasible, since \(2(1-t)<1\), and uniquely minimizes the objective. Thus this entire regime reduces, without loss or symmetry assumptions, to
\[
\Phi_j(t)=\frac{C_j}{t^\alpha}
+\frac{C-C_j}{(1-t)^\alpha},\qquad \frac12<t<1.
\]
The function \(\Phi_j\) is strictly convex; its derivative at \(1/2\) has the sign of \(C-2C_j\), and it tends to infinity as \(t\uparrow1\). If \(2C_j\le C\), it cannot improve on the boundary value \(2^\alpha C\). If \(2C_j>C\), it has precisely one interior minimizer, characterized by
\[
\left(\frac{t}{1-t}\right)^{\alpha+1}=
\frac{C_j}{C-C_j},
\quad t=\frac{U}{U+V};\qquad
\Phi_j(t)=(U+V)^{\alpha+1}.
\]
At most one index satisfies \(2C_j>C\), because all \(C_i\) are positive. Thus the formulas give the unique global normalized solution in every case, including the boundary equality.

**4. Budget and uniqueness.** The minimum cost at diameter at most \(d\) is \(F/d^\alpha\). Budget \(B\) therefore forces \(d\ge(F/B)^{1/\alpha}\), with equality realized by the stated vector of radii and its unique within-arm allocation. Combining strict uniqueness in steps 2 and 3 proves uniqueness of every edge conductance, even where the original conductance-price functional \(w\mapsto c_ew^\alpha\) is concave.

**5. Exponent transition.** For unit edge prices and arm lengths \(\ell_i\), the price aggregates are \(C_i=\ell_i^{\alpha+1}\). In the case \((3,2,2)\), the dominance boundary reads \(3^{\alpha+1}=2\,2^{\alpha+1}\), giving the displayed \(\alpha_c\). With a unique longest length \(L\), the ratio of other-arm cost to longest-arm cost is \(\sum_{i\ne j}(\ell_i/L)^{\alpha+1}\), a strictly decreasing function of \(\alpha>0\) tending to zero. Its limit as \(\alpha\downarrow0\) is \((\sum_{i\ne j}\ell_i)/L\), proving the remaining classification.

## Verification
The included `verify_spider.py` is a standalone Python 3 script using NumPy and SciPy. Running `python verify_spider.py` completed **1,256 assertions**. Tests cover five exponents (including concave pricing), 80 reproducibly generated heterogeneous spiders with 3–6 arms, checks that budgets bind, direct Laplacian-pseudoinverse resistance diameters, 960 feasible randomized competitor allocations, independent numerical convex optimization on arm resistances for 18 cases, special rational-input closed-form comparisons, and the exponent transition. Machine precision and nonlinear-solver tolerances are specified in the source code. Finite numerical checks do **not** establish the infinite-parameter theorem; steps 1–5 provide the proof.

## Relationship to prior work
Ghosh, Boyd, and Saberi (2006; extended 2008) establish the general effective-resistance network-design framework. Their proceedings paper explicitly observes that minimizing the **maximum** pairwise effective resistance is a convex problem for a **linear conductance budget** and admits an SDP formulation; their analytical tree calculation instead optimizes **total** pairwise resistance. The present result neither introduces the minimax objective nor claims the convex-program formulation as new. The asserted contribution is the closed-form, all-parameter **global optimizer classification** on arbitrarily priced spider trees under nonlinear power-law conductance budgets, including the sharp one-exception support geometry and the exponent-induced structural transition.

Chepoi, Noltemeier, and Vaxès study the diameter of trees under **linear costs for reductions of bounded pre-existing edge lengths**, a distinct feasible-cost model; their explicit linear-program constraints were inspected in the accessible author-uploaded full text. Hambrusch and Lim also study edge-reduction algorithms on trees. Abstract-level descriptions indicate a different model; the full Hambrusch–Lim paper was not available for decisive whole-paper comparison. A general theorem in that literature permitting precisely reciprocal-conductance power-law costs could subsume part of the present claim; none was verified. Searches of relevant indexed records and semantic findings did not reveal the same exact spider classification, but absence from search results is not proof of novelty.

## Limitations
The theorem applies to fixed spider-tree topology and power-law per-conductance prices; it does not classify arbitrary trees, cyclic networks, multiple objectives, or discrete edge purchases. The optimization is mathematical and does not model limits on maximum conductance or engineering reliability. A differently worded specialization of general tree-diameter upgrading literature or other unindexed work could cover the result. These comparisons are not independent scholarly review or external certification. All exact mathematical claims above follow from the included proof; numerical experiments alone are insufficient.

## References
1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of the 17th International Symposium on Mathematical Theory of Networks and Systems, Kyoto, July 24–28, 2006. https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf (proceedings first-public evidence).
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review **50** (2008), 37–66. DOI: 10.1137/050645452. https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf (sections 2.3, 5.1, and 8).
3. V. Chepoi, H. Noltemeier, and Y. Vaxès, *Upgrading Trees Under Diameter and Budget Constraints*, Networks **41** (2003), 24–35. DOI: 10.1002/net.10055 (publisher abstract accessible).
4. S. E. Hambrusch and H.-S. Lim, *Minimizing the Diameter in Tree Networks Under Edge Reductions*, Parallel Processing Letters **9** (1999), 361–371. DOI: 10.1142/S0129626499000335 (abstract accessible; full-text comparison unresolved).
