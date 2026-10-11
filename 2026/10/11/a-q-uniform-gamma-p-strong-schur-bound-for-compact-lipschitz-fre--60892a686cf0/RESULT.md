# A \(q\)-uniform \(\Gamma_p\) strong Schur bound for compact Lipschitz-free \(p\)-spaces
## Finding
Let \(0<p<q\le 1\), let \(M\) be a pointed \(q\)-metric space, and let \(W\subset \mathcal F_p(M)\) be bounded, infinite, \(\delta\)-separated, and have Kalton's property. Then for every \(0<c<\delta/(2^{1/p}\Gamma_p)\) there is a sequence in \(W\) with lower \(\ell_p\)-estimate \(c\). Consequently, for every compact pointed \(q\)-metric space \(K\), the free \(p\)-space \(\mathcal F_p(K)\) has the \(\Gamma_p\)-strong Schur \(p\)-property, where \(\Gamma_p\) is the uniform canonical-embedding constant from Theorem 2.1 of arXiv:2609.10747v1. This removes the source theorem's extra factor depending on \(q\); no assertion is made that \(\Gamma_p\) itself is the optimal universal constant.

Equivalently, if \((w_j)\) is the selected sequence, then every finitely supported scalar family \((\lambda_j)\) satisfies
\[
\left\|\sum_j \lambda_j w_j\right\|\ge c\left(\sum_j|\lambda_j|^p\right)^{1/p}.
\]
The new point is that the quantitative constant can be made independent of the gap \(q-p\). The published compact-base theorem gives instead \(\Gamma_p H_{p,q}^{1/p}\), where
\[
H_{p,q}=\frac1{1-16^{p-q}}+1+\frac1{1-16^{-p}},
\]
which diverges as \(q\downarrow p\).

## Assumptions and scope
All vector spaces are real. Fix \(0<p<q\le1\). A \(q\)-metric means that the \(q\)-th power of the distance is a metric. The symbol \(\Gamma_p\ge1\) denotes the uniform constant for the inverse of canonical inclusions \(\mathcal F_p(A)\to\mathcal F_p(A;M)\) over pointed \(p\)-metric inclusions. Kalton's property is used exactly in the form of Definition 4.5 of the focal source.

The statement concerns lower \(\ell_p\)-estimates. For the compact-base conclusion, the upper \(\ell_p\)-estimate required in the definition of the strong Schur property is automatic on the unit sphere by the \(p\)-triangle inequality. The endpoint \(q=p\) is not included, and no optimality claim for \(\Gamma_p\) is made.

## Proof
The proof replaces the fixed scale ratio \(4\) in the focal lacunary assembly by an arbitrarily large ratio and keeps track of the two geometric tails jointly.

Fix \(s>1\). Suppose positive scales satisfy
\[
b_j\le \frac{a_j}s,
\qquad
a_{j+1}\le \frac{b_j}s.
\]
Then \(a_{j+1}\le a_j/s^2\) and \(b_{j+1}\le b_j/s^2\). Let pointed maps \(\Phi_j:M\to E_j\) satisfy the detector estimate
\[
\|\Phi_j(x)-\Phi_j(y)\|^p
\le C\min\{h^p,h^q b_j^{p-q},a_j^p\},
\qquad h=d(x,y).
\]
Put \(\alpha=q-p>0\),
\[
A_s=\frac1{1-s^{-2\alpha}},
\qquad
B_s=\frac1{1-s^{-2p}}.
\]
For fixed \(h>0\), split the indices as in the focal proof:
\[
I_1=\{j:h\le b_j\},\qquad
I_2=\{j:b_j<h<a_j\},\qquad
I_3=\{j:a_j\le h\}.
\]
If \(r=\max I_1\), geometric summation gives
\[
\sum_{j\in I_1}h^q b_j^{p-q}
\le A_s h^p\left(\frac h{b_r}\right)^\alpha.
\]
If \(t=\min I_3\), similarly
\[
\sum_{j\in I_3}a_j^p
\le B_s h^p\left(\frac{a_t}h\right)^p.
\]
The middle set \(I_2\) contains at most one index.

If \(I_2=\{k\}\), then the nearest earlier and later scales satisfy \(b_{k-1}>s h\) and \(a_{k+1}<h/s\) whenever those indices exist. Hence
\[
\frac1{h^p}\sum_j\|\Phi_j(x)-\Phi_j(y)\|^p
\le C\left(1+A_s s^{-\alpha}+B_s s^{-p}\right).
\]
If \(I_2\) is empty and both tails are nonempty, then the adjacent boundary indices satisfy \(t=r+1\) and \(a_t\le b_r/s\). Writing \(x=h/b_r\) and \(y=a_t/h\), one has \(xy\le1/s\), so either \(x\le s^{-1/2}\) or \(y\le s^{-1/2}\). Therefore
\[
\frac1{h^p}\sum_j\|\Phi_j(x)-\Phi_j(y)\|^p
\le C\max\left\{B_s+A_s s^{-\alpha/2},
A_s+B_s s^{-p/2}\right\}.
\]
If one tail is empty, the corresponding bound only improves. Thus the assembled map has
\[
\operatorname{Lip}(\Phi)^p\le C G_s,
\]
where
\[
G_s=\max\left\{
1+A_s s^{-\alpha}+B_s s^{-p},
B_s+A_s s^{-\alpha/2},
A_s+B_s s^{-p/2}
\right\}.
\]
For fixed \(p<q\), one has \(G_s\to1\) as \(s\to\infty\).

