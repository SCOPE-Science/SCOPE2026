# A cubic isolated-gap law for three consecutive square coin denominations

## Finding
For each integer \(k\ge0\), set \(n=4k+3\). Let \(S_n\) be the set of all nonnegative integers representable as \(un^2+v(n+1)^2+w(n+2)^2\), with nonnegative integral \(u,v,w\). A positive integer \(g\notin S_n\) is called an **isolated gap** if both \(g-1\) and \(g+1\) belong to \(S_n\). The exact number of such gaps is
\[
\boxed{I(S_n)=n^3+1}\qquad(n\ge3,\ n\equiv3\pmod4).
\]
More finely, a canonical Apéry-coordinate partition has \(2n-2\) contributing points in its top row, each giving \(7(k+1)\) gaps, and \(k(2n-3)\) contributing points in its other rows, each giving \(2n+2\) gaps. No other coordinate contributes an isolated gap.

## Assumptions and scope
All coin coefficients are nonnegative integers. The Apéry set is taken relative to \(a=n^2\). Set \(b=(n+1)^2\), \(c=(n+2)^2\), \(L=4(n-1)\), \(d=2n-1\), and \(\alpha=2n+1\). Here \(a=(k+1)L+1\), \(\alpha d=4a-1\), and \(\gcd(a,b)=1\). The statement includes \(k=0\), where \(c=a+b\) and the third denomination is redundant.

## Proof
**1. A complete Apéry rectangle with a truncated boundary.** Direct expansion gives the three positive reduction identities
\[
(k+1)c=b+(k+1)a,\qquad Lb+c=(L+9)a,\qquad (L+1)b=kc+(15k+16)a.
\]
Use the first whenever the \(c\)-coefficient exceeds \(k\), the second when the \(c\)-coefficient is positive and the \(b\)-coefficient is at least \(L\), and the third when the \(b\)-coefficient exceeds \(L\). Every step decreases the total \(b,c\) component by a positive multiple of \(a\), so the process terminates. The resulting possible minimal nonnegative \(b,c\)-representations comprise
\[
\mathcal A=\{qb:0\le q\le L\}\ \cup\ \{qb+rc:1\le r\le k,\ 0\le q<L\}.
\]
To see these are exactly the Apéry representatives, write \(t=q-Lr\); since \(Lb+c=(L+9)a\), the residue of \(qb+rc\) modulo \(a\) is that of \(tb\). The allowed \(t\)'s run, exactly once, through every integer of \([-kL,L]\), a block of \(a=(k+1)L+1\) consecutive integers. Coprimality \(\gcd(a,b)=1\) gives distinct residues. The reductions show no smaller nonnegative combination with any residue exists, proving the claimed Apéry formula.

**2. Height and neighbors.** Let \(x(t)\in\{0,\ldots,a-1\}\) be the residue of \(\alpha t\) modulo \(a\). For \(t=q-Lr\) in the displayed coordinate region, its Apéry value is \(w(t)=qb+rc\). Since \(w(t)=tb+r(L+9)a\) and \(b=a+\alpha\), its *gap height* is exactly
\[
h(t)=\frac{w(t)-x(t)}a=q+9r+\left\lfloor\frac{\alpha t}{a}\right\rfloor.
\]
At residue \(x\), precisely the integers \(x,x+a,\ldots,x+(h_x-1)a\) fail to be representable, where \(h_x=h(t)\). Since \(\alpha d=4a-1\), the neighbors of a residue \(x(t)\) correspond to \(t+d\) (residue \(x-1\)) and \(t-d\) (residue \(x+1\)), interpreted modulo the length-\(a\) interval \([-kL,L]\). For all valid \(t\),
\[
\left\lfloor\frac{\alpha(t+d)}a\right\rfloor-\left\lfloor\frac{\alpha t}a\right\rfloor=4-\mathbf1_{\{t=0\}},\qquad
\left\lfloor\frac{\alpha t}a\right\rfloor-\left\lfloor\frac{\alpha(t-d)}a\right\rfloor=4-\mathbf1_{\{t=d\}}.
\]
These follow from \(\alpha d=4a-1\) and the fact that the only representatives with \(t\equiv0\) and \(t\equiv d\pmod a\) in our coordinate interval are \(t=0\) and \(t=d\).

