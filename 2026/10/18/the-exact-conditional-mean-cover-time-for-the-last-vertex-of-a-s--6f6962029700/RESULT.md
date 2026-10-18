# The exact conditional mean cover time for the last vertex of a symmetric cycle walk

## Finding

For every integer \(n\ge3\), run simple symmetric nearest-neighbour random walk on the cycle \(C_n\) from vertex \(0\). Let \(T\) be the time when the walk first visits every vertex, and \(L\) the vertex discovered at that time. Then for every \(k\in\{1,\ldots,n-1\}\),

\[
\Pr(L=k)=\frac1{n-1},\qquad
\mathbb E[T\mid L=k]=\frac{n^2+n-3}{3}+(k-1)(n-1-k).
\]

Consequently the difference between the largest and smallest conditional mean cover times is exactly \(\lfloor(n-2)^2/4\rfloor\). The conditioning produces an order-\(n^2\) difference, despite the marginal uniformity of \(L\). In particular, the unconditional expectation remains the classical \(n(n-1)/2\).

## Assumptions and scope

The walk moves at each integer time to either neighbor with probability \(1/2\), independently of its past. Vertex labels are modulo \(n\), with clockwise orientation \(0,1,\ldots,n-1\). The graph is an undirected simple cycle with \(n\ge3\); \(T\) includes the final step onto the last unvisited vertex. All conditional events in the theorem have positive probability.

## Proof

Let \(\tau_m\) be the time when exactly \(m\) different vertices have first been visited (so \(\tau_1=0\)). For \(m\ge2\), let \(R_m\) count discoveries extending the clockwise/right boundary among the first \(m-1\) discoveries after the start, and let \(S_m\in\{\mathrm R,\mathrm L\}\) be the direction of the most recent discovery. At each discovery the visited vertices form a contiguous arc, and the walker is at the endpoint just added. Until the next discovery it is a simple symmetric walk on the arc of \(m\) visited sites, absorbed one step outside either endpoint.

**Exit probabilities and weighted times.** Reindex this absorbing interval as \(\{0,1,\ldots,m+1\}\) with interior sites \(1,\ldots,m\). Starting from \(y\) the probability of exiting at \(m+1\) is \(u(y)=y/(m+1)\). If \(\sigma\) is the exit time, set \(w(y)=\mathbb E_y[\sigma\,\mathbf1_{\{\text{exit at }m+1\}}]\). Conditioning on the first step gives the Dirichlet difference equation

\[
w(y)=u(y)+\tfrac12w(y-1)+\tfrac12w(y+1),\quad
w(0)=w(m+1)=0.
\]

Its unique solution is

\[
w(y)=\frac{y((m+1)^2-y^2)}{3(m+1)}.
\]

Also \(\mathbb E_y\sigma=y(m+1-y)\). Thus, after \(m\) sites have been visited, the probability that the next discovery stays on the same side is \(m/(m+1)\), and that it switches sides is \(1/(m+1)\). The **joint** means of the waiting time and the next-side events are, respectively,

\[
a_m=\frac{m(2m+1)}{3(m+1)}\quad\text{(stay)},\qquad
b_m=\frac{m(m+2)}{3(m+1)}\quad\text{(switch)}.
\]

These joint means are not conditional waiting-time means; indeed \(a_m+b_m=m\). This distinction is needed for the time-weighted recursion.

**Joint occupancy/time induction.** Write \(F_m^s(r)=\Pr(R_m=r,S_m=s)\), and \(H_m^s(r)=\mathbb E[\tau_m\mathbf1_{\{R_m=r,S_m=s\}}]\). The state at \(m=2\) is either \((r,s)=(0,\mathrm L)\) or \((1,\mathrm R)\), each with probability \(1/2\) and with \(\tau_2=1\). For all later \(m\), the exact claim is

\[
F_m^{\mathrm R}(r)=\frac{r}{m(m-1)},\qquad
F_m^{\mathrm L}(r)=\frac{m-1-r}{m(m-1)},\quad 0\le r\le m-1,
\]

and, whenever the corresponding event has positive probability,

\[
\frac{H_m^{\mathrm R}(r)}{F_m^{\mathrm R}(r)}
=\frac{2m(m-1)-r^2}{3},\qquad
\frac{H_m^{\mathrm L}(r)}{F_m^{\mathrm L}(r)}
=\frac{m^2-1+2r(m-1)-r^2}{3}.
\]

