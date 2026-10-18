# Quadratic splitting and exact idempotent census for complete-graph evolution algebras

## Finding
For every integer \(n\geq3\), let \(E_n(K)\) be the evolution algebra of the complete graph on \(n\) vertices over a finite field \(K=\mathbb F_{p^f}\): on a natural basis \(e_1,\ldots,e_n\), distinct basis elements multiply to zero and
\[
e_i^2=\sum_{j\ne i} e_j.
\]
An idempotent is an element \(x\in E_n(K)\) satisfying \(x^2=x\). Let \(I_{n,p}(f)\) denote their number, **including zero**. All idempotents over an algebraic closure of \(\mathbb F_p\) are defined over \(\mathbb F_{p^2}\). In particular, \(I_{n,p}(f)\) depends only on the parity of \(f\).

For odd \(p\), put \(m_k=2k-n\), \(d_k=1-4k(n-k)\), and
\[
Z_{n,p}=\sum_{\substack{0\le k\le n\\m_k\equiv0\ ({\rm mod}\ p)}}\binom nk.
\]
Write \(\chi_{p^f}\) for the quadratic character of \(\mathbb F_{p^f}\), extended by \(\chi_{p^f}(0)=0\), with integers interpreted in the prime subfield. Then the complete formula is
\[
I_{n,p}(f)=
\begin{cases}
\frac{2^n-Z_{n,p}}2,&n\equiv1\pmod p,\\[4pt]
1+\frac{2^n-Z_{n,p}}2,&n\equiv-1\pmod p,\\[4pt]
2^{n-1}+\frac12\sum_{k=0}^n\binom nk\chi_{p^f}(d_k),&n\not\equiv\pm1\pmod p.
\end{cases}
\]
For \(p=2\), the complete formula is
\[
I_{n,2}(f)=
\begin{cases}
2^{n-1},&n\text{ odd},\\
2^{n-1},&n\text{ even and }f\text{ odd},\\
2^n,&n\text{ even and }f\text{ even}.
\end{cases}
\]
For odd primes satisfying \(p>n^2\), all \(2^n\) geometric idempotents are distinct and are rational over \(\mathbb F_{p^2}\). More generally, if \(p\) is odd, \(n\not\equiv\pm1\pmod p\), and \(f\) is even, then
\[
I_{n,p}(f)=2^n-\frac12\sum_{\substack{0\le k\le n\\d_k\equiv0\ ({\rm mod}\ p)}}\binom nk.
\]
Thus the exceptional characteristics and the deficit from the maximum are explicitly controlled by the integers \(1-4k(n-k)\) and \(n\pm1\).

## Assumptions and scope
The graph has no loops. Its associated structure matrix has zero diagonal and all off-diagonal entries equal to one. All assertions count solutions of the full idempotent equation, not just natural-basis vectors. The field characteristic is arbitrary; the odd- and even-characteristic formulas are separated because the parameterizations differ. The bound \(2^n\) is a count of distinct solutions (not scheme length). These results do not characterize expansion among general evolution algebras.

## Proof
Write \(x=\sum_i x_i e_i\) and \(S=\sum_j x_j^2\). Direct multiplication gives \((x^2)_i=S-x_i^2\), so the complete system is
\[
x_i^2+x_i=S \qquad(1\le i\le n).
\]
**Odd characteristic.** Set \(t_i=2x_i+1\). The system implies \(t_i^2=1+4S\), independent of \(i\). If the common square is zero, \(t_i=0\) for every \(i\); thus \(x_i=-1/2\), which satisfies the system exactly when \(n+1=0\) in the field. This contributes a single exceptional scalar idempotent.

Otherwise choose \(y\ne0\) with \(t_i=\epsilon_i y\), where each \(\epsilon_i\in\{1,-1\}\). Setting \(m=\sum_i\epsilon_i\), the equality \(4S=\sum_i(\epsilon_i y-1)^2=n(1+y^2)-2my\) and \(4S=y^2-1\) are equivalent to
\[
(n-1)y^2-2my+(n+1)=0.\tag{1}
\]
Conversely, any sign vector and any nonzero root of (1) determine an idempotent through \(x_i=(\epsilon_i y-1)/2\). Each idempotent with \(y\ne0\) is represented **exactly twice** by \((\epsilon,y)\) and \((-\epsilon,-y)\). There are \(\binom nk\) sign vectors with \(k\) positive coordinates, and for them \(m=m_k\).

If \(n\ne1\) in the prime field, (1) is genuinely quadratic, with discriminant \(4d_k\), hence \(1+\chi_{p^f}(d_k)\) roots. Its root zero must be excluded exactly when \(n=-1\) in that field. Accounting for the scalar solution and dividing the number of nonzero-root representations by two proves the middle and last branches: when \(n=-1\), the discriminant becomes \(m_k^2\), and its character is one unless \(m_k=0\). If \(n=1\), (1) reduces to \(-2my+2=0\), which has one nonzero solution when \(m\ne0\), and none when \(m=0\). This proves the first branch.

