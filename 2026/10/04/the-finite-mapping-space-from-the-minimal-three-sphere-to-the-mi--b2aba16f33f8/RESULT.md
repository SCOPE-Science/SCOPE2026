# The finite mapping space from the minimal three-sphere to the minimal two-sphere has two-sphere core
## Finding
For the canonical minimal finite sphere models \(X_3=S^0\oplus S^0\oplus S^0\oplus S^0\) and \(X_2=S^0\oplus S^0\oplus S^0\), the compact-open finite mapping space \(\operatorname{Map}(X_3,X_2)\) has exactly \(738\) points and admits \(732\) successive Stong beat-point deletions, with \(128\) up-beat and \(604\) down-beat deletions, leaving exactly the six constant maps. The surviving subspace is canonically order-isomorphic to \(X_2\), has no beat points, and therefore is the core. Hence \(\operatorname{core}(\operatorname{Map}(X_3,X_2))\cong X_2\) and \(\operatorname{Map}(X_3,X_2)\simeq X_2\).

The point count and the complete collapse are exact finite statements, not extrapolations from sampled cases. The certificate records every deletion in one explicit valid beat-point sequence.

## Assumptions and scope
Write \(S^0\) for the two-point antichain and \(\oplus\) for ordinal sum. Thus \(X_3\) has four two-point levels and eight points, while \(X_2\) has three two-point levels and six points. These are the canonical minimal finite models of \(S^3\) and \(S^2\), respectively.

Finite \(T_0\)-spaces are viewed as posets with the specialization order. A continuous map is therefore an order-preserving map. For finite source and target, the specialization order on the compact-open function space is the pointwise order: \(f\le g\) exactly when \(f(x)\le g(x)\) for every source point \(x\).

No statement is made here for arbitrary \(X_n\) and \(X_m\), nor for arbitrary weak orders.

## Proof
The proof is a complete finite certificate.

First enumerate all functions from the eight points of \(X_3\) to the six points of \(X_2\). Retain exactly those satisfying the order-preservation condition for every comparable source pair. The exhaustive enumeration contains exactly \(738\) maps.

Order these \(738\) maps pointwise. The file `DELETION_CERTIFICATE.json` gives an ordered list of \(732\) triples consisting of a deleted map, the type of beat point, and a witness. The verifier reconstructs the full mapping poset rather than trusting precomputed order relations. At each up-beat deletion it checks that the witness is the minimum of the current strict upper set; at each down-beat deletion it checks that the witness is the maximum of the current strict lower set. Consequently each deletion is a strong deformation retract by the standard beat-point theorem. The certificate contains \(128\) up-beat and \(604\) down-beat deletions.

After all \(732\) deletions, precisely six maps remain. They are exactly the constant maps. Sending a target point \(y\in X_2\) to the constant map with value \(y\) is an order isomorphism from \(X_2\) onto this six-point subspace. The verifier also checks directly that this terminal subposet has no beat points. It is therefore a core of the mapping space, and the displayed homotopy equivalence follows.

## Verification
Run `python verify.py` in the directory containing `verify.py` and `DELETION_CERTIFICATE.json`. The expected final line is:

`VERIFY_OK maps=738 deletions=732 up=128 down=604 core=6`

The verifier exhaustively filters all \(6^8\) set maps for monotonicity, rebuilds all pointwise comparabilities among the surviving \(738\) maps, replays every certified beat deletion against the current subposet, identifies the terminal six maps with the constants, checks their inherited order against \(X_2\), and verifies that the terminal subspace has no beat points.

## Relationship to prior work
Barmak and Minian identify the canonical minimal finite models of spheres and the role of finite-space reduction methods. May records that, for finite spaces, the compact-open function-space preorder is the pointwise order, and reviews Stong's characterization of finite-space cores by successive beat-point deletions. Those general results provide the framework used here; they do not supply the \(738\)-point enumeration or the \(732\)-step core certificate for this particular function space.

The result also marks a useful boundary between objectwise finite models and mapping spaces. Although \(X_3\) and \(X_2\) are weak models of \(S^3\) and \(S^2\), respectively, the finite mapping space here is homotopy equivalent to \(X_2\) and hence is connected. In contrast, the classical compact-open mapping space \(\operatorname{Map}(S^3,S^2)\) has infinitely many path components because \([S^3,S^2]\cong\pi_3(S^2)\cong\mathbb Z\). Thus replacing both spheres by their smallest finite models does not preserve this mapping-space homotopy information.

## Limitations
This is an exact result for the single adjacent pair \((X_3,X_2)\). The certificate does not prove a uniform formula for \(\operatorname{Map}(X_n,X_m)\), and the finite computation is not used as evidence for any unproved infinite family. The beat-point sequence is not claimed to be unique. The comparison with the classical mapping space concerns homotopy type and path components, not a natural comparison map between the two function spaces.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156, first public version 2006-11-06.
2. J. P. May, *Finite spaces and larger contexts*, especially Chapter 2 on function spaces and cores and Chapter 3 on non-Hausdorff suspensions.
3. The classical identity \(\pi_3(S^2)\cong\mathbb Z\) is the standard consequence of the Hopf fibration exact sequence.
