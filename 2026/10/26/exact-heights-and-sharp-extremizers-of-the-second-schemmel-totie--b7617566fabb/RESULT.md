# Exact heights and sharp extremizers of the second Schemmel totient on the 7-smooth odd integers

## Finding

Let \(L_2\) be the second Schemmel totient and, for \(n>1\), let \(R_2(n)\) be the least positive integer \(t\) with \(L_2^{(t)}(n)\in\{0,1\}\). On the multiplicatively closed set
\[
\mathcal S=\{3^a5^b7^c:a,b,c\in\mathbb Z_{\ge0}\},
\]
the function \(L_2\) maps every element into \(\mathcal S\). For every \((a,b,c)\ne(0,0,0)\), the exact height is
\[
R_2(3^a5^b7^c)=
\begin{cases}
a,&b=c=0,\\
b+c+\max(a,1),&b\ge1,\\
c+\max(a,2),&b=0,\ c\ge1.
\end{cases}
\]
For each integer \(k\ge2\), the unique maximum of \(n\) over the finite level \(\{n\in\mathcal S:n>1,\ R_2(n)=k\}\) is
\[
M_k=15\cdot 7^{k-2}.
\]
Thus the proposed inequality from Defant (2015),
\[
R_2(n)\ge\frac{\log((49/15)n)}{\log 7},
\]
holds throughout \(\mathcal S\setminus\{1,3\}\), with equality **exactly** at the infinite family \(n=15\cdot7^c\), \(c\ge0\). The level sizes are
\[
N_k=\#\{n\in\mathcal S:n>1,\ R_2(n)=k\}=
\begin{cases}
1,&k=1,\\3,&k=2,\\k(k+3)/2,&k\ge3.
\end{cases}
\]
Their formal generating function is
\[
\sum_{k\ge1}N_kz^k=\frac{2z}{(1-z)^2}+\frac{z^2}{(1-z)^3}-z-2z^2.
\]

## Assumptions and scope

All integers \(a,b,c\) are nonnegative; \(R_2\) is evaluated only at \(n>1\). Iteration terminates at \(1\) on \(\mathcal S\). The assertion concerns **only** positive odd integers with no prime factors outside \(\{3,5,7\}\), not the unrestricted inequality conjectured in the cited source. The definition of \(R_2\) agrees with Definition 2.1 in Defant's article (first positive iteration). The value at \(n=1\) is deliberately outside the stated level classification.

The prime alphabet \(\{3,5,7\}\) is natural for this dynamical problem: it is the smallest prime-support set containing \(7\) that is closed under the prime transitions \(7\mapsto5\mapsto3\mapsto1\) induced by \(L_2\). The infinite equality family for the motivating conjecture already lies in this subsemigroup.

## Proof

**Exact exponent transition.** The standard multiplicative prime-power formula for \(p>2\) is \(L_2(p^e)=p^{e-1}(p-2)\), for \(e\ge1\), while \(L_2(1)=1\). Applying it to \(3^a5^b7^c\) gives the deterministic map
\[
T(a,b,c)=\big((a-1)_++\mathbf1_{b>0},\ (b-1)_++\mathbf1_{c>0},\ (c-1)_+\big),
\quad (u)_+=\max(u,0).
\]
Every trajectory ends at \((0,0,0)\), the exponent vector of \(1\), because \(L_2(n)<n\) for all \(n>1\). This proves forward invariance and assures finite heights.

**Case \(b=c=0\).** The vector \((a,0,0)\) takes exactly \(a\) steps to reach \((0,0,0)\), giving the first case.

**Case \(b\ge1\).** During the initial \(c\) steps in which the third coordinate is positive, the second coordinate stays at its original positive value \(b\): in each such step it loses one unit and gains one from the third coordinate. Afterward it loses one unit per step for exactly \(b\) more steps. Thus the second coordinate first vanishes after exactly \(b+c\) iterations, being positive beforehand. The first coordinate stays constant while positive because it loses one and gains one from the positive second coordinate; starting from \(a=0\), it becomes \(1\) after the first iteration and stays at \(1\) for as long as the second coordinate is positive. Hence after \(b+c\) steps it is precisely \(\max(a,1)\), and that many further steps are required. This proves the second case.

**Case \(b=0<c\).** The second coordinate becomes \(1\) in the first step, and stays \(1\) until the third coordinate vanishes after \(c\) steps. It then decreases to \(0\) at time \(c+1\). At that time the first coordinate is \(\max(a-1,1)\) (also valid for \(a=0,1\)); its remaining time is that number. Thus the total time is \(c+1+\max(a-1,1)=c+\max(a,2)\), proving the third case.

