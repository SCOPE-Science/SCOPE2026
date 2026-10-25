# First parity-deep-hole transition in five-dimensional cross-polytope vertex averages

## Finding
Let \(V=\{\pm e_i:1\le i\le5\}\subset\mathbb R^5\), let \(K=\operatorname{conv}(V)=\{x:\|x\|_1\le1\}\), and let \(V_{(k)}=\{(v_1+\cdots+v_k)/k:v_i\in V\}\), with repetitions permitted, for every positive integer \(k\). Then the exact Euclidean Hausdorff distance is
\[
\boxed{d_H(V_{(k)},K)=\begin{cases}1/k,&k=1,2,\\\sqrt5/(2k),&k\ge3.\end{cases}}
\]
Thus the normalized covering radius changes precisely at three summands. The second branch has the established full-lattice \(D_5\) numerical covering radius; the contribution claimed here is the *finite*, bounded-cross-polytope transition and the all-resolution formula, not a new full-lattice covering constant.

## Assumptions and scope
All distances are ordinary Euclidean distances in \(\mathbb R^5\). The ten points are exactly the vertices of the standard regular cross-polytope; no additional points, rotations, or unequal summand weights are included. Hausdorff distance from the finite set to its convex hull equals the maximum nearest-site distance over the convex hull. Integer summands are counted with repetitions. The proof applies to every positive integer \(k\), not merely to a computational cutoff.

## Proof
**Discrete-site characterization.** Multiplication by \(k\) identifies the average set with
\[
\Lambda_k=\{z\in\mathbb Z^5:\|z\|_1\le k,\ \|z\|_1\equiv k\pmod 2\}.
\]
Necessity follows because each signed coordinate unit step changes the parity of the coordinate \(\ell_1\)-norm. Conversely, take \(|z_i|\) steps along the signed coordinate axes toward \(z\) and add \((k-\|z\|_1)/2\) cancelling pairs \(e_1,-e_1\). This constructs a length-\(k\) representation.

For \(y\in kK\), independent coordinate sign reflections allow \(y_i\ge0\). Replacing any integer-site coordinate by its absolute value preserves the site constraints and cannot increase its distance to nonnegative \(y_i\), so we may seek nonnegative sites. Write \(y_i=m_i+f_i\) with \(m_i=\lfloor y_i\rfloor\), \(0\le f_i<1\), and set \(t=k-\sum_i m_i\). Thus \(t\) is a nonnegative integer and \(\sum_i f_i\le t\). Put the fractions in decreasing order \(f_{(1)}\ge\cdots\ge f_{(5)}\). For any \(0\le r\le\min(5,t)\) with \(r\equiv t\pmod2\), rounding up the \(r\) largest fractions yields a legitimate point of \(\Lambda_k\), with squared approximation error
\[
E_r=\sum_{i=1}^5f_i^2+r-2\sum_{i=1}^{r}f_{(i)}.
\]
These are candidate sites; we never assume they exhaust all nearest sites.

**The small-slack cases.** At \(t=0\), necessarily all fractions vanish and the distance is zero. At \(t=1\), write \(u=f_{(1)}\). Since \(f_i^2\le uf_i\) and \(\sum f_i\le1\), the allowed one-up rounding satisfies \(E_1\le u+1-2u\le1\).

At \(t=2\), let \(u=f_{(1)}\), \(v=f_{(2)}\). If \(u\le1/2\), then \(E_0\le u\sum_i f_i\le1\). Otherwise, using \(f_i\le v\) for \(i\ge2\) and \(\sum f_i\le2\), we have
\[
E_0\le u^2+v(2-u),\qquad E_2\le1+(1-u)^2-uv.
\]
The first is at most one whenever \(v\le(1-u^2)/(2-u)\), and the second is at most one whenever \(v\ge(1-u)^2/u\). For \(1/2<u<1\), these conditions cover all \(v\), since \((1-u)^2/u\le(1-u^2)/(2-u)\). Thus the squared error is at most one whenever \(t\le2\).

**The unrestricted parity-rounding bound.** Consider rounding a vector \(f\in[0,1]^5\) to a Boolean vector of prescribed Hamming-weight parity. Put \(\delta_i=|f_i-1/2|\). Nearest-coordinate rounding has squared error \(B=\sum_i(1/2-\delta_i)^2=5/4-\sum_i\delta_i(1-\delta_i)\). If its parity is wrong, flip a coordinate with minimal \(\delta_i\); the squared error rises by \(2\delta_{\min}\). As \(\delta_i(1-\delta_i)\ge\delta_{\min}/2\) for every coordinate, the increase is at most the aggregate deficit. Hence some Boolean vector of either prescribed parity has squared error at most \(5/4\).

