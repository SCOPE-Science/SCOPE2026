# Symplectic counterexamples to quadric-based elementarity

## Result

Faraco--Rungi define an elementary subgroup of \(\mathrm{PSL}(3,\mathbb R)\), up to finite index, by preservation of a projective conic, equivalently by fixing a point of
\[
\mathbb P\operatorname{Sym}^2(V^*)\quad\text{or}\quad \mathbb P\operatorname{Sym}^2(V),
\]
and prove in projective dimension \(2\) that non-elementarity is equivalent to Zariski density. Their Problem 1.6 asks whether the same quadric-based definition has this property in all projective dimensions.

The proposed equivalence already fails in the next dimension, and in every odd projective dimension thereafter.

**Theorem.** Let \(m\ge 2\), let \(V=\mathbb R^{2m}\) carry a nondegenerate alternating form \(\omega\), and let
\[
G_m=\operatorname{PSp}(V,\omega)<\operatorname{PSL}(V)=\operatorname{PSL}(2m,\mathbb R)
\]
be the standard projective symplectic group. Then:

1. no finite-index subgroup of \(G_m\) fixes a point of \(\mathbb P\operatorname{Sym}^2(V^*)\) or of \(\mathbb P\operatorname{Sym}^2(V)\); hence \(G_m\) is non-elementary for the quadric-based definition, even with the finite-index convention of Definition B.1;
2. \(G_m\) is a proper Zariski-closed subgroup of \(\operatorname{PSL}(2m,\mathbb R)\).

Consequently the implication
\[
\text{non-elementary}\Longrightarrow\text{Zariski-dense in }\operatorname{PSL}(n+1,\mathbb R)
\]
fails for every odd \(n=2m-1\ge 3\). In particular, \(n=3\) is the first possible failure dimension: Faraco--Rungi prove the equivalence for \(n=2\), whereas \(\operatorname{PSp}(4,\mathbb R)<\operatorname{PSL}(4,\mathbb R)\) is already a counterexample.

## General mechanism

The obstruction is representation-theoretic and is not specific to symplectic groups.

**Lemma.** Let \(H<\operatorname{SL}(V)\) be connected and semisimple, and let \(\bar H<\operatorname{PSL}(V)\) be its projective image. If a finite-index subgroup of \(\bar H\) fixes a projective quadratic form, then \(H\) has a nonzero invariant vector in \(\operatorname{Sym}^2(V^*)\) or in \(\operatorname{Sym}^2(V)\).

**Proof.** A finite-index subgroup of a connected topological group is dense after taking ordinary closure: the closure still has finite index, hence is open, and connectedness forces that closure to be the whole group. Since a projective-point stabilizer is closed, it is therefore enough to consider a projective quadratic form fixed by all of \(H\).

Suppose \([q]\in\mathbb P\operatorname{Sym}^2(V^*)\) is fixed. Then
\[
h\cdot q=\chi(h)q
\]
for a continuous one-dimensional character \(\chi:H\to\mathbb R^*\). Its differential is a Lie-algebra character. Because the Lie algebra of a semisimple group equals its commutator algebra, that differential vanishes. Connectedness then gives \(\chi\equiv1\), so \(q\) is genuinely \(H\)-invariant. The same argument applies to \(\operatorname{Sym}^2(V)\). \(\square\)

Thus a proper connected semisimple projective subgroup whose defining representation has no symmetric invariant tensor is automatically a counterexample to quadric-based detection of Zariski density. The symplectic standard representation is the simplest such family: it carries a canonical invariant tensor in \(\Lambda^2(V^*)\), not in \(\operatorname{Sym}^2(V^*)\).

## Why the symplectic group preserves no quadric

The real symplectic group is connected and semisimple, so the preceding lemma applies to its projective image. It remains to prove
\[
\operatorname{Sym}^2(V^*)^{\operatorname{Sp}(V,\omega)}=0.
\]
The symplectic group acts transitively on \(V\setminus\{0\}\): any nonzero vector can be extended to a symplectic basis, and a change between two such bases is symplectic. If a quadratic form \(q\) were invariant, then \(q(v)\) would have the same value for every nonzero \(v\). But \(v\) and \(2v\) lie in the same orbit, while homogeneity gives
\[
q(2v)=4q(v).
\]
Hence \(q(v)=0\) for every nonzero \(v\), so \(q=0\).

