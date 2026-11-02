# Involution spectra and exact liftability in characteristic-two Nottingham jets

## Finding

Let \(q\) be any power of two and let \(N\geq 3\). Define the finite Nottingham jet group
\[
J_N(q)=\left\{f(t)=t+\sum_{j=2}^{N-1}a_jt^j\pmod {t^N}:a_j\in\mathbb F_q\right\}
\]
under substitution. Its order is \(q^{N-2}\). An element is *involutive* if its square under substitution is the identity, including the identity itself. A jet is *liftable* if it is the reduction of some power series \(F(t)\in t+t^2\mathbb F_q[[t]]\) satisfying \(F\circ F=t\). (The identity jet is liftable, even by nonidentity involutions of sufficiently large depth.) For nonidentity \(f\), its depth \(d\) is the unique integer \(1\leq d\leq N-2\) with \(a_2=\cdots=a_d=0\) and \(a_{d+1}\ne0\).

**Depth spectra.** The number \(I_{N,d}(q)\) of involutive jets of depth \(d\) is
\[
I_{N,d}(q)=\begin{cases}
(q-1)q^{N-d-2-\max\{0,\lfloor(N-1)/2\rfloor-d\}},&d\text{ odd},\\
(q-1)q^{N-d-2},&d\text{ even and }2d+1\geq N,\\
0,&d\text{ even and }2d+1<N.
\end{cases}
\]
The number of liftable jets in this depth stratum is
\[
L_{N,d}(q)=\begin{cases}
(q-1)q^{N-2-\lfloor(N+d-1)/2\rfloor},&d\text{ odd},\\
0,&d\text{ even}.
\end{cases}
\]

**Total spectra.** Write \(I_N(q)=1+\sum_{d=1}^{N-2}I_{N,d}(q)\), and \(L_N(q)=1+\sum_{d=1}^{N-2}L_{N,d}(q)\). Then
\[
\boxed{L_N(q)=q^{\lfloor(N-1)/2\rfloor}}
\]
and the entire involutive-jet count is
\[
\boxed{I_N(q)=\begin{cases}
q^{2k-1}(1+k(q-1)),&N=4k,\ k\geq1,\\
q^{2k-1}(q+k(q-1)),&N=4k+1,\ k\geq1,\\
q^{2k}(1+k(q-1)),&N=4k+2,\ k\geq1,\\
q^{2k}(1+(k+1)(q-1)),&N=4k+3,\ k\geq0.
\end{cases}}
\]
In particular the ratio \(L_N(q)/I_N(q)\) tends to zero at order \(1/N\) for each fixed even prime power \(q\). Thus finite quotient involutions are predominantly *not* shadows of actual order-two elements of the pro-two Nottingham group as the truncation length increases.

**Sharp lifting test.** Let \(f(t)=t+\sum_{j=d+1}^{N-1}a_jt^j\), considered as an ordinary polynomial (with all later coefficients zero). If its depth \(d\) is odd, its jet is liftable if and only if
\[
\boxed{f(f(t))\equiv t\pmod {t^{N+d}}.}
\]
For even depth, no nonidentity jet is liftable. The test is stronger than merely requiring \(f(f(t))\equiv t\pmod {t^N}\).

## Assumptions and scope

The characteristic is precisely two, \(q=2^e\) with \(e\ge1\), and \(N\) is an arbitrary integer at least three. The group operation is truncated power-series substitution, not polynomial multiplication. Counts include the identity unless explicitly depth-stratified. No conjugacy classification of the finite quotient is asserted; all formulas count actual group elements. A lift is an *infinite* formal series, not just an extension to a single larger finite quotient. These results concern one involution at a time, not arbitrary commuting tuples.

## Proof

Write an arbitrary nonidentity formal substitution as
\[
f(t)=t+u(t),\qquad u(t)=a t^{d+1}+\sum_{j\ge d+2}a_jt^j,\qquad a\ne0.
\]
All arguments below work over an arbitrary field of characteristic two; finiteness is used only when counting.

