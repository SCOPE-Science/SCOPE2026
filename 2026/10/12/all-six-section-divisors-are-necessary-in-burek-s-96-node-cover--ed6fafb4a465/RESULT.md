# All six section divisors are necessary in Burek's 96-node cover
## Finding
Let \(W\) be the Weierstrass model in Burek's rank-\(12\) elliptic Calabi--Yau construction, after the two transversal \(A_2\) curves have been resolved, and let
\[
P_1,\ P_2,\ P_6,\ P'_1,\ P'_2,\ P'_6
\]
be the six section images chosen in Burek's equation (7.7) as global divisorial centers for small resolutions of the \(96\) ordinary double points.

Evaluating all six section formulas at every one of the \(96\) nodes gives the following exact incidence profile.

Each of the six section images contains exactly \(32\) nodes. Across the \(96\) nodes, the number lying on exactly \(r\) of the six images is
\[
\boxed{
N_1=44,\quad
N_2=24,\quad
N_3=16,\quad
N_4=8,\quad
N_5=4,\quad
N_6=0.
}
\]
Moreover, the nodes lying on exactly one section are distributed as
\[
\boxed{
6,\ 6,\ 10,\ 6,\ 6,\ 10
}
\]
for
\[
P_1,\ P_2,\ P_6,\ P'_1,\ P'_2,\ P'_6,
\]
respectively.

Consequently every one of the six section divisors is indispensable: omitting any one leaves at least one ordinary double point uncovered. Therefore no proper subset of these six explicit section images covers all \(96\) nodes. In this precise sense, Burek's six-section cover is minimal.

## Assumptions and scope
The statement concerns Burek's explicit Weierstrass model over \(\mathbf C\) and only the six section images in equation (7.7). It does not assert that six is the minimum number of arbitrary Weil divisors, arbitrary sections, or arbitrary local small-resolution centers that could resolve the same nodal model.

Burek proves that the residual singularities away from the two transversal \(A_2\) curves are exactly \(96\) ordinary double points. They are indexed by the \(24\) roots \(v_0\) of
\[
J(v)=481^3B(v)^4-30^4A(v)^3
\]
and the four fourth roots \(t\) satisfying
\[
t^4=\frac{C(v_0)}{-4879},
\]
with
\[
A(z)=z^8+14z^4+1,\qquad
B(z)=z(z^4-1),\qquad
C(z)=z^{12}-33z^8-33z^4+1.
\]
At such a point,
\[
y=0,\qquad
x=\frac{3\cdot481^2 C(v_0)}{-4879\,A(v_0)}t^2.
\]

The six section formulas are the specializations \(P_j(2)\) and \(P_j(2i)\) for \(j\in\{1,2,6\}\) of Appendix A.

## Proof
For each of the \(24\) values \(v_0\) in Burek's Table 1, take the displayed fourth root \(\tau\) and the four values
\[
t=\tau,\ i\tau,\ -\tau,\ -i\tau.
\]
The exact checker first verifies
\[
J(v_0)=0,\qquad
\tau^4=\frac{C(v_0)}{-4879},
\]
so these give precisely the \(96\) node parameters described in Proposition 7.1.

For each of the six labels
\[
P_1,\ P_2,\ P_6,\ P'_1,\ P'_2,\ P'_6,
\]
the checker reconstructs the section coordinates directly from equations (A.2)--(A.6). A section is recorded as incident with a node exactly when both of its coordinates agree with the node coordinates above. All arithmetic is performed in \(\mathbf Q(i)\).

This exhaustive exact comparison produces \(32\) incidences for every section. Grouping the \(96\) nodes by the number of the six section images that contain them gives
\[
44+24+16+8+4=96
\]
nodes with incidence multiplicities \(1,2,3,4,5\), respectively. Counting the multiplicity-one nodes by their unique section gives
\[
6,\ 6,\ 10,\ 6,\ 6,\ 10.
\]

In particular every one of the six section images contains nodes that lie on none of the other five. Hence deleting any one section from the cover leaves those nodes uncovered. Therefore all six are necessary, and the minimum cover size inside this six-section family is exactly \(6\).

As a redundant cross-check, the checker enumerates all subsets of the six sections. No subset of size at most \(5\) covers all \(96\) nodes, while the full six-set does.

## Verification
The source premises were checked in the full text of Burek's paper. Proposition 7.1 gives the \(96\) ordinary double points and their coordinates. Lemma 7.2 identifies the six section images used in the resolution and proves that every node lies on at least one of them. Appendix A gives the exact section formulas, while Appendix B gives the \(24\) node parameters and one witnessing section for each node.

The standalone verifier in `artifacts/verify.py` independently evaluates all six candidate section images at every node rather than using only the single witness recorded in Table 1. It uses exact rational arithmetic in \(\mathbf Q(i)\), verifies all \(24\) roots and fourth-root parameters, reconstructs all \(96\) node coordinates, and checks the six section coordinate pairs. Its output in `artifacts/verification_output.txt` ends in `VERIFY_OK`.

The verifier reproduces
\[
(N_1,N_2,N_3,N_4,N_5)=(44,24,16,8,4),
\]
the six equal total incidence counts \(32\), the unique-node counts
\[
(6,6,10,6,6,10),
\]
and the minimum subset cover size \(6\).

## Relationship to prior work
Burek's paper proves that the chosen six section images cover all \(96\) nodes and uses them successively to construct a projective crepant resolution. Its Table 1 records one witnessing section through each node. It does not state the complete six-by-\(96\) incidence relation, the multiplicity distribution above, or that every one of the six chosen section divisors is necessary.

Kumar and Kuwata provide the elliptic K3 framework and explicit Mordell--Weil sections from which Burek's formulas arise, but their work predates this Calabi--Yau threefold and its \(96\)-node resolution problem.

Targeted searches for the exact source, the six named sections, node-incidence multiplicities, minimal section covers, and indispensable resolution centers did not locate a statement implying the complete incidence profile or its minimal-cover consequence.

## Limitations
Minimality is proved only within the explicit family
\[
\{P_1,P_2,P_6,P'_1,P'_2,P'_6\}.
\]
The result does not exclude a different collection of fewer global divisors or a different global resolution strategy.

The computation concerns the \(96\) ordinary double points and not the two transversal \(A_2\) curves, which are resolved separately in Burek's construction.

## References
D. Burek, “An elliptic Calabi--Yau threefold of Mordell--Weil rank twelve,” arXiv:2610.01276v1, first public 2026-10-01; especially Proposition 7.1, Lemma 7.2, Proposition 7.4, and Appendices A--B.

A. Kumar and M. Kuwata, “Elliptic K3 surfaces associated with the product of two elliptic curves: Mordell--Weil lattices and their fields of definition,” arXiv:1409.2931, Nagoya Mathematical Journal 228 (2017), 124--185.
