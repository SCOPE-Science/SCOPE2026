# Quadratic-character twists of phase-only quartic Fourier maximizers over nineteen elements

## Finding
Let \(F=\mathbb F_{19}\), \(\zeta=\exp(2\pi i/19)\), and let \(\chi:F^\times\to\{-1,1\}\) be the quadratic character. For each \(f:F\to\mathbb C\) with \(|f(t)|=1\) for every \(t\), define its unnormalized quartic-graph Fourier transform and averaged fourth moment by
\[
Tf(u,v)=\sum_{t\in F}f(t)\zeta^{ut+vt^4},\qquad
\mathcal M_4(f)=\frac1{19^2}\sum_{u,v\in F}|Tf(u,v)|^4.
\]
Then \(\mathcal M_4(f)\le991\), and **all** equality cases are exactly
\[
\boxed{f(0)=u,\qquad f(t)=v\,\chi(t)^\varepsilon\zeta^{At+Bt^4}\quad(t\ne0),}
\]
where \(u,v\in\mathbb T\), \(\varepsilon\in\{0,1\}\), and \(A,B\in F\). Every five-tuple of parameters is unique. Thus the equality space consists of exactly \(2\cdot19^2=722\) disjoint real two-dimensional tori; after quotienting by common input phase it consists of \(722\) disjoint circles. The numerical optimum \(991\), already implied by published additive-energy work, is **not** asserted as a new numerical discovery; the complete optimizer description, including the quadratic-character torsion, is the finding.

## Assumptions and scope
All field additions, powers, and polynomial coefficients are reduced modulo \(19\). The input has exactly nineteen coefficients, *all* of modulus one; there are no zeros. The output is averaged over the full \(19^2\)-point dual plane, while \(Tf\) itself is unnormalized. This is a phase-only theorem, not a claim of the sharp unrestricted \(\ell^2\to L^4\) extension norm. A phase family is an equality family only for the stated quartic curve \(\{(t,t^4):t\in F\}\). There is no inference from numerical experiments to other primes.

## Proof
**1. Additive-fiber reduction.** For \((s,h)\in F^2\), define \(C_{s,h}=\{(a,b)\in F^2:a+b=s,\ a^4+b^4=h\}\). Finite Fourier orthogonality, expanding the fourth power and averaging over both frequencies, gives exactly
\[
\mathcal M_4(f)=\sum_{s,h\in F}\left|\sum_{(a,b)\in C_{s,h}}f(a)f(b)\right|^2
\le\sum_{s,h}|C_{s,h}|^2=991.
\]
The constant function realizes every triangle-inequality equality. Hence equality for arbitrary unimodular \(f\) is equivalent to
\[
 f(a)f(b)=f(c)f(d)
\quad\text{whenever}\quad
 a+b=c+d,\ a^4+b^4=c^4+d^4.
\]
The exact ordered-fiber size histogram is \(19\) fibers of size \(1\), \(99\) of size \(2\), and \(36\) of size \(4\), giving \(19+99\cdot4+36\cdot16=991\). The standalone checker independently enumerates these integers; the already-published quartic-graph energy identity also specializes to \(991\).