**1. The parity lemma.** Let \(h=f\circ f\). The first possible nonidentity term of \(h\) occurs strictly later than the first nonidentity term of \(f\). Suppose \(h(t)=t+b t^{r+1}+O(t^{r+2})\), \(b\ne0\). Since \(h\) commutes with \(f\), comparing the leading nonzero coefficient in \(f\circ h-h\circ f\) gives
\[
(r-d)ab=0.
\]
Indeed, the first potentially nonzero commutator term occurs in degree \(d+r+1\), with coefficient \((r-d)ab\) up to sign; all lower terms cancel. Thus \(r\equiv d\pmod2\). If \(d\) is odd, then \(r\) is odd, and the first nonzero term of \(f\circ f-t\), if any, has an **even** exponent. It follows that, for odd \(d\), the congruence \(f\circ f\equiv t\pmod {t^M}\) is equivalent to the vanishing of the coefficients with even exponents less than \(M\). This equivalence is valid for every finite \(M\), by applying the parity lemma to the first hypothetical nonzero coefficient.

**2. Triangular equations in odd depth.** Expand
\[
f(f(t))-t=u(t)+u(t+u(t))
=\sum_{j\ge d+1}a_j\bigl((t+u(t))^j+t^j\bigr).
\]
In characteristic two, the first displayed nontrivial term can occur in degree \(2d+1\), and its coefficient is \((d+1)a^2\). When \(d\) is odd this coefficient is zero. For each **even** exponent \(n\ge2d+2\), the coefficient in degree \(n\) is
\[
[t^n](f\circ f-t)=a\,a_{n-d}+Q_n(a,a_{d+2},\ldots,a_{n-d-1}),
\]
where \(Q_n\) is a polynomial in coefficients of strictly smaller index. To see this, the contribution from the outer term of degree \(n-d\) is \((n-d)a a_{n-d}=a a_{n-d}\); a possible contribution from the leading outer term of degree \(d+1\) is zero because \(d+1\) is even; all terms containing two or more nontrivial insertions of the coefficient \(a_{n-d}\) have degree larger than \(n\). Terms with outer exponent greater than \(n-d\) likewise cannot contribute. Therefore the equation in even degree \(n\) uniquely determines \(a_{n-d}\), once the earlier coefficients are fixed. These are distinct coefficient positions as \(n\) increases.

For a finite jet of odd depth \(d\), there are \(N-d-2\) coefficients following the nonzero leading coefficient \(a\). Involutivity modulo \(t^N\) imposes precisely one independent equation for each even integer
\[
2d+2\le n\le N-1.
\]
Their number is \(\max\{0,\lfloor(N-1)/2\rfloor-d\}\). The parity lemma shows there are **no further odd-degree conditions**. There are \(q-1\) choices for \(a\), so the odd-depth formula for \(I_{N,d}(q)\) follows.

**3. Even depth.** For even \(d\), the coefficient of \(t^{2d+1}\) in \(f\circ f-t\) is \(a^2\ne0\). Hence the jet cannot be involutive if \(2d+1<N\). If \(2d+1\ge N\), no nonidentity term can occur below degree \(N\), and every choice of the later \(N-d-2\) coefficients works. This proves the even-depth formula. The same leading obstruction proves that no even-depth jet can lift to a genuine formal involution.

**4. Exact infinite liftability.** Fix odd depth \(d\) and an \(N\)-jet. If it has a full involution lift, changing coefficients of degrees at least \(N\) cannot affect its composition square in degrees below \(N+d\): the cancellation in \(u(t)+u(t+u(t))\) means any changed coefficient of degree \(j\) first contributes in degree at least \(j+d\). Thus the displayed congruence modulo \(t^{N+d}\) is necessary for the polynomial representative.

Conversely, suppose the polynomial representative satisfies that congruence. Starting with even degree \(n\ge N+d\), determine the as-yet-unspecified coefficient \(a_{n-d}\) by the triangular equation in Step 2; set any other new coefficients arbitrarily (for example, to zero). This recursion defines a formal series whose composition square has every even coefficient equal to zero. By Step 1 its entire composition square equals \(t\). The criterion is therefore necessary and sufficient. Among the original finite-jet coefficients, the strengthened congruence fixes precisely \(\lfloor(N+d-1)/2\rfloor-d\) positions. This gives the formula for \(L_{N,d}(q)\).

