# Exact eventual-growth threshold for ternary coin denumerants with weights \(2,3,c\)

## Finding

For an integer \(c\ge1\), let
\[
P_c(n)=\#\{(x,y,z)\in\mathbb Z_{\ge0}^3:2x+3y+cz=n\},\qquad n\ge0.
\]
Say that \(n\) is a *non-increase index* when \(P_c(n+1)\le P_c(n)\). The following classification is exact.

**Theorem.** For \(c=1\), the unique non-increase index is \(n=0\). For \(c\ge2\) with \(\gcd(c,6)=1\), there are finitely many non-increase indices; their largest member is
\[
N(c)=\begin{cases}
7c-7,&c\equiv1\pmod6,\\
7c-5,&c\equiv5\pmod6.
\end{cases}
\]
The last non-increase is an equality \(P_c(N(c)+1)=P_c(N(c))\), and \(P_c(n+1)>P_c(n)\) for **every** \(n>N(c)\). In contrast, whenever \(\gcd(c,6)>1\), there is a strict decrease at \(n=6kc\) for **every** integer \(k\ge0\). Consequently, eventual strict monotonicity holds if and only if \(\gcd(c,6)=1\), with the exact last obstruction as above.

## Assumptions and scope

All counts are of ordered coefficient vectors \((x,y,z)\) of nonnegative integers, so the third weight \(c\) is distinguished even if \(c=2\) or \(c=3\). The parameter \(c\) is any positive integer; \(n\) is any nonnegative integer. No pairwise distinctness of weights or asymptotic assumptions are imposed.

## Proof

