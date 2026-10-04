# Fourier-zero rigidity for unimodular three-point signals on cyclic groups
## Finding
Let \(N\ge 3\) and let \(S=\{x_0,x_1,x_2\}\subset \mathbb Z_N\) consist of three distinct points. Define
\[
g=\gcd(N,x_1-x_0,x_2-x_0),\qquad n=N/g,
\]
and let \(S_*=(S-x_0)/g\subset\mathbb Z_n\). Consider functions \(f:\mathbb Z_N\to\mathbb C\) with support exactly \(S\) whose three nonzero values have one common magnitude.

If \(3\mid n\) and the three elements of \(S_*\) form a complete residue system modulo \(3\), then the number of zeros of \(\widehat f\) is exactly either \(0\) or \(2g\), and both possibilities occur. In every other case the number of zeros is exactly either \(0\) or \(g\), and again both possibilities occur. Hence the attainable Fourier-support sizes are
\[
\{N,N-2g\}
\]
in the first case and
\[
\{N,N-g\}
\]
in the second.

For a prime \(p>3\), necessarily \(g=1\) and \(3\nmid p\). Thus an equal-magnitude three-sparse signal on \(\mathbb Z_p\) has at most one Fourier zero, and one zero is attainable.

## Assumptions and scope
The Fourier transform is evaluated on all characters of \(\mathbb Z_N\); its normalization is irrelevant for zero sets. Coefficient magnitudes must be equal and nonzero, but their phases are arbitrary. The theorem concerns exactly three support points and exact Fourier zeros, not approximate cancellation or norm minimization.

After translation and multiplication by a nonzero scalar, write the support as \(\{0,a,b\}\) and the Fourier samples as
\[
1+u\omega^{ak}+v\omega^{bk},\qquad |u|=|v|=1,
\]
where \(\omega=e^{2\pi i/N}\).

## Proof
Let \(\rho=e^{2\pi i/3}\). Three unit complex numbers with one equal to \(1\) sum to zero if and only if the other two are \(\rho\) and \(\rho^2\), in either order. Therefore a Fourier sample vanishes exactly when
\[
(u\omega^{ak},v\omega^{bk})=(\rho,\rho^2)
\]
or
\[
(u\omega^{ak},v\omega^{bk})=(\rho^2,\rho).
\]

Consider the homomorphism
\[
\Phi:\mathbb Z_N\to\mathbb T^2,\qquad \Phi(k)=(\omega^{ak},\omega^{bk}).
\]
Its kernel has cardinality \(g=\gcd(N,a,b)\). Consequently every nonempty fiber has exactly \(g\) elements. The two target orientations differ by multiplication by \((\rho,\rho^2)\). Thus, once one orientation occurs, the second occurs exactly when \((\rho,\rho^2)\in\operatorname{im}\Phi\). It follows immediately that every nonempty Fourier zero set has size \(g\) or \(2g\), with the latter possible exactly when this ratio lies in the image.

Put \(n=N/g\), \(\alpha=a/g\), and \(\beta=b/g\), so \(\gcd(n,\alpha,\beta)=1\). The ratio condition is equivalent to the existence of \(d\in\mathbb Z_n\) satisfying
\[
\alpha d\equiv n/3\pmod n,\qquad \beta d\equiv 2n/3\pmod n.
\]
It is therefore impossible unless \(3\mid n\). Write \(n=3^s m\) with \(3\nmid m\). The two congruences modulo \(m\), together with \(\gcd(m,\alpha,\beta)=1\), force \(m\mid d\). After writing \(d=m\eta\) and dividing by \(m\), the congruences modulo \(3^s\) are
\[
\alpha\eta\equiv 3^{s-1}\pmod{3^s},\qquad
\beta\eta\equiv 2\cdot3^{s-1}\pmod{3^s}.
\]
At least one of \(\alpha,\beta\) is nonzero modulo \(3\), so these force \(\eta=3^{s-1}t\) with
\[
\alpha t\equiv1\pmod3,\qquad \beta t\equiv2\pmod3.
\]
This is possible exactly when \(\{0,\alpha,\beta\}\) is a complete residue system modulo \(3\). Conversely, under that condition choose the appropriate nonzero \(t\pmod3\) and take \(d=m3^{s-1}t\); the displayed congruences hold. This proves the arithmetic dichotomy.

To realize a nonempty zero set, choose any character index \(k_0\) and set
\[
u=\rho\omega^{-ak_0},\qquad v=\rho^2\omega^{-bk_0}.
\]
Then \(k_0\) is a zero, and the preceding argument gives exactly \(g\) or \(2g\) zeros as dictated by the arithmetic condition. A zero-free phase choice also exists: for each of the finitely many character indices, cancellation permits only the two equilateral orientation pairs, so only finitely many points of the phase torus \(\mathbb T^2\) are excluded. This completes the classification.

## Verification
A standalone exact-integer checker exhausts all normalized supports \(\{0,a,b\}\) for \(3\le N\le180\). It independently compares the residue criterion with direct image membership, verifies the kernel size, and counts the zeros produced by the explicit phase construction using exact modular arithmetic. The replay result is

`VERIFY_OK triples=955860 paired=76776 single=879084 primes_gt3=39 N_max=180`.

The computation is corroborative; the theorem for all \(N\) follows from the proof above.

## Relationship to prior work
Tao's sharp uncertainty principle for prime cyclic groups implies that an unrestricted three-term polynomial on \(\mathbb Z_p\) can have at most two zeros on the \(p\)-th roots of unity. The present phase-only subclass is more rigid: for every prime \(p>3\), equal magnitudes permit at most one zero. Tao's theorem does not impose equal coefficient magnitudes and therefore does not imply this strengthening.

Delvaux and Van Barel recast finite Fourier uncertainty through rank-deficient submatrices and arbitrary null vectors. That framework controls when some coefficient vector can vanish on a specified row set, but it does not impose unimodular coordinates on the null vector. The equal-magnitude classification here is therefore a different constraint rather than a corollary of rank deficiency alone.

Gilbert and Rzeszotnik study norm extremals and biunimodular functions for Fourier transforms on finite Abelian groups. Their objective is global norm behavior rather than exact zeros of a three-sparse equal-magnitude signal.

## Limitations
The theorem is specific to exactly three support points. It does not classify four or more equal-magnitude coefficients, approximate zeros, stability under perturbations, or noncyclic finite Abelian groups. The literature comparison leaves a residual possibility that the elementary phase-rigidity statement appears under different terminology in older sequence-design or coding literature.

## References
1. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286v1, first submitted 2003-08-29; primary 1991 MSC 42A99.
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Fourier matrices*, Report TW470, 2006-09-28; primary AMS classification 42A99.
3. J. E. Gilbert and M. Rzeszotnik, *The norm of the Fourier transform on finite abelian groups*, Ann. Inst. Fourier 60 (2010), DOI 10.5802/aif.2556.
