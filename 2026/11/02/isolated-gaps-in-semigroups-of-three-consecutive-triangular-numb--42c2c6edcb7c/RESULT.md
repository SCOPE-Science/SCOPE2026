# Isolated gaps in semigroups of three consecutive triangular numbers

## Finding
Let \(T_n=n(n+1)/2\), and for each integer \(n\ge3\) let \(S_n=\langle T_n,T_{n+1},T_{n+2}\rangle\). An *isolated gap* is a positive integer \(g\notin S_n\) with \(g-1,g+1\in S_n\). Its number \(I_n\) is
\[
I_3=5,\qquad I_4=4,\qquad I_6=11,\qquad
I_n=\begin{cases}3n-1&n\ge5\text{ odd},\\3n-2&n\ge8\text{ even}.\end{cases}
\]
More strongly, for all \(n\ge7\), set \(a=T_n,b=T_{n+1},c=T_{n+2}\). When \(n=2m-1\), set \((A,B,d)=(2m-1,2m+1,m)\); when \(n=2m\), set \((A,B,d)=(m,m+1,2m+1)\). Then the entire isolated-gap set is the disjoint union
\[
\{yb+zc-a:y\in\{A-2,A-1\},1\le z\le d-2\}
\quad\cup\quad
\{yb+(d-1)c-ta:y\in\{A-2,A-1\},1\le t\le B-1\}.
\]

## Assumptions and scope
All semigroups are additive submonoids of nonnegative integers. The index is integral and \(n\ge3\); the displayed explicit gap-set classification has the stricter assumption \(n\ge7\). The small values \(n=3,4,5,6\) are included in the total-count statement. The case \(n=5\) also satisfies the same rectangular classification, but is not needed for the universal set statement.

## Proof
**1. A rectangular Apéry set.** Write \((a,b,c)=(Ad,Bd,Be)\), where
\[
(A,B,d,e)=\begin{cases}(2m-1,2m+1,m,m+1)&n=2m-1,\\(m,m+1,2m+1,2m+3)&n=2m.\end{cases}
\]
Here \(\gcd(A,B)=\gcd(d,e)=1\), \(c\equiv1\pmod d\), and the identities \(Ab=Ba\), \(dc=eb\) hold. Every element of \(S_n\) can be reduced by these two nonnegative relations to \(xa+yb+zc\), with \(x\ge0\), \(0\le y<A\), \(0\le z<d\). The residues of \(yb+zc\) modulo \(a=Ad\) are pairwise distinct: reduction modulo \(d\) fixes \(z\), and then coprimality of \(A,B\) fixes \(y\). Consequently the entire Apéry set relative to \(a\) is
\[
\operatorname{Ap}(S_n,a)=\{w(y,z)=yb+zc:0\le y<A,0\le z<d\}.
\]
Every missing integer of residue \(w(y,z)\pmod a\) has the form \(w(y,z)-ta\) for an integer \(t\ge1\). It is isolated exactly when
\[
1\le t\le \min\left(\frac{w(y,z)-w_{-}-1}{a},\frac{w(y,z)-w_{+}+1}{a}\right),
\]
where \(w_{-}\) and \(w_{+}\) are the unique Apéry representatives in the adjacent residue classes. Both fractions below are integers by the corresponding residue congruences.

**2. Interior neighbors.** The triangular-number identity \(a+c=2b+1\) gives \(2b-c=a-1\). For \(1\le z\le d-2\), the left and right neighbor representatives have coordinates \(((y+2)\bmod A,z-1)\) and \(((y-2)\bmod A,z+1)\), respectively. Put \(\epsilon_+=1\) when \(y\ge A-2\), otherwise zero, and \(\epsilon_-=1\) when \(y<2\), otherwise zero. Direct subtraction gives
\[
\frac{w-w_{-}-1}{a}=B\epsilon_+-1,\qquad
\frac{w-w_{+}+1}{a}=1-B\epsilon_-.
\]
For \(A\ge4\) both bounds are positive precisely when \(y=A-2\) or \(A-1\), where the upper bound on \(t\) equals \(1\). Thus exactly one isolated gap occurs for each such interior cell. At \(A=3\) only \(y=2\) contributes; at \(A=2\) no interior cell contributes.

