# Four-leader phase transitions on friendship networks

## Finding

Let the friendship network \(F_m=K_1\vee(mK_2)\) consist of one hub and \(m\) disjoint peripheral pairs, with every pair joined internally and both vertices joined to the hub. All edges have conductance one. For an integer \(m\ge2\), choose exactly four distinct vertices as equal-gain leaders, with gain \(\kappa>0\). For a set \(S\) of four leaders, let
\[
J_m(S,\kappa)=\frac12\operatorname{tr}\bigl(L_{F_m}+\kappa D_S\bigr)^{-1},
\]
where \(D_S\) is diagonal with ones on \(S\) and zeros elsewhere.

The following notation names **all** optimal sets within each configuration type (not only one representative):

- \(A_m\): the hub and exactly one peripheral vertex in each of three different pairs (defined for \(m\ge3\)).
- \(B_m\): no hub, with one peripheral vertex in each of four different pairs (defined for \(m\ge4\)).
- \(C_3\): no hub, with both vertices of one pair and one vertex from each other pair of \(F_3\).
- \(D_2\): no hub, with all four peripheral vertices of \(F_2\).

**Complete global classification.** For every \(\kappa>0\), minimizers among all four-element vertex subsets are precisely:

1. \(m=2\): type \(D_2\), for every gain.
2. \(m=3\): type \(A_3\) when \(0<\kappa<\gamma\), type \(C_3\) when \(\kappa>\gamma\), and both types at \(\kappa=\gamma\). Here \(\gamma\) is the unique positive root of
   \[
   4\gamma^4+53\gamma^3+150\gamma^2+117\gamma-54=0,
   \qquad 0.3<\gamma<\frac13.
   \]
3. \(m=4,5\): type \(B_m\), for every gain.
4. \(m=6,7\): type \(A_m\) for \(0<\kappa<\kappa_-(m)\) and \(\kappa>\kappa_+(m)\); type \(B_m\) for \(\kappa_-(m)<\kappa<\kappa_+(m)\); both types at either transition. The exact gains are
   \[
   \kappa_\pm(6)=\frac{39\pm3\sqrt{165}}4,\qquad
   \kappa_\pm(7)=\frac{9\pm3\sqrt5}4.
   \]
   In both cases \(\kappa_-(m)\kappa_+(m)=9/4\).
5. \(m\ge8\): type \(A_m\), for every gain.

No other leader configurations tie in any of these regimes or at their boundaries. In particular, for \(m=6,7\), the optimal allocation **leaves the hub, returns to it, and hence is reentrant as feedback gain increases**.

## Assumptions and scope

The network is undirected, connected, and unweighted. The selected four leaders have exactly the same strictly positive finite gain \(\kappa\); all other vertices have zero gain. The stochastic interpretation uses independent unit-intensity disturbances,
\[
 dX_t=-\bigl(L_{F_m}+\kappa D_S\bigr)X_t\,dt+dW_t.
\]
Since the grounded matrix is symmetric positive definite, the stationary covariance is half its inverse. Minimization of its trace is equivalent to minimization of the full inverse trace. There are no per-vertex prices, directed edges, gain optimization, or perfect/noiseless leaders in this claim.

## Proof

