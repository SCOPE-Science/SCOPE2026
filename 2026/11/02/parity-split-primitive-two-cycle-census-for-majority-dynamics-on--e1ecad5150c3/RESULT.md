# Parity-split primitive two-cycle census for majority dynamics on wheels

## Finding

On the labelled wheel \(W_n=K_1\vee C_n\), for every integer \(n\ge3\), synchronous binary strict-neighbour majority with tie retention has exactly two fixed configurations. All its remaining periodic configurations belong to primitive two-cycles. The complete number \(N_n\) of distinct primitive two-cycle orbits is given by the following explicit three-state transfer and strict-half-plane coefficient extraction.

Let \(u,v\) be formal indeterminates, and set
\[
M(u,v)=\begin{pmatrix}1&u&0\\0&0&uv\\1&0&uv\end{pmatrix},\qquad F_m(u,v)=\operatorname{tr}(M(u,v)^m).
\]
For a polynomial \(P(u,v)\), define
\[
\mathcal H_n(P)=\sum_{\substack{a,b\ge0\\2a>n,\,2b<n}}[u^av^b]P(u,v).
\]
Then
\[
\boxed{\displaystyle N_n=\begin{cases}
\mathcal H_n(F_n),&n\text{ odd},\\
2+\mathcal H_n(F_{n/2}^{\,2}),&n\text{ even}.
\end{cases}}
\]
For odd \(n\), every primitive two-cycle flips the wheel hub at each update. For even \(n\), precisely two primitive two-cycle orbits keep the hub fixed; these have alternating rim configurations. Hub-flipping primitive two-cycles exist for every odd \(n\ge3\) and for every even \(n\ge6\), but not for \(n=4\).

The polynomial \(F_m\) is fully explicit without matrix arithmetic. Its nonzero coefficients are \([u^0v^0]F_m=[u^mv^m]F_m=1\), and for \(0<a<m\) and \(q\ge1\),
\[
\boxed{\displaystyle [u^av^{a-q}]F_m=\frac{m}{q}\binom{a-q-1}{q-1}\binom{m-a-1}{q-1}}
\]
when \(a\ge2q\) and \(m-a\ge q\); every other coefficient is zero. Thus this is an exact binomial formula for each orbit count, with no uncomputed transfer entries.

The two-cycle census is exponentially large, in contrast to the two fixed configurations. In particular,
\[
\liminf_{n\to\infty}N_n^{1/n}\ge\rho>1,\qquad \rho^4=\rho+1,\qquad\rho\approx1.2207440846.
\]

## Assumptions and scope

The rim has labelled vertices indexed by \(i\in\mathbb Z/n\mathbb Z\); the distinguished hub is \(h\). At each synchronous round, each vertex adopts the strictly more common binary opinion among its graph neighbours, retaining its present opinion exactly in a tie. A fixed point is a configuration unchanged by one update. A primitive two-cycle orbit is an unordered pair of distinct configurations interchanged by one update, counted once even when the two configurations have symmetries. No spatial-rotation or color-complement quotient is imposed. The theorem is valid for every integer \(n\ge3\); in particular \(W_3\) is the four-vertex complete graph with a distinguished hub.

## Proof

Write the hub bit as \(h\in\{0,1\}\), and the rim bits as \(x_i\in\{0,1\}\). The hub has \(n\) neighbours. It becomes \(1\) if \(2\sum_i x_i>n\), becomes \(0\) if \(2\sum_i x_i<n\), and otherwise retains its bit. Each rim vertex has degree three, so its update is
\[
y_i=\begin{cases}x_{i-1}x_{i+1},&h=0,\\x_{i-1}\vee x_{i+1},&h=1.\end{cases}
\]

