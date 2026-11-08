# A fifth-degree obstruction to eventual complete symmetry for three consecutive odd generators

## Finding
For each odd integer \(a\ge3\), put \(b=a+2\), \(c=a+4\) and let
\[
 r_a(n)=\#\{(x,y,z)\in\mathbb Z_{\ge0}^3:ax+by+cz=n\}.
\]
Define \(q=(a+1)/4\) when \(a\equiv3\pmod4\) and \(q=(a-1)/4\) when \(a\equiv1\pmod4\); in both cases \(q\in\mathbb Z_{\ge1}\). Define \(P=abc\) and the following positive integers \(K,N,R\):
\[
\begin{array}{c|c|c}
 &a\equiv3\pmod4&a\equiv1\pmod4\\\hline
K&(b^2-7)/2&(2b^2-b-11)/2\\
N&bK+(q-1)P&bK+(q-1)P\\
R&\dfrac{(a+1)(a+4)(a^3-a^2-2a+4)}{32}&\dfrac{a^5+4a^4-7a^3-22a^2+16a+40}{32}
\end{array}
\]
Then the exact consecutive-value identities are
\[
\boxed{r_a(N)=R,\qquad r_a(N+1)=R-1.}
\]
Consequently the \(p\)-representation threshold set \(S_p(a,b,c)=\{n\ge0:r_a(n)>p\}\), at \(p=R-1\), is not a terminal ray and hence not \(p\)-completely-symmetric. In particular, if an integer \(T(a)\) has the property that all \(p\ge T(a)\) give \(p\)-completely-symmetric threshold sets, then \(T(a)\ge R\). In either residue class, \(R=a^5/32+O(a^4)\) as odd \(a\to\infty\).

## Assumptions and scope
All representations are ordered triples of multiplicities, not permutations of coin values; \(n\ge0\) is an integer. Since \(a\), \(a+2\), \(a+4\) are odd and pairwise coprime, their denumerant has an eventual quadratic quasipolynomial. The term \(p\)-completely-symmetric means that the threshold set equals the full ray starting at its least member (equivalently, its least member equals one plus its largest gap). The theorem constructs a specific obstructing threshold for every odd \(a\ge3\); it does not determine the **least** eventual terminal-ray threshold, does not assert that such a threshold always exists, and does not classify all exceptional thresholds.

## Proof
Write \(r(n)=r_a(n)\), \(b=a+2\), \(c=a+4\), and \(P=abc\). Because the three numbers are pairwise coprime, in the generating function
\[
\sum_{n\ge0}r(n)z^n=\frac1{(1-z^a)(1-z^b)(1-z^c)},
\]
all nontrivial roots-of-unity poles are simple, of orders dividing \(P\). Partial fractions at \(z=1\) and the other roots show that \(r(n)\) is the sum of a \(P\)-periodic function and a polynomial of the form \((n^2+3bn)/(2P)+C_0\). The coefficient \(3b=a+b+c\) follows by expanding the denominator through its first-order term at \(z=1\). Hence for every \(n\ge0\),
\[
 r(n+P)-r(n)=n+\frac{P+3b}{2},\qquad
 [r(n+P+1)-r(n+P)]-[r(n+1)-r(n)]=1.
\]
The quantity \((P+3b)/2\) is an integer because \(P\) and \(b\) are odd. Iteration yields
\[
 r(n+tP)=r(n)+t\left(n+\frac{P+3b}{2}\right)+\frac{Pt(t-1)}2\quad(t\in\mathbb Z_{\ge0}).\tag{1}
\]

It remains to evaluate two adjacent denumerants at \(n_0=bK\). Set \(h=(b+1)/2\). The representation equation is
\[
 b(x+y+z)+2(z-x)=n.
\]
At \(n=bK\), the difference \(z-x\) is a multiple of \(b\); at \(n=bK+1\), it is congruent to \(h\pmod b\). Splitting the integer quotient according to its nonnegative or negative sign and enforcing \(x,z\ge0\) gives these exact formulas. For integers \(E\ge0,L>0\) define
\[
 T(E,L)=\sum_{j=0}^{\lfloor E/L\rfloor}\left(1+\left\lfloor\frac{E-Lj}{2}\right\rfloor\right).
\]
Then, for the prescribed positive \(K\),
\[
 r(bK)=T(K,b+2)+T(K,b-2)-1-\lfloor K/2\rfloor,\tag{2}
\]
\[
 r(bK+1)=T(K-h-1,b+2)+T(K+h-1,b-2)-1-\lfloor(K+h-1)/2\rfloor.\tag{3}
\]
For completeness, the terms in the first sum of (2) correspond to \(z-x=bj\), \(j\ge0\), with \(y+2x=K-(b+2)j\). The second sum removes the \(i=0\) term and uses \(z-x=-bi\), \(i\ge1\), with \(y+2v=K-(b-2)i\) after setting \(x=bi+v\). In (3) the corresponding equations have right sides \(K-h-1-(b+2)j\) and \(K+h-1-(b-2)i\). These are bijections, so no solutions are omitted or duplicated.

