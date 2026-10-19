# The complete antidictionary of generalized Cantor words

## Finding

For every integer \(q\ge 3\), let \(C_q\) be the one-sided infinite fixed point beginning in \(1\) of the uniform substitution
\[
\mu_q(1)=1\,0^{q-2}1,\qquad \mu_q(0)=0^q.
\]
Write \(W_j=\mu_q^j(1)\), \(L_j=(q-2)q^j\), for integers \(j\ge0\). The *minimal absent factors* of \(C_q\)—the finite binary words not occurring contiguously in \(C_q\) whose every proper contiguous factor does occur—are **exactly** the following three disjoint families:
\[
\boxed{\begin{aligned}
\mathcal M(C_q)={}&\{1\,0^t1:t\ge0,\ t\notin\{L_j:j\ge0\}\}\\
&\cup\{0^{L_j+1}W_j0^{L_j+1}:j\ge0\}\\
&\cup\{1\,0^{L_j}W_j0^{L_j}1:j\ge0\}.
\end{aligned}}
\]
Thus for every \(n\ge2\), the number \(m_q(n)\) of minimal absent factors of length \(n\) is
\[
\boxed{m_q(n)=1-\mathbf 1_{\{n-2=L_j\text{ for some }j\}}+2\mathbf 1_{\{n-2=(2q-3)q^j\text{ for some }j\}}.}
\]
There are no minimal absent factors of length \(0\) or \(1\). In particular, the exact generating series, as a formal power series, is
\[
\boxed{\sum_{n\ge0}m_q(n)z^n=\frac{z^2}{1-z}-\sum_{j\ge0}z^{(q-2)q^j+2}+2\sum_{j\ge0}z^{(2q-3)q^j+2}.}
\]
The cumulative count through length \(N\ge2\) is
\[
N-1-\#\{j\ge0:L_j+2\le N\}+2\#\{j\ge0:(2q-3)q^j+2\le N\}=N+\log_q N+O_q(1).
\]
The exceptional lengths have two minimal absent factors when \(q=3\), and three when \(q\ge4\). For \(q=3\), every length at least four supports a minimal absent factor, while length three does not. For \(q\ge4\), the missing lengths are exactly \(L_j+2\).

## Assumptions and scope

The alphabet is \(\{0,1\}\) and *factor* means contiguous substring, never scattered subsequence. Both the generating word and the forbidden-factor language are infinite. Exponents in \(0^t\) denote a run of \(t\) zeros; \(W_0=1\). The classification ranges over all integers \(q\ge3\), \(j\ge0\), and \(t\ge0\). A proper factor of a word includes its length-one-deleted prefix and suffix. Since the factor language is factorial, a word is minimally absent if and only if it is absent but both length-one-deleted prefix and suffix occur.

## Proof

**1. Ruler gaps.** The substitution gives \(W_{j+1}=W_j0^{L_j}W_j\), so \(W_j\) is a palindrome with \(2^j\) occurrences of \(1\). Number the gaps between consecutive ones of \(C_q\) starting at \(i=1\). Their zero-run lengths are exactly
\[
g_i=L_{\nu_2(i)}=(q-2)q^{\nu_2(i)}\quad(i\ge1),
\]
where \(\nu_2(i)\) is the exponent of \(2\) dividing \(i\). This follows inductively: the gap at the midpoint of \(W_{j+1}\) has length \(L_j\), while the gaps in both half-blocks retain their old values. Consequently, the internal zero-run lengths in \(W_j\) are \(L_{\nu_2(i)}\) for \(1\le i<2^j\). Every finite admissible pattern of these ruler gaps occurs arbitrarily far to the right, by their periodic congruence conditions below.

**2. Exact occurrence test.** Consider any finite word containing \(r\ge1\) ones and write it uniquely as
\[
u=0^a1\,0^{t_1}1\cdots0^{t_{r-1}}1\,0^b
\]
with nonnegative integral runs. If some internal \(t_i\) is not among the \(L_j\), then \(u\) cannot occur. Otherwise put \(t_i=L_{e_i}\) and
\[
\kappa(s)=\min\{e\ge0:L_e\ge s\},\qquad s\ge0.
\]
An occurrence is equivalent to an integer \(x\ge1\) satisfying
\[
\nu_2(x)\ge\kappa(a),\qquad
\nu_2(x+i)=e_i\quad(1\le i<r),\qquad
\nu_2(x+r)\ge\kappa(b).
\tag{1}
\]
Here \(x\) is the gap index immediately preceding the first displayed one. An occurrence at the initial one with \(a=0\) also has a later counterpart: choose a sufficiently large multiple of a power of two to reproduce the finitely many subsequent gap valuations. Thus the use of \(x\ge1\) loses no factors.

