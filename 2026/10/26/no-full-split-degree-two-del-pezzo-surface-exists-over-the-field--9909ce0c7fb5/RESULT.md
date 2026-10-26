# No full split degree-two del Pezzo surface over \(\mathbb F_{37}\)

## Finding

**Theorem.** Let \(S\) be any split smooth del Pezzo surface of degree two defined over \(\mathbb F_{37}\). Among its \(37^2+8\cdot37+1=1666\) rational points there is at least one point outside the union of its 56 exceptional curves. Consequently there is **no full split degree-two del Pezzo surface over \(\mathbb F_{37}\)**. For odd prime powers the upper bound \(q\le37\) of Knecht and Reyes can therefore be sharpened to \(q\le31\).

A necessary incidence inequality for any full split degree-two del Pezzo surface in odd characteristic at least five is
\[
 (q-24)^2+\#Q(\mathbb F_q)\le169,
\]
provided the quadruple-point bound \(h\le21\) holds for the branch quartic. It does hold in characteristic \(37\). We make no blanket claim about characteristics in which the tame-lifting argument does not apply.

## Assumptions and scope

A degree-two del Pezzo surface is **split** if all 56 geometric exceptional \((-1)\)-curves are defined over the ground field. It is **full** if every rational point lies on at least one such curve. In characteristic distinct from two, its anticanonical map is a double cover of \(\mathbb P^2\) branched over a smooth plane quartic \(Q\). The 56 exceptional curves map in pairs to its 28 bitangents. Since all exceptional curves are rational, all 28 bitangents are rational in the split case.

