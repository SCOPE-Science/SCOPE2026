# Exact cycle spectra and minimal components of dyadic monomial shears

## Finding

For each integer \(d\ge3\), consider the polynomial permutation
\[
 f_d(x)=x+2x^d
\]
on \(\mathbb Z/2^k\mathbb Z\), for every integer \(k\ge1\). For any residue \(x\), let \(L_{d,k}(x)\) be its least positive orbit period. The **complete period formula** is
\[
L_{d,k}(x)=
\begin{cases}
  1,&x\equiv0\pmod{2^k},\\
  2^{k-1},&x\text{ odd},\ d\text{ even},\\
  1,&x\text{ odd},\ d\text{ odd},\ k=1,\\
  2^{\max\{1,k-2\}},&x\text{ odd},\ d\text{ odd},\ k\ge2,\\
  2^{\max\{0,k-1-ds\}},&\nu_2(x)=s,\ 1\le s<k.
\end{cases}
\]
Here \(\nu_2(x)=s\) for a nonzero residue means that \(2^s\) divides its integer representatives and \(2^{s+1}\) does not; this is unambiguous when \(s<k\). The map is a permutation at every depth.

More precisely, the exact minimal decomposition of the corresponding self-homeomorphism of the \(2\)-adic integers \(\mathbb Z_2\) consists of the fixed singleton \(\{0\}\) and the following clopen minimal components:

- If \(d\) is even, all odd \(2\)-adic integers comprise **one** minimal component.
- If \(d\) is odd, the odd integers comprise **two** minimal components, given by the residue pairs \(\{1,3\}\pmod8\) and \(\{5,7\}\pmod8\).
- For each integer \(s\ge1\), the valuation shell \(\{x:\nu_2(x)=s\}\) splits into exactly \(2^{(d-1)s}\) minimal components. They are the individual residue balls \(r+2^{1+ds}\mathbb Z_2\) with \(0\le r<2^{1+ds}\) and \(\nu_2(r)=s\).

Thus the parity of the polynomial degree produces a sharp one-versus-two component transition on odd units, while the exact component multiplicity at positive valuation is exponential in \((d-1)s\).

At finite depth, write \(C_{d,k}(s)\) for the number of cycles entirely inside the shell \(\nu_2(x)=s\), \(1\le s<k\). Then
\[
 C_{d,k}(s)=
 \begin{cases}
  2^{k-s-1},&k\le1+ds,\\
  2^{(d-1)s},&k\ge2+ds.
 \end{cases}
\]
There is one cycle containing zero. For \(k\ge2\), the odd shell has one cycle if \(d\) is even; for odd \(d\) it has one cycle at \(k=2\) and two cycles at \(k\ge3\). At \(k=1\), the odd residue is fixed.

## Assumptions and scope

All degrees \(d\ge3\), all residue depths \(k\ge1\), and all residue classes are included. The polynomial coefficient multiplying \(x^d\) is exactly \(2\); no claim is made for arbitrary odd multiples of that coefficient. The infinite decomposition is for the compact ring \(\mathbb Z_2\), with minimality meaning every forward orbit is dense in its component.

## Proof

**Permutation.** For any integer \(a\) and \(t\ge1\), the binomial theorem gives \(f_d(a+2^t)-f_d(a)\equiv2^t\pmod{2^{t+1}}\). Consequently each permutation of residues modulo \(2^t\) lifts to a permutation modulo \(2^{t+1}\); the initial map modulo two is the identity. This proves bijectivity for every \(k\).

