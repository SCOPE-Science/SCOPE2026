# Exact one-Frobenius number for a three-generator generalized repunit subfamily

## Finding
For each integer \(b\ge 2\), put
\[
A=b^2+b+1,\qquad G=A+b=(b+1)^2,\qquad H=2A-1=2b^2+2b+1.
\]
Let \(R_b(N)\) be the number of ordered triples \((x,y,z)\in\mathbb Z_{\ge0}^3\) solving \(Ax+Gy+Hz=N\). The exact one-Frobenius number of this triple—the largest \(N\in\mathbb Z_{\ge0}\) with \(R_b(N)\le1\)—is
\[
\boxed{g_1(A,G,H)=4b^3+2b^2-2.}
\]
The residue class modulo \(A\) of the **largest second-representation threshold** is uniquely \(A-2b\). In particular, at \(N=4b^3+2b^2-2\) there is exactly one factorization, whereas every larger nonnegative integer has at least two distinct factorizations.

## Assumptions and scope
The parameter \(b\) is an arbitrary integer at least two. All factorization coefficients are nonnegative integers; distinct coefficients give distinct factorizations even when their resulting integer is the same. Here \(g_1\) uses the at-most-one-representation convention, not the alternative exactly-one convention. Since \(\gcd(A,G)=\gcd(A,b)=1\), the number \(g_1\) exists. These generators constitute the \(n=3\), shift-parameter \(a=b\) instance of the generalized repunit semigroups defined by Branco, Colaço, and Ojeda [1].

## Proof
Write \(B=G+bH\). The identities
\[
(b+1)G=H+bA,\qquad b(b+1)=A-1
\]
will be used throughout. Fix a residue \(r\in\{0,\ldots,A-1\}\). List with multiplicity all the values \(uG+vH\), where \(u,v\ge0\) and \(uG+vH\equiv r\pmod A\), in increasing order. Write \(W_1(r)\) and \(W_2(r)\) for their first and second entries. These exist because \(\gcd(A,G)=1\). For a given \(N\equiv r\pmod A\), its representations by \(A,G,H\) correspond precisely to the pairs \((u,v)\) for which \(uG+vH\le N\); the remaining coefficient of \(A\) is uniquely \((N-uG-vH)/A\). Therefore the first integer in this residue with two representations is \(W_2(r)\), and
\[
g_1(A,G,H)=\max_{0\le r<A}W_2(r)-A.\tag{1}
\]
Indeed, \(W_2(r)-A\) has at most one representation, and all greater integers in the same residue as \(W_2(r)\) have at least two.

For every pair \((u,v)\), uniquely write \(u=(b+1)q+s\) with \(q\ge0\) and \(0\le s\le b\), and set \(z=q+v\). The residue condition becomes \(z\equiv bs-r\pmod A\), with \(z\ge q\); moreover,
\[
uG+vH=sG+zH+qbA.\tag{2}
\]
For fixed \(s\), take \(z_s\in\{0,\ldots,A-1\}\) representing \(bs-r\pmod A\), and set \(V_s=sG+z_sH\). This is the least weight for that \(s\), attained at \(q=0\). If \(z_s\ge1\), the next weight for the same \(s\) is \(V_s+bA\), attained at \(q=1,z=z_s\). If \(z_s=0\), the next is \(V_s+AH\), attained at \(q=0,z=A\). These statements use \(AH>bA\), valid for \(b\ge2\).

First suppose \(1\le r\le b^2\). There are unique \(1\le c\le b\) and \(1\le t\le b\) with \(r=b(c-1)+t\). Set \(e=b-t=bc-r\). Then \(0\le e\le b-1\). The seed weights are
\[
V_s=\begin{cases}
U+sB,&0\le s<c,\\
V+(s-c)B,&c\le s\le b,
\end{cases}
\qquad U=(A-r)H,\quad V=cG+eH.
\]
An exact subtraction gives
\[
U-V=(b+1)A+(b-c)B>0.\tag{3}
\]
Thus \(W_1(r)=V\). For \(e\ge1\), the next weight is \(W_2(r)=V+bA\): the same-\(s\) increase \(bA\) is smaller than the next seed increments \(B>bA\) and \((b+1)A>bA\). If \(e=0\), no same-\(s\) increment of \(bA\) is possible. When \(c<b\), the next seed at \(s=c+1\) gives \(W_2(r)=V+B\); when \(c=b\), the next seed at \(s=0\) gives \(W_2(r)=V+(b+1)A\). The alternatives at the first seed cost \(AH\), which is greater than both \(B\) and \((b+1)A\), respectively.

