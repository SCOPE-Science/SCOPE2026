# Full automorphism groups of a characteristic-two trigonal Kummer subfamily

## Finding
Let \(K\) be algebraically closed of characteristic \(2\), and let \(M\ge5\) be any odd integer with \(M\equiv2\pmod3\). Let \(X_M\) be the smooth projective model of
\[
y^3=x^M+x^{-M}.
\]
Then \(g(X_M)=M\) and
\[
\operatorname{Aut}_K(X_M)
=\langle a,b,t\rangle\cong C_3\times D_{2M},
\qquad |\operatorname{Aut}_K(X_M)|=6M,
\]
where \(D_{2M}\) has order \(2M\), and, for primitive roots of unity \(\zeta_3,\zeta_M\in K\),
\[
a(x,y)=(x,\zeta_3y),\quad b(x,y)=(\zeta_Mx,y),\quad t(x,y)=(x^{-1},y).
\]
In particular, \(X_5=X_{3,5}\) has genus five, full automorphism group \(C_3\times D_{10}\) of order \(30\), and a normal cyclic subgroup of order \(15\).

## Assumptions and scope
All automorphisms are geometric \(K\)-automorphisms of the unique smooth projective curve with the indicated function field. The characteristic is exactly two; \(M\) is odd, at least five, and congruent to two modulo three. No conclusion is asserted for \(M\equiv0,1\pmod3\), for smaller genera, or for curves with other Kummer exponents. The convention \(D_{2M}\) refers to the order-\(2M\) dihedral group.

## Proof
**1. Kummer cover and ramification.** Put \(f(x)=x^M+x^{-M}\). In characteristic two,
\[
f(x)=\frac{(x^M+1)^2}{x^M},\qquad
\operatorname{div}_{\mathbf P^1}(f)
=2\sum_{\zeta^M=1}[\zeta]-M[0]-M[\infty].
\]
The \(M\) roots are distinct since \(M\) is odd. Each of these \(M+2\) valuations is prime to three: their orders are \(2\) and \(-M\), with \(3\nmid M\). Consequently \(K(X_M)/K(x)\) is a separable cyclic Kummer extension of degree three, totally and tamely ramified over precisely those \(M+2\) base points. Riemann–Hurwitz gives
\[
2g(X_M)-2=3(-2)+(M+2)(3-1)=2M-2,
\]
so \(g(X_M)=M\ge5\).

**2. Uniqueness of the trigonal pencil.** If \(K(x')\subset K(X_M)\) were another rational subfield with \([K(X_M):K(x')]=3\) and \(K(x')\ne K(x)\), then the compositum \(K(x)K(x')\) would equal \(K(X_M)\): the degree-three extension over \(K(x)\) has no proper intermediate field, and \(K(x')\) is not contained in \(K(x)\). Thus \((x,x'):X_M\to\mathbf P^1\times\mathbf P^1\) would be birational onto a curve of bidegree \((3,3)\). Such a curve has arithmetic genus \((3-1)(3-1)=4\), and the genus of its normalization is at most four. This contradicts \(g(X_M)\ge5\). Therefore \(K(x)\) is the unique degree-three rational subfield (the unique trigonal pencil up to change of coordinate).

**3. Normality of the deck group.** Every automorphism \(\sigma\in\operatorname{Aut}_K(X_M)\) consequently preserves \(K(x)\); its restriction is \(x\mapsto\phi(x)\) for some \(\phi\in\operatorname{PGL}_2(K)\). Hence the cubic deck group \(A=\langle a\rangle\cong C_3\) is normal. The induced homomorphism
\[
\operatorname{Aut}_K(X_M)\longrightarrow\operatorname{PGL}_2(K)
\]
has kernel exactly \(A\), since \(K(X_M)/K(x)\) is Galois of degree three.

