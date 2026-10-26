# Gaussian support law for rank-two abelian subgroups of cycle graphical groups

## Finding
Let \(q\) be any prime power and \(n\ge 4\). Let \(C_n\) be the cycle on labelled vertices \(1,\ldots,n\), and let \(\mathcal B_n\) be the span over \(\mathbb F_q\) of the alternating edge matrices \(E_{i,i+1}-E_{i+1,i}\), with indices modulo \(n\). A two-dimensional subspace \(U\le\mathbb F_q^n\) is **totally isotropic** if \(u^{\mathsf T}Bv=0\) for every \(u,v\in U\) and \(B\in\mathcal B_n\). Its **vertex support** is \(S(U)=\{i:\text{some }u\in U\text{ has }u_i\ne0\}\), and \(K(U)=|S(U)|\).

Define \(H_{n,q}(t)=\sum_{\dim U=2,\ U\text{ isotropic}}t^{K(U)}\), \(w=(q-1)t\), and \(g_q=|\mathrm{GL}_2(\mathbb F_q)|=q(q-1)^2(q+1)\). Set
\[
\tau_0(w)=2,\qquad \tau_1(w)=1+w,\qquad \tau_j(w)=(1+w)\tau_{j-1}(w)+qw\tau_{j-2}(w)\quad(j\ge2).
\]
Then the complete vertex-support enumerator is
\[
\boxed{H_{n,q}(t)=\frac{\tau_n(w)+qw^n-(q+1)(1+w)^n+q}{g_q}.}
\]
In particular, if \(\Delta_q=\sqrt{5q^2-4q}\) and \(\lambda_q=(q+\Delta_q)/2\), then
\[
H_{n,q}(1)=\frac{\lambda_q^n+((q-\Delta_q)/2)^n+q(q-1)^n-(q+1)q^n+q}{g_q}
=\frac{\lambda_q^n}{g_q}\bigl(1+O_q((q/\lambda_q)^n)\bigr).
\]
For \(U_n\) uniformly selected among these isotropic two-planes, write \(K_n=K(U_n)\). As \(n\to\infty\) with \(q\) fixed,
\[
\boxed{\frac{K_n-\mu_q n}{\sqrt{\sigma_q^2n}}\ \Longrightarrow\ N(0,1),\qquad
\mu_q=\frac12+\frac{q-2}{2\Delta_q},\qquad
\sigma_q^2=\frac{q(q^2-1)}{\Delta_q^3}>0.}
\]
Also \(\mathbb E K_n=\mu_q n+O_q(n\rho_q^n)\) and \(\mathrm{Var}(K_n)=\sigma_q^2 n+O_q(n^2\rho_q^n)\) for some \(0<\rho_q<1\). In the ordered limit \(n\to\infty\) then \(q\to\infty\), the support density tends to \((1+1/\sqrt5)/2\), and the variance per vertex tends to \(1/(5\sqrt5)\).

