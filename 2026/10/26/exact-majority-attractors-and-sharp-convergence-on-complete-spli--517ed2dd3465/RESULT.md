# Exact majority attractors and sharp convergence on complete split graphs

## Finding

Let \(S_{a,b}=K_a\vee\overline{K_b}\) be the complete split graph with a labelled clique of size \(a\ge1\) and a labelled independent set of size \(b\ge1\). Under synchronous open-neighbourhood binary majority dynamics with retention of the existing state at ties, write \(F\) for the update, \(Q_{a,b}=\#\operatorname{Fix}(F)\), and \(P_{a,b}=\#\operatorname{Fix}(F^2)\). Then \(Q_{a,b}=2\) and

\[
P_{a,b}=2+2\mathbf1_{\{b\ge a\}}+H(a,b)+J(a,b),
\]

where

\[
H(a,b)=\begin{cases}
\binom{a}{a/2}\binom{b}{b/2},&a,b\text{ both even},\\
0,&\text{otherwise},
\end{cases}
\qquad
J(a,b)=\begin{cases}
2\binom{a}{(a-b)/2},&a>b\text{ and }a\equiv b\pmod2,\\
0,&\text{otherwise}.
\end{cases}
\]

Every orbit becomes periodic after at most three updates: \(F^5=F^3\). The bound is attained precisely when \(a>b\), \(a\equiv b\pmod2\), and \(b\ge3\). Every primitive periodic orbit has period two, except for the two consensus fixed points, so the exact number of primitive two-cycles is \((P_{a,b}-2)/2\).

In the naturally balanced core–periphery subfamily, the recurrent-state count jumps with the parity of the common size:

\[
P_{2m,2m}=4+\binom{2m}{m}^{2},\qquad
P_{2m+1,2m+1}=4\quad(m\ge1).
\]

This distinguishes exponential oscillatory multiplicity at even sizes from a single non-consensus two-cycle at odd sizes.

## Assumptions and scope

The graph is simple, undirected, loopless, and labelled; every independent-set vertex is adjacent to every clique vertex, and there are no edges between independent-set vertices. A configuration is a vector in \(\{0,1\}^{a+b}\). All vertices update simultaneously: a vertex adopts the strict neighbour majority, and on an exact tie retains its previous bit. The assertions hold for all integers \(a,b\ge1\), including the star and complete-graph boundary cases. The basin claim is only the uniform upper bound on transient depth, not an enumeration of individual basins.

Define \(T(x)=\min\{t\ge0:F^{t+2}x=F^t x\}\). The theorem claims \(\max_x T(x)\le3\), together with the exact criterion for equality.

## Proof

Let \(C\) denote the clique, \(I\) the independent set, \(c\) and \(\ell\) their numbers of ones, and \(s=c+\ell\). Put \(N=a+b\). Every clique vertex sees all vertices except itself; an independent-set vertex sees exactly the clique. Thus the update of the clique is

\[
F(x)|_C=\begin{cases}
\mathbf0,&2s<N,\\
\mathbf1,&2s>N,\\
\neg(x|_C),&2s=N,
\end{cases}
\]

where the final case can occur only for even \(N\). The independent part becomes \(\mathbf0\), remains unchanged, or becomes \(\mathbf1\), respectively, as \(2c<a\), \(2c=a\), or \(2c>a\). The clique formula also holds for odd \(N\): taking account of tie retention, a clique vertex initially equal to one requires \(s\ge(N+1)/2\), exactly the same threshold as a clique vertex initially equal to zero. These are exact coordinatewise identities, not an approximation by occupancy counts.

**Classification of periodic configurations.** Once the clique becomes monochromatic, it stays monochromatic. In a periodic orbit with monochromatic clique the independent part must also be monochromatic, because its next value is forced by the clique. On the resulting four configurations, \((\mathbf0,\mathbf0)\) and \((\mathbf1,\mathbf1)\) are fixed; the opposite-colour configurations \((\mathbf0,\mathbf1)\) and \((\mathbf1,\mathbf0)\) form a two-cycle exactly for \(b\ge a\), and otherwise both flow into consensus.

For a periodic configuration whose clique is mixed, the clique must stay mixed at every step; hence \(2(c+\ell)=N\). Its clique pattern is complemented at each step. When \(2c=a\), the independent part is unchanged and the balance condition forces \(a,b\) both even and \(\ell=b/2\). These configurations form the central family, with \(\binom{a}{a/2}\binom{b}{b/2}\) distinct recurrent states.

When \(2c<a\), the independent part is forced to zero after one update, and the new clique contains \(a-c\) ones. Preserving balance requires \(2(a-c)=N\), equivalently \(c=(a-b)/2\), so \(a>b\) with matching parity, while the original balance forces \(\ell=b\). Complementing the bits gives the second half of this two-cycle family, with \(c=(a+b)/2\) and \(\ell=0\). These two disjoint halves contribute \(2\binom{a}{(a-b)/2}\) states. The case \(2c>a\) is the symmetric half and yields nothing additional. The only fixed configurations are the two consensus states. The three disjoint two-cycle families give exactly the displayed formula for \(P_{a,b}\) and the orbit count. This enumerates all periodic states, not merely those seen by computation.

**Uniform convergence.** If \(2s\ne N\), the next clique is monochromatic. If it is zero, then either the independent part is already zero or full, or \(2c=a\) and it is still the old independent pattern; in the latter case \(2s<N\) forces \(\ell<b/2\), and the following update gives consensus zero. If the independent part is full while the clique is zero, this is either already the anti-aligned two-cycle (\(b\ge a\)) or goes to consensus at the next update (\(b<a\)). The one-clique case follows by bit complementation. Thus all initially unbalanced states have \(T(x)\le2\).

Now assume \(2s=N\). If \(2c=a\), the configuration is in the central two-cycle family. If \(2c<a\), the first step complements the clique and sets the independent part to zero. Feasibility of the initial independent count implies \(c\ge(a-b)/2\). At equality the state belongs to the other mixed-clique two-cycle family. At strict inequality, the new total \(a-c\) is below \(N/2\), so after two updates the configuration is exactly \((\mathbf0,\mathbf1)\). It is then periodic immediately when \(b\ge a\), and otherwise reaches consensus zero after one further update. The case \(2c>a\) is symmetric. Therefore \(T(x)\le3\) for every configuration, proving \(F^5=F^3\).

A depth-three configuration exists exactly when \(N\) is even, \(a>b\), and there is an integer \(c\) strictly between \((a-b)/2\) and \(a/2\). Such an integer exists precisely when \(a>b\), \(a\equiv b\pmod2\), and \(b\ge3\). For sufficiency, choose \(c=(a-b)/2+1\) clique ones and \(\ell=b-1\) independent ones. It is balanced and follows the strict-inequality branch to \((\mathbf0,\mathbf1)\), then consensus zero, so \(T(x)=3\). The complement gives another witness. Conversely, the preceding case analysis shows no other case has depth three.

## Verification

The standalone `verification/verify_split.py` checks the original graph-neighbour update directly, exhaustively over every labelled configuration for 79 parameter pairs with \(1\le a,b\le10\) and \(a+b\le14\). This comprises 253,956 labelled initial configurations. It compares the observed fixed and recurrent counts, the identity \(F^5=F^3\), and the sharp-depth criterion against the formulas. It then checks the derived occupancy map on all \((c,\ell)\) representatives for 900 additional parameter pairs with \(1\le a,b\le30\). Running the script with Python 3 reproduces the result in `verification/verify_output.txt`. The all-size theorem and sharpness rely on the preceding proof; finite checks are corroboration, not an infinite certificate.

## Relationship to prior work

Goles and Olivos established eventual period at most two for symmetric Boolean threshold networks, a theorem applying to this system but not supplying its exact attractor counts or its three-update bound. Benjamini, Chan, O'Donnell, Tamuz and Tan (first posted 2014-05-11) explain the same finite-graph theorem and investigate infinite unimodular and random-graph settings, not an exact complete-split-graph census. Turau (2022) develops fixed-point and two-cycle characterizations for trees, including the star boundary, but does not cover the dense complete split graphs with \(a\ge2\) except the trivial smallest overlap.

Earlier exact results for balanced complete multipartite graphs and for complete tripartite graphs overlap special graph choices but do not imply the simultaneous two-parameter formula, the full mixed-core classification, or the sharp universal transient statement. A known sequence for squared central binomial coefficients by itself does not identify them as recurrent-state counts in this dynamics. Exact statements were compared, not merely titles or graph labels.

## Limitations

The theorem concerns only complete split graphs and the specified tie-retaining open-neighbourhood rule; other split graphs, weighted ties, asynchronous updates and random dynamics are not covered. The convergence-depth distribution and sizes of attraction basins are not determined. Novelty is a bounded literature/database assessment rather than a uniqueness guarantee: an unindexed equivalent, or relevant material in inaccessible historical papers, remains possible. No independent audit has been conducted.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI `10.1016/0012-365X(80)90121-1`.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv `1405.2486`, first submitted 2014-05-11, https://arxiv.org/abs/1405.2486.
3. V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv `2202.01580`, first submitted 2022-02-03, https://arxiv.org/abs/2202.01580.
4. *Complete split graphs*, Graph Classes, https://www.graphclasses.org/classes/gc_1242.html (definition of the graph family).
