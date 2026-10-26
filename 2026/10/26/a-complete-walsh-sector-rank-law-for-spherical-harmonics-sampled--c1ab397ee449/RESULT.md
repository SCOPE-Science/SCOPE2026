# A complete Walsh-sector rank law for spherical harmonics sampled at hypercube vertices

## Finding

Let \(d\ge3\) be an integer and let \(X_d=\{d^{-1/2}(\varepsilon_1,\ldots,\varepsilon_d):\varepsilon_i\in\{-1,1\}\}\subset S^{d-1}\). Denote by \(\mathcal H_\ell\) the complex space of homogeneous harmonic polynomials of exactly degree \(\ell\ge0\), restricted to \(S^{d-1}\). For \(S\subseteq\{1,\ldots,d\}\), let \(\chi_S(\varepsilon)=\prod_{i\in S}\varepsilon_i\) be the corresponding Walsh character.

The image of the evaluation map \(E_\ell:\mathcal H_\ell\longrightarrow\mathbb C^{X_d}\) is **exactly** the span of the Walsh characters satisfying
\[
|S|\le\ell,\qquad |S|\equiv\ell\pmod 2,
\]
with precisely two additional exclusions: the constant character at \(\ell=2\), and the full-product character \(\chi_{\{1,\ldots,d\}}\) at \(\ell=d+2\). There are no other exceptional degrees or Walsh sectors, in any dimension \(d\ge3\).

Consequently, writing \(r_{d,\ell}=\operatorname{rank}E_\ell\),
\[
\boxed{\displaystyle r_{d,\ell}=\sum_{\substack{0\le s\le\min(d,\ell)\\s\equiv\ell\ (\mathrm{mod}\ 2)}}\binom ds-\mathbf 1_{\{\ell=2\}}-\mathbf 1_{\{\ell=d+2\}}.}
\]
The entire parity-compatible sample space has dimension \(2^{d-1}\). Every degree \(\ell\ge d+3\) reaches this dimension, whereas degree \(d+2\) has rank exactly \(2^{d-1}-1\). Degrees \(d\) and \(d+1\) are already parity-surjective before this isolated rank collapse. For \(d\ge4\), degree \(d-1\) is parity-surjective as well; in dimension three, degree two is exceptional instead. Thus \(d+3\) is the sharp eventual parity-surjectivity threshold.

In addition, the full sampling Gram spectrum is explicit: every Walsh sector of size \(s\) has the eigenvalue in the Verification section, repeated \(\binom ds\) times. The theorem decides exactly which of these eigenvalues vanish, without requiring an asymptotic approximation or a numerical rank threshold.

## Assumptions and scope

Coordinates are real at the sample points, but the harmonic polynomial spaces and sample vectors may be complex. A harmonic polynomial is a polynomial \(H\) satisfying \(\Delta H=0\), and *exact degree* excludes sums of different homogeneous degrees. The sphere carries normalized rotation-invariant surface measure. We do not identify the evaluation ranges of a low-pass sum \(\bigoplus_{j\le\ell}\mathcal H_j\) with those of a single exact degree. All rank statements concern the \(2^d\) distinct full-cube vertices, not an antipodal half-cube. The parity-compatible sector consists of functions \(F(-x)=(-1)^\ell F(x)\).

## Proof

**1. Walsh symmetries and the moment criterion.** The coordinate sign-change group acts on \(\mathcal H_\ell\) and on functions on \(X_d\), and evaluation intertwines those actions. The latter representation is a multiplicity-one sum of all Walsh characters. Thus each character is either wholly present or absent from the evaluation range. Homogeneity gives the parity restriction. Expansion of a degree-\(\ell\) polynomial on sign vectors shows that a character of size greater than \(\ell\) cannot occur.

Fix \(S\) of size \(s\). In unscaled coordinates introduce the homogeneous polynomial
\[
M_{\ell,S}(y)=2^{-d}\sum_{\varepsilon\in\{\pm1\}^d}\chi_S(\varepsilon)(\varepsilon\cdot y)^\ell.
\]
With the Fischer pairing \(\langle P,H\rangle_F=P(\partial)\overline H(y)|_{y=0}\) (using conjugation on coefficients in the usual Hermitian version), the weighted evaluation functional on \(\mathcal H_\ell\) is, up to a fixed nonzero scaling factor, pairing with \(M_{\ell,S}\). The Fischer decomposition of homogeneous polynomials says \(\mathcal P_\ell=\mathcal H_\ell\oplus |y|^2\mathcal P_{\ell-2}\), orthogonally for the Fischer pairing. Hence \(\chi_S\) is absent exactly when \(M_{\ell,S}\) is divisible by \(Q(y)=y_1^2+\cdots+y_d^2\).

