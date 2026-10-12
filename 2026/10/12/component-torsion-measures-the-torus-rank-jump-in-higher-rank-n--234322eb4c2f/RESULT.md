# Component torsion measures the torus-rank jump in higher-rank Néron models
## Finding
Let \(V\) be a valuation ring with algebraically closed fraction field \(F\), let \(E_F\) be a semi-abelian variety of dimension \(g\), and let \(N\) be its Néron model. Write \(t_\eta\) for the torus rank of \(E_F\). For a point \(s\in\operatorname{Spec}(V)\), write \(t_s\) for the torus rank of the semi-abelian identity component \(N_s^0\), and put
\[
\Phi_s=\pi_0(N_s).
\]
Then for every positive integer \(m\),
\[
|\Phi_s[m]|=m^{t_s-t_\eta}.
\]
Consequently \(t_s\ge t_\eta\), and the torsion subgroup of the divisible component group is
\[
\Phi_{s,\mathrm{tors}}\cong(\mathbf Q/\mathbf Z)^{t_s-t_\eta}.
\]
Thus the jump in torus rank is exactly the Prüfer rank of the torsion in the Néron component group.

## Assumptions and scope
The fraction field \(F\) is algebraically closed. Kaib--Werner prove that in this setting the Néron model exists for semi-abelian varieties and has semi-abelian fiberwise identity component. In particular, residue fields at non-generic points of \(\operatorname{Spec}(V)\) are algebraically closed. The statement concerns the algebraic Néron model and every point \(s\) of the valuation spectrum.

Only the torsion subgroup of \(\Phi_s\) is determined. A divisible abelian group can also contain a torsion-free \(\mathbf Q\)-vector-space summand, and the argument does not determine that summand.

## Proof
Kaib--Werner prove two inputs in the algebraically closed setting: first, \(\Phi_s\) is divisible; second, for every nonzero integer \(m\), multiplication
\[
[m]_N:N\longrightarrow N
\]
is finite, flat, and surjective.

Fix a positive integer \(m\). Its kernel \(N[m]\) is therefore finite flat over \(V\). Since \(\operatorname{Spec}(V)\) is connected, the rank of this finite flat group scheme is the rank of its generic fiber. A semi-abelian variety of dimension \(g\) and torus rank \(t_\eta\) is an extension of an abelian variety of dimension \(g-t_\eta\) by a torus of rank \(t_\eta\). Hence
\[
\operatorname{rk}_V N[m]=m^{2(g-t_\eta)}m^{t_\eta}=m^{2g-t_\eta}.
\]
After base change to the residue field at \(s\), the finite group scheme \(N_s[m]\) has the same length.

The identity component \(N_s^0\) is semi-abelian of dimension \(g\) and torus rank \(t_s\), so
\[
\operatorname{length} N_s^0[m]=m^{2g-t_s}.
\]
We now identify the components of \(N_s[m]\). If \(c\in\Phi_s[m]\), choose a point \(x\) in the component \(c\); this is possible because the residue field is algebraically closed. Since \(mc=0\), the point \(mx\) belongs to \(N_s^0\). Multiplication by \(m\) on a semi-abelian variety is surjective, so choose \(y\in N_s^0\) with \(my=mx\). Then \(x-y\in N_s[m]\) lies in the component \(c\). Conversely, every point of \(N_s[m]\) lies in an \(m\)-torsion component. Therefore the nonempty intersections of \(N_s[m]\) with components of \(N_s\) are indexed exactly by \(\Phi_s[m]\), and each is a translate of \(N_s^0[m]\). Taking lengths gives
\[
m^{2g-t_\eta}=|\Phi_s[m]|\,m^{2g-t_s},
\]
which proves
\[
|\Phi_s[m]|=m^{t_s-t_\eta}.
\]
The left side is an integer for every \(m\), so \(t_s\ge t_\eta\).

Finally, Kaib--Werner's divisibility theorem and the classification of divisible abelian groups imply that
\[
\Phi_{s,\mathrm{tors}}\cong\bigoplus_p C_{p^\infty}^{(r_p)}.
\]
Putting \(m=p\) in the formula gives \(|\Phi_s[p]|=p^{t_s-t_\eta}\), hence \(r_p=t_s-t_\eta\) for every prime \(p\). Reassembling the primary parts yields
\[
\Phi_{s,\mathrm{tors}}\cong(\mathbf Q/\mathbf Z)^{t_s-t_\eta}.
\]

## Verification
The proof uses scheme-theoretic lengths, so it remains valid when the residue characteristic divides \(m\); no reducedness of the torsion group schemes is assumed. The rank formula for multiplication by \(m\) on a semi-abelian variety follows multiplicatively from degree \(m^{2a}\) on an abelian part of dimension \(a\) and degree \(m^t\) on a rank-\(t\) torus.

The two nonstandard model-theoretic inputs were checked in the full text of arXiv:2610.01354v1: Lemma 5.11 proves divisibility of every fiberwise component group, and Proposition 6.12(2) proves that multiplication by every nonzero integer is finite, flat, and surjective on the Néron model. The same source explicitly exhibits the Tate-curve component group \(\mathbf Q/v_p(q)\mathbf Z\), which agrees with the formula when the generic torus rank is \(0\) and the special torus rank is \(1\).

## Relationship to prior work
Kaib--Werner prove the qualitative divisibility of \(\Phi_s\), the finite-flat-surjective multiplication theorem, and a quasi-compactness criterion. In the proof of that criterion they compare torsion cardinalities only after assuming the component group is trivial. The formula above removes that assumption and records the exact deficit in torsion as the torus rank changes.

There is an important classical rank-one analogue. Grothendieck proved that, for a semistable abelian variety over a discretely valued field, the direct limit of Néron component groups under ramified finite extensions is \(\operatorname{Hom}(X(T),\mathbf Q/\mathbf Z)\), where \(T\) is the toric part of the eventual special identity component. This explains the same \(\mathbf Q/\mathbf Z\)-phenomenon after passing through all ramification. The present statement instead concerns the actual component group over an arbitrary-rank valuation ring with algebraically closed fraction field, works for a semi-abelian generic fiber with possibly nonzero \(t_\eta\), and gives the exact \(m\)-torsion cardinality at every point of the valuation spectrum.

Targeted searches for the exact formula, its Prüfer-rank formulation, and the semi-abelian higher-rank version found the initiating paper and the classical direct-limit theorem but no statement that implies this arbitrary-rank actual-component formula.

## Limitations
Algebraic closedness of the fraction field is essential to the cited finite-flat-surjective multiplication theorem and to the divisibility statement used here. No formula is asserted for a general discretely valued field before algebraic closure, where component groups can be finite and multiplication on the Néron model need not be surjective. The torsion-free divisible part of \(\Phi_s\), if present, is not determined.

The classical Grothendieck theorem is a close rank-one analogue, so the originality claim is specifically the arbitrary-rank, actual-component, semi-abelian formula above; no claim is made that the underlying \(\mathbf Q/\mathbf Z\) phenomenon is new.

## References
1. Simon Kaib and Annette Werner, *Abeloid varieties over higher rank valued fields: Raynaud uniformization and Néron models*, arXiv:2610.01354v1, 1 October 2026.
2. Alexander Grothendieck, *Modèles de Néron et monodromie*, SGA 7 I, Exposé IX, Lecture Notes in Mathematics 288, Springer, 1972, especially §11.9.
3. Brian Conrad, *Semistable reduction for abelian varieties*, lecture notes, discussion of Grothendieck's component-group direct-limit theorem.
