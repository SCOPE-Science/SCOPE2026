# Equational-probability spectra classify finite abelian groups

## Finding
For every finite abelian group \(G\), its set of probabilities of all single equations in its group signature is the finite set
\[
\operatorname{PSpec}(G)=\left\{\frac{|G[d]|}{|G|}:d\mid\exp(G)\right\},\qquad G[d]=\{g\in G:dg=0\}.
\]
This is also the spectrum of its multiplication-semigroup reduct. **The unlabelled set of rational probabilities determines \(G\) up to isomorphism**, and the following conditions characterize precisely which finite rational sets occur.

Let \(S\) be a finite nonempty subset of \(\mathbb Q\cap(0,1]\). Put \(N=1/\min(S)\) and \(T=\{Ns:s\in S\}\). There exists a finite abelian \(G\) with \(S=\operatorname{PSpec}(G)\) if and only if all of the following hold:

1. \(1\in S\); \(N\) is a positive integer; every member of \(T\) is a positive integer dividing \(N\).
2. For each prime \(p\mid N\), the ordered distinct valuations \(E_p=\{v_p(t):t\in T\}=\{e_{p,0}<\cdots<e_{p,L_p}\}\) start at \(e_{p,0}=0\) and end at \(e_{p,L_p}=v_p(N)\). The positive successive differences \(\delta_{p,j}=e_{p,j}-e_{p,j-1}\), for \(1\le j\le L_p\), are weakly decreasing.
3. The set \(T\) contains **all and only** the independent primary combinations
\[
T=\left\{\prod_{p\mid N}p^{e_p}:e_p\in E_p\text{ independently for every }p\mid N\right\}.
\]
For \(N=1\), these conditions mean precisely \(S=\{1\}\), corresponding to the trivial group. Otherwise, the unique group is reconstructed as
\[
G\cong\bigoplus_{p\mid N}\ \bigoplus_{i=1}^{\delta_{p,1}}\mathbb Z/p^{\lambda_{p,i}}\mathbb Z,
\qquad\lambda_{p,i}=\#\{j:1\le j\le L_p,\ \delta_{p,j}\ge i\}.
\]
In particular, \(|\operatorname{PSpec}(G)|=\tau(\exp(G))\), where \(\tau\) counts positive divisors. This cardinality alone is generally **not** a complete invariant.

## Assumptions and scope
A *single equation* is any equality of two terms in finitely many uniformly and independently sampled variables, with a finite nonzero number of variables. Use the ordinary group signature (multiplication, inverse and identity) or the multiplication-only semigroup signature. No arbitrary constants, relations, conjunctions, disjunctions, or conditionally specified equations are allowed. The finite abelian group may be trivial. Valuations \(v_p\) are applied only to positive integers.

For an elementary-divisor presentation \(G\cong\bigoplus_p\bigoplus_{i=1}^{r_p}\mathbb Z/p^{\lambda_{p,i}}\mathbb Z\), with positive exponents \(\lambda_{p,i}\), the explicit spectrum is
\[
\operatorname{PSpec}(G)=\left\{\frac{1}{|G|}\prod_p p^{\sum_{i=1}^{r_p}\min(v_p(d),\lambda_{p,i})}:d\mid\exp(G)\right\}.
\]

## Proof
**1. Reducing all equations to torsion kernels.** In an abelian group, the difference of any two terms is a word \(\sum_{j=1}^k c_jx_j\) with integer coefficients. Write \(m=\exp(G)\) and \(d=\gcd(m,c_1,\ldots,c_k)\). The homomorphism \(\Phi:G^k\to G\), \(\Phi((x_j))=\sum_jc_jx_j\), has image exactly \(dG\). The containment \(\operatorname{im}\Phi\subseteq dG\) holds because each coefficient is divisible by \(d\). For the reverse containment, Bézout's identity expresses \(d=am+\sum_jb_jc_j\), so \(dg=\Phi((b_jg)_j)\) for each \(g\in G\). All fibers of \(\Phi\) have the same size; consequently
\[
\Pr(\Phi=0)=\frac{1}{|dG|}=\frac{|G[d]|}{|G|}.
\]
Every positive divisor \(d\mid m\) occurs using the one-variable equation \(dx=0\). Thus the displayed spectrum formula is an equality, not merely a containment. Conversely, the multiplication-only equation \(x^{m+d}=x^m\) realizes \(dx=0\); every multiplication-only equation is also a group equation. Therefore both signatures have the same probability set.

**2. Primary exponent profiles.** Decompose \(G=\bigoplus_pG_p\) and write \(G_p=\bigoplus_i\mathbb Z/p^{\lambda_{p,i}}\mathbb Z\). Then
\[
|G[d]|=\prod_p p^{f_p(v_p(d))},\qquad f_p(j)=\sum_i\min(j,\lambda_{p,i}).
\]
For integers \(0\le j\le L_p=\max_i\lambda_{p,i}\), the differences satisfy
\[
f_p(j)-f_p(j-1)=\#\{i:\lambda_{p,i}\ge j\}=\delta_{p,j}>0,
\]
and \(\delta_{p,j}\) are weakly decreasing. In particular \(f_p(0)=0\), \(f_p(L_p)=v_p(|G|)\), and all the values \(f_p(j)\) are distinct. Varying \(d\) among divisors of \(m\) permits the exponent \(v_p(d)\) to vary independently for each prime. Thus \(T=\{|G[d]|:d\mid m\}\) has exactly the stated primary product shape and the stated endpoint and concavity conditions; \(|S|=\prod_p(L_p+1)=\tau(m)\).

