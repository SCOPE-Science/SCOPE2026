# A sharp edge-space Kemeny comparison on arbitrary cycle bouquets

## Finding

Let \(G\) be the graph obtained by identifying one vertex of \(m\ge2\) pairwise otherwise disjoint simple cycles with lengths \(\ell_1,\ldots,\ell_m\ge3\). Put
\[
M=\sum_{i=1}^m\ell_i,\qquad
S_2=\sum_{i=1}^m\ell_i^2,\qquad
S_3=\sum_{i=1}^m\ell_i^3.
\]
On the **same set of \(2M\) directed edges**, let \(K_{\mathrm{nb}}\) denote Kemeny's constant for the uniform non-backtracking walk and \(K_{\mathrm e}\) Kemeny's constant for the ordinary edge-based simple random walk, both defined precisely below. Then
\[
\boxed{K_{\mathrm{nb}}=
\frac{(2m-1)^2M}{2m(m-1)}-\frac12-\frac{m-1}{2m}\frac{S_2}{M}}
\]
and
\[
\boxed{K_{\mathrm e}=M+m-1+\frac{S_2-m}{3}-\frac{S_3-M}{6M}.}
\]
The comparison is completely sharp:
\[
\begin{array}{ll}
K_{\mathrm{nb}}>K_{\mathrm e} &\text{exactly for }m=2,\ \{\ell_1,\ell_2\}=\{3,3\}\text{ or }\{3,4\};\\
K_{\mathrm{nb}}=K_{\mathrm e} &\text{exactly for }m=2,\ \{\ell_1,\ell_2\}=\{4,4\};\\
K_{\mathrm{nb}}<K_{\mathrm e} &\text{in every other case.}
\end{array}
\]
Thus preventing immediate reversals increases directed-edge stationary-target hitting time only for two small cycle bouquets, despite accelerating it for every bouquet containing at least three cycles.

## Assumptions and scope

The graph is undirected, unweighted, finite and simple. The cycles intersect **only** in one common hub \(h\); each has length at least three and \(m\ge2\). Write \(\mathcal A=\{(u,v):uv\in E(G)\}\) for the set of directed arcs. For an arc \((u,v)\), the next arc is \((v,w)\). Under the ordinary edge chain \(P_{\mathrm e}\), choose \(w\sim v\) uniformly; under the non-backtracking chain \(P_{\mathrm{nb}}\), choose uniformly among \(w\sim v\) with \(w\ne u\). All vertices have degree at least two, so the latter is defined.

Both chains are irreducible and doubly stochastic, hence have the uniform stationary law \(\pi(a)=1/(2M)\) on \(\mathcal A\). For either chain, its Kemeny constant is
\[
K(P)=\sum_{b\in\mathcal A}\pi(b)\,\mathbb E_a[\tau_b]
=\operatorname{tr}\bigl((I-P+\mathbf1\pi^{\mathsf T})^{-1}\bigr)-1,
\]
where \(\tau_b=\inf\{n\ge0:X_n=b\}\), including \(\tau_a=0\). This quantity does not depend on the starting arc \(a\). The result compares only these two **arc-space** quantities, not a vertex-projected non-backtracking constant. Periodicity is permitted; no mixing-rate statement is asserted.

## Proof

**1. Non-backtracking tour reduction.** Every oriented cycle furnishes one deterministic hub-to-hub tour of length \(\ell_i\), so there are \(2m\) tours, with two opposite orientations per cycle. At the hub, the next tour is chosen uniformly from the \(2m-1\) possibilities other than the immediate reverse of the incoming tour. Set \(t=(2m-1)^{-1}\); on the tour labels the transition matrix is \(Q=t(J-R)\), where \(R\) swaps opposite orientations. This tour chain is irreducible, and the arc chain has deterministic paths between hub choices, hence is irreducible too. Each arc-state transition matrix has column sum one: an arc entering from a vertex \(v\) receives \(\deg(v)\) ordinary predecessor contributions of size \(1/\deg(v)\), respectively \(\deg(v)-1\) allowed non-backtracking predecessor contributions of size \(1/(\deg(v)-1)\).

The transfer relation on each deterministic tour and the matrix determinant lemma, after separating symmetric and antisymmetric pairs of tour orientations, give the **full** characteristic polynomial
\[
\begin{split}
p(z):=\det(zI-P_{\mathrm{nb}})
={}&\prod_{i=1}^{m}(z^{\ell_i}-t)(z^{\ell_i}+t)\\
&\times\left(1-2t\sum_{i=1}^{m}\frac1{z^{\ell_i}+t}\right).
\end{split}
\]
Initially this identity is read away from the displayed denominators; cancellation extends it to a monic polynomial identity of degree \(2M\). Indeed on antisymmetric pair vectors \(Q\) acts as \(tI\), and on symmetric pair vectors it acts as \(-tI+2tJ_m\). Replacing each tour coordinate's spectral variable with \(z^{\ell_i}\) yields the two determinant factors above. This is an exact reduction, not a numerical eigenspectrum guess.

