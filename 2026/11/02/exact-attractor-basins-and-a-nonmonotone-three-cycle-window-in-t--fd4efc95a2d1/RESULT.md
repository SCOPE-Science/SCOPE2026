# Exact attractor basins and a nonmonotone three-cycle window in threshold-two cyclic automata on bicliques

## Finding

Consider the synchronous three-color cyclic cellular automaton on the labelled complete bipartite graph \(K_{a,b}\), with integers \(a,b\ge 2\) and threshold two. Every initial state enters a periodic orbit in at most three synchronous updates, and its eventual least period belongs to \(\{1,3,4\}\). This three-step bound is sharp exactly when \(\max(a,b)\ge4\). In particular, the global update map satisfies \(F^{15}=F^3\).

Define, for integers \(n\ge0\),
\[
\begin{aligned}
J_n&=\sum_{r=2}^{n-2}\binom nr \quad(\text{empty sums are zero}),\\
H_n&=\sum_{\substack{i+j+k=n\\i,j,k\ge2}}\frac{n!}{i!j!k!},\\
U_n&=\begin{cases}3,&n=1,\\6,&n=2,3,\\0,&\text{otherwise},\end{cases}\\
K_n&=J_n+nJ_{n-1},\\
L_n&=\begin{cases}n(n-1),&n\ge4,\\0,&n<4.\end{cases}
\end{aligned}
\]
Here \(J_n=2^n-2n-2\) when \(n\ge4\). Let \(B_d(a,b)\) count labelled initial configurations whose eventual least period is \(d\). Then
\[
\boxed{B_3(a,b)=H_aH_b+H_aU_b+U_aH_b}
\]
and
\[
\boxed{\begin{aligned}
B_4(a,b)={}&3H_aK_b+3K_aH_b+6K_aK_b\\
&+3K_aL_b+3L_aK_b.
\end{aligned}}
\]
The remaining states converge to fixed points:
\[
\boxed{B_1(a,b)=3^{a+b}-B_3(a,b)-B_4(a,b).}
\]
All eventual period-three configurations are already periodic at time zero. Exactly \(6J_aJ_b\) labelled configurations are periodic of least period four at time zero; the number of distinct primitive three- and four-cycle orbits is, respectively,
\[
\boxed{C_3(a,b)=B_3(a,b)/3,\qquad C_4(a,b)=3J_aJ_b/2.}
\]
For period four, the numbers entering at times zero and two are respectively
\[
B_{4,0}=6J_aJ_b,\qquad
B_{4,2}=3\bigl(H_a bJ_{b-1}+aJ_{a-1}H_b\bigr),
\]
and the time-one layer equals \(B_4-B_{4,0}-B_{4,2}\).

A primitive three-cycle exists if and only if both shores have at least six vertices, or one shore has at least six and the other has size two or three. In contrast, a primitive four-cycle exists exactly when both shores have at least four vertices. Thus, with one shore fixed at size six, three-cycles exist when the other shore has size two, disappear at sizes four and five, and reappear at size six. When both shore sizes tend to infinity, the probability of eventual period three under the uniform product initial coloring tends to one.

## Assumptions and scope

The vertex colors lie in \(\mathbb Z/3\mathbb Z\). A vertex currently of color \(c\) advances to \(c+1\pmod3\) if at least **two distinct neighbors** currently have color \(c+1\), and otherwise retains color \(c\). Updates on both shores are simultaneous. No within-shore edges exist. The initial configurations are labelled: any assignment of a color to each of the \(a+b\) distinct vertices is counted separately. The first periodic-entry time is the smallest nonnegative integer \(t\) such that \(F^t(x)\) belongs to a periodic orbit. Both parameters are arbitrary integers at least two; the proof does not assume equal shore sizes.

The model is cyclic cellular automaton, **not** Greenberg–Hastings: all three colors use the neighbor threshold at every update, rather than automatically advancing in refractory states. Threshold one is also a different map.

## Proof

**1. Finite, exact representation.** Partition each shore into three cohorts according to each vertex's *initial* color. Vertices in one cohort have identical future colors, by induction: their neighbor sets are identical, they start equal, and the synchronous rule preserves equality. A cohort never splits. Replace its cardinality \(r\) by the capped size \(\min(r,2)\), represented by that many labelled vertices. This replacement preserves the entire sequence of color decisions: at any time, a color class is a union of whole initial cohorts, and its size reaches the threshold two if and only if the sum of the capped cohort sizes reaches two. Hence the capped representative and the original configuration have precisely the same cohort-color histories and therefore the same first periodic-entry time and least period.

