# All-dimensional branch selection for the antipodal-distance constant

## Finding

Dibble and Hoisington define, for \(n\ge2\),
\[
A_n
=
(2^{n-1}\pi n)^{1/n}
\left(\frac{K_{n+1}}{\omega_{n+1}}\right)^{1/(n+1)},
\qquad
K_{n+1}
=
\frac{2}{\sqrt3\,(n+1)!},
\]
and
\[
B_n
=
\left(
(n-1)\frac{\omega_{n-1}}{\omega_{n-2}}-1
\right)^{-1}.
\]
Their Lemma A.2 shows that
\[
\rho_n^*>\rho_n
\quad\Longleftrightarrow\quad
A_n>B_n.
\]

The new conclusion is
\[
\boxed{A_n>B_n\quad\text{for every integer }n\ge2.}
\]
Hence
\[
\boxed{\rho_n^*>\rho_n\quad\text{for every integer }n\ge2.}
\]

Therefore the crossing of the increasing function \(\mathcal I_n\) and the decreasing function \(\mathcal J_n\) always occurs on the second branch of \(\mathcal I_n\). In particular, the equation derived in the source under the condition \(\rho_n^*>\rho_n\),
\[
\boxed{
\rho_n^*(\rho_n^*-1)^{n-1}
=
\pi n(n-1)2^{n-1}
\frac{\omega_{n-1}}{\omega_{n-2}}
\left(
\frac{K_{n+1}}{\omega_{n+1}}
\right)^{n/(n+1)},
}
\]
is valid in every dimension \(n\ge2\).

The source had verified \(A_n>B_n\) computationally through \(n=100000\) and proved it for all sufficiently large \(n\), but did not close the remaining all-dimensional logical gap.

## Assumptions and scope

Here
\[
\omega_m
=
\frac{\pi^{m/2}}{\Gamma(m/2+1)}
\]
is the volume of the Euclidean unit \(m\)-ball. The quantities \(A_n\), \(B_n\), \(\rho_n\), and \(\rho_n^*\) are exactly those of Appendix A of the cited paper.

The result concerns the authors' explicit lower-bound constant and its branch selection. It does not assert that this lower-bound constant is the optimal constant in their geometric theorem.

The proof has an infinite analytic tail and a finite exact certificate. No finite experiment is used to infer an infinite statement.

## Proof

Set
\[
r_n=\frac{\omega_{n-1}}{\omega_{n-2}}
=
\sqrt{\pi}\,
\frac{\Gamma(n/2)}{\Gamma((n+1)/2)}.
\]

By strict log-convexity of the gamma function,
\[
\Gamma\!\left(\frac{n+1}{2}\right)^2
<
\Gamma\!\left(\frac n2\right)
\Gamma\!\left(\frac n2+1\right)
=
\frac n2
\Gamma\!\left(\frac n2\right)^2.
\]
Thus
\[
r_n>\sqrt{\frac{2\pi}{n}}>\sqrt{\frac6n},
\]
where only \(\pi>3\) is used in the final inequality. Therefore
\[
B_n
<
\frac{1}{
(n-1)\sqrt{6/n}-1
}.
\]

For \(n\ge3\),
\[
(n-1)\sqrt6-n-\sqrt n>0.
\]
Indeed it is positive at \(n=3\), because
\[
2\sqrt6>3+\sqrt3,
\]
and its forward difference is
\[
\sqrt6-1-(\sqrt{n+1}-\sqrt n)>0.
\]
Consequently,
\[
B_n<\frac1{\sqrt n}
\qquad(n\ge3).
\]

A stronger tail estimate holds for \(n\ge14\):
\[
(n-1)\sqrt6-2n-\sqrt n>0.
\]
At \(n=14\), this is
\[
13\sqrt6>28+\sqrt{14},
\]
which follows by two squarings from
\[
729>686.
\]
For \(n\ge14\), the forward difference is positive because
\[
\sqrt6-2>\frac25
\]
while
\[
\sqrt{n+1}-\sqrt n
<
\frac17.
\]
Hence
\[
B_n<\frac1{2\sqrt n}
\qquad(n\ge14).
\]

It remains to bound \(A_n\) from below. The recurrence for ball volumes and the gamma duplication formula give
\[
\sqrt3\,\pi n!\,\omega_{n-1}
=
\sqrt3\,2^n\pi^{n/2}
\Gamma\!\left(\frac n2+1\right),
\]
so
\[
A_n
=
(2^{n-1}\pi n)^{1/n}
\left[
\frac{1}{
\sqrt3\,2^n\pi^{n/2}
\Gamma(n/2+1)}
\right]^{1/(n+1)}.
\]

For every integer \(n\ge2\),
\[
\Gamma\!\left(\frac n2+1\right)
\le
\sqrt{\frac{\pi n}{2}}
\left(\frac n2\right)^{n/2}.
\]
For even \(n\), this follows from
\[
m!\le m^m.
\]
For odd \(n=2m+1\), it follows directly from
\[
\Gamma\!\left(m+\frac32\right)
=
\sqrt\pi
\prod_{j=0}^{m}\left(j+\frac12\right)
\le
\sqrt\pi
\left(m+\frac12\right)^{m+1}.
\]

