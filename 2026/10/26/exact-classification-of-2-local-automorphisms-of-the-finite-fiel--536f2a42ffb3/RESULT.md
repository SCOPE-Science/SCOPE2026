# Exact classification of 2-local automorphisms of the finite-field affine Lie algebra

## Finding

Let \(k=\mathbb F_q\) and let \(L=ke\oplus kf\) be the two-dimensional nonabelian Lie algebra with \([e,f]=f\). Every 2-local automorphism \(\Phi:L\to L\) is uniquely determined by a permutation \(\sigma\) of \(k\) and a scalar \(\kappa\in k^\times\), via
\[
\Phi(ae+bf)=ae+a\sigma(b/a)f\quad(a\ne0),\qquad \Phi(bf)=\kappa bf.
\]
Consequently, there are exactly \(q!(q-1)\) 2-local automorphisms, of which exactly \(q(q-1)\) are genuine automorphisms. Every 2-local automorphism is a genuine automorphism if and only if \(q=2\).

## Assumptions and scope

The field \(k=\mathbb F_q\) is finite. A 2-local automorphism means an arbitrary map \(\Phi:L\to L\), not assumed additive or linear, such that for each pair \(u,v\in L\) there is one Lie algebra automorphism \(\alpha_{u,v}\) satisfying \(\Phi(u)=\alpha_{u,v}(u)\) and \(\Phi(v)=\alpha_{u,v}(v)\). The result concerns this single two-dimensional solvable, nonnilpotent Lie algebra and does not classify maps over infinite fields or on higher-dimensional Lie algebras.

## Proof

First determine the ordinary automorphism group. The derived ideal is \([L,L]=kf\), so it is characteristic. Every automorphism therefore has \(\alpha(f)=df\) and \(\alpha(e)=ae+bf\), with \(a,d\ne0\). The identity \([\alpha(e),\alpha(f)]=\alpha(f)\) gives \(ad=d\), hence \(a=1\). Conversely, every map
\[
\alpha_{u,d}(e)=e+uf,\qquad \alpha_{u,d}(f)=df,\qquad u\in k,\ d\in k^\times,
\]
is an automorphism. Thus \(|\operatorname{Aut}(L)|=q(q-1)\), and its action on coordinates is \(ae+bf\mapsto ae+(au+bd)f\).

Let \(\Phi\) be 2-local. Applying the definition to the pair \((z,0)\) shows that \(\Phi\) preserves the \(e\)-coordinate. Applying it to \((z,\lambda z)\) and using linearity of the witnessing automorphism gives \(\Phi(\lambda z)=\lambda\Phi(z)\) for all \(z\in L\) and \(\lambda\in k\). Write \(\Phi(ae+bf)=ae+F(a,b)f\). Define \(\sigma(s)=F(1,s)\) for \(s\in k\), and \(\kappa=F(0,1)\). Homogeneity gives
\[
\Phi(ae+asf)=ae+a\sigma(s)f\quad(a\ne0),\qquad \Phi(bf)=\kappa bf.
\]
The pair \((0,f)\) forces \(\kappa\ne0\).

For distinct \(s,t\in k\), apply 2-locality to \(e+sf\) and \(e+tf\). A single witness \(\alpha_{u,d}\) must satisfy \(\sigma(s)=u+sd\) and \(\sigma(t)=u+td\), so
\[
d=\frac{\sigma(t)-\sigma(s)}{t-s}\ne0.
\]
Therefore \(\sigma(s)\ne\sigma(t)\) whenever \(s\ne t\). Since \(k\) is finite, \(\sigma\) is a permutation. This proves necessity of the displayed parameterization.

Conversely, choose any permutation \(\sigma:k\to k\) and any \(\kappa\in k^\times\), and define \(\Phi\) by the displayed formulas. For two nonvertical vectors with distinct slopes \(s,t\), choose
\[
d=\frac{\sigma(t)-\sigma(s)}{t-s},\qquad u=\sigma(s)-sd.
\]
The permutation property makes \(d\ne0\), and \(\alpha_{u,d}\) matches both vectors. For a nonvertical vector of slope \(s\) paired with a nonzero vertical vector, choose \(d=\kappa\) and \(u=\sigma(s)-s\kappa\). Pairs of dependent vectors are matched by an automorphism matching one nonzero member, because \(\Phi\) is homogeneous on each line; the zero vector causes no extra condition. Two vertical vectors are dependent. Thus every such parameter pair defines a 2-local automorphism.

The parameters are unique: the values on \(e+sf\) recover \(\sigma(s)\), and the value on \(f\) recovers \(\kappa\). Hence there are \(q!(q-1)\) maps. An actual automorphism has \(\sigma(s)=u+ds\) and \(\kappa=d\), giving exactly \(q(q-1)\) maps. If \(q=2\), the only nonzero scalar is \(1\), and every permutation of \(\mathbb F_2\) is affine, so the two counts coincide and every 2-local automorphism is an automorphism. If \(q>2\), choose \(\sigma(s)=s\) and \(\kappa\ne1\); this gives a 2-local automorphism that is not an automorphism. The boundary is sharp.

## Verification

The proof is algebraic and applies to every finite field, including characteristic two. The only finite-field step is that injectivity of \(\sigma:k\to k\) implies surjectivity. The count follows from the bijection between the maps and \(\operatorname{Sym}(k)\times k^\times\). No finite enumeration is used as proof. Independent audit and independent validation have not been performed.

## Relationship to prior work

The 2024 literature studies local and 2-local maps on other finite-dimensional Lie structures. Sheng, Liu, and Liu treat model filiform Lie superalgebras over characteristic-zero fields and prove that their linear 2-local automorphisms are automorphisms; their object and linearity assumption differ from the present non-linear finite-field classification. Khudoyberdiyev and Jumaniyozov study local derivations and automorphisms on nilpotent Lie algebras, whereas \(L\) is solvable but not nilpotent. A 2026 paper of Bahturin and Olshanskii studies exact relatively-free-algebra growth for this same two-dimensional affine Lie algebra, a different invariant that does not imply the present classification. Searches for equivalent formulations and exact counts did not locate a source stating the permutation-and-vertical-scale parameterization; this is not by itself a proof of novelty, and the residual risks are recorded in the review.

## Limitations

The result is specific to the two-dimensional nonabelian Lie algebra over finite fields. Finiteness is essential for turning injectivity of the slope map into a permutation and for the exact factorial count. No claim is made for infinite fields, higher-dimensional solvable Lie algebras, or linear-only 2-local maps. The broader literature on 2-local maps is not exhausted.

## References

1. Yuqiu Sheng, Wende Liu, and Yang Liu, “Local Automorphisms and Local Superderivations of Model Filiform Lie Superalgebras,” *Journal of Mathematics* (2024), DOI: 10.1155/2024/6650997. First published 27 March 2024.
2. Abror Khudoyberdiyev and Doston Jumaniyozov, “Local derivations and automorphisms of nilpotent Lie algebra,” arXiv:2405.04209 (2024), first submitted 7 May 2024.
3. Yuri Bahturin and Alexander Olshanskii, “Locally finite varieties of nonassociative algebras,” arXiv:2603.09655v1 (2026), first public 10 March 2026; cited only for the distinct relatively-free-growth result on the same algebra.
