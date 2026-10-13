# All-order tricritical threshold for the three-loop countable hard-core tree model

## Finding

Consider the countable-state hard-core model whose compatibility graph has loops at states \(0,1,2\). Fix an integer Cayley-tree order \(k\ge2\), positive summable activities \((\lambda_i)_{i\ne0}\), and impose equal loop activities
\[
\lambda_1=\lambda_2=\lambda.
\]
Write
\[
\Lambda=\sum_{i\ne0}\lambda_i.
\]
The source gives the translation-invariant equations
\[
z_1=\lambda\left(\frac{1+z_1}{S}\right)^k,
\qquad
z_2=\lambda\left(\frac{1+z_2}{S}\right)^k,
\qquad
z_i=\lambda_i S^{-k}\quad(i\ne1,2),
\]
where
\[
S=1+\sum_{i\ne0}z_i.
\]

Every nonsymmetric positive solution, up to swapping states \(1\) and \(2\), is uniquely parameterized by \(s>0\):
\[
z_1=e^{ks}\frac{\sinh s}{\sinh((k-1)s)},
\qquad
z_2=e^{-ks}\frac{\sinh s}{\sinh((k-1)s)}.
\]
Put
\[
c_k(s)=\frac{\sinh s\,\sinh^{k-1}((k-1)s)}{\sinh^k(ks)},
\qquad
S_{k,\lambda}(s)=\left(\frac{\lambda}{c_k(s)}\right)^{1/k},
\]
\[
m_k(s)=1+2\cosh(ks)\frac{\sinh s}{\sinh((k-1)s)}.
\]
The branch is admissible exactly when
\[
S_{k,\lambda}(s)>m_k(s),
\]
and on that domain its required total activity is
\[
\boxed{
\Lambda_{k,\lambda}(s)
=2\lambda+\frac{\lambda}{c_k(s)}
\bigl(S_{k,\lambda}(s)-m_k(s)\bigr).
}
\]

Define
\[
\lambda_0(k)=\frac{(k+1)^k}{k^k(k-1)},
\qquad
\boxed{
\lambda_*(k)=\frac{(3k+1)^k}{3^k(k-1)^{k+1}}.
}
\]
Then \(\lambda_*(k)>\lambda_0(k)\). For \(\lambda>\lambda_0(k)\), the branch meets the symmetric solution at
\[
\Lambda_c(k,\lambda)
=2\lambda+\frac{\lambda}{c_*}
\left(S_*-\frac{k+1}{k-1}\right),
\]
where
\[
c_* = \frac{(k-1)^{k-1}}{k^k},
\qquad
S_* = \left(\frac{\lambda}{c_*}\right)^{1/k}.
\]
Near the merger,
\[
\Lambda_{k,\lambda}(s)
=\Lambda_c(k,\lambda)+Q_{k,\lambda}s^2+O(s^4),
\]
with
\[
Q_{k,\lambda}
=\frac{\lambda}{c_*}(k+1)
\left(
\frac{k-1}{2}S_*
-\frac{k(3k+1)}{6(k-1)}
\right).
\]
Therefore the branch bends below, is tangent to, or bends above its merger level according as \(\lambda<\lambda_*(k)\), \(\lambda=\lambda_*(k)\), or \(\lambda>\lambda_*(k)\). At equality the next term is
\[
\boxed{
\Lambda_{k,\lambda_*}(s)-\Lambda_c(k,\lambda_*)
=-\frac{\lambda_*}{c_*}
\frac{k(k+1)(37k^2+110k+37)}{1080(k-1)}s^4
+O(s^6),
}
\]
so the degeneracy is resolved on the downward side. Thus \(\lambda_*(k)\) is the exact tricritical activity for the local orientation of this symmetry-broken branch. In particular,
\[
\lambda_*(2)=\frac{49}{9},
\]
which identifies the source's special binary-tree constant as the first member of the all-order formula.

