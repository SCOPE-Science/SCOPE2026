# Every higher convolution power of the Dorff ellipse map loses local univalence

## Finding

Let \(f=h+\overline g\) be the explicit normalized convex harmonic disk-to-ellipse diffeomorphism in Wang and Zhong, *A counterexample to an open problem of Dorff* (2026), arXiv:2609.11556v1, with the exact coefficients specified below. Define its \(m\)-fold harmonic Hadamard power recursively using \(f^{\widetilde{*}1}=f\) and \(f^{\widetilde{*}(m+1)}=f^{\widetilde{*}m}\widetilde{*}f\).

**Theorem.** For every integer \(m\ge3\), write \(f^{\widetilde{*}m}=p_m+\overline{q_m}\). There is a real point \(x_m\in(-1,1)\) such that
\[
p_m'(x_m)=0,\qquad q_m'(x_m)\ne0,
\]
and hence \(J_{f^{\widetilde{*}m}}(x_m)<0\). The point can be chosen with the parity-determined sign
\[
(-1)^{m+1}x_m>0.
\]
Also \(J_{f^{\widetilde{*}m}}(0)=1\), so the Jacobian vanishes at an interior disk point and every \(m\)-fold power with \(m\ge3\) fails local univalence. The original paper establishes the same failure for \(m=2\); therefore no harmonic convolution power after the first is locally univalent.

## Assumptions and scope

Throughout, \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). The map is **exactly** the Wang–Zhong ellipse example, not an arbitrary convex harmonic mapping. Its analytic and coanalytic parts have the convergent expansions
\[
h(z)=z+\sum_{n\ge2}M_nz^n,\qquad
 g(z)=\sum_{n\ge2}N_nz^n,
\]
\[
M_n=Aa^{n-2}+Bb^{n-2},\qquad
N_n=Da^{n-2}+Cb^{n-2},
\]
where the exact rational parameters from their Section 6 are
\[
\begin{gathered}
a=-\frac{10}{11},\qquad b=\frac1{44},\\
A=-\frac{9890884608}{9139543205},\qquad
B=-\frac{251761689}{562995861428},\\
C=\frac{41190732}{12795360487},\qquad
D=\frac{1373955264}{9139543205}.
\end{gathered}
\]
In particular, \(A,B<0\), \(C,D>0\), and \(|A|>27/25>1\). The normalized harmonic Hadamard product multiplies analytic and coanalytic Taylor coefficients separately. Thus for all integers \(m\ge1\),
\[
p_m(z)=z+\sum_{n\ge2}M_n^m z^n,
\qquad q_m(z)=\sum_{n\ge2}N_n^m z^n.
\]
Since \(|a|,|b|<1\), all these series and their derivatives converge uniformly on the closed unit disk, and every boundary evaluation below is valid. The proof only asserts existence, sign and location of at least one critical point, not uniqueness or a full Jacobian-zero census.

## Proof

