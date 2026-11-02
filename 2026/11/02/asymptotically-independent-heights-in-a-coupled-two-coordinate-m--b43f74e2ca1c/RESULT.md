# Asymptotically independent heights in a coupled two-coordinate Moran walk

## Finding
Fix \(q\in(1/2,1)\). At every integer time, independently select one of the three simultaneous updates
\[
(x,y)\mapsto(x+1,1)\quad\text{with probability }1-q,\qquad
(x,y)\mapsto(1,y+1)\quad\text{with probability }1-q,\qquad
(x,y)\mapsto(x+1,y+1)\quad\text{with probability }2q-1,
\]
starting at \((X_0,Y_0)=(0,0)\). Put \(H_{X,n}=\max_{0\le t\le n}X_t\) and analogously \(H_{Y,n}\). For fixed \(c,C\in(0,\infty)\) with \(c\le C\), uniformly over integer thresholds \(h_X,h_Y\ge2\) obeying \(c\le nq^{h_i-1}\le C\),
\[
\Pr(H_{X,n}<h_X,\ H_{Y,n}<h_Y)
=\exp\left[-n(1-q)(q^{h_X-1}+q^{h_Y-1})\right]
+O_{q,c,C}\left(\frac{\log n}{n}\right).
\]
The corresponding joint law of *post-reset qualifying-run counts* is within \(O_{q,c,C}(\log n/n)\) in total variation of two independent Poisson variables with means \((n-h_i+1)(1-q)q^{h_i-1}\). Thus, for integer sequences of thresholds with \(nq^{h_i-1}\to\tau_i\in(0,\infty)\), the joint lower-tail probability tends to \(\exp(-(1-q)(\tau_X+\tau_Y))\): the two coordinate maxima have asymptotically independent **lattice extreme-value profiles**. In particular, the overall height \(H_n=\max(H_{X,n},H_{Y,n})\) has
\[
\Pr(H_n<h)=\exp[-2n(1-q)q^{h-1}]+O_{q,c,C}(\log n/n)
\]
in the same critical window. A continuously centered ordinary weak Gumbel limit is NOT asserted; the integer lattice produces a logarithmically periodic phase.

## Assumptions and scope
All updates are independent across time. The parameter \(q\) is fixed strictly between \(1/2\) and \(1\). Only the three displayed updates occur: the two coordinates cannot reset simultaneously. Height is the maximum over all times, not the terminal altitude. A reset puts the affected coordinate at \(1\); the special initial state is \(0\). The error constants may diverge at parameter endpoints. For \(c\le nq^{h_i-1}\le C\), both \(h_i\) are \(\log_{1/q}n+O_{q,c,C}(1)\).

## Proof
Write \(b=1-q\), \(a=2q-1\), and \(\ell_i=h_i-1\). For coordinate \(i\), mark an update time \(t\in\{1,\ldots,n-\ell_i\}\) when that coordinate resets at time \(t\) and then survives its next \(\ell_i\) updates. Denote the number of marks by \(N_i\). Each marker has probability \(bq^{\ell_i}\), and \(\mathbb EN_i=(n-\ell_i)bq^{\ell_i}\). If the initial \(h_i\) consecutive updates all preserve coordinate \(i\), it may reach height \(h_i\) without a preceding reset; this exceptional event has probability \(q^{h_i}=O(1/n)\). Otherwise \(H_{i,n}\ge h_i\) if and only if \(N_i\ge1\). This exact pathwise equivalence is independent of the other coordinate.

Every mark indicator depends only on the underlying independent update symbols in an interval of length \(\ell_i+1\). Use its interval-overlap neighborhood as a dependency graph. Put \(r=a/q^2=1-(1-q)^2/q^2\in[0,1)\). Same-coordinate marks at distinct times separated by at most \(\ell_i\) are incompatible, so their joint probability vanishes. Marks of different coordinates at the same time are also incompatible because there are no simultaneous resets.

