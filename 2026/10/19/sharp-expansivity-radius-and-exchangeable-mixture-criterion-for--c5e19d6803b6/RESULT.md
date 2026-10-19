# Sharp expansivity radius and exchangeable-mixture criterion for the Hilbert-cube shift

## Finding
Let \(Q=[0,1]^{\mathbb Z}\), let \(\sigma\) be the bilateral shift, and use the specific compatible metric
\[
\rho(x,y)=\sum_{j\in\mathbb Z}2^{-|j|}|x_j-y_j|.
\]
A probability measure \(\mu\) is \(r\)-expansive if \(\mu(\Gamma_r(x))=0\) for **every** \(x\in Q\), where
\[
\Gamma_r(x)=\{y\in Q:\rho(\sigma^n x,\sigma^n y)\le r\text{ for all }n\in\mathbb Z\}.
\]
Define its *sharp measure-expansivity radius* by
\[
\mathcal E(\mu)=\sup\bigl(\{r>0:\mu\text{ is }r\text{-expansive}\}\cup\{0\}\bigr).
\]
If \(\mu\) is **exchangeable** (invariant under every permutation of finitely many coordinates), its de Finetti representation is
\[
\mu=\int_{\mathcal P([0,1])}\nu^{\mathbb Z}\,\Pi(d\nu).
\]
For \(\nu\in\mathcal P([0,1])\), let \(D(\nu)=\max\operatorname{supp}\nu-\min\operatorname{supp}\nu\), and put \(d_* =\operatorname{ess\,inf}_{\nu\sim\Pi} D(\nu)\). Then
\[
\boxed{\mathcal E(\mu)=\frac32d_*},\qquad
\boxed{\mu\text{ is measure-expansive}\iff d_*>0}.
\]
More precisely, every \(0<r<3d_*/2\) is an expansivity radius, and no \(r>3d_*/2\) is. The theorem does not generally decide the behavior at \(r=3d_*/2\). In the Bernoulli case \(\mu=\nu^{\mathbb Z}\), the result is sharp **including** the boundary: all \(0<r<3D(\nu)/2\) work and all \(r\ge3D(\nu)/2\) fail.

There is, in particular, a **full-support, nonatomic, shift-invariant, exchangeable measure** that is not expansive even though every measure in its explicitly given ergodic decomposition is a mixing, expansive Bernoulli measure. Let \(\lambda\) denote Lebesgue measure on \([0,1]\), let \(u_m\) denote uniform measure on \([\tfrac12-\tfrac1{4m},\tfrac12+\tfrac1{4m}]\), and set
\[
\boxed{\mu=\frac12\lambda^{\mathbb Z}+\sum_{m=1}^{\infty}2^{-(m+1)}u_m^{\mathbb Z}}.
\]
Its sharp radius is zero, while \(\mathcal E(\lambda^{\mathbb Z})=3/2\) and \(\mathcal E(u_m^{\mathbb Z})=3/(4m)\).

## Assumptions and scope
All measures are Borel probability measures on compact metric spaces. Exchangeability means invariance under **all finite permutations** of the coordinate index set \(\mathbb Z\), not merely shift invariance. The unique de Finetti mixing law \(\Pi\) is defined on \(\mathcal P([0,1])\) with its weak topology, and the endpoints of the closed support of a probability measure are measurable functions of that measure. Every stated radius refers to the specific weighted \(\ell^1\) metric above, not an arbitrary topologically equivalent metric. The maximum possible distance is \(3\), since \(\sum_{j\in\mathbb Z}2^{-|j|}=3\). At zero support diameter the associated Bernoulli measure is supported on a fixed sequence and has no positive expansivity radius.

