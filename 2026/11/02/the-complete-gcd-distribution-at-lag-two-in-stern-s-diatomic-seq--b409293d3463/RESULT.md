# The complete gcd distribution at lag two in Stern's diatomic sequence

## Finding
Let the Stern sequence be \(s(0)=0\), \(s(1)=1\), \(s(2n)=s(n)\), and \(s(2n+1)=s(n)+s(n+1)\) for integers \(n\ge1\). For every \(n\ge0\), put \(G(n)=\gcd(s(n),s(n+2))\), taking the nonnegative greatest common divisor. For every positive integer \(d\), the natural density \(\delta_d\) of indices for which \(d\mid G(n)\) exists and is

\[
\delta_d=\begin{cases}
0,&2\mid d,\\[2pt]
\displaystyle\frac{2^{(d-1)/2}}{2^d-1}\prod_{p^a\parallel d}\frac1{p^{a-1}(p+1)},&d\text{ odd}.
\end{cases}
\]

The empty product is \(1\), so \(\delta_1=1\). All values \(G(n)\) are odd. For each odd positive integer \(h\), the exact-value natural density \(\pi(h)\) exists, is strictly positive, and is given by the absolutely convergent series

\[
\pi(h)=\sum_{\substack{j\ge1\\j\text{ odd}}}\mu(j)\delta_{hj};
\qquad \pi(h)=0\quad(h\text{ even}).
\]

Here \(\mu\) is the ordinary Möbius function. These numbers form a probability distribution: \(\sum_{h\ge1}\pi(h)=1\). In particular, \(\delta_3=1/14\), \(\delta_5=2/93\), \(\delta_7=1/127\), and \(\pi(1)\approx0.897340422146\).

## Assumptions and scope
The asymptotics are natural densities along all initial intervals \(\{0,\ldots,N-1\}\) as \(N\to\infty\), with each fixed \(d\) or \(h\). The theorem does not assert an effective error term uniform in growing \(d\) or \(h\). We invoke the established modular equidistribution theorem for primitive adjacent Stern pairs, rather than independently reproving its spectral estimates.

## Proof
**1. Exact lag-two identity.** Write any \(n\ge0\) uniquely as
\[
n=2^{k+1}u+2^k-1\qquad(k,u\ge0),
\]
where \(k\) is the length of the trailing run of binary ones. Put \(a=s(u)\), \(b=s(u+1)\). For \(k\ge1\), the digit-splitting formula
\[
s(2^{r}m+t)=s(2^{r}-t)s(m)+s(t)s(m+1),\qquad0\le t\le2^r,
\]
with \(r=k+1\), together with \(s(2^k-1)=k\) and \(s(2^k+1)=k+1\), gives
\[
s(n)=(k+1)a+kb,\qquad s(n+2)=ka+(k+1)b.
\]
The same formulas hold for \(k=0\) by the even-index recurrence. Since \(\gcd(a,b)=1\), subtraction and Euclid's algorithm yield
\[
\boxed{G(n)=\gcd(2k+1,a-b)}.
\]
Indeed the two displayed Stern values differ by \(a-b\), while the second is \((2k+1)b+k(a-b)\). Thus \(G(n)\) is always odd and at most \(2k+1\).

**2. Density of a fixed divisor.** For odd \(d\ge1\), the identity implies
\[
d\mid G(n)\quad\Longleftrightarrow\quad d\mid(2k+1)\text{ and }s(u)\equiv s(u+1)\pmod d.
\]
For each fixed \(k\), the indicated set of indices \(n\) has density \(2^{-(k+1)}q_d\), where \(q_d\) is the natural density of \(u\) satisfying the displayed congruence. Reznick's modular equidistribution theorem says that \((s(u),s(u+1))\bmod d\) is uniformly distributed on
\[
\mathcal P_d=\{(a,b)\bmod d:\gcd(a,b,d)=1\}.
\]
For any prime power \(p^a\parallel d\), there are \(p^{2a}-p^{2a-2}\) primitive pairs and \(p^a-p^{a-1}\) primitive diagonal pairs \(a=b\). The Chinese remainder theorem therefore gives
\[
q_d=\prod_{p^a\parallel d}\frac{p^a-p^{a-1}}{p^{2a}-p^{2a-2}}=\prod_{p^a\parallel d}\frac{1}{p^{a-1}(p+1)}.
\]
For \(d=1\) both products are empty and \(q_1=1\).

