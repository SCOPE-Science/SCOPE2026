# A midpoint-height peak reversal and cube-root optimum in uniform Dyck excursions

## Finding

Let \(n\ge2\). Sample uniformly from all Dyck paths of \(2n\) up/down steps, and let \(H\) be the altitude after step \(n\). Let \(P\) be the total number of peaks (adjacent up/down step pairs). For every feasible \(h\in\{0,1,\ldots,n\}\) with \(h\equiv n\pmod2\), write \(\mu_n(h)=\mathbb E[P\mid H=h]\). Then

\[
\mu_n(h)=\frac{(n-h)(n+h+2)}{2n}
 +\left(\frac{h(n+h+2)}{2n(h+1)}\right)^2.
\]

The sequence of these conditional means, ordered by increasing feasible midpoint height in steps of two, has **strictly decreasing consecutive differences** whenever there are at least three admissible heights. It is therefore unimodal, with at most two tied adjacent maximizers. Its initial difference has two exact parity-dependent phases:

\[
\mu_n(2)-\mu_n(0)=\frac{n^2-28n+16}{9n^2}
\quad(n\text{ even}),
\]
\[
\mu_n(3)-\mu_n(1)=\frac{(n-63)(5n-3)}{64n^2}
\quad(n\text{ odd}).
\]

Thus, for even \(2\le n\le26\), the means decrease strictly with midpoint height, while for every even \(n\ge28\) they first increase and subsequently decrease. For odd \(3\le n\le61\) they decrease strictly; at \(n=63\) the first two heights tie and all further means decrease; for every odd \(n\ge65\) they first increase and subsequently decrease. These are exhaustive finite-size phases.

If \(h_n\) is any maximizing feasible height, then

\[
h_n\sim (n/2)^{1/3},\qquad
\max_h\mu_n(h)=\frac{n+2}{2}+\frac14
-\frac{3}{2^{5/3}}n^{-1/3}+o(n^{-1/3}).
\]

In particular, a moderately *higher* midpoint eventually increases expected peak count, even though an excessively high midpoint forces the path toward one peak. The maximizer occupies the cube-root scale, not the diffusive square-root height scale typical of an unconditioned excursion.

## Assumptions and scope

A Dyck path is a sequence \(s_1,\ldots,s_{2n}\) with each \(s_i\in\{+1,-1\}\), nonnegative partial sums, and final sum zero. A peak is an index \(i\in\{1,\ldots,2n-1\}\) with \((s_i,s_{i+1})=(+1,-1)\). A feasible midpoint height \(h\) has the same parity as \(n\), lies between zero and \(n\), and has positive conditional probability. All statements are exact for the uniform distribution on Dyck paths; no continuum excursion or Bernoulli independence is assumed after conditioning. For \(n=1\) there is only one feasible height and one peak, a trivial omitted boundary.

## Proof

**Step 1: split at the midpoint.** Conditional on \(H=h\), the first \(n\) steps and the reversal-with-up/down-interchange of the last \(n\) steps are independent, uniformly distributed nonnegative paths of length \(n\) from altitude zero to \(h\). Call these ballot prefixes \(L\) and \(R\). Reversal with step interchange preserves the pattern up/down, hence preserves the number of internal peaks. If \(Q(L)\) denotes the number of peaks within a prefix, and \(I(L)\) indicates that its final step is up, then exactly

\[
P=Q(L)+Q(R)+I(L)I(R).
\]

**Step 2: count ballot-prefix peaks.** Put \(u=(n+h)/2\) and \(d=(n-h)/2\). The number of ballot prefixes is

\[
B(n,h)=\frac{h+1}{u+1}\binom{n}{d}.
\]

For an algebraic derivation of their mean peak count, let \(C(t,q)\) enumerate ordinary Dyck paths by semilength and peaks, with \(C(0,q)=1\). The first-return decomposition gives \(C=1+tC(C+q-1)\). A ballot prefix ending at height \(h\) decomposes uniquely into \(h+1\) Dyck excursions separated by \(h\) unmatched up-steps. The peak statistic is additive across those excursions, so its polynomial enumerator is \([t^d]C(t,q)^{h+1}\). For \(d\ge1\), Lagrange inversion with \(W=C-1=t(1+W)(q+W)\) yields

\[
[t^d]C(t,q)^{h+1}=\frac{h+1}{d}[w^{d-1}](1+w)^{h+d}(q+w)^d.
\]

At \(q=1\), this is \(B(n,h)\). Differentiating at \(q=1\), the total number of peaks over ballot prefixes is

\[
(h+1)\binom{n-1}{d-1},
\]

and therefore \(\mathbb E[Q(L)]=d(u+1)/n=(n-h)(n+h+2)/(4n)\). This also holds at \(d=0\), when the prefix is all up-steps and has no peak.

A ballot prefix ends with up if and only if its first \(n-1\) steps are a ballot prefix ending at height \(h-1\). By the ballot formula, including the boundary \(h=0\),

\[
\Pr(I(L)=1)=\frac{B(n-1,h-1)}{B(n,h)}
=\frac{h(u+1)}{n(h+1)}.
\]

Substituting the two independent half-prefix means and their boundary probability into the identity from Step 1 proves the formula for \(\mu_n(h)\).

