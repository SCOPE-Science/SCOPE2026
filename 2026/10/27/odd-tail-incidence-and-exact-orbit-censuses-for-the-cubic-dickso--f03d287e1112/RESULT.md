# Odd-tail incidence and exact orbit censuses for the cubic Dickson map modulo powers of two

## Finding

Consider the cubic Dickson map \(f(x)=x^3-3x\) on \(\mathbb Z/2^k\mathbb Z\), for any integer \(k\ge1\), and put \(r=k-1\). The preperiod \(\rho_k(x)\) is the least number of iterates before the orbit enters a cycle, and \(\pi_k(x)\) is the length of that eventual cycle. Use the convention \(\nu_2(0)=+\infty\).

**Individual classification.** If \(x=2t\), with \(t\) represented modulo \(2^r\), put \(a(t)=\nu_2(4t(t^2-1))\). Then
\[
\rho_k(2t)=0,\qquad \pi_k(2t)=2^{\max\{0,r-a(t)\}}.
\]
If \(x=2u+1\), with \(u\) represented modulo \(2^r\), put \(w(u)=\nu_2(u(u+1))\). Then
\[
\rho_k(2u+1)=1,\qquad \pi_k(2u+1)=2^{\max\{0,r-4-2w(u)\}}.
\]
Only comparisons of valuations with the modulus precision matter, so these formulas do not depend on the chosen integer representatives.

**Complete period census.** Define \(S=\max\{0,\lfloor(r-5)/2\rfloor\}\). Among the \(2^r\) odd residues (all of preperiod one), exactly \(2^{r-S}\) feed fixed points. For each \(s\in\{1,\ldots,S\}\), exactly \(2^{r-s}\) feed cycles of length \(2^{j_s}\), where \(j_s=r-4-2s\ge1\); no other positive-length classes are fed by odd residues. In particular, the first nontrivial odd-tail target cycles appear precisely when \(k=8\), and the positive exponents \(j_s\) all have the same parity.

The cycles themselves consist entirely of even residues. Writing \(C_{r,j}\) for the number of cycles of length \(2^j\), their census is
\[
C_{r,0}=\begin{cases}2^r,&0\le r\le3,\\12,&r=4,\\20,&r\ge5,\end{cases}
\qquad
C_{r,j}=\begin{cases}2,&r-j\in\{3,4\},\\10,&r-j\ge5,\\0,&\text{otherwise}\end{cases}\quad(j\ge1).
\]
This even-component census is a specialization of the known Chebyshev permutation-period classification; the new non-permutation information is the odd-tail placement described next.

**Distinguished cycles and uniform leaf incidence.** For every \(s\in\{1,\ldots,S\}\), exactly *two* of the ten cycles of length \(2^{j_s}\) receive odd predecessors. Every vertex of each distinguished cycle has exactly \(2^{s+3}\) odd immediate predecessors; every vertex of the other eight cycles at that length has none. Cycles of any other length greater than one have no odd predecessors. This determines the odd-leaf incidence on all nontrivial cycles, not merely total tail counts.

For illustration, modulo \(2^{12}\) there are \(2048\) periodic even states and \(2048\) strictly preperiodic odd states. Of the latter, \(256\) feed fixed points, while \(1024\), \(512\), and \(256\) feed eventual cycles of periods \(32\), \(8\), and \(2\), respectively. In each of those three period classes, exactly two cycles receive odd leaves, uniformly at each vertex.

## Assumptions and scope

All iterates and congruences are in \(\mathbb Z/2^k\mathbb Z\), \(k\ge1\). No orbit outside this finite ring is asserted periodic. The valuation of zero is infinity; its appearance in an exponent expression gives period one. Counts concern labeled residue classes, and a predecessor means one odd residue mapped to the specified even residue in a single application of \(f\). The fixed-point leaf distribution among individual fixed points is not asserted, only its exact aggregate.

## Proof