For real \(t\) with \(|t|<1\), define
\[
S_t(z)=\sum_{n\ge2}n t^{n-2}z^{n-1}
=\frac{z(2-tz)}{(1-tz)^2}.
\]
The binomial theorem applied to the exact geometric coefficient tails gives, for every integer \(m\ge1\),
\[
\begin{aligned}
p_m'(z)&=1+\sum_{j=0}^m\binom mj A^j B^{m-j}S_{a^jb^{m-j}}(z),\\
q_m'(z)&=\sum_{j=0}^m\binom mj D^j C^{m-j}S_{a^jb^{m-j}}(z).
\end{aligned}
\tag{1}
\]
Each number \(t=a^jb^{m-j}\) lies strictly between \(-1\) and \(1\). If \(-1\le x\le1\), \(x\ne0\), then \(2-tx>0\) and \((1-tx)^2>0\), so \(S_t(x)\) has the same sign as \(x\). Because \(C,D>0\), every summand of \(q_m'(x)\) has this sign. Hence
\[
q_m'(x)\ne0\qquad(0<|x|\le1).
\tag{2}
\]

Fix an arbitrary integer \(m\ge3\) and put \(\varepsilon_m=(-1)^{m+1}\), a real boundary point \(+1\) for odd \(m\) and \(-1\) for even \(m\). The coefficient \(A^jB^{m-j}\) in every term of the first sum in (1) has sign \((-1)^m\), whereas \(S_t(\varepsilon_m)\) has sign \(\varepsilon_m=(-1)^{m+1}\). Thus **every** term of \(p_m'(\varepsilon_m)-1\) is negative. Keeping just the \(j=m\) term yields
\[
p_m'(\varepsilon_m)
\le1-|A|^m \frac{2+\rho^m}{(1+\rho^m)^2},
\qquad \rho=\frac{10}{11}.
\tag{3}
\]
Indeed \(a^m\varepsilon_m=-\rho^m\), and consequently \(S_{a^m}(\varepsilon_m)=\varepsilon_m(2+\rho^m)/(1+\rho^m)^2\).

Set \(F(u)=(2+u)/(1+u)^2\) for \(0<u<1\). Direct differentiation gives \(F'(u)=-(3+u)/(1+u)^3<0\). Since \(\rho^m\) decreases strictly with \(m\) and \(|A|>1\), the positive expression \(|A|^mF(\rho^m)\) increases strictly with integer \(m\). For the first relevant exponent, \(|A|>27/25\) and exact rational arithmetic gives
\[
\left(\frac{27}{25}\right)^3
\frac{2+(10/11)^3}{(1+(10/11)^3)^2}
=1+\frac{136271021}{1048140625}>1.
\]
Thus \(|A|^mF(\rho^m)>1\) for **every integer** \(m\ge3\), and (3) implies
\[
p_m'(\varepsilon_m)<0,\qquad p_m'(0)=1.
\]
Because the coefficients of (1) are real, \(p_m'\) is real and continuous on the segment joining \(0\) to \(\varepsilon_m\). The intermediate value theorem gives \(x_m\) strictly between these endpoints, with \(p_m'(x_m)=0\). As \(x_m\ne0\), (2) gives \(q_m'(x_m)\ne0\). At that point
\[
J_{f^{\widetilde{*}m}}(x_m)
=|p_m'(x_m)|^2-|q_m'(x_m)|^2
=-|q_m'(x_m)|^2<0.
\]
Meanwhile \(p_m'(0)=1\) and \(q_m'(0)=0\), so the Jacobian at the origin equals \(1\). Continuity along the real segment from \(0\) to \(x_m\) forces an interior Jacobian zero. Lewy's necessary Jacobian criterion for locally one-to-one planar harmonic maps (recalled in the primary source, Theorem 2.1) proves failure of local univalence. The case \(m=2\) is the original Wang–Zhong theorem, not a new proof here. \(\square\)

## Verification

The accompanying standalone `artifacts/verify.py` works only with Python's standard-library exact `fractions.Fraction` and `math.comb`. It verifies all six source parameters, coefficient-sign hypotheses, the sharp rational base inequality and formula (3), then checks (1)–(3) for the sample integers \(3\le m\le12\). Run `python3 artifacts/verify.py` in the directory containing this file. The checker prints `EXACT_RATIONAL_CHECKS_PASS`. The **universal** statement is proved by the monotonicity/sign argument above, not inferred from these finite tests.

## Relationship to prior work

Wang and Zhong, arXiv:2609.11556v1 (2026), constructed the convex harmonic ellipse map and proved only the failure of its **second** harmonic convolution power, evaluating a negative Jacobian at a specific real point. A later result entitled *Unique real-axis fold point in the Dorff ellipse counterexample* further classifies exactly the real Jacobian sign for that same **second** power; it does not assert nonunivalence of any higher power. The present argument applies coefficient powers to the original exact geometric tails and proves a new all-integer instability theorem for the **third and every later power**, with the opposite real-axis direction for odd versus even exponents. Earlier positive harmonic-convolution results impose particular mapping or dilatation hypotheses and do not evaluate these higher powers of this explicit ellipse map.

## Limitations

The theorem concerns the single rationally specified 2026 ellipse map, not all maps in the normalized convex harmonic class. It establishes existence of one real analytic critical-point witness \(p_m'(x_m)=0\) for each \(m\ge3\), but does not determine whether that witness or the resulting Jacobian zero is unique, locate nonreal zeros, give a common neighborhood of negative Jacobian for all \(m\), or classify the critical sets quantitatively. Other potentially unpublished formulations have not been independently excluded.

## References

1. Z.-G. Wang and D. Zhong, *A counterexample to an open problem of Dorff*, arXiv:2609.11556v1, posted 10 September 2026, especially Sections 2 and 6–8, https://arxiv.org/abs/2609.11556.
2. M. Dorff, *Convolutions of planar harmonic convex mappings*, Complex Variables 45 (2001), 263–271, DOI:10.1080/17476930108815381.
3. Z. Boyd, M. Dorff, M. Nowak, M. Romney, and M. Wołoszkiewicz, *Univalency of convolutions of harmonic mappings*, Applied Mathematics and Computation 234 (2014), 326–332, DOI:10.1016/j.amc.2014.01.162.
4. *Unique real-axis fold point in the Dorff ellipse counterexample*, published mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-unique-real-axis-fold-point-in-the-dorff-ellipse-counterexample--8f1ef438e553.
