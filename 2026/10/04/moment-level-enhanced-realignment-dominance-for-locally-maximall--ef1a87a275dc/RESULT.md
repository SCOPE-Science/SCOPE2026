# Moment-level enhanced realignment dominance for locally maximally mixed states

## Finding
For a normalized bipartite state \(\rho\in M_{{d_A}}\otimes M_{{d_B}}\) with \(d_A,d_B\ge2\) and locally maximally mixed marginals
\[
\rho_A=\frac{{I_{{d_A}}}}{{d_A}},\qquad \rho_B=\frac{{I_{{d_B}}}}{{d_B}},
\]
define
\[
\widetilde\rho=\rho-\rho_A\otimes\rho_B,\qquad
G=\left(1-\frac1{{d_A}}\right)\left(1-\frac1{{d_B}}\right),\qquad
c=\frac1{{\sqrt{{d_A d_B}}}}.
\]
For \(k\ge1\), write
\[
r_k(X)=\operatorname{{Tr}}\!\left[(R(X)R(X)^*)^k\right].
\]
For every finite \(m\ge1\), let \(\alpha_m\) denote the optimal moment functional defined by minimizing the \(\ell_1\)-norm of a vector in \([0,1]^n\) with prescribed first \(m\) even moments. Then
\[
\alpha_m\bigl(r_1(\rho),\ldots,r_m(\rho)\bigr)
\le
\sqrt G\,\alpha_m\bigl(r_1(\widetilde\rho)/G,\ldots,r_m(\widetilde\rho)/G^m\bigr)+c.
\]
In particular,
\[
\alpha_m\bigl(r_1(\widetilde\rho)/G,\ldots,r_m(\widetilde\rho)/G^m\bigr)\le1
\quad\Longrightarrow\quad
\alpha_m\bigl(r_1(\rho),\ldots,r_m(\rho)\bigr)\le1,
\]
because
\[
\sqrt G+c
=
\sqrt{\left(1-\frac1{{d_A}}\right)\left(1-\frac1{{d_B}}\right)}
+\frac1{{\sqrt{{d_A d_B}}}}
\le1.
\]
Thus the open moment-level implication posed in arXiv:2609.29471v1 has an affirmative answer on the full locally maximally mixed class, simultaneously for every finite truncation order \(m\).

## Assumptions and scope
The state is finite-dimensional, positive semidefinite, normalized, and has exactly maximally mixed reduced states. Both local dimensions are at least two, so \(G>0\). The statement uses the realignment convention \(R(X)_{{ik,jl}}=X_{{ij,kl}}\) and the same moment functional \(\alpha_m\) as arXiv:2609.29471v1. No separability assumption is used in the transfer inequality itself; separability enters only when the resulting inequalities are used as entanglement criteria.

The result is not a claim about arbitrary marginals. The general implication asked in the source remains outside the proved scope.

## Proof
Let
\[
u_0=\frac{{\operatorname{{vec}}(I_{{d_A}})}}{{\sqrt{{d_A}}}},\qquad
v_0=\frac{{\operatorname{{vec}}(I_{{d_B}})}}{{\sqrt{{d_B}}}}.
\]
For the realignment convention above, direct index contraction gives
\[
R(X)\operatorname{{vec}}(I_{{d_B}})=\operatorname{{vec}}(\operatorname{{Tr}}_B X),
\]
and
\[
\operatorname{{vec}}(I_{{d_A}})^*R(X)
=\operatorname{{vec}}(\operatorname{{Tr}}_A X)^*.
\]
Since \(\widetilde\rho\) has zero partial traces,
\[
R(\widetilde\rho)v_0=0,\qquad u_0^*R(\widetilde\rho)=0.
\]
On the other hand,
\[
R(\rho_A\otimes\rho_B)
=\operatorname{{vec}}(\rho_A)\operatorname{{vec}}(\rho_B)^T
=c\,u_0v_0^T.
\]
Therefore, with respect to the orthogonal decompositions
\[
\mathbb C^{{d_B^2}}=\operatorname{{span}}\{{v_0\}\}\oplus v_0^\perp,
\qquad
\mathbb C^{{d_A^2}}=\operatorname{{span}}\{{u_0\}\}\oplus u_0^\perp,
\]
the realignment matrix has the block form
\[
R(\rho)=
\begin{{pmatrix}}
c&0\\
0&B
\end{{pmatrix}},
\]
where \(B\) is the restriction of \(R(\widetilde\rho)\) from \(v_0^\perp\) to \(u_0^\perp\). Equivalently, one forced zero singular value of \(R(\widetilde\rho)\) is replaced by \(c\). Hence, for every \(k\ge1\),
\[
r_k(\rho)=r_k(\widetilde\rho)+c^{{2k}}.
\]

