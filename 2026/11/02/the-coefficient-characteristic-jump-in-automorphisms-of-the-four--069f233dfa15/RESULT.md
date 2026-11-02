# The coefficient-characteristic jump in automorphisms of the four-element dihedral quandle algebra

## Finding

Let \(K\) be **any field**, and let \(E=K[R_4]\) be the four-dimensional (not necessarily associative) quandle algebra on \(e_0,e_1,e_2,e_3\), with \(e_i e_j=e_{2j-i\pmod 4}\). All automorphisms below are **\(K\)-linear algebra automorphisms**. Then

\[
\operatorname{Aut}_K(E)\cong
\begin{cases}
(K^\times\times K^\times)\rtimes C_2,&\operatorname{char}K\ne2,\\
(K^+)^4\rtimes C_2,&\operatorname{char}K=2.
\end{cases}
\]

In the first case the involution exchanges the two multiplicative factors; in the second, identify \((K^+)^4\) with the additive group \(M_2(K)\), and the involution sends \(C\) to \(PCP\), where \(P=\begin{pmatrix}0&1\\1&0\end{pmatrix}\). More precisely, the exact matrices of all automorphisms are given in the proof below. For \(K=\mathbb F_q\), the exact orders are \(2(q-1)^2\) for odd \(q\) and \(2q^4\) for even \(q\).

## Assumptions and scope

The field is arbitrary, including infinite, imperfect and characteristic-two fields. The quandle is the dihedral quandle of order four, not a general even dihedral quandle. Products in \(E\) extend \(e_i e_j=e_{2j-i\pmod4}\) bilinearly; the indices lie in \(\mathbb Z/4\mathbb Z\). Only \(K\)-linear bijections preserving this multiplication are classified, not semilinear permutations or automorphisms of the underlying quandle alone.

Put \(V=E\) and define the right annihilator by \(W=\{y\in E:xy=0\text{ for all }x\in E\}\). For \(y=\sum y_i e_i\), define its even/odd coefficient sums \(a(y)=y_0+y_2\) and \(b(y)=y_1+y_3\). Directly from the four multiplication rows, \(y\in W\) if and only if \(a(y)=b(y)=0\), so
\[
W=K(e_0-e_2)\oplus K(e_1-e_3)
\]
for every characteristic (subtraction equals addition in characteristic two). In particular, \(W\) is intrinsically characteristic, and every algebra automorphism preserves it.

## Proof

**Odd characteristic, and indeed every characteristic different from two.** Choose the ordered direct-sum basis
\[
s_0=e_0+e_2,\quad s_1=e_1+e_3,\qquad d_0=e_0-e_2,\quad d_1=e_1-e_3,
\]
with \(U=Ks_0\oplus Ks_1\) and \(W=Kd_0\oplus Kd_1\). Let \(\epsilon(y)=a(y)+b(y)\), \(\delta(y)=a(y)-b(y)\), and \(H=\operatorname{diag}(1,-1)\) on \(W\). Calculation on the four basis vectors gives the **complete** product rule
\[
(u+w)y=\epsilon(y)u+\delta(y)Hw\qquad(u\in U,\ w\in W,\ y\in E).
\tag{1}
\]
The two forms \(\epsilon\) and \(\delta\) vanish on \(W\), are linearly independent on \(U\), and \(\epsilon\ne0\).

Because the right annihilator is invariant, any putative automorphism \(F\) has matrix
\[
F=\begin{pmatrix}A&0\\ C&D\end{pmatrix},\qquad A,D\in\operatorname{GL}_2(K),\ C\in M_2(K).
\tag{2}
\]
Applying the algebra identity \(F(xy)=F(x)F(y)\) to the \(U\)-coordinates in (1) yields \(\epsilon(Ay)=\epsilon(y)\), viewing these forms on \(U\). Applying it to \(x\in W\) yields
\[
\delta(y)DH=\delta(Ay)HD\qquad(y\in U).
\tag{3}
\]
Since \(D,H\) are invertible, (3) implies that \(\delta\circ A=\beta\delta\) and \(DH=\beta HD\) for some \(\beta\in K^\times\). Squaring the conjugacy identity \(DHD^{-1}=\beta H\) gives \(\beta^2=1\), so \(\beta\in\{1,-1\}\).

Now (1) applied to \(x\in U\) and compared in the \(W\)-coordinate yields
\[
\epsilon(y)C=\delta(Ay)HC\qquad(y\in U).
\tag{4}
\]
The forms \(\epsilon\) and \(\delta\circ A\) are independent, so choose \(y\) with \(\epsilon(y)\ne0\) and \(\delta(Ay)=0\). Equation (4) forces \(C=0\). The pair \((\epsilon,\delta)\) is a basis of \(U^*\), so the conditions \(\epsilon\circ A=\epsilon\), \(\delta\circ A=\beta\delta\) determine \(A\) uniquely: \(A=I_2\) if \(\beta=1\), and \(A=P\) if \(\beta=-1\). The identity \(DH=\beta HD\) says precisely that \(D\) is diagonal with nonzero entries when \(\beta=1\), or antidiagonal with nonzero entries when \(\beta=-1\). All these matrices satisfy (1) directly. Thus the full group is the diagonal two-torus extended by an involution exchanging its two coordinates, proving the first case.