**4. Distinct Kummer-residue classes constrain the base map.** As \(A\) is normalized, its two nontrivial eigenlines over \(K(x)\) are \(K(x)y\) and \(K(x)y^2\). Thus, for some \(s\in\{1,2\}\) and \(u(x)\in K(x)^*\),
\[
\sigma(y)=u(x)y^s,\qquad f(\phi(x))=u(x)^3f(x)^s.
\]
Taking valuations at every point of \(\mathbf P^1\) modulo three, the multiset of nonzero residues of \(\operatorname{div}(f)\) must be carried to its scalar multiple by \(s\). Since \(-M\equiv1\pmod3\), exactly **two** branch points (\(0,\infty\)) have residue \(1\), whereas exactly **\(M\)** branch points (\(\mu_M\)) have residue \(2\). If \(s=2\), the two residue classes would be exchanged bijectively, requiring \(2=M\), which is impossible. Thus \(s=1\), and \(\phi\) must preserve each of the two subsets
\[
\{0,\infty\},\qquad \mu_M=\{\zeta\in K:\zeta^M=1\}.
\]

**5. Base transformations and lifts.** A projectivity preserving \(\{0,\infty\}\) setwise has the form \(\phi(x)=cx\) or \(\phi(x)=c/x\). Preservation of \(\mu_M\) is equivalent to \(c^M=1\). Therefore the base-image of the full automorphism group is contained in the order-\(2M\) dihedral group of these transformations. Every such transformation fixes \(f\): indeed \(f(\zeta_Mx)=f(x)\) and \(f(x^{-1})=f(x)\). The displayed maps \(b,t\) consequently lift all \(2M\) base transformations. The kernel is exactly \(A\), so the full group has order \(3\cdot2M=6M\). Finally \(a\) centralizes \(b,t\), while \(b^M=t^2=1\) and \(tbt=b^{-1}\). This proves the claimed direct-product structure, and the cyclic group \(\langle a,b\rangle\cong C_{3M}\) is normal as an index-two subgroup.

## Verification
The accompanying standalone `verify.py` checks, for a representative set of admissible exponents, exact characteristic-two polynomial identities and squarefreeness, the residue populations, the Riemann–Hurwitz genus equation, and a faithful permutation realization of the generated group with \(6M\) distinct elements. Its finite checks are **not** substituted for the argument covering every admissible \(M\). The critical uniqueness and Kummer character arguments are proven in Steps 2–4, independently of sampling.

## Relationship to prior work
Marco Timpanella's paper [1], Theorem 1.2 and Example 4.7, constructs the explicit subgroup \(C_3\times D_{2M}\) and notes its genus; Proposition 6.6 proves that this subgroup is full **if and only if** the order-\(3M\) subgroup is normal. Remark 6.7 specifically leaves that normality question open outside a larger-automorphism subfamily and singles out \(X_{3,5}\) as the first case. The present proof supplies an unconditional normality argument for all \(M\equiv2\pmod3\), \(M\ge5\), and thus determines the full group for those curves. The uniqueness-of-trigonal-pencil and Castelnuovo–Severi inequality are classical; no priority is claimed for these ingredients. A preprint [2] treats a related classification for cyclic-index-two automorphism groups and does not supply an unconditional full-group classification of this characteristic-two subfamily.

## Limitations
The congruence restriction is substantive: for \(M\equiv1\pmod3\), the two types of branch points have the same Kummer exponent residue, so Step 4 cannot distinguish them; some members of the source family indeed have larger automorphism groups. The result does not classify full groups for arbitrary \(k\), arbitrary \(M\), nor automorphisms over a non-algebraically-closed ground field. Independent external audit has not been performed. As with any literature-led result, an unindexed equivalent argument could remain undiscovered.

## References
[1] Marco Timpanella, *Large cyclic automorphism groups and cyclic subgroups of index two in characteristic two* (first public September 28, 2026), arXiv:2609.34709v1, especially Theorem 1.2, Example 4.7, Proposition 6.6, Remark 6.7. https://arxiv.org/abs/2609.34709

[2] Arianna Dionigi, Massimo Giulietti and Marco Timpanella, *Curves with a large automorphism group admitting a cyclic subgroup of index 2* (2026), arXiv:2607.15983. https://arxiv.org/abs/2607.15983