**Characteristic two.** Every pair of roots of \(z^2+z+S=0\) differs by zero or one. Consequently write all coordinates as \(x_i=a+\eta_i\), with \(\eta_i\in\{0,1\}\) and let \(k=\sum_i\eta_i\), interpreted modulo two. The equation becomes
\[
(n-1)a^2+a+k=0.\tag{2}
\]
For odd \(n\), the coefficient \(n-1\) vanishes and (2) has the unique solution \(a=k\in\mathbb F_2\). For even \(n\), it is \(a^2+a=k\): when \(k=0\) it has the two roots zero and one; when \(k=1\) it has the two roots in \(\mathbb F_4\setminus\mathbb F_2\) and has solutions in \(\mathbb F_{2^f}\) precisely when \(f\) is even. The representation \((a,\eta)\) identifies exactly with \((a+1,1-\eta)\), so division by two yields the stated counts.

**Quadratic splitting and sharpness.** In odd characteristic, equation (1) has coefficients in \(\mathbb F_p\) and degree at most two, hence all its roots lie in \(\mathbb F_{p^2}\); the exceptional scalar point does as well. In characteristic two, equation (2) has all roots in \(\mathbb F_4\). Thus every geometric idempotent is defined over the quadratic prime-field extension. The intersection \(\mathbb F_{p^f}\cap\mathbb F_{p^2}=\mathbb F_{p^{\gcd(f,2)}}\) proves parity dependence. For odd \(p>n^2\), neither \(n-1\) nor \(n+1\) vanishes and none of the nonzero integers \(d_k\) vanishes modulo \(p\); each sign vector then has two nonzero roots over \(\mathbb F_{p^2}\), giving exactly \(2^n\) idempotents after the two-to-one identification. For even \(f\) and arbitrary odd \(p\), the quadratic character of a nonzero prime-subfield element equals one, yielding the displayed deficit formula. This completes the proof.

## Verification
The accompanying standalone `verify.py` performs direct finite-field arithmetic (including explicit quadratic extensions) and enumerates all possible coordinate tuples for 38 configurations. For each, it checks the idempotent equations against the piecewise formulas rather than using the sign-vector parameterization to count candidates. These exhaustive **finite checks** are supplementary; the general proof is the two-to-one parameterization and root count above. The checker runs with `python3 verify.py` and ends with `VERIFY_OK`.

For instance, in dimension three and characteristic three there are exactly two idempotents over \(\mathbb F_3\), but eight over \(\mathbb F_9\). In dimension four and characteristic two the counts are eight over \(\mathbb F_2\) and sixteen over \(\mathbb F_4\). In dimension three and characteristic seven, the repeated-discriminant case gives five idempotents over both \(\mathbb F_7\) and \(\mathbb F_{49}\).

## Relationship to prior work
Giacomelli introduced expander evolution algebras and explicitly considered the complete-graph algebra in Example 10.2 of arXiv:2605.12672 (first submitted 2026-05-12). That paper analyzes expansion, graph structure, and dynamics, not finite-field idempotent counts or the prime-field quadratic splitting asserted here. Narkuziyev, arXiv:2005.05793, studies idempotents of evolution algebras associated to two permutations, whose structural rows have at most two supported columns and which do not yield this full complete-graph family for dimensions at least four. The later survey arXiv:2610.22248 (first submitted 2026-10-15) establishes general perfect-algebra idempotent upper bounds and finite-field averages; it does not compute the complete-graph arithmetic census or its extension-parity law. Existing idempotent problems in evolution algebras motivate the invariant, but no general claim of uniqueness in the literature is made.

## Limitations
Only the all-ones, zero-diagonal complete-graph evolution algebra is classified. Neither weighted complete graphs nor general expanders are treated. The idempotent bound and parity law concern this specific family; no conclusion is drawn for arbitrary nonassociative algebras. Literature searches cannot exclude an equivalent unindexed or unpublished formula. The scientific work has not received an independent audit.

## References
1. P. Giacomelli, *Expander Evolution Algebras*, arXiv:2605.12672, first submitted 2026-05-12; in particular Example 10.2 and Section 11. https://arxiv.org/abs/2605.12672
2. B. A. Narkuziyev, *Some remarks on evolution algebras corresponding to permutations*, arXiv:2005.05793, 2020, especially Section 4. https://arxiv.org/abs/2005.05793
3. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248, first submitted 2026-10-15, Sections 2.1.4 and 2.1.10. https://arxiv.org/abs/2610.22248
4. A. Elduque and A. Labra, *Evolution algebras and graphs*, J. Algebra Appl. 14 (2015), 1550103; arXiv:1312.4685. https://arxiv.org/abs/1312.4685
