# Common prime divisors of all Veronese coisotropic degrees

## Finding
Let \(V_{n,e}=v_e(\mathbb P^n_{\mathbb C})\), with \(n\ge1\) and \(e\ge2\). In the standard polar-degree convention used by Kohn, \(\delta_0=\deg V_{n,e}\) and the degrees of the coisotropic hypersurfaces are the polar degrees in the same order. Then
\[
\delta_i=\binom{n+1}{i}e^{\,n-i}(e-1)^i,\qquad 0\le i\le n.
\]
Consequently,
\[
\gcd(\delta_0,\ldots,\delta_n)=\prod_{p\mid e}p^{\nu_p(n+1)}.
\]
Equivalently, a prime \(p\) divides every Veronese coisotropic degree exactly when \(p\mid e\) and \(p\mid n+1\), and then the exact common \(p\)-adic exponent is \(\nu_p(n+1)\). In particular,
\[
\gcd(\delta_0,\ldots,\delta_n)=1\iff \gcd(e,n+1)=1,
\]
and for the quadratic Veronese the gcd is \(2^{\nu_2(n+1)}\).

## Assumptions and scope
The ground field is \(\mathbb C\), and the embedding is the standard Veronese embedding
\[
v_e:\mathbb P^n\hookrightarrow\mathbb P^{\binom{n+e}{e}-1}.
\]
The indexing is the standard projective polar-degree convention in which \(\delta_0\) is the degree of the variety and the last polar degree is the degree of the dual hypersurface. Thus
\[
\delta_0=e^n,\qquad \delta_n=(n+1)(e-1)^n.
\]
The theorem concerns the gcd of the complete polar vector; reversing the order of the vector, as some conormal-multidegree conventions do, does not change the gcd.

## Proof
Set \(N=n+1\). For the gcd it is convenient to reverse the polar vector. Put
\[
a_k=\delta_{N-k}=\binom Nk e^{k-1}(e-1)^{N-k},\qquad 1\le k\le N.
\]
Fix a prime \(p\). If \(p\nmid e\), the endpoint \(a_N=e^{N-1}\) has \(p\)-adic valuation zero, so \(p\) does not divide the gcd.

Now suppose \(p\mid e\). Write \(a=\nu_p(N)\) and \(b=\nu_p(e)\ge1\). Since \(p\nmid e-1\),
\[
\nu_p(a_k)=\nu_p\binom Nk+(k-1)b.
\]
From
\[
\binom Nk=\frac Nk\binom{N-1}{k-1}
\]
and integrality of the second factor,
\[
\nu_p\binom Nk\ge a-\nu_p(k).
\]
Also \(\nu_p(k)\le k-1\le(k-1)b\). Hence \(\nu_p(a_k)\ge a\) for every \(k\). At \(k=1\),
\[
a_1=N(e-1)^{N-1},
\]
so \(\nu_p(a_1)=a\). Therefore the minimum valuation over the complete polar vector is exactly \(\nu_p(N)\) for every prime dividing \(e\), proving the gcd formula.

For completeness, the standard smooth polar-class formula in this indexing is
\[
\delta_i=\sum_{j=0}^{i}(-1)^j\binom{n-j+1}{n-i+1}\int_{\mathbb P^n}c_j(T\mathbb P^n)H^{n-j}.
\]
With \(c_j(T\mathbb P^n)=\binom{n+1}{j}h^j\) and \(H=eh\), this becomes
\[
\delta_i=\sum_{j=0}^{i}(-1)^j\binom{n-j+1}{n-i+1}\binom{n+1}{j}e^{n-j}
=\binom{n+1}{i}e^{n-i}(e-1)^i.
\]

## Verification
The accompanying exact checker recomputes the polar vector both from the closed formula and from the Chern-class sum, verifies their equality on a finite regression range, checks the gcd identity on a larger finite range, and checks the identity
\[
\sum_{i=0}^{n}\delta_i=\frac{(2e-1)^{n+1}-(e-1)^{n+1}}{e}.
\]
These computations are regression checks only; the uniform theorem is proved by the valuation argument above.

## Relationship to prior work
Kohn proves that the degrees of the coisotropic hypersurfaces are the polar degrees and uses the convention \(\delta_0=\deg X\). Explicit polar-degree formulas for Segre--Veronese varieties are available in later work, and the formula above is the ordinary-Veronese specialization (possibly displayed in the reverse conormal-multidegree order in other conventions).

The contribution here is the exact arithmetic invariant of the complete polar vector: its gcd is precisely the part of \(n+1\) supported on primes dividing the embedding degree \(e\). The inspected sources give the geometric interpretation and explicit polar data but do not state this common-divisor classification.

## Limitations
The theorem concerns the gcd of the complete polar vector, not a proper subcollection. The gcd formula is a short consequence of the explicit vector, so an unindexed older source may contain the same arithmetic observation. Indexing conventions for conormal multidegrees vary; the formulas above use \(\delta_0=\deg V_{n,e}\), while reversing all entries leaves the gcd unchanged.

## References
1. Kathlén Kohn, “Coisotropic Hypersurfaces in Grassmannians,” arXiv:1607.05932; *Journal of Symbolic Computation* 103 (2021), 157–177, DOI: 10.1016/j.jsc.2019.12.002.
2. Türkü Özlüm Çelik, Asgar Jamneshan, Guido Montúfar, Bernd Sturmfels, and Lorenzo Venturello, “Wasserstein distance to independence models,” *Journal of Symbolic Computation* 104 (2021), 855–873, DOI: 10.1016/j.jsc.2020.10.005.
