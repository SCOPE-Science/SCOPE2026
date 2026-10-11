# Ramanujan resolution of representation-degree layers in finite Heisenberg groups
## Finding
Let \(H_n=H(\mathbb Z/n\mathbb Z)\), \(n\ge2\), be the finite Heisenberg group
\[
H_n=\{(x,y,z):x,y,z\in\mathbb Z/n\mathbb Z\},
\]
with multiplication
\[
(x,y,z)(x',y',z')=(x+x',y+y',z+z'+xy').
\]
Its center is \(Z=\{z_t=(0,0,t):t\in\mathbb Z/n\mathbb Z\}\).

For each divisor \(m\mid n\), let \(\Pi_m\) be the central Fourier projection in the regular representation onto the direct sum of all isotypic components corresponding to irreducible representations of degree exactly \(m\). Define the Ramanujan sum
\[
c_m(t)=\sum_{\substack{1\le a\le m\\(a,m)=1}}e^{2\pi iat/m}.
\]
Then the entire degree decomposition is realized spatially on the center:
\[
\boxed{(\Pi_m f)(g)=\frac1n\sum_{t=0}^{n-1}c_m(t)f(gz_t^{-1}).}
\]
In particular,
\[
\Pi_m\Pi_r=0\quad(m\ne r),\qquad \sum_{m\mid n}\Pi_m=I,
\]
and
\[
\operatorname{rank}\Pi_m=n^2\varphi(m).
\]
The exact endpoint Lebesgue constant of the degree layer is
\[
\boxed{
\|\Pi_m\|_{\ell^1\to\ell^1}
=\|\Pi_m\|_{\ell^\infty\to\ell^\infty}
=2^{\omega(m)}\frac{\varphi(m)}m,
}
\]
where \(\omega(m)\) is the number of distinct prime divisors of \(m\), with \(\omega(1)=0\). The complementary projection also has a closed norm:
\[
\boxed{
\|I-\Pi_m\|_{\ell^1\to\ell^1}
=\|I-\Pi_m\|_{\ell^\infty\to\ell^\infty}
=1+2^{\omega(m)}\frac{\varphi(m)}m-\frac{2\varphi(m)}n.
}
\]
Therefore
\[
\boxed{\|\Pi_m\|=1\quad\Longleftrightarrow\quad m\text{ is a power of }2,}
\]
where \(m=1=2^0\) is included. Thus endpoint contractivity of a representation-degree stratum is controlled purely by the odd-prime support of the degree.

## Assumptions and scope
All \(\ell^p(H_n)\) spaces use normalized counting measure. The operator \(\Pi_m\) is the canonical central spectral projection associated with the union of all irreducible blocks of degree \(m\); it is not a projection onto one chosen irreducible representation. The theorem concerns the three-dimensional finite Heisenberg group over \(\mathbb Z/n\mathbb Z\) for arbitrary composite or prime \(n\), and every divisor \(m\mid n\).

The result uses the standard fact that the irreducible representations of degree \(m\) have central character of exact order \(m\), and conversely that every exact-order \(m\) central character occurs only in degree \(m\). No assertion is made here about higher-dimensional Heisenberg groups, other two-step nilpotent groups, or interior \(\ell^p\) norms.

## Proof
Write \(R_{z_t}f(g)=f(gz_t^{-1})\) for right translation by the central element \(z_t\). For a character \(\psi\) of the cyclic center \(Z\), the orthogonal projection onto the \(\psi\)-eigenspace of the central translations is
\[
E_\psi f(g)=\frac1n\sum_{t=0}^{n-1}\overline{\psi(z_t)}\,f(gz_t^{-1}).
\]
The finite-Heisenberg representation classification gives, for every \(m\mid n\), exactly \((n/m)^2\varphi(m)\) irreducible representations of degree \(m\). Their central characters are precisely the \(\varphi(m)\) characters of \(Z\) having exact order \(m\), each occurring for \((n/m)^2\) inequivalent irreducibles. Hence the direct sum of all degree-\(m\) isotypic components is exactly the sum of the central eigenspaces for exact-order \(m\) characters:
\[
\Pi_m=\sum_{\substack{\psi\in\widehat Z\\\operatorname{ord}(\psi)=m}}E_\psi.
\]
Parameterizing those characters by \(\psi_a(z_t)=e^{2\pi iat/m}\), with \((a,m)=1\), gives
\[
\sum_{\operatorname{ord}(\psi)=m}\overline{\psi(z_t)}=c_m(-t)=c_m(t),
\]
since Ramanujan sums are real and even. This proves the kernel formula. The exact-order character classes partition \(\widehat Z\), so their spectral projectors are pairwise orthogonal and sum to the identity. Each central character eigenspace has dimension \(|H_n|/|Z|=n^2\), which gives
\[
\operatorname{rank}\Pi_m=n^2\varphi(m).
\]

As a convolution operator, \(\Pi_m\) has a signed measure supported on \(Z\), with mass \(c_m(t)/n\) at \(z_t\). A convolution operator on a finite group has the same \(\ell^1\) and \(\ell^\infty\) endpoint norm, equal here to the total variation of this measure; equality is attained by a point mass for \(\ell^1\), and by a phase-sign choice in one row for \(\ell^\infty\). Therefore
\[
\|\Pi_m\|=\frac1n\sum_{t=0}^{n-1}|c_m(t)|
=\frac1m\sum_{u=0}^{m-1}|c_m(u)|.
\]

It remains to evaluate one complete period. For a prime power \(p^a\),
\[
c_{p^a}(u)=
\begin{cases}
0,&p^{a-1}\nmid u,\\
-p^{a-1},&p^{a-1}\mid u\text{ and }p^a\nmid u,\\
\varphi(p^a),&p^a\mid u.
\end{cases}
\]
Consequently
\[
\sum_{u\bmod p^a}|c_{p^a}(u)|=2\varphi(p^a).
\]
Ramanujan sums factor under the Chinese remainder theorem for coprime moduli, and so does the absolute period sum. Thus
\[
\sum_{u\bmod m}|c_m(u)|=2^{\omega(m)}\varphi(m),
\]
which proves the endpoint norm formula.

For the complement, the convolution measure is \(\delta_e-\mu_m\), where \(\mu_m(z_t)=c_m(t)/n\). Since \(c_m(0)=\varphi(m)\le n\), its total variation is
\[
1-\frac{\varphi(m)}n
+\left(\|\Pi_m\|-\frac{\varphi(m)}n\right)
=1+2^{\omega(m)}\frac{\varphi(m)}m-\frac{2\varphi(m)}n.
\]
Finally,
\[
2^{\omega(m)}\frac{\varphi(m)}m
=\prod_{p\mid m}2\left(1-\frac1p\right).
\]
The factor for \(p=2\) equals \(1\), while every factor for an odd prime is strictly larger than \(1\). This proves the contractivity classification.

## Verification
The standalone `verify.py` uses exact rational arithmetic. For every \(2\le n\le120\) and every divisor \(m\mid n\), it checks the degree-count identity, the Ramanujan-kernel total variation formula, idempotence, pairwise orthogonality between distinct degree layers, the identity resolution, the rank formula, the complementary norm, and the power-of-two contractivity criterion. It terminates with

`VERIFY_OK n=2..120 degree_layers=601 exact_fraction_checks=all`

These finite checks are corroborative. The proof above establishes the statements for every \(n\ge2\).

## Relationship to prior work
Grassberger and Hörmann give an elementary classification of all irreducible representations of the finite Heisenberg group, including the dependence of representation degree on the central character. Their result supplies the representation-theoretic input but does not aggregate equal-degree blocks into a central Fourier projection or evaluate endpoint projection norms.

Bump, Diaconis, Hicks, Miclo and Widom later give a self-contained Fourier-analysis treatment of \(H_n\). Their Section 3.2 states that for every divisor \(m\mid n\) there are \((n/m)^2\varphi(m)\) irreducibles of degree \(m\), and displays their characters. Their paper studies random-walk Fourier matrices and does not state the Ramanujan degree-layer resolution or its endpoint Lebesgue constants.

Vaidyanathan studies Ramanujan subspaces for cyclic signal processing. That work makes the cyclic exact-period subspace generated by \(c_m\) a natural object, but the inspected public abstract does not address nonabelian Heisenberg representation-degree strata. The present result identifies those nonabelian degree strata exactly with central Ramanujan projectors and then evaluates their endpoint norms.

Greenleaf's norm-one idempotent-measure theorem is broader for the qualitative norm-one question: every norm-one idempotent measure on a locally compact group is a character-weighted Haar measure on a compact subgroup. Accordingly, no novelty is claimed for a general characterization of norm-one idempotents. Here the quantitative statement is the full degree-by-degree formula, including all noncontractive layers and the exact arithmetic criterion for when contractivity occurs.

## Limitations
The nonabelian-to-Ramanujan identification relies on the special representation theory of the three-dimensional finite Heisenberg group. It does not automatically extend to general two-step nilpotent groups. The endpoint norm of the cyclic Ramanujan projector is elementary once the kernel is identified, so a residual originality risk remains that the same absolute-sum formula or the power-of-two criterion appears in older number-theoretic or signal-processing literature under a different normalization. The inspected 2014 Ramanujan-subspace material was metadata and abstract rather than a full-text inspection; this risk is explicitly retained.

## References
1. J. Grassberger and G. Hörmann, “A note on representations of the finite Heisenberg group and sums of greatest common divisors,” *Discrete Mathematics & Theoretical Computer Science* 4 (2001), 91–100, DOI 10.46298/dmtcs.284.
2. D. Bump, P. Diaconis, A. Hicks, L. Miclo and H. Widom, “An Exercise(?) in Fourier Analysis on the Heisenberg Group,” *Annales de la Faculté des Sciences de Toulouse* 26 (2017), 263–288, DOI 10.5802/afst.1533.
3. P. P. Vaidyanathan, “Ramanujan Sums in the Context of Signal Processing—Part I: Fundamentals,” *IEEE Transactions on Signal Processing* 62 (2014), 4145–4157, DOI 10.1109/TSP.2014.2331617.
4. F. P. Greenleaf, “Norm decreasing homomorphisms of group algebras,” *Pacific Journal of Mathematics* 15 (1965), 1187–1219.
5. S. Thangavelu, “An analogue of Hardy's theorem for the Heisenberg group,” *Colloquium Mathematicum* 87 (2001), 137–145, DOI 10.4064/cm87-1-9; primary MSC 43A30.
