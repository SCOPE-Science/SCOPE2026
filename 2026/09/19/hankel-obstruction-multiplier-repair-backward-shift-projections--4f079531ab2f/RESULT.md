# Hankel obstruction and multiplier repair for minimal backward-shift projections

## Statement

Let \(S^*\) denote the backward shift on \(H^2(\mathbb D)\). For
\[
g(z)=\sum_{n\ge 0}\alpha_n z^n\in H^2(\mathbb D),
\]
consider the formal operator used in Lemma 2.1 of do Carmo--Ferreira, arXiv:2609.19311v1,
\[
L_g f(z)=\sum_{\ell\ge0}\langle S^{*\ell}g,f^\sharp\rangle z^\ell,
\qquad
f^\sharp(z)=\overline{f(\bar z)}.
\]
If \(f(z)=\sum_{i\ge0}\beta_i z^i\), then formally
\[
L_g f(z)=\sum_{\ell\ge0}\left(\sum_{i\ge0}\beta_i\alpha_{\ell+i}\right)z^\ell.
\]
Thus its matrix is the Hankel matrix \((\alpha_{\ell+i})_{\ell,i\ge0}\).

The following facts hold.

**Theorem 1 (exact domain obstruction).** The assertion that \(L_g:H^2\to H^2\) is well defined for every \(g\in H^2\) is false. On polynomials, \(L_g\) extends to a bounded operator on all of \(H^2\) if and only if
\[
zg\in \mathrm{BMOA},
\]
equivalently \(g\in\mathrm{BMOA}\). In particular, for
\[
g(z)=\sum_{n=0}^\infty (n+1)^{-3/4}z^n\in H^2
\]
and
\[
f(z)=\sum_{n=0}^\infty (n+1)^{-3/4}z^n\in H^2,
\]
the coefficient formula for \(L_gf\) produces a sequence that is not square summable, so \(L_gf\notin H^2\).

**Theorem 2 (bounded multiplier domain).** For arbitrary \(g\in H^2\) and \(f\in H^\infty\), the expression needed in the projection argument is always well defined and satisfies
\[
L_g f=M_{f^\sharp}^*g,
\qquad
\|L_g f\|_2\le \|f\|_\infty\|g\|_2.
\]

**Theorem 3 (multiplier repair, arbitrary multiplicity).** Let \(K\) be any complex Hilbert space and let
\[
B=S^*\otimes I_K
\]
on \(H^2(\mathbb D)\otimes K\). If \(M\ne\{0\}\) is a minimal closed \(B\)-invariant subspace, then there is a single closed \(S^*\)-invariant subspace \(V\subseteq H^2(\mathbb D)\) such that for every \(\eta\in K\), with coefficient map
\[
P_\eta:H^2\otimes K\to H^2,
\]
one has
\[
P_\eta(M)=\{0\}
\quad\text{or}\quad
\overline{P_\eta(M)}=V.
\]
Moreover, whenever \(P_\eta(M)\ne\{0\}\), the restriction \(P_\eta|_M\) is injective.

For \(K=H^2(\mathbb D_w)\), this gives the intended common one-variable shadow for minimal \(T_z^*\)-invariant subspaces of \(H^2(\mathbb D^2)\), while avoiding the invalid all-\(H^2\) synthesis assertion in Lemma 2.1 of arXiv:2609.19311v1.

## Proof of Theorem 1

For \(g(z)=\sum\alpha_nz^n\) and a polynomial \(f(z)=\sum\beta_i z^i\), direct coefficient calculation gives the Hankel matrix
\[
H_g=(\alpha_{\ell+i})_{\ell,i\ge0}.
\]
The classical Nehari theorem identifies bounded Hankel matrices on \(\ell_2\) with bounded Hankel forms. With the conventional shifted analytic symbol
\[
b(z)=zg(z)=\sum_{n\ge0}\alpha_n z^{n+1},
\]
the standard Hankel matrix of \(b\) has entries \(\alpha_{\ell+i}\). Hence \(H_g\) is bounded if and only if \(zg\in\mathrm{BMOA}\), equivalently \(g\in\mathrm{BMOA}\).

There is also a completely explicit counterexample requiring no abstract criterion. Put
\[
\alpha_n=\beta_n=(n+1)^{-3/4}.
\]
Both sequences are in \(\ell_2\). For the formal output coefficients
\[
c_\ell=\sum_{i=0}^\infty (i+1)^{-3/4}(\ell+i+1)^{-3/4},
\]
each scalar series converges, but restricting to \(0\le i\le\ell\) yields
\[
\begin{aligned}
c_\ell
&\ge (\ell+1)(\ell+1)^{-3/4}\,[2(\ell+1)]^{-3/4}\\
&=2^{-3/4}(\ell+1)^{-1/2}.
\end{aligned}
\]
Therefore \(\sum_\ell |c_\ell|^2=\infty\), so the displayed formula does not define an \(H^2\) vector.