For an \(X\)-mark at \(s\) and a \(Y\)-mark at \(s+k\), \(1\le k\le\ell_X\), the intersection of their success intervals has length \(L=\min(\ell_X-k,\ell_Y)\). Direct multiplication of the three possible update probabilities, including the forced single-coordinate reset at the second mark, yields the **exact** joint-marker probability
\[
\Pr(I_{X,s}=I_{Y,s+k}=1)
=b^2q^{\ell_X+\ell_Y-1}\left(\frac{a}{q^2}\right)^{L}.
\]
There is an analogous formula with \(X,Y\) interchanged. The geometric overlap sum is bounded by
\[
\sum_{k=1}^{\ell_X}r^{\min(\ell_X-k,\ell_Y)}
\le\frac1{1-r}+\max(0,\ell_X-\ell_Y)r^{\ell_Y}.
\]
The threshold window bounds \(|\ell_X-\ell_Y|\) uniformly. Since \(nq^{\ell_i}=O(1)\), the sum of expectations of jointly occurring, distinct neighboring marks is \(O_{q,c,C}(1/n)\). The dependency-graph sum of products of the individual marker probabilities is \(O_{q,c,C}((\log n)/n)\), as there are \(O(n\log n)\) neighboring ordered pairs and each marker probability is \(O(1/n)\). The conditional-independence correction outside neighborhoods is exactly zero, because disjoint time intervals involve independent symbols.

Apply the standard colored/point-process form of the Arratia–Goldstein–Gordon local-dependence Poisson bound to these two types of indicators. It gives
\[
 d_{\mathrm{TV}}\left(\mathcal L(N_X,N_Y),\operatorname{Pois}(\lambda_X)\otimes\operatorname{Pois}(\lambda_Y)\right)
 =O_{q,c,C}((\log n)/n),\quad
 \lambda_i=(n-\ell_i)bq^{\ell_i}.
\]
Passing to the simultaneous zero-count event, adding the two exceptional initial-run probabilities, and replacing \(\lambda_i\) by \(nbq^{\ell_i}\) (an error \(O(\log n/n)\)) proves the theorem. The subsequential independence statement and doubled-intensity overall-height profile follow immediately.

## Verification
The self-contained `moran_height_checker.py` verifies the exact marker-pair formula for rational parameter choices, including overlaps and boundary shifts, by independent enumeration of all three-letter update strings; verifies same-coordinate exclusion; verifies the pathwise relation between height exceedance and reset markers for finite histories; and compares a finite-state dynamic program against the predicted critical-window approximation. The checker passes 156987 assertions. These are finite checks, **not** a proof of the asymptotic theorem. The analytic proof uses the cited Poisson dependency-graph bound and the explicit uniform geometric sum; no computer-assisted infinite certification is claimed.

## Relationship to prior work
Aguech and Abdelkader (2023) study this exact symmetric two-coordinate model, including the joint terminal-altitude law and reset counts, and explicitly identify full-height analysis as a future objective. Althagafi and Abdelkader (2023) likewise treat terminal coordinates. Aguech, Althagafi and Banderier (arXiv:2311.13124, first posted 22 November 2023) establish one-coordinate discrete-Gumbel behavior and a general multidimensional *terminal* generating function, but their Section 5 does not establish joint height-extreme independence. Kong (arXiv:2405.01747, 2 May 2024) gives exact formulas for contiguous equal-letter runs in multiletter sequences; the present two overlapping survival predicates each aggregate multiple update letters, and the quantitative asymptotic joint independence is not a consequence of that displayed run classification. Standard Chen–Stein theory supplies the approximation method but does not by itself verify this model's cross-coordinate overlap sum or rule out persistent extreme dependence.

## Limitations
The model has fixed \(q\in(1/2,1)\); the theorem is not uniform as \(q\to1\), where complete dependence emerges, nor does it handle heterogeneous or time-dependent reset probabilities or higher dimensions. The finite-window estimate does not provide a global error bound for arbitrary thresholds. A full independent mathematical audit and definitive historical-priority review have not been performed.

## References
- R. Aguech and M. Abdelkader, *Two-Dimensional Moran Model: Final Altitude and Number of Resets*, Mathematics 11 (2023), 3774; first public publication 2 September 2023. DOI: https://doi.org/10.3390/math11173774.
- A. Althagafi and M. Abdelkader, *Two-Dimensional Moran Model*, Symmetry 15 (2023), 1046. https://doi.org/10.3390/sym15051046.
- R. Aguech, A. Althagafi and C. Banderier, *Height of Walks with Resets, the Moran Model, and the Discrete Gumbel Distribution*, arXiv:2311.13124 (2023), https://arxiv.org/abs/2311.13124.
- Y. Kong, *The m-th Longest Runs of Multivariate Random Sequences*, arXiv:2405.01747 (2024), https://arxiv.org/abs/2405.01747.
- R. Arratia, L. Goldstein and L. Gordon, *Two Moments Suffice for Poisson Approximations: The Chen–Stein Method*, Annals of Probability 17 (1989), 9–25.
