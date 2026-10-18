# Reentrant two-leader placement on weighted double-star consensus networks

## Finding

**Theorem (complete two-leader classification).** Let \(m\ge2\) be an integer. Form a weighted double-star tree \(D_m(b)\) from two hubs joined by an edge of conductance \(1/b\), where \(b>0\); each hub has \(m\) private leaves joined by unit-conductance edges. Exactly two distinct vertices receive equal finite leader-feedback gain \(\kappa>0\), and independent unit-intensity Brownian disturbances act at every vertex. Write \(r=1/\kappa\).

Let \(L\) be the weighted graph Laplacian, \(D_S\) the diagonal indicator of a two-vertex leader set \(S\), and \(J(S)=\frac12\operatorname{tr}(L+\kappa D_S)^{-1}\). Label **HH** the pair of both hubs, and **HL** any hub paired with a leaf *attached to the opposite hub*. Among all \(\binom{2m+2}{2}\) choices of \(S\), every global minimizer is HH or one of the \(2m\) opposite-side HL sets; no other pair can minimize.

The exact comparison is determined by
\[
P_m(b,r)=2(m-1)r^2+2\bigl((m-2)b-1\bigr)r+b\bigl((m-1)b-1\bigr).
\]
HH is the unique minimizing set if \(P_m>0\); the \(2m\) opposite-side HL pairs, and no others, minimize if \(P_m<0\); HH and exactly those \(2m\) HL pairs tie if \(P_m=0\). Define
\[
T_{HH}=\frac{2(bmr+bm+br+mr^2+2mr+r^2)}{b+2r},\quad
T_{HL}=\frac{2bmr+3bm+2br-b+2mr^2+6mr+2m+2r^2-1}{b+2r+1}.
\]
Then the minimum stationary total variance is exactly \(\frac12\min\{T_{HH},T_{HL}\}\).

Put
\[
b_0=\frac1{m-1},\qquad b_c=\frac{1+\sqrt{m^2-1}}{m^2-2},\qquad
r_\pm(b)=\frac{1-(m-2)b\pm\sqrt{1+2b-(m^2-2)b^2}}{2(m-1)}.
\]
For \(0<b\le b_0\), there is one positive switching point \(r_+\): HL wins for smaller positive \(r\), and HH wins for larger \(r\). For **every** \(b_0<b<b_c\), both roots are strictly positive and satisfy \(r_-<r_+\), producing the **reentrant** pattern HH–HL–HH as \(r\) increases, with ties at the two endpoints. At \(b=b_c\), the HH choice is strictly optimal except at the isolated positive double root where HH and HL tie. At \(b>b_c\), HH is uniquely optimal at every positive \(r\). The width of the reentrant bridge-resistance window satisfies \(b_c-b_0\sim(2m^3)^{-1}\) as \(m\to\infty\).

Already on six vertices, \(m=2\) and \(b=6/5\) give exact switching thresholds \(r_\pm=(5\pm\sqrt{13})/10\). The unique optimal pair type is HH at \(r=1/20\), opposite-side HL at \(r=1/2\), and HH again at \(r=2\).

## Assumptions and scope

The tree has \(2m+2\) vertices, \(m\) leaves on each hub, positive conductances, and no other edges. Every vertex experiences equal independent unit-strength process noise; the two selected leaders receive identical positive stabilizing feedback \(\kappa\), with no feedback on nonleaders. The stochastic dynamics are \(dX_t=-(L+\kappa D_S)X_t\,dt+dW_t\); the total stationary variance is \(J(S)=\frac12\operatorname{tr}(L+\kappa D_S)^{-1}\), since the drift matrix is positive definite for nonempty \(S\). All minima are over *unordered pairs of distinct vertices*; no assumption is made that leaders occupy different halves, hubs, or symmetric positions. Feedback strengths are finite and positive; limits at \(r=0\) are not part of the theorem.

## Proof

**1. Exact grounded-resistance reduction.** Introduce a new grounded vertex connected to each chosen leader by a resistance \(r=1/\kappa\). The augmented graph has exactly one cycle, comprising the two grounded branches and the original unique leader-to-leader tree path. The diagonal entry of \((L+\kappa D_S)^{-1}\) at vertex \(z\) is the effective resistance from \(z\) to ground. Let the leader path have resistance length \(d\), let \(x\in[0,d]\) be the resistance-coordinate of the projection of \(z\) onto this path measured from one leader, and let \(\delta\ge0\) be the resistance length of the hanging branch from \(z\) to its projection. Series/parallel reduction gives
\[
R_z=\delta+F_d(x),\qquad F_d(x)=\frac{(x+r)(d-x+r)}{d+2r}.
\]
The formula also holds for \(d>0\) with \(x=0\) or \(x=d\). Therefore \(2J(S)=\sum_z R_z\), a sum of explicit rational functions.

**2. Exhaust the five leader-position orbits.** The graph automorphisms interchange both sides and permute leaves independently. There are precisely five pair types: HH (both hubs), HL (hub with opposite-side leaf), HS (hub with same-side leaf), LL (leaves on opposite sides), and LS (two leaves on the same side). Write \(T_A=2J(S)\) for an arbitrary pair of type \(A\). Directly summing \(R_z\) yields
\[
\begin{aligned}
T_{HH}&=2m+2(m+1)F_b(0),\\
T_{HL}&=2m-1+(m+1)F_{b+1}(0)+mF_{b+1}(b)+F_{b+1}(b+1),\\
T_{LL}&=2(m-1)+2F_{b+2}(0)+2mF_{b+2}(1),\\
T_{HS}&=2m-1+(m+1)b+(2m+1)F_1(0)+F_1(1),\\
T_{LS}&=2m-2+(m+1)b+2F_2(0)+2mF_2(1).
\end{aligned}
\]
Here all resistances are positive, including the possibly nonunit bridge resistance \(b\).