Quantitatively, if
\[
f_N=N^{-1/2}\sum_{i=0}^{N-1}z^i,
\]
then \(\|f_N\|_2=1\) and the first \(N\) output coordinates give
\[
\|L_g f_N\|_2\ge 2^{-3/4}N^{1/4}.
\]
Thus even the polynomially defined operators are not uniformly bounded.

## Proof of Theorem 2

If \(f(z)=\sum\beta_i z^i\in H^\infty\), then
\[
f^\sharp(z)=\sum\overline{\beta_i}z^i\in H^\infty,
\qquad \|f^\sharp\|_\infty=\|f\|_\infty.
\]
The coefficient of \(z^\ell\) in \(M_{f^\sharp}^*g\) is exactly
\[
\sum_{i\ge0}\beta_i\alpha_{\ell+i}
=\langle S^{*\ell}g,f^\sharp\rangle.
\]
Hence \(L_gf=M_{f^\sharp}^*g\), and the multiplier norm estimate gives
\[
\|L_gf\|_2\le\|f\|_\infty\|g\|_2.
\]

## Proof of Theorem 3

For \(\eta\in K\), let
\[
V_\eta=\overline{P_\eta(M)}.
\]
Because \(P_\eta B=S^*P_\eta\), every \(V_\eta\) is \(S^*\)-invariant. Also, if \(V_\eta\ne\{0\}\), then
\[
M\cap\ker P_\eta
\]
is a closed \(B\)-invariant subspace of \(M\). Minimality forces it to be \(\{0\}\), since it cannot equal \(M\). Thus every nonzero coefficient map is injective on \(M\).

Now let \(V_\eta,V_\xi\ne\{0\}\). We prove \(V_\eta\subseteq V_\xi\). If \(V_\xi=H^2\), this is automatic. Otherwise Beurling's theorem gives an inner function \(\theta\) such that
\[
V_\xi=K_\theta:=H^2\ominus\theta H^2
=\ker M_\theta^*.
\]
Assume for contradiction that \(V_\eta\not\subseteq V_\xi\). Since \(P_\eta(M)\) is dense in \(V_\eta\), choose \(u\in M\) with
\[
P_\eta u\notin V_\xi.
\]
The orthogonal complement \(M^\perp\) is invariant under \(S\otimes I_K\), hence under \(M_\theta\otimes I_K\); consequently \(M\) is invariant under
\[
A=M_\theta^*\otimes I_K.
\]
Set \(v=Au\in M\). Coefficient maps intertwine \(A\) with \(M_\theta^*\), so
\[
P_\xi v=M_\theta^*P_\xi u=0,
\]
while
\[
P_\eta v=M_\theta^*P_\eta u\ne0.
\]
Hence \(v\ne0\) lies in \(M\cap\ker P_\xi\), contradicting injectivity of \(P_\xi|_M\). Therefore \(V_\eta\subseteq V_\xi\); exchanging \(\eta\) and \(\xi\) gives equality.

This argument uses only scalar Beurling theory and the \(H^\infty\) functional calculus of the backward shift. It does not require orthogonality of coefficient directions or a coordinate-by-coordinate case split.

## Relation to the recent source

The 2026 preprint arXiv:2609.19311v1 states in Lemma 2.1 that the displayed \(L_g\) is well defined on all of \(H^2\) for every \(g\in H^2\), and subsequently uses unrestricted \(\ell_2\)-coefficient synthesis. The explicit \((n+1)^{-3/4}\) example above disproves that lemma.

The same source's main intended rigidity phenomenon can nevertheless be recovered without that lemma. Theorem 3 proves a stronger formulation: it applies to a backward shift of arbitrary Hilbert multiplicity and shows that all nonzero coefficient shadows of a minimal invariant subspace have one common model space.

## Limitations

This result does not solve the invariant subspace problem and does not assert that every other argument in arXiv:2609.19311v1 or its earlier related work is repaired. The BMOA boundedness criterion is a classical consequence of Nehari's theorem and is not claimed as new. The originality claim concerns the explicit obstruction in the cited 2026 construction and the multiplier-based arbitrary-multiplicity repair of its projection-rigidity mechanism, to the best of our knowledge. A residual prior-art risk remains that the arbitrary-multiplicity common-shadow lemma is implicit in older vector-valued model-space or universal-shift literature.

## References

1. J. M. R. do Carmo and M. S. Ferreira, *Projections and minimal invariant subspaces in the Hardy space over the bidisk*, arXiv:2609.19311v1 (2026), https://arxiv.org/abs/2609.19311.
2. J. M. R. do Carmo and M. S. Ferreira, *On the invariant subspace problem via universal Toeplitz operators on the Hardy space \(H^2(\mathbb D^2)\)*, arXiv:2309.03427 (2023), https://arxiv.org/abs/2309.03427.
3. Z. Nehari, *On bounded bilinear forms*, Ann. of Math. 65 (1957), 153--162. A modern statement of the BMOA/Hankel criterion is summarized at https://doi.org/10.1112/jlms.12588.
4. Classical Beurling model-space description: a closed nonzero proper \(S^*\)-invariant subspace of \(H^2\) is \(K_\theta=H^2\ominus\theta H^2\) for an inner \(\theta\).
