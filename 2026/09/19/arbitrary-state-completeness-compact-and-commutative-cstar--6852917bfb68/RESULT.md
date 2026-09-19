# Exact arbitrary-state completeness boundary for two Hilbert \(C^*\)-module localization classes

## Result

Let
\[
\mathcal N_\tau^E=\{x\in E:\tau(\langle x,x\rangle)=0\}
\]
for a state \(\tau\) on a \(C^*\)-algebra \(A\) and a Hilbert \(A\)-module \(E\).  Write \(E_\tau\) for the Hilbert-space completion of \(E/\mathcal N_\tau^E\).

Abedi and Moslehian's abstract states the completeness equality
\[
E_\tau=E/\mathcal N_\tau^E
\]
for \(C^*\)-algebras of compact operators and for commutative \(C^*\)-algebras, after defining \(\tau\) as an arbitrary state.  The actual arguments in Section 2 impose purity: the commutative conclusion is stated for \(\tau\in P(A)\), and the compact-operator example likewise begins with a pure state.  The arbitrary-state extension is false, but in both classes it has a sharp finite-support replacement.

### Theorem A: \(C^*\)-algebras of compact operators

Let
\[
A=\bigoplus_{\lambda\in\Lambda}^{c_0}K(H_\lambda),
\]
and let \(\tau\) be a state.  Write
\[
\tau((a_\lambda))=\sum_{\lambda}\operatorname{Tr}(\rho_\lambda a_\lambda),
\qquad
\rho_\lambda\in S_1(H_\lambda)_+,
\qquad
\sum_\lambda\operatorname{Tr}\rho_\lambda=1,
\]
and let \(p_\lambda=s(\rho_\lambda)\), \(p=(p_\lambda)\in
A^{**}\cong\prod_\lambda B(H_\lambda)\).

The following are equivalent:

1. \(E/\mathcal N_\tau^E\) is complete for every Hilbert \(A\)-module \(E\).
2. \(A/\mathcal N_\tau^A\) is complete for the standard Hilbert module \(E=A\).
3. \(p\in A\).
4. Only finitely many \(\rho_\lambda\) are nonzero, and every nonzero \(\rho_\lambda\) has finite rank.

Moreover, for the standard module the completion has the explicit form
\[
A_\tau\cong
\bigoplus_{\lambda}^{\ell^2}
S_2(p_\lambda H_\lambda,H_\lambda)
\]
under the isometry
\[
a+\mathcal N_\tau^A\longmapsto
(a_\lambda\rho_\lambda^{1/2})_\lambda .
\]
Thus finite-rank mixed states, not only pure states, have the completeness property, while every state with infinite support projection fails it already on \(E=A\).

### Theorem B: commutative \(C^*\)-algebras

Let \(A=C_0(X)\) for a locally compact Hausdorff space \(X\), and let \(\tau(f)=\int_X f\,d\mu\) for the representing probability measure \(\mu\).  The following are equivalent:

1. \(E/\mathcal N_\tau^E\) is complete for every Hilbert \(C_0(X)\)-module \(E\).
2. \(C_0(X)/\mathcal N_\tau^{C_0(X)}\) is complete.
3. \(\operatorname{supp}\mu\) is finite.

Hence the arbitrary-state completeness property in the commutative case holds exactly for finite convex combinations of pure states.

## Proof

### 1. The standard module over a compact-operator algebra

For \(a=(a_\lambda)\in A\),
\[
\|a+\mathcal N_\tau^A\|_\tau^2
=\tau(a^*a)
=\sum_\lambda
\|a_\lambda\rho_\lambda^{1/2}\|_2^2.
\]
Hence
\[
J_\tau(a+\mathcal N_\tau^A)
=(a_\lambda\rho_\lambda^{1/2})_\lambda
\]
is isometric into
\[
\mathcal H_\rho=
\bigoplus_{\lambda}^{\ell^2}
S_2(p_\lambda H_\lambda,H_\lambda).
\]

Its range is dense.  Indeed, a Hilbert--Schmidt operator on
\(p_\lambda H_\lambda\) is approximated in \(S_2\)-norm by operators whose
domain is contained in a finite-dimensional spectral subspace of
\(\rho_\lambda\).  Such an operator \(T\) can be written
\(a_\lambda\rho_\lambda^{1/2}\) with \(a_\lambda\) finite rank, by applying
\(\rho_\lambda^{-1/2}\) only on that finite-dimensional spectral subspace.
Truncating to finitely many \(\lambda\)'s proves density in the direct sum.
Therefore \(\mathcal H_\rho\) is exactly the Hilbert completion.