Let \(Q(m)=\#\{(x,y)\in\mathbb Z_{\ge0}^2:2x+3y=m\}\) for \(m\ge0\), and set \(Q(m)=0\) for negative \(m\). Direct parity enumeration gives, for every \(h\ge0\),
\[
Q(6h)=h+1,\quad Q(6h+1)=h,\quad Q(6h+j)=h+1\ (2\le j\le5).
\]
Consequently, for all \(m\ge-1\), the difference \(e(m)=Q(m+1)-Q(m)\) depends only on \(m\bmod6\), with the residue table
\[
\begin{array}{c|rrrrrr}m\bmod6&0&1&2&3&4&5\\ \hline e(m)&-1&1&0&0&0&1\end{array}.
\]
The entry \(m=-1\) agrees with residue \(5\), since \(Q(0)-Q(-1)=1\). Summing the coefficient corresponding to the third weight gives \(P_c(n)=\sum_{j\ge0}Q(n-jc)\), hence for \(n=qc+r\), \(q\ge0\), \(0\le r<c\),
\[
\tag{1}P_c(n+1)-P_c(n)=\mathbf1_{\{r=c-1\}}+\sum_{i=0}^{q}e(r+ic).
\]
The additional indicator accounts for the term \(m=-1\), which occurs exactly when \(n+1\) is divisible by \(c\). Formula (1) is an exact identity for every parameter and index.

First assume \(\gcd(c,6)=1\). Then \(c\equiv\pm1\pmod6\), and each block of six consecutive terms \(e(r+ic)\) sums to \(1\), because it traverses all six residue classes. Write \(q=6h+s\), \(h\ge0\), \(0\le s\le5\). Equation (1) becomes
\[
\tag{2}P_c(n+1)-P_c(n)=h+\mathbf1_{\{r=c-1\}}+\sum_{i=0}^s e(r+ic).
\]
For a circular interval of \(1\) through \(6\) entries of the displayed residue table, traversed either forward or backward, the sum is at least \(-1\). Moreover, the sum equals \(-1\) **only** when that interval consists of the single entry at residue \(0\). Indeed, that is the only negative entry, and either neighboring entry has value \(+1\); every interval of length at least two containing residue \(0\) also contains one of those neighbors. An interval not containing residue \(0\) is nonnegative.

Thus (2) is positive whenever \(h\ge2\). At \(h=1\), it can vanish only when \(s=0\), \(r\equiv0\pmod6\), and \(r\ne c-1\), and it is then precisely zero. Therefore every non-increase index has \(q\le6\); at \(q=6\) the non-increases occur exactly at \(n=6c+r\) with \(0\le r\le c-2\) and \(6\mid r\). For \(c\equiv1\pmod6\), \(c\ge7\), the largest such residue is \(r=c-7\); for \(c\equiv5\pmod6\), \(c\ge5\), it is \(r=c-5\). The asserted exact last indices and their equality type follow. When \(c=1\), we always have \(r=c-1=0\). Formula (1) reduces to \(1+\sum_{i=0}^{n}e(i)\), which is zero for \(n=0\) and positive for all \(n\ge1\): its six-periodic prefix sums, including the initial \(-1\), show this directly.

Now assume \(\gcd(c,6)>1\), so \(c\ge2\) and \(c\bmod6\in\{0,2,3,4\}\). The six-step residue sum \(B_c=\sum_{i=1}^6e(ic)\) equals \(-6\) when \(6\mid c\), \(-3\) when \(c\equiv3\pmod6\), and \(-2\) when \(c\equiv2,4\pmod6\). In particular \(B_c<0\). At \(n=6kc\), formula (1) (with \(r=0<c-1\)) yields
\[
P_c(6kc+1)-P_c(6kc)=e(0)+kB_c=-1+kB_c<0
\]
for all \(k\ge0\). This proves infinitely many strict descents and completes the classification. \(\square\)

## Verification

The independent dynamic-programming enumerator in `artifacts/verify.py` checks all parameter values \(1\le c\le200\), computes denumerants through \(20c+30\), compares every adjacent difference against the exact six-residue formula (1), verifies the final equality and all later increases in that window for coprime parameters, and checks four explicit strict descents for each noncoprime parameter. It also checks the \(Q\)-difference table at \(-1\le m\le300\). The run returns `VERIFY_OK 408502`. The universal assertions rely on the proof, not these finite tests.

## Relationship to prior work

Yuchen Ding, *Restricted partition functions and additive complements* (2026, first public June 16), investigates positivity and polynomial growth of general restricted representation functions. The present family is a finite-weight unbounded-multiplicity case, but Ding does not establish an exact monotonicity cutoff for this family. The motivation is to distinguish coarse growth of representation counts from the exact index at which all local oscillations disappear.

Kevin Woods, *The generalized Frobenius problem via restricted partition functions* (2020), Proposition 1.19 and Theorem 1.8, supplies general eventual quasi-polynomial and growth machinery for denumerants. In particular, eventual strict increase for pairwise coprime weights is compatible with that theory. **Neither eventual monotonicity by itself nor the standard generating-function identity is claimed as new**. The proposed new result is the explicit, sharp final non-increase index simultaneously for every parameter \(c\), including the noncoprime obstruction family.

Komatsu, Hyun and Song, *\(p\)-numerical semigroup of the sequence of consecutive odd integers* (2026), study denumerants of arithmetic-progression coin systems; this is neighboring rather than identical subject matter. The present theorem concerns exact adjacent-index growth in a fixed minimal two-coin base with a variable third denomination.

## Limitations

The result is restricted to the natural three-weight family \((2,3,c)\), not arbitrary coin triples. It determines the final non-increase, not the entire set of earlier non-increase indices or an optimal general-denumerant algorithm. The proof is elementary and relies on the particularly simple six-residue difference table for \((2,3)\). Although targeted literature searches identified no exact covering cutoff, an equivalent observation in broader denumerant literature remains possible. No independent mathematical review has been performed.

## References

1. Y. Ding, *Restricted partition functions and additive complements*, Bull. Aust. Math. Soc. (2026), DOI `10.1017/S0004972726101920`, arXiv `2606.18027`, first public June 16, 2026.
2. K. Woods, *The generalized Frobenius problem via restricted partition functions*, arXiv `2011.00600` (2020), especially Theorem 1.8 and Proposition 1.19.
3. T. Komatsu, S. Hyun, K. Song, *\(p\)-numerical semigroup of the sequence of consecutive odd integers*, arXiv `2608.14053` (August 14, 2026).