**3. Reconstruction and realizability.** For a proposed finite set \(S\), the least possible probability is \(1/N\), because the equation \(x=y\) has probability \(1/|G|\) and every equation has probability at least this large by part 1. Hence the group order is forced to be \(N\). The distinct valuations in the normalized numerators \(T\) determine \(f_p(0),\ldots,f_p(L_p)\) without knowing which equation yielded which probability; uniqueness of prime factorization separates them. The successive increments \(\delta_{p,j}\) determine all \(\lambda_{p,i}\), since the number of cyclic \(p\)-power summands of length at least \(j\) is \(\delta_{p,j}\). This proves isomorphism rigidity.

Conversely, when conditions 1–3 hold, construct \(G\) using those \(\lambda_{p,i}\). The weakly decreasing increments ensure that the reconstructed length multiset is a partition and its conjugate has the prescribed increments. Telescoping gives \(f_p(j)=e_{p,j}\) and \(\sum_i\lambda_{p,i}=e_{p,L_p}=v_p(N)\), so \(|G|=N\). Independence condition 3 now forces \(\{|G[d]|:d\mid\exp(G)\}=T\), proving \(\operatorname{PSpec}(G)=S\). For \(N=1\), the trivial group gives \(S=\{1\}\). This establishes necessity, sufficiency, and uniqueness.

## Verification
Run `python3 verify.py` using only the Python standard library. The verifier enumerates all \(516\) isomorphism types of finite abelian groups with order at most \(256\), recovers each type from its spectrum, confirms the divisor-count cardinality, and detects no collisions. It separately checks \(604\) two-variable equations by direct tuple enumeration in small groups, comparing exact rational probabilities to the formula; it tests two unrealizable spectra that violate distinct inverse conditions. Its expected final line is `EXACT_GROUP_TYPES=516 EQUATION_CHECKS=604 VERIFY_OK`.

For illustration, the three order-eight groups have respectively
\[
\begin{aligned}
\operatorname{PSpec}(\mathbb Z/8\mathbb Z)&=\{1/8,1/4,1/2,1\},\\
\operatorname{PSpec}(\mathbb Z/4\mathbb Z\oplus\mathbb Z/2\mathbb Z)&=\{1/8,1/2,1\},\\
\operatorname{PSpec}((\mathbb Z/2\mathbb Z)^3)&=\{1/8,1\}.
\end{aligned}
\]
The non-realizable set \(\{1/8,1/4,1\}\) has increasing primary differences; \(\{1/6,1/3,1\}\) omits an independent prime-primary combination.

## Relationship to prior work
Cardó (2026, arXiv:2603.19487v1) introduced and studied this spectrum in the finite-algebra setting. Its Proposition 2.4 supplies a product-spectrum **inclusion**, Remark 2.5 explains agreement between group and semigroup signatures, Lemma 4.12 obtains the spectrum for cyclic prime-power groups, and Theorem 4.13 characterizes the **minimal** spectra. The separate preprint arXiv:2604.08446v1 studies general product inclusions, primality, and approximation, but not an inverse classification of arbitrary finite abelian spectra. The new content here is the exact coupled primary-factor description, characterization of all realizable finite-abelian spectra, and the reconstruction of the isomorphism type from an unlabelled probability set. A product inclusion alone does not establish equality: the two factors \(\mathbb Z/4\mathbb Z\) and \(\mathbb Z/2\mathbb Z\) yield four products of individual spectral values but only three values for their direct product.

## Limitations
This result applies to finite abelian groups and equations built from their basic group or semigroup operations, not general nonabelian groups, expanded signatures with arbitrary constants, or Boolean combinations of equations. Exact finite computations complement but do not replace the general proof. The uniqueness assertion concerns **these spectra as rational-value sets**, not their cardinalities; for instance, \(\mathbb Z/4\mathbb Z\) and \((\mathbb Z/4\mathbb Z)^2\) each have spectra of size three but different spectral values. An unrecognized equivalent result in older literature on torsion-profile or word-equation probabilities remains possible.

## References
1. Carles Cardó, *Minimal probabilistic spectrum grupoids*, arXiv:2603.19487v1 (first public 2026-03-19), especially Proposition 2.4, Remark 2.5, Lemma 4.12 and Theorem 4.13. https://arxiv.org/html/2603.19487v1
2. Carles Cardó, *Probabilistic equational spectrum, primality and approximation in finite algebras*, arXiv:2604.08446v1 (first public 2026-04-09), especially Definition 3.1 and the direct-product inclusion. https://arxiv.org/html/2604.08446v1
3. Fundamental theorem of finite abelian groups, standard elementary-divisor classification.
