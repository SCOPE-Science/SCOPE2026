# A corrected right-waist distribution for order-decreasing partial injections

## Finding

Let \(\mathcal D_n\) consist of all partial injections \(\alpha:D\to\{1,\ldots,n\}\), where \(D\subseteq\{1,\ldots,n\}\), satisfying \(\alpha(x)\le x\) for every \(x\in D\). For a nonempty image define the **right waist** \(w(\alpha)=\max\operatorname{im}\alpha\); set the empty map's waist to zero. Let \(F(n,k)\) be the number of maps of waist \(k\).

For all integers \(n\ge1\), \(1\le k\le n\), and \(m=n-k\),

\[
\boxed{F(n,k)=(m+1)\sum_{r=0}^{k-1}\left\{\begin{matrix}k\\k-r\end{matrix}\right\}\sum_{s=0}^{\min(m,k-1-r)}\binom ms\,(k-1-r)_{\underline s}.}
\]

Here \(\left\{\begin{matrix}a\\b\end{matrix}\right\}\) is a Stirling number of the second kind, and \((a)_{\underline s}=a(a-1)\cdots(a-s+1)\) with \((a)_{\underline0}=1\). Also \(F(n,0)=1\), and \(F(n,k)=0\) for \(k\notin\{0,\ldots,n\}\).

In particular, for every \(n\ge3\),

\[
\boxed{F(n,3)=(n-2)(n^2-2n+2)=5\binom n3+\binom{n-2}{3}.}
\]

Consequently the published right-waist Conjecture 4.2 of Umar, \(F(n,k)=\binom nk B_k\) with Bell numbers \(B_k\), is false. Its first failure in the ordering by \(n\) occurs at \((n,k)=(5,3)\): \(F(5,3)=51\), whereas \(\binom53 B_3=50\). The waist-three identity disproves it for every \(n\ge5\).

## Assumptions and scope

All maps are labeled partial one-to-one transformations on the finite chain \(\{1,\ldots,n\}\). The condition is order-**decreasing** (\(\alpha(x)\le x\)); the map is **not** required to be order-preserving (monotone). No restrictions on the domain beyond being a subset of the chain are imposed. The empty map is counted exactly once at waist zero. The theorem concerns individual labeled maps, not conjugacy classes.

## Proof

**1. Rook/Stirling subcount.** Let \(a(t,r)\) count order-decreasing partial injections on \(\{1,\ldots,t\}\) of rank \(r\), for integers \(t\ge0\) and \(0\le r\le t\). When extending from \(t-1\) to \(t\), either input \(t\) is absent, or it is mapped to one of \(t-r+1\) output values unoccupied by the previous rank-\((r-1)\) map. Thus

\[
a(t,r)=a(t-1,r)+(t-r+1)a(t-1,r-1),\quad a(0,0)=1.
\]

Taking out-of-range terms as zero, the recurrence and the Stirling recurrence give, for all such \(t,r\),

\[
a(t,r)=\left\{\begin{matrix}t+1\\t+1-r\end{matrix}\right\}.
\]

**2. Conditioning on the maximum image.** Fix \(n\ge k\ge1\), and put \(m=n-k\). Every map of waist \(k\) has a unique preimage \(x\) of \(k\), with \(k\le x\le n\); there are \(m+1\) choices. After fixing \(x\), the remaining \(m\) potential domain points in \(\{k,\ldots,n\}\setminus\{x\}\) are all at least \(k\), regardless of which \(x\) was chosen.

Restrict the map to inputs \(\{1,\ldots,k-1\}\). If the restriction has rank \(r\), its image uses \(r\) distinct numbers from \(\{1,\ldots,k-1\}\), and Step 1 gives exactly \(\left\{\begin{matrix}k\\k-r\end{matrix}\right\}\) possibilities. The \(m\) remaining potential domain points may contain any \(s\) mapped points, where \(0\le s\le\min(m,k-1-r)\). Choose these domain points in \(\binom ms\) ways; map them injectively into the \(k-1-r\) unused outputs in \((k-1-r)_{\underline s}\) ways. All such mappings are order-decreasing because every selected input is at least \(k\) and every remaining output is smaller than \(k\). The construction is reversible, so multiplying and summing yields the displayed exact formula, with no overcounting.

**3. Explicit contradiction and infinite family.** For \(k=3\), the three possible restriction ranks are \(r=0,1,2\), with Stirling coefficients \(1,3,1\). Their inner sums are respectively \(m^2+m+1\), \(1+m\), and \(1\). Hence

\[
F(n,3)=(m+1)(m^2+4m+5)=(n-2)(n^2-2n+2).
\]

Since \(B_3=5\), subtracting the conjectured \(5\binom n3\) gives exactly \(\binom{n-2}{3}\), which is positive for every \(n\ge5\). Direct evaluation of the proven formula gives the predicted distribution for \(1\le n\le4\), confirming the first failure at size five: at \(n=5\), the full waist distribution (including waist zero) is \((1,5,20,51,74,52)\), while the conjectured row is \((1,5,20,50,75,52)\).

## Verification

The standalone \(`verify.py`\) reproduces the formula using exact integer arithmetic; independently enumerates all partial injections and tests order decrease for \(1\le n\le7\); separately computes all counts using a subset-state dynamic program for \(1\le n\le16\); checks \(\sum_{k=0}^nF(n,k)=B_{n+1}\) for each checked \(n\); and verifies the waist-three polynomial and correction term for \(3\le n\le100\). Run with \(`python3 verify.py`\). A successful run emits \(`VERIFY_OK_UMAR_RIGHT_WAIST_CORRECTION`\). The general theorem is proved above; finite tests alone would not prove it.

## Relationship to prior work

A. Umar, *Some combinatorial problems in the theory of symmetric inverse semigroups*, Algebra and Discrete Mathematics **9** (2010), no. 2, pp. 115–126, Section 4, defines precisely this order-decreasing partial-injection semigroup, proves a distinct fixed-point distribution (Proposition 4.1), and explicitly proposes the now-refuted Bell-binomial right-waist formula (Conjecture 4.2 and Table 7). The known Stirling rank enumeration is used as input, not claimed as new. The contribution is the exact waist-refined count and the universal counterexample family.

Later work on orientation-preserving, order-preserving, or metric-constrained partial maps studies narrower transformation classes and does not by itself imply this unrestricted order-decreasing right-waist formula. The possibility of an equivalent formula elsewhere in the literature remains open to historical verification.

## Limitations

This does not enumerate joint right-waist/fixed-point/rank strata, describe multiplication or ideals of \(\mathcal D_n\), or establish historical uniqueness of the formula. Publication priority remains subject to examination of additional older enumeration literature. The recorded verification is a direct finite check and has not received independent mathematical auditing.

## References

1. A. Umar, *Some combinatorial problems in the theory of symmetric inverse semigroups*, **Algebra and Discrete Mathematics** 9 (2010), no. 2, 115–126, especially p. 121, Conjecture 4.2. https://adm.luguniv.edu.ua/downloads/issues/2010/N2/adm-n2-9.pdf
2. A. Umar, *On the semigroups of partial one-to-one order-decreasing finite transformations*, **Proceedings of the Royal Society of Edinburgh A** 123 (1993), 355–363. https://doi.org/10.1017/S0308210500025737
3. A. Umar, *Combinatorial results for semigroups of orientation-preserving partial transformations*, **Journal of Integer Sequences** 14 (2011), Article 11.7.5. https://cs.uwaterloo.ca/journals/JIS/VOL14/Umar/umar2.pdf