**2. Classify all nontrivial pair relations.** For a pair with sum \(s=a+b\) and product \(q=ab\), the power sum is
\[
 a^4+b^4=s^4-4s^2q+2q^2.
\]
If another unordered pair with the same sum has different product \(q'\), its fourth-power sum coincides precisely when \(q+q'=2s^2\). For \(s=0\), \(a=-b\) and the fourth sum is \(2a^4\). Since \(\gcd(4,18)=2\), this gives no distinct unordered pairs. For \(s\ne0\), scale all four entries by \(s^{-1}\), so their common sum is \(1\). Writing \(q'=2-q\), the two pairs exist over \(F\) precisely when both \(1-4q\) and \(1-4q'=4q-7\) are squares (zero permitted). Excluding the fixed product \(q=q'=1\), the only such products are
\[
\{q,q'\}=\{4,17\}\quad\text{or}\quad\{8,13\}.
\]
They yield precisely the unordered-pair comparisons
\[
\{1,6\}\sim\{12,14\},\qquad
\{1,8\}\sim\{12,16\},
\]
and their nonzero simultaneous dilations. These two dilation orbits each have \(18\) relations, are disjoint, and exhaust all \(36\) nontrivial comparisons. No such relation contains the coordinate \(0\). Each displayed equation is checked directly: the pairs have the same first-coordinate sum \(7\) or \(9\), respectively, and the same fourth-power sum modulo \(19\). The finite exhaustive \(q\)-list and the complete dilation count can be reconstructed by the attached exact-integer program; they also follow by enumerating the nine nonzero quadratic residues \(\{1,4,5,6,7,9,11,16,17\}\).

**3. Construct \(722\) allowable relative phase patterns.** The products of quadratic characters across each relation coincide: for the first seed, \(\chi(1\cdot6)=\chi(12\cdot14)=1\); for the second, \(\chi(1\cdot8)=\chi(12\cdot16)=-1\). Dilation multiplies both products by \(\chi(s)^2=1\). Therefore multiplying phases by \(\chi(t)\) preserves every relation. Similarly, the factors \(\zeta^{At+Bt^4}\) preserve every relation because both coordinate sums are equal. Finally, since no nontrivial relation contains \(0\), \(f(0)=u\) is unconstrained. This proves every displayed parameter choice attains the bound.

For distinct triples \((A,B,\varepsilon)\), the restrictions \(t\mapsto\chi(t)^\varepsilon\zeta^{At+Bt^4}\) to \(F^\times\) differ modulo *any* constant scalar. Indeed, a ratio involving exactly one \(\chi\) cannot be constant: a primitive nineteenth root of unity cannot have ratio \(-1\) between square and nonsquare entries. When \(\varepsilon\) agrees, constancy would make the polynomial \((A-A')t+(B-B')t^4-C\) vanish on \(18\) distinct elements for some \(C\in F\); its degree is at most four, so it is zero, implying \(A=A'\), \(B=B'\), and \(C=0\). Consequently the \(2\cdot19^2=722\) relative phase patterns are all distinct.

**4. Prove there are no others, using a finite integer certificate.** Let
\[
H=\{(n_1,\ldots,n_{18})\in\mathbb Z^{18}:\sum_{t=1}^{18}n_t=0\}.
\]
Deleting coordinate \(18\) identifies \(H\cong\mathbb Z^{17}\). Use only the first seed and its dilations \(w=1,2,\ldots,17\): define
\[
 R_w=e_{w}+e_{6w}-e_{12w}-e_{14w}\ \in H,
\]
with all indices reduced to \(\{1,\ldots,18\}\) modulo \(19\). Let \(M\) be the \(17\)-square integer matrix obtained by deleting coordinate \(18\) from the rows \(R_w\), with rows ordered by \(w=1,\dots,17\), columns indexed by \(1,\dots,17\). Exact fraction-free integer elimination gives the **nonzero determinant of absolute value \(722\)**. The standalone verifier defines \(M\) in fifteen lines using these explicit formulas and computes the determinant entirely over the integers using the Bareiss algorithm, with exact-divisibility assertions.

Thus the lattice \(L\) generated by these \(17\) relations has index \([H:L]=722\). Phase vectors on the \(18\) nonzero coordinates, modulo their common phase, are characters of \(H\); imposing the \(17\) relations restricts them to characters of \(H/L\), so there are **exactly \(722\)** such phase patterns. The previous paragraph constructed \(722\) distinct solutions, which also satisfy every remaining relation. They therefore exhaust all equality phases on \(F^\times\). The free phase \(f(0)\) provides one additional circle factor beyond the nonzero common phase, completing the asserted \(722\) two-tori and uniqueness.

## Verification
The standalone Python standard-library script `artifacts/verify.py` runs exact pair enumeration, confirms \(36\) comparisons in two \(18\)-element orbits and their quadratic-character preservation, verifies the ordered-fiber histogram and moment \(991\), computes the \(17\)-square determinant with exact integer Bareiss elimination, and checks nonconstancy of each nonzero additive-character pair. Run `python3 artifacts/verify.py` from the package root. Its recorded output is `artifacts/verification_output.txt`. Computation is exhaustive only for \(F=\mathbb F_{19}\), the precise finite field in the theorem, so no infinite-family assertion relies on this certificate.

## Relationship to prior work
González-Riquelme and Oliveira e Silva, *Sharp extension inequalities on finite fields* (2024), motivate exact fourth-moment Fourier extension and equality questions for conic and paraboloid settings, not this quartic phase-only equality subgroup. The published finding *Exact additive energy of the finite-field quartic graph* proves the quartic constant-input fourth moment for all finite fields of characteristic greater than three, including the value \(991\) at \(19\); it does **not** classify equality phases. The published findings *Quartic-image Singer geometry and all unimodular Fourier fourth-moment maximizers over thirteen elements* and *Sidon quartic-power images and the complete phase-only fourth-moment equality groups* classify the distinct Sidon primes \(13\) and \(5,13\), respectively. The second specifically limits the phase classification to those primes. In contrast, \(19\) is non-Sidon and has a genuine quadratic-character phase twist, captured by the index-\(722\) relation lattice. Thus neither the prior numerical energy nor prior prime-specific optimizer classifications implies this finding.

## Limitations
The conclusion is restricted to the prime field of nineteen elements and strictly unimodular inputs. No unrestricted Fourier extension norm, noise stability, general prime classification, or automatic independent mathematical validation is claimed. The arithmetically explicit determinant is a reproducible finite certificate for this one field. An older result expressed in Freiman-character or finite-additive-relation-lattice terminology could remain undiscovered.

## References
1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, first publicly posted 2024-05-26, especially its introductory finite-field extension and convolution framework.
2. *Exact additive energy of the finite-field quartic graph*, published mathematical finding, published-finding corpus, 2026-10-04, `2026/10/4/SCOPE-exact-additive-energy-of-the-finite-field-quartic-graph--235f10989b3f`.
3. *Quartic-image Singer geometry and all unimodular Fourier fourth-moment maximizers over thirteen elements*, published mathematical finding, published-finding corpus, 2026-10-11, `2026/10/11/SCOPE-quartic-image-singer-geometry-and-all-unimodular-fourier-fourth--3cf25572a021`.
4. *Sidon quartic-power images and the complete phase-only fourth-moment equality groups*, published mathematical finding, published-finding corpus, 2026-10-11, `2026/10/11/SCOPE-sidon-quartic-power-images-and-the-complete-phase-only-fourth-mo--bccd0021eeec`.
