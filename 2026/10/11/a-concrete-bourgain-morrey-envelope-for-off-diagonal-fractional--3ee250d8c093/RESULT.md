# A concrete Bourgain–Morrey envelope for off-diagonal fractional Gagliardo–Nirenberg targets

## Finding
Let \(0<s<1\), and for \(i\in\{1,2\}\) let
\[
1<p_i<u_i<r_i<\infty.
\]
For the Bourgain–Morrey spaces \(\mathcal M^{u_i}_{p_i,r_i}(\mathbb R^n)\), define the harmonic parameters
\[
\frac1{p_s}=\frac{1-s}{p_1}+\frac{s}{p_2},\qquad
\frac1{u_s}=\frac{1-s}{u_1}+\frac{s}{u_2},\qquad
\frac1{r_s}=\frac{1-s}{r_1}+\frac{s}{r_2}.
\]
Then
\[
(\mathcal M^{u_1}_{p_1,r_1})^{1-s}(\mathcal M^{u_2}_{p_2,r_2})^s
\hookrightarrow
\mathcal M^{u_s}_{p_s,r_s}
\]
contractively for the norms used in the cited source.

Combining this inclusion with Theorem 1.9(i) of Hu–Li–Yang–Yuan gives a concrete off-diagonal fractional Gagliardo–Nirenberg target. Namely, if \(k\in\mathbb N\), \(q\in[1,\infty)\), and
\[
n\left(\frac{1-s}{p_1}+\frac{s}{p_2}-\frac1q\right)<sk,
\]
then
\[
\|D_q^{s,k}(f)\|_{\mathcal M^{u_s}_{p_s,r_s}}
\lesssim
\|f\|_{\mathcal M^{u_1}_{p_1,r_1}}^{1-s}
\|\nabla^k f\|_{\mathcal M^{u_2}_{p_2,r_2}}^s
\]
for every \(f\in\mathcal M^{u_1}_{p_1,r_1}\cap\dot W^{k,\mathcal M^{u_2}_{p_2,r_2}}\). No compatibility relation among the three exponent ratios is required for this one-sided target inclusion.

## Assumptions and scope
For finite \(r\), the Bourgain–Morrey norm is
\[
\|f\|_{\mathcal M^u_{p,r}}
=
\left[
\sum_{Q\in\mathcal D}
\left(|Q|^{1/u-1/p}\|f\mathbf 1_Q\|_{L^p}\right)^r
\right]^{1/r},
\]
where \(\mathcal D\) is the dyadic cube family. The strict inequalities \(p_i<u_i<r_i<\infty\) place both factors in the nontrivial finite-\(r\) Banach regime recorded by Hu–Li–Yang–Yuan. They also imply \(p_s<u_s<r_s<\infty\).

The Calderón–Lozanovskiĭ product \(X^{1-s}Y^s\) is equipped with the norm obtained by infimizing \(\|g\|_X^{1-s}\|h\|_Y^s\) over factorizations \(|f|\le |g|^{1-s}|h|^s\).

The fractional difference quantity is
\[
D_q^{s,k}(f)(x)
=
\left[
\int_{\mathbb R^n}
\frac{|\Delta_h^k f(x)|^q}{|h|^{n+skq}}\,dh
\right]^{1/q},
\]
with
\[
\Delta_h^k f(x)=\sum_{j=0}^k(-1)^{k-j}\binom kj f(x+jh).
\]
The claim does not assert that the Calderón–Lozanovskiĭ product equals \(\mathcal M^{u_s}_{p_s,r_s}\). It supplies only the stated one-sided inclusion and its concrete Gagliardo–Nirenberg consequence.

## Proof
Take \(F\in(\mathcal M^{u_1}_{p_1,r_1})^{1-s}(\mathcal M^{u_2}_{p_2,r_2})^s\). By the definition of the Calderón–Lozanovskiĭ product, for every \(\varepsilon>0\) there are \(G\in\mathcal M^{u_1}_{p_1,r_1}\) and \(H\in\mathcal M^{u_2}_{p_2,r_2}\) such that
\[
|F|\le |G|^{1-s}|H|^s
\]
and
\[
\|G\|_{\mathcal M^{u_1}_{p_1,r_1}}^{1-s}
\|H\|_{\mathcal M^{u_2}_{p_2,r_2}}^s
\le
\|F\|_{(\mathcal M^{u_1}_{p_1,r_1})^{1-s}(\mathcal M^{u_2}_{p_2,r_2})^s}+\varepsilon.
\]