There are \(3^3-1=26\) nonempty triples of capped cohort sizes per shore, giving \(26^2=676\) representative pairs. On a representative with left color sequence \(x\) and right color sequence \(y\), the exact update is
\[
x'_i=\begin{cases}x_i+1\pmod3,&\#\{j:y_j=x_i+1\pmod3\}\ge2,\\x_i,&\text{otherwise},\end{cases}
\]
with the symmetric rule for \(y'_j\), evaluating both right-hand sides from the same old state. Exhaustive evaluation of the 676 small representatives, with cycle detection on full labelled representative colors, gives the following exact numbers of capped pairs classified by first entry \(t\) and least period \(d\):

| First entry \(t\) | Period 1 | Period 3 | Period 4 |
|---:|---:|---:|---:|
| 0 | 145 | 15 | 6 |
| 1 | 171 | 0 | 36 |
| 2 | 225 | 0 | 6 |
| 3 | 72 | 0 | 0 |

All 676 cases are enumerated and independently checked in `verify_symbolic.py`; the code is an exhaustive **finite** lemma, not a numerical extrapolation across graph sizes. There are explicit entry-three representatives for **every** pair with the second shore of size at least four: take right capped cohorts \((2,0,2)\) and left capped cohorts \((0,1,1)\) when the left shore has size two, or \((1,2,0)\) when it has size at least three. The underlying uncapped sizes can be chosen accordingly (the cohorts capped at two receive all extra vertices). Symmetry covers the reversed orientation. No entry-three representative is realizable when both shores have at most three vertices. This proves the global cutoff, its sharpness, and the permitted periods.

**2. Exact infinite-family basin counts.** Introduce formal symbols \(X,Y,Z,W\) for cohort weights. On the first shore, a cohort with capped multiplicity zero, one or two contributes, respectively, \(1\), \(Z\), or \(X\); on the second shore the weights are \(1,W,Y\). For a capped triple, multiply its three weights. Summing such monomials over the 676 signatures and selecting eventual period three gives the **formal polynomial identity**
\[
P_3(X,Y,Z,W)=X^3Y^3+X^3\bigl((1+W)^3-1\bigr)+Y^3\bigl((1+Z)^3-1\bigr).
\]
Selecting eventual period four gives
\[
\begin{aligned}
P_4(X,Y,Z,W)={}&3X^3Y^2(1+W)+3X^2(1+Z)Y^3\\
&+6X^2(1+Z)Y^2(1+W)\\
&+3X^2(1+Z)W^2Y+3Z^2XY^2(1+W).
\end{aligned}
\]
These are identities of ordinary polynomials with **integer coefficients**; the exact checker constructs both independently from all 676 representatives and compares every coefficient. For periodic states of period four, the polynomial is exactly \(6X^2Y^2\); the period-three periodic-state polynomial is all of \(P_3\).

To pass from those polynomial identities to labelled-state counts for **every** \(a,b\), use exponential generating functions in the shore-size indeterminates \(z,w\): a cohort having at least two vertices has weight \(e^z-1-z\), a singleton has weight \(z\), and an empty cohort has weight \(1\) (similarly with \(w\)). Substitute
\[
X=e^z-1-z,\quad Y=e^w-1-w,\quad Z=z,\quad W=w.
\]
The coefficient \(a!b![z^aw^b]\) counts exactly the labelled configurations on \(K_{a,b}\). We have
\[
\begin{array}{c|ccccc}
\text{EGF term}&X^2&X^3&(1+z)^3-1&X^2(1+z)&z^2X\\\hline
n![z^n](\cdot)&J_n&H_n&U_n&K_n&L_n
\end{array}
\]
for \(n\ge2\) (the value of \(U_1\) is included for use in the definition). Extracting coefficients of \(P_3\) and \(P_4\) yields the stated formulas. Subtraction from \(3^{a+b}\) gives \(B_1\). Because all period-three states enter at time zero, and the exact period-four periodic polynomial is \(6X^2Y^2\), division by the primitive periods gives the orbit counts. Selecting first-entry zero or two from the same classification proves the finer layer formulas.

**3. Existence and asymptotics.** The coefficient counts \(J_n\) and \(K_n\) are strictly positive precisely when \(n\ge4\); \(H_n>0\) precisely when \(n\ge6\), and \(U_n>0\) for \(n=2,3\) within the stated domain. The three-cycle and four-cycle existence characterizations follow directly. Under uniform random independent initial colors, \(H_n/3^n\) is the probability that all three initial colors occur at least twice in a shore of size \(n\). This probability tends to one exponentially (by a union bound on deficient color classes). Since \(B_3(a,b)\ge H_aH_b\) and the total is \(3^{a+b}\), its attraction probability tends to one when both sizes diverge.

## Verification

`verify_symbolic.py` is a self-contained Python 3 program using only the standard library. It constructs the 676 exact capped representative pairs, detects their actual periodic orbits, verifies the complete \((t,d)\) histogram, compares the **formal four-indeterminate polynomials coefficient by coefficient** (not merely at sampled sizes), and evaluates the resulting exact formula for all 121 integer pairs with \(2\le a,b\le12\). Its execution output is `symbolic_results.txt`.

`verify_direct.cpp` independently implements the full, labelled vertex-by-vertex rule (without cohort reduction). Compiled as `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct`, it exhaustively evolves all \(1,185,921\) labelled configurations across the 25 size pairs \(2\le a,b\le6\), checking the predicted eventual-period totals, universal first-entry bound, and selected individual transient layers. Its output is `direct_results.txt`. Both programs were executed successfully. The finite direct enumeration corroborates the exact finite-quotient and generating-polynomial proof; it is not offered as an infinite proof on its own.

## Relationship to prior work

Fisch, Gravner and Griffeath introduced and investigated cyclic contact-update rules with threshold and range parameters, primarily in lattice geometries; the later public arXiv version provides a day-verified citation. Gravner, Lyu and Sivakoff established powerful arbitrary-graph dynamics criteria for the **threshold-one** three-color CCA and GHM, based on an excitation-maximum representation; their threshold-one results do not include the threshold-two transition map here. Bello and Sivakoff analyzed contact thresholds at least two on **infinite regular trees**, again without a complete finite-biclique basin census.

The exact three-step cutoff, the all-size individual eventual-period basin formulas, and the nonmonotone three-cycle size window are the subject of the present result. The corresponding threshold-two GHM has a distinct local transition rule; its known biclique period formulas neither imply nor equal this cyclic automaton's formulas. Likewise, classifications for threshold-one CCA on bicliques and complete multipartite graphs do not control the threshold-two case.

## Limitations

The results concern only complete bipartite graphs with both sides at least two, three colors, synchronous updates, and contact threshold two. No assertion is made about arbitrary graphs, asynchronous updates, additional colors, or other thresholds. The first-entry-period basin formulas do not classify individual attraction basins of *specific* fixed configurations. The full-size theorem depends on the auditable 676-case finite lemma and its formal coefficient check; the labelled brute-force checks cover only sizes at most six. Searches of indexed literature cannot exclude equivalent results in uncatalogued or inaccessible prior work. Independent scientific review has not been undertaken.

The motivating model was published in a 1991 journal article, for which a precise public-release day was not verified here. The cited 1993-04-02 arXiv posting is the earliest verified **day-specific public source date** used in this record, not a claim that the model originated in 1993.

## References

1. R. Fisch, J. Gravner and D. Griffeath, “Threshold-range scaling of excitable cellular automata,” *Statistics and Computing* **1** (1991), 23–39, DOI: 10.1007/BF01890834. Public arXiv posting: `patt-sol/9304001`, April 2, 1993. Full-text archive: https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf.
2. J. Gravner, H. Lyu and D. Sivakoff, “Limiting behavior of 3-color excitable media on arbitrary graphs,” *Annals of Applied Probability* **28** (2018), 3324–3357, DOI: 10.1214/17-AAP1350, arXiv:1610.07320. Full text: https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf.
3. J. Bello and D. Sivakoff, “Cyclic Cellular Automata and Greenberg–Hastings Models on Regular Trees,” arXiv:2108.06404 (2021), https://arxiv.org/html/2108.06404v1.