**Characteristic two.** Take instead the ordered basis
\[
p_0=e_0,\quad p_1=e_1,\qquad d_0=e_0+e_2,\quad d_1=e_1+e_3.
\]
Again \(U=Kp_0\oplus Kp_1\) complements \(W=Kd_0\oplus Kd_1\). In the identifications \(U\cong K^2\), \(W\cong K^2\), let \(\lambda(v)=v_0+v_1\), \(N(u,v)=(u_0v_1,u_1v_0)\). Direct multiplication gives
\[
(u,w)(v,z)=\bigl(\lambda(v)u,\ \lambda(v)w+N(u,v)\bigr).
\tag{5}
\]
Every possible automorphism still has the block form (2), and substitution into (5) shows that it preserves multiplication **if and only if**
\[
\lambda\circ A=\lambda,\qquad DN(u,v)=N(Au,Av)\quad\text{for all }u,v\in K^2,
\tag{6}
\]
with \(C\) unrestricted.

Write the columns of \(A\) as \((a,c)^T\) and \((b,d)^T\). Since \(N(p_0,p_0)=N(p_1,p_1)=0\), (6) gives \(ac=bd=0\). Moreover \(\lambda\circ A=\lambda\) gives \(a+c=b+d=1\). Over any field of characteristic two, each column must therefore be either \((1,0)^T\) or \((0,1)^T\). Invertibility makes the two columns different: \(A=I_2\) or \(A=P\). Finally \(N(p_0,p_1)=d_0\), \(N(p_1,p_0)=d_1\) forces respectively \(D=I_2\) or \(D=P\). Consequently the full automorphism set is exactly
\[
\left\{\begin{pmatrix}P^\sigma&0\\C&P^\sigma\end{pmatrix}:
\sigma\in\{0,1\},\ C\in M_2(K)\right\}.
\tag{7}
\]
The subgroup with \(\sigma=0\) is isomorphic to \((M_2(K),+)\). Conjugation by \(\operatorname{diag}(P,P)\) takes its lower-left block \(C\) to \(PCP\), proving the stated split semidirect product. This argument proves exhaustiveness, including the characteristic-two exceptions. Counting the displayed matrices over finite fields proves both order formulas.

## Verification

The independent finite enumerator `verify.py` constructs the original four-element multiplication table, changes to the displayed characteristic-dependent bases, then enumerates *every* invertible block map preserving the intrinsic right annihilator. It checks all sixteen basis-product identities directly, without imposing the asserted group structure while testing membership. The actual run gives:

```
F_2: 576 annihilator-preserving invertible matrices checked, 32 automorphisms; expected 32: PASS
F_3: 186624 annihilator-preserving invertible matrices checked, 8 automorphisms; expected 8: PASS
VERIFY_OK
```

Run `python verify.py` from a directory containing the standalone script, using Python 3 and its standard library. The finite tests are consistency checks; the argument above proves the statements for every field, without finite extrapolation. In particular, the large characteristic-two group is not inferred from a sample.

## Relationship to prior work

Bardakov, Passi and Singh determined \(\operatorname{Aut}_{\mathbb Z}(\mathbb Z[R_4])\cong (C_2\times C_2)\rtimes C_2\), a result **not claimed as new** here. Their integral coefficient result is not a classification of field-coefficient automorphisms; in particular it does not imply the four-dimensional additive symmetry in characteristic two. Sangare and Ta's 2026 work computes automorphisms of trivial and many dihedral quandle algebras and gives an embedding for the even dihedral case when the coefficient domain has characteristic different from two, but not the complete arbitrary-field groups above. The present classification supplies a coefficient-sensitive structural boundary in the smallest nontrivial even dihedral case. Neither the general even-dihedral integral problem nor higher-order quandle algebras are settled by it.

## Limitations

The theorem concerns exactly \(R_4\) and field coefficients. It makes no statement about \(R_{4m}\) for \(m>1\), rings with zero divisors, or scheme-theoretic automorphism functors. Existing work already treats the integral \(R_4\) special case. Although targeted literature and research-record comparisons did not find the arbitrary-field formulas, an equivalent unindexed calculation remains a possible historical-priority risk. The numerical verifier checks only \(\mathbb F_2\) and \(\mathbb F_3\); correctness for other fields is from the written proof.

## References

1. B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550, first submitted August 3, 2026. See Section 4, especially Problem 4.14 and Theorem 4.15. https://arxiv.org/abs/2608.01550
2. V. G. Bardakov, I. B. S. Passi and M. Singh, *Zero-divisors and idempotents in quandle rings*, arXiv:2001.06843, first submitted January 19, 2020; Osaka Journal of Mathematics 59 (2022), 611–637. See Theorem 6.4. https://arxiv.org/abs/2001.06843