**3. Boundary neighbors.** Put \(s=e-2\), so \(s=m-1\) for odd \(n\) and \(s=2m+1\) for even \(n\). At \(z=0\), the left neighbor has coordinates \(((y-s)\bmod A,d-1)\). Writing \(q=(s-y+(y-s\bmod A))/A\ge0\), the left bound is \(-1-qB\), so these cells never yield isolated gaps. At \(z=d-1\), the right neighbor has coordinates \(((y+s)\bmod A,0)\). With \(q=\lfloor(y+s)/A\rfloor\), the right bound becomes \(qB+1\), whereas the left bound is \(B\epsilon_+-1\). Thus only \(y=A-2,A-1\) can contribute. For odd \(n\ge5\) and all even \(n\ge4\), both of these \(y\)-values have \(q\ge1\), and exactly \(B-1\) isolated gaps occur in each final-row cell. The lone exception \(n=3\) gives bounds \(1\) and \(4\) on these two cells.

**4. Count and initial values.** For odd \(n=2m-1\ge5\), \(A\ge5\), and the count is \(2[(d-2)+(B-1)]=2[(m-2)+2m]=3n-1\). For even \(n=2m\ge8\), \(A\ge4\), and the count is \(2[(d-2)+(B-1)]=2[(2m-1)+m]=3n-2\). The rectangular inequalities at \(n=3,4,6\) give, respectively, \(5,4,11\): at \(n=3\), there are no interior-row gaps and the two final cells contribute \(1+4\); at \(n=4\), no interior gaps and the two final cells contribute \(2+2\); at \(n=6\), five interior gaps and the two final cells contribute \(3+3\). For \(n\ge7\), the foregoing bounds also identify every gap listed in the Finding, proving the explicit classification.

## Verification
The accompanying standalone `verify.py` uses Dijkstra's shortest-path algorithm on residue classes to calculate Apéry sets independently of the rectangular formula. It checks all indices \(3\le n\le150\), each stated total and exact gap-set classification, covering 573796 Apéry residues; for \(3\le n\le16\), an independent membership dynamic program checks the entire interval through the Frobenius number. Run `python3 verify.py`; expected terminal marker: `VERIFY_OK`.

## Relationship to prior work
Robles-Pérez and Rosales (2017, arXiv:1706.04378) study precisely these three consecutive triangular generators, proving freeness and Frobenius-number formulas but not the isolated-gap counts or explicit lists above. Moreno-Frías and Rosales (2023, arXiv:2305.14967) study perfect numerical semigroups and isolated gaps for fixed Frobenius number, without this triangular family classification. Smith (2022) studies general Apéry criteria and explicit isolated gaps in embedding dimension two; Singh and Ram (2024, arXiv:2406.09848) also address the two-generator case. The present statement is an explicit embedding-dimension-three, infinite-parametric gap classification, rather than another Frobenius formula.

## Limitations
The theorem concerns precisely three consecutive triangular-number generators. It does not classify arbitrary telescopic triples, four-generator triangular systems, or other distances between missing elements. Although relevant full texts available openly were inspected, an unrestricted priority claim is not made; Smith's publisher-hosted full PDF could not be accessed during the literature check, leaving a residual bibliographic risk.

## References
Robles-Pérez, A. M., and Rosales, J. C., *The Frobenius number for sequences of triangular and tetrahedral numbers* (2017), https://arxiv.org/abs/1706.04378.

Moreno-Frías, M. A., and Rosales, J. C., *The covariety of perfect numerical semigroups with fixed Frobenius number* (2023), https://arxiv.org/abs/2305.14967.

Smith, H. J., *On isolated gaps in numerical semigroups* (2022), https://doi.org/10.3906/mat-2107-54.

Singh, S. N., and Ram, R. K., *On isolated gaps of numerical semigroups of embedding dimension two* (2024), https://arxiv.org/abs/2406.09848.