Write \(H(z)=1-2t\sum_i(z^{\ell_i}+t)^{-1}\) and \(F(z)=\prod_i(z^{\ell_i}-t)(z^{\ell_i}+t)\). At \(z=1\), \(H(1)=0\), \(F(1)\ne0\), and \(H'(1)=2tM/(1+t)^2>0\). Therefore eigenvalue one is simple and
\[
K_{\mathrm{nb}}=\frac{p''(1)}{2p'(1)}
=\frac{F'(1)}{F(1)}+\frac{H''(1)}{2H'(1)}.
\]
The logarithmic derivatives are
\[
\frac{F'(1)}{F(1)}
=\frac{M}{1-t}+\frac{M}{1+t},\qquad
\frac{H''(1)}{2H'(1)}
=-\frac12-\frac{1-t}{2(1+t)}\frac{S_2}{M}.
\]
Since \((1-t)/(1+t)=(m-1)/m\), the claimed expression for \(K_{\mathrm{nb}}\) follows. The formula \(K=p''(1)/(2p'(1))\) is obtained by summing \((1-\lambda)^{-1}\) over every non-unit eigenvalue of an irreducible finite chain; diagonalizability is not required.

**2. Ordinary edge chain.** The ordinary arc walk is the composition of the map from an incoming arc to its endpoint and the map from a vertex to a uniformly selected outgoing arc. Reversing the composition gives the ordinary vertex random walk. Therefore the two transition matrices have the same nonzero eigenvalues, counted algebraically. The graph has \(2M\) arc states and \(M-m+1\) vertices, so
\[
K_{\mathrm e}=K_{\mathrm v}+2M-(M-m+1)=K_{\mathrm v}+M+m-1.
\]
For an individual cycle of length \(\ell\), the vertex Kemeny constant is \((\ell^2-1)/6\). The resistance from the hub to a vertex at cyclic offset \(j\) is \(j(\ell-j)/\ell\), and the degree-weighted hub resistance moment is
\[
\mu_\ell=\sum_{v\in C_\ell}\deg_{C_\ell}(v)R_{C_\ell}(h,v)
=\frac{\ell^2-1}{3}.
\]
The weighted resistance identity is \(K_{\mathrm v}=(4M)^{-1}\sum_{u,v}d_ud_vR(u,v)\), with ordered pairs. The degree-weight measure on the bouquet is the sum of the degree-weight measures on its individual cycles: each cycle contributes two units of degree at the hub. For ordered pairs from different cycles, the resistance decomposes as \(R(u,h)+R(h,v)\). Thus the within-cycle contribution to the weighted resistance sum is \(4\sum_i\ell_i K(C_{\ell_i})\), and the cross-cycle contribution is \(4\sum_i(M-\ell_i)\mu_{\ell_i}\). Dividing by \(4M\) gives
\[
K_{\mathrm v}
=\frac1M\sum_{i=1}^m\left[
\ell_i\frac{\ell_i^2-1}{6}
+(M-\ell_i)\frac{\ell_i^2-1}{3}
\right]
=\frac{S_2-m}{3}-\frac{S_3-M}{6M}.
\]
This gives the asserted ordinary edge formula.

**3. Sharp sign classification.** Set \(\Delta=K_{\mathrm e}-K_{\mathrm{nb}}\) and \(A=S_2/3-S_3/(6M)\). Subtraction yields
\[
\Delta=A+\frac{m-1}{2m}\frac{S_2}{M}
-\left(1+\frac1{2m(m-1)}\right)M+\frac{2m-1}{3}.
\]
Treat one length as a real variable \(x\ge3\), keeping the other \(m-1\) lengths fixed and at least three. Then \(M\ge x+3\), \(S_3\ge9M\), and
\[
\frac{\partial A}{\partial x}
=\frac{4x-3x^2/M+S_3/M^2}{6}
\ge\frac{x+9-18/(x+3)}6\ge\frac32.
\]
Also \(S_2<M^2\), because at least two lengths are positive. Consequently
\[
\frac{\partial}{\partial x}\left(\frac{S_2}{M}\right)
=\frac{2x}{M}-\frac{S_2}{M^2}>-1,
\]
and hence
\[
\frac{\partial\Delta}{\partial x}
>\frac32-\frac{m-1}{2m}-1-\frac1{2m(m-1)}
=\frac{m-2}{2m(m-1)}\ge0.
\]
Thus \(\Delta\) is **strictly increasing in each cycle length** for every fixed \(m\ge2\).

At the equal-length point \(\ell_1=\cdots=\ell_m=\ell\), direct substitution gives
\[
\Delta=\frac{(2m-1)\{m(m-1)(\ell-1)(\ell-2)-3\ell\}}{6m(m-1)}.
\]
For \(m\ge3\), this is positive already at \(\ell=3\), and strict coordinate monotonicity covers all larger lengths. For \(m=2\), direct exact evaluations give
\[
\begin{array}{c|rrrr}
\{\ell_1,\ell_2\}&\{3,3\}&\{3,4\}&\{3,5\}&\{4,4\}\\\hline
\Delta&-5/4&-29/42&11/48&0
\end{array}
\]
Strict coordinate monotonicity now proves that these are the only negative or zero cases, finishing the classification. No upper bound on \(m\) or on the cycle lengths is used.

## Verification

The included `checker.py` constructs both transition matrices from the actual graph's directed arcs, verifies uniform stationary columns, and computes \(\operatorname{tr}(I-P+\mathbf1\pi^{\mathsf T})^{-1}-1\) by exact rational Gaussian elimination. It independently checks both closed forms on eight bouquets including unequal lengths and all three sign regimes. It also checks the full sign classification on the integer grid of two, three or four cycles with each length between three and seven, for a total of **799 exact assertions**. Run `python3 checker.py` with Python 3; no third-party modules or external data are needed. The finite tests are consistency checks, not the source of the infinite-dimensional theorem, which is proved above.

## Relationship to prior work

Breen–Faught–Glover–Kempton–Knudson–Oveson (2022 preprint, 2023 journal publication) introduced the non-backtracking edge-space Kemeny comparison, proved formulas for regular and biregular graphs, obtained explicit expressions for **cycle barbells** connected by paths, and numerically explored small graphs. Their numerical findings may already include the small exceptional instances here. Their cycle-barbell transition matrix assumes two distinct degree-three junctions (and gives non-backtracking choices with probability \(1/2\)), whereas a two-cycle single-hub bouquet has one degree-four junction (probability \(1/3\)). Thus the barbell formula cannot be specialized to the common-hub case simply by assigning a path of one vertex. Their stated graph-family results do not imply the arbitrary-length, arbitrary-petal sharp classification.

Breen–Kempton–Knudson–Shumway (2025) study **vertex-space** non-backtracking Kemeny definitions, including pinwheels with equal cycle lengths. Those constants are different observables from \(K_{\mathrm{nb}}\) here; their results are not an edge-space formula or comparison for unequal lengths. Standard one-separation resistance identities and ordinary edge/vertex spectral comparison are prior tools, not claimed new. Faught–Kempton–Knudson (2020) treat cyclically joined flower graphs, a different graph construction. The finding is the combined exact heterogeneous bouquet formulas and their sharp all-size edge-space sign theorem. Search cannot establish absolute priority; specialized unpublished or differently titled results remain a risk.

## Limitations

The model is restricted to one-hub bouquets of at least two simple cycles, with no added trees, bridges, weighted edges or shared paths. Both compared constants use directed-edge states; no conclusion is drawn about vertex-projected constants, mixing times, general cactus graphs or arbitrary non-backtracking chains. Some parameter choices give periodic irreducible chains, for which stationary distribution and Kemeny's constant still exist. No independent mathematical audit has been performed. The novelty comparison is qualified by the possibility of prior equivalent results outside the inspected literature.

## References

1. J. Breen, N. Faught, C. Glover, M. Kempton, A. Knudson and A. Oveson, *Kemeny's constant for non-backtracking random walks*, arXiv:2203.12049, first public version March 22, 2022; *Random Structures & Algorithms* 63 (2023), 343–363. https://arxiv.org/abs/2203.12049 .
2. J. Breen, M. Kempton, A. Knudson and M. Shumway, *On defining Kemeny's constant for non-backtracking random walks*, arXiv:2510.06650, first public version October 8, 2025. https://arxiv.org/abs/2510.06650 .
3. N. Faught, M. Kempton and A. Knudson, *Resistance distance, Kirchhoff index, and Kemeny's constant in flower graphs*, arXiv:2007.03103, first public version July 6, 2020. https://arxiv.org/abs/2007.03103 .
