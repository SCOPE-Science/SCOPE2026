# A uniform quantitative Wilf inequality for Proth numerical semigroups

## Finding

For integers \(n\ge3\) and odd \(m\) with \(3\le m<2^n\), let
\[
S=P_m(n)=\langle m2^{n+i}+1:i\ge0\rangle.
\]
Put \(r=\lfloor\log_2m\rfloor\), \(k=n+r\), and \(M=m2^n\). Write \(e=e(S)\) for the embedding dimension, \(g=g(S)\) for the genus (number of positive gaps), \(c=c(S)\) for the conductor (one greater than the largest gap), and \(\nu=|S\cap[0,c)|=c-g\). Then \(e=k+1\) and
\[
\boxed{
 e\nu-c\ \ge\ \frac{(k-1)M^2-(k+1)(2k+1)M+2k}{2}\ >\ 0.}
\]
In particular, Wilf's inequality \(c\le e\nu\) holds *strictly* for every Proth semigroup in this entire odd-parameter family, not only for the previously treated subfamily \(m=2^r+1\).

## Assumptions and scope

All semigroups contain zero and have finite complement in the nonnegative integers. The restrictions \(n\ge3\), \(m\ge3\) odd and \(m<2^n\) are essential to the family stated here; the Cunningham case \(m=1\) is not part of the claim. The integer \(r\) satisfies \(1\le r\le n-1\), and \(k=n+r\) satisfies \(4\le k\le2n-1\). The finite minimal generating set \(\{m2^{n+i}+1:0\le i\le k\}\), its cardinality \(k+1\), and the explicit Apéry description below are established in the cited primary literature.

## Proof

**Step 1: Greedy representatives.** Set \(a=M+1\) and \(b_i=2^i-1\) for \(1\le i\le k\). For each integer \(0\le j\le M\), let \(x_i(j)\) be the greedy coefficients of \(j\) in \(b_1,\ldots,b_k\), and put \(T(j)=\sum_{i=1}^k x_i(j)\). Theorems 5.2–5.3 of Liu–Xin–Ye–Yin give the Apéry representatives modulo \(a\) and the genus:
\[
N_{-j}=T(j)(M+1)+jM\quad(0\le j\le M),
\qquad g=\frac{M(M-1)}2+\sum_{j=1}^M T(j).
\]
The representatives \(N_{-j}\) occupy distinct classes \(-j\pmod a\); the Frobenius number is \(F=\max_jN_{-j}-a\), and \(c=F+1\).

**Step 2: A uniform greedy-weight bound.** Proposition 2.7 of the same source gives \(x_i(j)\in\{0,1,2\}\) for \(i<k\); if any \(x_i(j)=2\) with \(2\le i<k\), then all lower coefficients vanish. Consequently, among \(x_1(j),\ldots,x_{k-1}(j)\), at most one is \(2\) and their sum is at most \(k\). For the top coefficient,
\[
M=m2^n\le(2^{r+1}-1)2^n=2^{k+1}-2^n<2(2^k-1),
\]
so \(x_k(j)=\lfloor j/(2^k-1)\rfloor\le1\). It follows that \(0\le T(j)\le k+1\) for every \(0\le j\le M\), and hence
\[
 g\le\frac{M(M-1)}2+(k+1)M.
\]

**Step 3: Conductor lower bound.** Because \(M>0\), the greedy decomposition of \(M\) is nonempty, so \(T(M)\ge1\). The Apéry representative \(N_{-M}=T(M)(M+1)+M^2\) yields
\[
c\ge N_{-M}-(M+1)+1=M^2+(T(M)-1)(M+1)+1\ge M^2+1.
\]

**Step 4: The strict Wilf margin.** By the known embedding-dimension formula \(e=k+1\) and \(\nu=c-g\),
\[
e\nu-c=k c-(k+1)g
\ge k(M^2+1)-(k+1)\left(\frac{M(M-1)}2+(k+1)M\right)
=\frac{(k-1)M^2-(k+1)(2k+1)M+2k}{2}.
\]
Finally, \((k+1)(2k+1)/(k-1)=2k+5+6/(k-1)\le 2k+7\le4n+5\), since \(k\ge4\) and \(k\le2n-1\). Yet \(M\ge3\cdot2^n>4n+5\) for every \(n\ge3\), the last inequality following at \(n=3\) and then by induction. Thus \((k-1)M>(k+1)(2k+1)\). The claimed right-hand side is strictly positive. \(\square\)

## Verification

An independently implemented modular shortest-path computation reconstructed Apéry sets of \(119\) Proth semigroups for all permitted \(3\le n\le7\), and compared \(599039\) individual representatives against the greedy formula. For every case it checked genus, Frobenius number, the two analytic inequalities and the stated positive Wilf margin. The Python 3 standard-library script `verify.py` executes these finite comparisons. For \(n=3,m=3\), it yields \(k=4,M=24,g=334,F=651,e\nu-c=938\), whereas the certified algebraic lower bound equals \(328\). These are finite checks only; the proof above covers all allowed parameters.

## Relationship to prior work

Srivastava and Thakkar (2023, arXiv:2311.12462v1), Theorems 2.3 and 6.1, establish the embedding dimension for arbitrary odd parameters and Wilf's inequality for the special parameter \(m=2^r+1\). Their paper's abstract is broader than its precise Theorem 6.1; the current theorem claims nothing new on that special subfamily alone. Liu, Xin, Ye and Yin (arXiv:2306.03459v4, March 2025), Theorems 5.2–5.3 and Proposition 2.7, prove an exact arbitrary-parameter Apéry/genus formula. Their theorem is an indispensable *stronger structural input*; the uniform bound and strict all-parameter Wilf inequality here are derived consequences, not independent new Apéry or genus formulas. Those earlier exact formulas make the conclusion accessible, and the novelty is restricted to the explicitly proved uniform inequality and its quantified margin. A literature and mathematical-record comparison did not identify that precise all-parameter inequality in the inspected publications; unindexed or implicit prior deductions remain possible.

## Limitations

The theorem neither resolves Wilf's conjecture for arbitrary numerical semigroups nor provides a new exact genus or Frobenius formula. It treats only \(m\ge3\), odd and less than \(2^n\), with \(n\ge3\). Its absolute quantitative bound is deliberately non-sharp; it is not an equality classification. The proof uses the stated previously published Apéry and embedding-dimension theorems. The novelty of a consequence deduced from those formulas may be judged differently by an independent reviewer; no independent mathematical audit has been performed.

## References

1. P. Srivastava and D. Thakkar, *The Frobenius Problem for the Proth Numbers*, arXiv:2311.12462v1, first posted November 21, 2023, especially Theorems 2.3 and 6.1. https://arxiv.org/html/2311.12462v1
2. F. Liu, G. Xin, S. Ye and J. Yin, *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, arXiv:2306.03459v4 (March 6, 2025; original preprint June 6, 2023), especially Proposition 2.7 and Theorems 5.2–5.3. https://arxiv.org/html/2306.03459v4
3. A. Sammartano, *Numerical semigroups with large embedding dimension satisfy Wilf's conjecture*, arXiv:1111.1863 (2011), a general criterion whose linear embedding-dimension condition does not automatically cover this family. https://arxiv.org/abs/1111.1863
4. S. Eliahou, *Wilf's conjecture and Macaulay's theorem*, J. Eur. Math. Soc. 20 (2018), 2105–2129. The conductor-at-most-three-times-multiplicity criterion does not apply to the present general range. https://ems.press/journals/jems/articles/15545
