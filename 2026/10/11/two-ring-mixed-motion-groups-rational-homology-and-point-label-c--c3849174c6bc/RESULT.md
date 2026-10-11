# Two-ring mixed-motion groups: rational homology and point-label characters

## Finding

For each integer \(k\ge1\), let \(M_{2,k}\) denote the mixed configuration space of two unordered, pairwise unlinked Euclidean circles in the interior of a three-ball together with \(k\) mutually distinct, ordered points avoiding the circles. Put \(G_k=\pi_1(M_{2,k})\). There is a natural algebraic action of \(S_k\) on the split fundamental-group presentation, permuting point factors and fixing the ring-motion subgroup.

For a permutation \(\pi\in S_k\), write \(m_j(\pi)\) for its number of cycles of length \(j\), and define polynomials

\[
F_\pi(t)=\prod_{j\ge1}\left(1+2(-1)^{j-1}t^j\right)^{m_j(\pi)},\qquad
E_\pi(t)=\prod_{j\ge1,\;j\text{ even}}\left(1-2t^j\right)^{m_j(\pi)}.
\]

The full rational group-homology character is

\[
\boxed{\sum_{d\ge0}\operatorname{tr}\!\left(\pi\mid H_d(G_k;\mathbb Q)\right)t^d
=\left(t+\frac12\right)F_\pi(t)+\frac12E_\pi(t).}
\]

At the identity permutation this gives the complete rational Betti polynomial

\[
P_{G_k}(t)=\frac{1+(1+2t)^{k+1}}2,
\qquad
\beta_0=1,\quad
\beta_d=2^{d-1}\binom{k+1}{d}\ (1\le d\le k+1),\quad
\beta_d=0\ (d>k+1).
\]

For example the Betti vector for \(k=2\) is \((1,3,6,4)\). The complete formula, not just the identity specialization, determines the character of the \(S_k\)-module in every homological degree.

## Assumptions and scope

All homology groups are ordinary *group homology with rational coefficients*, equivalently homology of a classifying space \(BG_k\). No asphericity of the mixed configuration space \(M_{2,k}\) is assumed or used. The action on \(G_k\) is the algebraic action induced by permuting the \(k\) free factors in the split presentation below; it commutes with the diagonal ring-motion action. The formula applies to every \(k\ge1\), every \(\pi\in S_k\) and every degree \(d\ge0\). Empty products have value one.

## Proof

**1. The extension and its rational action.** Makri's Proposition 3.8 provides
\[
G_k\cong N_k\rtimes B,\qquad N_k=(F_2)^k,\qquad B=LB_2.
\]
Brendle--Hatcher's presentation, reproduced in Makri's Theorem 2.4, gives \(B\cong\mathbb Z*C_2=\langle\sigma,\rho\mid\rho^2=1\rangle\): all mixed relations involve at least three circles and disappear for two. The explicitly given basis-conjugating action of \(\sigma\) and permutation action of \(\rho\) both induce on \(V=H_1(F_2;\mathbb Q)\cong\mathbb Q^2\) the transposition \(J(e_1)=e_2,\;J(e_2)=e_1\). By rational Künneth,
\[
H_q(N_k;\mathbb Q)\cong\bigoplus_{I\subseteq\{1,\ldots,k\},\;|I|=q}V^{\otimes I}
\quad(0\le q\le k),
\]
with no homology in other degrees. Both \(\sigma\) and \(\rho\) act as \(J^{\otimes q}\) on each summand. A point-factor permutation acts on these graded tensor factors with the Koszul sign.

**2. Homology of the free-product base with coefficients.** For a rational \(B\)-module \(W\) on which \(\sigma\) and \(\rho\) both act through one involution \(J_W\), put \(W_+=\ker(J_W-1)\) and \(W_-=\ker(J_W+1)\). The Mayer--Vietoris sequence for \(B=\mathbb Z*C_2\) over the trivial amalgamated subgroup, together with rational acyclicity of \(C_2\) in positive degrees, gives
\[
H_0(B;W)=W_+,\qquad
0\longrightarrow W_+\longrightarrow H_1(B;W)\longrightarrow W_-\longrightarrow0,
\qquad H_p(B;W)=0\ (p\ge2).
\]
Indeed \(H_1(\mathbb Z;W)=W_+\), while the kernel of the edge map \(W\to H_0(\mathbb Z;W)\oplus H_0(C_2;W)\cong W_+\oplus W_+\) is \(W_-\). These exact sequences are natural for every operator commuting with \(J_W\); hence its trace on \(H_1(B;W)\) equals its trace on \(W_+\oplus W_-=W\), even if no canonical splitting is selected.