Now rerun the quantitative selection proof from the focal source. The recursion permits the stronger scale requirements: after \(b_{j-1}\) is chosen, choose any sufficiently small \(a_j\le b_{j-1}/s\); and the finite-support recovery lemma supplies a threshold \(b_0>0\) for which every \(0<b\le b_0\) works, so choose \(b_j\le\min\{b_0,a_j/s\}\). The detector recovery estimate remains
\[
\|T_j\gamma_j\|\ge \Gamma_p^{-1}\operatorname{dist}\!\left(\gamma_j,\mathcal F_p(F_j;M)\right).
\]
Accordingly, the assembled operator has norm at most \(G_s^{1/p}\).

Given
\[
0<c<\frac{\delta}{2^{1/p}\Gamma_p},
\]
choose \(s\) so large that
\[
c\Gamma_p G_s^{1/p}<\frac{\delta}{2^{1/p}}.
\]
The remaining choices of \(\rho\) and the approximation error can then be made exactly as in the source proof, with \(G_s^{1/p}\) in place of \(H_{p,q}^{1/p}\). The diagonal detector lemma yields a subsequence with lower \(\ell_p\)-estimate \(c\). This proves the first assertion.

For compact \(K\), every bounded subset of \(\mathcal F_p(K)\) has Kalton's property by a finite-net argument. Given any \(K_0>\Gamma_p\) and an infinite \(\delta\)-separated subset of the unit sphere, apply the first assertion with
\[
c=\frac{\delta}{K_0 2^{1/p}}<\frac{\delta}{\Gamma_p2^{1/p}}.
\]
The selected sequence has the required lower estimate, while its upper \(\ell_p\)-estimate is \(1\). Since \(K_0>\Gamma_p\ge1\), this is precisely the \(\Gamma_p\)-strong Schur \(p\)-property.

## Verification
The argument is infinite and symbolic; no finite experiment is used as proof. The critical points checked directly are: the generalized scales still force pairwise-disjoint middle intervals; the two tail series have ratios \(s^{-2(q-p)}\) and \(s^{-2p}\); when there is no middle index, the product of the two boundary ratios is at most \(1/s\); and the focal finite-support recovery lemma remains valid after making \(b_j\) arbitrarily smaller.

The source proof explicitly allows \(a_j\) to be chosen below a prescribed previous scale, and its recovery lemma states that every sufficiently small \(b\) works. These are the only places where the stronger superlacunary recursion must be checked. The endpoint \(q=p\) is excluded because the first geometric tail then loses decay.

## Relationship to prior work
Albiac, Ansorena and Cúth prove that compact pointed \(q\)-metric bases have the strong Schur \(p\)-property and give the explicit constant \(\Gamma_p H_{p,q}^{1/p}\). Their lacunary assembly fixes the ratio \(4\), estimates the three index regions independently, and therefore retains the factor \(H_{p,q}^{1/p}\). The present argument uses the freedom already present in their recursion to make the scales arbitrarily superlacunary and couples the two tails when the middle region is empty. The resulting assembly loss tends to \(1\), which removes the entire \(q\)-dependent factor.

The earlier paper introducing the strong Schur \(p\)-property proves, among other things, a constant-preserving theorem for \(\ell_p\)-sums of spaces. It does not state a compact-base theorem for arbitrary Lipschitz-free \(p\)-spaces with the \(\Gamma_p\) constant. Targeted searches using the source identifier, the exact strong-Schur terminology, the constant \(\Gamma_p\), superlacunary assembly, and the published \(K_{p,q}\) notation found no implication-equivalent statement.

## Limitations
The result requires \(0<p<q\le1\). It does not treat the boundary \(q=p\), where the tail exponent used in the assembly vanishes. It does not claim that \(\Gamma_p\) is the smallest possible strong-Schur constant, nor does it compute \(\Gamma_p\). For noncompact bases, the quantitative selection statement is asserted only for bounded separated sets having Kalton's property.

Because the focal preprint is very recent, indexing lag or a later revision could contain an equivalent optimization. The literature search also cannot exclude an older equivalent observation phrased entirely in terms of lacunary detector sums rather than strong Schur \(p\)-properties.

## References
1. F. Albiac, J. L. Ansorena, M. Cúth, *Structural consequences of the Schur \(p\)-property for Lipschitz-free \(p\)-spaces*, arXiv:2609.10747v1, first submitted 2026-09-09. See Theorem 2.1, Lemma 3.2, Lemma 4.4, Theorems 4.6 and 4.7.
2. F. Albiac, J. L. Ansorena, J. Bíma, M. Cúth, *Lipschitz free \(p\)-spaces for \(0<p<1\) in the light of the Schur \(p\)-property and the compact reduction*, Journal of Geometric Analysis 36 (2026), Paper 54, DOI:10.1007/s12220-025-02260-5. See Definition 2.5 and Theorem 3.6.
