# Finite-horizon periodicity and a sharp four-term census for odd-greedy Egyptian fractions

## Finding
Fix positive integers \(a\) and \(h\). For an odd integer \(d>a\), run the odd-greedy Egyptian-fraction algorithm on \(a/d\), permitting repeated unit-fraction denominators; let \(T_a(d)\) be its exact number of terms, or \(\infty\) if it never stops. Put
\[
M_j(a)=2\operatorname{lcm}(1,2,\ldots,2^j a),\qquad
P(a,h)=\prod_{j=0}^{h-1}M_j(a).
\]
Then the event \(T_a(d)\le h\), and also the exact stopping time \(T_a(d)=t\) for each \(t\le h\), depend only on the class of \(d\pmod {P(a,h)}\). In particular, for fixed \(a,h\), these sets are eventually periodic and possess computable rational natural densities among odd positive denominators. The assertion does not assume that the algorithm always terminates.

For the natural even-numerator family \(2/d\), \(d\ge5\) odd, an unexpectedly small, **minimal** exact period appears:
\[
T_2(d)=4 \quad\Longleftrightarrow\quad
 d\bmod 60\in\{7,35,47,55\}.
\]
The previously classified two-term case, \(T_2(d)=2\), occurs precisely when \(d\equiv1\pmod4\) or \(d\equiv3\pmod{12}\). Therefore the relative natural densities among odd denominators of stopping in precisely two and precisely four terms are, respectively, \(2/3\) and \(2/15\), and
\[
\lim_{X\to\infty}
\frac{\#\{d\le X:\ d\ge5,\ d\text{ odd},\ T_2(d)\le4\}}
{\#\{d\le X:\ d\ge5,\ d\text{ odd}\}}
=\frac45.
\]
The remaining density \(1/5\) has not stopped after four steps; no assertion about eventual termination is made.

## Assumptions and scope
The input consists of a positive integer numerator \(a\), an odd denominator \(d>a\), and the rational \(a/d\in(0,1)\); cancellation of any common factor is optional, because the algorithm is defined by the rational value. For a positive remainder \(A/B\in(0,1)\) with \(B\) odd, its next denominator \(u\) is the least *positive odd integer* satisfying \(u\ge B/A\), and the next unreduced remainder is \((Au-B)/(Bu)\). Stop at the first zero numerator, counting the just-used term. This is the convention of Louwsma and Martino (repetitions allowed), but for \(2/d\) with \(d\ge5\) no repetition arises. A finite-horizon statement does not assert finite ultimate stopping time.

## Proof
**1. Bounded unreduced numerators.** Define \(A_0=a\), \(B_0=d\), and, while \(A_j>0\), let \(u_j\) be the least odd integer not less than \(B_j/A_j\), setting
\[
A_{j+1}=A_j u_j-B_j,\qquad B_{j+1}=B_j u_j.
\]
By minimality of the odd ceiling, \(0\le u_j-B_j/A_j<2\), hence \(0\le A_{j+1}<2A_j\). Thus all positive numerator states encountered before step \(h\) satisfy \(1\le A_j\le 2^ja\), irrespective of denominator growth or cancellations. The denominators \(B_j\) remain odd and the positive remainders remain below one.

**2. An explicit periodicity certificate.** For \(0\le j\le h\), set \(Q_j=\prod_{i=j}^{h-1}M_i(a)\), so \(Q_0=P(a,h)\) and \(Q_h=1\). Compare two odd initial denominators \(d,d'>a\) with \(d'\equiv d\pmod{Q_0}\). Inductively suppose both are still active with *exactly equal* unreduced numerator \(A_j'=A_j>0\) and \(B_j'\equiv B_j\pmod{Q_j}\). Since \(2A_j\mid M_j(a)\), their denominator difference is a multiple of \(2A_jQ_{j+1}\). For an integer \(t\), we therefore have
\[
B_j'=B_j+2A_jQ_{j+1}t,\qquad
u_j'=u_j+2Q_{j+1}t.
\]
The latter equality follows because adding an even integer to \(B_j/A_j\) simply translates its least-odd-integer ceiling. Consequently
\[
A_{j+1}'=A_j(u_j+2Q_{j+1}t)-(B_j+2A_jQ_{j+1}t)=A_{j+1},
\]
and \(B_{j+1}'-B_{j+1}\) is divisible by \(Q_{j+1}\): both products \(B_j'u_j'\) and \(B_ju_j\) are congruent modulo \(Q_{j+1}\). If the new numerator is zero both processes halt simultaneously. This proves equality of the stopping behavior through step \(h\) for any input pair in the same residue class modulo \(P(a,h)\). A finite union of residue classes has a rational natural density, obtained by enumerating a complete residue system once; restricting to odd denominators causes no complication since the period is even.

**3. Two versus four steps for \(2/d\).** Take \(d\ge5\) odd. If \(d\equiv1\pmod4\), then \(u_0=(d+1)/2\) is odd, so \(A_1=1\); the next term is the unit fraction \(1/(du_0)\), and \(T_2(d)=2\). If \(d\equiv3\pmod4\), then \(u_0=(d+3)/2\) is odd and \(A_1=3\). Write \(B=d(d+3)/2\). Now \(3\mid B\) precisely when \(d\equiv3\pmod{12}\); in that case the next term ends the algorithm at step two. For the remaining odd denominators, \(d\equiv7\) or \(11\pmod{12}\), and \(B\equiv5\pmod6\). The next odd denominator is \(v=(B+4)/3\), and the next unreduced numerator is \(3v-B=4\), with denominator
\[
C=Bv=\frac{B(B+4)}3.
\]
For every odd \(B\), \(B(B+4)\equiv5\pmod8\). Because \(3^{-1}\equiv3\pmod8\), one gets \(C\equiv7\pmod8\). The next least odd denominator is \(w=(C+5)/4\), resulting in unreduced numerator \(4w-C=5\) and denominator \(D=Cw\). The *fourth* step finishes exactly when \(D\equiv0\pmod5\), equivalent to \(C\equiv0\pmod5\) since \(w\equiv4^{-1}C\pmod5\). Because 3 is invertible modulo 5, this means \(B\equiv0\) or \(1\pmod5\). Substituting \(B=d(d+3)/2\) shows this is equivalent to \(d\equiv0\) or \(2\pmod5\). The Chinese remainder theorem with \(d\equiv7\) or \(11\pmod{12}\) gives precisely the four classes \(\{7,35,47,55\}\pmod{60}\). Other cases cannot stop in four steps, because the fourth unreduced numerator remains nonzero. Neither can any \(2/d\) terminate at an odd length: at each step the odd-denominator recurrence reverses the numerator parity, from initially even to odd and back.

**4. Densities and minimality.** Of six odd residues modulo 12, four correspond to two-term stopping, giving \(2/3\). Of thirty odd residues modulo 60, four correspond to four-term stopping, giving \(2/15\). They are disjoint and add to \(4/5\). Modulus 60 is a period. No proper divisor is a period: class 7 belongs to the four-term set, whereas classes 37, 27 and 19 do not, excluding periods 30, 20 and 12 respectively. Any proper period together with 60 would force the greatest common divisor to be a proper period dividing one of these maximal proper divisors. Hence 60 is least.

## Verification
The accompanying standalone Python script `checker.py` uses only standard-library exact integers. It directly computes the first four odd-greedy steps for all 50,001 odd denominators from 5 through 100,005, compares the stopping times to the residue classification, checks explicit periodicity for several different numerators and horizons using the stated product period, and tests the numerator bound and minimal period. A separate reduced-fraction implementation supplies an independent arithmetic comparison for numerators 1 through 9 and odd denominators through 200. All checks passed when executed from the provided file. These finite tests test implementation and edge cases; the all-denominator statements follow from the preceding proofs, not extrapolation.

## Relationship to prior work
The odd-greedy termination problem remains open in general. Pihko (2001), particularly Theorem 3.8, constructs long forced trajectories and treats arithmetic families of residue numerators rather than finite-horizon stopping-class densities. Eppstein (2007) discusses subgreedy algorithms and observes that remainder numerators are efficiently tracked by modular arithmetic. Louwsma and Martino (2023, Theorem 3.2) parametrizes all expansions with a *fixed prefix of unit-fraction denominators*, and their 2025 Theorem 3 / Example 6 includes the **already known** classification of exactly two terms for \(2/d\). Their parametric description covers many individual four-term expansions in principle; its logical scope and this finding's full fixed-initial-numerator density classification have been compared. The new contribution claimed here is the uniform fixed-numerator finite-horizon period theorem together with the explicit, smallest-period four-term census and density; no credit is claimed for the two-term census, parity law, or basic greedy recurrence.

## Limitations
The explicit general period \(P(a,h)\) is enormous and is not claimed minimal. The theorem gives periodicity only at each fixed finite horizon, not eventual periodicity of the full stopping-time function and not universal termination. The \(4/5\) density refers to termination within four terms, not all-time termination. Searches of accessible literature and mathematical-result records did not establish uniqueness of these claims; an equivalent unindexed consequence of a broader parametrization, particularly the 2023 fixed-prefix description, is a residual originality risk.

## References
- J. Pihko, “Remarks on the ‘Greedy Odd’ Egyptian Fraction Algorithm,” *Fibonacci Quarterly* **39** (2001), 221–227, https://www.fq.math.ca/Scanned/39-3/pihko.pdf.
- D. Eppstein, “Subgreedy Egyptian Expansions,” January 10, 2007, https://11011110.github.io/blog/2007/01/10/subgreedy-egyptian-expansions.html.
- J. Louwsma and J. Martino, “Rational Numbers with Odd Greedy Expansion of Fixed Length,” arXiv:2309.07280v1, September 13, 2023, https://arxiv.org/pdf/2309.07280.
- J. Louwsma and J. Martino, “Rational Numbers with Two-Term Odd Greedy Expansion,” *Integers* **25** (2025), A46, https://math.colgate.edu/~integers/z46/z46.pdf.
- K. S. Brown, “Odd-Greedy Unit Fraction Expansions,” https://www.mathpages.com/home/kmath478.htm (web resource, publication date not verified).
