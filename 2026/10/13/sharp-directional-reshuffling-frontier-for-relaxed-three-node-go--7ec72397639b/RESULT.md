# Sharp directional reshuffling frontier for relaxed three-node gossip

## Finding

For the two edges of a three-node path, consider two consecutive randomized, equally relaxed pairwise-gossip operations. Sampling each edge independently with probability one half and sampling the two edges once each in a random order have **different pointwise mean-square rankings**. For every relaxation \(0<\omega<2\), let \(E_{\mathrm{iid}}(x)\) and \(E_{\mathrm{rr}}(x)\) be the expected squared disagreements after two operations from the same deterministic initial state \(x\). Then

\[
 E_{\mathrm{rr}}(x)\le E_{\mathrm{iid}}(x)\quad\text{for every }x\in\mathbb R^3
 \quad\Longleftrightarrow\quad 0<\omega\le\frac43.
\]

Below the boundary the inequality is strict for every nonconsensus state. At \(\omega=4/3\) equality holds on the nonconsensus direction \((1,-2,1)\), whereas at \(4/3<\omega<2\) that direction strictly **favors independent selection** and the orthogonal disagreement direction \((1,0,-1)\) strictly favors reshuffling. In particular, at \(\omega=3/2\), with the unit initial disagreements \(x_+=(1,-2,1)/\sqrt6\) and \(x_-=(1,0,-1)/\sqrt2\),

\[
\begin{array}{c|cc}
& E_{\mathrm{iid}} & E_{\mathrm{rr}}\\\hline
x_+ & 179/512 & 103/256\\
x_- & 257/512 & 61/256
\end{array}.
\]

A more general exact theorem gives the angular frontier. Let \(u,v\) be nonparallel unit vectors in a real Euclidean space, with \(c=|\langle u,v\rangle|\in(0,1)\). Set \(A=I-\omega uu^{\mathsf T}\) and \(B=I-\omega vv^{\mathsf T}\). Write \(E_{\mathrm{rr}}(x)=\tfrac12(\|ABx\|^2+\|BAx\|^2)\), and \(E_{\mathrm{iid}}(x)=\tfrac14(\|A^2x\|^2+\|ABx\|^2+\|BAx\|^2+\|B^2x\|^2)\). Orient \(v\) so \(\langle u,v\rangle=c>0\), and define the orthonormal bisectors \(e_+=(u+v)/\sqrt{2(1+c)}\), \(e_-=(u-v)/\sqrt{2(1-c)}\). For every deterministic \(x\), the exact difference is

\[
\boxed{\;E_{\mathrm{iid}}(x)-E_{\mathrm{rr}}(x)=
 \frac{\omega^2(2-\omega)(1-c^2)}4
 \Bigl([2-\omega(1+c)]\langle x,e_+\rangle^2+
       [2-\omega(1-c)]\langle x,e_-\rangle^2\Bigr).\;}
\]

Therefore pointwise reshuffling dominance holds precisely for \(\omega\le 2/(1+c)\) within the range \(0<\omega<2\). Beyond this threshold there are exactly one positive and one negative nonzero eigenvalue of the two-step Gram difference; on the common perpendicular the two risks are identical.

## Assumptions and scope

Pairwise gossip takes the centered opinion vector \(x\in\mathbb R^3\) and applies \(I-\omega ee^{\mathsf T}\), where \(e=(\mathbf e_i-\mathbf e_j)/\sqrt2\) is the normalized incidence vector of an edge. Thus \(\omega=1\) is exact endpoint averaging and \(1<\omega<2\) is overrelaxed averaging. Both compared methods use exactly two edge communications and choose either edge with marginal probability one half at each position. The mean of all node values is unchanged by every update. The expectation is conditional on a fixed, deterministic starting vector and concerns only two communications, not multiple epochs or runtime. The general angular theorem is stated for a finite-dimensional real Euclidean space and \(0<c<1\), with exact arithmetic and one common relaxation \(0<\omega<2\).

## Proof

**1. Sampling Gram matrices.** For symmetric \(A,B\) write

\[
Q_{\mathrm{rr}}=\frac12(AB^2A+BA^2B),\qquad
Q_{\mathrm{iid}}=\frac14(A^4+B^4+AB^2A+BA^2B).
\]

These follow by explicitly enumerating the two permutation orders and the four ordered draws with replacement. They satisfy \(E_\ast(x)=\langle x,Q_\ast x\rangle\). Therefore

\[
D:=Q_{\mathrm{iid}}-Q_{\mathrm{rr}}
=\frac14(A^4+B^4-AB^2A-BA^2B).
\]

**2. Exact operator reduction.** Put \(P=uu^{\mathsf T}\) and \(Q=vv^{\mathsf T}\). Since \(P^2=P\), \(Q^2=Q\),
\[
A^2=I-\omega(2-\omega)P,\qquad B^2=I-\omega(2-\omega)Q.
\]

Substituting these identities into \(D\), and using \(PQ=cuv^{\mathsf T}\), \(QP=cvu^{\mathsf T}\) after the harmless orientation choice, gives the exact identity

