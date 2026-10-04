# A \(0/1/\ge4\) codimension-two gap in Kato's prescribed-indefinite-fold construction
## Finding
Let
\[
b=\sigma_{z_1}^{m_1}\sigma_{z_2}^{m_2}\cdots\sigma_{z_\ell}^{m_\ell}
\]
be the compressed \(n\)-braid word used in Kato's construction, with \(n\ge2\), \(m_i\ne0\), \(1\le z_i\le n-1\), and \(z_i\ne z_{i+1}\). Let
\[
f_b:S^3\longrightarrow\mathbb R^2
\]
be the stable map produced in the proof of Kato's Theorem 1.1, whose indefinite fold locus is isotopic to the closure \(\widehat b\), with no cusp points and no type-\(\mathrm{II}^3\) singular fibers.

Define
\[
r(b)=\left|\{i:z_i\ne1\}\right|,
\qquad
o(b)=\left|\{i:m_i\text{ is odd}\}\right|.
\]
Then the exact number of type-\(\mathrm{II}^2\) singular fibers in this construction is
\[
\boxed{\left|\mathrm{II}^2(f_b)\right|=4r(b)+o(b).}
\]

Three immediate consequences are useful.

First,
\[
\left|\mathrm{II}^2(f_b)\right|\le5\ell.
\]

Second, the construction has a genuine low-complexity gap:
\[
\left|\mathrm{II}^2(f_b)\right|\notin\{2,3\}.
\]
Indeed, if the count is at most \(3\), then \(r(b)=0\). Since consecutive syllables in the compressed word have distinct generator indices, this forces \(\ell=1\) and \(b=\sigma_1^m\). The count is then \(0\) for even \(m\) and \(1\) for odd \(m\).

Third, if \(c(\widehat b)\) denotes the number of components of the closed braid, then
\[
\left|\mathrm{II}^2(f_b)\right|\equiv n-c(\widehat b)\pmod2.
\]
Thus, although the exact cost depends on the chosen braid word and on the distinguished generator \(\sigma_1\), its parity is forced by the strand number and the number of components.

## Assumptions and scope
The statement concerns the specific map constructed in the proof of Theorem 1.1 of Gakuto Kato's 2026 preprint. It does not claim that the displayed number is minimal among all stable maps having the same indefinite fold locus.

The braid word is in Kato's compressed form: each exponent is nonzero and adjacent syllables use different Artin generators. Negative exponents are allowed; only their parity enters the count.

A type-\(\mathrm{II}^2\) singular fiber is understood in the standard classification of singular fibers of stable maps from \(3\)-manifolds to surfaces. Kato's construction has no type-\(\mathrm{II}^3\) fibers.

## Proof
Kato decomposes the solid cylinder carrying the braid into pieces \(W_i\), one for each syllable \(\sigma_{z_i}^{m_i}\), and constructs a map
\[
\Psi^i:W_i\longrightarrow T_i.
\]
There are four local cases.

If \(z_i=1\) and \(m_i\) is even, the source states that the images of both the definite and indefinite fold points have no normal crossings. The local construction therefore contributes no type-\(\mathrm{II}^2\) fiber.

If \(z_i=1\) and \(m_i\) is odd, the construction inserts exactly one instance of Lemma 2.1. In that lemma the two adjacent saddle points meet at the middle level, and Figure 2 displays the connected singular fiber with the three-loop-chain topology drawn as type \(\mathrm{II}^2\) in Figure 1. The remaining isotopies in this case perform the half-twists and switch definite-fold heights; they do not introduce a second two-indefinite-point singular fiber. Hence this piece contributes exactly one type-\(\mathrm{II}^2\) fiber.

If \(z_i\ne1\) and \(m_i\) is even, Kato states explicitly that \(\Psi^i\) has four type-\(\mathrm{II}^2\) singular fibers.

If \(z_i\ne1\) and \(m_i\) is odd, Kato states explicitly that \(\Psi^i\) has five type-\(\mathrm{II}^2\) singular fibers.

Thus the local contribution is
\[
c_i=
\begin{cases}
0,&z_i=1,\ m_i\text{ even},\\
1,&z_i=1,\ m_i\text{ odd},\\
4,&z_i\ne1,\ m_i\text{ even},\\
5,&z_i\ne1,\ m_i\text{ odd}.
\end{cases}
\]
Equivalently,
\[
c_i=4\,\mathbf 1_{\{z_i\ne1\}}+\mathbf 1_{\{m_i\text{ odd}\}}.
\]

