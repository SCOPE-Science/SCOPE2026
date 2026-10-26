# Odd-truncation centralizer spectra for quadratic Frobenius-skew local rings

## Finding
Let \(s\ge 2\) be any prime power, \(K=\mathbb F_{s^2}\), \(L=\mathbb F_s\), and \(\sigma(c)=c^s\). For each integer \(a\ge1\) consider the associative unital finite ring
\[
R_a=K[x;\sigma]/(x^{2a+1}),\qquad xc=\sigma(c)x\quad(c\in K).
\]
Here \((x^{2a+1})\) is a two-sided ideal because \(\sigma\) is an automorphism. Define \(S=L[z]/(z^a)\). There is an additive isomorphism \(R_a/Z(R_a)\cong S^3\) under which **two elements of \(R_a\) commute precisely when the exterior product of their corresponding vectors in \(S^3\) vanishes**.

In particular \(|R_a|=s^{4a+2}\), \(|Z(R_a)|=s^{a+2}\), and the multiset of element-centralizer orders is exact:
\[
\begin{aligned}
&\#\{u:|C_{R_a}(u)|=s^{4a+2}\}=s^{a+2},\\
&\#\{u:|C_{R_a}(u)|=s^{2a+2+2t}\}
=s^{a+2}\bigl(s^{3(a-t)}-s^{3(a-t-1)}\bigr),\quad 0\le t<a.
\end{aligned}
\]
All listed centralizer orders are distinct, and there are no other possibilities. Consequently the commuting probability for independent uniformly sampled elements is
\[
\boxed{\displaystyle
\Pr_{u,v\in R_a}(uv=vu)
=s^{-3a}+s^{-2a}(1+s^{-1}+s^{-2})(1-s^{-a}).}
\]
As \(a\to\infty\) for fixed \(s\), this is asymptotic to \((1+s^{-1}+s^{-2})s^{-2a}\). All assertions include characteristic two.

## Assumptions and scope
The symbol \(K[x;\sigma]\) denotes a univariate Ore extension with zero \(\sigma\)-derivation. Every element of its quotient has a unique expression \(\sum_{i=0}^{2a}c_ix^i\) with \(c_i\in K\). Centralizers \(C_{R_a}(u)=\{v\in R_a:uv=vu\}\) are counted as sets, not necessarily commutative subrings. All probabilities use ordered independent uniform samples, with diagonal pairs included. The result concerns **odd** truncations \(2a+1\); no formula for even truncations is asserted. The parameter \(s\) can be a nonprime prime power.

For a vector \(v=(v_1,v_2,v_3)\in S^3\), its exterior square with \(w\) is zero if and only if all three minors \(v_iw_j-v_jw_i\), for \(1\le i<j\le3\), vanish in \(S\). For nonzero \(v\), define \(\nu(v)=\min_i\nu_z(v_i)\), where \(\nu_z(0)=a\); put \(\nu(0)=a\). The valuation is independent of representatives modulo \(z^a\).

## Proof
**Step 1: the central quotient and its commutation form.** Put \(z=x^2\), which commutes with every coefficient in \(K\) and with \(x\). Choose \(\theta\in K\setminus L\), and set \(\Delta=\sigma(\theta)-\theta\ne0\). Because \([K:L]=2\), write \(\sigma(\theta)=\theta+\Delta\), with \(\Delta\in K^\times\); no characteristic restriction is needed. Each \(u\in R_a\) can be written **uniquely** in the form
\[
 u=U(z)+\theta V(z)+z^a C+\bigl(B(z)+\theta D(z)\bigr)x,
\]
where \(U,V,B,D\in S\), \(C\in K\), and the first two terms use the standard representatives of degree below \(a\). Thus \(u\mapsto(V,B,D)\) is a surjective additive map to \(S^3\) with fibers of size \(s^a s^2=s^{a+2}\).

