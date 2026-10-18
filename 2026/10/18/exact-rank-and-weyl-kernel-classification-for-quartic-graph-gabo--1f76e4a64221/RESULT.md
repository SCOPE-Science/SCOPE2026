# Exact rank and Weyl-kernel classification for quartic-graph Gabor tomography

## Finding

Let \(p\ge5\) be prime, \(G=\mathbb F_p^2\), \(C=\{(t,t^4):t\in\mathbb F_p\}\), and \(g=p^{-1/2}\mathbf1_C\in\ell^2(G)\). Define \(W_{h,\eta}=M_\eta T_h\), with \((T_h f)(x)=f(x-h)\) and \((M_\eta f)(x)=\exp(2\pi i\eta\cdot x/p)f(x)\). For all \((h,\eta)\in G\times G\), set \(\Pi_{h,\eta}=|W_{h,\eta}g\rangle\langle W_{h,\eta}g|\) and define the complex-linear measurement map

\[
\mathcal L_g(X)=\bigl(\operatorname{tr}(X\Pi_{h,\eta})\bigr)_{h,\eta\in G},\qquad X\in\operatorname{End}_{\mathbb C}(\ell^2(G)).
\]

With \(\epsilon_p=\chi_p(-3)\in\{-1,1\}\) and \(\delta_p=\mathbf1_{\{p=7\}}\), its **exact complex rank** is

\[
\boxed{\operatorname{rank}\mathcal L_g
 =p^2\left(1+\frac{(p-1)(2p+\epsilon_p)}{3}\right)
 -(p-1)(1+2\delta_p).}
\]

The nullity is \(p^4-\operatorname{rank}\mathcal L_g\). Moreover its kernel is the complex span of precisely the Weyl operators \(W_{(a,b),(m,n)}\) whose labels satisfy one of the mutually disjoint conditions:

1. \(a=0\) and \(b\ne0\), with arbitrary \((m,n)\).
2. \(a\ne0\) and \(2ba^{-4}\notin\{u^3+u:u\in\mathbb F_p\}\), with arbitrary \((m,n)\).
3. \((a,b)=(0,0)\), \(n=0\), and \(m\ne0\).
4. \(p=7\), \((a,b)=(0,0)\), \(n\ne0\), and \(m/n\in\{3,4\}\).

Thus the exceptional prime \(7\) loses another \(2(p-1)\) Weyl directions beyond the generic formula; the full origin-block loss is \(3(p-1)\) there instead of \(p-1\). The result concerns **linear operator tomography**, not uniqueness or nonuniqueness of nonlinear pure-state phase retrieval.

## Assumptions and scope

All operations in the defining curve, labels, and ratio tests occur in the prime field \(\mathbb F_p\). Inversion \(a^{-4}\) is used only when \(a\ne0\). Fourier characters are \(e_p(s)=\exp(2\pi i s/p)\). The Hilbert space has complex dimension \(p^2\), so the operator space has dimension \(p^4\). The measurement system contains the **complete** set of \(p^4\) time-frequency shifts of one unit window, with no claim of minimality. No weighted or perturbed curve is asserted.

## Proof

**1. Operator-span reduction.** The \(p^4\) Weyl operators form an orthogonal basis of the complex operator space, since \(\operatorname{tr}(W_u^*W_v)=p^2\mathbf1_{u=v}\). Weyl conjugation acts diagonally on this basis by distinct phase-space characters. Expanding \(|g\rangle\langle g|\) in this basis and Fourier transforming the conjugated projectors shows that the span of the projectors is the span of those Weyl operators with nonzero expansion coefficients. These coefficients are, up to conjugation and nonzero phases, the ambiguity function

\[
A_g((a,b),(m,n))=\sum_{x\in G}\overline{g(x)}g(x+(a,b))e_p(-mx_1-nx_2).
\]

Consequently \(\operatorname{rank}\mathcal L_g\) equals the number of nonzero ambiguity coefficients, while the complex kernel consists exactly of the Weyl directions with zero ambiguity coefficients. This also supplies an independent linear-algebra proof of the kernel statement.

**2. Intersection and root-of-unity rigidity.** The ambiguity coefficient equals

\[
 p^{-1}\sum_{t:\ (t+a)^4-t^4=b}e_p(-mt-nt^4).
\]

If \(a=0\), intersections are empty when \(b\ne0\), and all \(p\) points occur when \(b=0\). For \(a\ne0\), put \(w=(2t+a)/a\); the identity

\[
 (t+a)^4-t^4=\frac{a^4}{2}(w^3+w)
\]

shows that the intersection size is \(0,1,2\), or \(3\). For a prime \(p\), a sum of strictly between \(0\) and \(p\) complex \(p\)-th roots of unity, each with coefficient \(1\), cannot vanish: the polynomial of residue counts would have to be a scalar multiple of \(1+T+\cdots+T^{p-1}\), its cyclotomic minimal polynomial. Thus every modulation is nonzero at a nonempty intersection for \(a\ne0\). There are \((p-1)V_p\) such translation labels, where \(V_p=|\{w^3+w:w\in\mathbb F_p\}|\).

