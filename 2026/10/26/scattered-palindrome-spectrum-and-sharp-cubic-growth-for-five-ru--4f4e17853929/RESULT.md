# Scattered palindrome spectrum and sharp cubic growth for five-run binary words

## Finding

Let \(w=0^a1^b0^c1^d0^e\) with \(a,b,c,d,e\) positive integers, and let \(P_w(z)\) be the polynomial in which the coefficient of \(z^\ell\) counts **distinct nonempty palindromic scattered subsequence strings** of length \(\ell\). Set
\[
A=\min(a,c+e),\quad B=\min(e,a+c),\quad E=\min(a,e),\quad T=\min(b,d).
\]
For \(m\geq0\), define \(U_m(z)=\sum_{j=1}^{m}z^j\) and \(V_m(z)=\sum_{j=1}^{m}z^{2j}\), with empty sums equal to zero. Then the complete length spectrum is
\[
\boxed{\begin{aligned}
P_w(z)={}&U_{a+c+e}(z)+U_{b+d}(z)+V_E(z)U_{b+d}(z)\\
&+(V_A(z)-V_E(z))U_b(z)+(V_B(z)-V_E(z))U_d(z)\\
&+V_T(z)U_c(z)(1+V_E(z)).
\end{aligned}}
\]
In particular, the total number of distinct nonempty scattered palindromes is
\[
\boxed{P_w(1)=a+b+c+d+e+b\min(a,c+e)+d\min(e,a+c)+(\min(a,e)+1)c\min(b,d).}
\]
Writing \(M_5(n)\) for the maximum of this number over all length-\(n\) binary words having exactly five nonempty maximal constant runs (either initial symbol), we have
\[
\boxed{M_5(n)=\frac{n^3}{108}+O(n^2)\qquad(n\longrightarrow\infty).}
\]
For any sequence of such words whose lengths \(n\) tend to infinity, the normalized ratio \(P_w(1)/n^3\) tends to \(1/108\) **if and only if** the ordered run lengths divided by \(n\) tend to
\[
\boxed{(1/6,\ 1/6,\ 1/3,\ 1/6,\ 1/6).}
\]
This is the first run-count threshold at which binary words can have cubically many distinct scattered palindromes: any word with at most four constant runs has only \(O(n^2)\) distinct scattered palindromes.

## Assumptions and scope

A scattered subsequence is obtained by deleting arbitrary positions while retaining the order of those kept. Subsequences are identified by their resulting strings, not their embeddings. A palindrome is invariant under reversal; the empty subsequence is excluded. All run lengths are positive. The statement concerns linear words (not cyclic rotations). Complementing all symbols does not affect the count, so the displayed alternating word covers both initial symbols. The spectrum formula and total formula are exact for every positive five-tuple; the extremal statement is asymptotic, not an asserted closed form for every finite \(n\).

## Proof

**Step 1: possible run patterns.** Any subsequence of a five-run word has at most five runs. A nonconstant binary palindrome must have an odd number of runs, so its only possible patterns are \(0^i1^j0^i\), \(1^i0^j1^i\), or \(0^i1^j0^k1^j0^i\), with positive exponents. Monochromatic palindromes are also possible. These five classes (the two monochromatic classes and the three mixed patterns) are disjoint by their strings.

**Step 2: monochromatic and five-run classes.** The monochromatic subsequences are \(0^r\) for \(1\leq r\leq a+c+e\) and \(1^r\) for \(1\leq r\leq b+d\), giving \(U_{a+c+e}+U_{b+d}\). Every five-run palindrome \(0^i1^j0^k1^j0^i\) must use its successive nonempty runs from the successive five input runs. Hence precisely \(1\leq i\leq E\), \(1\leq j\leq T\), and \(1\leq k\leq c\) are possible, giving \(V_E V_T U_c\).

**Step 3: three-run classes.** A palindrome \(1^i0^j1^i\) uses the two one-runs on either side of the middle zero-run; it occurs if and only if \(1\leq i\leq T\) and \(1\leq j\leq c\). Its contribution is \(V_T U_c\). For \(0^i1^j0^i\), if \(i\leq E\), its outer zeros can come from the first and last zero-runs. All \(b+d\) ones can be selected between them, so exactly \(1\leq j\leq b+d\) occur. If \(i>E\), at least one outer zero-run is too short. Then either the middle one-block must come entirely from the first one-run, for which \(i\leq A=\min(a,c+e)\) and \(j\leq b\), or entirely from the second one-run, for which \(i\leq B=\min(e,a+c)\) and \(j\leq d\). These extra ranges cannot overlap, since \(\min(A,B)=E\): if \(a\leq e\) then \(A=a=E\), whereas if \(e\leq a\) then \(B=e=E\). Thus the three disjoint contributions are \(V_E U_{b+d}\), \((V_A-V_E)U_b\), and \((V_B-V_E)U_d\). Collecting Steps 2 and 3 yields the displayed polynomial.