The allowed run lengths are exactly \(k=(d-1)/2+jd\) for \(j\ge0\). Summing their index weights gives
\[
\sum_{j\ge0}2^{-((d-1)/2+jd+1)}
=\frac{2^{(d-1)/2}}{2^d-1}.
\]
Passing from the density for any finite set of run lengths to the infinite union is valid: indices with \(k\ge K\) have upper density \(2^{-K}\), being exactly one residue class modulo \(2^K\). This proves the displayed \(\delta_d\). Even \(d\) cannot divide any odd \(G(n)\).

**3. Exact-value distribution and support.** The deterministic bound \(G(n)\le2k+1\) gives, for every \(H\ge1\),
\[
\limsup_{N\to\infty}\frac1N\#\{0\le n<N:G(n)\ge H\}
\le2^{-\lceil(H-1)/2\rceil}.
\]
For any fixed odd \(h\), restricting to finitely many run lengths gives a finite union of modular conditions, each of which has a natural density by the same primitive-pair equidistribution. The geometric tail in \(k\) makes these truncated densities converge to \(\pi(h)\); the displayed tail bound also proves total mass \(1\).

For each \(n\), the finite divisor inversion identity is
\[
\mathbf1_{\{G(n)=h\}}=
\sum_{\substack{j\ge1\\hj\mid G(n)}}\mu(j),\qquad(h\text{ odd}).
\]
To pass to natural densities, the total contribution from omitted \(j>J\) is bounded in magnitude by \(G(n)\mathbf1_{\{G(n)\ge h(J+1)\}}\), using the trivial bound on its number of divisors. Since \(G(n)\le2k+1\), the upper mean of this expression is bounded by a geometric tail \(\sum_{k\ge\lceil(h(J+1)-1)/2\rceil}(2k+1)2^{-(k+1)}\), which tends to zero. This justifies inversion. Absolute convergence also follows from \(\delta_d\le2^{-(d-1)/2}\) for odd \(d\ge1\).

Finally, for each odd \(h\), choose \(k=(h-1)/2\). The event \(s(u)\equiv s(u+1)\pmod h\) then forces \(G(n)=h\), since \(G(n)\) divides \(2k+1=h\). Consequently
\[
\pi(h)\ge2^{-(h+1)/2}\prod_{p^a\parallel h}\frac1{p^{a-1}(p+1)}>0.
\]
This proves the exact support and completes the theorem.

## Verification
The accompanying `verify_stern.py` checks the lag-two identity directly for all \(0\le n<262144\), confirms that all observed gcd values are odd, and directly enumerates the primitive-pair ratios for \(1\le d<100\). It compares observed divisor frequencies against exact rational formulas for \(1\le d<201\) (diagnostic comparisons only). These finite tests confirm arithmetic implementation, not the existence of infinite densities.

For \(\pi(1)\), summing the Möbius series over odd \(j\le99\) gives the displayed numerical value. The omitted absolute tail is bounded by \(2^{-49}\), using \(\delta_j\le2^{-(j-1)/2}\).

## Relationship to prior work
Bettin, Drappeau, and Spiegelhofer studied the statistical distribution of the individual Stern values in 2017 and established a logarithmic central limit theorem. Reznick (2006) proved the essential modular equidistribution of adjacent primitive Stern pairs (Theorem 4.7) and the binary digit-splitting identity (Corollary 2.4). Those strong antecedents are essential to this proof and are not claimed as new. The present conclusion concerns the *gcd of two nonadjacent terms*, a mixed trailing-run and modular statistic; the exact divisor-density product and full Möbius-inverted gcd distribution are not stated in the inspected antecedents. This is a derived mathematical result, not an independent reproof of the modular equidistribution theorem.

## Limitations
Priority is assessed against the inspected primary sources and targeted record/database searches, not guaranteed against inaccessible or unindexed literature. In particular, the complete law may be implicit in a broader treatment of shifted Stern pair statistics not found in the inspected record. No effective error uniform in variable modulus, multi-lag joint law, or higher-offset gcd classification is asserted.

## References
1. S. Bettin, S. Drappeau, and L. Spiegelhofer, *Statistical distribution of the Stern sequence*, arXiv:1704.05253v1, first posted 2017-04-18. https://arxiv.org/abs/1704.05253
2. B. Reznick, *Regularity properties of the Stern enumeration of the rationals*, arXiv:math/0610601, first posted 2006-10-19; especially Corollary 2.4 and Theorem 4.7. https://arxiv.org/abs/math/0610601
3. K. Dilcher and L. Ericksen, *Polynomials Whose Coefficients Are Stern Numbers*, Journal of Integer Sequences 24 (2021), article 21.10.3. https://cs.uwaterloo.ca/journals/JIS/VOL24/Dilcher/dilcher51.html
4. OEIS A002487, *Stern's diatomic sequence*. https://oeis.org/A002487
