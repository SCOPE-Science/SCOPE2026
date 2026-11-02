# Exact gap-residue equidistribution for three consecutive numerical-semigroup generators

## Finding
For every integer \(n\ge3\), let \(S_n=\langle n,n+1,n+2\rangle\), and write \(G_n=\mathbb N_0\setminus S_n\) for its finite gap set. A finite set is *equidistributed modulo* \(m\ge2\) if each residue class contains exactly \(|G_n|/m\) elements of the set. The complete classification is
\[
\boxed{G_n\text{ equidistributed modulo }m\iff n=2h+1\text{ and }[m\mid h+1\text{ or }(m\mid h\text{ and }3\nmid m)].}
\]
Thus no even parameter works; for \(n=11\) the admissible moduli are \(2,3,5,6\), whereas for \(n=13\) they are \(2,7\). The restriction at the prime \(3\) is essential.

## Assumptions and scope
Throughout, \(n,m\) are integers with \(n\ge3\), \(m\ge2\); the semigroup is the set of nonnegative integral combinations of the three displayed generators. If \(G_n(t)=\sum_{g\in G_n}t^g\), then the elementary roots-of-unity criterion says equidistribution modulo \(m\) is equivalent to \(G_n(\zeta)=0\) for **every** nonidentity \(m\)-th root of unity \(\zeta\). In particular, \(m\mid |G_n|\) is necessary. The proof is for all integers in the stated ranges, not merely the computational test range.

## Proof
**Step 1 (exact gaps).** Fix \(a=n\). In each nonzero residue class \(r\pmod a\), \(1\le r<a\), the least semigroup element is
\[
w_r=a\left\lceil\frac r2\right\rceil+r.
\]
Indeed, \(k\) copies of generators \(a+1,a+2\) contribute an increment in \([k,2k]\) beyond \(ka\). For \(k<\lceil r/2\rceil\), this positive increment is strictly less than \(r\), so cannot be congruent to \(r\pmod a\). Conversely \(k=\lceil r/2\rceil\) realizes increment \(r\), using at most one copy of \(a+1\). Adding copies of \(a\) cannot improve the minimum. It follows that
\[
G_a=\{r+aj:1\le r<a,\ 0\le j<\lceil r/2\rceil\}.
\]
Consequently the genus is \(|G_{2h}|=h^2\) and \(|G_{2h+1}|=h(h+1)\).

**Step 2 (even parameters cannot work).** Let \(a=2h\), \(h\ge2\). If equidistribution modulo \(m\) held then \(m\mid h^2\). Choose any prime \(p\mid m\); necessarily \(p\mid h\). For a primitive \(p\)-th root \(q\), we have \(q^h=1\). From Step 1,
\[
G_{2h}(q)=\sum_{s=1}^{h-1}s(q^{2s-1}+q^{2s})+hq^{2h-1}.
\]
If \(p=2\), this is \(-h\ne0\). If \(p\) is odd, the geometric-derivative identity \(\sum_{s=1}^{h-1}s(q^2)^s=-h/(1-q^2)\) gives \(G_{2h}(q)=-h/(1-q)\ne0\). Since \(q\) is also an \(m\)-th root, uniformity is impossible.

**Step 3 (odd parameters, generating polynomial).** Put \(a=2h+1\), \(h\ge1\). Pair residues \(r=2s-1,2s\) for \(1\le s\le h\), then set \(s=j+t+1\). Step 1 gives the exact polynomial
\[
G_{2h+1}(z)=z(1+z)\sum_{j,t\ge0\atop j+t\le h-1}z^{(a+2)j+2t}.
\]
For \(z\ne1\) with \(z^a\ne1\) and \(z^{a+2}\ne1\), summing the two finite geometric progressions yields
\[
G_{2h+1}(z)=\frac{z}{1-z}\left(\frac{1-z^{h(a+2)}}{1-z^{a+2}}-z^{2h}\frac{1-z^{ah}}{1-z^a}\right). \tag{1}
\]

