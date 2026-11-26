# A sharp invariant-measure dichotomy for binary lifts of regular Toeplitz words

## Finding

Fix integers \(p_1\ge6\) and \(q_k\ge4\) for all \(k\ge1\). The binary first-difference lift of the regular Toeplitz system defined below is minimal. It is uniquely ergodic if and only if \(\sum_{k\ge1}q_k^{-1}=\infty\). If the sum converges, the invariant probability measures form a closed line segment whose two endpoints are the only ergodic measures.

More precisely, let \(C_{k,a}\) denote the aligned level-\(k\) tower base with initial lifted symbol \(a\in\{0,1\}\), and put \(P_k=\prod_{j=k}^\infty(1-2/q_j)\). The entire segment in the convergent case is parametrized, uniquely and affinely, by \(t\in[-1,1]\), with
\[
 \mu_t(C_{k,0})=\frac{1+tP_k}{2p_k},\qquad
 \mu_t(C_{k,1})=\frac{1-tP_k}{2p_k}.
\]
The ergodic measures are \(\mu_{+1}\) and \(\mu_{-1}\). In the divergent case both tower-base masses are \(1/(2p_k)\), and every \(t\) in these formulas gives the same unique measure.

## Construction and scope

Let \(w_1=11 0^{p_1-3}\), and set
\[
 w_{k+1}=(w_k0)^{q_k-3}w_k1\,w_k1\,w_k,\qquad p_{k+1}=q_kp_k.
\]
Use the compatible Toeplitz skeletons \(w_k\square\) repeated with period \(p_k\), with the final letter \(\square\) unassigned. Let \(Y\) be the two-sided Toeplitz orbit closure so obtained. These are essential periods: before the next surviving hole, the earlier hole is filled with both symbols, and the skeleton at level \(k\) has exactly one hole residue modulo \(p_k\). The aligned odometer factor has coordinates \(\rho_k:Y\to\mathbb Z/p_k\mathbb Z\) with \(\rho_k(\sigma y)=\rho_k(y)+1\). In phase \(r\) the level-\(k\) hole residue in the coordinates of \(y\) is \(-1-r\pmod {p_k}\).

Define \(\pi(x)_j=x_{j+1}-x_j\pmod2\), \(X=\pi^{-1}(Y)\), and \(C_{k,a}=\{x:\rho_k(\pi(x))=0,\ x_0=a\}\). Both bases are nonempty, since each \(y\in Y\) has precisely two lifts, one for either initial symbol. The sets \(\sigma^r C_{k,a}\), \(0\le r<p_k\), form clopen partitions \(\mathcal P_k\) of \(X\). Generation here is only required modulo invariant null sets; we do not assert a finite set of exceptions to pointwise separation.

## Proof

**Refinement and incidence.** Each \(w_k\) has even parity: \(w_1\) has two ones, and \(w_{k+1}\) contains \(q_k\) copies of \(w_k\) and two extra ones. In a level-\(k+1\) block starting with lift symbol \(b\), the \(q_k\) level-\(k\) beginnings have symbol \(b\) except for the beginning immediately after the first of the two \(w_k1\) blocks. At that beginning the symbol is \(1-b\); crossing the second such block restores \(b\). This count is independent of the unresolved final hole. All the symbols of the lift within a level block (through its last position) are determined by its starting symbol and \(w_k\). Consequently each atom of \(\mathcal P_{k+1}\) sits in a specified atom of \(\mathcal P_k\), and the normalized incidence is
\[
 M_k=q_k^{-1}\begin{pmatrix}q_k-1&1\\1&q_k-1\end{pmatrix}.
\]

