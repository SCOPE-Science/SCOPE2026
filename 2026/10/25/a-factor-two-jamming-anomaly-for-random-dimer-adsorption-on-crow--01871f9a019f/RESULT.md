# A factor-two jamming anomaly for random dimer adsorption on crown graphs

## Finding
For each integer \(n\ge 2\), consider the crown graph \(G_n=K_{n,n}\setminus\{L_iR_i:1\le i\le n\}\). Independently at each permissible edge, dimers attempt irreversible deposition at unit Poisson rate; a deposition succeeds exactly when both endpoints remain vacant. Let \(p_n\) be the probability that the terminal state has two vacant vertices (one on each side), rather than perfect coverage. Then
\[
\frac{2}{n+1}-\frac{4(H_{n-1}+2-2/n)}{(n+1)(n+2)}\le p_n\le\frac{2}{n+1},\qquad H_k=\sum_{j=1}^k\frac1j.
\]
In particular, \(\lim_{n\to\infty}n p_n=2\), with \(p_n=2/n+O(\log n/n^2)\). The entire finite-size probability is given by an explicit rational two-index recurrence below. Thus the probability of a defective jammed state is asymptotically twice the naive \(1/n\) chance of a coincident unmatched pair under independently uniform terminal vertices. No independence of the actual terminal vertices is assumed.

## Assumptions and scope
The vertices are \(L_1,\ldots,L_n\) and \(R_1,\ldots,R_n\), and all \(n(n-1)\) edges \(L_iR_j\), \(i\ne j\), have the same positive arrival rate (rescaled to one). A successful dimer permanently occupies its endpoints; later attempts touching occupied endpoints are rejected. Equivalent descriptions are the random edge-priority greedy matching and successive uniform choices among currently available edges. The terminal state is almost surely reached after at most \(n\) accepted dimers. Only \(n\) or \(n-1\) dimers can be deposited for \(n\ge2\): if at least two vertices remain vacant on each side, at least one edge is available.

At a stage with \(m\) vacant left and \(m\) vacant right vertices, write \(q\) for the number of indices whose left and right vertices are both vacant. The number of permitted vacant-to-vacant edges is \(m^2-q\). Conditional on \((m,q)\), an accepted dimer changes \(q\) to \(q-2,q-1,q\) with respective probabilities
\[
\frac{q(q-1)}{m^2-q},\quad \frac{2q(m-q)}{m^2-q},\quad \frac{(m-q)^2}{m^2-q}.
\]
These probabilities depend on no further details of the remaining graph. Hence for \(1\le q\le m\), and also for \(q=0\), the exact bad-jamming probability \(f(m,q)\) is computed recursively from \(f(1,1)=1\), \(f(1,0)=0\), and for \(m\ge2\),
\[
f(m,q)=\frac{q(q-1)f(m-1,q-2)+2q(m-q)f(m-1,q-1)+(m-q)^2f(m-1,q)}{m^2-q},
\]
where terms having zero coefficients are omitted. The desired value is \(p_n=f(n,n)\). In particular \(p_2=0\), \(p_3=1/3\), \(p_4=4/21\), \(p_5=4/21\), and \(p_6=172/1029\).

## Proof
Let \(Q_m\) be the number of common vacant indices at the unique stage with \(m\) vacancies in each part, for \(1\le m\le n\). The chain always progresses to \(m=1\) unless it has already jammed; and when \(m=1\), \(Q_1=1\) exactly when its sole possible remaining left-right pair is a deleted edge. Thus \(p_n=\mathbb E Q_1\), while \(Q_n=n\). The transition counts above follow by selecting an edge with both indices common and distinct (\(q(q-1)\) choices), with exactly one common endpoint-index (\(2q(m-q)\) choices), or with neither (\((m-q)^2\) choices).

For \(m\ge2\), direct summation of those transitions yields
\[
\mathbb E(Q_{m-1}\mid Q_m=q)=q\left(1-\frac{2(m-1)}{m^2-q}\right).
\]
Define \(X_m=Q_m/[m(m+1)]\). Exact algebra gives
\[
\mathbb E(X_{m-1}\mid Q_m=q)-X_m=-\frac{2q(q-1)}{m(m+1)(m-1)(m^2-q)}.
\]
The right-hand side is nonpositive. Taking expectations and telescoping therefore gives \(p_n/2=\mathbb EX_1\le X_n=1/(n+1)\), proving the upper bound.