## Proof
**1. A sharp Bernoulli threshold.** Fix a probability law \(\nu\) on \([0,1]\), with closed support extrema \(a,b\) and diameter \(d=b-a\). When \(d=0\), \(\nu^{\mathbb Z}\) is a Dirac mass on a constant sequence, and no positive radius works. Suppose \(d>0\). For \(r\ge3d/2\), take the constant target \(x_j=(a+b)/2\) for every \(j\). For every \(y\) in the full-measure product support \([a,b]^{\mathbb Z}\) and every \(n\),
\[
\rho(\sigma^n x,\sigma^n y)\le\frac d2\sum_{j\in\mathbb Z}2^{-|j|}=\frac{3d}{2}\le r.
\]
Hence \(\nu^{\mathbb Z}(\Gamma_r(x))=1\), and \(r\) is not an expansivity radius.

For the converse fix \(0<r<3d/2\) and **any deterministic target** \(x\in Q\). Choose \(K\ge0\) and \(0<\eta<d/2\) such that
\[
(d/2-\eta)\,S_K>r,\qquad S_K=\sum_{|j|\le K}2^{-|j|}=3-2^{1-K}.
\]
Such \(K,\eta\) exist because \(S_K\uparrow3\). Both endpoint neighborhoods \([a,a+\eta]\) and \([b-\eta,b]\) have positive \(\nu\)-mass, since \(a,b\) belong to the support. Let \(p>0\) be the smaller of these two masses. For every index \(k\), at least one endpoint \(e_k\in\{a,b\}\) satisfies \(|x_k-e_k|\ge d/2\). Choose it deterministically. The event \(|Y_k-e_k|\le\eta\) thus has probability at least \(p\), and on this event \(|Y_k-x_k|\ge d/2-\eta\), for \(Y\sim\nu^{\mathbb Z}\).

Choose infinitely many disjoint integer blocks \(\{n_\ell-K,\ldots,n_\ell+K\}\), \(\ell\ge1\). The corresponding events requiring the endpoint condition at **every** coordinate in each block are independent; each has probability at least \(p^{2K+1}>0\). By the second Borel–Cantelli lemma, infinitely many of them occur with probability one. On each occurrence,
\[
\rho(\sigma^{n_\ell}x,\sigma^{n_\ell}Y)
\ge(d/2-\eta)S_K>r.
\]
Therefore \(\nu^{\mathbb Z}(\Gamma_r(x))=0\). This holds for every target \(x\), establishing the exact Bernoulli threshold including failure at equality.

**2. Exchangeable measures.** The de Finetti–Hewitt–Savage theorem for standard Borel alphabets gives the stated unique mixture representation, after enumerating \(\mathbb Z\). Write \(d_*=\operatorname{ess\,inf}_{\Pi}D\). If \(0<r<3d_*/2\), the Bernoulli result implies \(\nu^{\mathbb Z}(\Gamma_r(x))=0\) for \(\Pi\)-almost every \(\nu\) for **each** \(x\). Integration proves \(\mu(\Gamma_r(x))=0\) for every target \(x\).

Conversely let \(r>3d_*/2\). Choose \(\alpha\) satisfying \(d_*<\alpha<2r/3\). Then \(A=\{\nu:D(\nu)<\alpha\}\) has positive \(\Pi\)-mass. Since the interval of possible support midpoints \(c_\nu=(\min\operatorname{supp}\nu+\max\operatorname{supp}\nu)/2\) is compact, finitely many center neighborhoods of radius less than \(r/3-\alpha/2\) cover it. At least one neighborhood of center \(c\in[0,1]\) contains the midpoints of a positive-\(\Pi\)-mass subset \(A_c\subset A\). For every \(\nu\in A_c\), every support point \(s\) obeys \(|s-c|<r/3\). Let \(x=(\ldots,c,c,c,\ldots)\); then \(\nu^{\mathbb Z}(\Gamma_r(x))=1\) for every \(\nu\in A_c\). Consequently
\[
\mu(\Gamma_r(x))\ge\Pi(A_c)>0.
\]
Thus no \(r>3d_*/2\) works. These two implications prove both boxed formulas, including \(d_*=0\).