Write \(h,e,f\) for the numbers of geometric points where, respectively, exactly four, three, and two distinct bitangents meet. No point lies on more than four bitangents. For rational bitangents over a finite field, every pairwise intersection is rational, and these counts are integers. Write \(N=\#Q(\mathbb F_q)\).

## Proof

**Step 1: Pair-incidence normalization.** Every pair of 28 distinct lines meets exactly once in \(\mathbb P^2\). Counting pairs at all intersections gives
\[
 6h+3e+f=\binom{28}{2}=378.
\]
Since \(f\ge0\), one has \(3e\le378-6h\), so
\[
 6h+2e\le 252+2h.\tag{1}
\]

**Step 2: The necessary fullness equation.** Suppose \(S\) is full. Then every rational point of \(Q\) must lie on a bitangent: its unique point upstairs must lie on an exceptional curve. Let \(U\) be the union of the 28 rational bitangent lines, regarded as a set of rational points. Inclusion-exclusion by incidence multiplicity gives
\[
 \#U=28(q+1)-3h-2e-f.
\]
At every point of \(U\) outside \(Q\), the double-cover fiber consists of two rational points, because the point lies on a rational bitangent whose two exceptional components are defined over \(\mathbb F_q\). On \(Q\) the fiber consists of one rational point. Fullness therefore forces
\[
 \#S(\mathbb F_q)=2\#U-N=56q-700+6h+2e-N.
\]
The split surface is a blowup of seven \(\mathbb F_q\)-points of \(\mathbb P^2\), whence
\[
 \#S(\mathbb F_q)=q^2+8q+1.
\]
Equating these yields the necessary identity established by Knecht and Reyes:
\[
 (q-24)^2+N=6h+2e-125.\tag{2}
\]

**Step 3: The geometric cap on quadruple points in characteristic 37.** For a smooth plane quartic over an algebraically closed field of characteristic not two, the four-concurrent-biangents criterion of Kowalevskaya/Kuwata associates a bielliptic involution of the quartic to each fourfold point. The involution has that point as its isolated fixed point in the canonical plane, so different fourfold points yield different involutions. Hence \(h\) is at most the number of involutions of the quartic.

For characteristic \(37\), Dolgachev--Martin prove that automorphism groups of smooth plane quartics are tame and that such actions lift to characteristic zero. The number of involutions of the lifted curve is the same as in characteristic \(37\). The classical characteristic-zero genus-three bound is 21 (cf. Janasz--Pokora--Zieliński, Proposition 3.7). Thus
\[
 h\le21\qquad\text{in characteristic }37.\tag{3}
\]
This uses the algebraic characteristic-not-two correspondence, not an unsupported assertion that the complex line-arrangement proposition directly applies to a finite field.

**Step 4: Numerical contradiction.** Combining (1) and (3) yields
\[
 6h+2e\le252+2\cdot21=294.
\]
Equation (2) for \(q=37\) therefore gives \(169+N\le169\), or \(N=0\). But the Hasse--Weil bound for the smooth genus-three quartic gives
\[
 N\ge37+1-6\sqrt{37}\gt1.
\]
The strict inequality is exact because \(37^2\gt36\cdot37\). Therefore \(N\ge2\), a contradiction. Equivalently, fullness would require \(h\ge22\), which contradicts (3). This proves the theorem.

## Verification

A standalone integer-only auxiliary program `verify.py` checks \(\binom{28}{2}=378\), all nonnegative integer incidence triples satisfying \(6h+3e+f=378\) and \(h\le21\), the resulting maximal value \(6h+2e=294\), and the exact integral inequality \(38-6\sqrt{37}\gt1\). It verifies the numerical implications, not the cited geometric correspondence or the positive-characteristic lifting theorems. The latter are mathematical premises explicitly identified in the proof.

## Relationship to prior work

Knecht and Reyes (2015), Equation (6) and Theorem 1.5, obtain the necessary fullness equation and leave the field with 37 elements among five possible unresolved fields; their general bound is \(q\le37\). Kuwata (2005) proves the involution/concurrent-bitangents correspondence over fields of characteristic different from two. Janasz, Pokora and Zieliński (first posted 2023; revised 2024), Proposition 3.7, provide the sharp 21-point bound over the complex numbers. Dolgachev and Martin (2024), Corollary 4.3 and Section 4.5, give the tame-lifting input needed to transfer the involution count to characteristic 37.

The present result **combines** these prior geometric and arithmetic statements to eliminate the specific field left open by the earlier full-del-Pezzo classification. It does not claim a new general theorem about automorphism groups, bitangents, or the 2015 incidence equation. Searches of the relevant full texts did not locate the stated exclusion.

## Limitations

The conclusion is a nonexistence theorem for **full split** degree-two del Pezzo surfaces over \(\mathbb F_{37}\). It neither excludes nonsplit degree-two del Pezzo surfaces nor classifies the four remaining fields listed in Knecht--Reyes. The proof depends on the characteristic-not-two Kowalevskaya/Kuwata correspondence and the tame-lifting theorem. Full-text retrieval of the Kuwata paper was unavailable; targeted indexed excerpts confirmed its characteristic assumption and relevant theorem, but this leaves a bibliographic inspection risk. Literature searches cannot establish absolute uniqueness of the synthesis. No independent scientific audit has been performed.

## References

1. Amanda Knecht and Kristofer Reyes, *Full Degree Two del Pezzo Surfaces over Small Finite Fields*, arXiv:1510.04621, first public 15 October 2015, especially §2, Equation (6), Theorem 1.5 and Lemma 2.1. https://arxiv.org/abs/1510.04621
2. Masato Kuwata, *Twenty-eight double tangent lines of a plane quartic curve with an involution and the Mordell-Weil lattices*, Commentarii Mathematici Universitatis Sancti Pauli 54 (2005), 17--32. https://rikkyo.repo.nii.ac.jp/record/8706/files/AA00610867_54-01_02.pdf
3. Marek Janasz, Piotr Pokora and Marcin Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, Proposition 3.7. https://arxiv.org/pdf/2308.16514
4. Igor Dolgachev and Gebhard Martin, *Automorphisms of del Pezzo surfaces in odd characteristic*, J. London Math. Soc. (2024), DOI: 10.1112/jlms.12905, especially Corollary 4.3 and §4.5. https://doi.org/10.1112/jlms.12905
