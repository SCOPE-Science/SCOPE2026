# Exact three-site laws for the period-doubling substitution

## Finding

Let \(s_n\in\{-1,+1\}\) be the one-sided fixed point of the primitive period-doubling substitution \(+1\mapsto(+1,-1)\), \(-1\mapsto(+1,+1)\), with \(s_0=+1\). For distinct nonzero integer displacements \(a,b\), put
\[
 m=\min\{\nu_2(a),\nu_2(b),\nu_2(a-b)\},\qquad
 t=\max\{\nu_2(a),\nu_2(b),\nu_2(a-b)\},
\]
where \(\nu_2(h)\) is the exponent of \(2\) in \(|h|\) for nonzero integers \(h\). The three valuations consist of \(m,m,t\) with \(t>m\). Put \(n_0=\max\{0,-a,-b\}\) so that all indices below are nonnegative. The unrestricted, arbitrary-lag three-site signed correlation exists and is exactly
\[
 \boxed{\mathcal T(a,b)=\lim_{N\to\infty}\frac1N
 \sum_{n=n_0}^{N-1}s_n s_{n+a}s_{n+b}
 =\frac13-\frac{4(-1)^m}{3\,2^t}.}
\]
Equivalently, the expression is the moment under the unique invariant probability of the two-sided substitution hull.

For every nonzero integer \(h\), the first moment and pair correlations are
\[
 \mathbb E S_0=\frac13,\qquad
 \mathcal C(h)=\mathbb E(S_0S_h)=1-\frac4{3\,2^{\nu_2(h)}}.
\]
Consequently, for any \(\varepsilon_0,\varepsilon_1,\varepsilon_2\in\{-1,+1\}\), the **entire sparse three-site word law** is
\[
\begin{aligned}
 &\Pr(S_0=\varepsilon_0,S_a=\varepsilon_1,S_b=\varepsilon_2)\\
 &\quad=\frac18\bigg(1+\frac{\varepsilon_0+\varepsilon_1+\varepsilon_2}{3}
 +\mathcal C(a)\varepsilon_0\varepsilon_1
 +\mathcal C(b)\varepsilon_0\varepsilon_2
 +\mathcal C(a-b)\varepsilon_1\varepsilon_2
 +\mathcal T(a,b)\varepsilon_0\varepsilon_1\varepsilon_2\bigg).
\end{aligned}
\]
The sharp global range over distinct triple positions is
\[
 -\frac13\le\mathcal T(a,b)\le\frac23.
\]
Equality on the left occurs exactly when \((m,t)=(0,1)\); equality on the right occurs exactly when \((m,t)=(1,2)\). Exact vanishing occurs exactly when \((m,t)=(0,2)\). Thus, for example, \(\mathcal T(1,2)=-1/3\), \(\mathcal T(1,4)=0\), and \(\mathcal T(2,4)=2/3\).

## Assumptions and scope

The substitution and its unique invariant measure are fixed; the result does not concern arbitrary stationary binary processes with the same pair correlations. Displacements are any fixed, distinct, nonzero integers. All averaging and moments use the unique shift-invariant probability on the period-doubling hull; no independence or mixing is assumed. The formulas give normalized frequencies per integer site, not Fourier-transform normalization of diffraction amplitudes. Values of the \(2\)-adic sign at zero are irrelevant because zero has Haar measure zero.

## Proof

**1. Explicit sequence and invariant averaging.** The substitution immediately gives \(s_{2n}=+1\) and \(s_{2n+1}=-s_n\). Induction therefore gives
\[
 s_n=(-1)^{\nu_2(n+1)}\qquad(n\ge0).
\]
Let \(U\) be Haar-uniform on the additive compact group \(\mathbb Z_2\) of \(2\)-adic integers and define \(F(z)=(-1)^{\nu_2(z)}\) for \(z\ne0\) (arbitrary at \(z=0\)). Since integers run uniformly through residue classes modulo every power of two, and the exceptional set where a specified translated argument has valuation at least \(K\) has density \(2^{-K}\), each finite-site correlation of \(s\) equals its Haar expectation for \((F(U),F(U+a),F(U+b))\). More explicitly: approximate all signs by their \(2^K\)-periodic valuation truncations; each of the three errors is confined to one congruence class modulo \(2^K\), and then let \(K\to\infty\). This proves existence and identifies the invariant normalization without assuming ergodicity as an unproved limit claim.

