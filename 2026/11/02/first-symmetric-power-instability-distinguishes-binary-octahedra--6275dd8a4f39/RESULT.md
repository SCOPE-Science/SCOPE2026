# First symmetric-power instability distinguishes binary octahedral and icosahedral monodromy

## Finding
Let \(C\) be a smooth projective complex curve of genus \(2\), and let \(E\) be a stable rank-two bundle with \(\det E\cong\mathcal O_C\). Put \(X=\mathbb P_C(E)\) and \(S(X)=\bigoplus_{p\geq0}H^0(X,\operatorname{Sym}^p T_X)\), graded by \(p\). Let \(m(E)\) be the least positive integer \(k\) for which \(\operatorname{Sym}^k E\) is strictly semistable, or infinity if every symmetric power is stable.

**Claim.** If \(m(E)=4\), the unitary monodromy closure of \(E\) is the binary octahedral group \(2O\) (order \(48\)), and
\[
S(X)\cong\mathbb C[a,b,c]/(a^2+b^3+bc^3),
\quad(\deg a,\deg b,\deg c)=(9,6,4).
\]
If \(m(E)=6\), the unitary monodromy closure is the binary icosahedral group \(2I\) (order \(120\)), and
\[
S(X)\cong\mathbb C[a,b,c]/(a^2+b^3+c^5),
\quad(\deg a,\deg b,\deg c)=(15,10,6).
\]
Conversely, each stated monodromy group gives the respective value of \(m(E)\). Both possibilities occur on every genus-two curve.

## Assumptions and scope
The ground field is \(\mathbb C\); the bundle has rank two, degree zero, trivial determinant and is stable. The integer \(m(E)\) is the **first** strict-semistability index; merely knowing that \(\operatorname{Sym}^4 E\) or \(\operatorname{Sym}^6 E\) is strictly semistable without the earlier stability conditions is insufficient. The associated representations are unitary and their symmetric powers are polystable of slope zero, so any failure of stability is precisely strict semistability. Algebra generators are graded in symmetric-tensor degree, i.e. half their ordinary binary-form degree.

## Proof
**Unitary correspondence.** By the Narasimhan–Seshadri correspondence the bundle \(E\) is induced by an irreducible unitary representation \(\rho:\pi_1(C)\to SU(2)\). Let \(H\) be the compact closure of its image. Polystability and the correspondence imply \(\operatorname{Sym}^kE\) is stable exactly when \(\operatorname{Sym}^k\mathbb C^2\) is irreducible as an \(H\)-representation.

**First-invariant test.** The standard two-dimensional representation \(V\) is self-dual. Clebsch–Gordan gives
\[
\operatorname{End}(\operatorname{Sym}^kV)
\cong\bigoplus_{j=0}^{k}\operatorname{Sym}^{2j}V
\]
as \(SU(2)\)-representations. A unitary representation is irreducible if and only if its commuting-endomorphism dimension is one. Consequently the smallest \(k\geq1\) for which \(\operatorname{Sym}^kV\) reduces equals **half the smallest positive even degree of a nonconstant invariant** in \(\mathbb C[V]^H\).

**Classification of the holonomy.** The proper closed subgroups of \(SU(2)\) acting irreducibly on \(V\) are contained in the torus normalizer or are finite binary dihedral, tetrahedral, octahedral, or icosahedral groups. In the torus-normalizer and binary-dihedral cases, an invariant appears in degree at most four, hence \(m(E)\leq2\). For binary tetrahedral \(2T\), the first positive invariant degree is six; for binary octahedral \(2O\) it is eight; and for binary icosahedral \(2I\) it is twelve. These facts follow from the classical binary-polyhedral invariant-ring presentations, or their Molien series. The full group \(SU(2)\) has no nonconstant invariants and yields \(m(E)=\infty\). This proves that \(m(E)=4\) forces exactly \(2O\), and \(m(E)=6\) forces exactly \(2I\), with the converses. The relevant finite subgroups cannot be smaller than their stated binary groups because their first-invariant degrees would then be lower (classification applies to the actual closure).

