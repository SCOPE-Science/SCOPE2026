# Strict left-half-plane roots for every two-block Lah generating polynomial

## Finding
For **every integer** \(n\ge 2\), let \(X\sim\mathrm{Lah}(n,2)\) in the sense of Kabluchko and Marynych and write
\[
P_{n,2}(z)=\mathbb E[z^X].
\]
Then \(z=0\) is a zero of multiplicity exactly two and **every nonzero root** of \(P_{n,2}\) satisfies \(\operatorname{Re}z<0\). Equivalently, \(P_{n,2}(z)/z^2\) is strictly Hurwitz stable; when \(n=2\), it is the constant polynomial \(1\). The origin factor is essential: the unqualified statement that *all* roots have strictly negative real parts cannot hold for these generating polynomials.

## Assumptions and scope
Write \(\left[{n\atop j}\right]\) for the unsigned Stirling number of the first kind and \(\left\{{j\atop2}\right\}\) for the Stirling number of the second kind. For integers \(n\ge2\), define the ordinary Lah number
\[
L(n,2)=\sum_{j=2}^{n}\left[{n\atop j}\right]\left\{{j\atop 2}\right\}=\frac{n!(n-1)}2
\]
and the probability-generating polynomial
\[
P_{n,2}(z)=\frac1{L(n,2)}\sum_{j=2}^{n}\left[{n\atop j}\right]\left\{{j\atop 2}\right\}z^j.
\]
This is the ordinary \(r=0\) Lah law, not a general \(r\)-Lah law or a claim about arbitrary block number \(k\). Complex zeros are counted with multiplicity; the right-half-plane boundary is included in the excluded region for **nonzero** zeros.

## Proof
For \(j\ge2\), the two-block Stirling number is \(\left\{{j\atop2}\right\}=2^{j-1}-1\). The signed-free Stirling generating identity is
\[
R_n(w):=\prod_{h=0}^{n-1}(w+h)=\sum_{j=0}^{n}\left[{n\atop j}\right]w^j.
\]
Consequently the exact normalized representation is
\[
P_{n,2}(z)=\frac{R_n(2z)-2R_n(z)}{n!(n-1)}
=\frac{2z}{n!(n-1)}\left(\prod_{h=1}^{n-1}(2z+h)-\prod_{h=1}^{n-1}(z+h)\right).
\]
For any \(z\ne0\) with \(\operatorname{Re}z\ge0\) and any integer \(h\ge1\), the strict identity
\[
|2z+h|^2-|z+h|^2=3|z|^2+2h\operatorname{Re}z>0
\]
holds. Every factor in the first product therefore has strictly larger absolute value than the corresponding factor in the second. In particular,
\[
\left|\prod_{h=1}^{n-1}(2z+h)\right|>
\left|\prod_{h=1}^{n-1}(z+h)\right|,
\]
so their difference cannot vanish. Thus \(P_{n,2}(z)\ne0\) whenever \(z\ne0\) and \(\operatorname{Re}z\ge0\). Finally the coefficient of \(z^2\) is \(\left[{n\atop2}\right]/L(n,2)>0\), proving the origin has multiplicity exactly two for every \(n\ge2\). This establishes the theorem with no limit or numerical extrapolation.

The root claim is **genuinely non-real** at some degrees. For example, the unnormalized polynomial at \(n=8\) factors exactly as
\[
\sum_{j=2}^8\left[{8\atop j}\right]\left\{{j\atop2}\right\}z^j
=z^2(z+1)(z+2)(z+3)(127z^3+1002z^2+2573z+2178).
\]
The cubic has discriminant \(-307921820\), hence one real zero and a nonreal conjugate pair. All three have strictly negative real parts by the proved theorem; alternatively, the cubic Routh–Hurwitz inequality is \(1002\cdot2573-127\cdot2178=2301540>0\).

## Verification
Run \(`python3 verify.py`\) in the directory containing the attached verifier; it needs only the Python standard library. It checks the exact polynomial identity, origin multiplicity, normalization, and leading coefficient for every \(2\le n\le80\); and it checks the exact \(n=8\) factorization, cubic discriminant, and Routh–Hurwitz inequality. An observed run yielded `EXACT_IDENTITY_CASES: 79`, `N8_CUBIC_DISCRIMINANT: -307921820`, `N8_ROUTH_MARGIN: 2301540`, and `VERIFY_OK`. The all-degree conclusion follows solely from the analytic modulus argument, not from the finite checks.

## Relationship to prior work
Kabluchko and Marynych introduce the Lah generating polynomial in their Definition 1.1 and Lemma 3.1 and explicitly propose in Conjecture 3.11 that its zeros lie in the negative half-plane. Proposition 3.12 identifies a family of **particular negative integer roots**, whereas the claim here excludes *all* nonzero roots from the closed right half-plane for the complete \(k=2\) subfamily, regardless of whether those roots are real. The mandatory origin factor is accounted for explicitly. Their log-concavity and asymptotic results do not assert this global zero-location conclusion. Kabluchko and Steigenberger later extend the distributions to an \(r\)-parameter family and establish log-concavity and limit theorems; those results concern different properties and do not imply the stated polynomial half-plane stability without a new argument. The pointwise rising-factorial representation in the original paper supplies a starting identity; the uniform strict modulus comparison supplies the location proof.

## Limitations
The theorem treats exactly two blocks and finite integer \(n\ge2\). It does not establish the corresponding zero assertion for \(k\ge3\), nonzero deformation parameter \(r\), or a uniform quantitative gap between the roots and the imaginary axis. The existence of another equivalent proof under different terminology has not been excluded by a complete historical literature census; independent priority verification has not been performed.

## References
1. Z. Kabluchko and A. Marynych, *Lah distribution: Stirling numbers, records on compositions, and convex hulls of high-dimensional random walks*, arXiv:2105.11365, first submitted 24 May 2021; especially Definition 1.1, Lemma 3.1, Proposition 3.9, Conjecture 3.11, Proposition 3.12. https://arxiv.org/abs/2105.11365
2. Z. Kabluchko and D. A. Steigenberger, *r-Lah distribution: properties, limit theorems and an application to compressed sensing*, arXiv:2212.12277; especially Lemma 3.6 and Proposition 3.14. https://arxiv.org/abs/2212.12277
3. W.-M. Guo, *Zeros distribution and interlacing property for certain polynomial sequences*, *Open Mathematics*, DOI:10.1515/math-2024-0085. This treats Hankel determinants of different polynomial sequences, not the two-block Lah probability-generating polynomial.
