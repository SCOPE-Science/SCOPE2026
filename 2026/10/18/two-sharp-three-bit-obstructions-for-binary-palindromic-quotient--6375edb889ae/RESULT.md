# Two sharp three-bit obstructions for binary palindromic quotients

## Finding
Let \(\mathcal P\) denote the positive integers whose *standard binary expansions* are palindromes, and put
\[\mathcal U=\mathbb Z_{>0}\setminus (\mathcal P/\mathcal P).\]
Define \(\mathcal S\) to be the positive integers whose binary expansions either begin `101` and end `001`, or begin `111` and end `011`. Then
\[\mathcal S\subseteq\mathcal U,\qquad
\underline d(\mathcal S)=\frac1{20},\qquad
\overline d(\mathcal S)=\frac1{16}.\]
In particular, \(\underline d(\mathcal U)\ge 11/20\), counting all positive integers. The first forbidden cylinder (`101...001`) was proved by Bai--Meleshko--Riasat--Shallit; the added forbidden cylinder (`111...011`) and the two-cylinder bound are the contribution here.

There is also a complete classification *within the necessary three-leading/three-trailing-bit interval test*: among its \(16\) possible odd prefix/residue cells, only the two cells \((5,1)\) and \((7,3)\) fail the test. In each of the other \(14\) cells, at least one abstract choice of leading bits and length gap satisfies all tested constraints. **This does not assert that any particular integer in one of those cells has a palindromic-quotient representation.**

## Assumptions and scope
A positive binary palindrome has no leading zero and hence is odd. The word *begins* refers to the three highest bits of the standard binary expansion, and *ends* to its three lowest bits. The leading/trailing cylinder definition is meaningful only for lengths at least six; shorter integers are excluded from \(\mathcal S\). A quotient is an integer \(N=A/B\) for some positive \(A,B\in\mathcal P\), with exact equality. For \(X>0\), density means the lower or upper limit of \(|\mathcal S\cap[1,X]|/X\).

Write \(\ell(Y)\) for binary length. Let \(\rho(a)\) reverse the three bits of \(a\in\{4,5,6,7\}\), so \(\rho(4)=1,\rho(5)=5,\rho(6)=3,\rho(7)=7\). If a palindromic denominator has fewer than three bits, right-pad its binary expansion with zeros to form its three-bit leading block. This right padding preserves the identity \(B\equiv\rho(\beta)\pmod8\), since the only cases are \(B=1\) and \(B=3\).

## Proof
**Step 1: necessary length and prefix congruences.** Suppose an odd integer \(N\ge 8\) has \(L=\ell(N)\) bits, leading three-bit value \(p\in\{4,5,6,7\}\), and \(r=N\bmod8\in\{1,3,5,7\}\). Assume \(N=A/B\) with binary palindromes \(A,B\). Let their binary lengths be \(a,b\). Standard length bounds give \(a-b\in\{L-1,L\}\). Let \(\alpha,\beta\in\{4,5,6,7\}\) be the first three bits of \(A,B\), with the above padding convention for short \(B\). Palindromicity gives
\[r\,\rho(\beta)\equiv\rho(\alpha)\pmod8.\]
The fractional leading-value bounds and the length relation give \(t=2^{a-b-L+3}\in\{4,8\}\) and
\[\frac{t\alpha}{\beta+1}<\frac{N}{2^{L-3}}<\frac{t(\alpha+1)}{\beta}.\]
Because \(N\) is odd and \(L\ge4\), its normalized value belongs to \((p,p+1)\). Consequently the open intervals \((p,p+1)\) and \((t\alpha/(\beta+1),t(\alpha+1)/\beta)\) must intersect. Clearing positive denominators, this is precisely the pair
\[t\alpha<(p+1)(\beta+1),\qquad p\beta<t(\alpha+1).\tag{1}\]
Both inequalities and the congruence above are necessary, not in general sufficient, for representability.

**Step 2: exhaustive local classification.** The next table gives one allowed triple \((t,\beta,\alpha)\) satisfying the congruence and (1) whenever one exists. `none` means that exhaustive checking of \(2\cdot4\cdot4=32\) possibilities finds no such triple. The standalone exact-integer checker regenerates every cell and verifies both strict rational endpoint inequalities independently.

| Leading three bits of \(N\) | \(N\bmod 8=1\) | \(3\) | \(5\) | \(7\) |
|---|---|---|---|---|
| `100` | (4,4,4) | (4,4,6) | (4,4,5) | (4,5,6) |
| `101` | none | (4,4,6) | (4,4,5) | (4,4,7) |
| `110` | (8,4,4) | (4,4,6) | (8,5,4) | (4,4,7) |
| `111` | (8,4,4) | none | (8,5,4) | (4,4,7) |