For \(b^2<r<A\), every \(bs<r\), so \(V_s=(A-r)H+sB\). Since \(A-r\ge1\), the first two weights are \(W_1(r)=(A-r)H\) and \(W_2(r)=(A-r)H+bA\). Finally, at \(r=0\), the first weight is zero and the second is \(W_2(0)=B\), because \(AH>B\).

The largest of the preceding values is
\[
T=bG+(b-1)H+bA,
\]
attained uniquely when \(c=b\) and \(e=b-1\); this is \(r=bc-e=b^2-b+1=A-2b\). Indeed, the case \(e\ge1\) satisfies \(cG+eH+bA\le T\), with equality only there. In the remaining cases, the respective upper bounds are \(bG+bH\), \(bG+(b+1)A\), \(bH+bA\), and \(B\). Each is strictly less than \(T\): the first difference is \(bA-H=(b-2)A+1>0\); the second is \((b-1)H-A>0\); the third is \(bG-H=(b-2)A+b+1>0\); and the fourth follows from \(T-B=(b-1)G+bA-H>0\). Consequently, (1) yields
\[
g_1(A,G,H)=T-A=4b^3+2b^2-2.
\]
At this number the unique representation is \(N=(b-1)A+bG+(b-1)H\). The two different representations of \(N+A\) arising from the winning residue are \(bA+bG+(b-1)H\) and \((2b+1)G+(b-2)H\). This also demonstrates sharpness. \(\square\)

## Verification
The accompanying standalone `verify.py` uses two separate methods. First, it exhaustively enumerates the pairs \((u,v)\) below the proved candidate threshold and compares every residue's second weight with the derived piecewise formula for \(2\le b\le60\) (75,697 residue classes). Second, an unbounded-coin-change dynamic program computes every exact factorization count up to one full residue period past the claimed one-Frobenius number for \(2\le b\le32\). Both methods assert the unique maximizing residue and the closed expression. Run with `python3 verify.py`; the script uses only the Python standard library. These are finite cross-checks of the symbolic proof, not substitutes for the all-\(b\) argument.

## Relationship to prior work
Branco, Colaço, and Ojeda [1] define this generalized repunit family and determine its ordinary Frobenius number, genus, type, and ordinary Apéry sets, but do not give the one-Frobenius number (where exactly one representation is still permitted). Komatsu and Ying [2] develop the higher-representation-number framework and the generalized Apéry formula. Komatsu, Laishram, and Punyani [3] give \(p\)-Frobenius formulas for Jacobsthal/Fibonacci triples; their stated triple shape does not contain this family at \(b\ge2\), as their third generator is \(vaJ_{k-1}(v)+dJ_k(v)\) for positive parameters \(v,d\), whereas the present third generator is \(2A-1\). Liu, Xin, Ye, and Yin [4] supply ordinary Frobenius/genus results for related generalized repunit constructions. The proof here adds an explicit second-factorization threshold calculation for a natural full infinite subfamily, rather than substituting a parameter into an ordinary Frobenius formula.

## Limitations
The claim addresses one precisely defined infinite three-generator family and the at-most-one-representation invariant. It does not provide arbitrary \(p\)-Frobenius numbers, results for larger repunit embedding dimension, or publication-priority certification. The mathematical proof is independent of the finite computational checks. Prior-work comparison is limited to the identified and inspected published material; an unindexed equivalent result remains possible.

## References
[1] M. B. Branco, I. Colaço, I. Ojeda, *The Frobenius problem for generalized repunit numerical semigroups*, arXiv:2112.01106 (first public version December 2, 2021), https://arxiv.org/abs/2112.01106 .

[2] T. Komatsu, H. Ying, *\(p\)-numerical semigroups with \(p\)-symmetric properties*, arXiv:2207.08962 (first public version July 18, 2022), https://arxiv.org/abs/2207.08962 .

[3] T. Komatsu, S. Laishram, P. Punyani, *\(p\)-numerical semigroup of generalized Fibonacci triples*, arXiv:2304.00443 (first public version April 2, 2023), https://arxiv.org/abs/2304.00443 .

[4] F. Liu, G. Xin, S. Ye, J. Yin, *A Note on Generalized Repunit Numerical Semigroups*, arXiv:2306.10738 (first public version June 19, 2023), https://arxiv.org/abs/2306.10738 .