For every \(\lambda>\lambda_*(k)\), the admissible branch starts above \(\Lambda_c\) and ends at total activity \(2\lambda<\Lambda_c\). Hence, if \(s_0\) is its first positive admissibility endpoint and
\[
\Lambda_{\max}(k,\lambda)=
\max_{0\le s\le s_0}\Lambda_{k,\lambda}(s),
\]
then \(\Lambda_{\max}(k,\lambda)>\Lambda_c(k,\lambda)\). Every
\[
\Lambda_c(k,\lambda)<\Lambda<\Lambda_{\max}(k,\lambda)
\]
is attained by at least two distinct positive parameters \(s\), producing two swapped pairs of nonsymmetric normalized boundary laws. A symmetric normalized boundary law also exists for every such \(\Lambda\). Therefore the model has at least five distinct translation-invariant Gibbs measures throughout this nonempty interval.

## Assumptions and scope

The tree order is an integer \(k\ge2\). The activity sequence is positive and summable, with \(\lambda_1=\lambda_2=\lambda\). The result concerns translation-invariant normalized boundary laws for the source's three-loop compatibility graph. The location of the two nonzero loops is immaterial up to relabeling, as in the source.

The result does not classify arbitrary non-translation-invariant boundary laws, periodic boundary laws, or all Gibbs measures. For \(k>2\), it gives an at-least-five coexistence interval rather than an exact global count.

## Proof

Let
\[
c=\frac{\lambda}{S^k}.
\]
The two loop equations are
\[
z_1=c(1+z_1)^k,
\qquad
z_2=c(1+z_2)^k.
\]
For a nonsymmetric solution orient the labels so that \(z_1>z_2\), and set
\[
r=\frac{1+z_1}{1+z_2}>1.
\]
Dividing the loop equations gives \(z_1/z_2=r^k\). Solving this relation together with the definition of \(r\) gives, reversibly,
\[
z_1=\frac{r^{k-1}(r-1)}{r^{k-1}-1},
\qquad
z_2=\frac{r-1}{r(r^{k-1}-1)}.
\]
Writing \(r=e^{2s}\) yields the displayed hyperbolic parameterization. Substitution into \(c=z_1/(1+z_1)^k\) gives exactly \(c=c_k(s)\), so
\[
S=S_{k,\lambda}(s).
\]

For every state other than \(1,2\), the source equation gives \(z_i=\lambda_i/S^k\). Hence their total boundary mass equals
\[
\frac{\Lambda-2\lambda}{S^k}.
\]
Self-consistency requires this to equal \(S-m_k(s)\). This proves both the admissibility criterion and the exact formula for \(\Lambda_{k,\lambda}(s)\), and also proves the converse: every admissible parameter reconstructs a full positive boundary law for any positive activity sequence with the required total.

As \(s\downarrow0\),
\[
c_k(s)=c_*\exp\left(
-\frac{k(k-1)}{2}s^2
+\frac{k(k-1)(k^2-k+1)}{36}s^4
+O(s^6)
\right),
\]
and
\[
m_k(s)=\frac{k+1}{k-1}
+\frac{2k(k+1)}{3(k-1)}s^2
-\frac{2k(k+1)(k^2-5k+1)}{45(k-1)}s^4
+O(s^6).
\]
These expansions give the stated merger value and the coefficient \(Q_{k,\lambda}\). Solving \(Q_{k,\lambda}=0\) gives \(\lambda=\lambda_*(k)\). At this value the exact fourth-order coefficient simplifies to the strictly negative expression displayed in the finding. Also,
\[
\frac{\lambda_*(k)}{\lambda_0(k)}
=\left(\frac{k(3k+1)}{3(k^2-1)}\right)^k>1,
\]
so the tricritical point lies inside the locally admissible regime.