\[
 D=\frac{\omega^2(2-\omega)}4
 \Bigl([2-\omega(1-c^2)](P+Q)-2c(uv^{\mathsf T}+vu^{\mathsf T})\Bigr).
\]

Both \(P+Q\) and \(uv^{\mathsf T}+vu^{\mathsf T}\) preserve the orthogonal bisectors \(e_+,e_-\). Their respective eigenvalues there are \(1\pm c\) and \(\pm(1\pm c)\), so after collecting terms the eigenvalues of \(D\) are

\[
 d_\pm=\frac{\omega^2(2-\omega)(1-c^2)}4[2-\omega(1\pm c)].
\]

The restriction of \(D\) to \(\{u,v\}^{\perp}\) is zero. Expanding a general initial state in this orthogonal decomposition proves the exact quadratic-form formula, including all its quantifiers.

**3. Complete sign classification.** On \(0<\omega<2\) the common prefactor is strictly positive and \(2-\omega(1-c)>0\), since \(1-c<1\). The remaining eigenvalue \(d_+\) vanishes exactly when \(\omega=2/(1+c)\), is positive below, and is negative above. Since \(e_+,e_-\) are independent, this proves necessity, sufficiency, strictness and the existence of initial directions giving opposite rankings above the threshold. The endpoint \(\omega=2\) is excluded: there each update is an isometric reflection and the Gram difference vanishes, so claiming a negative eigenvalue at that endpoint would be false.

**4. Three-node path.** For adjacent edges choose \(u=(1,-1,0)/\sqrt2\) and \(v=(0,-1,1)/\sqrt2\); their inner product is \(c=1/2\). The bisectors are exactly \(e_+=(1,-2,1)/\sqrt6\) and \(e_-=(1,0,-1)/\sqrt2\). Both are orthogonal to consensus. Substituting \(c=1/2\) yields the threshold \(2/(1+c)=4/3\). At \(\omega=3/2\), the difference eigenvalues are \(-27/512\) and \(135/512\), respectively. Direct multiplication of the four transition matrices gives the individual rational risks reported above, completing the physical gossip example.

## Verification

The standalone `verify.py`, requiring SymPy as specified in `requirements.txt`, checks the generic two-dimensional symbolic Gram-difference identity and both bisector eigenvalue formulas, then executes a grid of exact rational nonorthogonal test pairs and relaxations. It also reconstructs the actual three-by-three edge-gossip matrices and verifies the four stated rational risks, the two opposite directional signs and consensus invariance. Execute `python verify.py` from the extracted file directory. The run reports 45 exact checks passing. The analytic operator decomposition, rather than the finite test grid, proves the universal claim.

## Relationship to prior work

Haddock, Jarman and Yap's 2021 block-gossip analysis explicitly connects gossip to randomized Kaczmarz and analyzes independently sampled blocks, but does not give a two-edge without-replacement/with-replacement **initial-direction** comparison or this overrelaxation threshold. Recht and Ré (2012) prove a two-matrix **operator-norm** comparison for positive-semidefinite updates and display the same general two-step Gram expectations. Operator-norm dominance does not imply the Loewner order classified here. Moreover, for \(\omega>1\) the relaxed projection factors have a negative eigenvalue, so their positive-semidefinite premise is unavailable in precisely the reversal regime. De Sa (2020) gives a qualitatively related failure of broader reshuffling comparisons using more elaborate matrix families, but not this two-edge sharp angle-dependent threshold. Related existing results on optimal relaxation for **reshuffling alone** determine a different quantity and do not compare individual starting-state risks against sampling with replacement. The contribution here is the exact directional sign law for the latter comparison, including the smallest connected-gossip graph and a sharp reversal under individually nonexpansive updates.

## Limitations

The theorem covers precisely two successive steps, the Euclidean squared-disagreement metric, the same common relaxation on both edges, and independent uniform index selection versus uniform random permutation. It does not predict multi-epoch spectral radii, almost-sure behavior, distributed communication costs, or finite-precision error. The exact angular statement excludes coincident and orthogonal update normals and the relaxation endpoints, where separate degeneracies arise. Equivalent specialized results in unindexed work remain a priority risk; no claim of external novelty certification is made.

## References

1. J. Haddock, B. Jarman and C. Yap, *Paving the Way for Consensus: Convergence of Block Gossip Algorithms*, arXiv:2110.14609v1, October 27, 2021, https://arxiv.org/abs/2110.14609 .
2. B. Recht and C. Ré, *Toward a Noncommutative Arithmetic-geometric Mean Inequality: Conjectures, Case-studies, and Consequences*, COLT / Proceedings of Machine Learning Research 23 (2012), https://proceedings.mlr.press/v23/recht12.html .
3. C. De Sa, *Random Reshuffling is Not Always Better*, NeurIPS 33 (2020), https://papers.neurips.cc/paper/2020/hash/42299f06ee419aa5d9d07798b56779e2-Abstract.html .
