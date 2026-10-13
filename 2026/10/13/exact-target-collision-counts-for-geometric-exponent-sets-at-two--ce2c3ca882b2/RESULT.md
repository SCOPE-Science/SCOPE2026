# Exact target-collision counts for geometric exponent sets at two-digit moduli

## Finding
Fix integers \(b\ge3\), \(n\ge2\), and \(q\ge1\). Put
\[
a_i=b^i-1\quad(0\le i<n),\qquad M=q b^{n-2},
\]
and count **indexed multiplicity vectors** by
\[
C_{b,n}(q)=\#\left\{(k_0,\ldots,k_{n-1})\in\mathbb Z_{\ge0}^{n}:
\sum_{i=0}^{n-1}k_i=n,\quad
\sum_{i=0}^{n-1}k_i a_i\equiv\sum_{i=0}^{n-1}a_i\pmod M\right\}.
\]
Then, with \((x)_+=\max(x,0)\),
\[
\boxed{C_{b,n}(q)=1+2\mathbf 1_{\{q\mid b-1\}}+(n-3)_+\mathbf 1_{\{b=3,\ q\mid4\}}.}
\]
Consequently the all-ones vector is the unique target-reaching multiplicity vector precisely when \(q\nmid b-1\), and additionally \(q\nmid4\) if \(b=3\) and \(n\ge4\). Equivalently, for \(b=3\), \(n\ge4\), the only forbidden factors are \(q\in\{1,2,4\}\); for \(b\ge4\), the forbidden factors are exactly the positive divisors of \(b-1\). The ternary exception turns on exactly at \(n=4\): \(C_{3,3}(4)=1\) but \(C_{3,4}(4)=2\).

## Assumptions and scope
The exponent positions are labeled \(0,\ldots,n-1\); vectors with different coordinates are counted separately even if the corresponding residues coincide modulo \(M\). This is the coefficient-collision notion used in cyclic coefficient extraction and makes sense even for \(M=1\). The theorem concerns every integer base \(b\ge3\), every size \(n\ge2\), and **all** positive integral factors \(q\) of the modulus \(M=q b^{n-2}\); no primality assumptions are imposed. It makes no assertion about arbitrary moduli not divisible by \(b^{n-2}\) or about globally least valid moduli.

## Proof
Because \(\sum_i k_i=n\), subtracting the constant \(-1\) from each geometric power does not change the target congruence. Thus count the vectors satisfying
\[
\sum_{i=0}^{n-1}k_i b^i\equiv\sum_{i=0}^{n-1}b^i\pmod{q b^{n-2}}.
\]
For \(n=2\), its three candidate vectors have power sums \(2\), \(b+1\), and \(2b\), with the middle one the target. The two other differences are \(\pm(b-1)\), giving exactly \(1+2\mathbf1_{\{q\mid b-1\}}\), as claimed.

Suppose henceforth that \(n\ge3\). Set \(P=b^{n-2}\) and \(L=1+b+\cdots+b^{n-3}\). The target power sum is
\[
T=L+(b+1)P.
\]
Given a candidate vector, put
\[
W=\sum_{i=0}^{n-3}k_i b^i,\qquad r=\sum_{i=0}^{n-3}k_i,
\qquad K=k_{n-2}+b k_{n-1}.
\]
The congruence modulo \(qP\), hence modulo \(P\), forces \(W\equiv L\pmod P\). Since \(0\le L<P\) and \(W\ge0\), there is an integer \(s\ge0\) such that \(W=L+sP\).

**Lower-digit rigidity.** Any representation of \(L+sP\) by the lower denominations \(1,b,\ldots,b^{n-3}\) needs at least \(n-2+bs\) coins. To see this, repeatedly replace \(b\) coins of denomination \(b^j\) with one coin of denomination \(b^{j+1}\), for \(j<n-3\). Each carry reduces the number of coins by \(b-1\) until all coefficients below the largest available denomination are less than \(b\). The terminal representation is unique: it has one coin at each of positions \(0,\ldots,n-4\) and \(1+bs\) coins at position \(n-3\), hence \(n-2+bs\) coins. As \(r\le n\) and \(b\ge3\), \(s\ge1\) would require \(r\ge n-2+b>n\). Therefore \(s=0\) and \(W=L\).

