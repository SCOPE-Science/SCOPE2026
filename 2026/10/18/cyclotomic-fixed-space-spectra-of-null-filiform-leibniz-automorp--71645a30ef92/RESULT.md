# Cyclotomic fixed-space spectra of null-filiform Leibniz automorphisms

## Finding

Let \(n\ge2\), let \(k=\mathbb F_q\) be any finite field, and let \(L_n\) be the right Leibniz algebra with basis \(e_1,\ldots,e_n\) and the only nonzero basis products
\[
[e_i,e_1]=e_{i+1}\qquad(1\le i<n).
\]
For \(\phi\in\operatorname{Aut}_k(L_n)\), set \(d(\phi)=\dim_k\ker(\phi-I)\). Write \(\varphi\) for Euler's totient function. Then the complete fixed-space generating polynomial \(P_{n,q}(T)=\sum_{\phi}T^{d(\phi)}\) is
\[
\boxed{P_{n,q}(T)=q^{n-1}\!\sum_{\substack{\ell\mid(q-1)\\\ell>n}}\!\varphi(\ell)
+\sum_{\substack{\ell\mid(q-1)\\\ell\le n}}\!\varphi(\ell)
\left[\sum_{j=1}^{\lfloor n/\ell\rfloor-1}(q-1)q^{n-1-j}T^j
+q^{n-\lfloor n/\ell\rfloor}T^{\lfloor n/\ell\rfloor}\right].}
\]
An empty inner sum is zero. This holds without any restriction on the characteristic, including \(q=2\). In particular, an automorphism with no nonzero fixed vector exists if and only if \(q-1>n\), and their number is \(q^{n-1}\sum_{\ell\mid(q-1),\,\ell>n}\varphi(\ell)\).

There is also a conjugacy-normal-form theorem explaining this formula. Fix an automorphism whose coefficient of \(e_1\) in \(\phi(e_1)\) is \(a\in k^\times\), and let \(\ell=\operatorname{ord}(a)\). Under an explicit identification with \(k[t]/(t^n)\), the operator \(\phi\) is \(aU(t)\sigma_a\), where \(U(0)=1\) and \(\sigma_a f(t)=f(at)\). Conjugation by the subgroup with leading coefficient one takes \(\phi\) to a **unique** operator \(aH(t^\ell)\sigma_a\) with \(H(0)=1\). Exactly \(q^{\lfloor(n-1)/\ell\rfloor}\) such conjugacy classes occur at a fixed \(a\); each has \(q^{n-1-\lfloor(n-1)/\ell\rfloor}\) automorphisms. If \(m=\lfloor n/\ell\rfloor>0\), the fixed-space dimension of the representative is the lesser of \(m\) and the order of vanishing of \(H(z)-1\) at \(z=0\). If \(m=0\), it is zero.

For every integer \(s\ge0\), the number of \(\operatorname{Aut}(L_n)\)-orbits on ordered \(s\)-tuples is exactly
\[
\frac{P_{n,q}(q^s)}{(q-1)q^{n-1}}.
\]
For one-tuples this specializes to \(1+\sum_{i=1}^{n}\gcd(i,q-1)\), providing a separate check of the classification.

## Assumptions and scope

The bracket is bilinear and satisfies the **right** Leibniz identity \([x,[y,z]]=[[x,y],z]-[[x,z],y]\). Every omitted basis product is zero. The result concerns field-linear algebra automorphisms, not derivations, local automorphisms, or automorphisms of the underlying additive group. Here \(q\) is any prime power, \(n\ge2\), and all kernels and ranks are over \(\mathbb F_q\). The integer \(\ell\) ranges over positive divisors of \(q-1\), and \(\operatorname{ord}(a)\) is the multiplicative order in \(k^\times\). Define the vanishing order of the zero series to be \(+\infty\).

## Proof

