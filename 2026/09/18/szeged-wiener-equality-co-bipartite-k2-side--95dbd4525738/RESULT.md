# Exact Szeged–Wiener equality in a co-bipartite class

## Status and provenance

This record gives a correct compact derivation and computational verification of the
two-vertex-side co-bipartite specialization of the Szeged–Wiener equality problem.

An independent audit on 29 September 2026 found that the original originality wording
was incomplete. A broader SCOPE record,

`2026/09/18/szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8`,

was committed at 2026-09-18 03:47:31 UTC and already contained the general
\((n-2)\)-clique formulas, including the adjacent-\(x,y\) case and the same equality
classification below (with the roles of the symbols \(C,D\) interchanged). This record
was committed later, at 2026-09-18 16:45:35 UTC. Accordingly, no separate discovery
priority is claimed here. The value of this record is its focused derivation and
reproducibility package for that specialization.

## Theorem

Let \(q\ge 8\), and let \(G\) be a 2-connected co-bipartite graph with a fixed clique
partition
\[
V(G)=Q\mathbin{\dot\cup}\{x,y\},\qquad Q\cong K_q,\qquad xy\in E(G).
\]
Partition \(Q\) into
\[
\begin{aligned}
A&=N_Q(x)\setminus N_Q(y),\\
B&=N_Q(y)\setminus N_Q(x),\\
C&=N_Q(x)\cap N_Q(y),\\
D&=Q\setminus(N_Q(x)\cup N_Q(y)),
\end{aligned}
\]
and put \(a=|A|, b=|B|, c=|C|, d=|D|\). Then
\[
\boxed{\eta(G)=8ab+2c(a+b)+3d(a+b)+4cd-4d,}
\tag{1}
\]
where \(\eta(G)=Sz(G)-W(G)\).

Since \(n=q+2\), equality \(\eta(G)=2n\) holds if and only if one of the following
occurs:

1. \(a=b=1,\ c=0,\ d=q-2\);
2. \(q=8\) and, up to interchanging \(x\) and \(y\),
   \[
   (a,b,c,d)=(1,0,1,6).
   \]

Thus for \(n\ge 11\) the Zhang–Li equality construction is unique in this subclass,
while at \(n=10\) there is one additional isomorphism type.

## Proof of the formula

The 2-connectivity conditions are
\[
a+c\ge1,\qquad b+c\ge1,\qquad a+b+c\ge2.
\tag{2}
\]
Under (2), \(G\) has diameter at most two. Its nonedges are exactly the pairs from
\(x\) to \(B\cup D\) and from \(y\) to \(A\cup D\), hence
\[
W(G)=\binom{q+2}{2}+a+b+2d.
\tag{3}
\]

For an edge \(uv\) in a diameter-two graph,
\[
n_{uv}(u)=\deg(u)-|N(u)\cap N(v)|.
\tag{4}
\]
Applying (4) to the four \(Q\)-types gives the following excesses over the baseline
contribution \(1\) for edges inside \(Q\):
\[
AB:3,\quad AC:1,\quad AD:1,\quad BC:1,\quad BD:1,\quad CD:2.
\]
The edge \(xy\) contributes \((a+1)(b+1)\). Each \(xA\) edge contributes
\(2(b+d+1)\), each \(xC\) edge contributes \(b+d+1\), each \(yB\) edge contributes
\(2(a+d+1)\), and each \(yC\) edge contributes \(a+d+1\). Summing these
contributions and subtracting (3) simplifies to (1).

## Equality classification

Let \(s=a+b\). Since \(q=a+b+c+d\), the equation \(\eta(G)=2(q+2)\) is
\[
8ab+2c(s-1)+d(3s+4c-6)-2s-4=0.
\tag{5}
\]

If \(c=0\), (2) forces \(a,b\ge1\). For \(s=2\) this means \(a=b=1\), and
(5) is identically zero for every \(d\). If \(s\ge3\), then \(ab\ge s-1\) and the
left side is strictly positive.

Now suppose \(c\ge1\). If \(a,b\ge1\), then \(s\ge2\) and \(ab\ge s-1\); rearranging
(5) shows that the nonnegative \(d\)-term would have to equal a negative number.
Thus \(ab=0\). By symmetry take \(b=0\), so \(s=a\). A direct check of (5) now gives:
for \(c=1\), \(d(3s-2)=6\), whose only \(q\ge8\) solution is
\((s,c,d)=(1,1,6)\); for \(c\ge2\), all integer solutions have \(q<8\).
This proves the classification.

## Relation to the earlier broader SCOPE record

The earlier record
`szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8` uses the convention
that its \(C\) consists of vertices adjacent to neither \(x\) nor \(y\), while its
\(D\) consists of vertices adjacent to both. In the adjacent-\(x,y\) case its formula is
\[
8ab+3C(a+b)+2D(a+b)+4CD-4C.
\]
Substituting \(C=d\) and \(D=c\) gives (1) exactly. Its \(n=10\) exceptional tuple
likewise becomes \((a,b,c,d)=(1,0,1,6)\) up to swapping \(x,y\).
Therefore this record is a specialization/corroboration of that earlier theorem,
not an independent originality claim.

## Computational verification

`artifacts/verify_small_side.py` uses only the Python standard library. It constructs
every parameter quadruple satisfying (2) for \(2\le q\le20\), computes all-pairs
distances, \(W\), and \(Sz\) from their definitions, and checks (1). It verifies
10,165 two-connected parameter quadruples and the stated equality classification
for \(8\le q\le20\). The computation is supplementary evidence; the proof above is
general.

## Literature context and limitations

Zhang and Li (arXiv:2609.20025) prove the \(2n\) lower bound for the relevant
unexceptional 2-connected graphs, construct equality examples, and pose the global
equality-classification problem. Bonamy–Knor–Lužar–Pinlou–Škrekovski (2017)
provide the earlier \(2n-6\) theory.

This record does not solve the global Zhang–Li equality problem. It treats only the
co-bipartite subclass with a two-vertex clique side, and after the provenance correction
it makes no separate discovery claim relative to the earlier broader SCOPE record.

## References

1. L. Zhang and E. Li, *Improved Bounds on the Szeged-Wiener Gap and the BKLPS
   Conjecture*, arXiv:2609.20025 (2026).
2. M. Bonamy, M. Knor, B. Lužar, A. Pinlou, and R. Škrekovski,
   *On the difference between the Szeged and the Wiener index*,
   Applied Mathematics and Computation 312 (2017), 202–213.
3. SCOPE record `2026/09/18/szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8`,
   committed 2026-09-18 03:47:31 UTC.
