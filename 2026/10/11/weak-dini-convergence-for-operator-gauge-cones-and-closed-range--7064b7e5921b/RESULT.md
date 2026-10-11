# Weak Dini convergence for operator-gauge cones and closed range

## Finding
Let \(X,Y\) be real Banach spaces and let \(T:X\to Y\) be a bounded injective linear operator. On \(Z=\mathbb R\oplus_1 X\) use the closed cone
\[
C_T=\{(t,x)\in Z:t\ge\|Tx\|_Y\}.
\]
The following three properties are equivalent:

1. \(T(X)\) is closed in \(Y\), equivalently \(\inf_{\|x\|_X=1}\|Tx\|_Y>0\).
2. Every increasing weakly convergent net in the ordered space \((Z,C_T)\) converges in norm.
3. The cone \(C_T\) is normal.

More precisely, if \(T\) is not bounded below, there is an increasing net \((z_d)\) with \(z_d\rightharpoonup0\) but \(\|z_d\|_Z\to1\). In particular, for \(X=Y=\ell_1(\mathbb N)\) and \((Tx)_k=2^{-k}x_k\), a classical non-normal cone on \(\mathbb R\oplus_1\ell_1\) fails the weak Dini property for **nets**, even though every weakly convergent **sequence** in this space converges in norm by the Schur property. The counterexample net is norm bounded, so the additional boundedness restriction discussed immediately after that open problem does not help for this concrete cone. This resolves the specific net-versus-sequence question raised after Example 6.1 in the cited paper; it does not resolve the unrestricted question for every possible non-normal cone.

## Assumptions and scope
All spaces and operators are real. One may take \(X
e\{0\}\); when \(X=\{0\}\), the equivalence holds trivially and the displayed infimum over the unit sphere is simply omitted. The direct-sum norm is \(\|(t,x)\|_Z=|t|+\|x\|_X\). The order \(z\le w\) means \(w-z\in C_T\). A net is increasing when \(d\preceq e\) implies \(z_d\le z_e\); weak convergence means pointwise convergence against every functional in \(Z^*=\mathbb R\oplus_\infty X^*\). The cone is closed because \(T\) is continuous, pointed because \(T\) is injective, and generating because \((1,0)\) is an interior point (as \(\|Tx\|\le\|T\|\|x\|\)). The proof does not assume separability, reflexivity, a lattice structure, or a basis.

## Proof
**Closed range gives norm convergence.** If \(T(X)\) is closed, injectivity and the bounded inverse theorem supply \(c>0\) such that \(\|Tx\|\ge c\|x\|\) for all \(x\in X\). Consider an increasing net \(z_d=(t_d,x_d)\) weakly converging to \((t,x)\). Its scalar coordinates \(t_d\) increase and converge to \(t\). Whenever \(d\preceq e\), the cone inequality gives
\[
\|x_e-x_d\|\le c^{-1}\|T(x_e-x_d)\|\le c^{-1}(t_e-t_d).
\]
Since the scalar net is Cauchy, the vector net is norm Cauchy: for any two indices \(e,f\succeq d\), apply the preceding inequality to \((d,e)\) and \((d,f)\) and use the triangle inequality. Completeness gives a norm limit. Its weak limit must equal \((t,x)\), proving property 2.

**Finite-codimensional near-kernel lemma.** If the bounded injective \(T\) is not bounded below, then for every finite subset \(F\subset X^*\) and every \(\varepsilon>0\) there exists \(u\in X\) with
\[
\|u\|=1,\qquad \phi(u)=0\ \ (\phi\in F),\qquad \|Tu\|\le\varepsilon.
\]
Indeed, \(M=\bigcap_{\phi\in F}\ker\phi\) is closed and finite-codimensional. Were \(T\) bounded below on \(M\), its image \(T(M)\) would be closed. Choosing a finite-dimensional complement \(E\) of \(M\) gives \(T(X)=T(M)+T(E)\), a closed subspace (a closed subspace plus a finite-dimensional subspace is closed). The bounded inverse theorem for \(T:X\to T(X)\) would then imply that \(T\) is bounded below on all of \(X\), a contradiction.