Take \(v\) similarly, with primed coefficients \(V',B',D'\). Separate even and odd powers of \(x\). The odd component of \(uv-vu\) is
\[
\Delta\bigl[(BV'-B'V)+\theta(DV'-D'V)\bigr]x,
\]
where coefficients are reduced modulo \(z^a\). The even component is
\[
 z\Delta(BD'-B'D),
\]
where the multiplier \(z\) embeds \(S\) injectively as \(zK[z]/(z^{a+1})\). Since \(\Delta\) is invertible and \(1,\theta\) are linearly independent over \(L\), the commutator vanishes if and only if
\[
BV'-B'V=DV'-D'V=BD'-B'D=0\quad\text{in }S.
\]
These are precisely the three exterior minors of \((V,B,D)\) and \((V',B',D')\). An element commutes with everything if and only if its image is zero: take the three standard basis vectors as test partners. Hence the kernel is exactly \(Z(R_a)\), giving \(R_a/Z(R_a)\cong S^3\) additively, with \(|Z(R_a)|=s^{a+2}\). Finally \(|R_a|=|K|^{2a+1}=s^{4a+2}\).

**Step 2: rank-one incidence over a chain ring.** If \(v\ne0\) has valuation \(t\in\{0,\ldots,a-1\}\), write \(v=z^t v_0\), where \(v_0\) has at least one unit coordinate. A matrix in \(\mathrm{GL}_3(S)\) sends \(v_0\) to the first standard basis vector. Such a change of basis preserves the vanishing of exterior products, so the number of \(w\in S^3\) with \(v\wedge w=0\) is the number satisfying
\[
z^t w_2=z^t w_3=0.
\]
Each of \(w_2,w_3\) has \(s^t\) choices from the annihilator \(z^{a-t}S\), while \(w_1\) has \(s^a\) choices. Therefore this number equals \(s^{a+2t}\). When \(v=0\), every one of the \(s^{3a}\) vectors commutes with it.

There are \(s^{3(a-t)}-s^{3(a-t-1)}\) vectors of valuation exactly \(t\): subtract those divisible by \(z^{t+1}\) from all vectors divisible by \(z^t\). Multiplying by the common fiber size \(|Z(R_a)|\) gives the element multiplicities. Multiplying the vector centralizer counts by the same factor yields \(|C_{R_a}(u)|=s^{a+2}s^{a+2t}=s^{2a+2+2t}\). The central case \(v=0\) gives the full ring size.

**Step 3: commuting probability.** Since all additive fibers have the same size, the proportion of commuting ordered pairs in \(R_a\) equals that in \(S^3\) under exterior-zero incidence. Thus
\[
\begin{aligned}
\Pr(uv=vu)
&=s^{-6a}\left(s^{3a}+\sum_{t=0}^{a-1}
\bigl[s^{3(a-t)}-s^{3(a-t-1)}\bigr]s^{a+2t}\right)\\
&=s^{-3a}+s^{-2a}(1-s^{-3})\sum_{t=0}^{a-1}s^{-t}\\
&=s^{-3a}+s^{-2a}(1+s^{-1}+s^{-2})(1-s^{-a}).
\end{aligned}
\]
The final asymptotic follows because \(s^{-a}\to0\). Each step is an exact finite-ring count, not an asymptotic approximation.

## Verification
The standalone file `verify_skew_commuting.py` implements arithmetic in explicit finite fields, constructs Ore products by the twisting rule, and enumerates commuting pairs without invoking the exterior-product theorem. Run `python verify_skew_commuting.py`. Exhaustive cases are \((s,2a+1)=(2,3),(2,5),(3,3)\), corresponding to ring sizes \(64,1024,729\). It also verifies twelve complete centralizer sizes over \(\mathbb F_{16}\) with fixed subfield \(\mathbb F_4\). Exhaustive centralizer histograms are respectively \(\{16:56,64:8\}\), \(\{64:896,256:112,1024:16\}\), and \(\{81:702,729:27\}\); ordered commuting-pair counts are \(1408,102400,76545\). Expected terminal marker: `ALL_SKEW_TRUNCATION_CHECKS_PASSED`. These cases do not prove the theorem for arbitrary \(a,s\); the proof above does.

## Relationship to prior work
Dutta, Basnet, and Nath develop the classification and commuting probabilities of finite rings with small numbers of distinct element-centralizers (arXiv:1803.04111, especially Section 3). Here the number of *centralizer sizes* is \(a+1\), not a classification by the number of distinct centralizer subsets; the stated profile requires an explicit computation for a varying family of local Ore quotients. Juráš and Ursul relate the possible commuting probabilities of arbitrary finite rings to class-two nilpotent groups (arXiv:2010.01188, Theorem 2.1), but this global value-set theorem does not calculate the above parameterized ring profile. Martínez-Peñas' classification of finite-field skew polynomial constructions (arXiv:1908.06833, Section 7) supplies an important structural setting, not the element-centralizer enumeration. Boulagouaz and Deajim (2022) treat finite-ring skew-polynomial quotients for code generator, control, and parity-check matrices, rather than ring commutator fibers. Richter and Silvestrov's Ore-centralizer results (arXiv:1308.3430) concern a polynomial-ring coefficient algebra and noninvertible endomorphisms, not the quadratic Galois involution quotient considered here.

The reduction of commutation to three minors is the new structural statement being assessed, along with the complete centralizer-order distribution and its asymptotic commuting probability. This is not a claim to have introduced Ore extensions, the standard centralizer identity for commuting probability, or basic local-ring valuation counts.

## Limitations
Only involutive quadratic Frobenius twists and odd nilpotence cutoffs are covered. Even cutoffs have a different top-degree condition and are not settled here. The result counts centralizer *orders*, not the number of distinct centralizer subsets, their ring isomorphism types, or their inclusion lattice. Existing general results could potentially imply the probability after an additional ring-specific reduction; an equivalent unindexed computation cannot be excluded. No independent mathematical audit has been performed. Sample computations cover only the finite configurations listed.

## References
1. J. Dutta, D. K. Basnet, R. K. Nath, *Commuting probabilities of \(n\)-centralizer finite rings*, arXiv:1803.04111v1 (2018-03-12), Section 3.
2. M. Juráš, M. Ursul, *On commuting probabilities in finite groups and rings*, arXiv:2010.01188v1 (2020-10-02), Theorem 2.1.
3. U. Martínez-Peñas, *Classification of multivariate skew polynomial rings over finite fields via affine transformations of variables*, arXiv:1908.06833v1 (2019-08-19), Section 7, Theorems 5–6.
4. M. Boulagouaz, A. Deajim, *Characterizations and Properties of Monic Principal Skew Codes over Rings*, DOI:10.1155/2022/9294459 (2022), Sections 3–6.
5. J. Richter, S. Silvestrov, *Centralizers in Ore extensions of polynomial rings*, arXiv:1308.3430, introduction and Theorem 1.1; scope comparison only.
