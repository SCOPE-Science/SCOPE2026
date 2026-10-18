# A uniqueness principle for seasonal ruin root matrices

## Finding
For every integer \(N\ge 2\), let \(X_1,\ldots,X_N\) be independent nonnegative integer-valued random variables, with laws repeated periodically. Put \(p_{j,k}=\Pr(X_j=k)\), \(a_j=p_{j,0}>0\), and \(g_j(z)=\mathbb E[z^{X_j}]\). Suppose that
\[
\sum_{j=1}^N\mathbb E X_j<N,\qquad \mathbb E[R^{X_j}]<\infty\quad(1\le j\le N)
\]
for some \(R>1\). Write \(Q(z)=z^N-\prod_{j=1}^Ng_j(z)\). Assume its \(N-1\) zeros in \(\{|z|\le1\}\setminus\{1\}\), counted with multiplicity, are distinct, denoted \(\alpha_1,\ldots,\alpha_{N-1}\). These zeros are nonzero because every \(a_j\) is positive. Define the \(N\)-by-\(N\) complex matrix \(A\) by
\[
A_{r,1}=a_N,\quad
A_{r,c}=a_{c-1}\frac{g_N(\alpha_r)\prod_{j=1}^{c-2}g_j(\alpha_r)}{\alpha_r^{c-1}}
\quad(1\le r<N,\ 2\le c\le N),
\]
with empty products equal to one, and last row
\[
A_{N,1}=a_N,\qquad A_{N,c}=a_{c-1}\quad(2\le c\le N).
\]
**Then \(\det A\ne0\).** Thus the root-cancellation and drift equations of the unit-premium periodic discrete-time risk model uniquely determine its initial phase probabilities in this light-tailed, simple-root regime.

## Assumptions and scope
The result concerns the unit-premium case, arbitrary finite seasonal period, strictly positive zero-claim probability in every season, strict negative mean reflected-walk drift over a full period, an exponential moment, and distinct nonunit zeros of the kernel inside or on the unit circle. The last condition does not demand that the nonunit zeros lie strictly inside that circle. The root count follows from the classical argument principle/Rouché comparison for \(z^N-\prod_jg_j(z)\) and the strict derivative inequality at \(1\); it is additionally stipulated in the theorem to specify precisely which matrix is considered. No conclusion is asserted for multiple roots, vanishing zero-claim probabilities, critical drift, or claim distributions without an exponential moment.

## Proof
**1. Algebraic reconstruction.** Let \(b=(b_1,\ldots,b_N)\in\mathbb C^N\) satisfy \(Ab=0\). Use cyclic indices \(F_{N+1}=F_1\), \(b_{N+1}=b_1\). Consider the formal power-series system
\[
zF_j(z)=g_j(z)F_{j+1}(z)+a_jb_{j+1}(z-1),\qquad 1\le j\le N.
\tag{1}
\]
Its coefficient matrix has determinant \(Q(z)\), and \(Q(0)=-\prod_ja_j\ne0\); therefore it has a unique solution in \(\mathbb C[[z]]^N\). The constant coefficient of (1) proves \(F_{j+1}(0)=b_{j+1}\).