**A weakly null increasing net without norm convergence.** Direct the set \(\mathcal D=\{(F,n):F\subset X^*\text{ finite},\ n\in\mathbb N\}\) by \((F,n)\preceq(G,m)\) if \(F\subseteq G\) and \(n\le m\). Set \(\delta_{F,n}=4^{-(|F|+n)}\). By the lemma choose \(u_{F,n}\in S_X\) annihilating every \(\phi\in F\) with \(\|Tu_{F,n}\|\le\delta_{F,n}\), and define
\[
z_{F,n}=(-2\delta_{F,n},u_{F,n}).
\]
For strictly comparable \(d\prec e\), the integer \(|F|+n\) increases by at least one, hence \(\delta_e\le\delta_d/4\). Therefore
\[
\|T(u_e-u_d)\|\le\delta_e+\delta_d
\le 2(\delta_d-\delta_e),
\]
which is exactly \(z_e-z_d\in C_T\). Equality of indices is trivial, so the net is increasing. For a fixed \(\phi\in X^*\), all sufficiently large indices have \(\phi\in F\), and hence \(\phi(u_{F,n})=0\). As \(n\to\infty\) in the directed set, \(\delta_{F,n}\to0\); consequently \(z_d\rightharpoonup0\) in \(Z\). Yet \(\|z_d\|_Z=1+2\delta_d\to1\), proving failure of property 2 when property 1 fails.

**Normality criterion.** If \(\|Tx\|\ge c\|x\|\), then for \(0\le(t,x)\le(s,y)\) we have \(0\le t\le s\), \(\|Tx\|\le t\), and thus \(\|(t,x)\|_Z\le(1+c^{-1})\|(s,y)\|_Z\). Conversely, if \(T\) is not bounded below, choose \(v_j\in S_X\) with \(\|Tv_j\|\to0\). The vectors
\[
q_j=\left(\tfrac12,\frac{v_j}{2\|Tv_j\|}\right)
\]
satisfy \(0\le q_j\le(1,0)\), but \(\|q_j\|_Z\to\infty\); therefore \(C_T\) is not normal. This proves the equivalence of properties 1 and 3, completing the proof.

## Verification
The standalone script `CHECK.py` uses exact rational arithmetic to test the finite-dimensional annihilator construction for the diagonal weights \(2^{-k}\), including nested finite families of functionals, the chosen scales, and the order inequalities. Its successful output is `VERIFY_OK rational_profiles=64 annihilator_tests=128 exact_order_pairs=746 infinite_net_proof_is_analytic=True`. The script checks finite samples only: the closed-range lemma, the uncountable directed set, and weak convergence against all members of \(X^*\) are proved analytically above.

## Relationship to prior work
Jochen Glück, *Increasing sequences in ordered Banach spaces—new theorems and open problems*, arXiv:2409.19768v1 (first posted 29 September 2024), develops Levi and Dini properties for closed cones. Its Example 6.1 gives the non-normal cone on \(\ell_1(\mathbb N_0)\) defined by \(x_0\ge\sum_{k\ge1}2^{-k}|x_k|\), and the discussion immediately thereafter explicitly leaves undecided whether every increasing weakly convergent **net** in that example converges in norm. The special case \(X=\ell_1\) and \(T\) the positive diagonal contraction identifies precisely that cone, after separating coordinate zero. Its Theorem 6.3 establishes a negative Dini criterion assuming the bidual wedge is pointed; Example 5.3(f) explains why this assumption fails for a non-normal cone on a Schur space. The new operator-gauge criterion constructs the missing monotone net directly, so neither published theorem implies this statement in that special case. The paper's general Open Problem 6.2 about **all** non-normal cones remains open.

## Limitations
The theorem concerns only cones defined by the norm of a bounded injective operator as above. It does not classify arbitrary closed cones or solve the general normality-versus-Dini-net question. No weakly convergent **sequence** with nonvanishing norms is asserted for the \(\ell_1\) instance, since that would contradict the Schur property. Exact finite checks do not establish the infinite-dimensional lemma or net argument. Searches of indexed results and accessible literature cannot exclude unpublished or unindexed equivalent statements.

## References
1. J. Glück, *Increasing sequences in ordered Banach spaces—new theorems and open problems*, arXiv:2409.19768v1, 29 September 2024, especially Theorem 2.1, Examples 5.3(f) and 6.1, Theorem 6.3, and Open Problem 6.2. https://arxiv.org/abs/2409.19768
2. The classical bounded inverse theorem and the finite-dimensional-subspace perturbation lemma for closed subspaces are used in the proof; no specialized external theorem beyond these is needed.
