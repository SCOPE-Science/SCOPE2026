# Nine repelling rank-two canard-fold networks at molecularity four

## Finding
Fix named chemical species \(\mathrm X\) (fast) and \(\mathrm Y\) (slow). Among all networks consisting of exactly three **distinct directed reactions** between nonnegative two-species complexes of total molecularity at most four, exactly **nine** admit positive rate constants and a positive equilibrium satisfying
\[
f=f_x=h=0,\quad f_{xx}\ne0,\quad f_yh_x<0,\quad \operatorname{rank}\begin{bmatrix}N\\N\circ a\\M\end{bmatrix}=2,\quad h_y>0.
\]
Here \(\dot x=f(x,y)\), \(\dot y=\varepsilon h(x,y)\), \(\varepsilon>0\), \(a\) lists reactant \(\mathrm X\)-orders, and \(N,M\) are the reaction stoichiometric changes. Thus these are *positive-slow-trace geometric canard folds* of rank two, with a repelling (linearly unstable) equilibrium for every \(\varepsilon>0\).

Among the nine, **exactly two** have all reactant molecularities at most three. No qualifying network has all its complexes of molecularity at most three. The nine networks, positive primitive kernel-flux vectors and exact moment signs are listed without quotienting by species exchange, graph isomorphism or other equivalences in `data/repelling_canard_molecularity4.tsv`.

One of the two trimolecular-reactant witnesses is
\[
2\mathrm Y\longrightarrow\mathrm X+3\mathrm Y,\qquad
\mathrm X\longrightarrow0,\qquad
2\mathrm X+\mathrm Y\longrightarrow3\mathrm X.
\]
For arbitrary positive rates \(\alpha,\beta,\gamma\), it has
\[
f=\alpha y^2-\beta x+\gamma x^2y,
\qquad h=\alpha y^2-\gamma x^2y,
\]
and a positive fold equilibrium
\[
y_* =\left(\frac{\beta^2}{4\alpha\gamma}\right)^{1/3},\qquad
x_* =\frac{\beta}{2\gamma y_*}.
\]
Its Jacobian is
\[
J_*=\begin{pmatrix}0&3\alpha y_*\\-\varepsilon\beta&\varepsilon\alpha y_*\end{pmatrix},
\qquad \operatorname{tr}J_*=\varepsilon\alpha y_*>0,\qquad
\det J_*=3\varepsilon\alpha\beta y_*>0.
\]
It is a repelling focus if \(0<\varepsilon<12\beta/(\alpha y_*)\), and has eigenvalues with positive real parts for every \(\varepsilon>0\).

## Assumptions and scope
A complex is a vector \((a,b)\) of nonnegative integers representing \(a\mathrm X+b\mathrm Y\), with molecularity \(a+b\). A directed reaction is an ordered pair of *different* complexes. The network is an **unordered set of exactly three** such reactions, with independent strictly positive mass-action rate constants. There are \(\binom{d+2}{2}\) available complexes and \(\binom{d+2}{2}\bigl(\binom{d+2}{2}-1\bigr)\) directed reactions at molecularity bound \(d\). Distinct reactant complexes are **not** required. Both source and target molecularities obey the degree bound. There are no assumed conservation laws, and \(\varepsilon\) multiplies only the slow equation. All counts distinguish \(\mathrm X\) from \(\mathrm Y\), and the direction of reactions is retained.

The term *geometric canard fold* is the local flux criterion \(f=f_x=h=0\), \(f_{xx}\ne0\), \(f_yh_x<0\) used in the motivating literature. Because the balance matrix has rank two, this fold is structurally fixed rather than transversally unfolded by the rate constants. **No Hopf bifurcation, family of limit cycles, or canard explosion is asserted.** The new classification concerns the sign of the slow trace and its exact minimum molecularity.

## Proof
For reaction \(r\), write the reactant as \((a_r,b_r)\), the product as \((c_r,d_r)\), the stoichiometric changes as \(N_r=c_r-a_r\) and \(M_r=d_r-b_r\), and the positive flux at a point \((x,y)\) as \(v_r=k_rx^{a_r}y^{b_r}\). Then
\[
f=\sum_r N_rv_r,\quad h=\sum_r M_rv_r,\quad
xf_x=\sum_r N_ra_rv_r.
\]
Set \(U=(N_ra_r)_r\) and form the integer balance matrix \(B=[N;U;M]\). Positive fold equilibria require \(Bv=0\) with all \(v_r>0\). Moreover,
\[
x^2f_{xx}=n_{20}=\sum_rN_ra_r(a_r-1)v_r,\quad
y f_y=n_{01}=\sum_rN_rb_rv_r,
\]
\[
x h_x=m_{10}=\sum_rM_ra_rv_r,\quad
y h_y=m_{01}=\sum_rM_rb_rv_r.
\]
The precise fold and Hopf-type sign conditions are \(n_{20}\ne0\) and \(n_{01}m_{10}<0\); slow trace positivity is \(m_{01}>0\). Each sign is unchanged by multiplication of the positive flux vector by a positive scalar.

If \(N\) and \(U\) were dependent, then every positive vector satisfying their null equations would have \(n_{20}=0\): on reactions with \(N_r\ne0\), all active \(a_r\) would have one common value (including the case that \(U=0\)), making \(n_{20}\) a scalar multiple of \(N\cdot v\). Therefore an admissible three-reaction network necessarily has independent \(N,U\). Its nullspace is the line spanned by the exact integer cross product \(w=N\times U\). This line contains a strictly positive vector if and only if all three entries of \(w\) have the same nonzero sign. If this holds, the additional condition \(M\cdot w=0\) is equivalent to \(\operatorname{rank}B=2\). Since \(\operatorname{rank}B\ge2\) is necessary, these conditions exhaust all possibilities. Conversely, any such positive \(v\) is realized at any prescribed \((x,y)>0\) by choosing \(k_r=v_r/(x^{a_r}y^{b_r})\); the signed moments above then give exactly the requested fold conditions.