If \(\ell=s+2k\) with \(k\ge0\), independence of the signs gives the exact generating identity
\[
M_{\ell,S}(y)=\ell!\left(\prod_{i\in S}y_i\right) P_{k,S}(y_1^2,\ldots,y_d^2),
\]
where the degree-\(k\) polynomial \(P_{k,S}\) is defined by
\[
P_{k,S}(z)=[t^{2k}]\prod_{i\in S}\frac{\sinh(t\sqrt{z_i})}{t\sqrt{z_i}}\prod_{j\notin S}\cosh(t\sqrt{z_j}).
\]
The entire even power series defines the expression also at zero arguments, without any square-root choices. For \(d\ge3\), \(Q(y)\) is irreducible over \(\mathbb C\), hence coprime to \(\prod_{i\in S}y_i\). It suffices to show that \(P_{k,S}(z)\) is not identically zero on the hyperplane \(z_1+\cdots+z_d=0\). Indeed, if \(Q\) divided the moment polynomial, coprimeness would force \(Q\) to divide \(P_{k,S}(y_1^2,\ldots,y_d^2)\); the latter would vanish at every complex vector with \(Q(y)=0\). But every complex \(z\) satisfying \(\sum_i z_i=0\) has coordinatewise square roots \(y_i\) with \(Q(y)=0\). Thus a nonzero \(P_{k,S}(z)\) at even one such \(z\) rules out divisibility, regardless of zeros of the prefactor \(\prod_{i\in S}y_i\) at that test point.

**2. Mixed-size characters.** Suppose \(0<s<d\). Choose one coordinate in \(S\) with \(z=1\) and one coordinate outside \(S\) with \(z=-1\), setting all others to zero. Then the restriction to the hyperplane is
\[
P_{k,S}(z)=[t^{2k}]\frac{\sinh t}{t}\cos t
=\frac{\operatorname{Re}(1+i)^{2k+1}}{(2k+1)!}.
\]
The real part is \(\pm2^k\), never zero. This proves the presence of every mixed Walsh sector allowed by degree and parity.

**3. The constant character.** For \(s=0\), \(P_{0,\varnothing}=1\), while \(P_{1,\varnothing}(z)=\tfrac12\sum_i z_i\), so the degree-two constant character is missing. At \(z=(1,-1,0,\ldots,0)\),
\[
P_{k,\varnothing}(z)=[t^{2k}]\cosh t\cos t
=\frac{2^k\cos(k\pi/2)}{(2k)!},
\]
which is nonzero for even \(k\). For odd \(k\ge3\), work instead on the same null hyperplane with \(z(v)=(1,-1-v,v,0,\ldots,0)\). Elementary differentiation of the generating functions gives
\[
\left.\frac{d}{dv}P_{k,\varnothing}(z(v))\right|_{v=0}
=\frac{(-1)^{(k-1)/2}2^{k-2}(2k-2)}{(2k-1)!}\ne0.
\]
The derivative vanishes at \(k=1\), consistently with the exact exceptional polynomial above. All remaining constant sectors occur.

**4. The full-product character.** For \(s=d\), \(P_{0,[d]}=1\) but \(P_{1,[d]}(z)=\tfrac16\sum_i z_i\); hence degree \(d+2\) lacks this one character. At \(z=(1,-1,0,\ldots,0)\),
\[
P_{k,[d]}(z)=[t^{2k}]\frac{\sinh t\sin t}{t^2}
=\frac{2^{k+1}\sin((k+1)\pi/2)}{(2k+2)!},
\]
which is nonzero for even \(k\). For odd \(k\ge3\), the three-coordinate null-hyperplane path \(z(v)=(1,-1-v,v,0,\ldots,0)\) is available because \(d\ge3\). Direct differentiation gives
\[
\left.\frac{d}{dv}P_{k,[d]}(z(v))\right|_{v=0}
=\frac{(-1)^{(k-1)/2}2^k(k-1)}{3(2k+1)(2k)!}\ne0.
\]
Again the degree-two increment \(k=1\) is precisely the exception. This exhausts the possible Walsh sectors.