**Step 4 (all roots-of-unity zeros subject to the genus).** Let \(q\ne1\) be a root of unity with \(q^{h(h+1)}=1\), and put \(H=q^h\). Since \(a=2h+1\), \(\gcd(a,h(h+1))=1\). Thus \(q^a\ne1\). Also \(\gcd(a+2,h(h+1))=\gcd(3,h)\); hence \(q^{a+2}=1\) is possible only if \(3\mid h\) and \(q\) has exact order \(3\). First exclude this singular case. Reducing exponents \(h(a+2)\equiv h\) and \(ah\equiv-h\pmod{h(h+1)}\) in (1) gives
\[
G_{2h+1}(q)=\frac{q(1-H)(1-qH)\,[1+(1+q)H+q^2H^2]}
{(1-q)(1-qH^2)(1-q^3H^2)}.\tag{2}
\]
The quadratic factor in brackets does **not** vanish: if it did, with \(W=qH\) on the unit circle, division by \(W\) would give \(W+W^{-1}=-(1+q^{-1})\). The left side is real, forcing \(q\) real. As \(q\ne1\), necessarily \(q=-1\), but then \(W=q^{h+1}=\pm1\), and the displayed equation is impossible. Therefore, outside the singular case,
\[
G_{2h+1}(q)=0\quad\Longleftrightarrow\quad q^h=1\ \text{or}\ q^{h+1}=1.\tag{3}
\]
If instead \(3\mid h\) and \(q\) is a primitive cube root, then \(q^{a+2}=1\). The finite polynomial of Step 3, not (1), gives
\[
G_{2h+1}(q)=(q+q^2)\sum_{t=0}^{h-1}(h-t)q^{2t}
=\frac h3(q^2+2q)\ne0.\tag{4}
\]
The last equality follows by grouping \(t\) into consecutive blocks of three.

**Step 5 (classification).** Suppose the gaps are equidistributed modulo \(m\). Then \(m\mid h(h+1)\) and the polynomial vanishes at a primitive \(m\)-th root. Equations (3)–(4) imply \(m\mid h\) or \(m\mid h+1\). If \(m\mid h\) and \(3\mid m\), equidistribution would also force vanishing at the primitive cube roots, contradicting (4), since then \(3\mid h\). Conversely, if \(m\mid h+1\), every nontrivial \(m\)-th root has order dividing \(h+1\) and is nonsingular in (2), hence is a zero. If \(m\mid h\) and \(3\nmid m\), every nontrivial \(m\)-th root similarly satisfies (3) without the singularity. The roots-of-unity criterion completes the proof. \(\square\)

## Verification
A standalone standard-library script `verify.py` recomputes Apéry minima by shortest paths on residues, constructs the gaps directly, and compares their actual residue counts with the theorem. It checks all \(3\le n\le170\) and \(2\le m<\min(3n,220)\), totaling 29,098 parameter-modulus pairs. It also independently checks the predicted genus for each parameter. This finite test supports the algebra but is not a proof of the infinite result.

## Relationship to prior work
C. M. Shor, *On evenly distributed sets of gaps of numerical semigroups* (arXiv:2101.01760v1, 5 January 2021; journal title *Equidistribution of numerical semigroup gaps modulo m*, DOI 10.1016/j.disc.2022.112995) develops the gap-polynomial and Apéry criteria and determines the cases of two generators and maximal embedding dimension with arithmetic Apéry data. Those general criteria motivate the present problem; this theorem specializes to an embedding-dimension-three family with a nonarithmetic Apéry set for \(n\ge4\), then classifies **all** allowed moduli by a separate root-of-unity factorization. The general Fourier equivalence is prior work, not claimed new.

P. A. García-Sánchez, L. González and F. Planas-Vilanova, *Elements with unique length factorization of a numerical semigroup generated by three consecutive numbers* (arXiv:2404.06358v1, 9 April 2024) treats the same generators but classifies factorization lengths and denumerants rather than modular distributions of gaps. The standard description of the Frobenius number and Apéry structure for intervals is also prior knowledge; no new Frobenius or genus formula is claimed.

## Limitations
The theorem concerns **gap residue counts**, not factorization-length residue counts or arbitrary arithmetic-progression generators. The calculation proves an exact universal classification but does not claim priority against every unindexed publication; a hidden specialization of a broader result remains a bibliographic risk. The finite checks cover a bounded domain, while equations (1)–(4) establish the full statement. The method does not classify larger generator intervals.

## References
1. C. M. Shor, *On evenly distributed sets of gaps of numerical semigroups*, arXiv:2101.01760v1, 2021-01-05, https://arxiv.org/abs/2101.01760. Journal version: *Equidistribution of numerical semigroup gaps modulo m*, Discrete Mathematics 345 (2022), 112995, DOI 10.1016/j.disc.2022.112995.
2. P. A. García-Sánchez, L. González, F. Planas-Vilanova, *Elements with unique length factorization of a numerical semigroup generated by three consecutive numbers*, arXiv:2404.06358v1, 2024-04-09, https://arxiv.org/abs/2404.06358.
3. C. M. Shor and J. H. Sim, *Equidistribution Conditions for Gaps of Geometric Numerical Semigroups*, arXiv:2503.10826v1, 2025-03-13, https://arxiv.org/abs/2503.10826 (different generator family).