For \(t\ge4\), all parity-compatible Boolean weights are feasible: the even weights are \(0,2,4\), and for odd \(t\ge5\) the odd weights are \(1,3,5\). Therefore the preceding bound produces an admissible \(\Lambda_k\)-site with squared error at most \(5/4\).

**The exceptional slack \(t=3\).** Here allowed Boolean weights are one and three; weight five would violate the \(\ell_1\)-budget. Choose a **minimum-error** Boolean rounding of odd parity; the preceding parity-rounding lemma guarantees its squared error is at most \(5/4\). If this minimizer has weight one or three, the bound holds. Otherwise, the minimizer has weight five and therefore is no worse than the best weight-three rounding. This implies \(E_5\le E_3\), or \(f_{(4)}+f_{(5)}\ge1\). Put \(u=f_{(4)}\), \(v=f_{(5)}\). Since the fractions are ordered and their sum is at most three, these conditions imply \(1/2\le u\le2/3\) and \(v\le\min(u,3-4u)\). In particular,
\[
E_3\le3(1-u)^2+u^2+v^2.
\]
For \(1/2\le u\le3/5\), this is at most \(3-6u+5u^2\le5/4\). For \(3/5\le u\le2/3\), it is at most \(12-30u+20u^2\le6/5\). Thus an admissible site is within squared distance \(5/4\) even at \(t=3\). Combining the cases, every \(y\in kK\) has squared distance at most one for \(k\le2\), and at most \(5/4\) for every \(k\ge3\).

**Sharpness.** At \(k=1\), the origin \(y=0\) is distance one from every \(\Lambda_1\)-point. At \(k=2\), the point \(y=e_1\in2K\) is distance one from every nearest allowed even-parity site (for example \(0\)). For every \(k\ge3\), the half-integer vector \(y=(1/2,1/2,1/2,1/2,1/2)\) lies in \(kK\) because \(\|y\|_1=5/2\le k\). Its distance from *every* integer vector is at least \(\sqrt5/2\); this value is attained by the allowed site \(z=0\) when \(k\) is even and \(z=e_1\) when \(k\) is odd. Rescale by \(1/k\) to obtain the exact stated Hausdorff distances for all \(k\).

## Verification
The standalone standard-library checker `check.py` verifies the rounding inequalities by exhaustive quarter-grid tests of every feasible fractional vector for \(t=1,\ldots,6\), and directly constructs parity-lattice sites for the sharp witnesses at \(k=1,\ldots,6\). The observed output was `FIVE_CROSSPOLYTOPE_HAUSDORFF_OK grid_checks= 12890  witness_resolutions=6`. These are exact-rational finite stress tests; the argument above, not the checker, proves the all-\(k\) result.

## Relationship to prior work
Van Hintum (2026) studies the general Hausdorff-convexification threshold under Minkowski averaging. The present object is the precise finite average of the *vertices* of a five-dimensional regular cross-polytope. The earlier simplex-grid result on published-finding corpus computes the corresponding invariant for the vertices of a regular simplex, whose barycentric mesh is an \(A_n\) lattice; its formula does not imply the parity-constrained cross-polytope mesh here. Classical infinite-root-lattice results already give the \(D_5\) covering radius \(\sqrt5/2\), thus covering the numerical large-resolution branch after rescaling, but do not themselves imply that clipping to \(kK\) preserves it precisely from \(k=3\), or the exceptional first two resolutions.

## Limitations
This is a canonical-family geometric theorem, not a universal Hausdorff-convexification estimate. It is restricted to five dimensions and equal-weight averages of the ten vertices; it does not classify arbitrary cross-polytope dimensions or all deep-hole locations. The full text of the closest 2026 general convexification preprint could not be accessed during comparison, so historical priority remains provisional. The constant in the large-resolution branch is classical, not claimed independently new.

## References
1. Peter van Hintum, *The sharp threshold for Hausdorff convexification under Minkowski addition*, arXiv:2606.10815v1, first public 9 June 2026; abstract reviewed, full text inaccessible at review time.
2. *Exact deep-hole spectrum of regular-simplex Minkowski vertex averages*, published public research record 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-deep-hole-spectrum-of-regular-simplex-minkowski-vertex-ave--a5282e569b3d ; full RESULT.md inspected.
3. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, 3rd edition, 1999, classical Euclidean \(D_n\) covering-radius results.
