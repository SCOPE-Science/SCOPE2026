# An all-degree spectral law for Fourier sampling on q-ary Hamming spheres

## Finding

Let \(q\ge3\) and \(n\ge2\) be integers, and let \(1\le d\le\min\{k,n-k\}\). On \(G=(\mathbb Z/q\mathbb Z)^n\), equip functions with the uniform probability inner product. Let \(\mathcal H_{\le d}\) be the span of characters involving at most \(d\) coordinates. Write \(S_k=\{x\in G:\#\{i:x_i\ne0\}=k\}\) and
\[
K=P_{\mathcal H_{\le d}}M_{\mathbf1_{S_k}}P_{\mathcal H_{\le d}}\big|_{\mathcal H_{\le d}}.
\]
The following formulas determine **every eigenvalue, with multiplicity, including the zero eigenspace**, for every integer alphabet size (prime-power or not).

Put \(p=(q-1)/q\), \(v=p(1-p)\), and define \(\binom{m}{-1}=0\). For \(0\le s\le d\) and \(0\le j\le d-s\), let
\[
m=n-s,\qquad \ell=k-s,\qquad r=d-s,\qquad
\kappa_{s,j,a}=[t^{a-j}](1+(1-p)t)^{\ell-j}(1-pt)^{m-\ell-j}
\]
for \(j\le a\le r\), and let \((b)_{\downarrow j}=b(b-1)\cdots(b-j+1)\), with \((b)_{\downarrow0}=1\). Set
\[
\boxed{\displaystyle
\Lambda_{s,j}=\binom m\ell p^\ell(1-p)^{m-\ell}
\frac{(\ell)_{\downarrow j}(m-\ell)_{\downarrow j}}{(m)_{\downarrow 2j}}
\sum_{a=j}^{r}\frac{\kappa_{s,j,a}^{\,2}}{v^a\binom{m-2j}{a-j}}.}
\]
**Each \(\Lambda_{s,j}\) is strictly positive**, occurring with multiplicity
\[
\boxed{\displaystyle
M_{s,j}=\binom ns(q-2)^s\left(\binom mj-\binom m{j-1}\right).}
\]
Equal values from different pairs are combined. There are no additional nonzero eigenvalues. More precisely,
\[
\boxed{\displaystyle
\operatorname{rank}K=\binom nd(q-1)^d,\quad
\ker K=\left(\sum_{i=1}^n\mathbf1_{\{x_i\ne0\}}-k\right)\mathcal H_{\le d-1},\quad
\dim\ker K=\sum_{a=0}^{d-1}\binom na(q-1)^a.}
\]
In particular, a single algebraic equation generates the **entire** nullspace in each allowed Fourier degree. Every positive singular value of the restriction map from \(\mathcal H_{\le d}\) to the shell, with the inherited full-group measure, is \(\sqrt{\Lambda_{s,j}}\), repeated \(M_{s,j}\) times. For shell-normalized probability measure, the squared singular values are \(\Lambda_{s,j}/\Pr(S_k)\). All eigenvalues are rational.

## Assumptions and scope

The group \(G\) has \(q^n\) elements and has normalized Haar counting measure. The orthogonal projector \(P_{\mathcal H_{\le d}}\) and multiplication \(M_{\mathbf1_{S_k}}\) both act on \(L^2(G)\). The Fourier interaction degree of a character is its number of nontrivial coordinate components. The spectrum refers to the compressed operator on \(\mathcal H_{\le d}\), **not** to its action on the full \(L^2(G)\). The requirement \(d\le\min\{k,n-k\}\) places the slice away from both degree-boundary collapses and guarantees all displayed denominators are positive. No field structure on the alphabet is used.

## Proof

**1. Label-contrast reduction.** On one copy of \(\mathbb Z/q\mathbb Z\), set \(z=\mathbf1_{\{x\ne0\}}\). The function space is the orthogonal sum of constants, the centered activity \(z-p\), and the \((q-2)\)-dimensional contrast space
\[
W=\left\{w:w(0)=0,\ \sum_{a\ne0}w(a)=0\right\}.
\]
This is an orthogonal decomposition for uniform measure; each nonconstant summand counts as one Fourier interaction. Tensor products split \(\mathcal H_{\le d}\) orthogonally by a subset \(T\subset[n]\) of \(s\) contrast coordinates, \(s\le d\), and a choice of one of \((q-2)^s\) contrast directions. The remaining coordinates carry biased Boolean squarefree polynomials of degree at most \(r=d-s\), with independent Bernoulli-\(p\) activities. In a shell inner product, contrast directions at distinct subsets, or distinct vectors in the same subset, are orthogonal because the nonzero letter at each contrast coordinate is averaged uniformly. Contrast functions vanish unless all \(s\) marked activities are one. Their conditional second moments gain a factor \(p^{-s}\), exactly canceling the probability \(p^s\) of those marked activities. Consequently, each such block is unitarily equivalent to the biased Boolean operator
\[
B_{m,\ell,r}=P_{\le r}^{(p)}M_{\mathbf1_{\{|z|=\ell\}}}P_{\le r}^{(p)},
\qquad (m,\ell,r)=(n-s,k-s,d-s),
\]
on \(m\) independent Bernoulli-\(p\) bits. There are \(\binom ns(q-2)^s\) identical copies.

**2. Harmonic irreducibles and their norms.** For \(0\le j\le r\), take a coefficient array \(h=(h_J)_{|J|=j}\) in the kernel of the Boolean lowering operator \((Dh)_I=\sum_{a\notin I}h_{I\cup\{a\}}\), for \(|I|=j-1\). The dimension of that kernel is \(\binom mj-\binom m{j-1}\) because \(j\le r\le m/2\). Let
\[
H_h(z)=\sum_{|J|=j}h_J\prod_{i\in J}z_i,\qquad
F_{a,h}(z)=\sum_{|U|=a}\left(\sum_{\substack{J\subseteq U\\|J|=j}}h_J\right)\prod_{i\in U}(z_i-p)
\]
for \(j\le a\le r\). The spaces spanned by \(F_{a,h}\), over all \(j\) and \(a\), exhaust the biased Boolean polynomial space of degree at most \(r\). Distinct \(a\) are orthogonal for product measure. For fixed \(a\), the incidence raising identity \(DU-UD=(m-2j)I\), applied successively, gives
\[
\langle F_{a,h},F_{a,h'}\rangle_p=
 v^a\binom{m-2j}{a-j}\langle h,h'\rangle,
\qquad \langle h,h'\rangle=\sum_{|J|=j}h_J\overline{h'_J}.
\]
The dimension and norm identities may also be obtained from the standard Young-orthogonal harmonic basis on the Boolean slice [1]. Their elementary incidence proof uses \(D=U^*\) and positivity of \(DU=UD+(m-2j)I\) below the midpoint.

**3. Restriction generating identity.** Harmonicity \(Dh=0\) implies \(H_h(z+c\mathbf1)=H_h(z)\) for every scalar \(c\). Consider
\[
\sum_{a=j}^{m}t^{a-j}F_{a,h}(z)
 =\prod_{i=1}^m(1+t(z_i-p))\,
 H_h\!\left(\frac{z_i-p}{1+t(z_i-p)}:1\le i\le m\right).
\]
For Boolean \(z_i\), the rational function in the argument is affine in \(z_i\), with slope \(B(t)=((1+(1-p)t)(1-pt))^{-1}\). Homogeneity and translation invariance turn the last factor into \(B(t)^jH_h(z)\). On the slice \(|z|=\ell\), the generating identity therefore becomes
\[
\sum_{a=j}^{m}t^{a-j}F_{a,h}(z)
=(1+(1-p)t)^{\ell-j}(1-pt)^{m-\ell-j}H_h(z).
\]
Coefficient comparison proves the exact restriction rule \(F_{a,h}|_{|z|=\ell}=\kappa_{s,j,a}H_h|_{|z|=\ell}\).

**4. Slice normalization.** On the uniform slice of weight \(\ell\), the harmonic quadratic form is permutation-invariant and scalar on the irreducible degree-\(j\) harmonic coefficient module. To compute its scalar, use \(H(z)=\prod_{b=1}^j(z_{u_b}-z_{v_b})\) for \(j\) disjoint coordinate pairs. Its coefficient norm squared is \(2^j\), while its squared slice mean is \(2^j\binom{m-2j}{\ell-j}/\binom m\ell\). Thus for all degree-\(j\) harmonic arrays,
\[
\mathbb E_{|z|=\ell}H_h\overline{H_{h'}}
=\frac{(\ell)_{\downarrow j}(m-\ell)_{\downarrow j}}{(m)_{\downarrow2j}}\langle h,h'\rangle.
\]
Orthogonality across distinct harmonic degrees on the slice follows from the same Young decomposition. The conditional restriction of the orthogonal vectors \(F_{a,h}\) for fixed \(j,h\) is therefore proportional to the **same** \(H_h\). For each coefficient direction \(h\), the compression is a rank-one Gram block across \(a=j,\ldots,r\). Its only positive eigenvalue is its squared restriction norm, namely \(\Lambda_{s,j}\), after multiplying by the Bernoulli slice mass \(\binom m\ell p^\ell(1-p)^{m-\ell}\). The multiplicity before and after restoring contrasts is exactly \(M_{s,j}\). Positivity follows already from \(\kappa_{s,j,j}=1\).

**5. Rank and exact kernel.** Summing positive multiplicities first over \(j\) and then over \(s\) gives
\[
\sum_{s=0}^{d}\binom ns(q-2)^s\binom{n-s}{d-s}
=\binom nd(q-1)^d.
\]
Indeed, \(\sum_{j=0}^{r}(\binom mj-\binom m{j-1})=\binom mr\). The proposed kernel inclusion is immediate because multiplication by the activity deviation \(L=\sum_i z_i-k\) annihilates every function on \(S_k\), and it maps \(\mathcal H_{\le d-1}\) into \(\mathcal H_{\le d}\).

For completeness, multiplication by \(L\) is injective in this degree range. Resolve a putative nonzero kernel vector by its contrast subset \(T\) and choose its highest nonzero Boolean degree \(a\le d-1-|T|\). On this summand, the top degree of multiplication by \(L\) is the incidence raising map from degree \(a\) to \(a+1\). Since \(a<(n-|T|)/2\), that raising map is injective by \(DU=UD+(m-2a)I\) and \(D=U^*\). Hence multiplication by \(L\) is injective on all of \(\mathcal H_{\le d-1}\). Its image has dimension \(\sum_{a=0}^{d-1}\binom na(q-1)^a\), which equals \(\dim\mathcal H_{\le d}-\operatorname{rank}K\). Therefore the displayed kernel inclusion is equality, completing the proof.

## Verification

The accompanying reproducible `artifacts/verify.py` computes complete rational Gram-matrix characteristic polynomials, independently from the spectral formula, for the cases \((q,n,k,d)=(3,4,2,2),(3,5,2,2),(4,4,2,2)\). All polynomial coefficients agree exactly. It also tests the genuinely higher-degree instance \((3,6,3,3)\) by independent floating-point matrix diagonalization of the full \(233\)-dimensional Fourier-band Gram matrix, finding the predicted \(160\) positive eigenvalues with an absolute spectral discrepancy below \(10^{-11}\). The code uses Python 3 with SymPy and NumPy; run `python artifacts/verify.py`. These finite checks are corroboration only, not a proof of the quantified theorem.

## Relationship to prior work

Filmus [1] constructs an orthogonal harmonic basis on **binary** Hamming slices, supplying foundational slice norm identities. Filmus and Mossel [2] analyze harmonic restriction, representation and polynomial uniqueness on **binary** slices. Vasil'eva [3] treats reconstruction of certain **individual** eigenspaces of the \(q\)-ary hypercube. Those frameworks motivate the problem and supply related techniques, but the statements examined do not give the complete all-degree spectrum of a **mixed Fourier band** compressed onto a nonbinary fixed-weight sphere, with label-contrast multiplicities and the explicit one-equation nullspace. Subsequent work on Hamming-ball adjacency spectra [4] concerns a different operator. The formulas here can be compared with known Krawtchouk and Johnson-scheme decompositions and may admit alternative algebraic derivations.

## Limitations

The theorem addresses the interior regime \(1\le d\le\min\{k,n-k\}\) only. It neither describes all boundary regimes nor proves any universal optimal reconstruction condition number: the formulas permit one to calculate the quotient condition number for chosen parameters. The comparison with the literature is finite and cannot establish absolute priority; equivalent formulas may be embedded in historical Terwilliger-algebra, association-scheme, or harmonic-analysis treatments. Independent mathematical verification has not been performed. Computational examples do not replace the all-parameter proof.

## References

[1] Y. Filmus, *An orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142 (first version publicly posted 2014-06-01), https://arxiv.org/abs/1406.0142.

[2] Y. Filmus and E. Mossel, *Harmonicity and invariance on slices of the Boolean cube*, arXiv:1507.02713 (first posted 2015-07-09), https://arxiv.org/abs/1507.02713.

[3] I. Vasil'eva, *Reconstruction of Eigenfunctions of q-ary n-dimensional Hypercube*, arXiv:1412.3622 (first posted 2014-12-11), https://arxiv.org/abs/1412.3622.

[4] A. Avni and A. Samorodnitsky, *Eigenvalues and eigenfunctions of a Hamming ball*, arXiv:2411.14597 (2024), https://arxiv.org/abs/2411.14597.
