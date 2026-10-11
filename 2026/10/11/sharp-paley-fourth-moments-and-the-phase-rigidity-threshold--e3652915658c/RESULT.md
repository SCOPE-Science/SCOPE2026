# Sharp Paley fourth moments and the phase-rigidity threshold

## Finding

Let \(p\ge 7\) be a rational prime with \(p\equiv3\pmod4\). Write \(H=\{a^2:a\in\mathbb F_p^\times\}\), \(m=|H|=(p-1)/2\), and \(\omega=e^{2\pi i/p}\). For every family of complex coefficients \((c_h)_{h\in H}\), put
\[
F_c(x)=\sum_{h\in H}c_h\omega^{hx},\qquad x\in\mathbb F_p.
\]
Then the sharp normalized fourth-moment inequality is
\[
\boxed{\frac1p\sum_{x\in\mathbb F_p}|F_c(x)|^4
\le \frac{m^2+1}{2m}\left(\sum_{h\in H}|c_h|^2\right)^2.}
\]
Equality always holds for the zero coefficient family. For nonzero families, the equality set is complete and exhibits a sharp arithmetic transition:

- If \(p=7\), equality holds exactly when all three coefficient moduli are equal. After quotienting by common nonzero complex scalars, the extremizers constitute a two-dimensional phase torus.
- For **every** prime \(p\ge11\) with \(p\equiv3\pmod4\), equality holds exactly when
\[
\boxed{c_h=C\,\omega^{kh}\quad(h\in H),\qquad C\in\mathbb C^\times,\quad k\in\mathbb F_p.}
\]
Thus there are precisely \(p\) projective extremizers for \(p\ge11\); no non-character phase assignments attain the sharp bound.

The value of the sharp constant, together with this complete equality classification, concerns the Fourier synthesis operator with **unrestricted complex** coefficient amplitudes and phases on the Paley quadratic-residue spectrum.

## Assumptions and scope

The field is a prime field, not an arbitrary prime-power field; \(p\equiv3\pmod4\) ensures that the nonzero squares form a cyclic skew Paley difference set in the additive group. Counting measure in the left-hand side is normalized by \(1/p\). The coefficient norm on the right is the **unnormalized** sum of squared moduli. There is no restriction to real, unimodular, or nonnegative coefficients. The result does not claim an analogous equality description for primes congruent to one modulo four or for general difference sets.

## Proof

**1. Paley difference counts.** Let \(\chi\) denote the Legendre character with \(\chi(0)=0\). Because \(\chi(-1)=-1\), the elementary character identities
\[
\sum_{b\in\mathbb F_p}\chi(b)=0,
\qquad\sum_{b\in\mathbb F_p}\chi(b)\chi(b+t)=-1\quad(t\ne0)
\]
show that, for every nonzero \(t\),
\[
N_t:=|\{(a,b)\in H^2:a-b=t\}|=\frac{p-3}{4}=:\ell=\frac{m-1}{2}.
\]
Indeed, expand \(\sum_b(1+\chi(b))(1+\chi(b+t))=p-1\), then remove the two exceptional positions \(b=0,-t\); their sum is \(2+\chi(t)+\chi(-t)=2\), hence \(4N_t=p-3\). Also \(N_0=m\).

**2. The exact inequality and all its immediate equality conditions.** Define \(S=\sum_{h\in H}|c_h|^2\) and, for \(t\in\mathbb F_p\),
\[
R(t)=\sum_{a,b\in H:\,a-b=t}c_a\overline{c_b}.
\]
Fourier orthogonality gives the exact convolution identity
\[
\frac1p\sum_x|F_c(x)|^4=\sum_{t\in\mathbb F_p}|R(t)|^2.
\]
Here \(R(0)=S\). For \(t\ne0\), Cauchy–Schwarz across exactly \(\ell\) ordered pairs yields
\[
|R(t)|^2\le\ell\sum_{a-b=t}|c_a|^2|c_b|^2.
\]
Consequently
\[
\begin{aligned}
\frac1p\sum_x|F_c(x)|^4
&\le S^2+\ell\left(S^2-\sum_{h\in H}|c_h|^4\right)\\
&\le \left[1+\ell\left(1-\frac1m\right)\right]S^2
=\frac{m^2+1}{2m}S^2.
\end{aligned}
\]
For \(S>0\), equality in the last step holds exactly when all \(|c_h|\) are the same strictly positive number. Equality in the first step then means that, for each fixed nonzero \(t\), **every** product \(c_a\overline{c_b}\) with \(a-b=t\) has the same complex value. These conditions are also sufficient. Choosing \(c_h=C\omega^{kh}\) makes every product on a fixed difference class equal to \(|C|^2\omega^{kt}\); hence the constant is attained and sharp.