**3. Collapse and the degree shift.** The rational Lyndon--Hochschild--Serre homology spectral sequence for \(N_k\to G_k\to B\) has
\[
E^2_{p,q}=H_p(B;H_q(N_k;\mathbb Q)),\qquad p\in\{0,1\}.
\]
It has no possible differentials and is natural for \(S_k\). Traces are additive in the resulting filtration. Write \(A_q(\pi)\) for the trace on \(H_0(B;H_q(N_k))\) and \(T_q(\pi)\) for the trace on \(H_q(N_k)\). Step 2 gives \(\operatorname{tr}(\pi|H_1(B;H_q(N_k)))=T_q(\pi)\), so
\[
\sum_{d\ge0}\operatorname{tr}(\pi|H_d(G_k;\mathbb Q))t^d
=\sum_{q\ge0}A_q(\pi)t^q+t\sum_{q\ge0}T_q(\pi)t^q.
\]

**4. Cycle enumeration, including signs.** A permutation contributes to the trace on \(H_q(N_k)\) only on subsets \(I\) that are unions of whole cycles of \(\pi\). For a selected cycle of length \(j\), the graded tensor permutation has Koszul sign \((-1)^{j-1}\), and the unsigned trace on \(V^{\otimes j}\) equals \(2\). Thus \(\sum_qT_q(\pi)t^q=F_\pi(t)\). The projector onto the plus-eigenspace of \(J^{\otimes q}\) is \(\tfrac12(1+J^{\otimes q})\). On a selected \(j\)-cycle, the trace of the tensor-permutation composed with \(J^{\otimes j}\) equals \(\operatorname{tr}(J^j)\), namely \(0\) for odd \(j\) and \(2\) for even \(j\); the same Koszul sign remains. Therefore
\[
\sum_q A_q(\pi)t^q=\tfrac12(F_\pi(t)+E_\pi(t)).
\]
Substitution into Step 3 proves the boxed character identity. For the identity permutation \(F_{\mathrm{id}}=(1+2t)^k\) and \(E_{\mathrm{id}}=1\), whence the Betti formula and vanishing above degree \(k+1\). Every step is valid for all \(k\), not by finite extrapolation.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. It independently enumerates permutation-stable supports and binary tensor-basis assignments for every one of the \(874\) permutations in \(S_0,\ldots,S_6\), including the signed trace of the swap involution; it checks the resulting homology characters against the separate cycle-factor product and the identity Betti formula. The exact output is `VERIFY_OK 874 permutations in 0<=k<=6`. The all-parameter proof is symbolic; finite checks verify conventions and arithmetic but do not establish infinite quantifiers.

## Relationship to prior work

Makri, *Mixed configuration spaces, fixed points and Loop braid groups* (arXiv:2610.04382v1, first public 2026-10-03), proves the fibration and split presentation \(G_k\cong(F_2)^k\rtimes LB_2\), but does not derive rational Betti numbers or point-permutation characters. Brendle--Hatcher construct and present ring-motion groups; their presentation provides \(LB_2\cong\mathbb Z*C_2\), not the cohomology of the mixed point-motion extension. Jensen--McCammond--Meier calculate the integral cohomology of the **pure ring-motion** group \(P\Sigma_n\), not this extension with ordered point factors. An exact character formula potentially implicit in other computations cannot be completely excluded by indexing searches; explicit implication comparisons are recorded in the accompanying scientific review.

## Limitations

This is rational **group** homology; it makes no claim about \(H_*(M_{2,k};\mathbb Q)\), integral torsion, cup products, multiplicative cohomology, higher homotopy, or extensions to three or more circles. The \(S_k\)-action is specified through the split algebraic presentation. No independent audit has been conducted.

## References

1. S. Makri, *Mixed configuration spaces, fixed points and Loop braid groups*, arXiv:2610.04382v1 (first public October 3, 2026), especially Theorem 2.4, Proposition 3.8 and the generator action. https://arxiv.org/html/2610.04382v1
2. T. Brendle and A. Hatcher, *Configuration spaces of rings and wickets*, Comment. Math. Helv. 88 (2013), 131--162; arXiv:0805.4354. https://arxiv.org/abs/0805.4354
3. C. Jensen, J. McCammond and J. Meier, *The integral cohomology of the group of loops*, Geom. Topol. 10 (2006), 759--784. https://doi.org/10.2140/gt.2006.10.759