For \(\lambda>\lambda_*(k)\), admissibility holds for all sufficiently small positive \(s\), and \(\Lambda_{k,\lambda}(s)>\Lambda_c(k,\lambda)\) there. On the other hand,
\[
c_k(s)\sim e^{-2(k-1)s},
\qquad
S_{k,\lambda}(s)\sim \lambda^{1/k}e^{2(k-1)s/k},
\qquad
m_k(s)\sim e^{2s},
\]
so \(S_{k,\lambda}(s)-m_k(s)\to-\infty\). Let \(s_0\) be the first positive zero of this continuous difference. Then the branch is admissible on \((0,s_0)\), while
\[
\Lambda_{k,\lambda}(s_0)=2\lambda<\Lambda_c(k,\lambda).
\]
Continuity therefore gives an interior maximum strictly above \(\Lambda_c\), and every intermediate level between \(\Lambda_c\) and that maximum is crossed at least twice. Each crossing yields a distinct nonsymmetric solution, and swapping \(z_1,z_2\) gives its partner.

It remains to supply a symmetric solution at the same total activity. Put \(z_1=z_2=z>0\). The loop equation determines
\[
S(z)=\lambda^{1/k}(1+z)z^{-1/k}.
\]
The full self-consistency equation is
\[
F(z)=S(z)-1-2z-\frac{\Lambda-2\lambda}{S(z)^k}=0.
\]
For \(k\ge2\), one has \(F(z)\to+\infty\) as \(z\downarrow0\) and \(F(z)\to-\infty\) as \(z\to\infty\). Thus a positive symmetric solution exists by continuity.

Every constructed boundary law is summable. A positive summable sequence belongs to \(\ell^p\) for every \(p>1\), in particular for \(p=(k+1)/k\). The source's normalisability criterion and normalized boundary-law correspondence therefore convert the five distinct normalized boundary laws into five distinct translation-invariant Gibbs measures.

## Verification

The standalone checker `verify_three_loop.py` verifies the reversible branch equations numerically for orders \(2\) through \(14\), verifies the threshold inequality and the exact vanishing quadratic coefficient at \(\lambda_*(k)\) for orders \(2\) through \(100\), and reconstructs the exact negative quartic coefficient with rational arithmetic. Its successful output is

`VERIFY_OK exact_orders=2..100 residual_cases=39 worst_residual=5.274e-16 k2_threshold=49/9`

The finite checks are corroborative only. The all-order statements are proved analytically above.

## Relationship to prior work

Khakimov and Makhammadaliev write the three-loop translation-invariant system for general \(k\), but explicitly state that the general case is difficult and then restrict the uniqueness/non-uniqueness theorem to \(k=2\). Their binary-tree theorem contains the threshold \(49/9\) and a five-measure interval. The result above identifies \(49/9\) as \(\lambda_*(2)\), gives the all-order tricritical formula, and proves an at-least-five coexistence interval for every \(k\ge2\) once \(\lambda>\lambda_*(k)\).

The related countable-state hard-core model of Rozikov and Haydarov uses a different compatibility graph \(G^*\): nonzero neighboring spins are forbidden and no nonzero loops occur. Its scalar recursion and periodic-measure theorem therefore do not imply the three-loop branch above.

A separate same-period result for a countable-state hard-core operator with a parity adjacency pattern has a superficially similar two-mass symmetry-breaking parameterization, but its compatibility graph and its activity self-consistency equation are different. In particular, its control parameter is a parity activity total, not the total countable activity \(\Lambda\) of the present three-loop model, so its theorem does not imply the displayed \(\lambda_*(k)\), \(\Lambda_c\), or the three-loop coexistence interval.

## Limitations

The result proves the exact local tricritical threshold and existence of a nonempty five-measure interval above it. It does not prove that the branch has a unique global maximum, that five is the exact number of translation-invariant Gibbs measures for \(k>2\), or that the measures are extreme, stable, or thermodynamically dominant. A weakly indexed equivalent derivation under different variables remains a residual literature risk.

## References

1. R. M. Khakimov and M. T. Makhammadaliev, *Translation-Invariant Gibbs Measures for the Hard Core Model with a Countable Set of Spin Values*, arXiv:2310.12602v1; Lobachevskii Journal of Mathematics 45 (2024), DOI:10.1134/S1995080224604508.
2. U. A. Rozikov and F. H. Haydarov, *A HC model with countable set of spin values: uncountable set of Gibbs measures*, arXiv:2206.06333v1; International Journal of Geometric Methods in Modern Physics 19 (2022), DOI:10.1142/S0129055X22500398.
