# Affine symmetry identifies the Paley-19 directed flag complex and its homology character
## Finding
Let \(P_{19}\) be the tournament on \(\mathbb Z/19\mathbb Z\) in which \(x\to y\) exactly when \(y-x\) is a nonzero quadratic residue modulo \(19\). Then
\[
\operatorname{dFl}(P_{19})\simeq \bigvee^{154}S^3\vee S^4.
\]
Let
\[
A=\{x\mapsto ax+b: a\in(\mathbb F_{19}^\times)^2,\ b\in\mathbb F_{19}\}\cong C_{19}\rtimes C_9.
\]
The induced action on \(H_4(\operatorname{dFl}(P_{19});\mathbb Q)\) is trivial. The character \(\chi_3\) of the action on \(H_3\) is
\[
\chi_3(g)=\begin{cases}
154,&g=1,\\
2,&g\text{ is a nonidentity translation},\\
1,&g(x)=ax+b\text{ with }a\ne1.
\end{cases}
\]
Consequently, after restriction to the translation subgroup \(C_{19}\),
\[
H_3(\operatorname{dFl}(P_{19});\mathbb Q)\cong 10\mathbf 1\oplus 8\,\mathbb Q(\zeta_{19}).
\]

## Assumptions and scope
The directed flag complex of a tournament is the simplicial complex whose faces are its transitive subtournaments. The statement concerns the canonical Paley tournament at order \(19\) and the explicit affine subgroup \(A\); it does not assert that \(A\) is being newly classified as the full automorphism group, nor does it classify equivariant homotopy types.

## Proof
The nonzero quadratic residues modulo \(19\) are
\[
\{1,4,5,6,7,9,11,16,17\}.
\]
Exact enumeration verifies that every vertex of \(P_{19}\) has outdegree \(9\) and every pair of vertices has exactly \(4\) common out-neighbors. Thus \(P_{19}\) is a doubly regular tournament.

Govc's Proposition 3.4 classifies the two isomorphism types of doubly regular tournaments on \(19\) vertices by the homotopy types of their directed flag complexes: one type has \(\bigvee^{154}S^3\vee S^4\), while the other has \(\bigvee^{135}S^3\). The supplied verifier independently enumerates every transitive vertex subset of \(P_{19}\) and obtains the face vector
\[
(19,171,684,1026,342),
\]
so
\[
\chi(\operatorname{dFl}(P_{19}))=19-171+684-1026+342=-152.
\]
The two published candidate homotopy types have Euler characteristics \(-152\) and \(-134\), respectively. Hence the Paley tournament is the first type, proving the displayed homotopy equivalence. As an independent chain check, the verifier obtains boundary ranks \((18,153,531,341)\) over each of \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{19}\), giving Betti vector \((1,0,0,154,1)\) in each of those fields.

For each quadratic residue \(a\) and each \(b\in\mathbb F_{19}\), the affine map \(x\mapsto ax+b\) preserves the Paley orientation, so it acts simplicially. The group \(A\) has odd order \(171\). Since \(H_4\) is one-dimensional over \(\mathbb Q\), its character has image in the finite torsion subgroup of \(\mathbb Q^\times\), namely \(\{\pm1\}\); odd order forces this character to be trivial.

The verifier next computes the signed simplicial Lefschetz number for all \(171\) elements of \(A\) by enumerating the setwise fixed transitive faces and their orientation signs. It obtains
\[
L(g)=\begin{cases}
-152,&g=1,\\
0,&g\text{ is a nonidentity translation},\\
1,&g(x)=ax+b\text{ with }a\ne1.
\end{cases}
\]
Because the only nonzero rational homology groups are \(H_0\), \(H_3\), and \(H_4\), with trivial characters on \(H_0\) and \(H_4\), the Lefschetz formula gives \(L(g)=2-\chi_3(g)\). This is exactly the stated character.

Finally, over \(\mathbb Q\), the cyclic group \(C_{19}\) has two rational irreducibles: the trivial representation and \(\mathbb Q(\zeta_{19})\), whose dimensions are \(1\) and \(18\), and whose characters at a nonidentity element are \(1\) and \(-1\). If the multiplicities are \(u\) and \(v\), then
\[
u+18v=154,\qquad u-v=2,
\]
so \(u=10\) and \(v=8\).

## Verification
Run `python3 verify.py`. It reconstructs the tournament from the quadratic residues, checks double regularity, enumerates every transitive face, recomputes the face vector and Euler characteristic, computes boundary ranks over five prime fields, verifies all \(171\) affine maps preserve the tournament, and performs the complete signed fixed-face Lefschetz calculation. The expected terminal field is `"status":"VERIFY_OK"`. The checked output is stored in `verification_output.json`.

## Relationship to prior work
Govc [1] proves a complete nonequivariant homotopy classification for doubly regular tournaments through \(27\) vertices. At order \(19\), the published statement gives two homotopy types but does not identify the Paley tournament by name, and the inspected paper text contains no occurrence of “Paley.” The present result identifies the canonical Paley object within that two-type list and determines the complete character of its natural \(171\)-element affine symmetry subgroup on rational homology. The latter information is not determined by the nonequivariant homotopy type.

## Limitations
The homotopy-type step uses Govc's published two-type classification at order \(19\); the supplied computation independently distinguishes which type is Paley and checks homology over several fields, but it is not a fresh integral Smith-form derivation of the entire homotopy classification. The character statement is for the explicit affine Paley subgroup \(A\). No claim is made about integral representation lattices, equivariant attaching maps, or larger orders.

## References
[1] D. Govc, “Computing Homotopy Types of Directed Flag Complexes,” arXiv:2006.05333v1, submitted 2020-06-09. Primary MSC 55-08; Proposition 3.4 treats doubly regular tournaments.