If \(p\in A\), then only finitely many \(p_\lambda\) are nonzero and each has
finite rank.  For any \(T=(T_\lambda)\in\mathcal H_\rho\), every
\(T_\lambda:p_\lambda H_\lambda\to H_\lambda\) has finite rank, and
\[
a_\lambda=T_\lambda
(\rho_\lambda|_{p_\lambda H_\lambda})^{-1/2}p_\lambda
\]
is compact.  With only finitely many nonzero blocks, \(a=(a_\lambda)\in A\)
and \(a\rho^{1/2}=T\).  Hence \(J_\tau\) is onto and
\(A/\mathcal N_\tau^A\) is complete.

Conversely, suppose \(p\notin A\).  The vector
\[
\rho^{1/2}=(\rho_\lambda^{1/2})_\lambda\in\mathcal H_\rho
\]
lies in the completion.  If it were \(a\rho^{1/2}\) for some \(a\in A\),
then \(a_\lambda\) would equal the identity on \(p_\lambda H_\lambda\) for
every \(\lambda\).  If some \(p_\lambda\) has infinite rank, this is
impossible because a compact operator cannot restrict to the identity on an
infinite-dimensional subspace.  If infinitely many \(p_\lambda\) are
nonzero, it is impossible because then \(\|a_\lambda\|\ge1\) on infinitely
many blocks, contradicting the \(c_0\)-condition.  Thus \(J_\tau\) is not
onto, and the quotient is incomplete.

This proves the equivalence of (2)--(4).

### 2. Every Hilbert module when \(p\in A\)

Assume \(p\in A\).  Then \(pAp\) is finite dimensional and
\(\tau|_{pAp}\) is faithful.  For every Hilbert \(A\)-module \(E\),
\[
\mathcal N_\tau^E=\{x\in E:xp=0\}.
\]
Indeed,
\[
\tau(\langle x,x\rangle)
=\tau(p\langle x,x\rangle p)
=\tau(\langle xp,xp\rangle),
\]
and faithfulness on \(pAp\) makes the last quantity zero exactly when
\(xp=0\).

Therefore
\[
E/\mathcal N_\tau^E\longrightarrow Ep,\qquad
x+\mathcal N_\tau^E\longmapsto xp
\]
is a linear bijection.  Since \(pAp\) is finite dimensional and
\(\tau|_{pAp}\) is faithful, there is \(m>0\) such that
\[
m\|b\|\le \tau(b)\le \|b\|
\qquad(b\in(pAp)_+).
\]
Consequently the scalar \(\tau\)-norm on \(Ep\) is equivalent to its Hilbert
module norm.  The space \(Ep\) is closed in \(E\), being the range of the
bounded projection \(x\mapsto xp\).  Hence it is complete in the scalar
norm.  This proves (3)\(\Rightarrow\)(1), while
(1)\(\Rightarrow\)(2) is immediate.

### 3. The commutative standard module

For \(A=C_0(X)\),
\[
\|f+\mathcal N_\tau^A\|_\tau
=\|f\|_{L^2(\mu)}.
\]
The image of \(C_0(X)\) is dense in \(L^2(\mu)\), so the quotient is complete
exactly when that image is already closed.

If \(S=\operatorname{supp}\mu\) is finite, the quotient is finite
dimensional and hence complete.

Suppose \(S\) is infinite and the quotient were complete.  Its kernel in the
\(C^*\)-norm is the ideal of functions vanishing on \(S\), so the same
vector space also carries the Banach quotient norm
\[
\|f+\mathcal N_\tau^A\|_{\infty,q}=\sup_{x\in S}|f(x)|.
\]
The identity from this Banach quotient to the assumed-complete
\(\tau\)-quotient is continuous because
\(\|f\|_{L^2(\mu)}\le\|f\|_\infty\).  By the bounded inverse theorem there
would be \(C>0\) such that
\[
\sup_{S}|f|\le C\|f\|_{L^2(\mu)}
\qquad(f\in C_0(X)).
\]
This is impossible for infinite \(S\).  For each \(n\), choose \(n\)
distinct points of \(S\) and pairwise disjoint neighborhoods of them.  One
of these neighborhoods has \(\mu\)-measure at most \(1/n\).  Local compact
regularity gives \(f_n\in C_c(X)\) supported there with
\(0\le f_n\le1\) and \(f_n(x_n)=1\).  Then
\[
\sup_S|f_n|=1,\qquad
\|f_n\|_{L^2(\mu)}\le n^{-1/2},
\]
a contradiction.  Thus \(S\) must be finite.