**1. Parameterization.** Every algebra endomorphism is determined by \(\phi(e_1)=a e_1+b_2e_2+\cdots+b_ne_n\), since \(e_{i+1}=[e_i,e_1]\). Induction gives
\[
\phi(e_i)=a^{i-1}\sum_{r=1}^{n-i+1}b_r e_{i+r-1},\qquad b_1=a.
\]
For \(a\ne0\), its diagonal entries are \(a,a^2,\ldots,a^n\), so it is invertible; its image of \(e_j\) for \(j\ge2\) has zero \(e_1\)-coefficient, ensuring that all defining zero brackets are preserved. Conversely, \(a=0\) implies \(\phi(e_2)=0\). Thus \(|\operatorname{Aut}(L_n)|=(q-1)q^{n-1}\), and the parameters are unique.

Identify \(e_i\longleftrightarrow t^{i-1}\) in \(R=k[t]/(t^n)\). Put \(U(t)=1+\sum_{j=1}^{n-1}(b_{j+1}/a)t^j\) and \(\sigma_a f(t)=f(at)\). Directly from the displayed formula, \(\phi\) acts as \(aM_U\sigma_a\), where \(M_U\) denotes multiplication by \(U\). When \(a=1\), these operators are exactly the multiplications \(M_W\) for arbitrary units \(W\in1+tR\).

**2. Unique resonant normal form.** Fix \(a\) of order \(\ell\); note that \(\ell\mid(q-1)\), so \(\ell\) is prime to the characteristic. Conjugating \(aM_U\sigma_a\) by \(M_W\), with \(W\in1+tR\), replaces \(U\) by \(U(t)W(at)/W(t)\). Construct \(W=1+\sum_{j=1}^{n-1}w_jt^j\) and \(H=1+\sum_{r=1}^{\lfloor(n-1)/\ell\rfloor}h_rz^r\) recursively from
\[
U(t)W(at)=H(t^\ell)W(t)\pmod{t^n}.
\]
At degree \(j\), earlier choices being fixed, the new contribution from \(w_j\) to the difference of the two sides is \((a^j-1)w_j\). If \(\ell\nmid j\), this scalar is invertible, and one can choose a unique \(w_j\) to cancel the coefficient. If \(\ell\mid j\), choose \(w_j=0\) and set the unique coefficient \(h_{j/\ell}\) to cancel the difference. This proves existence.

For uniqueness, let \(N(U)=\prod_{r=0}^{\ell-1}U(a^rt)\). Conjugation does not change this norm, by telescoping. For \(U=H(t^\ell)\), it equals \(H(t^\ell)^\ell\). Raising to the \(\ell\)-th power is an automorphism of the finite abelian \(p\)-group \(1+t^\ell k[t^\ell]/(t^n)\) because \(\gcd(\ell,p)=1\). Thus \(H\) is uniquely determined by \(N(U)\). Conversely, units \(W\) centralizing \(aM_H\sigma_a\) satisfy \(W(at)=W(t)\), exactly the units supported at exponents divisible by \(\ell\). There are \(q^{M}\) of them, where \(M=\lfloor(n-1)/\ell\rfloor\). Orbit-stabilizer in the group \(1+tR\), of order \(q^{n-1}\), gives \(q^{n-1-M}\) elements per orbit and \(q^M\) distinct normal forms. In particular, the coefficients \(h_1,\ldots,h_M\) are uniformly distributed as \(U\) varies with fixed \(a\).

**3. Exact kernel dimensions.** Split the monomial basis of \(R\) into congruence classes modulo \(\ell\): for each residue \(r\), use the span of \(t^{r+j\ell}\) with exponent less than \(n\). Because \(H(t^\ell)\) preserves each class, \(aH(t^\ell)\sigma_a-I\) restricts there to multiplication by \(a^{r+1}H(z)-1\). If \(a^{r+1}\ne1\), this is a unit and has zero kernel. The only possible exceptional residue is \(r=\ell-1\), occurring exactly when \(\ell\le n\); its dimension is \(m=\lfloor n/\ell\rfloor\). On that summand the operator is multiplication by \(H(z)-1\) in \(k[z]/(z^m)\), whose kernel has dimension \(\min(m,\operatorname{ord}_z(H-1))\). For \(1\le j<m\), this dimension equals \(j\) precisely when \(h_1=\cdots=h_{j-1}=0\) and \(h_j\ne0\); this occurs with probability \((q-1)q^{-j}\). Dimension \(m\) occurs precisely when \(h_1=\cdots=h_{m-1}=0\), with probability \(q^{-(m-1)}\). These coefficients exist even if \(n\) is a multiple of \(\ell\). If \(m=0\), there is no eigenvalue one and the kernel is zero.

