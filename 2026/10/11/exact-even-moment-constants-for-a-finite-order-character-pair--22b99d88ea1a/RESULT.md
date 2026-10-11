# Exact even-moment constants for a finite-order character pair
## Finding
Let \(G\) be a compact abelian group with normalized Haar measure, let \(\lambda_0,\lambda_1\in\widehat G\) be distinct characters, and let \(h\ge2\) be an integer. Set
\[
\chi=\lambda_1\lambda_0^{-1}.
\]
If \(\chi\) has finite order \(q\ge2\), then the sharp constant in
\[
\|a\lambda_0+b\lambda_1\|_{L^{2h}(G)}
\le K_{q,h}(|a|^2+|b|^2)^{1/2}
\]
is
\[
K_{q,h}^{2h}
=2^{-h}\sum_{\substack{0\le m\le2h\\m\equiv h\pmod q}}
\binom{2h}{m}.
\]
If \(\chi\) has infinite order, then
\[
K_{\infty,h}^{2h}=2^{-h}\binom{2h}{h}.
\]
Consequently, the finite-order constant agrees exactly with the continuous two-frequency value when \(q>h\), and is strictly larger when \(2\le q\le h\).

Every nonzero extremizer satisfies \(|a|=|b|\). If \(q>h\), or if \(\chi\) has infinite order, every relative coefficient phase is extremal. If \(2\le q\le h\), equality holds exactly when
\[
q(\arg b-\arg a)\in2\pi\mathbb Z.
\]

## Assumptions and scope
The group is compact abelian and Haar measure is normalized to total mass one. The two characters are distinct. The quotient character \(\chi\) either has a finite image consisting of the \(q\)-th roots of unity or has infinite image; a closed infinite subgroup of the circle is the whole circle. The exponent is an even integer \(2h\) with \(h\ge2\).

The result is a complete two-character calculation. It does not assert an analogous closed formula for three or more characters, where several independent additive relations can interact.

## Proof
Multiplication by \(\lambda_0\) does not change the norm, so it is enough to study \(a+b\chi\). If \(\chi\) has finite order \(q\), Haar measure pushes forward to the uniform probability measure on the \(q\)-th roots of unity. Write
\[
s=|a|^2+|b|^2,
\qquad
t=\frac{|a||b|}{s}\in[0,1/2],
\qquad
\phi=\arg b-\arg a.
\]
For \(s>0\), root-of-unity averaging gives
\[
\frac{\|a+b\chi\|_{2h}^{2h}}{s^h}
=\frac1q\sum_{j=0}^{q-1}
\left(1+2t\cos\left(\phi+\frac{2\pi j}{q}\right)\right)^h.
\]
Expand first in powers of \(2t\cos\theta\), and then expand each cosine power into exponentials. Root-of-unity orthogonality yields
\[
\Phi_{q,h}(t,\phi)
=\sum_{r=0}^{h}\binom hr t^r
\sum_{\substack{0\le k\le r\\q\mid r-2k}}
\binom rk e^{i(r-2k)\phi}.
\]
After pairing the terms indexed by \(k\) and \(r-k\), this is a real cosine polynomial whose coefficients are all nonnegative. Hence
\[
\Phi_{q,h}(t,\phi)\le \Phi_{q,h}(t,0).
\]
If \(q>h\), every surviving frequency \(r-2k\) is zero, so the expression is independent of \(\phi\). If \(q\le h\), the term \(r=q\) contains a strictly positive multiple of \(\cos(q\phi)\). Therefore equality in the phase bound is possible exactly when \(q\phi\in2\pi\mathbb Z\); that condition also makes every surviving multiple-of-\(q\) frequency equal to one.

At \(\phi=0\), every coefficient of \(\Phi_{q,h}(t,0)\) as a polynomial in \(t\) is nonnegative. Its \(t^2\) coefficient is strictly positive because the zero-frequency term with \(r=2\) and \(k=1\) is present. Thus \(\Phi_{q,h}(t,0)\) is strictly increasing for \(t>0\), and its maximum on \([0,1/2]\) occurs at \(t=1/2\). By the arithmetic-geometric mean inequality, \(t=1/2\) is equivalent to \(|a|=|b|\).

At \(t=1/2\) and aligned phase,
\[
K_{q,h}^{2h}
=2^{-h}\frac1q\sum_{j=0}^{q-1}|1+e^{2\pi i j/q}|^{2h}.
\]
For \(|z|=1\),
\[
|1+z|^{2h}=z^{-h}(1+z)^{2h}
=\sum_{m=0}^{2h}\binom{2h}{m}z^{m-h}.
\]
Averaging over the \(q\)-th roots of unity keeps exactly the exponents divisible by \(q\), which proves the displayed binomial-congruence formula. When \(q>h\), only \(m=h\) can survive. When \(q\le h\), the two additional indices \(m=h-q\) and \(m=h+q\) are present, so the constant is strictly larger than the central-binomial value.

If \(\chi\) has infinite order, its image is the whole circle and Haar pushforward is Haar measure on the circle. The same Fourier expansion leaves only the zero frequency, giving the central-binomial formula and phase independence. The strict \(t\)-monotonicity argument again forces equal coefficient magnitudes.

## Verification
The proof is symbolic and does not depend on finite computation. The accompanying `artifacts/verify.py` independently checks the root-filter identity by two exact integer expansions for all \(2\le q\le18\) and \(2\le h\le14\), checks the threshold dichotomy against the central binomial coefficient, verifies the existence or absence of nonzero phase frequencies in the two regimes, and performs deterministic numerical inequality tests for representative coefficient phases and magnitudes. These computations corroborate the algebra; the all-parameter proof is the argument above.

## Relationship to prior work
The classical \(\Lambda(p)\)-set framework asks for sharp constants controlling \(L^p\) norms of Fourier sums by coefficient \(\ell^2\) norms. Michels formulates this framework for character sets on compact abelian groups and studies structural consequences for infinite sets and operator ideals. The present result evaluates the complete two-character even-moment problem and isolates the exact finite-order aliasing threshold.

For a continuously distributed circle phase, the central-binomial moment is consistent with the complex Steinhaus setting studied in Kahane--Khintchine theory. The new finite-order term is the congruence-class correction caused by root-of-unity aliasing. In particular, finite and continuous behavior agree for all moments below the quotient-character order and split exactly when the half-moment reaches that order.

Previously tabulated special cases for ternary sixth moments and fourth-root eighth moments correspond only to \((q,h)=(3,3)\) and \((q,h)=(4,4)\). They do not imply the all-order formula, the exact threshold \(q=h\), or the complete relative-phase transition.

## Limitations
The result concerns a two-dimensional character span and even integer moments. It does not address non-even exponents, and it does not classify higher-cardinality spectra where several additive relations coexist. An originality risk remains that the two-character root-filter formula may have appeared in older finite-group or thin-set literature under different notation; the closest inspected sources do not state the all-order sharp constant together with the threshold and equality classification.

## References
1. C. Michels, “\(\Lambda(p)\)-sets and the limit order of operator ideals,” arXiv:math/9904176v1, first public 30 April 1999.
2. G. Peskir, “Best Constants in Kahane--Khintchine Inequalities for Complex Steinhaus Functions,” Proceedings of the American Mathematical Society 123 (1995), 3101--3111.
