# Fiber divisibility divides \(g-1\) for positive Lefschetz fibrations
## Finding
Let \(f:X\to S^2\) be a Lefschetz fibration in the conventions of Baykur--Hamada, with regular fiber \(\Sigma_g\) of genus \(g\ge2\), and let \(m(f)\) be the divisibility of \([\Sigma_g]\) in \(H_2(X;\mathbb Z)/\operatorname{Tor}\). Then \(m(f)\mid(g-1)\). Consequently every genus-\(2\) or genus-\(3\) such fibration admits a positive \(2\)-section; more generally, every genus \(g\ge3\) such fibration admits a positive \(g-1\)-section, while every genus-\(2\) such fibration admits a positive \(d\)-section for every \(d\ge2\).

The point is that the almost-complex first Chern class does more than show that the fiber is non-torsion: its characteristic parity removes the extra factor of \(2\) from the immediate divisibility bound.

## Assumptions and scope
A Lefschetz fibration means a relatively minimal map from a closed, connected, smooth, oriented four-manifold to \(S^2\), with connected regular fibers, distinct critical values, nonempty critical locus, and only positive Lefschetz singularities, exactly as in the cited source. The regular fiber has genus \(g\ge2\). Let \(F=[\Sigma_g]\) denote its homology class and let \(m=m(f)\) be its divisibility in the free abelian group \(H_2(X;\mathbb Z)/\operatorname{Tor}\).

No assertion is made for achiral Lefschetz fibrations. The statement does not claim that \(F\) is primitive for \(g\ge3\), and it does not settle the universal \(2\)-section question in genus \(g\ge4\).

## Proof
Baykur--Hamada prove that \(F\) is non-torsion and define \(m\) as its divisibility in \(H_2(X;\mathbb Z)/\operatorname{Tor}\). Thus there is a primitive class \(A\) in the free quotient such that
\[
F=mA.
\]
A regular fiber has self-intersection zero, so
\[
0=F^2=m^2A^2.
\]
The intersection pairing takes integer values on the free quotient, hence \(A^2=0\).

For an almost complex structure \(J\) adapted to the fibration, the source records
\[
\langle c_1(TX,J),F\rangle=\chi(\Sigma_g)=2-2g.
\]
For every almost complex oriented four-manifold, \(c_1(TX,J)\bmod2=w_2(X)\). The Wu formula therefore says that \(c_1(TX,J)\) is characteristic:
\[
\langle c_1(TX,J),x\rangle\equiv x^2\pmod2
\]
for every \(x\in H_2(X;\mathbb Z)/\operatorname{Tor}\). Applying this to \(A\) and using \(A^2=0\), there is an integer \(k\) with
\[
\langle c_1(TX,J),A\rangle=2k.
\]
Consequently
\[
2-2g=\langle c_1(TX,J),mA\rangle=2mk,
\]
so
\[
g-1=-mk.
\]
Hence \(m\mid(g-1)\).

Baykur--Hamada's Corollary 8 states that the positive multisection degrees \(d\ge2\) are exactly the multiples of \(m(f)\). If \(g=2\), the divisibility relation forces \(m=1\), so every \(d\ge2\) occurs, in particular \(d=2\). If \(g=3\), then \(m\mid2\), so a \(2\)-section exists. For every \(g\ge3\), the integer \(g-1\ge2\) is a multiple of \(m\), so a positive \(g-1\)-section exists.

## Verification
The argument is symbolic. Its critical inputs were checked directly in the full text of arXiv:2610.01776v1: the definition of \(m(f)\) as fiber divisibility, Corollary 8 identifying all multisection degrees, the adapted almost-complex evaluation \(\langle c_1,F\rangle=2-2g\), and Question 20 asking whether \(m(f)\) always divides \(2\).

The remaining topological step is the standard characteristic-class identity \(c_1\bmod2=w_2\) together with the Wu formula. Torsion causes no ambiguity: the intersection form and Chern-class pairing used above descend to the free quotient, and integral cohomology classes vanish on torsion homology.

Two boundary checks are immediate. For \(g=2\), the theorem gives \(m=1\). For \(g=3\), it gives \(m\in\{1,2\}\), exactly enough for a \(2\)-section. No finite experiment is used as a substitute for the universal proof.

## Relationship to prior work
Baykur--Hamada introduce the obstruction controlling sections and prove that its abelianization has order \(m(f)\), with positive multisection degrees exactly the multiples of \(m(f)\). They explicitly ask whether every Lefschetz fibration over \(S^2\) admits a \(2\)-section, equivalently whether \(m(f)\mid2\), and note that the stronger claimed primitivity theorem has a gap. The divisibility-by-\(g-1\) statement is not stated in the inspected paper.

Their earlier work on arbitrary-signature Lefschetz fibrations gives a monodromy method for computing fiber divisibility but does not state the characteristic-parity bound \(m(f)\mid(g-1)\). Older multisection papers provide explicit genus-two fibrations with \(2\)-sections; those examples do not imply universal existence for every genus-two or genus-three fibration.

Targeted searches for fiber-divisibility, characteristic-class, genus-minus-one, genus-two \(2\)-section, genus-three \(2\)-section, and \(g-1\)-section formulations did not locate a theorem implying the claim.

## Limitations
The theorem uses positivity through the source's Lefschetz-fibration conventions and multisection existence theorem. It does not apply verbatim to achiral Lefschetz fibrations, for which the source notes low-degree multisection behavior can fail.

For \(g\ge4\), the bound \(m(f)\mid(g-1)\) alone need not imply \(m(f)\mid2\), so the source's general Question 20 remains open in those genera. The proof also does not establish primitivity except in genus \(2\).

A residual originality risk remains that the characteristic-parity observation could occur in older unindexed four-manifold literature under different terminology; the inspected sources and targeted searches did not reveal such a statement.

## References
1. R. Inanç Baykur and Noriyuki Hamada, *Sections, pseudosections, and multisections of Lefschetz fibrations*, arXiv:2610.01776v1, first posted 2026-10-01.
2. R. Inanç Baykur and Noriyuki Hamada, *Lefschetz fibrations with arbitrary signature*, Journal of the European Mathematical Society, online-first article; see in particular the proposition computing the divisibility of a regular fiber from monodromy.
3. R. Inanç Baykur and Kenta Hayano, *Multisections of Lefschetz fibrations and topology of symplectic 4-manifolds*, Geometry & Topology 20 (2016), 2335--2395.
4. J. Milnor and J. Stasheff, *Characteristic Classes*, for \(c_1\bmod2=w_2\) and the Wu formula.
