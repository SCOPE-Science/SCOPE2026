# Exact sixth-moment Strichartz norm of five consecutive periodic Schrödinger modes

## Finding

Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with normalized Haar measure. For \(a_0,\ldots,a_4\in\mathbb C\), write
\[
U_a(x,t)=\sum_{n=0}^{4}a_n e^{i(nx-n^2t)},\qquad S=\sum_{n=0}^{4}|a_n|^2.
\]
There is a unique \(b_*\in(0,\tfrac12)\) satisfying
\[
831b_*^4+2576b_*^3+1340b_*^2-182b_*-56=0.
\]
Put
\[
a_* =\frac{1+11b_*-8b_*^2}{10+25b_*},\qquad c_*=1-2a_*-2b_*.
\]
These three numbers are strictly positive, and the **exact sharp sixth-power Strichartz constant** is
\[
\boxed{\sup_{S>0}\frac{\int_{\mathbb T^2}|U_a(x,t)|^6\,\frac{dx\,dt}{(2\pi)^2}}{S^3}
=6-9(2a_*^2+2b_*^2+c_*^2)+4(2a_*^3+2b_*^3+c_*^3)+18a_*b_*^2
=4.5186200812816083658776462004075\ldots.}
\]
The sharp norm constant is the sixth root of this number, approximately \(1.2857828773572631\). Every nonzero extremizer, and no other vector, satisfies
\[
\frac{(|a_0|^2,|a_1|^2,|a_2|^2,|a_3|^2,|a_4|^2)}{S}
=(a_*,b_*,c_*,b_*,a_*)
\]
and
\[
\arg(a_0)+2\arg(a_3)-2\arg(a_1)-\arg(a_4)\equiv0\pmod{2\pi}.
\]
All five entries of an extremizer are nonzero. Apart from this one phase relation, the coefficient phases are free. The value and optimizer classification are independent of the sign convention in the time exponent.

## Assumptions and scope

The assertion holds for arbitrary complex coefficients supported on the **fixed five consecutive integer frequencies** \(\{0,1,2,3,4\}\), and for the full normalized spacetime torus; it makes no claim concerning arbitrary larger spectral supports, finite observation windows, or a universal sharp constant across all bandwidths. Translating the entire five-frequency interval changes \(U_a\) by measure-preserving spacetime modulation and shear, so the same result holds for any interval of five consecutive integer frequencies.

## Proof

**Step 1: the unique sixth-moment resonance.** By orthogonality on \(\mathbb T^2\), the sixth moment is the sum of squares of the coefficient sums in the fibers of the map sending an unordered triple \((j,k,\ell)\) to \((j+k+\ell,j^2+k^2+\ell^2)\). Exhausting all 35 unordered triples from \(\{0,1,2,3,4\}\), only one fiber contains two different triples:
\[
(0,3,3)\longleftrightarrow(1,1,4),
\qquad \sum n=6,\quad \sum n^2=18.
\]
The other 33 fibers are singletons. The multiplicity of each exceptional triple is three. Thus, for \(u_j=|a_j|^2/S\), \(S>0\), the normalized moment is exactly
\[
\mathcal M=6-9\sum_{j=0}^{4}u_j^2+4\sum_{j=0}^{4}u_j^3
+\frac{18}{S^3}\operatorname{Re}(a_0a_3^2\overline{a_1^2a_4}).\tag{1}
\]
The first three terms follow from the diagonal triple types with multinomial weights \(1,3,6\). The final term is the only off-diagonal interference. It is at most \(18\sqrt{u_0u_4}\,u_1u_3\); equality with nonzero entries is equivalent to the stated phase condition.

**Step 2: strict amplitude-pair symmetrization.** Fix \(u_0+u_4=s\), with \(u_0=s/2+\delta\) and \(u_4=s/2-\delta\). Replacing the pair by \(s/2,s/2\) raises the nonresonant part of (1) by \((18-12s)\delta^2\), which is strictly positive for \(\delta\ne0\) because \(0\le s\le1\). The phase-optimized resonant part also cannot decrease, because \(\sqrt{u_0u_4}\) is maximized at equality. The same computation with \(u_1,u_3\), using their fixed sum and the product \(u_1u_3\), likewise proves strict improvement unless \(u_1=u_3\). Accordingly every extremizing squared-magnitude profile has the form
\[
(u_0,u_1,u_2,u_3,u_4)=(a,b,c,b,a),\qquad c=1-2a-2b\ge0,
\]
with \(a,b\ge0\) and \(a+b\le\tfrac12\). Conversely these symmetric profiles permit the maximal resonance phase, so optimizing (1) is equivalent to optimizing
\[
\begin{aligned}
F(a,b)&=6-9(2a^2+2b^2+c^2)+4(2a^3+2b^3+c^3)+18ab^2\\
&=-24a^3-96a^2b-78ab^2-24b^3-6a^2-6b^2+24ab+12a+12b+1.
\end{aligned}\tag{2}
\]