The unique minimal lower representation of \(L\) uses one coin at each lower position, so has \(n-2\) coins. Each inverse carry (splitting one coin of denomination \(b^j\) into \(b\) coins of denomination \(b^{j-1}\)) raises the count by exactly \(b-1\). Thus every lower representation has \(r\equiv n-2\pmod{b-1}\). With \(r\le n\), if \(b\ge4\) there is only \(r=n-2\), and if \(b=3\) there are only \(r=n-2\) and \(r=n\).

In the first case \(r=n-2\), uniqueness of the minimal representation forces the lower coordinates all to be one, and there are exactly two coins left among the upper two positions. Their possible values of \(K\) are \(2\), \(b+1\), and \(2b\), each once. The middle choice is the all-ones vector; the other two have target differences \(\pm(b-1)P\), so each occurs precisely when \(q\mid b-1\).

Only in base \(3\) can \(r=n\) arise. The count exceeds the lower minimum by two, exactly one inverse carry. Every such representation is obtained by splitting one of the \(n-3\) lower coins in positions \(1,\ldots,n-3\); these choices are distinct. There are none for \(n=3\) and precisely \(n-3\) for \(n\ge4\). Both upper coordinates then vanish, giving \(K=0\) and target difference \(-(b+1)P=-4P\). These vectors therefore occur precisely when \(q\mid4\). The two disjoint types and the all-ones vector give the displayed formula. \(\square\)

## Verification
The attached standalone Python 3 program `verify_collision.py` directly enumerates every size-\(n\) indexed multiset (using combinations with repetition, not the carry proof) for all \(3\le b\le9\), \(2\le n\le8\), and \(1\le q\le39\). All \(1911\) parameter triples agree with the formula, including the ternary transition \(C_{3,3}(4)=1\), \(C_{3,4}(4)=2\). Run `python3 verify_collision.py`. The accompanying `verification_output.txt` records the exact result from a completed run. These finite calculations corroborate the theorem but do not establish its universal quantifiers; the carrying proof does.

## Relationship to prior work
Fonollosa's 2026 paper introduced the single-target multiset validity condition and determined the **least valid modulus for the binary set** \(\{2^i-1\}\). Its binary digit-sum lemma and collision framework motivate the present question, but its theorem is specifically binary and does not imply the counted geometric-base classification above. The companion paper develops the permanent/coefficient-extraction interpretation; the accessible abstract states that general criterion rather than the present exact nonbinary fiber sizes. In particular, the new exceptional ternary split and the exhaustive dependence on divisors of \(b-1\) are not consequences of the published binary least-modulus formula by changing a parameter. Related results on general subset sums or arbitrary finite abelian group evaluations do not calculate these indexed collision fibers.

## Limitations
The theorem counts multiplicity vectors rather than distinct residue-multisets when exponent residues collide. It characterizes the arithmetic-progression family of moduli divisible by \(b^{n-2}\), not all moduli and not the globally minimal modulus. No generalization to \(b=2\) is asserted; binary splitting changes a coin count by one and has substantially different collision behavior. The independently stated complete theorem rests on the written carrying proof; finite checks provide only corroboration. Literature comparison cannot rule out unindexed equivalent work, and the companion paper's full text was not available for complete inspection.

## References
1. José A. R. Fonollosa, *Minimum modulus for the unique multiset-sum problem*, arXiv:2607.08366v1 (first publicly submitted 2026-07-09), updated v2 2026-07-14. https://arxiv.org/abs/2607.08366
2. José A. R. Fonollosa, *Ryser, Glynn, and the discrete Fourier transform: orthogonal schemes for the permanent*, arXiv:2607.09949 (2026). https://arxiv.org/abs/2607.09949