For each positive index \(y\), the assertion \(\nu_2(y)=e\) means \(y\equiv2^e\pmod{2^{e+1}}\), while \(\nu_2(y)\ge e\) means \(y\equiv0\pmod{2^e}\). Hence (1) is a finite set of residue conditions on \(x\) whose moduli are powers of two. **It is solvable if and only if every pair of those conditions is compatible.** Indeed, the condition with largest modulus, if pairwise compatible, satisfies every other condition. Any resulting residue class has arbitrarily large positive representatives. This is a complete, independently usable occurrence criterion.

**3. Endpoint reduction.** Suppose \(u\) is minimally absent and all internal gaps are allowed. Some two congruence conditions in (1) conflict. Since deleting either end letter makes the word occur, each conflict must involve both of the two endpoint constraints affected by the deletions. Removing an initial zero can only lower \(\kappa(a)\), whereas removing an initial one replaces the first exact-gap condition by a lower-bound condition. The right endpoint behaves symmetrically. Therefore, the conflicting pair has one of four types: boundary–boundary, exact–exact, or either of the two boundary–exact orientations.

**4. Boundary–boundary.** Here \(a,b>0\), and deleting the end zeros must strictly lower their thresholds. Thus \(a=L_{k-1}+1\), \(b=L_{\ell-1}+1\) for some \(k,\ell\ge1\). The two original conditions require \(2^{\min(k,\ell)}\mid r\), which fails. Deleting the first or last zero requires respectively \(2^{\min(k-1,\ell)}\mid r\) or \(2^{\min(k,\ell-1)}\mid r\). Both are possible only when \(k=\ell\) and
\[
\nu_2(r)=k-1.
\]
Put \(j=k-1\). If \(r>2^j\), then \(r\ge3\cdot2^j\). Consider the internal gap index \(t=r-2^j\), where \(1\le t<r\). A realization of the prefix after deleting the final zero has \(2^{j+1}\mid x\), hence \(\nu_2(x+t)\ge j+1\). A realization of the suffix after deleting the initial zero has \(2^{j+1}\mid x+r\), hence \(\nu_2(x+t)=j\). This contradicts the fixed internal gap. Consequently \(r=2^j\), the internal gaps must be those of \(W_j\), and
\[
u=0^{L_j+1}W_j0^{L_j+1}.
\]

**5. Exact–exact.** Here \(a=b=0\), with at least two internal gaps, and the first and last have exponents \(e,f\) at gap indices distance \(d\ge1\). Deleting the last one makes the last gap a lower bound \(\nu_2\ge f\); deleting the first one similarly makes the first gap a lower bound \(\nu_2\ge e\). If \(e<f\), the first of these relaxed conditions already forces \(\nu_2(d)=e\), which also makes the two original exact congruences compatible; similarly \(e>f\) is excluded by the other deletion. Thus \(e=f=j\). Exact incompatibility, together with either relaxed compatibility, implies \(\nu_2(d)=j\): the distance is an odd multiple of \(2^j\). If \(d>2^j\), consider the internal gap at distance \(2^j\) from the first. The realizable prefix, starting with exact exponent \(j\), forces this gap to have exponent at least \(j+1\). The realizable suffix, whose first gap exponent is at least \(j+1\) and whose last is exactly \(j\), forces that same internal gap to have exponent exactly \(j\). Contradiction. So \(d=2^j\). The intervening exponents are \(\nu_2(1),\ldots,\nu_2(2^j-1)\), and
\[
u=1\,0^{L_j}W_j0^{L_j}1.
\]

**6. Mixed endpoints cannot be minimal.** By reversal, it suffices to treat a left boundary and a right exact gap, whose indices are distance \(d\ge1\) apart. Let the left threshold be \(k\ge1\), and the final exact exponent be \(f\). A realizable prefix has left valuation at least \(k\) and final valuation at least \(f\); a realizable suffix has left valuation at least \(k-1\) and final valuation exactly \(f\). Incompatibility of the two original endpoint conditions forces
\[
f=k-1,\qquad 2^k\mid d.
\]
To verify this assertion: the prefix gives \(\nu_2(d)\ge f\); if \(f\ge k\) the original pair is compatible, and if \(f<k-1\) then the relaxed left constraint still cannot yield exact exponent \(f\) without making the original pair compatible. Thus \(f=k-1\), and exact incompatibility forces \(2^k\mid d\). At internal position \(t=2^{k-1}<d\), the prefix forces valuation exactly \(k-1\), whereas the suffix (which must start with valuation exactly \(k-1\)) forces valuation at least \(k\). Contradiction.