**Step 3: strict discrete concavity.** Extend the rational formula to real \(x\in[0,n]\) and denote it by \(F_n(x)\). Direct differentiation and setting \(y=x+1\) give

\[
F_n''(x)=\frac{(1-2n)y^4-2n(n+1)y+3(n+1)^2}
{2n^2y^4}.
\]

For \(n\ge3\) and \(x\ge1\), one has \(y\ge2\) and \(3(n+1)-2ny\le3-n\le0\), so the numerator equals \((1-2n)y^4+(n+1)[3(n+1)-2ny]<0\). It follows that consecutive step-two differences decrease strictly for odd heights, and for even heights starting at \(h=2\). The only remaining even-grid boundary is obtained by direct substitution:

\[
F_n(4)-2F_n(2)+F_n(0)
=-\frac{2(7n^2+434n-248)}{225n^2}<0
\quad(n\ge4).
\]

Together these prove strict discrete concavity on the entire feasible grid. Substitution at the first two heights gives the two displayed initial differences. The even quadratic has its larger zero at \(14+6\sqrt5\), strictly between 26 and 28; the odd difference vanishes exactly at \(n=63\). The terminal value is \(\mu_n(n)=1\), proving the stated increase/then-decrease classifications.

**Step 4: asymptotic maximizing height.** For \(h\to\infty\) with \(h=o(n)\), uniformly on growing ranges with \(h\) comparable to \(n^{1/3}\), the exact expression gives

\[
\mu_n(h)=\frac{n+2}{2}+\frac14-
\frac{h^2}{2n}-\frac{1}{2h}
+O\!\left(\frac{h}{n}+\frac1{h^2}\right).
\]

Moreover, the exact step-two difference obeys, uniformly for \(h\asymp n^{1/3}\),

\[
\mu_n(h+2)-\mu_n(h)=\frac1{h^2}-\frac{2h}{n}+o(n^{-2/3}).
\]

For fixed positive \(c\), setting \(h\sim c n^{1/3}\) makes the sign of this difference that of \(c^{-2}-2c\). Strict discrete concavity implies every maximizing height is asymptotic to \(2^{-1/3}n^{1/3}\). More explicitly, the difference is positive below any fixed smaller multiple and negative above any fixed larger multiple; the extreme small- and large-height ranges are excluded by the same strict concavity and comparison. Evaluating the preceding uniform expansion at the maximum gives the stated \(3/2^{5/3}\) correction.

## Verification

Run `python3 verify.py` with Python 3 and its standard library. The script independently enumerates all Dyck paths up to semilength 11, independently computes ballot-prefix peak totals by finite-state dynamic programming through length 120, tests every valid closed-form expectation, and checks discrete concavity and exact first-difference phases through semilength 500. It passes 160,183 exact assertions. Enumerations are finite checks supporting the separately supplied proof, not proofs of the unbounded statements. The large-height numerical checks are illustrative only; the cube-root limit is proved analytically in Step 4.

## Relationship to prior work

Classical Catalan/Narayana enumeration gives the unconditional peak distribution; ballot enumeration and Lagrange inversion supply standard proof ingredients. Ding and Du (2011) study peak counts and Narayana numbers; Mortimer and Prellberg (2012, revised 2014) give an equidistribution for peak counts; and Du, Nie and Sun (2014, revised 2015) extend peak enumeration to other paths. Elizalde (2004) counts selected middle peaks and uses the height at the middle in a different permutation-avoidance statistic. These works do not establish in the material inspected the parity-specific reversal of the *conditional total peak mean*, the strictly concave height profile, or its cube-root optimum. The conditional formula is elementary once the classical enumerators are combined; it is not independently asserted to be a new Narayana enumeration.

## Limitations

The theorem concerns conditional expectations, not stochastic dominance of full peak-count distributions. It does not claim a central limit theorem, concentration bound, independence of peaks, or a previously unknown Catalan counting sequence. The older literature may contain implicit bivariate refinements from which the expectation could be recovered; a claim of definitive historical priority is not made. The classification is mathematically proved but has not been independently audited.

## References

1. Y. Ding and R. R. X. Du, *Counting Humps in Motzkin paths*, arXiv:1109.2661v1, first publicly posted 2011-09-13, https://arxiv.org/abs/1109.2661.
2. P. R. G. Mortimer and T. Prellberg, *A Bijection on Bilateral Dyck Paths*, arXiv:1208.3061v1, first posted 2012-08-15, https://arxiv.org/abs/1208.3061.
3. R. R. X. Du, Y. Nie and X. Sun, *Enumerations of humps and peaks in (k,a)-paths and (n,m)-Dyck paths via bijective proofs*, arXiv:1406.2449v1, first posted 2014-06-10, https://arxiv.org/abs/1406.2449.
4. S. Elizalde, *Multiple pattern avoidance with respect to fixed points and excedances*, Electron. J. Combin. 11 (2004), R51, https://math.dartmouth.edu/~sergi/papers/v11i1r51.pdf.
5. T. Mansour, *Counting peaks at height k in a Dyck path*, J. Integer Seq. 5 (2002), https://cs.uwaterloo.ca/journals/JIS/VOL5/Mansour/mansour6.html.