The symplectic form identifies the standard module with its dual via
\[
v\longmapsto \omega(v,\cdot),
\]
so the same conclusion holds for \(\operatorname{Sym}^2(V)\). The lemma therefore rules out every quadric, including degenerate quadrics and quadrics preserved only after passage to finite index.

## Why the subgroup is not Zariski-dense

Before projectivisation, \(\operatorname{Sp}(2m,\mathbb R)\) is the real algebraic subgroup of \(\operatorname{SL}(2m,\mathbb R)\) defined by
\[
g^{T}Jg=J
\]
for a symplectic matrix \(J\). Its projective image is therefore an algebraic subgroup of \(\operatorname{PSL}(2m,\mathbb R)\). It is proper for \(m\ge2\), for example by the dimension comparison
\[
\dim\operatorname{Sp}(2m,\mathbb R)=m(2m+1)
<4m^2-1=\dim\operatorname{PSL}(2m,\mathbb R).
\]
Hence its Zariski closure is itself and is strictly smaller than the ambient projective linear group.

## Discrete surface-group counterexamples in projective dimension three

The phenomenon is not restricted to using a positive-dimensional Lie subgroup as the counterexample. Audibert proved that \(\operatorname{Sp}(4,\mathbb Z)\) contains Zariski-dense surface subgroups. Let \(\Gamma<\operatorname{Sp}(4,\mathbb Z)\) be such a surface subgroup and project it to \(\operatorname{PSL}(4,\mathbb R)\). Its Zariski closure is \(\operatorname{PSp}(4,\mathbb R)\), not \(\operatorname{PSL}(4,\mathbb R)\).

If a finite-index subgroup of \(\Gamma\) fixed a projective quadratic form, then its Zariski closure would fix the same projective point. Finite-index subgroups of a Zariski-dense subgroup of a connected algebraic group remain Zariski-dense, so \(\operatorname{PSp}(4,\mathbb R)\) would fix a quadric, contradicting the theorem above. Thus there are discrete surface-group images in \(\operatorname{PSL}(4,\mathbb R)\) that are non-elementary for the proposed definition but not ambient-Zariski-dense.

## Interpretation

The dimension-two equivalence works because the proper algebraic subgroups relevant there are detected by invariant conics or their degenerations. In higher dimension, preservation of a quadratic form detects orthogonal-type structure but cannot detect all proper algebraic subgroups. Symplectic type provides the first obstruction: the subgroup is geometrically distinguished by an alternating form, while the proposed elementary invariant only probes symmetric degree-two tensors.

This suggests that any higher-dimensional replacement for the dimension-two criterion must allow a richer collection of algebraic invariants than quadrics alone.

## Limitations

This result gives a negative answer to the proposed equivalence in Problem 1.6 and an infinite family of counterexamples, but it does not classify elementary subgroups of \(\operatorname{PSL}(n+1,\mathbb R)\) in higher dimension. It also does not determine in which even projective dimensions analogous counterexamples exist, nor does it propose a complete substitute invariant that detects every proper algebraic subgroup.

The representation-theoretic ingredients used in the proof--semisimple groups having no nontrivial one-dimensional infinitesimal characters, transitivity of the standard symplectic action on nonzero vectors, and the algebraicity of \(\operatorname{Sp}\)--are classical. The new claim is the application of these facts to Faraco--Rungi's newly posed quadric-based characterisation problem, including the sharp first failure at projective dimension three and the surface-group corollary.

## References

1. G. Faraco and N. Rungi, *Branched real projective structures on surfaces and geometrisation of representations*, arXiv:2609.18436 (2026), especially Definition B.1, Theorem B.2, and Problem 1.6. https://arxiv.org/abs/2609.18436
2. J. Audibert, *Maximal representations in lattices of the symplectic group*, arXiv:2307.06791 (2023). https://arxiv.org/abs/2307.06791
