# Klein-four symmetry of four-robust ladder clique complexes

## Finding

Let \(L_n=P_2\square P_n\) be the ladder graph with two rows and \(n\ge4\) columns. Let \(K_n=\operatorname{Cliq}_4(L_n)\) consist of vertex subsets containing no independent four-set. The commuting involutions \(a\) (interchange rows) and \(b\) (reverse columns) act simplicially on \(K_n\). Set \(N_n=\binom{n-1}{3}\) and \(f_n=n/2-1\) for even \(n\), \(f_n=0\) for odd \(n\). Then the entire rational homology character in degree five is

\[
\big(\operatorname{tr}(1),\operatorname{tr}(a),\operatorname{tr}(b),\operatorname{tr}(ab)\big)
=(N_n,-N_n,-f_n,f_n).
\]

Every other reduced rational homology group vanishes. More precisely, as a rational representation of \(\langle a,b\rangle\cong C_2\times C_2\),

\[
\widetilde H_5(K_n;\mathbb Q)\cong
\varepsilon_a\otimes\varepsilon_b\otimes
\mathbb Q\left[\binom{[n-1]}3\right],
\]

where \(b\) reverses the \(n-1\) square indices, \(a\) acts trivially on their three-element subsets, and \(\varepsilon_a\), \(\varepsilon_b\) are the respective one-dimensional sign characters. This is an isomorphism of rational modules, not a claim of a canonical integral basis.

For the topological quotients by the indicated subgroups, all reduced rational homology vanishes outside degree five, and the degree-five ranks are

\[
\dim\widetilde H_5(|K_n|/\langle a\rangle;\mathbb Q)=0,\quad
\dim\widetilde H_5(|K_n|/\langle b\rangle;\mathbb Q)=\frac{N_n-f_n}{2},
\]
\[
\dim\widetilde H_5(|K_n|/\langle ab\rangle;\mathbb Q)=\frac{N_n+f_n}{2},\quad
\widetilde H_*(|K_n|/\langle a,b\rangle;\mathbb Q)=0.
\]

## Assumptions and scope

Here \(P_s\) is the undirected path on \(s\) vertices. The vertices of \(L_n\) are \((r,c)\) for \(r\in\{0,1\}\) and \(0\le c<n\); an edge joins vertices in the same column and opposite rows or in the same row and consecutive columns. Define \(a(r,c)=(1-r,c)\) and \(b(r,c)=(r,n-1-c)\). All homology is reduced, and the equivariant and quotient conclusions use rational coefficients except where the published ordinary integral homology is cited. No claim is made for higher-width grids, other robustness parameters or integral equivariant lattice structure.

The required nonequivariant input is the previously published theorem that the total four-cut complex of \(L_n\) is homotopy equivalent to a wedge of \(N_n\) spheres of dimension \(2n-8\). Combinatorial Alexander duality gives

\[
\widetilde H_j(K_n;\mathbb Q)=0\quad (j\ne5),\qquad
\dim\widetilde H_5(K_n;\mathbb Q)=N_n.
\]

These ordinary Betti numbers and the general Alexander-dual relationship are established prior work, not part of the new claim. The new information concerns the action and its quotients.

## Proof

**1. Signed Lefschetz reduction.** Since \(L_n\) is bipartite, König's equality implies \(\alpha(L_n[S])=|S|-\nu(L_n[S])\), with \(\nu\) the size of a maximum matching. Consequently, \(S\in K_n\) implies \(|S|\le6\). Every set with at most three vertices is a face; a four-set is a face precisely when it contains an edge; a five-set is a face precisely when it contains a two-edge matching; and a six-set is a face precisely when it has a perfect matching.

For an involution \(g\), let its vertex orbits of length two be the *pair orbits*, and call its fixed vertices *singleton orbits*. A \(g\)-stable face is a union of \(t\) pair orbits and \(u\) singleton orbits. The simplicial action on its oriented face has sign \((-1)^t\). Its contribution to the **negative** of the reduced Lefschetz number is \((-1)^{t+u}\), including the empty face with contribution \(1\): indeed a nonempty face of size \(2t+u\) has chain degree \(2t+u-1\), and the augmented empty face has degree \(-1\). Since the only reduced homology lies in degree five, \(-\widetilde L(g)=\operatorname{tr}(g_*|\widetilde H_5)\). Therefore the desired trace, not the Lefschetz number itself, is the stated signed sum over invariant faces.

**2. Row exchange.** The \(n\) pair orbits under \(a\) are the vertical rungs. A selection of \(t\) rungs has independence number exactly \(t\): the rung edges form a matching of size \(t\), while bipartite coloring supplies an independent set of size \(t\). Hence precisely the choices \(t=0,1,2,3\) are faces, and

\[
\operatorname{tr}(a)=\sum_{t=0}^{3}(-1)^t\binom nt
=-\binom{n-1}{3}=-N_n.
\]

**3. Column reversal at even width.** Write \(n=2m\), \(m\ge2\). There are \(2m\) pair orbits, two of which each contain a horizontal edge across the middle gap (called *central orbits*). Every one-orbit selection is a face. For a two-orbit selection to be a face, the four vertices must contain an edge. This happens either when a central orbit is chosen (\(4m-3\) choices of orbit pairs) or when two noncentral orbits are adjacent in the half-ladder \(P_2\square P_{m-1}\) (\(3m-5\) choices). Thus there are \(7m-8\) admissible two-orbit selections.