**Minimality.** The base Toeplitz system is minimal, and its single-hole densities \(1/p_k\) also make it regular. Choose a base point whose odometer phase is not an embedded integer (the factor is onto the uncountable odometer). Its entire orbit has this property and is dense in \(Y\). It suffices to consider nonempty cylinders specified on intervals \([i,j]\) that contain zero and have at least two coordinates, since any nonempty cylinder contains such a cylinder. Realize the projected word on \([i,j-1]\) in this dense orbit and choose the lift with the prescribed symbol at \(i\). For this point each difference coordinate in the window is eventually outside the hole residue, since a coordinate \(h\) remaining a hole at every stage would imply phase \(-1-h\) in the odometer. At a sufficiently large level the interval lies inside the aligned block containing zero (crossing between consecutive blocks would cross the hole). The atom containing the chosen lift is then contained in the cylinder. Every orbit visits both \(C_{k,0}\) and \(C_{k,1}\) in any full aligned level-\(k+1\) block by the incidence count and visits their translates at the required times. Hence every orbit meets every nonempty cylinder; \(X\) is minimal.

**All invariant probabilities.** For an invariant probability \(\mu\), let \(v_{k,a}=p_k\mu(C_{k,a})\). Invariance and the partitions give \(v_{k,0}+v_{k,1}=1\), and refinement gives \(v_k=M_k v_{k+1}\) for column vectors. Conversely, take a compatible sequence of probability vectors. For each \(N\) choose a point in each \(C_{N,a}\) and place mass \(v_{N,a}/p_N\) on each iterate along the first \(p_N\) steps of that point. These measures have exactly the prescribed masses on \(\mathcal P_k\) whenever \(k\le N\), by refinement and compatibility. A weak-* accumulation point is invariant: the difference of integrals against a continuous function after shifting is bounded by \(2\|f\|_\infty/p_N\), from the endpoints of the finite orbit segments. The accumulation point retains the prescribed masses since the atoms are clopen.

To see uniqueness given those masses, the phase distribution at each level is uniform under every invariant probability because the shift cyclically permutes its residues. Enlarge any fixed coordinate window to an interval \([i,j]\) containing zero. The phases where a hole meets \([i,j-1]\) have total mass at most \((j-i)/p_k\). On every other phase the interval lies inside the aligned block containing zero, and the atom determines the lifted word there. Thus the atom masses determine all cylinder probabilities in the limit. Equivalently, outside the countable set of embedded integer phases (Haar-null in the odometer), every finite interval is determined at some level. This argument makes no assumption about a finite exceptional set of points in \(X\).

**Dichotomy.** Write \(d_k=v_{k,0}-v_{k,1}\). The incidence gives \(d_k=(1-2/q_k)d_{k+1}\). Iteration and \(|d_k|\le1\) imply \(|d_k|\le P_k\). The negative logarithms of the factors are comparable to \(1/q_k\) uniformly on \(q_k\ge4\); thus all \(P_k\) vanish in the divergent case, and there is exactly one compatible family. Otherwise, \(d_k/P_k\) is independent of \(k\), and every \(t\in[-1,1]\) gives a compatible family. The established affine bijection with invariant probabilities identifies the endpoints as the extreme points, hence the only ergodic measures.

## Reproducibility

The companion `verify.py` checks symbolic parities, rational matrices and their four-stage products on finite parameter ranges, and samples the first four steps of three nested word constructions. These are finite checks; the proof above supplies the infinite-sequence and invariant-measure assertions.

## Relationship to prior work and limitations

Kang and Jäger, *On lifts of strictly ergodic subshifts by permutative sliding block codes*, [arXiv:2609.01140v1](https://arxiv.org/html/2609.01140v1), Thms. 1.5, 5.4 and 6.13, supply the construction and minimality argument. Their aperture-discrepancy lower bound already implies non-unique ergodicity in the summable regime. The explicit conclusion here is the converse for the stated parameter family and the full invariant simplex with its tower-base masses; the incidence and inverse-limit method itself is standard (see Bezuglyi, Karpel and Kwiatkowski, *Exact number of ergodic invariant measures for Bratteli diagrams*, [arXiv:1709.00055v3](https://arxiv.org/html/1709.00055v3), Remark 7.4 and §7.2). The result does not classify general Toeplitz systems, other filling schemes, or other permutative lifts, and does not assert mixing or spectral equivalence.