**3. Exact cubic image.** Write \(\epsilon=\chi_p(-3)\). The number of ordered off-diagonal pairs with \(u^3+u=v^3+v\) is the number of pairs \(u\ne v\) satisfying \(u^2+uv+v^2=-1\). Completing the square, or using the norm-one conic, gives \(p-\epsilon\) solutions to the quadratic equation before removing the \(1+\epsilon\) diagonal solutions. Thus the off-diagonal count is \(p-1-2\epsilon\). A cubic fiber has exactly two distinct roots precisely when it has a repeated root, which requires \(3u^2+1=0\); when \(\epsilon=1\) there are two critical points with distinct image values, and otherwise none. Consequently the populations of fibers of sizes \(2\) and \(3\) are respectively \(1+\epsilon\) and \((p-3-4\epsilon)/6\), because off-diagonal ordered pairs contribute \(2\) or \(6\). Counting the \(p\) inputs then gives \((p-1)/2\) fibers of size \(1\), and hence

\[
\boxed{V_p=\frac{2p+\epsilon}{3}.}
\]

(The empty-fiber population is \((p-\epsilon)/3\).) This argument includes \(p=5\) and \(p=7\).

**4. Complete-translation Fourier zeros.** At \((a,b)=(0,0)\), the ambiguity coefficient is \(p^{-1}\sum_t e_p(-mt-nt^4)\). By the same cyclotomic-minimal-polynomial argument, it vanishes if and only if \(t\mapsto mt+nt^4\) permutes \(\mathbb F_p\). When \(n=0\), precisely \(m\ne0\) gives such a permutation, yielding \(p-1\) zeros. When \(n\ne0\), this condition is equivalent to \(t\mapsto t^4+ct\) being a permutation, where \(c=m/n\).

For \(p=5\) or \(p\ge11\), no \(c\) works. Indeed, \(c=0\) fails since \(t^4\) cannot permute an odd prime field. For \(c\ne0\), let \(N=p-1\). Choose an integer \(k\) satisfying \(N/4\le k<N/2\) and \(k\equiv N\pmod3\). Such \(k\) exists for \(N=4\) and \(N=10\), and for every even \(N\ge12\), where the interval contains at least three consecutive integers. Put \(j=(N-k)/3\), so \(0\le j\le k<p\). In the binomial expansion of \((t^4+ct)^k\), exactly one exponent \(k+3j\) is a positive multiple of \(N\), since \(k+3j=N\) and \(4k<2N\). It follows that

\[
 \sum_{t\in\mathbb F_p}(t^4+ct)^k=-\binom{k}{j}c^{k-j}\ne0\pmod p.
\]

A permutation would give the vanishing sum \(\sum_t t^k=0\) because \(1\le k\le p-2\), a contradiction. At \(p=7\), direct evaluation of the seven residue values for each \(c\in\mathbb F_7\) shows that exactly \(c=3,4\) permute; this finite step is also exhaustively checked in the standalone verifier. Thus there are \((p-1)(1+2\delta_p)\) origin-translation zeros.

**5. Assembly.** Every one of the \((p-1)V_p\) nonempty nonzero-translation intersections contributes all \(p^2\) nonzero modulations. The zero-translation case contributes \(p^2-(p-1)(1+2\delta_p)\). Summing and inserting the value of \(V_p\) yields the stated rank. The four zero patterns in the finding are precisely the omitted labels, giving the exact kernel.

## Verification

Run `python verify.py` with Python \(\ge3.8\). The verifier uses exact modular arithmetic and the prime cyclotomic zero test, not floating-point approximations. It independently constructs all curve-translation intersections and tests **every** translation-modulation label at primes \(5,7,11,13,17,19,23,29,31\). The recorded output is `verification_output.json`; all nine test primes pass, including the exceptional \(p=7\) and all complete rank/nullity counts. These finite checks corroborate the all-prime proof but do not replace it. The critical number-theoretic steps are proven above.

## Relationship to prior work

Finite-prime-field Gabor windows, especially graph supports, are studied by Iosevich, Kolountzakis, Lyubarskii, Mayeli and Pakianathan (2017). Their Gabor **orthonormal-basis** characterization does not supply ranks of the complete lifted projector system of the quartic graph. Alaifari and Wellershoff (2019) analyze discrete Gabor phase-retrieval stability and ambiguity-function reconstruction, not this arithmetic operator-space rank. The classical classification of small-degree permutation polynomials and binomial permutation criteria supply background for the exceptional \(p=7\) origin block; the new statement combines that phenomenon with the exact cubic translated-intersection image and the full Weyl-kernel count. The displayed rank and all four kernel strata are not claimed as consequences of the cited papers.

## Limitations

The theorem is for prime, not general prime-power, fields. It measures complex-linear operator tomography; positivity-restricted or rank-one injectivity, exact least singular value, and the full nonzero singular spectrum are not determined. Prior-work comparison is a best-knowledge mathematical assessment, not a claim of exhaustive bibliography or independent validation. The two- and three-point intersection argument crucially uses \(p>3\); the origin permutation statement uses prime cyclotomic rigidity.

## References

1. A. Iosevich, M. Kolountzakis, Yu. Lyubarskii, A. Mayeli, J. Pakianathan, *On Gabor orthonormal bases over finite prime fields*, arXiv:1712.09120 (first public 2017-12-25), https://arxiv.org/pdf/1712.09120.
2. R. Alaifari, M. Wellershoff, *Stability estimates for phase retrieval from discrete Gabor measurements*, arXiv:1901.05296 (first public 2019-01-12), https://arxiv.org/pdf/1901.05296.
3. M. Ayad, K. Belghaba, O. Kihel, *On permutation binomials over finite fields*, Bulletin of the Australian Mathematical Society (2014), DOI:10.1017/S0004972713000208, https://doi.org/10.1017/S0004972713000208.