**Step 4: total count.** At \(z=1\), \(U_m(1)=V_m(1)=m\). Therefore
\[
P_w(1)=n+E(b+d)+(A-E)b+(B-E)d+Tc(1+E)=n+Ab+Bd+(E+1)Tc.
\]
All inequalities and equalities used above hold for every positive five-tuple, including equal outer run lengths.

**Step 5: sharp cubic coefficient and rigidity.** Put \(n=a+b+c+d+e\). Since \(2E+2T+c\leq n\), the arithmetic-geometric mean inequality gives
\[
ETc=\frac{(2E)(2T)c}{4}\leq\frac{1}{4}\left(\frac{n}{3}\right)^3=\frac{n^3}{108}.
\]
The other terms in the exact formula are uniformly quadratic: \(Ab+Bd\leq(a+c+e)(b+d)\leq n^2/4\), \(Tc\leq n^2/8\), and the remaining contribution is \(n\). Thus \(P_w(1)\leq n^3/108+3n^2/8+n\). For lengths \(n=6m\), the five-run words with lengths \((m,m,2m,m,m)\) give exactly \(2m^3+4m^2+6m\). For other sufficiently large \(n\), choose \(a=b=d=e=\lfloor n/6\rfloor\) and \(c=n-4\lfloor n/6\rfloor\), which produces \(n^3/108+O(n^2)\). This proves the sharp asymptotic.

For rigidity, if \(P_w(1)/n^3\to1/108\), the quadratic remainder disappears after division by \(n^3\), so \((2E/n)(2T/n)(c/n)\to1/27\), with their sum at most one. Equality is approached in the arithmetic-geometric mean inequality only when all three quantities tend to \(1/3\) and their sum tends to one. Therefore \(E/n\to1/6\), \(T/n\to1/6\), \(c/n\to1/3\), and the nonnegative slack \(n-(2E+2T+c)=(a-E)+(e-E)+(b-T)+(d-T)\) is \(o(n)\). Hence the full run-length proportions have the stated limit. Conversely those proportions inserted into the exact formula yield the limit \(1/108\).

**Step 6: four-run boundary.** With at most four input runs, every nonconstant palindromic subsequence has precisely three runs. A three-run palindrome is specified by just two positive exponents, both bounded by \(n\), so at most \(2n^2\) such strings occur. Together with at most \(2n\) monochromatic possibilities this is \(O(n^2)\), whereas the five-run construction above is cubic.

## Verification

The standalone program `verify.py` builds the actual set of distinct subsequence strings by iterative set extension, filters palindromes, and compares the entire length histogram with the formula for all \(4^5=1024\) positive run-length tuples with each run length at most four. It checks the closed total independently and enumerates all five-run compositions for \(5\leq n\leq30\) to provide finite extremal comparison data. It also checks the scaled exact construction for seven values. Execute `python3 verify.py` with Python 3 and no third-party dependencies. The expected leading output is `VERIFY_OK 1024 complete independent subsequence spectra, exact integer maxima n=5..30, symmetric witnesses, scaled constructions`. This finite testing is not offered as proof of the theorem for unbounded parameters; the proof is in Steps 1–6.

## Relationship to prior work

Mahalingam and Pandoh [1] formulate the invariant \(SP(w)\), prove general Fibonacci-type bounds, and study extrema conditioned on alphabet size. The exact five-run polynomial, the \(1/108\) run-restricted asymptotic and the uniqueness of its limiting run proportions are not among the inspected statements. Holub and Saari [2] show that the full set of scattered palindromic subsequences determines a binary word up to reversal, and investigate longest such subsequences and extension measures, not the five-run cardinality. Müllner and Ryzhikov [3] study longest palindrome and antipalindrome subsequences, particularly for circular words; their length bounds do not count distinct strings. General counting bounds do not imply the sharper run-restricted exact formula.

## Limitations

The theorem is for binary words with exactly five positive runs and for the at-most-four-run growth boundary. It does not supply an exact finite-\(n\) maximization formula, a classification of every finite maximizer, or general formulas for arbitrary run counts. The \(O(n^2)\) term is not claimed to be optimal. Searches and primary-literature comparisons do not establish global uniqueness of the result; an equivalent unindexed specialization could exist. Computational checks cover finite inputs only.

## References

[1] K. Mahalingam and P. Pandoh, *Counting scattered palindromes in a finite word*, arXiv:2108.02729, first public version 2021-08-05. https://arxiv.org/abs/2108.02729

[2] Š. Holub and K. Saari, *On highly palindromic words*, Discrete Applied Mathematics 157 (2009), 953–959. DOI:10.1016/j.dam.2008.03.039. Author-hosted manuscript: https://www.karlin.mff.cuni.cz/~holub/soubory/subpal.pdf

[3] C. Müllner and A. Ryzhikov, *Palindromic subsequences in finite words*, arXiv:1901.07502, 2019-01-22. https://arxiv.org/abs/1901.07502
