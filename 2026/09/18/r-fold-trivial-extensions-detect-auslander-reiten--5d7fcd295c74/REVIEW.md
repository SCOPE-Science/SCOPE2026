# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** The corner theorem reduces to three standard and directly checkable facts. First, induction \(F=-\otimes_A e\Gamma\) along an idempotent is fully faithful and reflects projectivity. Second, the hypothesis \({}_Ae\Gamma\in\operatorname{add}(A\oplus DA)\), together with \(\operatorname{Ext}_A^{>0}(X,A)=0\), gives \(\operatorname{Tor}_{>0}^A(X,e\Gamma)=0\) via
\[
D\operatorname{Tor}_i^A(X,DA)\cong\operatorname{Ext}_A^i(X,DDA)\cong\operatorname{Ext}_A^i(X,A).
\]
Third, the resulting induced projective resolution gives
\[
\operatorname{Ext}_\Gamma^n(FX,FX)\cong\operatorname{Ext}_A^n(X,X).
\]
Thus TC2 upstairs forces projectivity of \(FX\), and projectivity reflection forces projectivity of \(X\).

For the standard \(r\)-fold trivial extension with \(r\ge2\), a diagonal corner has \(eT_r(A)e\cong A\) and \({}_AeT_r(A)\cong A\oplus DA\). The standard algebra is self-injective. Hence the corner theorem applies for every \(r\ge2\), not only \(r=2\). The canonical Nakayama automorphism cyclically permutes the \(r\) diagonal blocks and has exact order \(r\); this yields the fixed-order equivalence. The dimension identity \(\dim_kT_r(A)=2r\dim_kA\) follows directly from the \(r\) copies each of \(A\) and \(DA\).

The converse implication in the fixed-order theorem is also sound: if ARC holds universally, it holds for every Frobenius algebra, where self-injectivity makes \(\operatorname{Ext}^{>0}(M,\Gamma)=0\) automatic, so ARC specializes to TC2. No step uses classification of self-injective algebras.

The boundary \(r=1\) was checked separately. The one-fold trivial extension is symmetric, but the corner used in the proof is no longer available in the required form; the record therefore makes no order-one claim.

## Originality

**PASS, to the best of our knowledge.** Enomoto's 2026 preprint proves the implication \(\operatorname{TC2}(T_2(A))\Rightarrow\operatorname{ARC}(A)\) and supplies the idempotent-induction/Ext-comparison mechanism. That result is treated as prior work. Chan–Darpö–Iyama–Marczinzik treat \(r\)-fold trivial extensions, their self-injectivity and cyclic Nakayama automorphisms; these structural facts are also treated as prior work.

Targeted searches for combinations and synonymous formulations of “r-fold trivial extension”, “Tachikawa conjecture”, “Auslander–Reiten conjecture”, “Nakayama automorphism/order”, “idempotent corner”, and orbit-algebra terminology did not locate a statement that for every fixed \(r\ge2\), TC2 on \(T_r(A)\) alone is equivalent to universal ARC, nor the broader corner criterion or the resulting all-orders counterexample proliferation.

Broader work of Chen–Hu–Qin–Wang transfers ARC under certain singular equivalences, recollements and change-of-rings settings. It establishes important neighboring reduction principles, but the located statements do not supply the present self-injective-corner criterion or fixed-Nakayama-order reduction.

Residual risk remains because the all-\(r\) corollary is an elementary synthesis of Enomoto's very recent argument with standard orbit-algebra facts; an equivalent observation may have appeared under different terminology. Accordingly, no claim of exhaustive literature coverage or first discovery is made.

## Value

**PASS.** The result sharpens a new universal implication into a family of much smaller test classes. For any single prescribed \(r\ge2\), one may restrict TC2 to Frobenius algebras carrying a Nakayama automorphism of exactly that order and still recover universal ARC. Dually, a hypothetical ARC counterexample would not merely imply one TC2 counterexample: it would generate explicit TC2 counterexamples in every standard finite Nakayama order \(r\ge2\), with dimensions growing linearly as \(2r\dim A\). The corner criterion is also reusable beyond trivial extensions whenever \({}_Ae\Gamma\) is built from \(A\) and \(DA\).

## Scope of the claim

No novelty is claimed for ARC, TC2, Enomoto's two-fold theorem, induction along an idempotent, standard tensor–Hom duality, the definition of \(r\)-fold trivial extensions, their self-injectivity, or their cyclic Nakayama automorphisms. The claimed contribution is the corner transfer criterion in the stated form, its uniform application to every \(r\ge2\), the fixed-order equivalence, and the quantitative counterexample-proliferation consequence.