**No higher periodic orbits.** Replace binary bits by signs \(s_i\in\{-1,1\}\). Let \(W\) be the symmetric adjacency matrix, augmented by a unit diagonal entry at exactly the even-degree vertices. Then every local field \((Ws)_i\) is an odd nonzero integer and an update chooses \(s_i'=\operatorname{sgn}((Ws)_i)\). For successive states \(s(t)\), set \(L(t)=s(t)^TWs(t-1)\). Symmetry and the pointwise strict-maximizer property show
\[
L(t+1)-L(t)=\sum_i\bigl(s_i(t+1)-s_i(t-1)\bigr)(Ws(t))_i\ge0,
\]
with strict inequality whenever \(s(t+1)\ne s(t-1)\). Since \(L\) takes bounded integer values on the finite state space, eventually \(s(t+1)=s(t-1)\). Hence the only periods are one and two.

**Fixed configurations.** If the hub is \(0\), a fixed rim bit \(x_i=1\) forces both of its immediate neighbours to be \(1\), hence forces the entire rim to be \(1\). That would switch the hub, a contradiction. Thus the only fixed state with hub \(0\) has every rim bit \(0\). Complementation gives the unique fixed state with hub \(1\).

**Cycles with constant hub.** With hub \(0\) at two consecutive updates, the rim satisfies
\[
x_i(t+2)=x_i(t)x_{i-2}(t)x_{i+2}(t).
\]
If this equals \(x_i(t)\), each present \(1\) propagates along its entire orbit under adding two rim indices. For odd \(n\), the only candidates are the constant rims and the all-one rim forces a hub change. For even \(n\), the two parity classes may independently be uniformly \(0\) or \(1\); the only primitive two-cycle choice with hub \(0\) alternates the parity classes, with the hub held by an exact tie at both steps. The complemented configurations provide exactly one additional orbit with hub \(1\). This proves the constant-hub count of two for even \(n\) and zero for odd \(n\).

**Cycles with flipping hub.** Every such orbit has exactly one representative with hub \(0\). Starting at that representative, put \(A=\sum_i x_i\), and let \(B=\sum_i x_{i-1}x_{i+1}\). The first update produces rim \(y_i=x_{i-1}x_{i+1}\) and hub \(1\) exactly when \(2A>n\). The second update produces
\[
z_i=y_{i-1}\vee y_{i+1}=x_i\bigl(x_{i-2}\vee x_{i+2}\bigr).
\]
It switches the hub back to \(0\) exactly when \(2B<n\). Therefore the initial configuration is a genuine two-cycle representative if and only if
\[
2A>n,\qquad 2B<n,\qquad x_i=1\Longrightarrow x_{i-2}=1\text{ or }x_{i+2}=1
\]
for every rim index. The last condition states that the set of ones has no isolated site in the cyclic step-two ordering. These three requirements are both necessary and sufficient. Distinct admissible rim words give distinct primitive two-cycle orbits, without a factor of two.

**Transfer enumeration.** The step-two adjacency forms one ring of length \(n\) if \(n\) is odd and two labelled rings of length \(n/2\) if \(n\) is even; in the length-two case its two oriented adjacent pairs are counted with multiplicity, as required by \(B\). For one cyclic word, permit runs of ones only when their length is at least two. A three-state automaton records the last symbol being zero, the first one of a run, or a subsequent one. Its weighted adjacency matrix is \(M(u,v)\): every one contributes \(u\), and every adjacent pair of ones contributes an extra \(v\). A mixed cyclic word has a unique consistent state assignment; the all-zero and all-one words also each have exactly one. Consequently \(F_m=\operatorname{tr}(M^m)\) counts exactly these cyclic words by their numbers \(A\) of ones and \(B\) of adjacent one-pairs. Independent parity rings multiply these polynomials. Imposing the two strict half-plane inequalities proves the displayed formula for \(N_n\).

For the binomial form, take a mixed admissible cyclic word with \(a\) ones and exactly \(q\) nonempty one-runs. The runs of ones have lengths at least two; the intervening zero-runs have lengths at least one. The ordered compositions contribute \(\binom{a-q-1}{q-1}\binom{m-a-1}{q-1}\); marking the starting rim position gives a factor \(m\), while each word is marked \(q\) times. This proves the coefficient formula.

**Existence and exponential lower bound.** For odd \(n\), a single run of \((n+1)/2\) ones in the step-two cyclic ordering has \(A=(n+1)/2\) and \(B=(n-1)/2\), so hub-flipping cycles exist. For even \(n=2m\ge6\), choose one run of length two in one parity ring and one run of length \(m-1\) in the other; then \(A=m+1\) and \(B=m-1\). At \(n=4\) each parity ring has length two and can be only all-zero or all-one, so the strict inequalities cannot both hold.

For a quantitative exponential lower bound, form cyclic step-two words by concatenating blocks \(110\) and \(1110\), with each word starting at a block boundary. Such a word has no isolated ones and has more than half its sites equal to one. It has strictly fewer than half its step-two adjacency pairs equal to \(11\) whenever at least one \(110\) block occurs. Ordered block compositions of a given length are distinct words; their number \(c_m\) satisfies \(c_m=c_{m-3}+c_{m-4}\) and grows at rate \(\rho^m\), where \(\rho^4=\rho+1\). When \(n\) is odd, no all-\(1110\) composition has length \(n\). For even \(n\), apply the construction independently to both parity rings and omit at most one all-\(1110\) pair. The resulting valid families have sizes at least \(c_n\) and \(c_{n/2}^2-1\), respectively. Taking \(n\)-th roots proves the lower bound.

## Verification

A standalone Python verifier implements the original synchronous wheel updates, independently enumerates all configurations for \(3\le n\le16\), and compares fixed points, constant-hub two-cycles and switching-hub two-cycles against the exact formula. It examines \(262{,}128\) configurations. Separately, it enumerates cyclic words to verify the run polynomial for lengths two through twelve and multiplies the three-state polynomial matrix to verify transfer traces for lengths two through ten. All comparisons passed.

For \(n=3,4,5,6,7,8,9,10\), the exact primitive two-cycle orbit counts are respectively \(3,2,5,11,21,34,66,77\). At \(n=11,12,13,14,15,16\), they are \(220,227,715,835,2318,2978\). The verifier records these values and prints `WHEEL_MAJORITY_ORBITS_VERIFY_OK` on success. Run `python3 verify.py` with Python 3; only the standard library is required.

## Relationship to prior work

The finite-graph period-at-most-two theorem is due to Goles and Olivos and is established background, not a new claim here. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486v1), and Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519v1), study the same synchronous tie-retaining majority model but establish periodicity, convergence and voting-time results rather than the wheel-specific primitive-orbit census.