The rectangles \(T_i\) have disjoint interiors. Kato glues the maps \(\Psi^i\) along their common boundary Morse functions, then attaches a product map on the complementary cylinder and a natural projection on the second solid torus. These attachments introduce no additional codimension-two singular fiber. Therefore
\[
\left|\mathrm{II}^2(f_b)\right|
=\sum_{i=1}^{\ell}c_i
=4r(b)+o(b).
\]

The bound
\[
\left|\mathrm{II}^2(f_b)\right|\le5\ell
\]
is immediate.

For the low-complexity claim, if the count is at most \(3\), then \(r(b)=0\), so every \(z_i=1\). Compression requires \(z_i\ne z_{i+1}\), hence \(\ell=1\). The formula then gives cost \(0\) or \(1\) according to the parity of the single exponent.

For the parity statement, let \(\pi_b\in S_n\) be the permutation of the braid. Each Artin generator has odd permutation sign, so
\[
\operatorname{sgn}(\pi_b)
=(-1)^{\sum_i m_i}
=(-1)^{o(b)}.
\]
If \(\pi_b\) has \(c(\widehat b)\) cycles, then its sign is
\[
(-1)^{n-c(\widehat b)}.
\]
Since \(4r(b)\) is even,
\[
\left|\mathrm{II}^2(f_b)\right|
\equiv o(b)
\equiv n-c(\widehat b)\pmod2.
\]

## Verification
The critical local counts were checked directly in the full text of arXiv:2609.09937v1.

For \(z_i=1\) and even exponent, the proof records no normal crossing of the indefinite-fold image. For \(z_i=1\) and odd exponent, the proof invokes Lemma 2.1 once; the middle fiber in Figure 2 matches the type-\(\mathrm{II}^2\) model in Figure 1. For \(z_i\ne1\), the proof explicitly gives four type-\(\mathrm{II}^2\) fibers in the even case and five in the odd case.

The gluing step was also checked: after the \(W_i\)-pieces are joined, the remaining pieces are induced by product structure and by a natural projection, and Kato's final map is stable, cusp-free, and type-\(\mathrm{II}^3\)-free. No extra codimension-two event is inserted by those attachments.

The parity corollary is independent of the singularity calculation once the exact count is known: it follows from the permutation sign of a braid word and the equality between the number of components of a braid closure and the number of cycles of its induced permutation.

No finite experiment is used to establish the theorem.

## Relationship to prior work
Kato's 2026 preprint proves the new qualitative existence theorem that every link in \(S^3\) can be realized as the indefinite fold locus of a cusp-free stable map to \(\mathbb R^2\) with no type-\(\mathrm{II}^3\) fibers. Its proof gives the four local constructions above, including explicit four- and five-fiber counts in the two \(z_i\ne1\) cases, but it does not state the aggregate formula \(4r(b)+o(b)\), the \(0/1/\ge4\) gap, or the parity law.

Ishikawa and Koda introduced stable map complexity as a weighted count of codimension-two singular fibers and studied links placed in the definite-fold part of a stable map. Their low-complexity classification and crossing-number bounds therefore motivate counting type-\(\mathrm{II}^2\) fibers, but they do not give a braid-syllable formula for Kato's newly prescribed indefinite-fold construction.

Ichihara and Kato later obtained exact type-\(\mathrm{II}^2\) counts for a two-bridge family with the link as the definite fold locus. That result has a different prescribed locus and a different construction.

## Limitations
The formula is construction-specific. It is not an invariant of the link alone and does not assert minimality among all cusp-free stable maps with the same indefinite fold locus.

The exact integer depends on the chosen braid representative and on Kato's distinguished generator \(\sigma_1\). Markov moves can change the word and the strand number.

The low-complexity gap \(0/1/\ge4\) is therefore a classification of outputs of this construction, not a classification of all stable maps realizing a fixed link as an indefinite fold locus.

## References
1. G. Kato, *Links and singularities of stable maps from \(3\)-manifolds to surfaces*, arXiv:2609.09937v1, first posted 2026-09-09.
2. M. Ishikawa and Y. Koda, *Stable maps and branched shadows of \(3\)-manifolds*, Math. Ann. 367 (2017), 1819--1863; arXiv:1403.0596v1.
3. K. Ichihara and G. Kato, *Two-bridge links and stable maps into the plane*, J. Knot Theory Ramifications 34 (2025), 2550007; arXiv:2405.14296.
