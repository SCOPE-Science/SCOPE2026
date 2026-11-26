# Exact parity-residue law for unavoidable Alabama losses in paired populations

## Finding

Let the four populations be \((a,a,b,b)\), where \(0<a<b\) are coprime integers. For each positive integer house size use Hamilton's largest-remainder method, with independent choices among valid tie resolutions at successive sizes. A loss at \(h\to h+1\) is **unavoidable** if every pair of valid allocations has some constituency whose allocation decreases.

Let \(P=2(a+b)\) and \(r_h=ah\bmod P\), with \(0\le r_h<P\). A loss is unavoidable exactly when
\[
\begin{array}{ll}
h\text{ even}:& 2(a+b)<2r_h<a+3b,\\
h\text{ odd}:& a+b<2r_h<2b.
\end{array}
\]
In every such event one of the smaller constituencies loses a seat. Equality at an endpoint does not force a loss.

For **all** integers \(l,u\), define
\[
E(l,u)=\max\{0,\lfloor u/2\rfloor-\lfloor(l-1)/2\rfloor\},\qquad
O(l,u)=\max\{0,\lfloor(u+1)/2\rfloor-\lfloor l/2\rfloor\}.
\]
These count the even and odd integers, respectively, in the interval \([l,u]\), with zero for an empty interval. Set
\[
l_e=a+b+1,\quad u_e=\lfloor(a+3b-1)/2\rfloor,\qquad
l_o=\lfloor(a+b)/2\rfloor+1,\quad u_o=b-1.
\]
Then the number of unavoidable transitions in one size period of length \(P\) is
\[
N(a,b)=E(l_e,u_e)+\begin{cases}O(l_o,u_o),&a\text{ odd},\\ E(l_o,u_o),&a\text{ even}.\end{cases}
\]
The minimum total population admitting an unavoidable loss is \(10\), attained uniquely by \((1,1,4,4)\) up to swapping the pairs. This profile attains the earliest possible transition, \(3\to4\). For fixed positive \(a\), as \(b\to\infty\) through integers coprime to \(a\), \(N(a,b)/P\to1/4\).

## Assumptions and scope

Hamilton's rule assigns the integer part of each quota \(hp_i/P\), then fills the remaining seats in decreasing order of fractional remainders, allowing arbitrary resolution of equal remainders. There is no minimum allotment per constituency. Multiplying all populations by a common positive integer does not change the allocations. The result does not assume a fixed tie-breaking rule or classify losses under any one such rule.

## Proof

Write \(\alpha=a/P\), so \(0<\alpha<1/4\) and the large quota per unit house size is \(1/2-\alpha\). At house size \(h\), write \(h\alpha=q+x\) with \(q\) integral and \(0\le x<1\). The small-quota remainder is \(x\); the large-quota remainder is \(\{h/2-h\alpha\}\). Let \(S_h\) range over the possible combined allocations to the two smaller constituencies.

At even \(h\), \(S_h-2q\) is \(0\) for \(x<1/2\), is \(2\) for \(x>1/2\), and can be \(0,1,2\) at \(x=1/2\). Indeed for \(x>0\) there are two residual seats and the large remainder is \(1-x\). At \(x=0\) there are no residual seats. At odd \(h\), \(S_h-2q\) is \(0\) for \(0\le x<1/4\), \(1\) for \(1/4<x<3/4\), and \(2\) for \(3/4<x<1\). At \(x=1/4\) it can be \(0,1\), and at \(x=3/4\) it can be \(1,2\). To see this, the large remainder is \(1/2-x\) for \(x\le1/2\), with one residual seat, and \(3/2-x\) for \(x>1/2\), with three residual seats. This also gives the values at \(x=0,1/2\).

There is a pair of allocations with no individual loss exactly when one can choose the pair totals so that \(S_{h+1}-S_h\) is \(0\) or \(1\): since the total increases by one, these are exactly the choices where neither pair total falls. To lift such choices to individual allocations, do this within each equal pair. If the integer quota per member grows, every new allocation is at least every old allocation to that member, since a residual seat contributes at most one. If it does not grow, a nondecreasing pair total permits the new set of recipients to contain the old set. Every permutation within an equal pair is allowed without affecting the numbers of residual seats of the two pairs. Conversely, a falling pair total necessarily entails an individual loss.

