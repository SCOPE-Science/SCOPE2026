# Equality in the Kodaira-dimension-one Noether bound forces a rational-normal canonical base
## Finding
Let \(V\) be a smooth projective complex threefold with \(\kappa(V)=1\), \(p_g(V)\ge2\), and
\[
\operatorname{Ivol}(V)=p_g(V)-1.
\]
Resolve the canonical map and write its Stein factorization as
\[
V'\longrightarrow \Gamma\longrightarrow T\subset \mathbf P^{p_g(V)-1}.
\]
Then \(\Gamma\cong\mathbf P^1\), the finite map \(\Gamma\to T\) has degree one, and \(T\) is the rational normal curve of degree \(p_g(V)-1\). Consequently the resolved canonical map is the Iitaka fibration followed by the rational-normal embedding
\[
\mathbf P^1\hookrightarrow\mathbf P^{p_g(V)-1}.
\]
If \(X\) is a minimal model and \(f:X\to\mathbf P^1\) is its Iitaka fibration with
\[
K_X\sim_{\mathbf Q}f^*L,
\]
then
\[
L\sim_{\mathbf Q}\mathcal O_{\mathbf P^1}(p_g(V)-1).
\]

## Assumptions and scope
The ground field is \(\mathbf C\). The threefold \(V\) is smooth and projective, has Kodaira dimension one, and has \(p_g(V)\ge2\), so its canonical system has positive projective dimension. The Iitaka volume is normalized as in Chen--Hu--Jiang--Liu: on a minimal model \(X\), the semiample canonical divisor defines an Iitaka fibration \(f:X\to Z\) and satisfies \(K_X\sim_{\mathbf Q}f^*L\), with \(\operatorname{Ivol}(V)=\deg L\) because \(Z\) is a curve.

The conclusion concerns the equality case of the sharp inequality \(\operatorname{Ivol}(V)\ge p_g(V)-1\). It does not claim that all Kodaira-dimension-one threefolds have rational Iitaka base, nor does it classify the general fibers of the equality examples.

## Proof
Put \(r=p_g(V)-1>0\). In the notation used for the canonical linear system in the source, after resolving indeterminacy the canonical map has Stein factorization
\[
V'\xrightarrow{g}\Gamma\xrightarrow{\tau}T\subset\mathbf P^r,
\]
where \(\Gamma\) is a smooth projective curve and \(\tau\) is finite. Let \(A\) be the line bundle on \(\Gamma\) obtained by pulling back \(\mathcal O_T(1)\), and write \(a=\deg A\). The canonical sections give \(h^0(\Gamma,A)\ge r+1\). The curve estimate used in Remark 2.6 of Chen--Hu--Jiang--Liu gives
\[
a\ge h^0(\Gamma,A)-1\ge r,
\]
with equality in the first inequality only when \(\Gamma\) has genus zero.

Lemma 2.8 of the same source compares the canonical movable divisor with the divisor defining the Iitaka fibration. For \(m=1\), it yields on the one-dimensional base
\[
\deg L\ge a.
\]
Under the assumed equality,
\[
r=\operatorname{Ivol}(V)=\deg L\ge a\ge r,
\]
so every inequality is an equality. Hence \(a=r\), \(\Gamma\) has genus zero, and therefore \(\Gamma\cong\mathbf P^1\).

Let \(e=\deg(\tau)\). Since \(A=\tau^*\mathcal O_T(1)\),
\[
a=e\,\deg T.
\]
The canonical image \(T\subset\mathbf P^r\) is a nondegenerate integral curve, so \(\deg T\ge r\). Combining this with \(a=r\) gives
\[
r=e\,\deg T\ge e r.
\]
Because \(r>0\), one gets \(e=1\) and \(\deg T=r\). A nondegenerate integral curve of degree \(r\) in \(\mathbf P^r\) is a rational normal curve. Thus \(T\cong\mathbf P^1\), and the finite degree-one map \(\Gamma\to T\) is an isomorphism.

Finally, equality \(\deg L=a\) in the effective comparison of Lemma 2.8 means that the effective \(\mathbf Q\)-divisor measuring the difference has degree zero, hence vanishes. After identifying the Iitaka base with \(\Gamma\cong\mathbf P^1\), the canonical movable line bundle has degree \(r\). Since line bundles on \(\mathbf P^1\) are determined by degree,
\[
L\sim_{\mathbf Q}\mathcal O_{\mathbf P^1}(r)
=\mathcal O_{\mathbf P^1}(p_g(V)-1).
\]
This also shows that the resolved canonical map is the Iitaka fibration followed by the complete degree-\(r\) Veronese embedding of \(\mathbf P^1\).

## Verification
The proof was reconstructed from the full accessible text of arXiv:2610.02689v1, specifically the definition of Iitaka volume and Iitaka fibration, Setting 2.4, Remark 2.6, Lemmas 2.7 and 2.8, and the proof of Theorem 1.2. The source proves
\[
\operatorname{Ivol}(V)\ge p_g(V)-1
\]
for \(\kappa(V)=1\), and its curve-side construction supplies the stronger intermediate quantity \(a=\deg A\). The equality argument above checks both possible losses: the finite degree from the Stein base to the canonical image and the degree excess of a nondegenerate projective curve.

The source's Example 4.5 gives equality families for every indicated parameter in that construction, so the equality regime is nonempty. No finite experiment is used as a proof. The only external geometric input beyond the source lemmas is the classical classification of nondegenerate curves of minimal degree.

## Relationship to prior work
Chen--Hu--Jiang--Liu prove the sharp Kodaira-dimension-one inequality and give equality examples, while their explicit equality-classification theorem is devoted to the Kodaira-dimension-two case. A full-text search of arXiv:2610.02689v1 for the phrase “rational normal” returns no occurrence, and the inspected statement/proof of Theorem 1.2 does not identify the canonical image or the degree of its Stein factor in the equality case.

Targeted published-finding searches were run for the equality formula, rational-normal canonical images, minimal-degree canonical curves, and the exact arXiv identifier. No located statement implied the conclusion above. The closest returned results concerned unrelated anticanonical-volume extrema, stable-surface pluricanonical thresholds, and normalization questions.

## Limitations
The claim requires \(p_g(V)\ge2\); when \(p_g(V)=1\), the canonical map has zero-dimensional image and the argument through a nondegenerate projective curve does not apply. The result is birational in the same sense as the source: it identifies the resolved canonical map and the Iitaka base, not a preferred morphism on every smooth birational model. It does not classify the fibers of the resulting fibration or the moduli of equality examples.

Originality was checked against the initiating full text, the current and prior ledgers, and several statement-level published searches. An equivalent observation under different notation could still exist outside the inspected literature; no database search is a proof of global novelty.

## References
1. Meng Chen, Yong Hu, Chen Jiang, Yang Liu, *Sharp Noether-type inequalities for 3-folds of intermediate Kodaira dimensions*, arXiv:2610.02689v1, first public 2 October 2026. See Theorem 1.2, Setting 2.4, Remark 2.6, Lemmas 2.7--2.8, and Example 4.5.