Here is an elementary closed evaluation rule: if \(m=\lfloor E/L\rfloor\), and \(\eta(E,m)\) counts those \(j\in\{0,\ldots,m\}\) for which \(E-Lj\) is odd, then
\[
 T(E,L)=(m+1)(1+E/2)-Lm(m+1)/4-\eta(E,m)/2.\tag{4}
\]
Both relevant values of \(L\), namely \(b+2\) and \(b-2\), are odd. Thus \(\eta(E,m)=\lfloor(m+1)/2\rfloor\) if \(E\) is even and \(\eta(E,m)=\lfloor m/2\rfloor+1\) if \(E\) is odd. Substituting the two stated formulas for \(K\) into (2)–(4) yields the following complete finite algebraic table. Its entries under \(m\) are the upper indices of the four summands in order: the \(b+2\) and \(b-2\) sums of (2), followed by those of (3).
\[
\begin{array}{c|c|c|c}
a & (m_1,m_2,m_3,m_4)&r(bK)&r(bK+1)\\\hline
4q-1 &(2q-1,\ 2q+1,\ 2q-2,\ 2q+1)&8q^3+6q^2&8q^3+6q^2-q\\
4q+1 &(4q,\ 4q+4,\ 4q-1,\ 4q+4)&32q^3+64q^2+35q+4&32q^3+64q^2+34q+4
\end{array}
\]
(The upper indices in the second and fourth entries include the removed zero term in (2) and (3).) In either case, therefore,
\[
 r(bK+1)-r(bK)=-q.\tag{5}
\]
Apply the first-difference shift identity \(t=q-1\) times to (5). With \(N=bK+(q-1)P\), this gives \(r(N+1)-r(N)=-1\). Using (1) to evaluate \(r(N)\) from the table, and expanding \(b=a+2\), \(P=a(a+2)(a+4)\), gives precisely the two displayed polynomial formulas \(R\). Thus \(r(N)=R\) and \(r(N+1)=R-1\), with \(R\in\mathbb Z_{>0}\) since it is a representation count.

For \(p=R-1\), the element \(N\) belongs to \(S_p\), while \(N+1\) does not. Therefore \(S_p\) cannot be a terminal ray, regardless of its least member. The inequality \(T(a)\ge R\) follows because a putative eventual terminal-ray range beginning at or below \(R-1\) would include this obstruction. The leading coefficient in each polynomial formula is \(1/32\), proving the growth statement. \(\square\)

## Verification
The independent integer checker `check_witnesses.py` evaluates \(r_a(n)\) in two ways: a modular-inverse coin summation and a distinct indexed floor-sum count. It verifies the two base-count polynomials, final witness pair, and six sample instances of the period-shift identity for all 19 odd integers \(3\le a\le39\). Its output is in `check_output.txt`: 190 exact checked assertions. Illustrative \((a,N,R)\) values include \((3,45,14)\), \((5,280,135)\), \((7,1026,781)\), \((9,2497,2456)\), \((11,5343,6705)\), and \((37,531648,2389267)\). These experiments corroborate but do not replace the all-odd-integer proof above.

## Relationship to prior work
Komatsu and Ying's original 2022 paper treats the same three-term arithmetic progression and proves exact generalized Frobenius and genus formulas for \(0\le p\le\lfloor a/2\rfloor\). Its final section explicitly identifies the unsolved larger-\(p\), consecutive-odd case. The present construction concerns \(p\) of fifth-degree size and proves neither their low-level formulas nor a generalized Frobenius formula; it instead supplies an explicit obstruction to terminal-ray behavior. Komatsu and Ying's 2022 theory and Komatsu's 2024 sequel define related \(p\)-symmetry notions, including the stronger complete-symmetry condition. Komatsu, Hyun and Song's 2026 paper on longer runs of consecutive odd integers proves \(p\)-Frobenius formulas for two specific longer-generator families; it does not state the universal three-denomination high-threshold down-step formula derived here. In particular, the three-coin family is not the longer family with cardinality growing with the first generator; its smallest case can overlap as a special case, but the unbounded polynomial in \(a\) is not implied by the reported results. Even-even-odd triples admit a parity decomposition that is inapplicable to these all-odd triples. Existing quasipolynomial theory does imply the period-shift tool; this elementary tool is not claimed as original.

## Limitations
Only an explicit **lower bound** on any eventual complete-symmetry onset is proved, not the sharp onset and not existence of the onset. The construction covers odd \(a\ge3\) and step two only. The \(p\)-Frobenius function is not determined. A different or unindexed source might already contain these exact adjacent denumerant identities or a stronger general threshold result; the literature comparison is best-knowledge rather than proof of global uniqueness. Independent validation has not been performed.

## References
1. T. Komatsu and H. Ying, *The \(p\)-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052v1 (27 June 2022), https://arxiv.org/abs/2206.13052 ; full lawful text https://arxiv.org/html/2206.13052v3 .
2. T. Komatsu and H. Ying, *\(p\)-numerical semigroups with \(p\)-symmetric properties*, arXiv:2207.08962v1 (18 July 2022), https://arxiv.org/abs/2207.08962 .
3. T. Komatsu, *\(p\)-numerical semigroups with \(p\)-symmetric properties, II*, arXiv:2409.02394v1 (4 September 2024), https://arxiv.org/html/2409.02394v1 .
4. T. Komatsu, S. Hyun and K. Song, *\(p\)-numerical semigroup of the sequence of consecutive odd integers*, arXiv:2608.14053v1 (14 August 2026), https://arxiv.org/abs/2608.14053 .
5. T. Komatsu, *Arithmetic approach to \(p\)-numerical semigroups*, RIMS Kyoto Kôkyûroku 2264, https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/2264-01.pdf .