Write \(u_h=c_h/|c_h|\) at equality. Since each nonzero difference occurs, the relations imply that the function
\[
v:\mathbb F_p\longrightarrow\mathbb T,
\qquad v(0)=1,
\qquad v(a-b)=u_a\overline{u_b}\quad(a,b\in H)
\]
is well-defined, with \(v(-t)=\overline{v(t)}\). It remains to show that \(v\) is an additive character when \(p\ge11\).

**3. Character rigidity for primes at least nineteen.** Suppose \(x,y,x+y\) are nonzero. If there is \(b\in H\) with \(b+x,b-y\in H\), then
\[
\begin{aligned}
v(x)v(y)&=(u_{b+x}\overline{u_b})(u_b\overline{u_{b-y}})\\
&=u_{b+x}\overline{u_{b-y}}=v(x+y).
\end{aligned}
\]
Cases where \(x=0\), \(y=0\), or \(x+y=0\) already follow from \(v(0)=1\) and \(v(-t)=\overline{v(t)}\).

For distinct shifts \(0,x,-y\), let
\[
T(x,y)=\sum_{b\in\mathbb F_p}\chi\bigl(b(b+x)(b-y)\bigr).
\]
The elementary linear- and quadratic-character sums, together with the classical Weil bound for a squarefree cubic, yield
\[
|T(x,y)|\le2\sqrt p.
\]
Expanding the three factors \((1+\chi(b))(1+\chi(b+x))(1+\chi(b-y))\) gives total \(p-3+T(x,y)\). At the three roots the product of these factors is at most four. After excluding these roots, each remaining value equals eight times the indicator that \(b,b+x,b-y\) are all squares. Therefore
\[
8\,|H\cap(H-x)\cap(H+y)|\ \ge\ p-15-2\sqrt p.
\]
This is strictly positive for every \(p\ge31\), since the lower bound is already positive at \(31\) and increases thereafter.

The two remaining primes \(p\equiv3\pmod4\) in the range \(19\le p<31\) are \(19\) and \(23\). Exhaustively enumerating exactly all pairs \((x,y)\) with \(x,y,x+y\ne0\), using the explicit set of nonzero squares, gives these complete histograms of \(|H\cap(H-x)\cap(H+y)|\):

| Prime | Intersection size 1 | Size 2 | Size 3 | Number of tested pairs |
| --- | ---: | ---: | ---: | ---: |
| \(19\) | \(126\) | \(162\) | \(18\) | \(306\) |
| \(23\) | \(66\) | \(264\) | \(132\) | \(462\) |

The plain-Python exhaustive loops in `checker.py` use integer modular arithmetic only and reproduce these counts. There are no untested pairs in the stated finite ranges. Hence \(v(x+y)=v(x)v(y)\) for every \(x,y\) whenever \(p\ge19\). Every character of the cyclic additive group \(\mathbb F_p\) is \(v(t)=\omega^{kt}\) for some \(k\in\mathbb F_p\). Fixing any \(h_0\in H\) and putting \(C=u_{h_0}\omega^{-kh_0}|c_{h_0}|\) recovers \(c_h=C\omega^{kh}\).

