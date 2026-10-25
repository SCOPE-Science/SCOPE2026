# Exact shifted-flat prime densities and a sharp ternary gap

## Finding
Fix a positive odd integer \(h\). For an even positive integer \(m\), say that \(m\) is *flat* when its odd part is squarefree. Put
\[
B_h(X)=\#\{\text{primes }p:h<p\le X,\ p-h\text{ and }p+h\text{ are flat}\}.
\]
Then the natural relative density among primes exists and is
\[
\lim_{X\to\infty}\frac{B_h(X)}{\pi(X)}
=\Delta(h):=\prod_{\substack{q\ge3\ \mathrm{prime}\\q\nmid h}}
\left(1-\frac{2}{q(q-1)}\right).
\]
Writing
\[
C=\prod_{q\ge3\ \mathrm{prime}}\left(1-\frac{2}{q(q-1)}\right),
\qquad \Delta(h)=C\prod_{q\mid h}\left(1-\frac{2}{q(q-1)}\right)^{-1},
\]
we have \(C>1/2\) and the **uniformly separated sharp density bands**
\[
\begin{cases}
C\le\Delta(h)<2/3,&3\nmid h,\\
3C/2\le\Delta(h)<1,&3\mid h.
\end{cases}
\]
The lower endpoints occur at \(h=1\) and \(h=3\), respectively; the upper endpoints are suprema, approached along products of increasingly many odd primes (excluding \(3\) in the first case). The density depends only on the set of odd prime divisors of \(h\), and \(\Delta(3h)=3\Delta(h)/2\) whenever \(3\nmid h\).

## Assumptions and scope
All shifts \(h\) are fixed positive odd integers; the limit takes \(X\) to infinity with \(h\) fixed. All variable letters \(p,q\) denoting primes are ordinary rational primes, and \(q\ge3\). A number is flat here if it is even and its largest odd divisor is squarefree, matching the shifted-flat terminology for odd-prime inputs. Finitely many primes \(p\le h\), as well as \(p=2\), have no effect on the density. No uniformity in growing \(h\) is asserted.

## Proof
**Local obstruction.** Fix a prime \(q\ge3\). For primes \(p\ne q\), the residue of \(p\) modulo \(q^2\) is invertible. If \(q\mid h\), then \(p-h\equiv p+h\equiv p\not\equiv0\pmod q\), so \(q^2\) divides neither shift. If \(q\nmid h\), the two forbidden residues are \(p\equiv h\pmod{q^2}\) and \(p\equiv-h\pmod{q^2}\). They are distinct (since \(q\nmid2h\)) and both units. Of the \(\varphi(q^2)=q(q-1)\) invertible residues, precisely \(q(q-1)-2\) are allowed.

**Finite sieve.** For \(Y\ge3\), require the absence of odd square divisors \(q^2\mid p\pm h\) for all prime \(q\le Y\). The Chinese remainder theorem supplies exactly the product of the local allowed proportions, and the prime number theorem in fixed reduced arithmetic progressions gives
\[
\#\{p\le X:\text{no forbidden }q^2\text{ for }q\le Y\}
=\bigl(\Delta_Y(h)+o_{Y,h}(1)\bigr)\pi(X),
\]
where \(\Delta_Y(h)=\prod_{3\le q\le Y,\ q\nmid h}(1-2/[q(q-1)])\).

**Large-square tail.** The difference between this count and \(B_h(X)\) is at most the number of primes \(p\le X\) for which \(q^2\mid p-h\) or \(q^2\mid p+h\) for some odd prime \(q>Y\). Ignore the finitely many \(p\le h\). For \(Y<q\le X^{1/4}\), the Brun--Titchmarsh inequality in either reduced class \(p\equiv\pm h\pmod{q^2}\) gives, when \(q\nmid h\),
\[
\pi(X;q^2,\pm h)\le\frac{2X}{\varphi(q^2)\log(X/q^2)}
\le\frac{4X}{q(q-1)\log X}.
\]
If \(q\mid h\), there are at most finitely many exceptional primes, and, for \(q>Y\ge h\), this cannot occur. Summing both signs yields at most
\[
\frac{8X}{\log X}\sum_{q>Y}\frac{1}{q(q-1)}.
\]
For \(q>X^{1/4}\), necessarily \(q\le\sqrt{X+h}\). Each sign has at most \((X+h)/q^2+1\) integer candidates. Summing over all integers in this range, rather than just primes, gives \(O_h(X^{3/4}+X^{1/2})=o(\pi(X))\). Thus the normalized limsup of the tail is at most \(8\sum_{q>Y}1/[q(q-1)]\), which tends to zero as \(Y\to\infty\). This passes the finite-sieve density to the convergent infinite product and proves the formula.

