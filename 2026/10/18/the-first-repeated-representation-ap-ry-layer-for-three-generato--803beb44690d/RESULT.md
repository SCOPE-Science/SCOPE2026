# The first repeated-representation Apéry layer for three-generator generalized repunits

## Finding
For every integer \(b\ge2\), let \(m=b^2+b+1\) and consider the ordered triple
\[
A_b=(m,m+1,m+b+1).
\]
Let \(d_b(N)\) count **ordered coefficient triples** \((x,y,z)\in\mathbb Z_{\ge0}^3\) satisfying \(mx+(m+1)y+(m+b+1)z=N\). For each residue \(0\le r<m\), let \(W_r\) be the least nonnegative \(N\equiv r\pmod m\) having at least two distinct such coefficient triples. Uniquely write
\[
r=(b+1)q+s,\qquad 0\le s\le b,
\]
where \(0\le q\le b\), with \(q=b\) only when \(s=0\). Then the complete first repeated-representation Apéry layer is
\[
 W_r=m K_b(q,s)+r,\qquad
 K_b(q,s)=\begin{cases}
 q+b+2,&s=b,\\
 s+b+2,&0\le s<b,\ q=0,\\
 q+s+b,&0\le s<b,\ q\ge1.
 \end{cases}
\]
In particular, letting \(g_1(A_b)=\max\{N\ge0:d_b(N)\le1\}\) and \(n_1(A_b)=\#\{N\ge0:d_b(N)\le1\}\), one has
\[
g_1(A_b)=\begin{cases}
(2b+1)m-2,&b=2,3,\\
(3b-2)m-3,&b\ge4,
\end{cases}
\qquad
n_1(A_b)=\frac{b(4b^2+b+11)}2.
\]

## Assumptions and scope
All quantities are exact integers; \(b\) ranges over **all** integers at least two. The three generators are distinct and coprime (the first two are consecutive), so eventual multiplicity at least two is guaranteed. We count coefficient triples for the stated **three-element minimal generating set**, not alternative factorizations using the longer infinite generalized repunit sequence. The triple is the case \(a=1,n=3\) of the generalized repunit family \(S_a(b,n)\) in Branco–Colaço–Ojeda. By the source's minimal-generator theorem, these are precisely its minimal generators. For \(p=1\), the definition includes integers with zero **or** one representation, including \(N=0\), which has one representation.

## Proof
Fix \(b\ge2\), \(m=b^2+b+1\), and \(0\le r<m\). Write an arbitrary integer of this residue as \(N=mk+r\) with \(k\ge0\). The defining equation is equivalent to
\[
 mk+r=m(x+y+z)+y+(b+1)z.
\]
Since \(y,z\ge0\) and \(0\le r<m\), there is a unique nonnegative integer \(t\) such that
\[
y+(b+1)z=r+tm.
\]
Put \(h_t=\lfloor(r+tm)/(b+1)\rfloor\) and \(s_t=(r+tm)\bmod(b+1)\), with \(0\le s_t\le b\). Every possible nonnegative pair \((y,z)\) at fixed \(t\) is represented uniquely by an integer \(j\) with \(0\le j\le h_t\), through
\[
 z=h_t-j,\qquad y=s_t+(b+1)j.
\]
The remaining coefficient must equal \(x=k-t-y-z\), so this particular triple exists **if and only if**
\[
 k\ge L_{t,j}:=t+h_t+s_t+bj.
\]
Distinct pairs \((t,j)\) yield distinct triples. In particular, the number of representations at residue \(r\) and height \(k\) is exactly the number of pairs \((t,j)\) in the stated ranges for which \(L_{t,j}\le k\).

Now use \(m=b(b+1)+1\). The smallest required height at fixed \(t\) is \(L_{t,0}\), and its successive increases satisfy
\[
 L_{t+1,0}-L_{t,0}=\begin{cases}
 b+2,&s_t<b,\\2,&s_t=b.
 \end{cases}
\]
Both increments are positive. At \(t=0\), the Euclidean division \(r=(b+1)q+s\) gives \(L_{0,0}=q+s\). If \(q\ge1\), the next candidate in this same row is \(L_{0,1}=q+s+b\), while for \(q=0\) that pair is forbidden. The first candidate in any later row is \(L_{1,0}\), and since the row minima strictly increase no row \(t\ge2\) can precede it. Directly,
\[
L_{1,0}=L_{0,0}+\begin{cases}
 b+2,&s<b,\\2,&s=b.
\end{cases}
\]
Thus the second-smallest element (counting multiplicity, including ties) among **all** admissible heights \(L_{t,j}\) is exactly \(K_b(q,s)\) in the displayed three cases. This proves the complete \(W_r\) formula: at lower heights there is at most one representation, and at this height there are at least two. Adding \(m\) to \(N\) increases \(x\) in each representation by one, so once a residue has two representations it continues to have at least two for all subsequent heights.

For the largest gap, in the four residue regimes the maximal \(W_r\) occurs at the largest admissible \(q,s\). Their respective maximal values are
\[
\begin{array}{c|c}
 s=b&(2b+2)m-2\\
 1\le q\le b-1,\ 0\le s<b&(3b-1)m-3\\
 q=0,\ s<b&(2b+1)m+b-1\\
 q=b,\ s=0&(2b+1)m-1.
\end{array}
\]
The third and fourth entries are strictly smaller than the first. The second minus the first is \((b-3)m-1\), hence the first is largest for \(b=2,3\), while the second is largest for \(b\ge4\). Since the last deficient integer in each residue is \(W_r-m\), this yields the asserted formula for \(g_1(A_b)\), including the exact changeover between \(b=3\) and \(b=4\).

Finally, for each \(r\) the deficient nonnegative elements of that residue are precisely \(r,r+m,\ldots,r+(K_b(q,s)-1)m\). Thus
\[
 n_1(A_b)=\sum_{r=0}^{m-1}K_b(q,s).
\]
Split this sum into \(q=0,0\le s<b\); \(1\le q\le b-1,0\le s<b\); \(0\le q\le b-1,s=b\); and the single boundary \((q,s)=(b,0)\). Substituting the three formulas and evaluating the finite arithmetic sums gives
\[
 \sum_{s=0}^{b-1}(s+b+2)+
 \sum_{q=1}^{b-1}\sum_{s=0}^{b-1}(q+s+b)+
 \sum_{q=0}^{b-1}(q+b+2)+2b
 =\frac{b(4b^2+b+11)}2,
\]
which proves the genus formula.

## Verification
The accompanying self-contained `CHECK.py` counts representations by unbounded-coin dynamic programming for every base \(2\le b\le20\). It verifies the predicted second-representation threshold for all \(3097\) residue classes, and separately checks the resulting Frobenius maxima and gap cardinalities. For bases \(2\le b\le8\), it also independently enumerates the last coefficient and solves the remaining two-coin congruence, comparing exact counts at \(4594\) input integers. Representative pairs \((g_1,n_1)\) are \((33,29)\) for \(b=2\), \((89,75)\) for \(b=3\), and \((207,158)\) for \(b=4\). Finite tests corroborate the symbolic proof, rather than extending its logical scope.

## Relationship to prior work
Branco, Colaço, and Ojeda introduced generalized repunit semigroups and gave their ordinary Apéry sets, usual Frobenius numbers, and usual genera. Their results concern the existence of at least one factorization, not the full location of the first **two** factorizations. Komatsu studied generalized Frobenius numbers for consecutive *repunit-length* generators \(R_n(b),R_{n+1}(b),\ldots\), whereas the present generators have differences \(1,b\), and are not that sequence. Komatsu's shifted-geometric triple results cover integer triples whose successive positive differences have the form \(aB^n(B-1),aB^{n+1}(B-1)\). Here the differences are \(1,b\), so this family does not meet those positive-integer hypotheses uniformly (indeed \(b\ge3\) is impossible). Komatsu and Ying treat equal-spacing arithmetic-progression triples; the consecutive gaps here are unequal. Subwattanachai's restricted triple formula concerns a separate divisibility regime. The present piecewise two-representation threshold and changeover at \(b=4\) were not obtained from those formulas.

## Limitations
The result is exclusively the \(p=1\) threshold for the stated three-generator family; it does not determine higher \(p\)-Apéry layers or claim a general solution for arbitrary three generators. Exhaustive finite checks alone do not prove an infinite formula; the proof is the height ordering above. Comparisons are bounded to the referenced and searched literature, and unexamined broader formulas could affect a future novelty assessment. The mathematical review is not independent validation.

## References
1. M. B. Branco, I. Colaço and I. Ojeda, *The Frobenius problem for generalized repunit numerical semigroups*, arXiv:2112.01106 (v1 submitted 2021-12-02), https://arxiv.org/abs/2112.01106 .
2. T. Komatsu, *The Frobenius number associated with the number of representations for sequences of repunits*, Comptes Rendus Mathématique **361** (2023), 73–89, https://doi.org/10.5802/crmath.394 .
3. T. Komatsu, *The Frobenius number for shifted geometric sequences associated with the number of solutions*, arXiv:2209.13118, https://arxiv.org/abs/2209.13118 .
4. T. Komatsu and H. Ying, *The p-Numerical Semigroup of the Triple of Arithmetic Progressions*, Symmetry **15** (2023), 1328, https://doi.org/10.3390/sym15071328 .
5. S. Subwattanachai, *Generalized Frobenius Number of Three Variables*, arXiv:2309.09149, https://arxiv.org/abs/2309.09149 .
