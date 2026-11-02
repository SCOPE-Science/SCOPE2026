# Uniqueness of the asymptotic Farey inversion minimizer

## Finding
For an integer \(n\ge4\), let \(\mathcal F_n\) be the Farey sequence of order \(n\). Call two of its members \(a/b<c/d\) **inverted** when \(a<c\) and \(b>d\). Write \(f(n)\) for the minimum number of Farey fractions *strictly between* an inverted pair. For every integer \(n\ge5{,}504{,}798\), write \(n=4m+r\), where \(0\le r\le3\). Exactly **one** inverted ordered pair realizes \(f(n)\):

\[
(a/b,c/d)=
\begin{cases}
((2m-1)/(4m),\;2m/(4m-1)),&r=0,\\
(2m/(4m+1),\;(2m+1)/(4m)),&r\in\{1,2,3\}.
\end{cases}
\]

The corresponding minimal intervening counts are \(m+1\), \(m+2\), \(m+2\), and \(m+4\) for \(r=0,1,2,3\), respectively. The numerical minimum and the displayed witnesses occur in earlier literature; the statement that these are the *only* minimizers is the additional result.

## Assumptions and scope
Fractions are in lowest terms, belong to \([0,1]\), and have positive denominators at most \(n\). Pairs are ordered by numerical value; uniqueness does not mean uniqueness up to symmetry. The explicit cutoff comes from the uniform analytic error bound in Wang–Xie–Zhao [2, Section 5]. The theorem does not assert uniqueness below that cutoff, nor classify pairs with more than the minimal number of intervening terms.

## Proof
**1. Reduction to a left endpoint.** If \(a/b<c/d\) is inverted, then \(c\ge a+1\), \(d\le b-1\), and hence \(1\le a\le b-2\). Put
\[
C_n(a,b)=\#\left(\mathcal F_n\cap\left(a/b,(a+1)/(b-1)\right)\right).
\]
Since \(c/d\ge(a+1)/(b-1)\), the number of fractions strictly between the inverted pair is at least \(C_n(a,b)\). The constructions of van Doorn [1, Theorem 1] show \(f(n)\le U(n)\), where \(U(4m)=m+1\), \(U(4m+1)=U(4m+2)=m+2\), and \(U(4m+3)=m+4\).

**2. Exclusion away from one half.** If \(b\le n/4\), the bound in [2, proof of Theorem 3.1] is \(C_n(a,b)>4n/7-1>U(n)\) in the stated range. If \(b>n/4\) and \(b-2a\notin\{1,2\}\), the explicit Section 5 estimate in [2] gives
\[
C_n(a,b)\ge\frac{5n}{18}-E(n)>\frac n4+4\ge U(n)
\]
for all \(n\ge5{,}504{,}798\), with
\[
E(n)=(9\lfloor\sqrt n\rfloor+3)
\left(\frac{61}{100}\log(9\lfloor\sqrt n\rfloor+3)+\frac76\right)
<\frac n{36}-4.
\]
Thus a minimizing left endpoint must satisfy \(b-2a\in\{1,2\}\).

**3. Three nested interval families.** If \(b-2a=2\), coprimality forces \(a=2t-1\), \(b=4t\), and the candidate interval is
\[I_t=((2t-1)/(4t),\;2t/(4t-1)),\quad1\le t\le m.\]
If \(b-2a=1\) and \(a\) is even, the interval is
\[J_t=(2t/(4t+1),\;(2t+1)/(4t)),\quad1\le t\le m\ (r>0),\quad t\le m-1\ (r=0).\]
If \(b-2a=1\) and \(a\) is odd, the interval is
\[K_t=((2t+1)/(4t+3),\;(t+1)/(2t+1)),\quad 0\le t\le m-1,\]
with the additional possible case \(K_m\) when \(r=3\). Each family shrinks as \(t\) increases. The reduced right endpoint of \(K_t\) is not necessarily an eligible numerator-increasing/denominator-decreasing endpoint, so the case \(K_m\) is treated separately.

**4. Strict comparison for all noncanonical left endpoints.** The explicit fraction lists in [2, proof of Theorem 4.1] give the lower counts \(U(n)\) in the terminal intervals of these families. Each noncanonical case has a *further* interior Farey fraction not in the corresponding cited list:

* For \(I_m\) with \(r=1,2\), the extra fraction is \((2m+1)/(4m+1)\). For \(r=3\), it is \((2m+2)/(4m+3)\). In both cases the denominator is at most \(n\), the fraction is reduced, and cross multiplication places it strictly inside \(I_m\). Thus \(C_n(I_m)>U(n)\) whenever \(r>0\).
* For \(I_t\) when \(r=0\) and \(t<m\), the interval \(I_t\) contains \(I_m\) and also \((m-1)/(2m-1)\), which lies strictly between the left endpoints of \(I_{m-1}\) and \(I_m\). Hence its count exceeds \(U(n)\).
* For \(J_t\) when \(r=0\), necessarily \(t\le m-1\). The \(m+1\) fractions \(s/(2s-1)\) for \(m\le s\le2m\) from [2] are joined by \(1/2\) in \(J_{m-1}\); hence the count is at least \(m+2>U(n)\).
* For \(J_t\) when \(r>0\) and \(t<m\), the interval \(J_t\) contains \(J_m\) and the extra reduced fraction \(m/(2m-1)\), strictly between the right endpoints of \(J_m\) and \(J_{m-1}\). Hence the count exceeds \(U(n)\).
* For \(K_t\) with \(t\le m-1\), the lists in [2, Theorem 4.1] already give at least \(U(n)\) fractions in \(K_{m-1}\). The reduced fraction \((2m+1)/(4m)\) is strictly inside \(K_{m-1}\) but is absent from each of those lists. Therefore \(C_n(K_t)>U(n)\) for every such \(t\).