The Haar probability of \(\nu_2(U)=j\) is \(2^{-j-1}\) for \(j\ge0\). Hence
\[
 M:=\mathbb EF(U)=\sum_{j\ge0}(-1)^j2^{-j-1}=\frac13.
\]

**2. Exact pair moment.** Fix \(h\ne0\) with \(r=\nu_2(h)\). When \(\nu_2(U)<r\), the two signs agree and their product is \(1\). This event has probability \(1-2^{-r}\). On the complementary event, factor out \(2^r\): the remaining translated arguments differ by an odd integer, so exactly one is even. Conditioned on its being even, its residual valuation is \(1+\nu_2(W)\) for Haar-uniform \(W\), and the odd argument contributes sign \(+1\). The conditional product mean is therefore \(-M=-1/3\). Thus
\[
 \mathcal C(h)=(1-2^{-r})-\frac13\,2^{-r}
 =1-\frac4{3\,2^r}.
\]

**3. Valuation geometry of three sites.** For \(d_0=0,d_1=a,d_2=b\), the ultrametric triangle property shows exactly two of \(\nu_2(d_i-d_j)\) equal the minimum \(m\), while the remaining one equals \(t>m\). Consequently all three offsets agree modulo \(2^m\); two of them (the *close pair*) agree modulo \(2^{m+1}\), and the remaining *far site* has the opposite residue modulo \(2^{m+1}\).

When \(\nu_2(U+d_0)<m\), all three shifted arguments have the same valuation, say \(j<m\), so their sign product is \((-1)^j\). These cases contribute
\[
 L_m=\sum_{j=0}^{m-1}(-1)^j2^{-j-1}
 =\frac{1-(-1/2)^m}{3};
\]
for \(m=0\) this is the empty sum \(0\).

The remaining case has probability \(2^{-m}\). It splits equally into two residue classes modulo \(2^{m+1}\). On the class in which the far site is divisible by \(2^{m+1}\), the close pair both have valuation exactly \(m\), and the conditional triple mean is
\[
 (-1)^{m+1}M=\frac{(-1)^{m+1}}3.
\]
On the other class, the close pair are divisible by \(2^{m+1}\) while the far site has valuation exactly \(m\). Divide out \(2^{m+1}\) from the two close arguments. Their difference has valuation \(t-m-1\), and the pair calculation gives conditional triple mean
\[
 (-1)^m\left(1-\frac4{3\,2^{t-m-1}}\right).
\]
Adding all disjoint cases,
\[
\begin{aligned}
\mathcal T(a,b)
 &=L_m+2^{-m-1}\left[
 \frac{(-1)^{m+1}}3
 +(-1)^m\left(1-\frac4{3\,2^{t-m-1}}\right)\right]\\
 &=\frac13-\frac{4(-1)^m}{3\,2^t}.
\end{aligned}
\]
This calculation holds for arbitrary fixed nonzero integer displacements, including negative ones, because Haar measure is translation-invariant.

**4. All three-site probabilities and sharp bounds.** For signs \(\varepsilon\in\{-1,+1\}^3\), expand the exact identity
\[
 \mathbf{1}_{\{S_0=\varepsilon_0,S_a=\varepsilon_1,S_b=\varepsilon_2\}}
 =\frac18\prod_{j=0}^2(1+\varepsilon_j S_{d_j}).
\]
Taking expectations and inserting the one-, two-, and three-point values proves the word-probability formula. Since \(m\ge0\), \(t\ge m+1\), and both have integer values, a negative correction is largest in magnitude exactly at \(m=0,t=1\), while a positive correction is largest exactly at \(m=1,t=2\). Finally zero requires \((-1)^m=1\) and \(2^t=4\), forcing \((m,t)=(0,2)\). Each listed valuation pattern is realized by the example pairs in the finding, proving sharpness.