To control the telescoping loss, consider ordered pairs of distinct common vacant indices and the falling factorial \((q)_2=q(q-1)\). For \(m\ge3\), conditional on \(Q_m=q\ge2\), a fixed ordered pair survives the next deposition if and only if the chosen edge avoids both indices on both sides. There are \((m-2)^2-(q-2)\) such edges; hence
\[
\mathbb E((Q_{m-1})_2\mid Q_m=q)=(q)_2\frac{m^2-4m+6-q}{m^2-q}.
\]
The ratio is at most \((m-2)/(m+2)\), since after cross multiplication the right-minus-left numerator is \(4q+2m-12\ge2\). For \(q<2\), both sides vanish. Consequently \((Q_m)_2/[(m-1)m(m+1)(m+2)]\) is a nonnegative reverse-time supermartingale down to \(m=2\). Since \(Q_n=n\), for \(2\le m\le n\),
\[
\mathbb E(Q_m)_2\le\frac{(m-1)m(m+1)(m+2)}{(n+1)(n+2)}.
\]
Also \(Q_m\le m\), so \(m^2-Q_m\ge m(m-1)\). The nonnegative drift loss \(D_m=X_m-\mathbb E(X_{m-1}\mid Q_m)\) obeys
\[
\mathbb E D_m\le\frac{2(m+2)}{(n+1)(n+2)m(m-1)}.
\]
Summing from \(m=2\) to \(n\), and using
\[
\sum_{m=2}^n\frac{m+2}{m(m-1)}=H_{n-1}+2-\frac2n,
\]
gives the stated lower bound. The two bounds differ by \(O(\log n/n^2)\), so \(n p_n\to2\) and the stated error follows. The exceptional early jamming event has strictly positive probability for \(n\ge3\), since the \(n-1\) left and right vertices excluding one common index admit a deranged perfect matching and every prescribed sequence of its edges has positive probability.

## Verification
The standalone `verify.py` uses exact rational arithmetic in two independent implementations: the \((m,q)\)-state recurrence, and a full set-of-vacant-vertices recursion, with independent counting of all possible next edges. Both produce identical \(p_n\) for \(2\le n\le6\). It also independently enumerates transition counts for every equal-cardinality pair of vacancy sets on graphs of sizes \(3\le n\le7\), and checks both probability bounds for \(2\le n\le6\). Its executed output ends `All exact independent finite-state checks passed.` These finite checks corroborate but do not replace the all-size moment proof.

## Relationship to prior work
Random sequential edge adsorption is a classic greedy-matching model, treated generally by Pippenger, *Random Sequential Adsorption on Graphs* (1989). Pippenger's stated high-girth/local-cycle results do not directly supply this dense crown-graph sharp defect probability: every crown edge lies in many four-cycles when the size is large. Bonnier, Leroyer and Pommiers, arXiv:cond-mat/9412019 (first public submission 5 December 1994), analyze dimer/segment adsorption on a one-dimensional dashed line rather than a crown graph. Lebovka and collaborators, arXiv:1507.04590, address defect-influenced deposition of rods on square lattices, not this finite dense bipartite model. Johnston, Kayll and Palmer, arXiv:2209.11319, count static perfect matchings that avoid a deleted matching; this differs from the law of a random *greedy* matching, which is not uniform among perfect matchings and can jam deficiently. The all-graph greedy-matching literature gives general bounds, but no equivalent sharp coefficient for this particular dense deleted-matching graph was found in the inspected material. This is a bounded literature assessment, not a proof of novelty.

## Limitations
The conclusion assumes uniform edge arrival rates, a single deleted perfect matching, and irreversible hard-core dimers on the complete balanced bipartite substrate. The result is about terminal defect probability, not adsorption times, spatially sparse substrates, random graph disorder, or nonuniform rate matrices. The explicit finite-size lower bound can be negative at small sizes (where it is still valid but uninformative). Larger literature surveys and independent mathematical validation may identify earlier equivalent specializations of general random-greedy matching theorems.

## References
- N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. **2** (1989), 393–401, doi:10.1137/0402034.
- B. Bonnier, Y. Leroyer and E. Pommiers, *Random sequential adsorption on a dashed line*, arXiv:cond-mat/9412019 (first submitted 1994-12-05).
- N. I. Lebovka et al., *Jamming and percolation in generalized models of random sequential adsorption of linear k-mers on a square lattice*, arXiv:1507.04590 (2015-07-16).
- D. Johnston, P. M. Kayll and C. Palmer, *Deranged matchings: proofs and conjectures*, arXiv:2209.11319 (2022-09-22).