**Doubling lemma.** Let \(G\in\mathbb Z[X]\), let \(x\in\mathbb Z\), and put \(\Delta=G(x)-x\). Suppose \(t=\nu_2(\Delta)\ge2\), and \(G'(z)\equiv1\pmod4\) at every point of the forward \(G\)-orbit of \(x\). Taylor's polynomial identity gives
\[
G(G(x))-x=\Delta(1+G'(x))+\Delta^2 H(x,\Delta)
\]
for an integer polynomial \(H\). Since \(1+G'(x)\equiv2\pmod4\) and \(2t\ge t+2\), its valuation is exactly \(t+1\). The derivative of \(G^2\) is also congruent to one modulo four on the same invariant orbit. Repetition therefore increases the valuation by exactly one at each period-doubling step.

**Positive valuation shells.** Suppose \(\nu_2(x)=s\ge1\). Then
\[
 \nu_2(f_d(x)-x)=1+ds\ge4,
 \qquad f_d'(x)=1+2d x^{d-1}\equiv1\pmod4.
\]
The valuation of each iterate remains \(s\), so the derivative congruence holds throughout. By the doubling lemma,
\[
 \nu_2\!\left(f_d^{2^t}(x)-x\right)=1+ds+t\quad(t\ge0).
\]
Thus the first power-of-two iterate acting as the identity modulo \(2^k\) has exponent \(\max\{0,k-1-ds\}\). Since all residues eventually return after a power-of-two number of steps, this is their precise period.

**Odd units.** For odd \(x\), one has the exact identity
\[
f_d^2(x)-x=2x^d\left(1+(1+2x^{d-1})^d\right).
\]
If \(d\) is even, then \(1+2x^{d-1}\equiv3\pmod4\); raising to an even exponent gives one modulo four, so the displayed difference has valuation exactly two. Both \(f_d'\) and \((f_d^2)'\) are congruent to one modulo four on odd residues. The doubling lemma gives \(\nu_2(f_d^{2^t}(x)-x)=t+1\) for all \(t\ge1\).

If \(d\) is odd, \(x^{d-1}\equiv1\pmod8\), so \(1+2x^{d-1}\equiv3\pmod{16}\). For an odd exponent \(d\), factoring \(Y^d+1\) by \(Y+1\) shows that the quotient is odd when \(Y\) is odd; therefore
\[
 \nu_2\left(1+(1+2x^{d-1})^d\right)=2.
\]
Hence \(\nu_2(f_d^2(x)-x)=3\). On odd residues, \(f_d'(x)\equiv3\pmod4\), so \((f_d^2)'(x)\equiv1\pmod4\), and the doubling lemma applied to \(f_d^2\) gives \(\nu_2(f_d^{2^t}(x)-x)=t+2\) for all \(t\ge1\). Together with \(\nu_2(f_d(x)-x)=1\), these exact valuations yield the asserted odd periods, including small depths \(k=1,2,3\).

**Period powers and completeness.** The preceding valuations show that each residue is fixed by some iterate of power-of-two length; as \(f_d\) is bijective, every least period divides such a power and so is itself a power of two. Each valuation shell has \(2^{k-s-1}\) residues at depth \(k\). Dividing that cardinality by its common orbit length proves the stated finite cycle counts.

For \(s\ge1\), \(f_d(x)-x\) is divisible by \(2^{1+ds}\). Thus each ball \(r+2^{1+ds}\mathbb Z_2\), with \(\nu_2(r)=s\), is invariant. For every \(k\ge1+ds\), its reduction contains exactly \(2^{k-1-ds}\) elements, equal to their orbit length, so it is a single cycle. Therefore every orbit is dense in that ball. There are exactly \(2^{(d-1)s}\) such balls.

For even \(d\), the odd shell is one cycle at each finite depth, so the odd \(2\)-adic ball is minimal. For odd \(d\), reduction modulo eight acts as multiplication by three on the four odd residues, yielding precisely the two invariant pairs \(\{1,3\}\) and \(\{5,7\}\). At every deeper depth each such pair lifts to \(2^{k-2}\) elements, their common full orbit length, so each pair defines one minimal component. The only fixed point in \(\mathbb Z_2\) is \(0\), since \(f_d(x)=x\) is equivalent to \(2x^d=0\). These cases partition \(\mathbb Z_2\) and finish the proof.

## Verification

The included `verify.py` directly constructs the finite permutations and follows every orbit, without relying on the proof's period formulas to generate those orbits. It checks all \(d\in\{3,\dots,21\}\) and \(k\in\{1,\dots,13\}\), compares each element's period and the full independent cycle histogram with the formulas, and prints a single `VERIFY_OK` line. This finite experiment checks examples and implementation details but is not used as proof of infinite completeness.

## Relationship to prior work

Rivest's 2001 classification proves that the polynomial is a permutation modulo every power of two; it does not specify orbit periods or minimal components. Anashin's 2007 treatment explicitly includes the quadratic map \(x+2x^2\) as a measure-preserving example and develops general \(2\)-adic ergodicity tools. Fan and Liao (2010) establish a general minimal-decomposition framework and treat every quadratic polynomial in depth; the quadratic degree is therefore excluded from the new all-degree statement. Their general cycle-lifting theory is relevant to the method, but the degree-dependent explicit shell census for all \(d\ge3\) is not stated in the material inspected. The theorem supplies that complete specialization with a direct valuation proof.

## Limitations

The novelty comparison is relative to the sources inspected and record searches, not a claim of exhaustive bibliographic priority. General \(p\)-adic lifting results may yield related cases after nontrivial specialization. The formula is for coefficient \(2\) only; for arbitrary \(2a\) with odd \(a\), especially odd degree, a different orbit spectrum can occur. None of the finite verification ranges substitutes for the proof's universal quantifiers. Independent validation has not been performed.

## References

1. R. L. Rivest, *Permutation Polynomials Modulo \(2^w\)*, Finite Fields and Their Applications 7 (2001), 287–292, doi:10.1006/ffta.2000.0282. Author-hosted full text: https://people.csail.mit.edu/rivest/pubs/Riv01c.pdf . Published online 2001-02-12.
2. V. Anashin, *Non-Archimedean Ergodic Theory and Pseudorandom Generators*, arXiv:0710.1418 (2007). https://arxiv.org/pdf/0710.1418 .
3. A. Fan and L. Liao, *On Minimal Decomposition of \(p\)-Adic Polynomial Dynamical Systems*, arXiv:1010.5583 (2010); Advances in Mathematics 228 (2011), 2116–2144. https://arxiv.org/pdf/1010.5583 .