For an **odd prime** \(p\), let \(G_{C_n}(\mathbb F_p)\) be the class-two exponent-\(p\) graphical group of \(C_n\). Its commutator subgroup \(G'\) has order \(p^n\). The isotropic planes above correspond exactly to the abelian subgroups \(A\) satisfying \(G'\le A\le G\) and \(|A:G'|=p^2\). Thus the formulas also give the number of these subgroups, their vertex-support spectrum in the distinguished graphical presentation, and its Gaussian limit.

## Assumptions and scope
The finite-field enumeration is valid for all prime powers \(q\), including characteristic two. The group interpretation concerns odd prime fields \(\mathbb F_p\) and subgroups containing the full commutator subgroup; arbitrary subgroups and non-prime residue-field additive subgroups are **not** counted. Cycles have \(n\ge4\) for nonempty two-plane families; the triangle has no such planes. The normal law is a fixed-field, growing-cycle statement, not a simultaneous uniform limit in \(n\) and \(q\). Vertex support is relative to the labelled graph presentation, and is not asserted invariant under all group automorphisms.

## Proof
**Step 1: rank-two row criterion and an exact graph formula.** Choose an ordered basis of a two-plane \(U\) and form its \(2\times n\) matrix \(M\), with vertex columns \(c_i\in\mathbb F_q^2\). For each edge \(\{i,j\}\), the isotropy condition is precisely \(\det(c_i,c_j)=0\). On the set \(S\) of nonzero columns, all columns in each connected component of the induced graph \(G[S]\) therefore lie on one common one-dimensional line of \(\mathbb F_q^2\). Conversely this condition is sufficient. For \(S\ne\varnothing\), writing \(c(S)\) for the number of induced connected components, the number of admissible ordered matrices with precisely this support is
\[
(q-1)^{|S|}(q+1)^{c(S)}.
\]
Of these, exactly \((q-1)^{|S|}(q+1)\) have rank one: all components select the same line. (For empty support, the unique matrix has rank zero.) Each rank-two plane has exactly \(g_q\) ordered bases. Hence for an arbitrary labelled graph on \(n\) vertices the support polynomial is
\[
\frac1{g_q}\left[\sum_{S\subseteq V}((q-1)t)^{|S|}(q+1)^{c(S)}-(q+1)(1+(q-1)t)^n+q\right].\tag{1}
\]
The final \(+q\) corrects the empty support; this calculation uses only finite fields and is valid in every characteristic.

**Step 2: the cycle transfer and exact polynomial.** Put \(z=q+1\) and \(w=(q-1)t\). For cyclic binary occupancy states \(a,b\in\{0,1\}\), introduce
\[
T(w)=\begin{pmatrix}1&zw\\1&w\end{pmatrix}.
\]
For a cyclic sequence containing both zeros and ones, the number of transitions \(0\to1\) is the number of components of the occupied induced subgraph. Thus its contribution to \(\operatorname{tr}(T(w)^n)\) is \(w^{|S|}z^{c(S)}\). The all-zero term is already correct. The all-one term contributes \(w^n\) to the trace but should contribute \(zw^n\); therefore
\[
\sum_{S\subseteq V(C_n)}w^{|S|}z^{c(S)}=\operatorname{tr}(T(w)^n)+(z-1)w^n.
\]
The characteristic polynomial of \(T(w)\) is \(X^2-(1+w)X-qw\); its power traces have initial values \(2,1+w\) and the stated recurrence. Substitution in (1) proves the boxed support enumerator.

**Step 3: exponential growth and Gaussian limit.** For \(w\) near \(q-1\) define
\[
\lambda_{\pm}(w)=\frac{1+w\pm\sqrt{(1+w)^2+4qw}}2.
\]
At \(w=q-1\), \(\lambda_+=\lambda_q>q>\max\{|\lambda_-|,q-1\}\). This yields the asserted asymptotic for \(H_{n,q}(1)\). Moreover, in a sufficiently small complex neighborhood of \(s=0\), analytic branches give uniformly
\[
\mathbb E(e^{sK_n})=\frac{H_{n,q}(e^s)}{H_{n,q}(1)}
=\left(\frac{\lambda_+((q-1)e^s)}{\lambda_q}\right)^n(1+O_q(\eta_q^n))
\]
for some \(\eta_q<1\), including all derivatives on a smaller neighborhood.

Set \(L(s)=\log\lambda_+((q-1)e^s)-\log\lambda_q\). Differentiating the quadratic equation \(\lambda^2-(1+w)\lambda-qw=0\) gives
\[
\lambda'(w)=\frac{\lambda(w)+q}{\sqrt{(1+w)^2+4qw}},\qquad
\lambda''(w)=-\frac{2q(q+1)}{((1+w)^2+4qw)^{3/2}}.
\]
At \(w=q-1\), the same quadratic equation yields \(\lambda_q(\lambda_q-q)=q(q-1)\). It follows that \(L'(0)=\mu_q\) and \(L''(0)=\sigma_q^2\) with the positive constants displayed above. Consequently
\[
L(s)=\mu_qs+\tfrac12\sigma_q^2s^2+O_q(|s|^3).
\]
For each fixed real \(u\), substitute \(s=iu/\sqrt{n\sigma_q^2}\), cancel the centering factor, and obtain the limiting characteristic function \(e^{-u^2/2}\). Lévy's continuity theorem gives the normal limit; differentiation of the uniform analytic estimate gives the mean and variance errors. Finally, the stated ordered large-field limits follow directly from \(\Delta_q/q\to\sqrt5\).

**Step 4: finite-group interpretation.** For odd \(p\), the cycle graphical group has an elementary abelian quotient \(G/G'\cong\mathbb F_p^n\) and \(G'\cong\mathbb F_p^{E(C_n)}\), with the commutator pairing given componentwise by the alternating edge matrices. The inverse-image correspondence between subgroups containing \(G'\) and subspaces of \(G/G'\) identifies a subgroup as abelian exactly when its quotient plane is isotropic. Since \(|E(C_n)|=n\), the relevant abelian subgroups have order \(p^{n+2}\), as stated.

## Verification
A standalone `verify.py` enumerates all ordered pairs of finite-field vectors independently of the graph-support argument, discards linearly dependent pairs, checks every cycle-edge determinant, divides resulting support counts by \(|\mathrm{GL}_2(\mathbb F_q)|\), and compares with both an independent induced-component subset count and an independent polynomial trace recurrence. Exhaustive direct enumerations cover \((q,n)=(2,3),(2,4),(2,5),(2,6),(2,7),(3,3),(3,4),(3,5),(5,3),(5,4)\). The component and recurrence methods are additionally compared for \(q\in\{2,3,4,5,7,9\}\) and \(3\le n\le12\); these last comparisons are polynomial identities and do not require explicit field arithmetic. Numerical derivatives of larger finite polynomials agree with the analytic constants, but no finite computation is used as proof of the limit.

## Relationship to prior work
Qiao's August 2024 work proves polynomial enumeration of totally isotropic subspaces of graphical alternating matrix spaces and interprets them as abelian subgroups of graphical class-two groups; its Lemma 2.3 supplies a related row-dependence criterion. That general finite enumeration subsumes **unrefined** rank-two subgroup counts in principle, so those counts are not claimed as an independent novelty. The present claim concerns the support-refined exact transfer and, decisively, the fixed-field Gaussian support law with explicit mean, variance and golden-ratio limit for growing cycles. Rossmann (2021/2022) enumerates conjugacy classes by size in graphical groups; that invariant does not determine the support distribution of abelian subgroups. Previously reported cycle graphical-group character-degree formulas count irreducible representations, not the subgroup support statistic considered here.

## Limitations
No exhaustive publication-priority claim is made. Weighted induced-component partition functions and transfer-matrix Gaussian limits are classical tools; a prior specialization under Potts/vertex-random-cluster terminology may exist. The labelled-support statistic is presentation-dependent. The group claim is restricted to odd prime fields, since for extension fields arbitrary additive subgroups need not be linear over the field. Neither the number of **all** abelian subgroups nor the support law for quotient dimension three or larger is established here.

## References
- Y. Qiao, *A q-analogue of graph independence polynomials with a group-theoretic interpretation*, arXiv:2408.09963v1 (first posted 2024-08-19), especially Theorem 1.2, Section 1.3, and Lemma 2.3. https://arxiv.org/abs/2408.09963
- T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564v1 (first posted 2021-07-12), especially Theorem A and Section 1.6. https://arxiv.org/abs/2107.05564
- P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009, Chapter IX (quasi-powers and transfer methods); the characteristic-function argument needed here is given explicitly above.
