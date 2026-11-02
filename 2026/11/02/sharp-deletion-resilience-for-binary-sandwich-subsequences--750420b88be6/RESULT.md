# Sharp deletion resilience for binary sandwich subsequences

## Finding

Fix two distinct binary letters \(0,1\). For integers \(b\ge 1\) and \(r\ge0\), put \(p_b=0\,1^b\,0\). A word \(w\) is *\(r\)-robust for \(p_b\)* when **every** word obtained by deleting exactly \(r\) positions from \(w\) still contains \(p_b\) as an order-preserving, not necessarily contiguous subsequence. Write \(L_b(r)\) for the minimum length of such a word. Then

\[
\boxed{L_b(r)=b+2+2r+\min\{r,b-1\}.}
\]

An explicit shortest witness is
\[
\boxed{w_{b,r}=0^{\,s+1}\,1^b\,(01)^r\,0,\qquad s=\min\{r,b-1\}.}
\]

Equivalently, for a word \(w\), let \(\delta_b(w)\) be the minimum number of deleted positions needed to leave a subsequence avoiding \(p_b\), including zero deletions if already avoided. For \(n\ge b+2\), the exact extremal deletion resilience is
\[
\max_{w\in\{0,1\}^n}\delta_b(w)=
\begin{cases}
1+\lfloor(n-b-2)/3\rfloor,&b+2\le n<4b-1,\\
1+\lfloor(n-2b-1)/2\rfloor,&n\ge4b-1.
\end{cases}
\]
For \(n<b+2\), this maximum is zero. In particular \(L_2(r)=2r+5\) for \(r\ge1\), and \(L_2(0)=4\).

## Assumptions and scope

All words are finite binary words, and subsequence means scattered subsequence. Deletions remove arbitrary positions, not necessarily a contiguous interval. The parameters \(b\) and \(r\) are arbitrary integers in the stated ranges. The alphabet is ordered only for notational convenience. Complementing the letters gives the corresponding result for \(1\,0^b\,1\).

The minimum deletion number \(\delta_b(w)\) is well-defined because deleting all positions always yields a word avoiding the nonempty pattern. \(r\)-robustness means \(\delta_b(w)\ge r+1\), provided the original word has at least \(r\) positions; all displayed witnesses do.

## Proof

**A gap formula.** Suppose \(w\) has \(Z\ge2\) zeros, enumerated from left to right. Let \(g_i\) count the ones between its \(i\)-th and \((i+1)\)-st zeros, and put \(G_{ij}=\sum_{t=i}^{j-1}g_t\) for \(1\le i<j\le Z\). A subsequence contains \(0\,1^b\,0\) exactly when there are at least \(b\) ones between its first and last zeros. If at least two zeros survive a deletion, write \(i,j\) for the indices in \(w\) of its first and last surviving zeros. All \(i-1+Z-j\) outer zeros must have been deleted, along with at least \((G_{ij}-b+1)_+\) interior ones. Conversely those deletions suffice to avoid the pattern; other zeros in the interval may be retained. If at most one zero survives, at least \(Z-1\) zeros have been deleted. Thus
\[
\delta_b(w)=\min\left\{Z-1,\ \min_{1\le i<j\le Z}\left(i-1+Z-j+\max\{0,G_{ij}-b+1\}\right)\right\}.
\tag{1}
\]
If \(Z<2\), then \(\delta_b(w)=0\).

**Lower bound.** Let \(\delta_b(w)\ge r+1\). Deleting all but one zero, or all but \(b-1\) ones, shows that \(w\) contains at least \(r+2\) zeros and at least \(r+b\) ones. Write its zero count as \(Z=r+2+z\), where \(z\ge0\). If \(z\ge r\), then
\[
|w|\ge Z+(r+b)\ge b+2+3r\ge b+2+2r+\min\{r,b-1\}.
\]
Suppose \(z<r\). Apply (1) to the interval of the first \(r+1\) zeros. The cost of deleting all zeros to its right is \(z+1\), so its interior ones count \(G_1\) must satisfy
\[
 z+1+\max\{0,G_1-b+1\}\ge r+1,
 \quad\text{hence}\quad G_1\ge b+r-z-1.
\]
Apply (1) again to the interval of the last \(z+2\) zeros. There are \(r\) preceding zeros, so the ones count \(G_2\) between these last zeros must satisfy \(r+\max\{0,G_2-b+1\}\ge r+1\), giving \(G_2\ge b\). These two open zero-to-zero intervals have disjoint interiors (they meet only at the \((r+1)\)-st zero). Hence the number of ones in \(w\) is at least
\[
G_1+G_2\ge 2b+r-z-1.
\]
Consequently
\[
|w|\ge (r+2+z)+(2b+r-z-1)
=2r+2b+1\ge b+2+2r+\min\{r,b-1\}.
\]
This establishes the universal lower bound.