Set
\[
a_k=\frac{{r_k(\widetilde\rho)}}{{G^k}},\qquad 1\le k\le m.
\]
Take any feasible vector \(y=(y_i)\) for the moment problem defining \(\alpha_m(a_1,\ldots,a_m)\). Thus \(0\le y_i\le1\) and
\[
\sum_i y_i^{{2k}}=a_k,\qquad 1\le k\le m.
\]
Form a new vector
\[
z=(\sqrt G\,y_1,\ldots,\sqrt G\,y_n,c).
\]
Every component of \(z\) lies in \([0,1]\), and the moment identity above yields
\[
\sum_i z_i^{{2k}}
=G^k a_k+c^{{2k}}
=r_k(\rho).
\]
So \(z\) is feasible for the uncentered moment problem and
\[
\alpha_m(r_1(\rho),\ldots,r_m(\rho))
\le \sqrt G\sum_i y_i+c.
\]
Taking the infimum over feasible \(y\) gives the quantitative transfer inequality.

Finally, put \(a=1/d_A\) and \(b=1/d_B\). Cauchy--Schwarz applied to the two unit vectors
\[
(\sqrt{{1-a}},\sqrt a),\qquad(\sqrt{{1-b}},\sqrt b)
\]
gives
\[
\sqrt{{(1-a)(1-b)}}+\sqrt{{ab}}\le1,
\]
which is exactly \(\sqrt G+c\le1\). This proves the stated implication.

## Verification
The proof is analytic. The bundled checker independently verifies, for deterministic positive locally maximally mixed examples in several rectangular local dimensions, the two null-direction identities, the exact moment relation
\[
r_k(\rho)-r_k(\widetilde\rho)=c^{{2k}}
\]
for several \(k\), positivity and marginal normalization, and the coefficient inequality \(\sqrt G+c\le1\). These finite checks test implementation and normalization only; they are not used as a proof of the all-dimensions statement.

## Relationship to prior work
Mallick, Gulati, and Nechita introduce the optimal finite-moment realignment functional, prove the corresponding standard and centered separability criteria, and explicitly ask whether centered moment non-detection always implies standard moment non-detection. Their paper proves the analogous implication for the full trace norm but leaves the finite-moment question open.

Zhang, Zhang, Zhang, and Guo introduced the enhanced realignment criterion. Sarbicki, Scala, and Chruściński later related enhanced realignment to correlation-tensor criteria and use an identity-plus-traceless local operator basis. That literature makes the special role of the identity direction natural, but the inspected sources do not state the finite-moment transfer inequality above or resolve the 2026 moment-level question on locally maximally mixed states.

The present result is a partial answer to the 2026 open question: it covers every finite moment order and arbitrary finite local dimensions, but only under maximally mixed marginals.

## Limitations
The argument relies crucially on both reduced states being proportional to the identity. For general marginals, the rank-one term \(R(\rho_A\otimes\rho_B)\) need not occupy singular directions orthogonal to the centered realignment matrix, so the exact power-sum decomposition can fail. No claim is made that the general implication holds.

The originality check was targeted rather than exhaustive. Correlation-tensor formulations of enhanced realignment are established prior work, and an equivalent moment-transfer observation could in principle appear under different terminology. The specific finite-moment implication, quantitative \(\alpha_m\) inequality, and connection to the explicit 2026 open question were not found in the inspected sources or semantic searches.

## References
1. B. Mallick, A. Gulati, I. Nechita, *Optimal entanglement criteria from trace invariants*, arXiv:2609.29471v1 (2026).
2. C.-J. Zhang, Y.-S. Zhang, S. Zhang, G.-C. Guo, *Entanglement detection beyond the computable cross-norm or realignment criterion*, Phys. Rev. A 77, 060301(R) (2008), arXiv:0709.3766.
3. G. Sarbicki, G. Scala, D. Chruściński, *Enhanced realignment criterion vs. linear entanglement witnesses*, J. Phys. A: Math. Theor. 53, 455302 (2020), arXiv:2002.00646.