**5. Rank and the sharp threshold.** Walsh characters are linearly independent and their weight-\(s\) multiplicity is \(\binom ds\). Summing the present sectors proves the rank formula. For \(\ell\ge d\), all characters of the matching parity satisfy the degree bound; there are exactly \(2^{d-1}\), except for the one missing at \(\ell=d+2\). This yields all threshold assertions, including sharpness of the eventual threshold \(d+3\). No finite computation is used in this step.

## Verification

For \(d\ge3\), put \(\lambda=(d-2)/2\) and \(h_{d,\ell}=\dim\mathcal H_\ell\). The sphere-normalized harmonic reproducing polynomial is \(q_{d,\ell}(u)=h_{d,\ell} C_\ell^\lambda(u)/C_\ell^\lambda(1)\), with the standard Gegenbauer convention. With normalized sample evaluation \(2^{-d/2} E_\ell\), the Gram eigenvalue of every Walsh character of size \(s\) is
\[
\Lambda_{d,\ell,s}=2^{-d}\sum_{a=0}^s\sum_{b=0}^{d-s}(-1)^a\binom sa\binom{d-s}b\,q_{d,\ell}\!\left(1-\frac{2(a+b)}d\right).
\]
The proof shows that \(\Lambda_{d,\ell,s}>0\) exactly for the included sectors, and it vanishes for every excluded sector. Positivity is also independently guaranteed by the Gram construction.

The standalone checker `checker.py` evaluates this formula entirely with rational arithmetic using the Gegenbauer three-term recurrence. It tests all sectors for each \(3\le d\le12\) and \(0\le\ell\le d+12\) (1825 eigenvalues), along with the null-hyperplane derivative formulas for odd \(k\le11\). These are finite consistency checks, not substitutes for the all-dimensional argument above. Run `python checker.py` with Python 3.10 or later; the only dependency is the standard library. Its saved output is `checker_output.txt`.

## Relationship to prior work

Bannai, Okuda and Tagami develop the theory of spherical designs of a fixed harmonic index, Gegenbauer reproducing kernels and Fisher inequalities; their 2013 original preprint does not present the exact-degree evaluation range on all vertices of a Euclidean hypercube, nor the two missing Walsh sectors. Zhu, Bannai, Bannai, Kim and Yu extend the harmonic-index design theory, principally establishing bounds and classification results for tight designs; their 2015 preprint does not state this rank law. Hyun treats discrete harmonic distributions and equitable partitions of a Hamming hypercube rather than restrictions of Euclidean homogeneous harmonic polynomials to the embedded vertex set. These discrete harmonics are not being identified with the spherical harmonics here. Classical Walsh/Krawtchouk diagonalization and Fischer decomposition supply background ingredients, and the displayed Gram formula is a standard consequence of those ingredients; the claim of interest is the exact **all-degree nonvanishing classification** and its isolated degree-\(d+2\) rank defect. See the references and the distinct checks recorded in `AUDIT.json`.

## Limitations

The theorem is for the **complete uniform vertex set** of a regular hypercube in \(\mathbb R^d\), with \(d\ge3\). It does not classify arbitrary subsets, nonuniform vertex weights, noisy reconstruction, or the condition number of the positive eigenvalue sectors. The result concerns exact-degree spaces, not cumulative harmonic bands. The inspected literature comparisons are not a proof of global publication novelty; historical discrete/association-scheme sources may contain an equivalent result not identified here. The full text of one related discrete-Hamming article was inaccessible, and it is treated as an unresolved literature-access risk rather than as evidence of noncoverage.

## References

1. E. Bannai, T. Okuda and M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101v1, first public preprint 2013-08-23, https://arxiv.org/pdf/1308.5101.
2. Y. Zhu, E. Bannai, E. Bannai, K.-T. Kim and W.-H. Yu, *More on spherical designs of harmonic index t*, arXiv:1507.05373, first preprint 2015-07-20, https://arxiv.org/pdf/1507.05373.
3. J. Y. Hyun, *Harmonic Distributions for Equitable Partitions of a Hypercube*, Journal of Combinatorial Designs 23 (2015), 289–304, first online 2014-09-30, https://doi.org/10.1002/jcd.21412.