**Sharpness.** Put \(s=\min\{r,b-1\}\) and \(w=0^{s+1}1^b(01)^r0\). It has \(Z=r+s+2\) zeros. Its interzero gaps consist, in order, of \(s\) zero gaps, one gap of size \(b\), and \(r\) gaps of size one. The option of retaining at most one zero costs \(Z-1=r+s+1\ge r+1\). For an interval \([i,j]\) of surviving outer zeros there are three cases:

1. If both indices are in the initial \(s+1\) zeros, removing the \(r+1\) final zeros is necessary, so the cost in (1) is at least \(r+1\).
2. If both are in the final \(r+1\) zeros, let \(\ell=j-i\), with \(1\le\ell\le r\). The total deletion cost in (1) is \(r+s+1-\ell+\max\{0,\ell-b+1\}=r+s+1-\min\{\ell,b-1\}\ge r+1\).
3. If the interval crosses the unique gap of size \(b\), write \(j=s+2+k\) where \(0\le k\le r\). Its gap sum is \(b+k\). The deletion cost is \((i-1)+(r-k)+(k+1)=r+i\ge r+1\).

Thus \(\delta_b(w)\ge r+1\) and its length is \(b+2+2r+s\). Combined with the lower bound, the expression for \(L_b(r)\) follows. The gap formula also gives \(\delta_b(w)=r+1\): for \(s\ge1\) use all initial zeros as the surviving interval, while if \(s=0\) and \(r\ge1\), then \(b=1\) and all final zeros yield cost \(r+1\); \(r=0\) is immediate.

**Fixed-length extremum.** Appending letters cannot decrease \(\delta_b\). Thus a word of length \(n\) with \(\delta_b(w)\ge r+1\) exists precisely when \(n\ge L_b(r)\). Inverting the increasing piecewise formula for \(L_b(r)\), with breakpoint \(r=b-1\), gives the displayed two regimes and the threshold \(n=4b-1\).

## Verification

The standalone program `verify_sandwich.py` uses a dynamic program for the longest pattern-avoiding subsequence and independently implements the gap formula. It compares them exhaustively on all binary words of lengths zero through fourteen for each \(1\le b\le5\), checks the full fixed-length extremal profile, tests the constructed witnesses through larger values of \(b,r\), and directly enumerates small deletion masks. Running `python3 verify_sandwich.py` reproduces `verification_output.txt`. These finite checks corroborate, rather than substitute for, the argument for unbounded parameters.

## Relationship to prior work

Xie, Sun and Ge (2026, Theorem III.2) consider the particular forbidden subsequence \(0110\) while separating insertion-covering from deletion-covering. Their proof shows that a suitable deletion can avoid \(0110\) in every binary word of length \(2r+4\) for positive \(r\). The present \(b=2\) formula shows that boundary is sharp by an explicit witness of length \(2r+5\), and the general theorem supplies the exact two-parameter pattern \(0\,1^b\,0\) threshold and all-length resilience profile. General bounds on the number of deletion descendants or on simultaneous occurrence of every length-\(k\) subsequence do not assert this single-pattern worst-deletion threshold.

## Limitations

No classification of all shortest extremal words is claimed. The pattern is a three-run sandwich with identical outer symbols, and the theorem does not determine analogous thresholds for arbitrary binary patterns or more complicated alternating blocks. Formal independent peer review has not been performed.

## References

1. C. Xie, Y. Sun and G. Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379v1 (first publicly posted 2026-06-13), especially Section III, Theorem III.2. https://arxiv.org/html/2606.15379
2. Y. Liron and M. Langberg, *A characterization of the number of subsequences obtained via the deletion channel*, arXiv:1202.1644 (2012). https://arxiv.org/abs/1202.1644
