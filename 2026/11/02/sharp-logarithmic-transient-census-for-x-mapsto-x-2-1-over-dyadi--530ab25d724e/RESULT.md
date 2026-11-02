# Sharp logarithmic transient census for \(x\mapsto x^2-1\) over dyadic rings

## Finding
For every integer \(n\ge2\), let \(f_n(x)=x^2-1\) on \(R_n=\mathbb Z/2^n\mathbb Z\). Its entire functional graph has the unique cycle \(0\mapsto-1\mapsto0\). If \(d_n(x)\) is the least nonnegative integer \(t\) such that \(f_n^t(x)\) belongs to this two-cycle, then the exact maximal depth is
\[
T_n=\begin{cases}2\lfloor\log_2(n+1)\rfloor-2,&n+1\text{ is a power of two},\\2\lfloor\log_2(n+1)\rfloor-1,&\text{otherwise}.\end{cases}
\]
The complete depth histogram has a closed form. Write \(C_n(t)=\#\{x\in R_n:d_n(x)\le t\}\), with \(C_n(0)=2\). For integers \(k\le n\), define
\[
E_n(k)=2^{n-\min\{n,\max\{1,k\}\}},\qquad
O_n(k)=\begin{cases}2^{n-1},&k\le3,\\2^{n-k+2},&4\le k\le n.\end{cases}
\]
For every integer \(r\ge0\),
\[
C_n(2r+1)=E_n\!\left(\left\lceil\frac{n+2}{2^{r+1}}\right\rceil-1\right)+O_n\!\left(\left\lceil\frac{n+1}{2^r}\right\rceil-1\right).
\]
For every integer \(r\ge1\),
\[
C_n(2r)=E_n\!\left(\left\lceil\frac{n+1}{2^r}\right\rceil-1\right)+O_n\!\left(\left\lceil\frac{n+2}{2^r}\right\rceil-1\right).
\]
Thus the number of vertices at depth exactly \(t\ge1\) is \(C_n(t)-C_n(t-1)\), and the two cycle vertices have depth zero. The equations apply at arbitrarily large \(t\), when both sides become \(2^n\).

## Assumptions and scope
All valuations are the usual \(2\)-adic valuation \(\nu_2\), extended by \(\nu_2(0)=\infty\). Residues are represented by their compatible \(2\)-adic lifts whenever a valuation is used. The formulas count **all** residues of \(R_n\), not an experimentally selected region. At \(n=1\), the two residues already form the cycle and the maximum depth is zero; the displayed classification is stated for \(n\ge2\).

## Proof
**1. Unique periodic cycle.** Parity alternates under \(f(x)=x^2-1\). Its two-step iterate is
\[
F(x)=f^2(x)=x^2(x^2-2).
\]
For any even \(x\ne0\), \(\nu_2(F(x))=2\nu_2(x)+1>\nu_2(x)\). For odd \(x\), \(f(x)\) is even, and for every odd \(x\notin\{1,-1\}\) one has \(\nu_2(f(x))=\nu_2(x^2-1)\ge3\). The odd points \(1\) and \(-1\) also reach the displayed cycle after at most two steps. Thus every residue modulo \(2^n\) eventually enters \(\{0,-1\}\). The two points are a genuine cycle, so no other cycles exist.

**2. Exact iterated valuations.** Let \(x\) be even and let \(a=\nu_2(x)\ge1\). For all integers \(r\ge0\), by induction on \(\nu_2(F(y))=2\nu_2(y)+1\),
\[
\nu_2(f^{2r}(x))=2^r(a+1)-1,\quad
\nu_2(f^{2r+1}(x)+1)=2^{r+1}(a+1)-2.
\]
The identities include the case \(x=0\) under the conventional \(\infty\) valuation. If \(x\) is odd, put \(b=\nu_2(x^2-1)\ge3\). Since \(f(x)\) is even, the same induction gives
\[
\nu_2(f^{2r+1}(x))=2^r(b+1)-1\quad(r\ge0),
\]
\[
\nu_2(f^{2r}(x)+1)=2^r(b+1)-2\quad(r\ge1).
\]
In the odd cases \(x=\pm1\), the infinite valuation convention gives the correct exact cycle entry. At even iterations the target periodic vertex is \(0\) for an initially even point and \(-1\) for an initially odd point; at odd iterations the targets are reversed. Since the map preserves congruences, arrival at the corresponding target modulo \(2^n\) is equivalent to entry by that time.

**3. Exact counting of initial valuations.** The number of even residues satisfying \(\nu_2(x)\ge k\) is \(E_n(k)\): for \(k\le1\) every even residue qualifies, and otherwise exactly one multiple of \(2^k\) in each congruence class, with the one zero residue for \(k\ge n\). For an odd residue, \(\nu_2(x^2-1)\ge3\) automatically. For \(4\le k\le n\), the equation \(x^2\equiv1\pmod{2^k}\) has precisely four roots modulo \(2^k\), each lifting to \(2^{n-k}\) residues modulo \(2^n\), giving \(O_n(k)\). Solving the four valuation inequalities from step 2 for \(a\) and \(b\) yields exactly the two displayed formulas for \(C_n\). All thresholds involved are at most \(n\), so the definition of \(O_n\) suffices.

**4. Sharp maximal depth.** Initial even residues of valuation one exist for every \(n\ge2\); their arrival is slowest. An odd point has \(b\ge3\), and its corresponding valuation at each positive time is at least that for an even point with \(a=1\). For these extremal even points, the arrival threshold at even time \(2r\) is \(n\le2^{r+1}-1\), and at odd time \(2r+1\) it is \(n\le2^{r+2}-2\). The first such time is \(2h-2\) when \(n+1=2^h\), and \(2h-1\) otherwise, where \(h=\lfloor\log_2(n+1)\rfloor\). This proves the stated maximum, which is actually attained.

## Verification
The standalone standard-library script `verify_minus_one.py` exhaustively constructs the directed graph for every \(2\le n\le16\), detects every directed cycle, computes the complete histogram directly, compares every cumulative count to the symbolic formulas, and checks the sharp maximum. It reports `VERIFY_OK n_levels=15 total_graph_vertices=131068 sharp_tail_formulas=15`. Finite calculation corroborates the independently proved formulas rather than proving all \(n\).

## Relationship to prior work
Fan and Liao, *On minimal decomposition of p-adic polynomial dynamical systems* (arXiv:1010.5583, publicly available October 27, 2010), Theorem 6.1(2), already proves that every quadratic map \(x^2-\lambda\) with \(\lambda\equiv1\pmod4\) has a globally attracting \(2\)-cycle on \(\mathbb Z_2\). Accordingly **global attraction is not claimed as new** here. The contribution is the full exact depth distribution at every finite dyadic level and the sharp, discontinuously jumping logarithmic maximum for the superattracting special parameter \(\lambda=1\); the cited theorem neither states those counts nor their exact maximum. Results on the Chebyshev map \(x^2-2\) and on \(x^2+1\) concern different maps whose finite-level depth laws are not the present formula.

## Limitations
This is an exact finite-ring census, not a global classification of all quadratic parameters, all primes, or derivative-sensitive lifting of arbitrary cycles. No claim is made that the qualitative attracting cycle is new. The possibility that a separately published functional-graph enumeration already implies these quantitative formulas remains an originality risk. Independent external verification has not been performed.

## References
1. A. H. Fan and L. Liao, *On minimal decomposition of p-adic polynomial dynamical systems*, arXiv:1010.5583v1 (2010), Theorem 6.1 and its proof; later *Advances in Mathematics* 228 (2011), 2116–2144, DOI:10.1016/j.aim.2011.06.032.
2. The four-square-roots theorem modulo powers of two and elementary \(2\)-adic valuation identities (standard elementary number theory).