Therefore
\[
A_n\ge L_n,
\]
where
\[
L_n
=
\frac{
(2^{n-1}\pi n)^{1/n}
}{
\left[
\sqrt3\,2^{n/2}
(\pi n)^{n/2}
\sqrt{\pi n/2}
\right]^{1/(n+1)}
}.
\]
A simplification gives
\[
L_n\sqrt n
=
\frac{(\pi n)^{1/n}}{\sqrt\pi}\,
\frac{
2^{(n-1)(n+2)/(2n(n+1))}
}{
3^{1/(2(n+1))}
}.
\]
For \(n\ge2\),
\[
\frac{(n-1)(n+2)}{2n(n+1)}
\ge\frac13.
\]
Using
\[
\pi<4,\qquad
2^{1/3}>\frac54,\qquad
3^{1/6}<\frac54,
\]
and \((\pi n)^{1/n}>1\), one obtains
\[
L_n\sqrt n>\frac12.
\]
Thus
\[
A_n>\frac1{2\sqrt n}
\qquad(n\ge2).
\]

This already combines with the stronger bound for \(B_n\) to prove
\[
A_n>B_n
\qquad(n\ge14).
\]

For the finite block \(3\le n\le13\), it suffices to sharpen the lower bound to
\[
A_n>\frac1{\sqrt n},
\]
because \(B_n<1/\sqrt n\) was proved analytically for every \(n\ge3\).

That finite statement is checked exactly, without floating point. Use the classical rational bounds
\[
3<\pi<\frac{22}{7},
\qquad
\sqrt3<\frac74.
\]
For integer \(m\),
\[
\omega_{2k}=\frac{\pi^k}{k!},
\qquad
\omega_{2k+1}
=
\frac{2^{k+1}\pi^k}{(2k+1)!!}.
\]
Replacing \(\pi\) in the positive factor of \(A_n\) by \(3\), and replacing \(\pi\) and \(\sqrt3\) in its denominator by \(22/7\) and \(7/4\), gives a rational lower bound \(\underline A_n\). The inequality
\[
\underline A_n>\frac1{\sqrt n}
\]
is equivalent, after raising to the positive power \(n(n+1)\), to a rational inequality. The bundled certificate verifies all eleven cases \(3\le n\le13\) exactly; its smallest normalized rational margin occurs at \(n=3\) and equals
\[
\frac{1944365472}{1771561}>1000>1.
\]

Finally, for \(n=2\),
\[
B_2=1
\]
and direct simplification gives
\[
A_2^6=\frac{4\pi}{3}>1,
\]
so \(A_2>B_2\).

Combining the three ranges proves the theorem.

## Verification

The analytic tail \(n\ge14\) is independent of computation. The only finite computation concerns \(3\le n\le13\), where the supplied checker uses Python integer and rational arithmetic only.

The checker reconstructs the rational lower bound from the exact even- and odd-dimensional ball-volume formulas, raises away all radicals, and verifies the eleven rational inequalities. It also verifies that the minimum finite certificate is the \(n=3\) value displayed above.

The primary source was inspected in version 1 at Lemma A.2, the statement that \(A_n>B_n\) had been computationally checked through \(100000\), Lemma A.5 proving only eventual positivity, and the conditional degree-\(n\) equation. Version 2 retains the same gap.

## Relationship to prior work

Dibble and Hoisington reduce the branch question exactly to \(A_n>B_n\). Their version 1 states that this inequality was checked computationally for \(n\le100000\) and then proves only
\[
\lim_{n\to\infty}\frac{A_n}{B_n}=2\sqrt e,
\]
which yields \(A_n>B_n\) for all sufficiently large \(n\). They subsequently write the degree-\(n\) equation only for dimensions satisfying \(\rho_n^*>\rho_n\).

The present argument closes that gap for every \(n\ge2\). It uses a gamma-ratio lower bound from strict log-convexity, an elementary parity bound for \(\Gamma(n/2+1)\), and an exact finite rational bridge between the two analytic regimes.

Targeted searches by the paper identifier, the symbols \(A_n\), \(B_n\), \(\rho_n^*\), the branch condition, and the phrase describing the \(100000\)-dimensional computation located no later public proof of the all-dimensional inequality.

## Limitations

The theorem settles only the branch condition inside the explicit constant construction of the source. It does not improve the geometric ingredients from which that constant is built, and it does not determine the optimal constant in the underlying area-versus-displacement problem.

The finite bridge uses standard rational enclosures for \(\pi\) and \(\sqrt3\); these are deliberately coarse, and the resulting margins are much larger than needed.

A contemporaneous or poorly indexed proof of the same all-dimensional branch inequality remains a bibliographic risk.

## References

1. James Dibble and Joseph Hoisington, *Area and antipodal distance in convex hypersurfaces*, arXiv:2604.02667v1, 3 April 2026.
2. James Dibble and Joseph Hoisington, *Area and antipodal distance in convex hypersurfaces*, arXiv:2604.02667v2, 22 April 2026.
