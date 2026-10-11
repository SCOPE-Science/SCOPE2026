# Exact logarithmic switching lifetime near a nonfreezing seven-agent confidence system

## Finding
For a fixed seven-agent synchronous bounded-confidence (SBC) system, a natural two-dimensional family of initial opinions has a complete, explicit proximity-graph switching phase diagram. In particular, the nonfreezing orbit occupies a boundary ray of the family, while arbitrarily nearby initial states can have an arbitrarily large *finite* number of graph changes. The final change occurs on a sharp logarithmic time scale.

Set
\[
\begin{aligned}
z&=(0,36,72,84,96,132,168),\\
r&=(18,42,48,12,48,42,18),\\
v_-&=(0,2,-3,0,3,-2,0),\\
v_+&=(0,2,1,0,-1,-2,0).
\end{aligned}
\]
For any real \(0\le a,b\le1\), initialize the system at \(x(0)=z+a v_-+b v_+\). Its entire trajectory is
\[
x(t)=z+a\left(-\frac16\right)^t v_-+b2^{-t}v_+ \qquad(t=0,1,2,\ldots).
\]
Every proximity arc stays fixed except the two arcs from agent 4 to agents 3 and 5, which are either both present or both absent. They are present at integer time \(t\) if and only if
\[
b2^{-t}\ge3a\left(-\frac16\right)^t.
\]
In particular, the graph is constant from time zero if \(a=0\) or \(b\ge3a\). If \(a>0\) and \(b=0\), its graph changes at every step forever. For \(a>0\) and \(0<b<3a\), set
\[
k=\left\lceil\log_9\left(\frac{3a}{b}\right)\right\rceil.
\]
Then exactly \(2k-1\) changes occur between consecutive graph snapshots, and the graph is constant from the **sharp time** \(T=2k-1\) onward. At fixed \(a>0\), the stabilization time satisfies
\[
T=\log_3(a/b)+O(1)\qquad(b\downarrow0).
\]
For uniformly distributed \((a,b)\) in the unit square, let \(S\) count the graph changes, ignoring the zero-area nonfreezing edge. Then
\[
\Pr(S\ge2m-1)=
\begin{cases}
5/6,&m=1,\\
3^{3-2m}/2,&m\ge2,
\end{cases}
\qquad \mathbb E[S]=\frac{29}{24}.
\]
The area statement is an exact geometric corollary of the same phase diagram, not a stochastic modification of the deterministic dynamics.

## Assumptions and scope
Agent indices range over \(1,\ldots,7\). The confidence radius of agent \(i\) is \(r_i\). At integer time \(t\ge0\), define the outgoing neighborhood
\[
N_i(t)=\{j\in\{1,\ldots,7\}:|x_j(t)-x_i(t)|\le r_i\},
\]
and update all coordinates synchronously by
\[
x_i(t+1)=\frac{1}{|N_i(t)|}\sum_{j\in N_i(t)}x_j(t).
\]
The inequality is inclusive at confidence thresholds; this convention is essential on the switching-boundary parameter curves. The proximity digraph contains the directed arc \(i\to j\) precisely when \(j\in N_i(t)\). Here a *graph change* means that consecutive digraphs differ. The theorem claims an exact classification only for the displayed compact two-parameter family with these fixed radii, not for all seven-agent systems.

## Proof
Write \(u=a(-1/6)^t\), \(v=b2^{-t}\). For all relevant times, \(-1/6\le u\le1\) and \(0\le v\le1\). The displayed candidate state becomes
\[
(0,\;36+2u+2v,\;72-3u+v,\;84,\;96+3u-v,\;132-2u-2v,\;168).
\]
It is strictly ordered throughout the rectangle \([-1/6,1]\times[0,1]\). In this rectangle the gaps between the first four agents obey
\[
\begin{aligned}
x_2-x_1&=36+2u+2v\in[35\tfrac23,40],\\
x_3-x_2&=36-5u-v\in[30,36\tfrac56],\\
x_4-x_2&=48-2u-2v\in[44,48\tfrac13],\\
x_4-x_3&=12+3u-v\in[10\tfrac12,15].
\end{aligned}
\]
The remaining relevant gaps satisfy \(x_3-x_1=72-3u+v>48\), \(x_5-x_3=24+6u-2v<48\), and \(x_6-x_3=60+u-3v>48\). Reflection about \(84\) handles the opposite side. Comparison with the seven confidence radii proves that the six noncentral neighborhoods are always
\[
\begin{array}{lll}
N_1=\{1\}, & N_2=\{1,2,3\}, & N_3=\{2,3,4,5\},\\
N_5=\{3,4,5,6\}, & N_6=\{5,6,7\}, & N_7=\{7\}.
\end{array}
\]
For agent 4 the only possible neighbors besides itself are agents 3 and 5. Their distances from agent 4 both equal \(12+3u-v\), so
\[
N_4=\{3,4,5\}\ \Longleftrightarrow\ v\ge3u;
\]
otherwise \(N_4=\{4\}\). In either case agent 4's averaged opinion stays exactly \(84\), since \(x_3+x_5=168\). Averaging the fixed neighborhoods gives
\[
x_2(t+1)=36-u/3+v,
\qquad x_3(t+1)=72+u/2+v/2,
\]
and reflection determines agents 5 and 6, with agents 1 and 7 fixed. Thus the entire state evolves by \(u\mapsto-u/6\) and \(v\mapsto v/2\). Induction from the initial condition proves the exact trajectory and all graph assertions up to the time count.

