# Cartesian-product rigidity of cores of finite spaces
## Finding
Let \(X\) and \(Y\) be nonempty finite \(T_0\)-spaces, identified with their specialization posets, and give \(X\times Y\) the coordinatewise product order. For \((x,y)\in X\times Y\):

- \((x,y)\) is an up beat point exactly when either \(x\) is an up beat point of \(X\) and \(y\) is maximal in \(Y\), or \(y\) is an up beat point of \(Y\) and \(x\) is maximal in \(X\).
- \((x,y)\) is a down beat point exactly when either \(x\) is a down beat point of \(X\) and \(y\) is minimal in \(Y\), or \(y\) is a down beat point of \(Y\) and \(x\) is minimal in \(X\).

Consequently, \(X\times Y\) is minimal in the beat-point sense if and only if both \(X\) and \(Y\) are minimal. If \(C_X\subseteq X\) and \(C_Y\subseteq Y\) are cores, then \(C_X\times C_Y\) is a core of \(X\times Y\). In particular,
\[
\lvert\operatorname{core}(X\times Y)\rvert
=
\lvert\operatorname{core}(X)\rvert\,\lvert\operatorname{core}(Y)\rvert.
\]
The same statements iterate over every finite nonempty Cartesian product.

## Assumptions and scope
A finite \(T_0\)-space is viewed as a finite poset. An up beat point \(x\) is a point for which the strict upper set \(\{x'>x\}\) has a minimum; a down beat point is defined dually. A finite space is minimal if it has no beat points, and a core is a minimal strong deformation retract obtained by deleting beat points. Empty factors are excluded. No assertion is made about weak-point reductions or minimality among all weakly equivalent finite models.

## Proof
For an up beat point, write
\[
S_{(x,y)}=\{(x',y'):(x,y)<(x',y')\}
\]
in the coordinatewise product order. Suppose \(S_{(x,y)}\) has a minimum \((a,b)\).

If \(x\) is not maximal, choose \(x_1>x\). Then \((x_1,y)\in S_{(x,y)}\), so \((a,b)\le (x_1,y)\). Since \(b\ge y\) already, this forces \(b=y\). Similarly, if \(y\) is not maximal, then \(a=x\). Hence \(x\) and \(y\) cannot both be nonmaximal, because that would force the minimum of the strict upper set to equal \((x,y)\), which is not in the strict upper set.

Therefore at least one coordinate is maximal. If \(y\) is maximal, then
\[
S_{(x,y)}=\{(x',y):x'>x\},
\]
which has a minimum exactly when \(\{x'>x\}\) has a minimum, that is, exactly when \(x\) is an up beat point of \(X\). The case where \(x\) is maximal is symmetric. This proves the up-beat characterization. Applying the same argument to the opposite orders gives the down-beat characterization.

If \(X\) and \(Y\) are minimal, the two characterizations show that the product has no beat point. Conversely, if \(x\) is an up beat point of \(X\), choose any maximal \(y\in Y\); then \((x,y)\) is an up beat point of \(X\times Y\). If \(x\) is a down beat point, choose any minimal \(y\in Y\). Thus a nonminimal factor makes the product nonminimal, and the same argument applies to \(Y\).

Now let \(C_X\) and \(C_Y\) be cores. Since each is a strong deformation retract of its ambient finite space, \(C_X\times C_Y\) is a strong deformation retract of \(X\times Y\), by taking the product of the two deformation retractions. The preceding paragraph shows that \(C_X\times C_Y\) is minimal. Hence it is a core of \(X\times Y\). Core uniqueness up to homeomorphism then gives the cardinality formula. Induction gives the finite-product version.

## Verification
The symbolic proof is complete and does not depend on finite enumeration. The accompanying dependency-free program `verify.py` constructs every labeled poset on one through four points, confirms the standard counts \(1,3,19,219\), and checks the two beat-point equivalences on 2,281 product pairs: all pairs of factors of size at most three, together with every four-point factor paired in both orders with every factor of size at most two. It performs 32,720 pointwise beat-characterization checks and 2,281 minimality-equivalence checks. The recorded replay output is `verification_output.txt` and begins with `VERIFY_OK`.

## Relationship to prior work
Barmak and Minian give the finite-space/poset correspondence, the beat-point definitions, the strong deformation retract obtained by deleting a beat point, and the existence and uniqueness up to homeomorphism of cores. Their accessible full text contains no occurrence of the term “product” and does not state the product beat-point classification above. The present result isolates exactly how beat points behave under the Cartesian product and derives multiplicativity of core cardinality from that local classification.

Searches were also run for equivalent formulations involving minimal finite spaces, product posets, Stong cores, product cores, and multiplicativity of core size. No inspected source or searched record supplied an implication-equivalent statement. This is evidence of noncoverage only relative to those searches and inspected material, not an absolute novelty theorem.

## Limitations
The result concerns strong homotopy reduction by beat points. It does not claim that weak-point cores, minimal weak models, simple-homotopy reductions, or graph-homomorphism cores behave multiplicatively under products. The exhaustive computation is a stress test of small cases, not the proof of the general theorem. Older literature not available in full text during the comparison remains a residual originality risk.

## References
1. J. A. Barmak and E. G. Minian, “Simple homotopy types and finite spaces,” arXiv:math/0611158, first version 2006-11-06; Advances in Mathematics 218 (2008), 87–104, doi:10.1016/j.aim.2007.11.019.
2. J. A. Barmak, *Algebraic Topology of Finite Topological Spaces and Applications*, Lecture Notes in Mathematics 2032, Springer, 2011, doi:10.1007/978-3-642-22003-6.