**Step 3: exclude every boundary.** On \(a=0\) or \(b=0\), (2) becomes \(-24x^3-6x^2+12x+1\), whose maximum on \([0,\tfrac12]\) is \(31/9\), attained at \(x=1/3\). On \(c=0\), substituting \(b=1/2-a\) gives
\[
F(a,\tfrac12-a)=\frac{36a^3-84a^2+33a+5}{2},\qquad 0\le a\le\tfrac12.
\]
Its maximum is \((97\sqrt{97}-260)/162\), at \(a=(14-\sqrt{97})/18\), strictly less than \(9/2\), because \(97^3<989^2\). The admissible interior point \(a=b=1/5\) gives \(F=563/125>9/2\). Compactness therefore forces all global maxima into the open triangle.

**Step 4: exactly one interior stationary point.** Differentiating (2), the equations \(F_a=F_b=0\) are
\[
\begin{split}
f&=12a^2+32ab+2a+13b^2-4b-2=0,\\
g&=8a^2+13ab-2a+6b^2+b-1=0,
\end{split}
\]
where \(F_a=-6f\), \(F_b=-12g\). Their combination
\[
8f-12g=4\bigl((25b+10)a+8b^2-11b-1\bigr)=0
\]
forces \(a=(1+11b-8b^2)/(10+25b)\). Substituting into \(f\), and clearing the positive denominator, yields
\[
(10+25b)^2 f\left(\frac{1+11b-8b^2}{10+25b},b\right)
=3\bigl(831b^4+2576b^3+1340b^2-182b-56\bigr).
\]
The quartic has exactly one positive real root by Descartes' rule of signs (its descending coefficient signs are \(+,+,+,-,-\); its value at zero is negative). Since a global maximum has already been shown to occur in the interior, this unique positive root must generate its stationary point. Therefore the maximizer \((a_*,b_*)\) of (2) is unique and has \(c_*>0\). Numerically, using rational bisection,
\[
(a_*,b_*,c_*)=(0.1960270698894905\ldots,\ 0.2221936294185893\ldots,\ 0.1635586013838403\ldots).
\]
The phase equality characterization in Step 1 now gives every equality case and proves the sharp constant.

## Verification

The accompanying standalone \(`verify.py`\) uses only the Python standard library. Running \(`python3 verify.py`\) checks the exact 35-triple resonance census, reconstructs the sixth-moment identity from 100 independently seeded Gaussian-integer coefficient vectors, verifies the polynomial elimination identity with exact rational arithmetic, isolates the unique positive quartic root by 180 rational bisection steps, and checks numerical brackets for the three weights and the sixth moment. The proof of global optimality is the analytic symmetrization, boundary comparison, and unique-critical-point argument above, **not** extrapolation from the finite tests.

## Relationship to prior work

Dai and Guo (first posted 2026-04-28) prove the correct logarithmic order of the global critical periodic Schrödinger \(L^6\) Strichartz estimate as bandwidth grows. Their inspected theorem and proof establish a bandwidth-dependent inequality, not the exact five-mode norm or all its extremizers. A related September 2026 manuscript by Deng, Fan, S. Guo, Z. Guo and Luo also concerns sharp global periodic Strichartz bounds; its full text was not obtained and its possible overlap remains an explicit priority risk.

The related published finite-four-character result, *Sharp sixth-moment norm for one balanced triple-sum defect*, gives the boundary value \((97\sqrt{97}-260)/162\) for a four-character collision. The present five-mode exact constant is strictly larger, with a strictly positive central mode, so it is not a specialization of that four-character statement. Ordinary three-character Fourier sixth moments and sixth moments over finite-field parabolas involve different frequency configurations or ambient groups. No identical five-mode classification was located in targeted searches; this absence does not establish absolute historical priority.

## Limitations

The theorem is restricted to a fixed five-consecutive-mode subspace and normalized full-period spacetime \(L^6\) averaging. It is not an asymptotic \(N\to\infty\) estimate, and gives no global sharp constants for more than five modes. The full text of the potentially adjacent September 2026 manuscript and some indexed finite-character records was inaccessible; overlap with unindexed finite-band numerical tables remains possible. These are historical-priority limitations, not mathematical assertions of independence or external certification.

## References

1. P. Dai and Z. Guo, *Sharp Strichartz estimate for the 1D periodic Schrödinger equation*, arXiv:2604.25593v1, first public 2026-04-28, https://arxiv.org/html/2604.25593v1.
2. Y. Deng, C. Fan, S. Guo, Z. Guo and Y. Luo, *Sharp Strichartz estimates on the one-dimensional torus*, arXiv:2609.18670v1, first public 2026-09-16, https://arxiv.org/abs/2609.18670 (abstract inspected; full text unavailable in this review).
3. *Sharp sixth-moment norm for one balanced triple-sum defect*, published indexed mathematical record, 2026-10-11 (abstract-level mathematical statement inspected; full proof not accessible).
