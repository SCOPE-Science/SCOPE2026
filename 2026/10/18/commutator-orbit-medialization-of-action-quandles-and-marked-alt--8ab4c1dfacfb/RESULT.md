# Commutator-orbit medialization of action quandles and marked alternating-orbit splitting

## Finding
**Theorem.** Let \(G\) be any group acting on the right on a nonempty set \(X\). On \(Q(X,G)=X\times G\) put Kai's quandle operation
\[
 (x,g)\triangleright(y,h)=(x^{g^{-1}h},h^{-1}gh).
\]
Let \(G'=[G,G]\). The group \(G'\) acts diagonally by \((x,g)\cdot a=(x^a,a^{-1}ga)\). The *universal medial quotient* of \(Q(X,G)\) (the initial medial quandle receiving a homomorphism from it) is precisely the induced orbit quandle:
\[
\boxed{Q(X,G)^{\mathrm{med}}\cong (X\times G)/G'.}
\]
In particular, orbit equivalence here is a quandle congruence, rather than merely an equivalence relation on elements.

For the natural action of \(G=S_n\) on \(X=[n]\), set \(Q_n=Q([n],S_n)\). For \(n\ge2\), its medial quotient consists of simultaneous \(A_n\)-relabeling orbits of *marked permutations*: a permutation together with one distinguished symbol. An \(S_n\)-orbit is specified by a partition \(\lambda\vdash n\) and the length \(d\) of the cycle containing the distinguished symbol; Kai established these original connected-component parameters. The single \(S_n\)-orbit splits into two medial-quotient points exactly when the partition \(\mu=\lambda\setminus\{d\}\) of the other cycles has **pairwise distinct odd parts** (the empty partition qualifies). Otherwise it gives one point.

Write \(m_1(\lambda)\) for the number of parts equal to one. The total cardinality admits two independent exact expressions:
\[
 \boxed{\left|Q_n^{\mathrm{med}}\right|=
 \sum_{\lambda\vdash n}\left|\{d:d\in\lambda\}\right|
 +\sum_{d=1}^n\#\{\mu\vdash n-d:\mu\text{ has distinct odd parts}\}
 =2\sum_{\substack{\lambda\vdash n\\n-\ell(\lambda)\text{ even}}}m_1(\lambda).}
\]
For \(n=1\), the cardinality is one, as \(A_1=S_1\). At \(n=2,3,4,5,6,7\), the exact values are \(4,6,10,16,24,36\).

## Assumptions and scope
The action need not be faithful or transitive and \(G\) need not be finite in the general theorem. The quandle convention is right self-distributivity with right translations \(s_y(z)=z\triangleright y\). A *medial quandle* satisfies \((a\triangleright b)\triangleright(c\triangleright d)=(a\triangleright c)\triangleright(b\triangleright d)\). A medial quotient is universal among quandle homomorphisms into medial quandles; it is not a quotient of the underlying group alone. In the specialized counting statement, \(n\) is any positive integer; \(S_n\) and \(A_n\) are the symmetric and alternating groups on \([n]\). Partition parts \(d\) are counted without repetition in the first sum but \(m_1(\lambda)\) counts each fixed point in the second sum.

## Proof
**1. A displacement-orbit lemma.** For any quandle \(T\), let \(D=\operatorname{Dis}(T)=\langle s_u s_v^{-1}:u,v\in T\rangle\), its displacement group, and \(N=[D,D]\). The standard medial-quandle criterion states that \(T\) is medial if and only if \(D\) is abelian. We show that \(N\)-orbits give the *universal* medial quotient. Because \(D\) is normal in \(\operatorname{Inn}(T)\) and \(N\) is characteristic in \(D\), \(N\) is normal in the inner group. If \(a\sim n(a)\) for \(n\in N\), then applying any \(s_b\) or its inverse preserves \(\sim\). If \(b\sim n(b)\), the right translations satisfy \(s_{n(b)}=n s_b n^{-1}\), hence \(s_{n(b)}s_b^{-1}\in N\). Therefore changing either operand within its \(N\)-orbit preserves the output orbit, so \(\sim\) is a quandle congruence. The quotient displacement group is the image of \(D\) in the induced permutation action on \(T/N\), in which every element of \(N=[D,D]\) acts trivially. Hence this image is abelian and the quotient is medial. Conversely, for any homomorphism \(f:T\to M\) to a medial quandle, the action of every commutator of displacements on \(f(T)\) is trivial: the displacements restrict to an abelian group on the medial subquandle \(f(T)\). Thus \(f\) is constant on each \(N\)-orbit and factors uniquely through \(T/N\). This proves the universal property.

**2. Evaluate the displacement group of the action quandle.** Define automorphisms \(\Psi_h(x,g)=(x^h,h^{-1}gh)\) and \(\zeta(x,g)=(x^g,g)\). From Kai's action formula one obtains
\[
 s_{(y,h)}=\zeta^{-1}\Psi_h,
\]
independently of \(y\), with \(\zeta\) commuting with all such translations (Kai, Lemma 3.9 and Corollary 3.12). In particular \(s_{(y,h)}s_{(z,1)}^{-1}=\Psi_h\). Every relative translation is likewise a product of these diagonal automorphisms. Consequently \(D=\Psi(G)\), and \([D,D]=\Psi(G')\). Its element-orbits are exactly the diagonal \(G'\)-orbits. Step 1 proves the first assertion, for every action regardless of kernel.

**3. Splitting of marked conjugacy orbits.** For \(n\ge2\), \(S_n'=A_n\), including the case \(n=2\), when \(A_2\) is trivial. A simultaneous \(S_n\)-orbit of a marked permutation \((x,\sigma)\) is determined by the cycle partition \(\lambda\) of \(\sigma\) and the length \(d\) of its cycle containing \(x\). As \(A_n\) has index two, that orbit splits into two \(A_n\)-orbits if and only if the stabilizer of \((x,\sigma)\) within \(S_n\) contains no odd permutation. This stabilizer is the centralizer of \(\sigma\) fixing \(x\). Commuting with \(\sigma\) and fixing one position on the distinguished cycle forces that entire cycle to be fixed pointwise. On the remaining cycles, the stabilizer permits their rotations and exchanges of cycles of equal lengths. A rotation of any even-length remaining cycle is odd; swapping two remaining cycles of the same odd length is odd. If every remaining cycle length is odd and no length repeats, each remaining rotation is even and no exchanges exist, so all stabilizer elements are even. This proves the exact splitting condition, including \(\mu=\varnothing\).

**4. Count the quotient.** There is one \(S_n\)-orbit for each \((\lambda,d)\) with \(d\) a distinct part of \(\lambda\). By Step 3, splitting pairs are in bijection with \(d\in\{1,\ldots,n\}\) and partitions of \(n-d\) into distinct odd parts. This proves the first expression. Independently, Burnside's lemma for the diagonal \(A_n\)-action on \([n]\times S_n\) gives
\[
 \left|Q_n^{\mathrm{med}}\right|=
 \frac{1}{|A_n|}\sum_{a\in A_n}\left|\operatorname{Fix}_{[n]}(a)\right|\left|C_{S_n}(a)\right|.
\]
A conjugacy class of cycle type \(\lambda\) has size \(n!/z_\lambda\) and centralizer size \(z_\lambda\), and contributes precisely when its permutations are even, i.e. \(n-\ell(\lambda)\) is even. Each such class contributes \((n!/|A_n|)m_1(\lambda)=2m_1(\lambda)\). This gives the second expression. For \(n=1\), the unique marked permutation gives one point. \(\square\)

## Verification
The standalone `quandle_medial_verify.py` uses only the Python standard library. It explicitly enumerates the diagonal \(A_n\)-orbits of marked permutations for \(2\le n\le7\), compares their splitting against the distinct-odd-parts criterion, and checks both enumerative expressions. It constructs the original quandle product independently from the defining permutation formula, tests quotient congruence exhaustively for \(n\le4\) and by generating changes of representatives for \(5\le n\le6\), and tests the four-variable medial identity on all quotient quadruples for \(n\le7\). It returns `VERIFY_OK` and the counts \(4,6,10,16,24,36\). Run `python3 quandle_medial_verify.py` after extracting the embedded artifacts. These finite computations check implementation and boundary cases; the all-group universal property and all-\(n\) enumeration rest on the proof.

## Relationship to prior work
Kai, *Quandles from Group Actions and a Cayley-type Embedding Theorem* (arXiv:2609.17438, submitted September 15, 2026), introduced the action-quandle construction, determined the inner group and diagonal connected components, and classified the \(S_n\)-orbits by marked cycle type. We rely on those structural antecedents. His Sections 3–4 do not give the universal medial quotient, the \(A_n\)-orbit splitting condition, or the cardinality formula. The general equivalence between mediality and an abelian displacement group is standard medial-quandle theory and is not claimed as new. Bardakov and Sangare, *Constructions and Automorphisms of Quandles* (arXiv:2610.18676, first submitted October 13, 2026), discuss medialization of conjugation quandles and compute its size for \(S_3\); their Section 5 does not cover the action construction or the marked alternating-orbit census. This latter work postdates the motivating source and the October 11 cohort cutoff and is included only as comparison literature. Classical alternating-class splitting for ordinary permutation conjugacy classes is known; the *pointed* stabilizer and its different criterion are essential here.

## Limitations
The orbit description need not be a smaller group-action quandle based merely on \(G/G'\); it retains pointed conjugation-orbit information. The theorem does not determine homology, full automorphism groups, or the number of medial quotients of arbitrary finite quandles. Equivalent formulations in unindexed literature remain possible. The quotient does not identify which other quandle invariants survive; only the universal medial image is determined.

## References
1. Ryoya Kai, *Quandles from Group Actions and a Cayley-type Embedding Theorem*, arXiv:2609.17438v3, Sections 3–4; initial public submission 2026-09-15. https://arxiv.org/abs/2609.17438
2. Valeriy G. Bardakov and Birama Sangare, *Constructions and Automorphisms of Quandles*, arXiv:2610.18676v1, Section 5; first submitted 2026-10-13 (comparison only). https://arxiv.org/abs/2610.18676
3. General criterion that a quandle is medial exactly when its displacement group is abelian; standard medial-quandle structure theory, invoked with a direct universal-property proof above.