**3. Full-support counterexample.** For the specified mixture, the weights sum to one, and every component is an ergodic, strongly mixing Bernoulli process with a nondegenerate marginal: thus every component is expansive by step 1. The \(\lambda^{\mathbb Z}\) component gives full support of \(\mu\) on \(Q\), and all components are atomless, so \(\mu\) is atomless. The interval diameter for \(u_m\) is \(1/(2m)\), hence the essential infimum of all component support diameters is zero. Equivalently, for any \(r>0\), choose \(m\) with \(3/(4m)\le r\). With the constant target \(x_j=1/2\), the \(u_m^{\mathbb Z}\)-component is entirely contained in \(\Gamma_r(x)\), giving \(\mu(\Gamma_r(x))\ge2^{-(m+1)}>0\). The mixed law is therefore not expansive, despite all of its ergodic components being expansive.

## Verification
All infinite-parameter assertions follow from the preceding proof; the finite-block event argument is not replaced by finite enumeration. The exact identity \(S_K=3-2^{1-K}\), the component-diameter formulas, and the mixture-weight normalization admit independent rational-arithmetic checks using `verify_examples.py` included with this result. That script verifies illustrative finite-block inequalities but does not itself prove the almost-sure Borel–Cantelli conclusion or the de Finetti representation. The boundary target for a Bernoulli law is explicit and establishes that \(r=3D(\nu)/2\) cannot be included in its expansive-radius interval.

## Relationship to prior work
Lacerda [1, Theorem A and Section 2] proves that the Hilbert-cube shift is expansive for product Lebesgue measure and gives \(0<r<1/2\) as sufficient for the same metric. Here its **optimal supremal radius** is \(3/2\), and the theorem extends to all *exchangeable dependent* invariant laws through a sharp de Finetti-mixture criterion. Lacerda's discussion of non-identically distributed independent marginals does not assert a dependent-mixture criterion or its sharp radius. The published independent-coordinate concentration classification [2] gives an iff statement for measures \(\bigotimes_j\nu_j\); it does not cover nontrivial dependent exchangeable mixtures \(\int\nu^{\mathbb Z}\Pi(d\nu)\) and does not determine the sharp constant \(3D(\nu)/2\) in this metric. Lee–Morales–Shin [3, Lemma 3.2] prove convexity of the class of measures sharing a **fixed** expansivity constant; our example does not contradict this and instead shows why varying radii cannot be ignored under countably infinite mixtures. The representation theorem itself is classical [4, 5].

## Limitations
The criterion is confined to exchangeable (finite-permutation invariant) measures; it does not classify general stationary dependent processes. Sharp numerical radii depend on the specified metric, though the existence of some positive expansivity radius is topologically invariant. Whether a general exchangeable mixture is expansive **at the critical radius** \(3d_*/2\) is not determined. The example is a mathematical invariant mixture, not a claim about the occurrence of such a mixture in physical systems. An equivalent statement could exist in unindexed symbolic dynamics or probability literature.

## References
[1] G. Lacerda, *Typical expansive measures for infinite-dimensional maps*, arXiv:2610.09482v1 (first public 2026-10-07), https://arxiv.org/html/2610.09482v1.

[2] *A concentration criterion and Baire dichotomy for product measures on the Hilbert-cube shift*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-concentration-criterion-and-baire-dichotomy-for-product-measur--a21666c938a0 (RESULT.md inspected).

[3] K. Lee, C. A. Morales and B. Shin, *On the set of expansive measures*, Communications in Contemporary Mathematics 20 (2018), 1750086, DOI:10.1142/S0219199717500869, https://www.researchgate.net/publication/320301812_On_the_set_of_expansive_measures (Lemma 3.2 inspected).

[4] E. Hewitt and L. J. Savage, *Symmetric Measures on Cartesian Products*, Transactions of the American Mathematical Society 80 (1955), 470–501, DOI:10.1090/S0002-9947-1955-0076206-8.

[5] T. Fritz, T. Gonda and P. Perrone, *De Finetti's Theorem in Categorical Probability*, arXiv:2105.02639 (2021), https://arxiv.org/abs/2105.02639.
