# Every prescribed finite Nakayama order detects the Auslander–Reiten conjecture

## Result

Let \(k\) be a field, let \(D=\operatorname{Hom}_k(-,k)\), and work with finite-dimensional right modules. Recall that a finite-dimensional algebra \(A\) satisfies the **Auslander–Reiten conjecture (ARC)** if
\[
\operatorname{Ext}_A^i(X,X\oplus A)=0\quad(i>0)
\]
forces \(X\) to be projective. A self-injective algebra \(\Gamma\) satisfies **Tachikawa's second conjecture (TC2)** if
\[
\operatorname{Ext}_\Gamma^i(M,M)=0\quad(i>0)
\]
forces \(M\) to be projective.

The following corner criterion isolates the mechanism behind the two-fold trivial-extension argument.

**Theorem 1 (self-injective corner transfer).** Let \(\Gamma\) be a finite-dimensional self-injective \(k\)-algebra, let \(e\in\Gamma\) be an idempotent, and put \(A=e\Gamma e\). Assume, as left \(A\)-modules,
\[
{}_A e\Gamma\in \operatorname{add}({}_A A\oplus {}_A DA).
\]
If \(\Gamma\) satisfies TC2, then \(A\) satisfies ARC.

More precisely, if \(X\) is a non-projective ARC witness for \(A\), meaning
\[
\operatorname{Ext}_A^i(X,X\oplus A)=0\quad(i>0),
\]
then
\[
F(X):=X\otimes_A e\Gamma
\]
is non-projective and self-orthogonal over \(\Gamma\). Thus any failure of ARC at the corner produces a failure of TC2 upstairs.

For an integer \(r\ge2\), let \(T_r(A)\) be the standard \(r\)-fold trivial extension. It has \(r\) copies of \(A\) on the diagonal and \(r\) cyclic copies of \(DA\) on the adjacent off-diagonal positions. It is self-injective. If \(e\) is any diagonal block idempotent, then
\[
eT_r(A)e\cong A,
\qquad
{}_A eT_r(A)\cong {}_A A\oplus {}_A DA.
\]
Therefore Theorem 1 immediately gives the following uniform extension of the two-fold case.

**Corollary 2 (all fold numbers).** For every \(r\ge2\),
\[
\boxed{\operatorname{TC2}(T_r(A))\Longrightarrow \operatorname{ARC}(A).}
\]
If \(X\) is a non-projective ARC witness for \(A\), then
\[
X_r:=X\otimes_A eT_r(A)
\]
is a non-projective self-orthogonal \(T_r(A)\)-module for every \(r\ge2\).

The standard Nakayama automorphism of \(T_r(A)\) is the cyclic shift of the \(r\) diagonal blocks and has exact order \(r\). Hence the previous statement can be sharpened into a fixed-order reduction.

**Theorem 3 (fixed Nakayama order).** Fix any integer \(r\ge2\). The following universal assertions are equivalent:

1. every finite-dimensional \(k\)-algebra satisfies ARC;
2. every \(r\)-fold trivial extension \(T_r(A)\) satisfies TC2;
3. every finite-dimensional Frobenius \(k\)-algebra admitting a Nakayama automorphism of exact order \(r\) satisfies TC2.

Thus no mixture of Nakayama orders is needed: **TC2 restricted to any one prescribed finite order \(r\ge2\) already detects the full Auslander–Reiten conjecture.**

There is also a quantitative consequence. Since
\[
\dim_k T_r(A)=2r\,\dim_k A,
\]
a single ARC counterexample algebra of dimension \(d\) would produce TC2 counterexample algebras of dimensions
\[
4d,6d,8d,\ldots,
\]
with standard Nakayama automorphisms of exact orders \(2,3,4,\ldots\), respectively.

## Proof of Theorem 1

Let
\[
F=-\otimes_A e\Gamma:\operatorname{mod}A\longrightarrow\operatorname{mod}\Gamma.
\]
For any idempotent \(e\), induction along \(e\) is fully faithful and reflects projectivity: indeed \((FY)e\cong Y\) naturally, and if \(FY\) is projective then a split lift of an epimorphism from a finite free \(A\)-module descends through full faithfulness to split the original epimorphism.

Now let \(X\) satisfy the ARC vanishing condition. Since
\[
{}_A e\Gamma\in\operatorname{add}({}_A A\oplus{}_A DA),
\]
it is enough to show
\(
\operatorname{Tor}_i^A(X,DA)=0
\)
for \(i>0\). Finite-dimensional tensor–Hom duality gives
\[
D\operatorname{Tor}_i^A(X,DA)
\cong
\operatorname{Ext}_A^i(X,DDA)
\cong
\operatorname{Ext}_A^i(X,A)=0.
\]
Hence
\[
\operatorname{Tor}_i^A(X,e\Gamma)=0\qquad(i>0).
\]
If \(P_\bullet\to X\) is a projective resolution, then \(P_\bullet\otimes_A e\Gamma\to FX\) is therefore a projective resolution over \(\Gamma\). Tensor–Hom adjunction yields, for every \(\Gamma\)-module \(Z\),
\[
\operatorname{Ext}_\Gamma^n(FX,Z)
\cong
\operatorname{Ext}_A^n(X,Ze)
\qquad(n\ge0).
\]
Taking \(Z=FX\) and using \((FX)e\cong X\) gives
\[
\operatorname{Ext}_\Gamma^n(FX,FX)
\cong
\operatorname{Ext}_A^n(X,X)=0
\qquad(n>0).
\]
If \(\Gamma\) satisfies TC2, then \(FX\) is projective, and reflection of projectivity forces \(X\) to be projective. This proves the transfer statement. Conversely, if \(X\) is a non-projective ARC witness, the same Ext comparison shows that \(FX\) is self-orthogonal and reflection of projectivity shows that it remains non-projective.

