# Closed-graph repair and optimal bounds for a resolution-of-identity g-fusion criterion
## Finding
Let \(H\) be a Hilbert space, let \(W_j\subseteq H\) be closed subspaces, let \(v_j>0\) be bounded weights, and let \(\Lambda_j\in\mathcal B(H,H_j)\). Assume the two hypotheses printed in Ghosh and Samanta, Theorem 3.4: for every \(f\in H\), the sequence \((\Lambda_jP_{W_j}f)_j\) is square-summable, and \(\{v_jP_{W_j}\Lambda_j^*\Lambda_jP_{W_j}\}_j\) is a resolution of the identity.

Define \(U:H	o\bigoplus_j H_j\) by \(Uf=(\Lambda_jP_{W_j}f)_j\), put \(B_0=\|U\|^2\), and put \(M=\sup_j v_j\). Then
\[
rac1{B_0}\|f\|^2\le \sum_j v_j^2\|\Lambda_jP_{W_j}f\|^2\le M\|f\|^2\qquad(f\in H).
\]
These are the best universal bounds determined only by \((B_0,M)\), under the necessary compatibility condition \(MB_0\ge1\).

## Assumptions and scope
The index set is countable as in the source convention. No lower bound on the positive weights is assumed. The phrase “resolution of the identity” is used in the source sense: the operator series converges unconditionally to the identity on every vector. The result concerns the literal hypotheses of Theorem 3.4 and does not assert optimal frame bounds for a specific family when additional structure is known.

## Proof
For every \(f\in H\), hypothesis (I) says exactly that \(Uf\in\bigoplus_jH_j\). The map \(U\) is linear and everywhere defined. If \(f_n	o f\) in \(H\) and \(Uf_n	o y\) in the Hilbert direct sum, continuity of each coordinate projection gives
\[
y_j=\lim_n\Lambda_jP_{W_j}f_n=\Lambda_jP_{W_j}f.
\]
Hence \(y=Uf\), so the graph of \(U\) is closed. The closed graph theorem implies that \(U\) is bounded, and therefore
\[
\sum_j\|\Lambda_jP_{W_j}f\|^2\le B_0\|f\|^2.
\]
This supplies the uniform constant that is used, but not justified, in the printed proof.

Write \(a_j=\|\Lambda_jP_{W_j}f\|^2\). Taking the inner product of the resolution identity with \(f\) yields
\[
\|f\|^2=\sum_j v_j a_j.
\]
All terms are nonnegative. Cauchy–Schwarz gives
\[
\|f\|^4=\left(\sum_jv_ja_j\right)^2
\le \left(\sum_ja_j\right)\left(\sum_jv_j^2a_j\right)
\le B_0\|f\|^2\sum_jv_j^2a_j,
\]
which proves the lower bound \(1/B_0\). For the upper bound,
\[
\sum_jv_j^2a_j\le M\sum_jv_ja_j=M\|f\|^2.
\]
The same identity and the unweighted Bessel estimate imply \(1\le MB_0\) whenever \(H
e\{0\}\).

Sharpness is scalar. For the lower bound, take \(H=\mathbb C\), one active atom with \(\|\Lambda_1\|^2=B_0\) and weight \(v_1=1/B_0\); if \(M>1/B_0\), add a zero atom carrying weight \(M\). The resolution identity holds and the weighted energy is exactly \((1/B_0)\|f\|^2\).

For the upper bound, if \(MB_0=1\), the same one-atom example has weighted energy \(M\|f\|^2\). If \(MB_0>1\), choose \(0<\varepsilon<1/B_0\) and two scalar atoms whose squared operator norms are
\[
q_1=\frac{1-\varepsilon B_0}{M-\varepsilon},\qquad
q_2=\frac{MB_0-1}{M-\varepsilon}.
\]
Then \(q_1+q_2=B_0\), \(Mq_1+\varepsilon q_2=1\), and the weighted energy coefficient is
\[
M^2q_1+\varepsilon^2q_2=M-\varepsilon(MB_0-1),
\]
which tends to \(M\) as \(\varepsilon\downarrow0\). Thus no smaller universal upper constant is possible.

## Verification
The proof uses only the closed graph theorem, the defining resolution identity, Cauchy–Schwarz, and explicit one- and two-atom scalar constructions. The scalar sharpness formulas were algebraically checked by substitution. No finite computation is used to justify an infinite-dimensional statement.

## Relationship to prior work
Ghosh and Samanta, Theorem 3.4, states the qualitative g-fusion-frame conclusion under the same two hypotheses. Its printed proof applies the pointwise constant from hypothesis (I) as though it were uniform and gives an upper estimate corresponding to \(M^2B_0\). The closed-graph argument above repairs that quantifier step. The resolution identity then gives the sharper upper estimate \(M\), while Cauchy–Schwarz gives \(1/B_0\); the scalar models show that these constants are universally sharp.

A later Hilbert \(C^*\)-module paper by Nhari and Rossafi develops an analogous resolution framework, but the checked material does not state this Hilbert-space closed-graph repair together with the sharp pair \((1/B_0,M)\).

## Limitations
The universal bounds use only \(B_0\) and \(M\); a particular family may have better optimal frame bounds. The sharp upper bound for \(MB_0>1\) is a supremal universal bound, approached by a two-atom family as \(\varepsilon\downarrow0\), rather than necessarily attained at fixed \((B_0,M)\). An unindexed earlier observation of the same repair or constants cannot be excluded.

## References
1. P. Ghosh and T. K. Samanta, “Generalized atomic subspaces for operators in Hilbert spaces,” *Mathematica Bohemica* 147 (2022), 325–345. DOI: 10.21136/MB.2021.0130-20. Preprint: arXiv:2102.01965v1.
2. F.-D. Nhari and M. Rossafi, “G-atomic submodules for operators in Hilbert C*-modules,” *Journal of Mathematical and Computational Science* 11 (2021), 8146–8172. DOI: 10.28919/jmcs/6783.
