# A sharp first \(p\)-Frobenius phase for three consecutive Pell-type numbers

## Finding

For integers \(u\ge2\) and \(i\ge2\), let the Pell-type sequence be
\[P_0=0,\quad P_1=1,\quad P_{j+2}=uP_{j+1}+P_j.\]
Put \(A=P_i\), \(B=P_{i+1}\), \(C=P_{i+2}\), and \(K=\lfloor A/u\rfloor\). Write \(R(N)\) for the number of ordered coefficient triples \((x,y,z)\in\mathbb Z_{\ge0}^3\) with \(Ax+By+Cz=N\); distinct triples are counted as distinct representations. Define \(g_p\) to be the largest \(N\ge0\) satisfying \(R(N)\le p\).

**Theorem (first phase and its sharp break).** For every integer \(0\le p\le K\),
\[g_p=B(A+up-1)-A.\]
At the next index,
\[g_{K+1}=\begin{cases}B(2A-1),&i\text{ even},\\B(2A-1)-A,&i\text{ odd}.\end{cases}\]
The earlier affine formula fails at this index in both parity classes. Each boundary \(g_p\) has exactly \(p\) representations. Every greater integer has at least \(p+1\) representations.

In fact, for every \(0\le y<A\) and \(0\le p\le K+1\), put \(r=\lfloor y/u\rfloor\). The exact first integer in the residue class \(By\pmod A\) with more than \(p\) representations is
\[T_p(y)=By+Aq_p(y),\qquad q_p(y)=\begin{cases}p,&r\ge p,\\ B+p-r-1,&r<p.\end{cases}\]
The maximizing residue class is unique: for \(p\le K\) it is \(B(up-1)\pmod A\) when \(p>0\), and \(-B\pmod A\) when \(p=0\); for \(p=K+1\) it is \(-B\pmod A\). All these facts concern unrestricted index and parameter ranges indicated above.

## Assumptions and scope

Only \(u\ge2\), \(i\ge2\), and integral \(0\le p\le K+1\) are assumed. The three denominations are positive and pairwise distinct. Adjacent Pell-type terms are coprime because \(\gcd(P_{j+1},P_j)=\gcd(P_j,P_{j-1})=1\). Also \(B>A\), \(C=A+uB\), \(K<B\), and \(P_i\equiv0\pmod u\) for even \(i\) and \(P_i\equiv1\pmod u\) for odd \(i\). These follow directly from the recurrence. In particular \(uB>A\), and \(\gcd(A,B)=1\) makes \(By\) with \(0\le y<A\) a complete residue system modulo \(A\).

## Proof

**Exact representation count.** More generally suppose positive coprime integers \(A<B\) and \(u\ge2\) satisfy \(C=A+uB\). Fix \(0\le y<A\) and write every integer in its residue class uniquely as \(N=By+Aq\), with \(q\in\mathbb Z\). Every triple \((x,v,z)\ge0\) representing \(N\) determines \(x'=x+z\), \(v'=v+uz\), so that \(Ax'+Bv'=N\). Conversely, each two-denomination solution \((x',v')\) lifts to exactly \(\min(x',\lfloor v'/u\rfloor)+1\) triples, indexed by \(0\le z\le\min(x',\lfloor v'/u\rfloor)\).

Since \(0\le y<A\) and \(\gcd(A,B)=1\), all nonnegative two-denomination solutions have \(v'=y+Aj\), \(x'=q-Bj\), for integers \(0\le j\le\lfloor q/B\rfloor\). Thus the exact count is \(0\) if \(q<0\), and otherwise
\[R(By+Aq)=\sum_{j=0}^{\lfloor q/B\rfloor}\left(1+\min\left\{q-Bj,\left\lfloor\frac{y+Aj}{u}\right\rfloor\right\}\right).\tag{1}\]
It follows at once that \(R(By+Aq)\) is nondecreasing in \(q\).

**Exact thresholds.** Take \(K=\lfloor A/u\rfloor\) and \(0\le p\le K+1\). Put \(r=\lfloor y/u\rfloor\). When \(r\ge p\), the first \(p+1\) representations occur at \(q=p<B\): for \(0\le q<B\), only \(j=0\) occurs and \(R=1+\min(q,r)\). The case \(p=0\) is included.

When \(r<p\), there are at most \(r+1\le p\) representations for \(0\le q<B\). For \(q=B+h\) with \(0\le h\le p-r-1\), no \(j\ge2\) appears, since \(p-1\le K<B\). Moreover \(\lfloor(y+A)/u\rfloor\ge K\ge p-r-1\), and \(B+h\ge r\). Therefore formula (1) gives
\[R(By+A(B+h))=(r+1)+(h+1)=r+h+2.\]
Its first value at least \(p+1\) occurs precisely for \(h=p-r-1\), proving the stated \(T_p(y)\). In either case \(T_p(y)-A\) has at most \(p\) representations (exactly \(p\) at each maximizing residue), and every higher integer in the same residue class has at least \(p+1\).