**4. The exceptional prime eleven.** Now \(H=\{1,3,4,5,9\}\). The four valid equal-sum relations
\[
1+5=3+3,\quad1+1=4+9,\quad1+9=5+5,\quad3+5=4+4\pmod{11}
\]
imply, from the already proved difference-class phase condition,
\[
u_1u_5=u_3^2,\quad u_1^2=u_4u_9,\quad u_1u_9=u_5^2,\quad u_3u_5=u_4^2.
\]
After dividing by common phase \(u_1\), write the four remaining phases as \(z_3,z_4,z_5,z_9\). These constraints are the kernel of the monomial homomorphism of the four-torus whose integer exponent matrix is
\[
M=\begin{pmatrix}-2&0&1&0\\0&1&0&1\\0&0&-2&1\\1&-2&1&0\end{pmatrix},
\qquad|\det M|=11.
\]
An integer matrix of full rank defines a torus endomorphism with exactly \(|\det M|\) kernel points, so there are **at most eleven** normalized solutions to these four necessary relations. The eleven distinct character restrictions \((u_h)=(\omega^{kh})_{h\in H}\) satisfy them, and already attain equality. Thus these are precisely all extremizers at \(p=11\). The determinant is checked independently using fraction-free integer elimination in `checker.py`.

**5. The exceptional prime seven.** Now \(m=3\) and \(\ell=1\): each nonzero difference has exactly one ordered representation, so the Cauchy–Schwarz step in part 2 is automatically equality for every phase assignment. Equality requires only constant coefficient modulus, giving the claimed projective two-torus. The two extra phase degrees of freedom at \(p=7\) prove the threshold \(p=11\) is sharp among the allowed primes.

## Verification

Run `python3 checker.py` with the Python standard library. Its exact-arithmetic checks reproduce the Paley difference multiplicities for eight primes \(7,11,19,23,31,43,47,59\), both small-prime triple-intersection histograms, the integer determinant \(11\), the small-prime equal-sum relations, and weighted integer coefficient fourth-moment inequalities. The recorded run returned `EXACT_COMBINATORIAL_CERTIFICATE_PASS 335`. These finite checks corroborate, but do not replace, the general proof: its only non-elementary external input is the classical Weil bound for quadratic-character sums of squarefree cubics. The calculation for \(19\) and \(23\) is fully exhaustive rather than a numerical sample.

## Relationship to prior work

Paley difference sets and their uniform nonzero difference multiplicities are classical. Günther and Schmidt study asymptotic merit factors and low aperiodic fourth moments of \(\pm1\)-coefficient polynomials built from difference sets, explicitly including Paley sets; their assertions do not optimize **periodic** fourth moments over arbitrary complex coefficients or classify equality phases on \(H\). Hanson and Petridis study additive decompositions of multiplicative subgroups and quadratic residues; their results motivate the additive structure of \(H\), but do not give this sharp Fourier norm/equality statement. Lev and Sonn study representations of residue sets as differences, with a different quantifier and principally congruence-one arithmetic. González-Riquelme and Oliveira e Silva establish sharp extension results for paraboloids and cones, not the Paley residue support considered here. Closely adjacent discrete Fourier results do not automatically imply the character-rigidity transition.

## Limitations

The theorem is proved only for primes \(p\equiv3\pmod4\) and the specified fourth moment. It does not characterize extremizers for other difference sets, arbitrary prime powers, or other moments. The Weil character-sum estimate is invoked as a standard established theorem, not reproved. A historically equivalent Freiman-phase formulation or an older Paley fourth-moment equality theorem remains a plausible bibliographic risk; no blanket novelty or independent verification is claimed.

## References

1. C. Günther and K.-U. Schmidt, *Merit factors of polynomials derived from difference sets*, arXiv:1503.05858, especially Sections 1–2 on Paley difference sets and asymptotic merit factors.
2. B. Hanson and G. Petridis, *Refined Estimates Concerning Sumsets Contained in the Roots of Unity*, arXiv:1905.09134, initial public version 2019-05-22.
3. V. F. Lev and J. Sonn, *Quadratic Residues and Difference Sets*, arXiv:1502.06833.
4. C. González-Riquelme and D. Oliveira e Silva, *Sharp Extension Inequalities on Finite Fields*, arXiv:2405.16647.
5. Classical Weil bound for quadratic-character sums of squarefree cubic polynomials: \(|\sum_{x\in\mathbb F_p}\chi(P(x))|\le2\sqrt p\) for a squarefree cubic \(P\in\mathbb F_p[x]\).