**1. Periodic even states and one-step odd tails.** Write \(g(t)=4t^3-3t\), so that \(f(2t)=2g(t)\). The reduction of \(g\) modulo two is the identity and \(g'(t)=12t^2-3\) is odd everywhere. Each bijection modulo \(2^h\) therefore lifts uniquely to a bijection modulo \(2^{h+1}\); hence \(g\) permutes \(\mathbb Z/2^r\mathbb Z\). All even residues are periodic. For odd \(x\), the value \(f(x)\) is even. Since the parity classes are disjoint and the even class is invariant and permuted, every odd residue has preperiod exactly one.

**2. The exact dyadic period-lifting identity.** For each integer \(t\),
\[
g(t)-t=4t(t^2-1),\qquad g'(t)\equiv1\pmod4.
\]
If \(t\notin\{0,\pm1\}\), write \(a=\nu_2(g(t)-t)\); then \(a\ge3\). More generally, for any iterate \(G=g^{\circ 2^j}\), the derivative satisfies \(G'(t)\equiv1\pmod4\). If \(\delta=G(t)-t\) has valuation at least three, the integral-polynomial Taylor identity gives
\[
G(G(t))-t=\delta\bigl(1+G'(t)+\delta Q(t,\delta)\bigr)
\]
for an integer polynomial \(Q\). The expression in parentheses is exactly twice an odd integer, so every doubling of the iteration count raises the valuation by exactly one. Induction gives
\[
\nu_2\bigl(g^{\circ 2^j}(t)-t\bigr)=a+j\quad(j\ge0).
\]
For \(t\in\{0,\pm1\}\), the point is fixed. The least period modulo \(2^r\) is therefore \(2^{\max\{0,r-a\}}\), proving the even-state formula.

**3. The even cycle census.** For any \(3\le a<r\), an even \(t\) satisfies \(a(t)=a\) exactly when \(\nu_2(t)=a-2\); there are \(2^{r-a+1}\) such residues. An odd \(t\) has \(a(t)\ge5\), and \(a(t)=a\) precisely when one of \(t-1,t+1\) has valuation \(a-3\) and the other has valuation one. For \(5\le a<r\), these odd residues number \(2^{r-a+3}\). Thus the total number with \(a(t)=a\) is \(2^{r-a+1}\) for \(a=3,4\), and \(5\cdot2^{r-a+1}\) for \(a\ge5\). Each such point has period \(2^{r-a}\); dividing by that period gives two or ten cycles, respectively. Subtracting all nonfixed points from \(2^r\) gives the displayed fixed-point counts, including \(20\) for every \(r\ge5\).

**4. Individual odd-tail periods and counts.** With \(x=2u+1\), direct expansion gives
\[
f(x)=2h(u),\qquad h(u)=4u^3+6u^2-1.
\]
If \(u\) is even, \(h(u)+1=2u^2(2u+3)\), while \(\nu_2(h(u)-1)=1\) unless \(u=0\), when \(h=-1\). If \(u\) is odd, \(h(u)-1=2(u+1)^2(2u-1)\), while \(\nu_2(h(u)+1)=1\) unless \(u=-1\), when \(h=1\). Hence, in both cases, with the convention at zero,
\[
\nu_2(4h(u)(h(u)^2-1))=4+2\nu_2(u(u+1)).
\]
Applying step 2 to \(h(u)\) proves the odd-state period formula. For \(1\le s<r\), exactly \(2^{r-s}\) residue classes \(u\pmod{2^r}\) satisfy \(\nu_2(u(u+1))=s\): each of the neighborhoods of \(0\) and \(-1\) contributes \(2^{r-s-1}\). Those with \(s\le S\) have positive period exponent \(r-4-2s\), while all others feed fixed points. The geometric sum \(2^r-\sum_{s=1}^{S}2^{r-s}=2^{r-S}\) establishes the aggregate fixed-point tail count; it also covers \(r=0\) directly.

**5. Two distinguished cycles and exact uniform incidence.** Fix \(1\le s\le S\), put \(j=r-4-2s\ge1\), and \(q=r-2s-1=j+3\ge4\). For \(u=2^sv\) with \(v\) odd, or \(u+1=2^sv\) with \(v\) odd, the entry value \(h(u)\) respectively has the form
\[
h(u)=-1+2^{2s+1}B_+(v),\quad B_+(v)=v^2(2^{s+1}v+3),
\]
\[
h(u)=1+2^{2s+1}B_-(v),\quad B_-(v)=v^2(2^{s+1}v-3).
\]
For odd \(v\), each \(B_\pm(v)\pmod8\) has a single fixed odd residue: for \(s=1\), the residues are \(7\) and \(1\); for \(s\ge2\), they are \(3\) and \(5\). Each map \(B_\pm\) takes all odd inputs modulo \(2^q\) *four-to-one* onto the one residue class modulo eight. To prove this, the assertion is immediate at precision three. For every odd \(v\) and integer \(a\ge2\), direct expansion gives
\[
\nu_2\bigl(B_\pm(v+2^a)-B_\pm(v)\bigr)=a+1.
\]
Thus two roots separated by \(2^{q-1}\) modulo \(2^q\) land in opposite lifts modulo \(2^{q+1}\), while either root has two lifts producing the same lifted output. Induction preserves four roots for each admissible output at every precision.

Each of the two classes of entry states \(t=h(u)\pmod{2^r}\), specified by the sign and the fixed scaled residue modulo eight, has exactly \(2^{q-3}=2^j\) elements. Every element has period exactly \(2^j\). Each class is invariant under \(g\): for \(\epsilon=\pm1\), the identity
\[
g(\epsilon+\delta)-\epsilon=9\delta+12\epsilon\delta^2+4\delta^3
\]
preserves both \(\nu_2(\delta)=2s+1\) and \(\delta/2^{2s+1}\pmod8\). An invariant set with exactly \(2^j\) elements, all of period \(2^j\), consists of one cycle. The two signs yield two distinct cycles. For a prescribed vertex in either cycle, the congruence for \(B_\pm\) has four solutions for odd \(v\pmod{2^q}\); allowing all representatives modulo \(2^{r-s}\) multiplies this by \(2^{s+1}\). Thus exactly \(2^{s+3}\) odd vertices map to each chosen cycle vertex. Since every odd input was classified in step 4, no other nontrivial cycles admit odd predecessors. This completes the proof.

## Verification

The standalone `verify.py` independently traces every orbit modulo \(2^k\) for \(1\le k\le15\), checking the minimal preperiod, eventual period, cycle counts, odd-tail counts, and exact distinguished-cycle incidence. It also compares dyadic valuation growth of iterates at 99 integer inputs (excluding the three fixed integers). The verifier does not presume that modular exploration proves the infinitely many precisions; that conclusion comes from the induction and elementary valuation counts above.

Run `python3 verify.py` from the directory containing the two files. No external Python packages are required.

## Relationship to prior work

Gassert's *Chebyshev Action on Finite Fields* (arXiv:1209.4396v1, September 20, 2012) gives prime-degree Chebyshev functional graphs over finite fields. Iwasaki and Umeno (arXiv:1602.08238v1, February 26, 2016) determine orbital periods of odd-degree ordinary Chebyshev permutation polynomials modulo powers of two. Lu, Dai, and Li (arXiv:2605.21819v1, May 20, 2026) give a substantially broader analysis of these permutation polynomials, including cycle counts; in particular, the *even-state* cycle census above is not claimed to be novel.

The monic Dickson map \(x^3-3x\) is instead **nonpermuting** on the full binary ring. The doubling conjugacy only applies to its even states; odd residues have no integral half-coordinate. The additional claims here are their sharp one-step entry rule, complete odd-tail target-period census, and the two-of-ten distinguished-cycle uniform leaf-incidence classification. Existing results on the permutation map do not directly enumerate the nonlinear odd input fibres. Related early Chebyshev-period work by Ishii (2008) addresses permutation Chebyshev periodicity rather than the specified monic odd branch, although its entire Japanese full text was not inspected.

## Limitations

The result is specific to \(x^3-3x\) and moduli \(2^k\). It classifies the odd-preperiod-one distribution and odd incidence on nonfixed cycles, but it does not give each individual fixed vertex's odd indegree. Some even-cycle formulas are already encompassed by prior work on the ordinary Chebyshev permutation polynomial. The principal originality risk is an equivalent odd-fibre classification in unlocated literature or as an unstated derived consequence of broader finite-ring dynamical formulas. No independent mathematical audit has been conducted.

## References

1. T. A. Gassert, *Chebyshev Action on Finite Fields*, arXiv:1209.4396v1 (September 20, 2012), https://arxiv.org/abs/1209.4396.
2. A. Iwasaki and K. Umeno, *Three Theorems on odd degree Chebyshev polynomials and more generalized permutation polynomials over a ring of module \(2^w\)*, arXiv:1602.08238v1 (February 26, 2016), https://arxiv.org/abs/1602.08238.
3. X. Lu, Y. Dai, C. Li, *Graph Structure of Chebyshev Permutation Polynomials over Binary and Ternary Adic Rings*, arXiv:2605.21819v1 (May 20, 2026), https://arxiv.org/abs/2605.21819.
4. M. Ishii, *Periodicity of Chebyshev Polynomials over the Residue Ring of \(\mathbb Z/2^r\mathbb Z\) and An Electronic Signature*, Transactions of the Japan Society for Industrial and Applied Mathematics 18 (2008), 257–265, doi:10.11540/jsiamt.18.2_257.