## Proof of Corollary 2

For the standard \(r\)-fold trivial extension with \(r\ge2\), a diagonal idempotent \(e\) cuts out one copy of \(A\), while its row contains exactly one copy of \(A\) and one cyclic copy of \(DA\). Thus
\[
eT_r(A)e\cong A,
\qquad
{}_A eT_r(A)\cong A\oplus DA.
\]
The algebra \(T_r(A)\) is self-injective, so Theorem 1 applies verbatim.

## Proof of Theorem 3

The implication (1) \(\Rightarrow\) (3) is immediate: a finite-dimensional Frobenius algebra is self-injective, so \(\operatorname{Ext}^i(M,\Gamma)=0\) automatically for \(i>0\); ARC for \(\Gamma\) therefore specializes to TC2.

For (3) \(\Rightarrow\) (2), the standard \(r\)-fold trivial extension is Frobenius, and its Nakayama automorphism is the cyclic block shift of exact order \(r\).

Finally, (2) \(\Rightarrow\) (1) is Corollary 2 applied separately to every finite-dimensional algebra \(A\). This proves the equivalence.

## Relation to prior work

Enomoto proved in 2026 that TC2 for the **two-fold** trivial extension \(T_2(A)\) implies ARC for \(A\). His proof develops the idempotent-induction lemma used above: induction is fully faithful and reflects projectivity, and a Tor-vanishing hypothesis gives the Ext comparison. Theorem 1 abstracts the exact module-theoretic hypothesis needed for that argument, while Corollary 2 applies it to every standard \(r\)-fold trivial extension with \(r\ge2\).

The structure of \(r\)-fold trivial extensions is classical. Chan, Darpö, Iyama and Marczinzik record that \(T_r(A)\) is self-injective and that its Nakayama automorphism is the cyclic one-step shift; in particular \(T_r(A)\) is symmetric exactly for \(r=1\). Their work studies periodicity, fractional Calabi–Yau properties and representation-finiteness, not the ARC/TC2 reduction proved here.

Broader transfer results for ARC under singular equivalences, recollements and change-of-rings functors are known, notably work of Chen, Hu, Qin and Wang. The present criterion is a direct self-injective-corner mechanism tailored to self-orthogonality and the \(A\oplus DA\) left-module decomposition.

Targeted searches using “r-fold trivial extension”, “Tachikawa conjecture”, “Auslander–Reiten conjecture”, “Nakayama automorphism/order”, “idempotent corner”, and equivalent orbit-algebra terminology did not locate the all-\(r\) transfer, the fixed-order equivalence, or the counterexample-proliferation statement. Originality is therefore claimed only to the best of our knowledge.

## Limitations

The result is stated over a field so that the duality \(D=\operatorname{Hom}_k(-,k)\) and the standard finite-dimensional Frobenius/Nakayama formalism apply directly. Enomoto's two-fold theorem is more general, treating artin algebras over a commutative artinian base.

The fixed-order theorem is deliberately stated for \(r\ge2\). The standard one-fold trivial extension \(T_1(A)=A\ltimes DA\) is symmetric, but the diagonal-corner realization used here no longer gives \(eT_1(A)e\cong A\) with \({}_AeT_1(A)\cong A\oplus DA\). No claim is made here that the analogous universal reduction for Nakayama order \(1\) is true or false.

The phrase “admits a Nakayama automorphism of exact order \(r\)” is used because Nakayama automorphisms are determined only up to inner automorphism in general. The canonical cyclic shift on \(T_r(A)\) has exact order \(r\), which is all that is required for the reduction.

Enomoto's source is a recent first version and may be revised. The fixed-order consequence is an elementary synthesis once the idempotent-induction mechanism and the standard \(r\)-fold trivial-extension structure are placed together, so an equivalent observation may exist under orbit-algebra terminology even though the targeted searches above did not locate one.

## References

1. H. Enomoto, *Tachikawa's second conjecture implies the Auslander–Reiten conjecture*, arXiv:2609.19172v1 (2026). https://arxiv.org/abs/2609.19172
2. A. Chan, E. Darpö, O. Iyama, R. Marczinzik, *Periodic trivial extension algebras and fractionally Calabi–Yau algebras*, Annales scientifiques de l'École normale supérieure 58 (2025), 463–510. https://doi.org/10.24033/asens.2610
3. Y. Chen, W. Hu, Y. Qin, R. Wang, *Singular equivalences and Auslander-Reiten conjecture*, Journal of Algebra 623 (2023), 42–63. https://arxiv.org/abs/2011.02729
