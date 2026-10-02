# Exact finite-abelian defect classes for object cotorsion completeness

## Statement

Let \(\mathcal S\) be an essentially small Hom-finite semisimple \(k\)-linear abelian
category with finitely many simple isomorphism classes. Put
\[
K=K_0(\mathcal S),
\]
let \(H\le K\) have finite index, write \(G=K/H\), and let \(\mathcal A_H\) be the
bounded complexes whose Euler class lies in \(H\). Define
\[
\mathcal F_H=\{X:H^n(X)=0\text{ for }n\ge1\},\qquad
\mathcal C_H=\{X:H^n(X)=0\text{ for }n\le1\}.
\]

The finite-Grothendieck-quotient construction and the associated complete ideal
cotorsion pair are prior results. The contribution here is the exact object-level
defect classification.

For \(A\in\mathcal A_H\), set
\[
\delta_-(A)=[\chi_K(H^{\le0}(A))]\in G,\qquad
\delta_+(A)=[\chi_K(H^{\ge2}(A))]\in G.
\]
Then a special \(\mathcal F_H\)-precover of \(A\) exists if and only if
\(\delta_-(A)=0\), and a special \(\mathcal C_H\)-preenvelope exists if and only if
\(\delta_+(A)=0\).

Moreover,
\[
\{(\delta_-(A),\delta_+(A)):A\in\mathcal A_H\}=G\times G.
\]
Consequently the object cotorsion pair is complete exactly when \(G=0\).
Every finite abelian group occurs as such a defect group.

## Proof

Semisimplicity splits every bounded complex as its cohomology, with zero differential,
plus a contractible summand. Suppose
\[
0\to C\to F\to A\to0
\]
is a special object precover with \(F\in\mathcal F_H\) and \(C\in\mathcal C_H\).
The long cohomology sequence forces
\[
H^*(F)\cong H^{\le0}(A).
\]
Since \(F\in\mathcal A_H\), this gives \(\delta_-(A)=0\).

Conversely, decompose
\[
A\cong L\oplus U\oplus Q,\qquad
L=H^{\le0}(A),\quad U=H^{\ge1}(A),
\]
with \(Q\) contractible. If \(\delta_-(A)=0\), then both \(L\) and \(U\) have Euler
class in \(H\). The standard contractible-cone deflation onto \(U\), together with
the identity on \(L\oplus Q\), gives a special \(\mathcal F_H\)-precover inside
\(\mathcal A_H\). The preenvelope criterion is dual.

For the spectrum, let \(g,h\in G\). Because \(K\) is free on the simple classes and
\(G\) is finite, choose objects \(L,M,W\in\mathcal S\) representing respectively
\(g\), \(g+h\), and \(h\) in \(G\). Set
\[
A=S^0(L)\oplus S^1(M)\oplus S^2(W).
\]
Then the total Euler class is zero in \(G\), so \(A\in\mathcal A_H\), while
\[
(\delta_-(A),\delta_+(A))=(g,h).
\]
Thus every pair occurs.

Finally, every finite abelian group \(G\) is a quotient of some \(\mathbb Z^r\).
Taking a semisimple category with \(r\) simple objects and \(H\) equal to the kernel
of a chosen surjection realizes \(G\).

## Prior boundary

A published 17 September 2026 result already proves the general finite-quotient
Frobenius construction, completeness of the ideal cotorsion pair, failure of object
completeness for every nontrivial finite quotient, and the idempotent-completion
statement. Ren--Wang give the parity specialization. Those results are prior input
here and are not claimed as contributions.

The surviving result is the exact pair of obstruction maps, the full \(G\times G\)
defect spectrum, and arbitrary finite-abelian realization.

## Limitations

The argument uses semisimplicity, finitely many simple isomorphism classes, and a
finite-index subgroup. It makes no claim for arbitrary exact categories or
infinite-index quotients. The foundational ideal-approximation literature remains a
residual source-overlap risk because its complete 2013 article was not available for
full-text inspection during this assessment.

## References

1. Published result, *Finite Grothendieck quotients produce cotorsion completeness
   obstructions*, 17 September 2026.
2. J. Ren and Y. Wang, *A parity obstruction to completeness of object cotorsion
   pairs*, arXiv:2609.18681.
3. X. H. Fu, P. A. Guil Asensio, I. Herzog, and B. Torrecillas,
   *Ideal approximation theory*, Advances in Mathematics 244 (2013), 750--790.