**1. A block-inverse formula covering every leader set.** For each peripheral pair, let \(t=0,1,2\) be its number of leaders, and let \(N_t\) be the number of pairs with occupancy \(t\). Let \(h\in\{0,1\}\) indicate whether the hub is a leader. The constraints are
\[
 N_0+N_1+N_2=m,\qquad h+N_1+2N_2=4.
\]
Order the hub first. The two-by-two peripheral blocks of the grounded Laplacian, up to permutation of the two vertices, are
\[
 B_0=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\quad
 B_1=\begin{pmatrix}2+\kappa&-1\\-1&2\end{pmatrix},\quad
 B_2=\begin{pmatrix}2+\kappa&-1\\-1&2+\kappa\end{pmatrix}.
\]
Define \(\tau_t=\operatorname{tr}(B_t^{-1})\), \(g_t=\mathbf1^TB_t^{-1}\mathbf1\), and \(w_t=\mathbf1^TB_t^{-2}\mathbf1\). Direct inversion gives
\[
\begin{array}{c|ccc}
 t&\tau_t&g_t&w_t\\ \hline
0&4/3&2&2\\
1&(\kappa+4)/(2\kappa+3)&(\kappa+6)/(2\kappa+3)&(\kappa^2+6\kappa+18)/(2\kappa+3)^2\\
2&2(\kappa+2)/((\kappa+1)(\kappa+3))&2/(\kappa+1)&2/(\kappa+1)^2
\end{array}
\]
The Schur complement of the peripheral blocks is
\[
\sigma=2m+\kappa h-\sum_{t=0}^2N_tg_t>0.
\]
The inequality follows from positive definiteness of \(L_{F_m}+\kappa D_S\) for nonempty \(S\). The block inversion identity yields the exact objective formula
\[
\boxed{\mathcal T_m(h,N_1,N_2)=2J_m(S,\kappa)
=\sum_{t=0}^2N_t\tau_t+
\frac{1+\sum_{t=0}^2N_tw_t}{2m+\kappa h-\sum_{t=0}^2N_tg_t}.}
\]
Thus placements with the same occupancy profile have identical objective values, and all possible placements are accounted for.

**2. Reduce to the two unclustered profiles for \(m\ge4\).** Denote \(H=\mathcal T_m(1,3,0)\), \(H_p=\mathcal T_m(1,1,1)\), \(Q=\mathcal T_m(0,4,0)\), \(Q_p=\mathcal T_m(0,2,1)\), and \(Q_{pp}=\mathcal T_m(0,0,2)\). These are exactly the five possible profiles when \(m\ge4\). Substitution into the displayed block formula and cancellation yields
\[
H_p-H=\frac{P_H}{6(\kappa+3)(\kappa+6)(2\kappa+3)(\kappa^2+6\kappa+6)},
\]
\[
Q_p-Q=\frac{P_1}{12(\kappa+3)(2\kappa+3)(5\kappa+6)},\quad
Q_{pp}-Q=\frac{P_2}{12(\kappa+1)(\kappa+3)(2\kappa+3)},
\]
where
\[
\begin{aligned}
P_H={}&4\kappa^5+78\kappa^4+(24m+465)\kappa^3
 +(144m+1053)\kappa^2+(270m+729)\kappa+162m+81,\\
P_1={}&(8m+52)\kappa^3+(48m+252)\kappa^2
 +(90m+189)\kappa+54m+27,\\
P_2={}&(4m+22)\kappa^3+(22m+103)\kappa^2
 +(36m+66)\kappa+18m+9.
\end{aligned}
\]
Every displayed numerator and denominator is strictly positive for \(m\ge4\), \(\kappa>0\). Therefore only the profiles \(A_m\) and \(B_m\) can be optimal. The difference between these two is
\[
\boxed{Q-H=\frac{(8m-44)\kappa^2+(24m-222)\kappa+18m-99}{12(\kappa+6)(2\kappa+3)}.}
\]
Because minimizing \(J_m\) is equivalent to minimizing \(\mathcal T_m\), a positive difference means \(A_m\) wins. For \(m=4,5\), all three numerator coefficients are negative, so \(B_m\) wins. For \(m=6\), the numerator is \(4\kappa^2-78\kappa+9\); for \(m=7\), it is \(12\kappa^2-54\kappa+27=3(4\kappa^2-18\kappa+9)\). Each quadratic has exactly two distinct positive roots, equal to the stated thresholds, and is negative strictly between them. For \(m=8\), the numerator is \(20\kappa^2-30\kappa+45>0\), since its discriminant is negative. Increasing \(m\) by one increases that numerator by \(8\kappa^2+24\kappa+18>0\); hence all \(m\ge8\) favor \(A_m\). The two quadratic constant-to-leading-coefficient ratios equal \(9/4\), proving the common root-product law.