It remains to evaluate **finite integer tests** on every unordered three-element subset of the directed reactions. The self-contained standard-library Python file `computations/check_repelling_canard.py` implements the cross product and integer moments directly; there are no numerical tolerances or sampling decisions. In the four-molecularity universe this checks precisely \(\binom{210}{3}=1{,}521{,}520\) distinct networks. The exhaustive counts are:

| Maximal complex molecularity | Rank-two, positive-null triples | Geometric canard-fold triples | Negative slow trace | Zero slow trace | Positive slow trace |
|---|---:|---:|---:|---:|---:|
| 2 | 0 | 0 | 0 | 0 | 0 |
| 3 | 82 | 16 | 11 | 5 | 0 |
| 4 | 1590 | 350 | 278 | 63 | **9** |

The full nine-row output is `data/repelling_canard_molecularity4.tsv`; exactly rows 4 and 5 have source degree at most three. Every row specifies the three distinct reactions by the machine notation `a:b>c:d`, the positive integer kernel flux \((v_1,v_2,v_3)\), and the four integral moments \((n_{20},n_{01},m_{10},m_{01})\). The script both generates this table and asserts these complete counts. These exhaustive finite tests are a proof because the cross-product reduction gives necessary and sufficient conditions for **each** possible reaction set, and the loops cover every such set once.

For the displayed network, the equations give \(h=f-xf_x\). Solving \(h=f_x=0\) produces the stated unique positive \((x_*,y_*)\), where \(f=0\). Direct differentiation yields \(f_{xx}=2\gamma y_*>0\), \(f_y=3\alpha y_*>0\), \(h_x=-\beta<0\), \(h_y=\alpha y_*>0\), proving the strict conditions without relying on enumeration. Its Jacobian has positive trace and determinant, hence both eigenvalues have positive real parts. The discriminant is \(\varepsilon\alpha y_*(\varepsilon\alpha y_*-12\beta)\), proving the focus range.

## Verification
Run `python3 computations/check_repelling_canard.py` using Python's standard library. The program checks the complete cases of maximal complex molecularity two, three and four, emits the exact nine-row TSV in its own `computations` directory if that directory is writable, and terminates with the explicit `PASS` message if all counts and the displayed witness agree. The archived table is in `data/repelling_canard_molecularity4.tsv`; its numeric entries were compared exactly to the checker output. The direct symbolic witness proof above stands separately from the exhaustive combinatorial classification.

## Relationship to prior work
Beldiman and Halanay, arXiv:2610.27188v1 (first publicly available 19 October 2026), establish the general flux criterion and classify minimal canard networks for total complex molecularity at most three. Their Section 3 shows that a rank-two admissible fold has Jacobian trace \(\varepsilon m_{01}/y\), and their Section 8 reports 16 three-reaction rank-two canard networks, none having positive trace. **Those structural criteria and the degree-three exclusion are prior results, not claimed as new.** The finding here is the exact degree-four extension: nine distinct positively traced networks, including the complete list and the sharp first-degree witness.

Banaji, Boros and Hofbauer (arXiv:2304.02303) classify three-reaction quadratic-sourced mass-action systems admitting Hopf bifurcations, with a different result on fourth-order product complexes. Their Hopf and isolated-periodic-orbit statements do not imply the rank-two, positive-slow-trace codimension-zero fold classification here; in particular the displayed witness has a degree-three reactant and asserts no Hopf bifurcation. Banaji (arXiv:2609.07265v1) establishes broad dual-equation tools for fold/cusp bifurcations, not the present slow-fast rank-two degree-four sign census. Prior published findings on fold/multistationarity of three-species networks and on onset orders of reaction-diffusion networks concern different objects and parameters.

## Limitations
The count nine is **labelled reaction-set counting**, not a count of dynamical equivalence classes; it does not classify four-reaction systems, rank-three unfolding canards, higher molecularities, or limit cycles. The fold is codimension zero within the stipulated mass-action architecture. The existence of a repelling equilibrium is not the existence of a Hopf bifurcation or canard explosion. The complete enumeration is exact finite arithmetic but has not received independent audit. The exact number nine is supported by the supplied self-contained checker, not a separate hand enumeration. Historical-priority comparison cannot rule out every unpublished or differently indexed degree-four census.

## References
1. M.-M. Beldiman and A.-D. Halanay, *Canard points in planar mass-action networks: a flux criterion, a duality, and a complete classification*, arXiv:2610.27188v1, 19 October 2026; https://arxiv.org/html/2610.27188v1 . Sections 3, 8 and 9.
2. M. Banaji, B. Boros and J. Hofbauer, *Oscillations in three-reaction quadratic mass-action systems*, arXiv:2304.02303, 2023; https://arxiv.org/abs/2304.02303 .
3. M. Banaji, *On the computation of fold and cusp bifurcations in mass action networks via dual equations*, arXiv:2609.07265v1, 7 September 2026; https://arxiv.org/html/2609.07265v1 .
4. M. Banaji, B. Boros and J. Hofbauer, *Bifurcations in planar, quadratic mass-action networks with few reactions and low molecularity*, *Nonlinear Dynamics* (2024); https://doi.org/10.1007/s11071-024-10068-1 .