**5. Summing the spectra.** Sum the liftable odd-depth fibers by writing \(d=2s+1\). Their exponents form a descending consecutive sequence; the geometric sum telescopes to
\[
1+\sum_{\substack{1\le d\le N-2\\d\text{ odd}}}L_{N,d}(q)
=q^{\lfloor(N-1)/2\rfloor}.
\]
For the full involution total, the low odd depths contribute a common weight \((q-1)q^{\lfloor(N-2)/2\rfloor}\), while all sufficiently high depths are unconstrained and contribute one terminal geometric sum. Separating \(N\) into its four residue classes modulo four gives the four displayed formulas. For fixed \(q\), their multiplicative factors grow linearly in \(N\), whereas the liftable total is a single power of \(q\) of the same half-length scale; this gives \(L_N(q)/I_N(q)=\Theta(1/N)\).

## Verification

A standalone checker `nottingham_checker.py` enumerates every substitution over \(\mathbb F_2\) for lengths \(3\) through \(13\), over \(\mathbb F_4\) for lengths \(3\) through \(8\), and over \(\mathbb F_8\) for lengths \(3\) through \(6\). Its arithmetic constructs extension fields using the irreducible polynomials \(z^2+z+1\) and \(z^3+z+1\), not integer arithmetic modulo the field size. It directly composes each candidate jet, tests involutivity, and independently tests the finite polynomial lifting criterion at precision \(N+d\). The checks match every depth-fiber formula and both totals, including the identity.

For example, over \(\mathbb F_2\), the ordered pairs (all involutive jets, liftable jets) are \((4,2)\) at \(N=4\), \((24,8)\) at \(N=8\), and \((128,32)\) at \(N=12\). Over \(\mathbb F_4\), they are \((16,4)\) at \(N=4\) and \((448,64)\) at \(N=8\). The machine-output record is `nottingham_verification.txt` and ends with `NOTTINGHAM_JET_INVOLUTION_DEPTH_AND_LIFTABILITY_OK`. The infinitely many remaining cases are established by the proof rather than finite enumeration.

## Relationship to prior work

P. P. Pálfy, *The number of conjugacy classes in some quotients of the Nottingham group* (1998, first verified online 2009), calculates the **total number of conjugacy classes** in specific finite quotients over prime fields through a bounded level. Its basic leading-term commutator formula is an established ingredient of Step 1 above. The inspected article's class-number theorem and centralizer analysis do not state the present all-level order-two element count or exact liftability fibers.

J. Lubin, *Torsion in the Nottingham group* (first online 2011), explains Klopsch's classification of **genuine** finite-order power series by depth and leading coefficient and develops higher-ramification descriptions. This establishes the importance of distinguishing actual pro-group torsion from torsion that appears only in a truncated quotient. The inspected Sections 1 and 4 classify infinite torsion up to conjugacy, not the cardinalities of its images in each finite jet group, nor the full involution spectrum in each finite quotient.

P. Hegedűs, *The Nottingham Group for p = 2* (2001), concerns the characteristic-two Nottingham group, notably its derived series and hereditary just-infiniteness. The accessible abstract does not resolve the present counting claims; the unavailable full text is a specific residual overlap risk. An indexed result on truncated Nottingham braces in odd characteristic concerns a different algebraic structure and does not imply the characteristic-two substitution-square formulas here.

## Limitations

The formulas are restricted to characteristic two, and no finite-quotient conjugacy-class or orbit-size classification is claimed. The distinction between a formal involution and a finite-order jet matters: most finite-level involutions are not liftable. Historical priority has not been conclusively established, especially against uninspected older sources on the characteristic-two Nottingham group. The correctness proof is independent of the finite-field experiments, and no independent mathematical audit has been performed.

## References

1. P. P. Pálfy, *The number of conjugacy classes in some quotients of the Nottingham group*, Proceedings of the Edinburgh Mathematical Society 41 (1998), 369–384. DOI: 10.1017/S0013091500019714. Verified online publication: 2009-01-20. Full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8BFAF4025F094C0D082FDF12F0B7BDF3/S0013091500019714a.pdf/number_of_conjugacy_classes_in_some_quotients_of_the_nottingham_group.pdf
2. J. Lubin, *Torsion in the Nottingham group*, Bulletin of the London Mathematical Society 43 (2011), 547–560. DOI: 10.1112/blms/bdq120. Online publication: 2011-01-28. Author's manuscript: https://www.math.brown.edu/~lubinj/TorsInNott.pdf
3. P. Hegedűs, *The Nottingham Group for p = 2*, Journal of Algebra 246 (2001), 55–69. DOI: 10.1006/jabr.2001.8948. The complete article was unavailable for inspection.