### 4. Every commutative Hilbert module for finitely supported \(\mu\)

Write
\[
\mu=\sum_{j=1}^m w_j\delta_{x_j},
\qquad w_j>0.
\]
For a Hilbert \(C_0(X)\)-module \(E\), let \(E_{x_j}\) be the Hilbert-space
fiber obtained from the pure state \(\delta_{x_j}\).  The map
\[
E/\mathcal N_\tau^E
\longrightarrow
\bigoplus_{j=1}^m E_{x_j},
\qquad
[x]\longmapsto
(\sqrt{w_j}[x]_{x_j})_{j=1}^m
\]
is isometric.  It is onto: choose \(h_j\in C_0(X)\) with
\(h_j(x_i)=\delta_{ij}\); representatives of any prescribed fiber vectors
can then be patched by \(\sum_j y_jh_j\).  The finite Hilbert direct sum on
the right is complete.  This proves Theorem B.

## Explicit counterexamples to the unrestricted abstract formulation

For a noncommutative example, let
\[
A=K(\ell^2),\qquad
\tau(a)=\sum_{n\ge1}2^{-n}\langle ae_n,e_n\rangle,
\qquad E=A.
\]
The state is faithful, so \(\mathcal N_\tau^A=0\).  If \(P_N\) projects onto
\(\operatorname{span}\{e_1,\ldots,e_N\}\), then
\[
\|P_M-P_N\|_\tau^2
=\sum_{n=N+1}^{M}2^{-n}\longrightarrow0.
\]
If \(P_N\) converged in the \(\tau\)-norm to a compact operator \(a\), then
for every fixed \(k\),
\[
2^{-k}\|(P_N-a)e_k\|^2
\le \|P_N-a\|_\tau^2,
\]
so \(ae_k=e_k\) for all \(k\), forcing \(a=I\), a contradiction.  Thus the
quotient is not complete even for the standard module over \(K(\ell^2)\).

For a commutative example, \(A=C([0,1])\) with Lebesgue state has standard
module completion \(L^2[0,1]\), while the image of \(C([0,1])\) is a proper
dense subspace.

## Relation to prior work

Abedi--Moslehian define \(\mathcal N_\tau^E\) for arbitrary states, but the
body of their completeness argument uses pure states.  In particular,
their introduction says that the commutative conclusion is for
\(\tau\in P(A)\); Proposition 2.10 assumes a pure state and a minimal support
projection; and Example 2.12 treats a pure state on a \(c_0\)-sum of compact
operator algebras.  Pure states are therefore contained in the positive
part of the present boundary, but arbitrary mixed states are not.

The ingredients used above -- the trace-class dual of \(K(H)\), the
decomposition of \(C^*\)-algebras of compact operators, density of
finite-rank operators in Schatten classes, the Riesz representation theorem,
and standard Hilbert-module fibers -- are classical.  The contribution here
is the sharp arbitrary-state classification in the two classes highlighted
by the recent paper, together with the explicit completion model and
counterexamples.

## Limitations

The theorem does not classify states with the completeness property on an
arbitrary \(C^*\)-algebra, nor does it classify completeness for an
individual Hilbert module when the universal "for every \(E\)" property
fails.  The compact-operator and commutative criteria are different in
form: a point-mass support projection need not belong to \(C_0(X)\), so the
compact-operator proof does not directly subsume the commutative one.

Originality is asserted only to the best of our knowledge.  Searches for the
exact and synonymous formulations did not locate the two sharp criteria.
The most plausible residual prior-art risk is classical GNS/localization
literature in which closedness of the cyclic image may be characterized in
different language.  No specific inaccessible paper was identified as
containing an equivalent theorem.

## References

1. S. Abedi and M. S. Moslehian, *Schatten norms on Hilbert \(C^*\)-modules via pure states*, Mathematica Scandinavica 131 (2025), 535--557; arXiv:2609.13944v1 (12 September 2026). https://arxiv.org/abs/2609.13944
2. S. Abedi and M. S. Moslehian, journal page and DOI: https://doi.org/10.7146/math.scand.a-160044
3. R. V. Kadison, *Irreducible operator algebras*, Proc. Natl. Acad. Sci. USA 43 (1957), 273--276. https://doi.org/10.1073/pnas.43.3.273