**Sharp gap.** The factors at \(q=3,5,7\) multiply to \(4/7\). For the remaining odd primes, write \(q=2j+1\) with \(j\ge5\); then
\[
\sum_{q\ge11}\frac{2}{q(q-1)}
<\sum_{j=5}^{\infty}\frac{1}{2j^2}<\frac18.
\]
The product bound \(\prod(1-u_j)\ge1-\sum u_j\) therefore shows \(C>(4/7)(7/8)=1/2\). Each omitted factor when \(q\mid h\) strictly increases \(\Delta(h)\). If \(3\nmid h\), the factor \(2/3\) at \(q=3\) remains, so \(C\le\Delta(h)<2/3\). If \(3\mid h\), that factor is absent, so \(3C/2\le\Delta(h)<1\). The upper bounds are strict because a fixed \(h\) misses infinitely many prime factors. For the first supremum take \(h\) to be the product of odd primes from \(5\) through \(T\); for the second include \(3\). The residual Euler products tend to their claimed limits by absolute convergence. This also proves the prime-support invariance and ternary scaling identity.

## Verification
The accompanying `verify.py` checks the exact allowed-residue counts at prime-square moduli, the Chinese remainder count for the first three odd primes, the finite product correction for selected odd shifts, and direct shifted-flat frequency counts over primes up to a prescribed cutoff. The infinite density and sharp separation follow from the proof, not from these finite checks. A sample with \(X=600000\) and primes \(p>106\) gives frequencies near \(0.5355\) at \(h=1\), \(0.8035\) at \(h=3\), and \(0.9363\) at \(h=105\).

## Relationship to prior work
Broughan and Zhou (2010, Theorem 8) prove the unshifted case \(h=1\), with constant \(C\), and their subsequent comment explicitly describes numerical observations for **general fixed odd shifts**, including the split between shifts divisible and not divisible by three, as warranting investigation. The present theorem gives the entire odd-shift law and a strict gap between the two classes. Its analytic sieve is close to their method, but the prime-divisor correction and sharp shift-dependent separation are not established by that theorem. Mirsky's earlier work concerns squarefree shifted integers and prime-plus-power-free representations, but no equivalent all-odd-shift double-flat density is established by the material inspected.

## Limitations
No uniform error term as \(h\) grows with \(X\) is asserted. The theorem gives asymptotic densities, not an effective least simultaneous shifted-flat prime in each class. Although the exact general-shift statement was not found in inspected material, more general unpublished or unindexed sieve theorems may already imply it; the dependence on the known \(h=1\) sieve creates a nontrivial priority risk. The numerical tests are finite and are not substitutes for the prime number theorem in arithmetic progressions and Brun--Titchmarsh.

## References
Broughan, K. A. and Zhou, Q. (2010), “Flat primes and thin primes”, *Bulletin of the Australian Mathematical Society* **82**, 282–292, doi:10.1017/S0004972710000067. Theorem 8 and the comment on odd shifts (pp. 288–290). First public online date: 2010-04-26.

Mirsky, L. (1949), “The number of representations of an integer as the sum of a prime and a k-free integer”, *American Mathematical Monthly* **56**, 17–19, doi:10.1080/00029890.1949.11990233.

Montgomery, H. L. and Vaughan, R. C. (2007), *Multiplicative Number Theory I: Classical Theory*, Cambridge University Press (standard prime number theorem in arithmetic progressions and Brun--Titchmarsh inequality).