For a fixed scalar \(a\), multiply these probabilities by \(q^{n-1}\). There are exactly \(\varphi(\ell)\) elements of order \(\ell\) in the cyclic group \(\mathbb F_q^\times\). Summing over these orders gives the asserted polynomial, including its boundary cases. Burnside's lemma applies to the diagonal action on \(L_n^s\): an automorphism with fixed-space dimension \(d\) fixes exactly \(q^{sd}\) tuples. The one-tuple formula can also be obtained directly: a nonzero element with first nonzero basis coefficient at \(e_i\) has \(\gcd(i,q-1)\) orbits, since its leading coefficient varies by \(i\)-th powers and the free higher automorphism parameters eliminate all later coefficients.

## Verification

The standalone file `verify.py` constructs each automorphism matrix directly from its defining brackets, computes \(\dim\ker(\phi-I)\) by independent finite-field Gaussian elimination, and compares complete distributions with the theorem. It exhausts 13 field-and-dimension cases over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_8,\mathbb F_9\). It separately verifies the normal-form conjugacy equation, class counts and equal orbit sizes for four cases, and checks Burnside's one-tuple formula in every enumerated case. All checks return `VERIFY_OK`. The arbitrary-\(n\) and arbitrary-\(q\) assertions are proved above, not inferred from finite experiments.

## Relationship to prior work

Casas, Ladra, Omirov and Karimjanov (2012, arXiv:1202.5275) provide the canonical null-filiform Leibniz algebra model while classifying solvable extensions; Khudoyberdiyev and Omirov (2013, arXiv:1304.0126) study cohomology and deformations. Calderón, Camacho, Kaygorodov and Omirov (2017, arXiv:1708.01753) determine the automorphism form and cyclic toral gradings, including residue-class eigen-decompositions for diagonal automorphisms. Normurodovna (2026, DOI:10.55640/eijmrms-06-06-16) provides the automorphism matrix and studies local maps over \(\mathbb C\). The contribution here is the **complete finite-field fixed-space multiplicity distribution for all automorphisms**, including their nonsemisimple resonances, together with the unipotent-conjugacy normal form and orbit sizes. The sources inspected do not state these conclusions; the normal form is not a consequence of listing toral gradings alone.

## Limitations

The theorem is specific to the stated right null-filiform Leibniz algebra; it does not classify arbitrary filiform Leibniz algebras, derivation fixed spaces, or automorphism conjugacy under the full group (only the subgroup with leading coefficient one at each fixed scalar). Independent external mathematical audit has not been performed. Literature searches cannot prove global novelty; further unlocated algebraic-group treatments could contain equivalent results.

## References

1. J. M. Casas, M. Ladra, B. A. Omirov, I. A. Karimjanov, *Classification of solvable Leibniz algebras with null-filiform nilradical*, arXiv:1202.5275 (first posted 2012-02-23), Sections 2–3, https://arxiv.org/abs/1202.5275.
2. A. Kh. Khudoyberdiyev and B. A. Omirov, *Infinitesimal deformations of null-filiform Leibniz superalgebras*, arXiv:1304.0126 (first posted 2013-03-30), Sections 2–3, https://arxiv.org/abs/1304.0126.
3. A. Calderón, L. Camacho, I. Kaygorodov and B. Omirov, *Gradings of null-filiform and naturally graded filiform Leibniz algebras*, arXiv:1708.01753 (first posted 2017-08-05), Section 3.1, https://arxiv.org/abs/1708.01753.
4. O. N. Normurodovna, *Derivations, Automorphisms And Local Derivations of Null-Filiform Leibniz Algebras*, European International Journal of Multidisciplinary Research and Management Studies 6 (2026), 94–100, DOI:10.55640/eijmrms-06-06-16; Theorem 2 and Section 8, https://doi.org/10.55640/eijmrms-06-06-16.