**3. Isolated-gap contribution of a residue.** For \(1\le x\le a-2\), the isolated gaps having residue \(x\) number
\[
\max\{0,h_x-\max(h_{x-1},h_{x+1})\}.
\]
For residue \(a-1\), replace \(h_{x+1}\) by \(h_0-1=-1\), accounting for the carry between successive \(a\)-blocks; residue zero contributes no gaps. These formulas follow by writing every gap as \(x+ja\) and checking both neighboring integers individually.

If \(q<d\), the \(x+1\) neighbor is higher: for \(r<k\) it lies at \((q+L-d,r+1)\), with height difference \(h_x-h_{x+1}=-(2n+2)\); when \(r=k\), including \(k=0\), the wrap goes to top coordinate \((q+L+1-d,0)\), giving difference \(-7(k+1)\). Hence no such cell contributes.

If \(q\ge d\) and \(r\ge1\), the \(x-1\) neighbor is at \((q+d-L,r-1)\), and its height is lower by exactly \(L-d+5=2n+2\). The \(x+1\) neighbor has height lower by \(d+4=2n+3\). Thus this cell contributes exactly \(2n+2\) isolated gaps. There are \(k(L-d)=k(2n-3)\) such cells.

If \(q\ge d\) and \(r=0\), the \(x-1\) neighbor wraps to \((q+d-L-1,k)\), so its height is lower by \(7(k+1)\). The \(x+1\) neighbor is lower by \(d+4=2n+3\), except when \(q=d\), where \(x=a-1\), and its effective right-hand height is \(-1\). In that case \(h_x=d+3=2n+2\), so the right-hand difference \(h_x+1\) is still at least \(7(k+1)\). Since \(2n+3>7(k+1)\), every such top-row cell contributes \(7(k+1)\). Their number is \(L-d+1=2n-2\).

**4. Total.** Adding the disjoint contributions yields
\[
I(S_n)=k(2n-3)(2n+2)+(2n-2)7(k+1)=n^3+1,
\]
by substituting \(n=4k+3\). This proves the theorem for every stated integer \(n\), without extrapolating from finite checks.

## Verification
The accompanying dependency-free Python verifier, `verify_isolated.py`, separately obtains Apéry sets using Dijkstra's algorithm on residues and checks them against the proven coordinate formula for every \(n=3,7,\ldots,83\) (21 cases, 51,149 residue representatives in total). It computes isolated-gap numbers from independently obtained heights and checks the cubic formula. For \(n=3,7,11\), it separately enumerates representability and neighboring membership. All tests passed. Reproduce with `python3 verify_isolated.py`. The finite tests are supplementary to the complete symbolic proof above.

## Relationship to prior work
Fel's treatment of three consecutive squares develops their semigroup arithmetic and Frobenius/genus invariants, but the inspected material does not provide the isolated-gap cubic law. Moreno-Frías and Rosales define isolated gaps and study perfect numerical semigroups, without giving the three-square family count. Singh and Ram give isolated-gap formulas for embedding-dimension-two semigroups; the present square family has embedding dimension three for \(n\ge7\), so those formulas do not settle it. This theorem counts a different invariant from conductor/genus, and no equivalent statement was located in the checked sources. The possibility of an earlier unindexed equivalent calculation is not excluded.

## Limitations
Only \(n\equiv3\pmod4\) is asserted. The proof does not give formulas for other residue classes or classify isolated-gap locations as a single explicit interval list. Overlap searches cannot certify absolute novelty. No independent validation has been performed.

## References
1. L. G. Fel, “Numerical semigroups generated by squares, cubes and quartics of three consecutive integers,” arXiv:1608.08693 (2016), https://arxiv.org/abs/1608.08693.
2. M. A. Moreno-Frías and J. C. Rosales, “The covariety of perfect numerical semigroups with fixed Frobenius number,” arXiv:2305.14967 (2023), https://arxiv.org/abs/2305.14967.
3. Shubh N. Singh and Ranjan K. Ram, “On Isolated Gaps of Numerical Semigroups of embedding dimension two,” arXiv:2406.09848 (2024), https://arxiv.org/abs/2406.09848.