**3. Eliminate every competing orbit rigorously.** Algebraic simplification of those five rational functions gives
\[
T_{HL}-T_{HS}=-\frac{bQ_{HS}}{(2r+1)(b+2r+1)},
\]
where
\[
Q_{HS}=2bmr+bm+2br+b+2mr^2+2mr+2r^2+4r+1.
\]
Likewise
\[
T_{HL}-T_{LL}=-\frac{Q_{LL}}{(b+2r+1)(b+2r+2)},
\]
with
\[
Q_{LL}=(m-1)b^2+2(m-2)br+(2m-3)b+2(m-1)r^2+(4m-6)r+2(m-1),
\]
and
\[
T_{HS}-T_{LS}=-\frac{(m-1)r^2+(2m-3)r+(m-1)}{(r+1)(2r+1)}.
\]
Every displayed numerator and denominator is strictly positive when \(m\ge2\) and \(b,r>0\). Hence \(T_{HL}<T_{HS}<T_{LS}\), and \(T_{HL}<T_{LL}\). No LS, LL or HS set can be optimal, including along switching boundaries.

**4. HH versus HL and complete phase diagram.** The remaining exact difference factors as
\[
T_{HH}-T_{HL}=-\frac{P_m(b,r)}{(b+2r)(b+2r+1)}.
\]
Both denominators are positive, so the sign of \(P_m\) gives every optimizer and the optimal variance. The quadratic is strictly convex in \(r\), with discriminant \(4[1+2b-(m^2-2)b^2]\), and constant term \(b[(m-1)b-1]\). If \(b<b_0\), the constant term is negative; hence there is exactly one positive root \(r_+\). At \(b=b_0\) one root is zero and the other positive. If \(b_0<b<b_c\), the constant is positive, the discriminant positive, and the sum of roots \([1-(m-2)b]/(m-1)\) is positive. (Indeed \(b_c<1/(m-2)\) for \(m>2\); the case \(m=2\) is immediate.) Thus both roots are positive, and strict convexity gives precisely the asserted negative interior interval. At \(b=b_c\), the discriminant vanishes, the vertex is at a positive \(r\), and the unique zero is double. Above \(b_c\), the discriminant is negative and the leading coefficient positive, so \(P_m>0\) for all real \(r\). Expansion of the explicit thresholds gives \(b_c-b_0=1/(2m^3)+O(m^{-4})\). No unlisted cases remain.

**5. Exact six-vertex witness.** For \(m=2\), \(b=6/5\), the quadratic has roots \((5\pm\sqrt{13})/10\). Substitution of \(r=1/20,1/2,2\) into the difference formula gives respectively negative, positive, and negative signs; step 3 excludes all other pair types. These are exact rational and quadratic-irrational certificates, not numerical conjectures.

## Verification

The standalone `verification/verify.py` uses Python 3.10+ and SymPy. Run from the package root with `python verification/verify.py`. It checks the symbolic five-orbit formulas and factorization identities, the two switching-root identities, exact witness inequalities, and independently constructs weighted Laplacians to compare all unordered two-vertex choices with inverse-trace formulas for four network sizes and four parameter pairs each. A successful run reports 681 assertions. These finite calculations corroborate the identities; the proof of the statements for every integer \(m\ge2\) and real \(b,r>0\) is the sign argument above.

## Relationship to prior work

Lin, Fardad, and Jovanović (2013) introduced optimization of leader positions in stochastically forced networks, including noisy and noise-free leaders, and algorithms for the discrete selection problem. Fitch and Leonard (2014) gave general joint-centrality expressions for leader-set performance; their framework can evaluate any fixed pair and thus subsumes the underlying objective formula. The contribution here is not a new noise model, general resistance identity, or universal leader-selection algorithm: it is the complete **weighted-double-star** optimizer classification, exclusion of three pair orbits by explicit positive differences, and a parameter-dependent reentrant region with a sharp boundary for every \(m\). Patterson, McGlohon, and Dyagilev (2014) treat one-dimensional formations with a different pinned-leader setup; Patterson, Yi, and Zhang (2017) relate graph resistance and leader selection, including algorithms and certain explicit tree/cycle cases, but do not state this weighted two-finite-gain double-star diagram in the inspected text.

## Limitations

The result assumes a balanced double star, one bridge resistance parameter, equal feedback gains and equal disturbance intensities; unbalanced trees, heterogeneous leader gains, multiple leaders, and other performance criteria are not classified. Earlier general joint-centrality/resistance formulas can in principle be specialized to this graph. No priority or independence from those general theories is claimed. An equivalent unindexed or differently formulated exact special-case result may exist. The result has not been independently reviewed.

## References

1. F. Lin, M. Fardad, and M. R. Jovanović, “Algorithms for leader selection in stochastically forced consensus networks,” arXiv:1302.0450, first publicly posted 2013-02-03. https://arxiv.org/abs/1302.0450
2. K. E. Fitch and N. E. Leonard, “Joint centrality distinguishes optimal leaders in noisy networks,” arXiv:1407.1569, first publicly posted 2014-07-07. https://arxiv.org/abs/1407.1569
3. S. Patterson, B. McGlohon, and K. Dyagilev, “Efficient optimal k-leader selection for coherent one-dimensional formations,” arXiv:1412.6595, 2014. https://arxiv.org/abs/1412.6595
4. S. Patterson, Y. Yi, and Z. Zhang, “A resistance distance-based approach for optimal leader selection in noisy consensus networks,” arXiv:1708.06873, 2017. https://arxiv.org/abs/1708.06873