**Sharp level maximum.** Fix \(k\ge2\) and write \(n=3^a5^b7^c\) of height \(k\). If \(b\ge1\) and \(a\ge1\), then \(k=a+b+c\), and
\[
\frac{n}{15\cdot7^{k-2}}=\left(\frac37\right)^{a-1}\left(\frac57\right)^{b-1}\le1.
\]
Equality forces \(a=b=1\), so \(c=k-2\). If \(b\ge1,a=0\), then \(k=b+c+1\), and the ratio equals \(\tfrac13(\tfrac57)^{b-1}<1\). If \(b=0,c\ge1,a\le2\), then \(k=c+2\) and the ratio is \(3^a/15\le3/5<1\). If \(b=0,c\ge1,a\ge3\), then \(k=c+a\) and the ratio is \(\tfrac35(\tfrac37)^{a-2}<1\). Finally, if \(b=c=0,a\ge2\), the same last ratio applies with \(k=a\). These disjoint cases cover the level. Thus \(M_k=15\cdot7^{k-2}\), uniquely. Equivalently \(n\le(15/49)7^{R_2(n)}\) for \(n>3\) in \(\mathcal S\), which is exactly Defant's lower bound on \(R_2(n)\), with the stated equality cases.

**Exact level cardinalities.** For \(k\ge3\), the disjoint regions in the exponent lattice contribute: (i) \(1\) for \(b=c=0\); (ii) \(2(k-1)\) for \(b\ge1,a\in\{0,1\}\); (iii) \((k-1)(k-2)/2\) for \(b\ge1,a\ge2\); (iv) \(3\) for \(b=0,c\ge1,a\in\{0,1,2\}\); and (v) \(k-3\) for \(b=0,c\ge1,a\ge3\). Their sum is \(k(k+3)/2\). Directly at the boundaries, \(N_1=1\), \(N_2=3\). The rational generating function follows by the geometric-series identities for sums of \(kz^k\) and \(k^2z^k\).

## Verification

A dependency-free integer-arithmetic verifier is provided as `verify.py`. It independently computes \(L_2(n)\) using trial division and the prime-power formula, iterates to \(1\), compares with all three closed formulas on every exponent triple in a reproducible finite cube, independently counts each entire height level through a chosen cutoff, and checks the unique maximum and equality cases. It is finite corroboration: the unrestricted quantifiers are justified by the proof above, not by extrapolating the computations. Run `python3 verify.py` from the extracted package directory.

## Relationship to prior work

Defant, *On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions* (first public journal publication 2015-01-13), defines \(R_m\), proves structural results for its terminal value \(H_m\), and in Section 4 formulates the proposed global lower bound for \(R_2\). The source does not give the formula for \(R_2\) on the \(\{3,5,7\}\)-supported subsemigroup, its height-level generating function, or the restricted uniqueness of every sharp extremizer. This theorem proves an exact, natural invariant-subsemigroup case, not the full conjecture.

Defant, *A Note about Iterated Arithmetic Functions* (arXiv:1501.06075v1, 2015), gives a general theorem for complete multiplicativity of **terminal-value** functions \(H\), rather than level-by-level iteration times. Harrington and Jones, *On the Iteration of a Function Related to Euler's \(\phi\)-Function* (2010), study the related shifted iterate count on a domain that excludes prime factors congruent to \(1\pmod3\) along the trajectory, by Defant's Section 4 description; that domain does not contain inputs with prime factor \(7\). The Harrington–Jones full text could not be directly inspected here, so any broader results therein remain an explicit comparison risk.

## Limitations

The global conjecture for arbitrary odd integers is unproved here. No asymptotic density among all odd integers is claimed. The arithmetic checker only covers its documented finite exponent ranges; it is not an infinite proof. Additional unidentified prior results or uninspected full text, especially general iterate-height theorems extending beyond restricted domains, remain an originality risk.

## References

1. Colin Defant, *On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions*, *Journal of Integer Sequences* **18** (2015), Article 15.2.1, first published 2015-01-13. Full open-access version: https://arxiv.org/html/1506.05426v1 (arXiv version publicly posted 2015-06-17).
2. Colin Defant, *A Note about Iterated Arithmetic Functions*, arXiv:1501.06075v1, publicly posted 2015-01-24. Open-access full text: https://arxiv.org/html/1501.06075v1.
3. J. Harrington and L. Jones, *On the Iteration of a Function Related to Euler's \(\phi\)-Function*, *Integers* **10** (2010), 497–515, DOI: 10.1515/integ.2010.042. Scope described in [1, Section 4]; complete full-text comparison not completed.
