# Multiplier repair and arbitrary-multiplicity rigidity for minimal backward-shift projections

## Statement

Let \(K\) be a complex Hilbert space and let
\[
B=S^*\otimes I_K
\]
act on \(H^2(\mathbb D)\otimes K\). Let \(M\ne\{0\}\) be a minimal closed
\(B\)-invariant subspace. For \(\eta\in K\), let
\[
P_\eta:H^2\otimes K\to H^2
\]
be the coefficient map in direction \(\eta\).

Then there is a single closed \(S^*\)-invariant subspace \(V\subseteq H^2\) such
that, for every \(\eta\in K\),
\[
P_\eta(M)=\{0\}
\quad\text{or}\quad
\overline{P_\eta(M)}=V.
\]
Whenever \(P_\eta(M)\ne\{0\}\), the restriction \(P_\eta|_M\) is injective.

A complementary bounded-domain identity explains how to avoid unrestricted
orbit synthesis. If
\[
g\in H^2,\qquad f\in H^\infty,
\]
then the Hankel-expression used in backward-shift synthesis satisfies
\[
L_g f=M_{f^\sharp}^*g,\qquad
\|L_gf\|_2\le\|f\|_\infty\|g\|_2.
\]

The classical BMOA boundary and the explicit counterexample to unrestricted
all-\(H^2\) synthesis are prior results and are not claimed here.

## Proof

For \(\eta\in K\), put
\[
V_\eta=\overline{P_\eta(M)}.
\]
Since \(P_\eta B=S^*P_\eta\), every \(V_\eta\) is \(S^*\)-invariant. If
\(V_\eta\ne\{0\}\), then
\[
M\cap\ker P_\eta
\]
is a closed \(B\)-invariant subspace of the minimal space \(M\). It cannot equal
\(M\), so it is zero. Thus every nonzero coefficient map is injective on \(M\).

Take \(\eta,\xi\) with both image closures nonzero. We prove
\(V_\eta\subseteq V_\xi\). If \(V_\xi=H^2\), there is nothing to prove. Otherwise
Beurling's theorem gives an inner function \(\theta\) with
\[
V_\xi=K_\theta=H^2\ominus\theta H^2=\ker M_\theta^*.
\]
Because \(M\) is invariant under \(S^*\otimes I_K\), its orthogonal complement is
invariant under \(S\otimes I_K\), hence under \(M_\theta\otimes I_K\).
Consequently \(M\) is invariant under
\[
M_\theta^*\otimes I_K.
\]

If \(V_\eta\not\subseteq V_\xi\), choose \(u\in M\) with
\(P_\eta u\notin K_\theta\). Put
\[
v=(M_\theta^*\otimes I_K)u\in M.
\]
Then
\[
P_\xi v=M_\theta^*P_\xi u=0,
\]
but
\[
P_\eta v=M_\theta^*P_\eta u\ne0.
\]
Thus \(v\ne0\) belongs to \(M\cap\ker P_\xi\), contradicting injectivity.
Therefore \(V_\eta\subseteq V_\xi\), and symmetry gives equality.

For the bounded-domain identity, coefficient comparison gives
\[
L_gf=M_{f^\sharp}^*g.
\]
The multiplier bound immediately yields
\[
\|L_gf\|_2\le\|f\|_\infty\|g\|_2.
\]

## Prior boundary

A published 18 September 2026 result already identifies the relevant orbit-synthesis
operator as a Hankel matrix, gives the exact BMOA boundedness threshold, and provides
an explicit \(H^2\) counterexample to the universal synthesis claim in
arXiv:2609.19311. Those facts are prior input.

The surviving contribution is the direct multiplier-domain repair and, chiefly, the
common-shadow theorem above for arbitrary Hilbert multiplicity and arbitrary
coefficient directions.

## Limitations

The result does not solve the invariant subspace problem and does not validate every
argument in the motivating preprint. The BMOA criterion and Beurling's theorem are
classical. The full text of the very recent motivating preprint was not available in
the accessible text interface during this assessment, so an implicit equivalent
arbitrary-multiplicity lemma remains a residual prior-art risk.

## References

1. M. dos Santos Ferreira and J. M. Ribeiro do Carmo,
   *Projections and minimal invariant subspaces in the Hardy space over the bidisk*,
   arXiv:2609.19311.
2. Published result, *The sharp BMOA boundary for a backward-shift Hankel operator*,
   18 September 2026.
3. Classical Nehari--Fefferman and Beurling model-space theorems.