Set
\[
L_b(z)=a_Nb_1+\sum_{c=2}^Na_{c-1}b_c\,
\frac{g_N(z)\prod_{j=1}^{c-2}g_j(z)}{z^{c-1}}.
\]
Successive substitution in (1), beginning with the equation for \(F_N\), gives the exact formal identity
\[
Q(z)F_N(z)=(z-1)z^{N-1}L_b(z).
\tag{2}
\]
The first \(N-1\) rows of \(Ab=0\) assert \(L_b(\alpha_r)=0\), and the final row asserts \(L_b(1)=0\). The latter is meaningful because \(g_j(1)=1\). We have \(Q'(1)=N-\sum_j\mathbb EX_j>0\), so \(1\) is a simple zero of \(Q\). Consequently, in the meromorphic quotient (2) each nonunit zero in the closed unit disk is removable, and at \(1\) the numerator vanishes at least twice. It follows that \(F_N\) extends holomorphically to a disk \(\{|z|<1+\varepsilon\}\), for some \(\varepsilon>0\), with \(F_N(1)=0\). Here the exponential moment makes all \(g_j\) analytic on a common disk larger than the unit disk; isolated zeros of \(Q\) yield the stated uniform margin. Reversing equations (1) from \(F_N\) to \(F_{N-1},\ldots,F_1\) divides only by \(z\), and the apparent singularity at \(0\) is removable because the formal solution exists. Hence every \(F_j\) is analytic on a possibly smaller disk of radius greater than one. Evaluating (1) at \(1\) yields \(F_j(1)=F_{j+1}(1)\); thus every \(F_j(1)=0\).

**2. Signed invariant measure.** Write \(F_j(z)=\sum_{w\ge0}\mu_j(w)z^w\). Analyticity past the unit circle implies \(\sum_w|\mu_j(w)|<\infty\). By the constant-coefficient argument \(\mu_j(0)=b_j\). Equation (1) is exactly the probability-generating-function identity for the reflected transition
\[
 w\longmapsto\max\{0,w+X_j-1\},
\]
acting on a finite complex measure at cyclic phase \(j+1\) to produce the measure at phase \(j\). Indeed, the only correction to the unreflected generating function \(z^{-1}g_j(z)F_{j+1}(z)\) is the transition from \(w=0,X_j=0\), whose probability mass \(a_jb_{j+1}\) moves from exponent \(-1\) to exponent \(0\), producing precisely \(a_jb_{j+1}(1-z^{-1})\). Taking the disjoint union of phase-labelled nonnegative integer states, the measures \(N^{-1}\mu_j\) form one finite complex invariant measure \(\nu\) of this countable-state Markov chain. Its total mass is
\[
\nu(\Omega)=\frac1N\sum_jF_j(1)=0.
\tag{3}
\]

**3. Uniqueness of the invariant measure.** The \(N\)-step skeleton on a fixed phase has negative constant expected drift \(\sum_j\mathbb E X_j-N<0\) whenever \(w\ge N\), because reflection cannot occur during that block. Its expected next state is finite everywhere. Foster's drift criterion on the countable state space gives positive recurrence of the communicating class accessible from \(0\); the positive probabilities \(\Pr(X_j=0)=a_j\) mean that, from every state and phase, a finite run of zero claims reaches the reference zero state with positive probability. Thus there is exactly one closed recurrent class, all other states are transient, and the phase-labelled chain has a unique invariant probability \(\pi\). For completeness, the Cesàro transition kernels converge from every initial state to \(\pi\), so dominated convergence against any finite complex invariant measure gives \(\nu=\nu(\Omega)\pi\). By (3), \(\nu=0\). Therefore every \(\mu_j=0\), whence \(b_j=\mu_j(0)=0\) for each \(j\). Thus \(\ker A=\{0\}\), proving \(\det A\ne0\). \(\square\)

## Verification
A standalone exact-arithmetic check of an illustrative genuinely periodic case appears in `check_example.py`. Take \(N=2\), with \(g_1(z)=(3+z^2)/4\) and \(g_2(z)=(2+z^2)/3\). Then
\[
Q(z)=-\frac{(z-1)(z+1)(z^2-6)}{12},\qquad
A=\begin{pmatrix}2/3&-3/4\\2/3&3/4\end{pmatrix},\qquad\det A=1.
\]
The code reconstructs these polynomial and matrix identities with rational arithmetic. This finite check is illustrative only; the theorem rests on the preceding argument for arbitrary \(N\).

## Relationship to prior work
Grigutis, Jankauskas, and Šiaulys, *Multi seasonal discrete time risk model revisited* (arXiv:2207.03196v1, 2022), develop the unit-premium \(N\)-seasonal generating-function system and its root-cancellation matrix, particularly their equations (11)–(15) and (28); that source does not establish the determinant's general nonvanishing. Gervė and Grigutis, *Distribution of shifted discrete random walk generated by distinct random variables and applications in ruin theory* (arXiv:2211.14629v1, later published 2024), give a broader premium-rate construction and explicitly pose nonsingularity as Conjecture 1; their section 4 includes the exact unit-premium matrix as (25). The present result gives a direct signed-invariant-measure proof of nonsingularity for the unit-premium, exponentially light-tailed subfamily under simple roots, rather than a numerical matrix observation or an algebraic restatement of the previously derived equations. The proof uses standard countable-state recurrence theory in a new implication from analytic pole cancellation to unique solvability of the specific root matrix.

## Limitations
This theorem does not settle the arbitrary-premium form of the conjecture or remove the exponential-moment, positive-zero-mass, negative-drift, and simple-root hypotheses. It does not calculate ruin probabilities explicitly. Standard Markov-chain uniqueness is invoked with a complete drift/accessibility verification, not a numerical approximation. A database/literature search cannot logically certify global novelty; independent verification remains appropriate.

## References
1. A. Grigutis, J. Jankauskas, J. Šiaulys, *Multi seasonal discrete time risk model revisited*, arXiv:2207.03196v1 (public 2022-07-07), primary MSC 60G50; especially Theorem 1 and equation (28). https://arxiv.org/pdf/2207.03196
2. S. Gervė, A. Grigutis, *Distribution of shifted discrete random walk generated by distinct random variables and applications in ruin theory*, arXiv:2211.14629v1 (public 2022-11-26), *Modern Stochastics: Theory and Applications* **11** (2024), 323–357, DOI:10.15559/24-VMSTA249; especially equation (25), Conjecture 1, and Lemma 4. https://vmsta.org/journal/VMSTA/article/296/read
3. Standard countable-state Markov-chain Foster drift and Cesàro ergodic theorems, as used in the explicit argument above (no specialized published nonsingularity theorem assumed).