For a three-orbit selection to be a face, its six vertices require a perfect matching. Without a central orbit, the two mirrored halves have three selected vertices each and cannot match across the middle gap. With exactly one central orbit, the other two orbit representatives must be adjacent in the half-ladder; there are \(2(3m-5)\) choices. With both central orbits, the third representative must be one of the two vertices immediately outside the central columns; there are exactly two choices. Consequently there are \(6m-8\) admissible three-orbit selections. Therefore

\[
\operatorname{tr}(b)=1-2m+(7m-8)-(6m-8)=1-m=-f_n.
\]

**4. Column reversal at odd width.** Write \(n=2m+1\), \(m\ge2\). There are \(2m\) pair orbits and two singleton vertices in the central rung. For \(t=0,1\), every selection of pair orbits combined with any subset of the two central vertices is a face. For \(t=2\), this holds precisely when the two orbit representatives are adjacent in \(P_2\square P_m\), for which there are \(2(m-1)+m=3m-2\) choices. If not adjacent, the two mirrored pairs cannot be matched, even after adding one or both middle vertices. A face with three pair orbits and no middle vertex is excluded because its left and right halves each have three vertices. Adding one middle vertex gives seven vertices, also excluded. Adding both middle vertices gives a six-to-eight parity obstruction: the reversal preserves the ladder's bipartition, so the two selected vertices in every pair orbit have the same color, while the central rung contributes one of each color. Such a selection has odd numbers of vertices in both color classes and cannot have an equal \(4+4\) color split required by a perfect matching. Thus every contribution with fixed \(t\le2\) cancels by \(\sum_{u=0}^2(-1)^u\binom2u=0\), and \(\operatorname{tr}(b)=0\).

**5. Combined involution at even width.** Write \(n=2m\). The \(2m\) pair orbits under \(ab\) contain no internal edges. Distinct orbit pairs joined by an edge correspond exactly to the \(3m-2\) edges of the folded half-ladder \(P_2\square P_m\); edges crossing the central gap duplicate a folded rung. Thus exactly \(3m-2\) two-orbit selections give faces. The involution \(ab\) preserves bipartite color classes, so each pair orbit is monochromatic. Three pair orbits contribute an even number of vertices to each color class; a perfect matching of six vertices would require three vertices of each color, which is impossible. Hence

\[
\operatorname{tr}(ab)=1-2m+(3m-2)=m-1=f_n.
\]

**6. Combined involution at odd width.** Write \(n=2m+1\). There is one central pair orbit (the vertical central rung) and \(2m\) noncentral pair orbits. Exactly \(2m\) two-orbit selections use the central orbit; among the noncentral orbits, the \(3m-2\) edges of \(P_2\square P_m\) give all other admissible two-orbit choices. There are therefore \(5m-2\) two-orbit faces. A three-orbit union has a perfect matching precisely when it comprises the central orbit together with two adjacent noncentral representatives, giving \(3m-2\) choices: without the central orbit, each half contains an odd number of selected vertices and no crossing edge; with the central orbit but nonadjacent representatives, two of the four outer vertices remain unmatched. It follows that

\[
\operatorname{tr}(ab)=1-(2m+1)+(5m-2)-(3m-2)=0=f_n.
\]

**7. Representation and quotient.** The module \(\mathbb Q[\binom{[n-1]}3]\) has dimension \(N_n\). Reversal of its square indices fixes \(f_n\) of the three-element subsets: if \(n-1\) is even there are none, while if it is odd each invariant triple consists of the unique central index and one of \((n-2)/2\) exchanged index pairs. Twisting by both sign characters yields exactly the four calculated traces. Because \(C_2\times C_2\) is finite abelian, its rational representations are determined by these four traces, proving the isomorphism. Rational homology of a finite-group quotient equals the invariant part of rational homology (cellular transfer after equivariant triangulation). Averaging the characters gives the four displayed quotient formulas. The full invariant part vanishes because \(a\) acts as minus the identity.

## Verification

The accompanying `verify.py` independently enumerates all invariant faces and their signed contributions for every integer \(4\le n\le36\), testing 99 nonidentity symmetry traces. It also builds every face and the complete augmented simplicial boundary matrices over \(\mathbb F_2\) for \(n=4,5,6,7,8\), checking concentration in degree five with multiplicity \(1,4,10,20,35\). These are finite cross-checks, not a substitute for the counting proof. Run with `python3 verify.py`. Its reproducible output is `verification_output.txt`.

## Relationship to prior work

Chandrakar, Hazra, Rout and Singh, *Topology of total cut complexes and cut complexes of grid graphs* (arXiv:2408.07646), Theorem 1.1 and the proof of Theorem 3.3, establish the nonequivariant ladder total-cut homotopy type and hence (by Alexander duality) the ordinary homology of \(K_n\). Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs* (arXiv:2602.11365), defines these complexes and studies grid homotopy but does not give the simultaneous row/column reversal character. Earlier equivariant results at robustness three do not imply this robustness-four character; the binomial rank and group action must be distinguished.

## Limitations

The complete four-character calculation and quotient formulas are proved for the specified two-row ladders and \(n\ge4\). The proof does not identify a canonical integral basis of three-square cycles, an equivariant homotopy type, quotient integral torsion, or results for general rectangular grids. Published records were compared for direct and stronger implications; nonindexed equivariant results may still exist.

## References

1. H. Chandrakar, N. R. Hazra, D. Rout and A. Singh, *Topology of total cut complexes and cut complexes of grid graphs*, arXiv:2408.07646, Theorem 1.1 and Section 3. https://arxiv.org/abs/2408.07646
2. M. Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first posted February 11, 2026, introduction and Corollary 3. https://arxiv.org/abs/2602.11365
3. A. Björner and M. Tancer, *Note: Combinatorial Alexander duality—a short and elementary proof*, Discrete Comput. Geom. **42** (2009), 586–593.