## Verification

The optional standalone `verify.py` uses only exact integer and rational arithmetic. It checks the analytic pair and triple formulas against full finite dyadic residue cycles at moduli \(2^9\), \(2^{11}\), and \(2^{13}\); checks positivity and normalization of 7,936 explicit sign-word probabilities; and tests the valuation classification. It reports `VERIFY_OK: 638 exact dyadic/valuation comparisons, 7936 exact joint-word probabilities` when run with `python3 verify.py`.

The finite-residue discrepancy bound is a rigorous elementary support check: the true \(2\)-adic sign and the periodic truncated sign differ only on one residue class, of Haar measure \(2^{-K}\); a triple product can differ at most at three such translated classes and by at most \(2\) each, yielding \(6\cdot2^{-K}\). The unrestricted result instead follows from the proof above; finite tests alone do not prove an infinite assertion.

## Relationship to prior work

Baake and Grimm (2010, §3) give this substitution, its \(2\)-adic internal space, the sign recursion and exact two-point autocorrelations/diffraction. The present calculation accepts these established facts and explicitly evaluates the three-point sign moment at **every** distinct pair of time displacements, including exact vanishing, extrema and the complete three-site probability table.

Deng and Moody (2009, Proposition 1), as well as their companion work on weighted model sets and higher point-correlations (2009), give the general regular-model-set principle expressing all pattern frequencies and weighted multi-point moments as Haar measures of window intersections. That framework provides an implicit route to any fixed pattern frequency. It does not state the single, valuation-only, all-lag evaluation or its sharp classification. Poláková (2019, Theorem 1.2) evaluates arbitrary **contiguous-word** cylinder probabilities of the same subshift. Any fixed sparse three-site probability can also be recovered by summing its full-word cylinder probabilities; such a potentially long summation is not mistaken for a separate new existence theorem here. The specific direct two-scale valuation collapse across all unbounded lag pairs, including its global zero and extremal classes, is the claimed evaluated contribution. Mazáč (2025) develops general exact patch-frequency renormalisation for substitution systems. His symbolic Theorem 10 assumes an irreducible substitution characteristic polynomial; the period-doubling matrix has characteristic polynomial \(z^2-z-2=(z-2)(z+1)\), so this particular transfer theorem cannot be applied here directly. The general renormalisation viewpoint remains pertinent, not a claim of previously absent patch computability.

## Limitations

No claim is made for general substitutions, arbitrary stationary processes, four or more observation sites, or uniformly varying time lags. The formula does not prove reconstruction of a dynamical system from its two-point function, nor mixing, decay of all correlations, a new spectral classification, or an independent priority determination. The available broader exact cylinder and regular-model-set formulas may already imply each fixed-lag number; the distinction claimed is the explicit **uniform valuation law and sharp global classification**. Literature searches and full-text comparisons reduce but do not eliminate the possibility of an earlier equivalent specialized formula.

## References

1. X. Deng and R. V. Moody, *How model sets can be determined by their two-point and three-point correlations*, arXiv:0901.4381 (first posted 2009-01-28), Proposition 1. https://arxiv.org/abs/0901.4381
2. M. Baake and U. Grimm, *Diffraction of limit periodic point sets*, arXiv:1007.0707 (first posted 2010-07-05), §3, especially equations (5), (9)–(12). https://arxiv.org/abs/1007.0707
3. X. Deng and R. V. Moody, *Weighted model sets and their higher point-correlations*, arXiv:0904.4552 (first posted 2009-04-29), §2 and equation (2). https://arxiv.org/pdf/0904.4552
4. M. Poláková, *Complexity and invariant measure of the period-doubling subshift*, arXiv:1902.08387 (first posted 2019-02-22), Theorems 1.1–1.2 and §4. https://arxiv.org/abs/1902.08387
5. J. Mazáč, *Exact renormalisation for patch frequencies in inflation systems*, arXiv:2507.07753 (first posted 2025-07-10), general patch-frequency framework. https://arxiv.org/abs/2507.07753