For completeness, the step from \(m\) to \(m+1\) uses, for a new right discovery,

\[
F_{m+1}^{\mathrm R}(r+1)=\frac{mF_m^{\mathrm R}(r)+F_m^{\mathrm L}(r)}{m+1},
\]

\[
H_{m+1}^{\mathrm R}(r+1)=\frac{mH_m^{\mathrm R}(r)+H_m^{\mathrm L}(r)}{m+1}
+a_m F_m^{\mathrm R}(r)+b_m F_m^{\mathrm L}(r).
\]

For a new left discovery the corresponding formulas interchange the coefficients \(m/(m+1)\) and \(1/(m+1)\), and interchange \(a_m\) and \(b_m\). Substituting the displayed expressions for \(F,H\), all four identities reduce to polynomial identities. This verifies the induction including the boundary zero-probability states.

Summing over the last side now gives \(\Pr(R_m=r)=1/m\) and

\[
\mathbb E[\tau_m\mid R_m=r]=\frac{m^2-1}{3}+r(m-1-r).
\]

**Conditioning on the final vertex.** At the stage \(m=n-1\) there is one unvisited vertex. It is \(k\) exactly when \(R_{n-1}=k-1\). From either endpoint of the \((n-1)\)-vertex visited arc, the expected remaining time to discover the unique missing vertex equals \(n-1\) by the same gambler's-ruin formula. Since this conditional expectation is independent of the side and the precise previous history, the tower property gives

\[
\mathbb E[T\mid L=k]=\frac{(n-1)^2-1}{3}
+(k-1)(n-k-1)+(n-1)
=\frac{n^2+n-3}{3}+(k-1)(n-k-1).
\]

The uniform law for \(L\) follows simultaneously from \(\Pr(R_{n-1}=k-1)=1/(n-1)\). Finally, \((k-1)(n-1-k)\) is a concave quadratic on the integers \(1\le k\le n-1\), with minimum zero and maximum \(\lfloor(n-2)^2/4\rfloor\), establishing the full profile and extrema.

## Verification

Run `python verify_cycle_last_conditional.py` using Python's standard library only. The script checks the exact joint-state recurrences through sixty visited vertices and directly verifies the absorbing gambler's-ruin time/exit difference equation for finite interval lengths. Independently, substitution of the symbolic proposed formulas into each of the four induction identities yields identically zero rational residuals; this is the algebra used in the proof. The finite checker is corroboration, not a substitute for the all-size induction.

## Relationship to prior work

Idnani and Salem (2026), first publicly posted October 10, establish a connected-arc representation, directional probabilities and the marginal distribution of the last vertex for symmetric and biased cycle walks. Their Section 4.1 derives formulas for the **unweighted** directional occupancy probabilities; the present theorem computes the **time-weighted** occupancy probabilities and obtains the conditional mean cover time, which is not determined by their marginal last-vertex law. Maiti and Sarkar (2019) study the unconditional cycle cover time and the last-vertex law, but the relevant sections do not provide the exact conditioning profile above. Aldous and Fill's classical treatment likewise provides the unconditional mean and marginal uniform last-vertex law. The principal contribution here is not any of those established marginal statements, but the exact nonconstant quadratic joint time-location moment.

## Limitations

The formula is for discrete-time, homogeneous, simple **symmetric** nearest-neighbour walks on finite cycles, not biased walks, time-inhomogeneous bias, general graphs, or full conditional distributions of cover time. The result is a same-model mathematical derivation; independent novelty review has not been performed. Although directly relevant primary texts were compared, an unlocated earlier conditional-moment formula remains a priority risk.

## References

1. K. Idnani and J. Salem, *Last-Coverage Probabilities of Random Walks on Cycle Graphs for Symmetric, Biased, and Time-Dependent Walks*, arXiv:2610.15115, first submitted October 10, 2026. https://arxiv.org/abs/2610.15115
2. S. I. Maiti and J. Sarkar, *Symmetric Walks on Paths and Cycles*, Mathematics Magazine **92** (2019), 252–268. https://doi.org/10.1080/0025570X.2019.1611166
3. D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 6 (draft book), cycle cover-time and last-vertex examples.