**3. Small networks.** For \(m=2\), the only profiles are \(H_p\) and \(Q_{pp}\), and
\[
 Q_{pp}-H_p=-\frac{\kappa^4+11\kappa^3+33\kappa^2+37\kappa+6}{4(\kappa+1)(\kappa+3)(\kappa^2+6\kappa+6)}<0.
\]
For \(m=3\), the possible profiles are \(H,H_p,Q_p,Q_{pp}\). The comparison \(H_p>H\) follows from \(P_H>0\) above, while
\[
 Q_{pp}-Q_p=\frac{94\kappa^4+577\kappa^3+1029\kappa^2+711\kappa+189}{12(\kappa+1)(\kappa+3)(2\kappa+3)(5\kappa+6)}>0.
\]
Finally,
\[
 Q_p-H=-\frac{4\kappa^4+53\kappa^3+150\kappa^2+117\kappa-54}{2(\kappa+3)(\kappa+6)(2\kappa+3)(5\kappa+6)}.
\]
The numerator polynomial has exactly one positive real root by Descartes' rule (one coefficient sign change), its value at zero is negative, and it tends to positive infinity. Its signs therefore give the stated \(m=3\) transition. All strict dominance comparisons exclude any omitted ties. This completes the global classification.

## Verification

The companion `verify.py` requires Python 3 and SymPy. It symbolically checks seven exact rational difference identities (including the three clustering penalties and all small-network comparisons), reconstructs and inverts the full grounded Laplacian independently with exact rational arithmetic for every four-leader subset on \(F_m\) for \(m=2,3,4,5\) at four positive rational gains (1,984 exact comparisons), and additionally tests representative gains and profiles on larger networks. It checks exact transition algebra and brackets the unique positive quartic root. To reproduce from the same directory, run `python verify.py`.

The symbolic difference identities and the coefficient-sign/Descartes arguments are the universal proof. The finite direct inverses are independent consistency checks, not a substitute for an all-\(m\), all-\(\kappa\) argument.

## Relationship to prior work

Lin, Fardad, and Jovanović (2013 preprint; 2014 journal) formulate finite-gain stochastic leader placement using exactly the inverse-trace criterion above, and develop general relaxations and selection algorithms rather than an exact friendship-network four-leader classification. Fitch and Leonard (2014 preprint; 2015 revision) derive joint-centrality formulas, with explicit optimizing examples primarily for one or two leaders on paths and cycles; the present result is neither a quotation of those general formulas nor a direct two-leader specialization.

Sun, Li, and Liu (2020) analyze noisy consensus on windmill-type networks, including leader–follower coherence with freely assigned leaders. Only its abstract and bibliographic record could be inspected. That abstract does not determine whether it contains an equivalent **finite positive-gain, four-leader optimization**, so historical overlap with its inaccessible detailed results remains an explicit risk. Results on generalized windmill graph invariants or on binary power-domination sensors concern different objectives and do not imply this phase classification.

## Limitations

The classification is for exactly four equal-gain leaders and the friendship graph \(K_1\vee(mK_2)\) with unit edges. It does not classify larger cliques per blade, unequal gains, prices, directed networks, different noise covariances, or all optimal configurations under an independently optimized gain budget. The limiting perfectly pinned/noiseless problem is not included as a finite-\(\kappa\) claim. Independent mathematical validation and historical-priority evaluation have not been performed.

## References

1. F. Lin, M. Fardad, M. R. Jovanović, *Algorithms for leader selection in stochastically forced consensus networks*, arXiv:1302.0450v1 (first public 2013-02-03), expanded v2 (2013-05-29), IEEE Transactions on Automatic Control 59 (2014), 1789–1802. https://arxiv.org/abs/1302.0450
2. K. E. Fitch, N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569v1 (2014-07-07), revised 2015-06-15. https://arxiv.org/abs/1407.1569
3. W. Sun, Y. Li, S. Liu, *Noisy consensus dynamics in windmill-type graphs*, Chaos 30 (2020), 123131, DOI:10.1063/5.0020696. Abstract accessible at https://pubmed.ncbi.nlm.nih.gov/33380064/ ; full text not inspected.
