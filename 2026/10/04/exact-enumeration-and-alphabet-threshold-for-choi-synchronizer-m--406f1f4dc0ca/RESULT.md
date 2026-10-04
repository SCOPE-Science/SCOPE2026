# Exact enumeration and alphabet threshold for Choi synchronizer maps
## Finding
Let \(q=p^m\) be a prime power, and let \(N(q)\) be the number of maps \(\psi:\mathbb F_q^2\to\mathbb F_q\) satisfying, for every \(a,b\in\mathbb F_q\),
\[
\psi(a,b)\ne a,\qquad \psi(a,b)\ne b,\qquad \psi(a+1,b+1)\ne \psi(a,b)+1.
\]
These are exactly the map conditions used in Theorem 10 of Choi's 2026 self-synchronizing single-deletion construction. Define
\[
P_p(r)=(r-1)^p+(-1)^p(r-1).
\]
Then
\[
N(q)=P_p(q-1)^{q/p}\,P_p(q-2)^{q(q-1)/p}.
\]
In particular, such a map exists if and only if \(q\ge 4\). For example, \(N(4)=2304\), so the quartic map displayed by Choi is one of many admissible maps.

## Assumptions and scope
The field order is a prime power \(q=p^m\), with \(p\) the characteristic and \(1\) the multiplicative identity viewed additively in the translation \((a,b)\mapsto(a+1,b+1)\). The result classifies and counts only the maps satisfying the three conditions above. It does not claim that Choi's later DNA-specific encoding and decoding algorithms, which are formulated over \(\mathbb F_4\), automatically extend to every \(q\ge4\).

## Proof
Let \(T(a,b)=(a+1,b+1)\). Since \(1\) has additive order \(p\), every \(T\)-orbit in \(\mathbb F_q^2\) has length \(p\). Choose one representative \((a_0,b_0)\) of an orbit and write its points as \((a_0+i,b_0+i)\), where \(i\in\mathbb F_p\) is identified with the prime subfield. Write
\[
\psi(a_0+i,b_0+i)=z_i+i.
\]
The two avoidance conditions become
\[
z_i\notin\{a_0,b_0\},
\]
while the translation condition becomes
\[
z_{i+1}\ne z_i
\]
with indices taken cyclically modulo \(p\). Thus an orbit contributes exactly the number of proper cyclic colorings of \(p\) positions from the fixed allowed set \(\mathbb F_q\setminus\{a_0,b_0\}\).

If \(a_0=b_0\), that allowed set has \(q-1\) elements. If \(a_0\ne b_0\), it has \(q-2\) elements. The number of proper cyclic colorings with \(r\) colors is
\[
P_p(r)=(r-1)^p+(-1)^p(r-1).
\]
For \(p=2\), this is \(r(r-1)\); for odd \(p\), it is \((r-1)^p-(r-1)\).

There are \(q/p\) diagonal \(T\)-orbits because the diagonal contains \(q\) ordered pairs, and there are \(q(q-1)/p\) off-diagonal orbits. Choices on different orbits are independent. Multiplication of the orbit counts gives
\[
N(q)=P_p(q-1)^{q/p}\,P_p(q-2)^{q(q-1)/p}.
\]

For \(q=2\), an off-diagonal pair has no symbol distinct from both coordinates, so \(N(2)=0\). For \(q=3\), the characteristic is \(3\) and even a diagonal orbit has only two allowed colors on a three-cycle, so \(P_3(2)=0\) and \(N(3)=0\). If \(q\ge4\) has characteristic \(2\), then \(q-2\ge2\) and \(P_2(q-2)>0\). If \(q\ge4\) has odd characteristic, then necessarily \(q\ge5\), so \(q-2\ge3\) and \(P_p(q-2)>0\). The diagonal factor is also positive in both cases. Hence \(N(q)>0\) exactly for \(q\ge4\).

## Verification
The accompanying `verify_psi.py` reconstructs the orbit reduction in additive coordinate models of finite fields, explicitly builds admissible maps for representative prime powers \(q\in\{4,5,8,9,25\}\), checks all three defining inequalities on every ordered pair, verifies the closed count for \(q=4\), and exhaustively confirms nonexistence for \(q=2\) and \(q=3\). These finite checks support the algebra but are not used as a substitute for the general proof.

## Relationship to prior work
Choi's arXiv:2603.27271v1 states the three conditions above for a map over \(\mathbb F_q\) in Theorem 10, then immediately gives an explicit map only for \(q=4\) in Definition 11. The subsequent self-synchronizing DNA algorithms specialize to \(\mathbb F_4\). The earlier 2020 CIS-code paper develops general \(q\)-ary single-deletion correction but predates the self-synchronizing map condition. Targeted searches for the exact map condition, its finite-field existence threshold, an enumeration formula, and equivalent cycle-coloring formulations did not locate a prior result giving the formula above or the sharp \(q\ge4\) threshold.

## Limitations
The literature search cannot prove global novelty, and terminology for equivalent synchronizer maps may differ. The 2020 paper was checked through its bibliographic record and abstract, while the 2026 arXiv paper was inspected in full around the relevant theorem, explicit quartic map, later specialization, conclusion, and references. The result concerns the algebraic map ingredient only; extending every later self-synchronizing DNA step to nonquartic alphabets would require additional work.

## References
1. W.-H. Choi, "Algorithms of self-synchronizing single-deletion-correcting codes," arXiv:2603.27271v1, 28 March 2026. Theorem 10 and Definition 11.
2. W.-H. Choi, H. J. Kim, and Y. Lee, "Construction of single-deletion-correcting DNA codes using CIS codes," Designs, Codes and Cryptography 88 (2020), 2581–2596, DOI: 10.1007/s10623-020-00802-2.