Here all displayed additional fractions have denominator at most \(n\); differences of the relevant cross products equal \(1\) or \(2\), so no unproved approximation enters these strict inequalities.

**5. The exceptional left endpoint.** For \(r=3\), the remaining \(K_m\) begins at \(L=(2m+1)/(4m+3)\). Any possible inverted right endpoint \(c/d\) has \(c\ge2m+2\), \(d\le4m+2\), and \((c,d)\ne(2m+2,4m+2)\) because that pair is not coprime. Thus
\[c/d\ge(2m+2)/(4m+1).\]
The proof of Theorem 1.2 in [2] identifies \(m+4=U(n)\) distinct Farey fractions in the half-open interval \( (L,(2m+1)/(4m)] \), namely \(1/2\), \((2m+1)/(4m)\), and \(s/(2s-1)\) for \(m+1\le s\le2m+2\), with the rightmost endpoint \((2m+1)/(4m)\) counted as interior to \((L,c/d)\). One further reduced fraction, \(m/(2m-1)\), lies strictly between \((2m+1)/(4m)\) and \((2m+2)/(4m+1)\) whenever \(m>2\); the latter inequality follows by cross multiplication from \(m-2>0\). Hence the actual inverted pair contains at least \(U(n)+1\) intervening fractions. This excludes \(K_m\).

**6. Existence and uniqueness of the right endpoint.** Only \(I_m\) for \(r=0\) and \(J_m\) for \(r>0\) remain. Van Doorn's explicit lists of successive Farey fractions [1, Theorem 1] show that their displayed endpoints are reduced, belong to \(\mathcal F_n\), are inverted, and enclose exactly \(U(n)\) intervening fractions. In either surviving interval, the candidate \((a+1)/(b-1)\) is *itself* the displayed reduced right endpoint. Choosing any later \(c/d\) would put this reduced candidate strictly between the two endpoints, producing at least \(U(n)+1\) fractions. Thus each surviving left endpoint has a unique minimizing right endpoint, proving the theorem. \(\square\)

## Verification
Running `python3 verify.py` regenerates the Farey sequences with exact rational comparisons, checks 220 central interval cardinalities for \(6\le m\le25\), and independently enumerates all inverted minimizers at 32 sample orders between \(120\) and \(200\). It also checks the numerical strictness of the explicit published error inequality at \(n=5{,}504{,}798\). Those finite tests corroborate the new strict comparisons; the argument for *all* larger \(n\) uses the cited uniform analytic bound and the symbolic inequalities in the proof. Finite tests are not asserted to prove an infinite statement.

## Relationship to prior work
Van Doorn [1, Section 2] constructs the exact candidate pairs and explicitly proposes a stronger investigation of *all* near-optimal inverted pairs. Wang, Xie and Zhao [2] determine the minimum count \(f(n)\) and prove uniform exclusion of off-center intervals, but the statements of their main theorems do not classify or count all minimizers. Cipollini [3] determines the asymptotic minimum only. OEIS A386893 [4] records \(f(n)\), not the number or uniqueness of attaining pairs. The present theorem refines the exact minimization result to a unique optimizer, not merely a value or existence assertion. Its main analytic exclusion is deliberately inherited from [2].

## Limitations
The cutoff \(5{,}504{,}798\) is sufficient, not shown optimal. Smaller orders can have additional minimizing pairs; no classification below the stated cutoff is claimed. A separate bibliographic source could conceivably already contain the optimizer classification, although targeted searches found none. The proof depends on the published uniform counting estimate and exact Farey continuation formulas in [1,2], not on new independent proofs of those foundational results.

## References
1. W. van Doorn, *Improved bounds for the Mayer–Erdős phenomenon on similarly ordered Farey fractions*, arXiv:2509.00121v1 (28 August 2025), especially Theorem 1 and Section 2. https://arxiv.org/html/2509.00121v1
2. Y. Wang, M. Xie and Z. Zhao, *An exact formula for Erdős’ problem 1005*, arXiv:2608.15681v1 (16 August 2026), Theorems 3.1 and 4.1, proof of Theorem 1.2, and Section 5. https://arxiv.org/html/2608.15681v1
3. R. Cipollini, *Optimality of Wouter van Doorn's Upper Bound for the Mayer–Erdős Farey Problem*, arXiv:2607.23302v1 (25 July 2026). https://arxiv.org/abs/2607.23302
4. OEIS Foundation, A386893, *Minimal number of Farey fractions in between two fractions that are not similarly ordered*. https://oeis.org/A386893