For the existing \((p,r)=(5,1)\) obstruction, the congruence forces \(\alpha=\beta\). If \(t=4\), the upper bound for the normalized quotient is at most \(4(1+1/4)=5\), whereas the normalized value exceeds \(5\); if \(t=8\), the lower bound is at least \(8\cdot4/5=32/5>6\), whereas the normalized value is less than \(6\). This reconstructs the published exclusion.

For the additional \((p,r)=(7,3)\) obstruction, the congruence allows only \((\beta,\alpha)=(4,6),(5,7),(6,4),(7,5)\). When \(t=4\), every corresponding upper quotient bound \(4(\alpha+1)/\beta\) is at most \(7\), so it cannot reach the normalized interval \((7,8)\). When \(t=8\), the pairs \((4,6),(5,7)\) have lower bound \(8\alpha/(\beta+1)>8\), while \((6,4),(7,5)\) have upper bound \(8(\alpha+1)/\beta<7\). No quotient with this prefix and residue exists. Lengths less than six cannot meet the disjoint first-three/last-three conditions except by overlap; a direct check of lengths at most five finds no integer in either cylinder. Thus \(\mathcal S\subseteq\mathcal U\).

**Step 3: exact density of the union.** For each \(k\ge3\), put \(t=2^k\). The complete binary-length shell \([4t,8t)\) contains \(t/8\) elements of \(\mathcal S\) in each of \([5t,6t)\) and \([7t,8t)\), and none in the other two quarters. Shorter complete shells contribute \(t/4+O(1)\) elements. Uniformly for \(u\in[4,8]\), at \(X=ut\) the normalized counting ratio therefore tends along growing \(k\) to
\[F(u)=\frac{\tfrac14+\tfrac18\operatorname{clip}(u-5)+\tfrac18\operatorname{clip}(u-7)}{u},\qquad
\operatorname{clip}(v)=\max(0,\min(1,v)).\]
On the four successive unit intervals this is \(1/(4u)\), \((u-3)/(8u)\), \(3/(8u)\), and \((u-4)/(8u)\). Their minima and maxima are \(1/20\) and \(1/16\), respectively. Endpoint and floor errors are bounded by \(O(1)\), so these are the true lower and upper asymptotic densities. Every even positive integer is outside \(\mathcal P/\mathcal P\), because the quotient of two odd integers cannot be an even integer. The even integers and \(\mathcal S\) are disjoint, hence \(\underline d(\mathcal U)\ge\tfrac12+\tfrac1{20}=\tfrac{11}{20}\).

## Verification
Run `python3 verify.py` in the same directory. This exact-arithmetic program enumerates all \(16\) odd leading/residue cells, independently verifies the open-interval conditions using rational numbers, tests all forbidden integers up to \(2^{10}\) against binary-palindrome denominators below \(2^{15}\), and checks every shell pattern from \(k=3\) through \(k=13\). It prints `VERIFIED`. The finite tests are checks, not a substitute for Steps 1--3; the only exhaustive search required by the infinite proof is over the explicitly enumerated finite \(32\)-state local domain.

## Relationship to prior work
Bai, Meleshko, Riasat, and Shallit (2022), Section 2.4, Theorem 6 and Corollary 1, prove the `101...001` forbidden cylinder and its \(1/40\) lower density. Their Remark 4 invites improving the lower bound using other intervals. The present additional `111...011` cylinder yields the strictly stronger \(1/20\) lower density for explicitly forbidden *odd* integers and determines all exclusions produced by the simple three-bit prefix/residue necessary test. The source's general decision automaton determines representability of individual inputs, but the inspected text does not state the present uniform two-cylinder theorem or density. This comparison is limited to the source passages read and the searches described in the companion review; an independently published extension may exist.

## Limitations
This theorem identifies an explicit subset of the unrepresentable integers, not all unrepresentable integers. The empty-cell classification is complete only for the defined three-bit necessary condition: a nonempty cell is not a sufficient certificate of an actual palindromic quotient. The lower bound \(11/20\) for the full unrepresentable set is not claimed to be sharp. The source already suggests other intervals can improve its bound, and longer-prefix tests may strengthen this result. Independent audit has not been performed.

## References
Bai, J. H.; Meleshko, J.; Riasat, S.; Shallit, J., *Quotients of Palindromic and Antipalindromic Numbers*, arXiv:2202.13694 (first posted February 28, 2022); *INTEGERS* 22 (2022), paper A96, Section 2.4, Theorem 6, Corollary 1, Remark 4. https://arxiv.org/abs/2202.13694 ; https://math.colgate.edu/~integers/w96/w96.pdf
