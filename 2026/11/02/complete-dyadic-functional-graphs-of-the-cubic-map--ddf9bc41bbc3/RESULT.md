# Complete dyadic functional graphs of the cubic map

## Finding

For each integer \(k\ge5\), consider the polynomial function
\[
F_k:\mathbb Z/2^k\mathbb Z\longrightarrow\mathbb Z/2^k\mathbb Z,\qquad F_k(x)=x+x^3.
\]
Its entire directed functional graph has an explicit cycle and fiber census:

1. The even residues are precisely the periodic vertices; the odd residues are leaves of preperiod exactly one. The zero residue is fixed.
2. For each \(r\in\{1,\ldots,k-1\}\), every residue satisfying \(\nu_2(x)=r\) has exact period
\[
L_{k,r}=2^{\max(k-3r,0)}.
\]
There are exactly
\[
C_{k,r}=2^{k-r-1-\max(k-3r,0)}
\]
cycles of this length lying in the valuation-\(r\) stratum. Together with the zero cycle, these are all cycles. In particular the total number of cycles equals \(1+\sum_{r=1}^{k-1}C_{k,r}\).
3. An even vertex \(y\) receives exactly eight odd predecessors if \(y\equiv2\) or \(-2\pmod{32}\), and none otherwise. Every even vertex has exactly one even predecessor.
4. Accordingly the exact indegree multiplicities are
\[
\#\{\deg^-=0\}=2^{k-1},\quad
\#\{\deg^-=1\}=7\cdot2^{k-4},\quad
\#\{\deg^-=9\}=2^{k-4}.
\]
The basins are the cycles with eight additional leaves attached to each cycle vertex congruent to \(\pm2\pmod{32}\); no other branches exist.

## Assumptions and scope

The variable \(k\) ranges over all integers at least five. All residues and predecessors are counted modulo \(2^k\), and a cycle length means least strictly positive period. For a nonzero residue \(x\), the valuation \(\nu_2(x)\) is the largest integer \(r<k\) for which the residue is divisible by \(2^r\). The valuation of zero is not used in period formulas. Directed edges point from each residue to its unique polynomial image; indegree counts distinct residues, not multiplicity of roots as a polynomial.

## Proof

**Even isometry.** For arbitrary even integers \(a,b\),
\[
F(a)-F(b)=(a-b)(1+a^2+ab+b^2).
\]
The parenthetical factor is congruent to \(1\pmod4\). Hence \(\nu_2(F(a)-F(b))=\nu_2(a-b)\) when \(a\ne b\), and the polynomial induces a permutation of the even residues at every dyadic level. Moreover, for every iterate \(G=F^m\) and all even \(a,b\), the quotient \((G(a)-G(b))/(a-b)\) is congruent to \(1\pmod4\): this property is preserved by composition, since all iterates of even arguments remain even.

**Exact periods.** Let \(x\) be nonzero and even, with \(\nu_2(x)=r\). Write \(G_t=F^{2^t}\) and \(\delta_t=G_t(x)-x\) using integer representatives and polynomial iteration over the integers. Initially \(\delta_0=x^3\), so \(\nu_2(\delta_0)=3r\). Since \(x\) and \(x+\delta_t=G_t(x)\) are both even, the preceding quotient law gives an integer \(u_t\) such that
\[
G_t(x+\delta_t)-G_t(x)=\delta_t(1+4u_t).
\]
Consequently
\[
\delta_{t+1}=G_t(G_t(x))-x=2\delta_t(1+2u_t),
\]
and therefore \(\nu_2(\delta_t)=3r+t\) for every \(t\ge0\). If \(3r\ge k\), the point is fixed. Otherwise the \(2^{k-3r}\)-th iterate fixes it modulo \(2^k\), whereas the preceding half-power does not; its least period must therefore be exactly \(2^{k-3r}\). The valuation stratum has \(2^{k-r-1}\) elements. Dividing by the common period gives the stated exact number of cycles. The residue zero is fixed separately.

**Odd fibers.** If odd integers \(a,b\) satisfy \(a\equiv b\pmod8\), then \(a^2\equiv ab\equiv b^2\equiv1\pmod8\). The same difference factorization now yields
\[
\nu_2(F(a)-F(b))=\nu_2(a-b)+2
\]
whenever \(a\ne b\). Direct substitution for the four odd residue classes modulo eight shows
\[
F(a)\equiv
\begin{cases}
2\pmod{32},&a\equiv1,5\pmod8,\\
-2\pmod{32},&a\equiv3,7\pmod8.
\end{cases}
\]
For a fixed class modulo eight there are \(2^{k-3}\) inputs; two give the same output modulo \(2^k\) precisely when their difference is divisible by \(2^{k-2}\). Thus every output in the corresponding class modulo 32 has exactly four inputs from that odd class, by exact counting of both finite residue sets. Two odd classes contribute to each target class, giving exactly eight odd predecessors of each \(y\equiv\pm2\pmod{32}\). All other even targets have none. Every odd input maps to an even residue because \(x(1+x^2)\) is even for odd \(x\).

**Components and indegrees.** Every even vertex has one even predecessor by bijectivity and is periodic. No odd vertex is in the image. There are \(2^{k-1}\) odd vertices, and \(2^{k-4}\) even targets belonging to the two classes \(\pm2\pmod{32}\). Those targets have indegree nine; the remaining \(2^{k-1}-2^{k-4}=7\cdot2^{k-4}\) even targets have indegree one. These identities account for all \(2^k\) vertices and every edge. They also prove the claimed graph structure and the absence of branches of height greater than one. \(\square\)

## Verification

The accompanying standard-library Python program `verify_cubic_dyadic.py` independently constructs every edge, cycles the full even permutation, counts the exact valuation-period pairs, checks the odd-preimage target classes, and checks the indegree histogram for every \(5\le k\le16\). It prints `VERIFY_OK exhaustive_levels=5..16 all_cycles_odd_fibers_and_indegrees` upon success. These finite tests are checks rather than the proof for arbitrary \(k\); the preceding algebraic valuation argument is unrestricted.

## Relationship to prior work

Fan and Liao establish general cycle-lifting and minimal decomposition principles for \(p\)-adic polynomial maps, and explicitly analyze quadratic maps such as \(x\mapsto x^2+x\) on the two-adic integers. The present statement is about the distinct cubic map \(x\mapsto x+x^3\), including the full finite-ring cycle lengths and exact ramified odd-fiber census. The general theorems and the quadratic classification do not state this cubic graph histogram. Other literature on monomial dynamics and polynomial permutation groups supplies relevant context but is not claimed to be absent from the field. A systematic historical-priority certificate is not available; an equivalent deduction in uninspected work remains possible.

## Limitations

Only the specified cubic polynomial on the rings \(\mathbb Z/2^k\mathbb Z\) with \(k\ge5\) is classified. The theorem does not describe odd prime powers, arbitrary cubic coefficients, or continuous two-adic invariant measures. The finite verifier covers a bounded selection of moduli, whereas the proof covers all stated moduli. Historical originality is assessed against the sources inspected, not proved by a negative search; no independent mathematical audit has been performed.

## References

Ai-Hua Fan and Lingmin Liao, *On minimal decomposition of \(p\)-adic polynomial dynamical systems*, arXiv:1010.5583, first public October 27, 2010; *Advances in Mathematics* 228 (2011), 2116–2144. Full author preprint: https://arxiv.org/abs/1010.5583.

David L. desJardins and Michael E. Zieve, *Polynomial Mappings mod p^n*, arXiv:math/0103046, first public March 7, 2001 (the stated results treat odd primes).