**Even to odd.** If \(x<1/2\), then \(x+\alpha<3/4\) and the possible increase can be chosen as \(0\) or \(1\). At \(x=1/2\), choose \(S_h=2q+1=S_{h+1}\). If \(x>1/2\), then \(S_h=2q+2\). For \(x+\alpha<3/4\) the next value is \(2q+1\), so the loss is forced. At \(x+\alpha=3/4\), one can instead choose \(2q+2\). If \(3/4<x+\alpha<1\) the next total is \(2q+2\); for \(x+\alpha\ge1\) the integer part increases and the new remainder is less than \(1/4\), giving the same total \(2q+2\). This leaves exactly \(1/2<x<3/4-\alpha\).

**Odd to even.** For \(x<1/2-\alpha\), the next total is \(2q\). This forces a loss precisely if \(x>1/4\); at \(x=1/4\) the old total can be chosen to be \(2q\). At \(x=1/2-\alpha\), the old total is \(2q+1\), which is an option at the next size as well. For \(1/2-\alpha<x<1-\alpha\), the next total is \(2q+2\) and the old one can be chosen as \(2q+1\) or \(2q+2\). For \(x\ge1-\alpha\), the old total is \(2q+2\) and the quota wrap leaves the new pair at \(2q+2\). The only forced region is thus \(1/4<x<1/2-\alpha\).

Substituting \(x=r_h/P\) into these two open intervals gives the residue criterion. For counting, use the joint period \(P\) of parity and residue. If \(a\) is odd, multiplication by \(a\) permutes the residues modulo \(P\) and preserves parity. If \(a\) is even, \(\gcd(a,P)=2\) and \(a+b\) is odd. Each even residue occurs twice per period at sizes differing by \(a+b\), once at each parity. Counting in the two integer intervals gives the formula for \(N\).

At \(h=1,2\) the smaller remainder is respectively \(\alpha<1/4\) and \(2\alpha<1/2\), so neither transition is forced. The only primitive pairs with \(a+b<5\) are \((1,2)\) and \((1,3)\); both counts are zero. At \(a+b=5\), the count is two for \((1,4)\) and zero for \((2,3)\). At house size three the \((1,1,4,4)\) allocations are \((1,0,1,1)\) and \((0,1,1,1)\); at size four there is only \((0,0,2,2)\). Finally the two open residue intervals each have length \((b-a)/2\); the number of integers of each specified parity per interval differs from half its length by at most a constant. Thus \(N(a,b)=(b-a)/2+O(1)\) with absolute error bound, yielding the limit. \(\square\)

## Verification

The accompanying standard-library Python diagnostic `verify.py` can be run with `python3 verify.py`. It enumerates all legal Hamilton allocations and compares the forced-loss condition with the strict residue inequalities for coprime \(1\le a<b\le40\) over one period. It also compares the closed count with period summation for coprime \(1\le a<b\le79\) and checks the minimum example. These finite diagnostics are supplementary; the proof establishes the full range.

## Relationship to prior work and limitations

Hamilton's house-size paradox is classical. Janson and Linusson discuss periodicity for rational populations, while their main probability theorem assumes rational linear independence, excluding the present family. Saari gives a general geometric explanation of the paradox, and Varshney considers a different incompatibility for four-state apportionment across house sizes. The related exact three-state equal-pair residue classification (Resultary record 494a0538d100) has a different population family and tie criterion. The result here classifies the rational two-pair family with an all-resolutions quantifier. It does not cover arbitrary population profiles, changes of population, or enumeration of tie-dependent losses. These distinctions do not establish historical priority.

## References

- S. Janson and S. Linusson, *The probability of the Alabama paradox*, Journal of Applied Probability 49 (2012), 773–794, doi:10.1239/jap/1346955333.
- D. G. Saari, *Picture book of apportionment and voting difficulties*, Public Choice (2026), doi:10.1007/s11127-026-01480-9.
- L. R. Varshney, *Quota and population monotonicity across house sizes are incompatible for apportionment to four states*, arXiv:2608.02759.
- M. L. Balinski and H. P. Young, *The quota method of apportionment*, American Mathematical Monthly 82 (1975), 701–730.