For each dyadic cube \(Q\), Hölder's inequality and the identity for \(p_s\) give
\[
\|F\mathbf1_Q\|_{L^{p_s}}
\le
\|G\mathbf1_Q\|_{L^{p_1}}^{1-s}
\|H\mathbf1_Q\|_{L^{p_2}}^s.
\]
The cube weight factors exactly because
\[
\frac1{u_s}-\frac1{p_s}
=(1-s)\left(\frac1{u_1}-\frac1{p_1}\right)
+s\left(\frac1{u_2}-\frac1{p_2}\right).
\]
Thus, if
\[
A_Q=|Q|^{1/u_1-1/p_1}\|G\mathbf1_Q\|_{L^{p_1}},\qquad
B_Q=|Q|^{1/u_2-1/p_2}\|H\mathbf1_Q\|_{L^{p_2}},
\]
then the \(Q\)-term for \(F\) is at most \(A_Q^{1-s}B_Q^s\). A second Hölder inequality, now over the dyadic cube index, uses
\[
\frac1{r_s}=\frac{1-s}{r_1}+\frac{s}{r_2}
\]
and yields
\[
\|F\|_{\mathcal M^{u_s}_{p_s,r_s}}
\le
\|G\|_{\mathcal M^{u_1}_{p_1,r_1}}^{1-s}
\|H\|_{\mathcal M^{u_2}_{p_2,r_2}}^s.
\]
Taking the infimum over admissible factorizations proves the contractive inclusion.

Hu–Li–Yang–Yuan record that the lower generalized Boyd index of \(\mathcal M^u_{p,r}\) is \(p\) in this regime. Applying their Theorem 1.9(i) with the two factor spaces gives the estimate in their Calderón–Lozanovskiĭ target under
\[
n\left(\frac{1-s}{p_1}+\frac{s}{p_2}-\frac1q\right)<sk.
\]
The contractive inclusion just proved then gives the displayed concrete Bourgain–Morrey estimate.

## Verification
The proof is symbolic and uses only two instances of Hölder's inequality plus the exact affine identities among reciprocal exponents. The local \(L^p\) exponents and the outer \(\ell^r\) exponents were checked independently. The cube power is exactly the convex combination required by \(u_s\) and \(p_s\); hence no residual power of \(|Q|\) remains.

The primary source was inspected at its definition of \(D_q^{s,k}\), Definition 2.9 of the Calderón–Lozanovskiĭ norm, Theorem 1.9, and the Bourgain–Morrey subsection. Its Section 6.1 records the nontrivial range, the lower generalized Boyd index, the abstract product target, and the statement that a general explicit product description remains unknown.

## Relationship to prior work
Hu–Li–Yang–Yuan prove the off-diagonal fractional Gagliardo–Nirenberg inequality with abstract target
\[
(\mathcal M^{u_1}_{p_1,r_1})^{1-s}(\mathcal M^{u_2}_{p_2,r_2})^s.
\]
Their Bourgain–Morrey application table keeps that target abstract. They cite Zhao–Sawano–Tao–Yang–Yuan for explicit Calderón-product identifications under suitable compatibility conditions, and state that a general explicit description is unknown.

The present result does not attempt that missing equality. Instead it gives a compatibility-free, one-sided concrete envelope sufficient to turn the new abstract off-diagonal inequality into a fully explicit Bourgain–Morrey estimate throughout the finite nontrivial regime. The proof is independent of any interpolation identity.

## Limitations
No reverse inclusion is proved. The target \(\mathcal M^{u_s}_{p_s,r_s}\) is not claimed to be optimal within the Bourgain–Morrey scale. The statement is restricted to finite \(r_1,r_2\) with \(1<p_i<u_i<r_i<\infty\); endpoint regimes with \(r_i=\infty\) are not included here. A full-text comparison with the 2023 Calderón-product paper was not available in the inspected material, so an equivalent unindexed one-sided lemma there remains a residual originality risk.

## References
1. P. Hu, Y. Li, D. Yang, W. Yuan, *Fractional Gagliardo–Nirenberg Inequalities: Pointwise Estimates, Sharp Asymptotics, and Optimal Target Spaces*, arXiv:2608.06813v1 (2026).
2. Y. Zhao, Y. Sawano, J. Tao, D. Yang, W. Yuan, *Bourgain–Morrey Spaces Mixed with Structure of Besov Spaces*, Proc. Steklov Inst. Math. 323 (2023), 244–295, DOI:10.1134/S0081543823050152.
3. N. Hatano, T. Nogayama, Y. Sawano, D. I. Hakim, *Bourgain–Morrey spaces and their applications to boundedness of operators*, J. Funct. Anal. 284 (2023), 109720, DOI:10.1016/j.jfa.2022.109720.