**7. Verification of both required proper factors.** A missing gap \(1\,0^t1\), with \(t\notin\{L_j\}\), is absent; both its length-one-deleted prefix and suffix occur because the gap sequence has arbitrarily long zero runs. Each displayed boundary–boundary word is absent because two gap indices distance \(2^j\) cannot both be multiples of \(2^{j+1}\). Removing either extreme zero changes one required run length from \(L_j+1\) to \(L_j\), so one can take the adjacent gap valuations to be \((\ge j+1,j)\) or \((j,\ge j+1)\); all interior gaps match \(W_j\). Each displayed exact–exact word is absent because two gap indices distance \(2^j\) cannot both have valuation \(j\); removing either extreme one permits valuations \((j,\ge j+1)\) or \((\ge j+1,j)\) instead, again with the interior gaps of \(W_j\). Therefore both length-one-deleted factors occur for each candidate. Parts 3–6 exclude all other possibilities.

**8. Counting.** The families are disjoint: the first begins and ends with ones and has exactly two ones, the second begins and ends with zeros, and the third begins and ends with ones and has at least three ones. Both exceptional words indexed by \(j\) have length
\[
q^j+2(L_j+1)=(2q-3)q^j+2.
\]
The first family contributes one word at length \(n\ge2\) unless \(n-2=L_j\). This proves the length formula and generating function. Since both lacunary index sets have \(\log_q N+O_q(1)\) elements through \(N\), the cumulative asymptotic follows. For \(q=3\), \((2q-3)q^j=L_{j+1}\); for \(q\ge4\), \((2q-3)/(q-2)\) is not an integral power of \(q\), so the exceptional sets are disjoint. This proves the stated special cases.

## Verification

The self-contained `verify_cantor.py` provides two logically separate finite checks: an infinite-word factor-membership test directly from power-of-two congruences, and independent finite prefixes generated both by substitution and the base-\(q\) digit characterization. It exhausts every binary word through length \(14\) for \(q=3,\ldots,8\); separately it compares the predicted minimal absent factors with prefix-derived factor sets at \(365\) parameter–length pairs and verifies \(110\) larger-scale forbidden words and their proper prefixes/suffixes by exact congruences. It does not replace the proof at unbounded lengths. Run with `python3 verify_cantor.py` using Python 3 standard library.

## Relationship to prior work

The generalized Cantor substitutions and their right-special-factor and ordinary factor-complexity descriptions appear in Lü, Chen, Guo and Wen, *On the permutation complexity of the Cantor-like sequences* (2016). The present classification does not change those established definitions, and earlier explicit right-special results provide potentially useful ingredients for an alternative derivation. Barton et al. (2014) and Crochemore et al. (2015) established general efficient algorithms and the formalism for minimal absent words, rather than an explicit infinite antidictionary for this substitution family. The claimed contribution here is precisely the complete three-family forbidden-factor classification, the lacunary length spectrum and the closed generating series.

## Limitations

This is an exact theorem about *contiguous* factors of the one-sided infinite fixed point, not about absent scattered subsequences and not the finite-prefix antidictionary. No claim is made for the substitution with \(q=2\), nor for arbitrary substitutions. The finite checks are corroboration and do not establish the all-rank statements independently. The accessible publisher-indexed material for the most closely related Cantor-like factor-complexity paper did not provide a retrievable complete publisher document, leaving a literature overlap risk: its right-special formulas might support a shorter deduction not recognized in the literature comparison. No independent external audit has been performed.

## References

1. C. Barton, A. Heliou, L. Mouchard and S. P. Pissis, *Linear-time Computation of Minimal Absent Words Using Suffix Array*, first posted June 24, 2014, arXiv:1406.6341.
2. M. Crochemore, G. Fici, R. Mercaş and S. P. Pissis, *Linear-Time Sequence Comparison Using Minimal Absent Words & Applications*, first posted June 16, 2015, arXiv:1506.04917.
3. X.-T. Lü, J. Chen, Y.-J. Guo and Z. Wen, *On the permutation complexity of the Cantor-like sequences*, Theoretical Computer Science 616 (2016), 100–110, doi:10.1016/j.tcs.2015.12.022.