At every odd time, \(u\le0\) while \(v\ge0\), so the two central arcs are always present. At even time \(t=2j\), they are present precisely when
\[
b\,4^{-j}\ge3a\,36^{-j}
\quad\Longleftrightarrow\quad b\ge3a\,9^{-j}.
\]
If \(b\ge3a\), this holds at every even time as well. If \(b=0<a\), it fails at every even time. In the remaining regime \(0<b<3a\), exactly the even instants \(0,2,\ldots,2(k-1)\) omit the arcs, with
\[
k=\left\lceil\log_9(3a/b)\right\rceil.
\]
The alternating sequence changes at each step through time \(2k-1\), then never changes again; there are therefore exactly \(2k-1\) changes. Equality \(b=3a9^{-j}\) gives inclusion at time \(2j\), consistently with the ceiling formula. The logarithmic estimate follows by multiplying the ceiling by two.

For the area-law corollary, \(k\ge m\) holds precisely when \(b<3^{3-2m}a\). When \(m=1\), integration of the part of the unit square under \(b<3a\) gives area \(5/6\). For \(m\ge2\), the slope is at most \(1/3\), and direct integration gives area \(3^{3-2m}/2\). Since the switching count is \(2k-1\) when \(k\ge1\) and zero otherwise, summing the geometric tail yields
\[
\mathbb E[S]=\frac56+2\sum_{m=2}^{\infty}\frac{3^{3-2m}}2
=\frac56+\frac38=\frac{29}{24}.
\]

## Verification
The included standalone `check.py` uses exact rational arithmetic; it has no nonstandard dependencies. Running `python3 check.py` checked 73 distinct parameter pairs, 4,818 exact one-step updates, all predicted neighbor sets, switch counts, equality boundaries, and the first three parameter-area tail values. Its output begins `PASS`. These tests validate finite identities only; the assertion for every real parameter and every time follows from the displayed analytic bounds and induction. The script is provided as a reproducibility aid rather than a formal proof engine.

## Relationship to prior work
Hegarty, Ognissanti and Wedin [1, Section 2] exhibited the seven-agent SBC trajectory corresponding to \(a=1,b=0\), proving that its proximity digraph never settles. The present theorem keeps their radii and original negative-eigenvalue mode, adds a linearly independent decaying positive mode, and determines the full two-mode switching diagram, its exact finite switching count and logarithmic stabilization time, together with an area distribution. It does not claim the previously published nonfreezing example as a new result. Their discussion of generic initial configurations motivates studying perturbations, but supplies no corresponding exact two-dimensional count law in the inspected text. Mirtabatabaei and Bullo [2] provide a general framework for state transition graphs and asymptotic behavior under fixed neighborhood structure; the explicit switching-count conclusions above are not among those general fixed-graph criteria.

## Limitations
The family is a two-dimensional plane inside seven-dimensional opinion space, not an open set of arbitrary initial opinions. Its infinite-switch locus is a boundary of that plane, and the phase diagram does not establish global almost-everywhere graph stabilization for the complete SBC model. The probability formulas refer only to Lebesgue-uniform parameters in the stated square. Priority beyond the two inspected primary papers remains uncertain, and no independent mathematical audit has been performed.

## References
[1] P. Hegarty, D. Ognissanti, E. Wedin, *Non-freezing of the proximity digraph and non-pseudostable convergence in heterogeneous Hegselmann–Krause models: Counterexamples to conjectures and results of Mirtabatabaei and Bullo*, arXiv:2610.03229v1 (first public version, 2026-10-02), especially Sections 2 and 6. https://arxiv.org/abs/2610.03229

[2] A. Mirtabatabaei, F. Bullo, *Opinion dynamics in heterogeneous networks: Convergence conjectures and theorems*, arXiv:1103.2829v2 (2011 preprint), especially the fixed-topology spectral analysis. https://arxiv.org/abs/1103.2829