**Maximal residue.** If \(1\le p\le K\), for \(r<p\) the maximal \(T_p(y)\) in the band \(ur\le y\le\min(u(r+1)-1,A-1)\) occurs at its largest \(y\). The band maximum increases by \(uB-A>0\) with \(r\), and the last such band is \(r=p-1\), \(y=up-1\), yielding
\[\max_{r<p}T_p(y)=B(A+up-1).\]
For \(r\ge p\), the largest threshold is at most \(B(A-1)+Ap\), smaller by \(p(uB-A)>0\). For \(p=0\), the largest threshold is simply \(B(A-1)\), at \(y=A-1\). Hence subtracting \(A\) proves the first formula and uniqueness.

For \(p=K+1\), every possible band has \(r<p\). Its maximal threshold increases strictly between full adjacent bands by \(uB-A>0\), and within each band by \(B\). If \(A=uK+1\), the final band contains only \(y=uK\); the increment from the previous band maximum is then \(B-A>0\). Therefore the unique maximizer is \(y=A-1\). If \(A=uK\), then \(r=K-1\), \(q_p(y)=B+1\), and \(T_p(A-1)=B(2A-1)+A\). If \(A=uK+1\), then \(r=K\), \(q_p(y)=B\), and \(T_p(A-1)=B(2A-1)\). The recurrence gives precisely the even/odd index alternatives, and subtraction of \(A\) proves the second formula.

Finally, extrapolating the earlier affine formula to \(p=K+1\) exceeds the true value by \(uB-A>0\) when \(i\) is even, and by \((u-1)B>0\) when \(i\) is odd. Thus this is the sharp first break. \(\square\)

## Verification

The separately implemented finite checker `verify.py` uses coin-change dynamic programming, direct enumeration of coefficient triples, and separate threshold formulas. It checks the first-crossing inequalities for every residue and every claimed \(p\) in 20 parameter cases, 12,341 residue thresholds, 194 global extrema, and 660 direct count comparisons. The reproducible log is `verification_output.txt`; run `python3 verify.py` from the directory containing the checker. This finite verification is supplemental; the proof above establishes all quantified cases.

For illustration, \(u=2\), \(i=3\) gives denominations \((5,12,29)\) and \(K=2\), hence \((g_0,g_1,g_2,g_3)=(43,67,91,103)\). For \(u=2\), \(i=4\), the denominations are \((12,29,70)\), \(K=6\), and the sharp-break value is \(g_7=667\).

## Relationship to prior work

The generalized Frobenius problem counts representations of numerical semigroup elements. Komatsu and Pita-Ruiz (2023) study Jacobsthal triplets with index gaps and explicitly raise Pell-type extensions. Komatsu, Laishram, and Punyani (2023) obtain formulas for Jacobsthal-polynomial triples of shape \((a,va+b,vaJ_{k-1}(v)+bJ_k(v))\). Komatsu and Mu (2023 preprint; 2025 journal) determine \(p\)-Frobenius formulas for Pell triples of the different shape \((P_i(u),P_{i+2}(u),P_{i+k}(u))\). Their results do not directly give thresholds for the *three consecutive* terms \((P_i(u),P_{i+1}(u),P_{i+2}(u))\), which depend on a different two-denomination lifting identity. Woods (2023) proves general eventual quasi-polynomial behavior for sufficiently large \(p\); it does not give these small-\(p\) exact phase boundaries. The usual two-coin Frobenius formula is recovered at \(p=0\), because the third generator is redundant for ordinary membership, but not for representation multiplicity.

## Limitations

The result determines the exact \(p\)-Apéry threshold in every residue only for \(0\le p\le K+1\); it makes no formula claim for larger \(p\). It does not determine the corresponding \(p\)-genus or all representation counts in closed form beyond the explicit summation (1). A mathematically equivalent statement in unindexed or uninspected literature remains possible.

## References

1. T. Komatsu and C. Pita-Ruiz, “The Frobenius Number for Jacobsthal Triples Associated with Number of Solutions,” *Axioms* **12** (2023), 98, DOI 10.3390/axioms12020098 (public 2023-01-17).
2. T. Komatsu, S. Laishram, and P. Punyani, “p-numerical semigroup of generalized Fibonacci triples,” arXiv:2304.00443 (initial posting 2023-04-02).
3. T. Komatsu and J. Mu, “p-numerical semigroups of Pell triples,” arXiv:2307.08998 (initial posting 2023-07-18); *Journal of the Ramanujan Mathematical Society* **40** (2025), 5–22.
4. K. Woods, “The Generalized Frobenius Problem via Restricted Partition Functions,” *Electronic Journal of Combinatorics* **30** (2023), P3.27, DOI 10.37236/11161.
