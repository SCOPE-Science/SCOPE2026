# A unique involutory translate and trace-rigid two-cycle exclusion for a binary permutation trinomial

## Finding
For every odd integer \(m\ge3\), write \(q=2^m\), \(d=(m+1)/2\), and \(K=\mathbb F_q\). Set
\[
F_\delta(X)=X+X^{2^d-1}+X^{q-2^d+1}+\delta\quad(\delta\in K).
\]
Each \(F_\delta\) is a permutation of \(K\). Precisely \(F_1\) is an involution: it fixes no elements and has exactly \(q/2\) disjoint two-cycles. Every \(F_\delta\) with \(\delta\ne1\) has no point of least period two, and has exactly \(2\) fixed points when the absolute trace \(\operatorname{Tr}_{K/\mathbb F_2}(\delta)\) is zero, and none when it is one. Consequently the full \(q\)-parameter family contains exactly one all-two-cycle permutation, \(q/2\) permutations with two fixed points and no two-cycles, and \(q/2-1\) permutations with neither fixed points nor two-cycles.

## Assumptions and scope
Throughout, \(m\ge3\) is odd; the characteristic is two; exponentiation denotes the polynomial map on the entire field, including zero. A fixed point is a solution of \(F_\delta(x)=x\); a point of *least period two* obeys \(F_\delta^{\circ2}(x)=x\) and \(F_\delta(x)\ne x\). The absolute trace is \(\sum_{j=0}^{m-1}\delta^{2^j}\in\mathbb F_2\). The original unshifted trinomial is Theorem 1 of Ding–Qu–Wang–J. Yuan–P. Yuan (2014), whose first public arXiv version is dated 2014-02-24.

## Proof
Put \(s=2^d\), \(r=s-1\), and define a power permutation \(H:K\to K\) by \(H(u)=u^{s+1}\). Since \(2d=m+1\), the identity \((s-1)(s+1)=2^{m+1}-1\equiv1\pmod{q-1}\) proves that \(H\) is bijective, with inverse \(x\mapsto x^r\). All power identities below also hold at zero. With \(f=F_0\), reducing exponents modulo \(q-1\) gives
\[
(H(u))^r=u,\qquad (H(u))^{q-s+1}=u^s.
\]
Hence, writing \(L(u)=u+u^s\),
\[
f(H(u))=H(u)+L(u),\qquad H(u+1)=H(u)+L(u)+1,
\]
so
\[
F_\delta(H(u))=H(u+1)+1+\delta.\tag{1}
\]
In particular, \(F_1=H\circ T_1\circ H^{-1}\), where \(T_1(u)=u+1\). Translation by one in characteristic two is a fixed-point-free involution on \(K\). This proves that \(F_1\) has exactly \(q\) points of least period two and no fixed point. More generally \(F_\delta=T_{1+\delta}\circ H\circ T_1\circ H^{-1}\), proving every \(F_\delta\) is bijective.

Because \(\gcd(d,m)=1\), an element with \(u^{2^d}=u\) lies in \(\mathbb F_2\), so \(\ker L=\{0,1\}\). Since \(\operatorname{Tr}(u^{2^d})=\operatorname{Tr}(u)\), the image of \(L\) lies in the trace-zero hyperplane. Both have \(q/2\) members, so the image is precisely that hyperplane. As \(F_\delta(H(u))=H(u)+L(u)+\delta\), its fixed points correspond exactly to \(L(u)=\delta\), giving two for trace-zero \(\delta\) and none for trace-one \(\delta\). For odd \(m\), \(\operatorname{Tr}(1)=1\); thus \(F_1\) is automatically in the zero-fixed-point case.

For the exclusion of other two-cycles, fix \(\delta\) and \(u\in K\), and put \(v=H^{-1}(F_\delta(H(u)))\). Applying the identity \(F_\delta(H(t))=H(t)+L(t)+\delta\) twice gives
\[
F_\delta^{\circ2}(H(u))=H(u)+L(u)+L(v).
\]
If \(H(u)\) has period dividing two, then \(L(v)=L(u)\), which by the kernel calculation forces \(v=u\) or \(v=u+1\). In the first case, \(F_\delta(H(u))=H(u)\), so the point is fixed. In the second, compare \(H(v)=H(u+1)=H(u)+L(u)+1\) with \(H(v)=F_\delta(H(u))=H(u)+L(u)+\delta\); this forces \(\delta=1\). Therefore when \(\delta\ne1\), every period-at-most-two point is fixed and no genuine two-cycle exists. Together with the exceptional case and trace-fiber count, this proves the theorem.

## Verification
The accompanying \(\texttt{verify.py}\) uses only the Python standard library. It constructs characteristic-two extension fields from tested irreducible binary polynomials and evaluates the original trinomial and its second iterate directly. It exhaustively tests all \(\delta\) for \(m=3,5,7,9\), and selected trace-zero, trace-one, and exceptional translates for \(m=11,13\); it checks permutation bijectivity, the exact fixed-point census, all least-two-period counts, and the exceptional involution. Its successful output is \(\texttt{VERIFY_OK}\), with \(694\) translate cases and \(351296\) state checks. These finite experiments corroborate, but do not replace, the proof for every odd \(m\).

## Relationship to prior work
Ding, Qu, Wang, Jin Yuan, and Pingzhi Yuan's Theorem 1 [1] proves that \(f\) is a permutation polynomial for all odd \(m>1\). Their proof is about bijectivity of the unshifted polynomial, not the complete additive-translate cycle census. The present exact zero-versus-all two-cycle dichotomy and the trace-controlled fixed-point classification follow from a distinct, explicit power-conjugacy argument. Searches of published mathematical records and related permutation-polynomial literature did not identify a statement implying this theorem. These searches do not constitute an exhaustive priority guarantee.

## Limitations
The result classifies fixed points and primitive two-cycles, not longer cycles. It applies to this specific trinomial for odd binary extension degree \(m\ge3\), not to arbitrary permutations, other shift types, or even extension degree. Historical literature could contain an equivalent conjugacy or period-two calculation not located in the searches. The direct computations verify only finite instances.

## References
[1] C. Ding, L. Qu, Q. Wang, J. Yuan, P. Yuan, *Permutation trinomials over finite fields with even characteristic*, arXiv:1402.5734v1, posted 2014-02-24, Theorem 1. https://arxiv.org/html/1402.5734v1

[2] X.-D. Hou, *Determination of a Type of Permutation Trinomials over Finite Fields, II*, arXiv:1404.1822 (2014), related permutation-trinomial family rather than the present cycle census. https://arxiv.org/abs/1404.1822
