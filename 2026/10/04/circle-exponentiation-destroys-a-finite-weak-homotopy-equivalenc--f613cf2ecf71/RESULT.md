# Circle exponentiation destroys a finite weak homotopy equivalence
## Finding
Let \(C\) be the four-point minimal finite circle with two minimal and two maximal points, and let \(R\) be the nine-point Cianci--Ottina weakly contractible but noncontractible finite \(T_0\)-space from Figure 1 of arXiv:1608.05307v1. Then the compact-open mapping space \(\operatorname{Map}(C,R)\) has exactly \(461\) points. It admits \(426\) successive Stong beat-point deletions (\(179\) up-beat and \(247\) down-beat) to a \(35\)-point beat-free core. The order complex of that core has simplex vector \((35,94,80,24)\) and admits \(90\) elementary simplicial collapses to a connected graph with \(25\) vertices and \(28\) edges, hence cycle rank \(4\). Therefore \(\operatorname{Map}(C,R)\) has weak homotopy type \(\bigvee^4 S^1\). Since \(R\to *\) is a weak homotopy equivalence, the induced map \(\operatorname{Map}(C,R)\to\operatorname{Map}(C,*)\) is not a weak homotopy equivalence. Thus exponentiation by the four-point finite circle does not preserve weak homotopy equivalences between finite \(T_0\)-spaces.

## Assumptions and scope
Write \(C=\{u_0,u_1,v_0,v_1\}\), with \(u_i<v_j\) for every \(i,j\in\{0,1\}\) and no other strict comparabilities. This is the standard four-point minimal finite model of \(S^1\).

The target \(R\) has points \(c_1,c_2,c_3,b_1,b_2,b_3,a_1,a_2,a_3\). Its cover relations, read from Figure 1 of Cianci--Ottina, are
\[
\begin{aligned}
&c_1,c_2<b_1,\qquad c_1,c_2,c_3<b_2,\qquad c_2,c_3<b_3,\\
&b_1<a_1,a_2,\qquad b_2<a_1,a_3,\qquad b_3<a_2,a_3.
\end{aligned}
\]
The order is the transitive closure of these covers. Cianci--Ottina prove that the order complex \(\mathcal K(R)\) is contractible while \(R\) has no beat points, so \(R\) is weakly contractible but not contractible as a finite space.

For finite \(T_0\)-spaces, continuous maps are order-preserving maps. The compact-open function-space specialization order agrees with pointwise order, so \(f\le g\) in \(\operatorname{Map}(C,R)\) exactly when \(f(x)\le g(x)\) for every \(x\in C\).

## Proof
There are only \(9^4\) set maps \(C\to R\). Exhaustively testing the four source comparabilities against the transitive closure of the target order leaves exactly \(461\) order-preserving maps.

On these \(461\) maps, form the pointwise order. Repeatedly delete a beat point only after verifying its defining witness in the current subspace: for an up-beat point, the strict upper set has a minimum; for a down-beat point, the strict lower set has a maximum. The certificate records \(426\) legal deletions, split as \(179\) up-beat and \(247\) down-beat deletions. The remaining \(35\)-point subspace has no beat points. By Stong's beat-point theorem, each deletion is a strong deformation retract, so this \(35\)-point space is a core of the mapping space.

The order complex of the core is then enumerated exactly from all chains. It has \(35\) vertices, \(94\) edges, \(80\) triangles, and \(24\) tetrahedra. The certificate next gives \(90\) elementary simplicial collapses. At each step the proposed free face is a codimension-one face contained in a unique maximal simplex at that stage. The remaining complex is a connected graph with \(25\) vertices and \(28\) edges. Its first Betti number is therefore
\[
28-25+1=4,
\]
and a connected graph of rank \(4\) is homotopy equivalent to \(\bigvee^4 S^1\). Hence
\[
\mathcal K(\operatorname{Map}(C,R))\simeq \bigvee^4 S^1.
\]
McCord's weak equivalence from a finite space to its order complex yields the asserted weak homotopy type of \(\operatorname{Map}(C,R)\).

Finally, the terminal map \(R\to *\) is a weak homotopy equivalence because \(\mathcal K(R)\) is contractible. But
\[
H_1(\operatorname{Map}(C,R);\mathbb Z)\cong\mathbb Z^4,
\qquad
H_1(\operatorname{Map}(C,*);\mathbb Z)=0.
\]
Therefore the exponentiated map cannot be a weak homotopy equivalence.

## Verification
The standalone verifier `artifacts/verify.py` reconstructs \(C\), \(R\), all \(461\) monotone maps, the full pointwise order, every beat-point witness, every chain in the \(35\)-point core, and every elementary collapse. It also cross-checks `artifacts/certificate.json` against the recomputed proof objects. A successful replay prints:

`VERIFY_OK maps=461 deletions=426 up=179 down=247 core=35 simplices=35,94,80,24 collapses=90 graph=25,28 rank=4`

The finite enumeration and collapse checks are exhaustive; no sampling or timeout inference is used.

## Relationship to prior work
Cianci and Ottina determine the smallest weakly contractible noncontractible finite spaces and give the nine-point model \(R\), including the fact that \(\mathcal K(R)\) is contractible and \(R\) has no beat points. Their paper does not compute \(\operatorname{Map}(C,R)\).

May's treatment of finite function spaces establishes that the compact-open specialization order is the pointwise order and gives the comparability-fence criterion for homotopy of maps. Kukieła develops function spaces, cores, and homotopy theory for Alexandroff spaces in broader generality. These results supply the framework but do not state the \(461\)-map count, the \(35\)-point core, the collapse to rank \(4\), or the resulting failure of preservation of weak equivalences in this example.

Rival's 1976 fixed-point paper is bibliographically relevant because Cianci--Ottina note that the same nine-point poset appears there. The accessible material located for that paper did not provide a function-space computation of the present kind; this remains a literature-comparison risk rather than evidence of coverage.

## Limitations
No minimality statement is made for the counterexample: the calculation proves failure of weak-equivalence preservation for this canonical pair \(C,R\), not that no smaller source or target can do so. No assertion is made here about all weakly contractible finite spaces, about the opposite poset \(R^{\mathrm{op}}\), or about preservation under other mapping-space constructions. The particular simplicial-collapse sequence is a certificate, not a claim of uniqueness.

## References
1. N. Cianci and M. Ottina, *Smallest homotopically trivial non-contractible spaces*, arXiv:1608.05307v1, first public 2016-08-18.
2. J. P. May, *Finite Spaces and Larger Contexts*, Chapter 2, especially the sections on function spaces and homotopy.
3. M. Kukieła, *On homotopy types of Alexandroff spaces*, arXiv:0901.2621v1.
4. I. Rival, *A fixed point theorem for finite partially ordered sets*, Journal of Combinatorial Theory, Series A 21 (1976), 309--318.