**The graded algebra.** For this ruled surface the symmetric-tensor identification is
\[
S(X)_p\cong H^0(C,\operatorname{Sym}^{2p}E)
\cong(\operatorname{Sym}^{2p}V)^H.
\]
The last identification uses the fact that holomorphic sections of a unitary flat degree-zero bundle are parallel. Since \(-I\in2O,2I\), all invariant binary forms have even ordinary degree. Klein's binary-octahedral and binary-icosahedral invariant rings have presentations
\[
\mathbb C[V]^{2O}\cong\mathbb C[A,B,C]/(A^2+B^3+BC^3),
\quad(\deg_{V}A,\deg_{V}B,\deg_{V}C)=(18,12,8),
\]
\[
\mathbb C[V]^{2I}\cong\mathbb C[A,B,C]/(A^2+B^3+C^5),
\quad(\deg_{V}A,\deg_{V}B,\deg_{V}C)=(30,20,12).
\]
Dividing all polynomial degrees by two proves the two asserted presentations for \(S(X)\). Corresponding Hilbert series are
\[
\frac{1-t^{18}}{(1-t^9)(1-t^6)(1-t^4)}
\quad\text{and}\quad
\frac{1-t^{30}}{(1-t^{15})(1-t^{10})(1-t^6)}.
\]

**Existence.** Each finite group \(2O\) and \(2I\) is two-generated. Every genus-two surface group surjects onto a chosen two-generated finite group: map its first two standard \(a\)-generators to the chosen generators and both corresponding \(b\)-generators to the identity. The relation \([a_1,b_1][a_2,b_2]=1\) is satisfied. Composing with the faithful irreducible inclusion into \(SU(2)\) produces a stable bundle with exactly that monodromy and the specified first semistability index.

## Verification
The argument reduces the universal cases to compact-subgroup classification, the Clebsch–Gordan decomposition, and classical invariant-ring presentations. For reproducibility, verify the three generator weights against their relation weight: \(2\cdot9=3\cdot6=6+3\cdot4=18\); \(2\cdot15=3\cdot10=5\cdot6=30\). The inverse Hilbert-series leading term agrees with finite-group orders because \(18/(9\cdot6\cdot4)=1/12=4/48\) and \(30/(15\cdot10\cdot6)=1/30=4/120\); the factor four results from halving both binary-form degrees. These arithmetic checks do not substitute for the invariant-theory and holonomy proofs.

## Relationship to prior work
McPherson's 2026 treatment computes the low-first-instability cases and explicitly leaves the two higher types (rank-two destabilization of \(\operatorname{Sym}^4E\) and rank-three destabilization of \(\operatorname{Sym}^6E\)) for future computation. The present result covers precisely the cases in which the first instability occurs in these degrees, by identifying the *exhaustive* monodromy alternatives and then their invariant rings. Beauville and Liu discuss invariant-algebra descriptions for finite-monodromy constructions; the earlier examples and classical Klein invariant rings are used here, not claimed as new. Kim's work addresses strict semistability and the lower symmetric powers. The added assertion is the first-instability rigidity: no other genus-two stable degree-zero bundle can realize these two first-instability indices or different algebras there.

## Limitations
This does not classify all bundles for which \(\operatorname{Sym}^4E\) or \(\operatorname{Sym}^6E\) is strictly semistable if lower powers already fail stability. The binary invariant presentations and finite subgroup classification are classical inputs, not new results. The extension to nontrivial determinants requires a normalized reformulation. Independent mathematical audit and exhaustive priority assessment have not been performed.

## References
1. L. McPherson, *Computing S(X) for Ruled Surfaces Defined by Stable Bundles on Curves of Genus 2*, arXiv:2610.22573v1 (first public 2026-10-15), https://arxiv.org/abs/2610.22573 .
2. A. Beauville and J. Liu, *The algebra of symmetric tensors on smooth projective varieties*, arXiv:2309.12888, https://arxiv.org/abs/2309.12888 .
3. J.-S. Kim, *Stability of symmetric powers of vector bundles of rank two with even degree on a curve*, arXiv:2006.11733, https://arxiv.org/abs/2006.11733 .
4. Classical classification of finite subgroups of \(SU(2)\) and Klein's binary-polyhedral invariant rings (\(E_7\) and \(E_8\) Kleinian hypersurfaces).