Agur, Fraenkel and Klein (1988) enumerate fixed points for the one-dimensional cyclic nearest-neighbour majority rule. Their cyclic-word counting concerns a cycle with no hub and does not imply the hub-switching inequalities or the wheel census. Turau (arXiv:2202.01580) studies fixed points and two-cycles for trees, which do not include wheels. Aledo et al. (2020) count periodic points of maxterm/minterm Boolean systems; those update operators are not the tie-retaining majority rule on the whole wheel. General symbolic or transfer counting of constrained cyclic strings is also prior mathematical technique. The novel assessed assertion is the wheel-specific phase classification and resulting exact binomial/transfer orbit formula, not the transfer or cyclic-composition methods in isolation.

## Limitations

This is a count of initially periodic orbits, not of attraction-basin sizes, first periodic-entry times, or all transient trajectories. The positive exponential lower bound is not a determination of an exact exponential growth rate. The mathematical proof is self-contained, and finite verification is a cross-check rather than an infinite proof. A related result under an unindexed alternative terminology or in inaccessible earlier material may exist; no independent scientific audit has been performed.

## References

1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first posted 2014-05-11. https://arxiv.org/abs/1405.2486
2. D. Kaaser, F. Mallmann-Trenn, E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1, first posted 2015-08-14. https://arxiv.org/abs/1508.03519
3. Z. Agur, A. S. Fraenkel, S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302. DOI:10.1016/0012-365X(88)90005-2. Accessible copy: https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf
4. V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580. https://arxiv.org/abs/2202.01580
5. J. A. Aledo, A. Barzanouni, G. Malekbala, L. Sharifan, J. C. Valverde, *Counting Periodic Points in Parallel Graph Dynamical Systems*, Complexity (2020), Article 9708347. DOI:10.1155/2020/9708347.
6. E. Goles, J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189.
