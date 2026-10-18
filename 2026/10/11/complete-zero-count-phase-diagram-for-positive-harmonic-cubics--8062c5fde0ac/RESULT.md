# Complete zero-count phase diagram for positive harmonic cubics

## Finding

For all real parameters \(a,b>0\), consider the complex-valued harmonic polynomial
\[
F_{a,b}(z)=z^3+az+b\overline z-1,\qquad z\in\mathbb C,
\]
and let \(N(a,b)\) denote the number of **distinct complex zeros** of \(F_{a,b}\), including any singular zeros only once. Put
\[
D=4(2b-a)^3-27,\qquad
E=4(a+2b)^2(b-a)-27,\qquad H=3a-2b.
\]
The complete positive-parameter zero-count classification is as follows.

When \(b\le a\):

| Condition | \(N(a,b)\) |
| --- | ---: |
| \(D<0\) | \(3\) |
| \(D=0\) | \(5\) |
| \(D>0\) | \(7\) |

When \(b>a\):

| Condition | \(N(a,b)\) |
| --- | ---: |
| \(D<0\) | \(3\) |
| \(D=0\) and \(H>0\) | \(5\) |
| \(D=0\) and \(H\le0\) | \(3\) |
| \(D>0\) and \(E>0\) | \(5\) |
| \(D>0\), \(E=0\), and \(H>0\) | \(5\) |
| \(D>0\), \(E=0\), and \(H\le0\) | \(3\) |
| \(D>0\), \(E<0\), and \(H>0\) | \(7\) |
| \(D>0\), \(E<0\), and \(H\le0\) | \(3\) |

This exhaustive classification takes only the values \(3,5,7\), including all parameter-transition equalities. The maximum \(7\) is attained on an open set even when \(a>b\), so the orientation-preserving linear part does not prevent maximal valence. In particular, \((a,b)=(3,5/2)\) has seven distinct **regular** zeros: one real zero and six nonreal zeros
\[
z=x\pm i\sqrt{3x^2+\tfrac12},
\qquad x\in\left\{\tfrac12,\frac{-1+\sqrt5}{4},\frac{-1-\sqrt5}{4}\right\}.
\]
The real zero is the unique real solution of \(x^3+\tfrac{11}{2}x=1\). The seven roots are all regular because the harmonic Jacobian is nonzero at each.

## Assumptions and scope

The parameters \(a,b\) are strictly positive real numbers, with no restrictions on size or relative order. Zeros are counted in the whole complex plane, as distinct points, **not** by algebraic multiplicity at singular transition values. A regular zero means a zero with nonzero real Jacobian \(J_F=|F_z|^2-|F_{\bar z}|^2\). The complex constant term is fixed at \(-1\), and the analytic cubic has leading coefficient \(1\).

## Proof

Write \(z=x+iy\), and set \(d=b-a\) and \(S=2b-a\). Direct expansion yields
\[
\operatorname{Re}F=x^3-3xy^2+(a+b)x-1,\qquad
\operatorname{Im}F=y(3x^2-y^2-d).
\]
If \(y=0\), the zero equation becomes \(x^3+(a+b)x-1=0\). This has exactly one real solution \(x_0>0\), since the left side has derivative \(3x^2+a+b>0\), is negative at \(0\), and tends to positive infinity.

If \(y\ne0\), the imaginary part vanishes exactly when \(y^2=3x^2-d>0\). Substitution in the real part, with no division by a possibly vanishing factor, gives the cubic
\[
P(x)=8x^3-2Sx+1=0.
\]
Conversely, **each distinct real zero** \(x\) of \(P\) satisfying \(3x^2-d>0\) produces exactly the two zeros \(x\pm i\sqrt{3x^2-d}\) of \(F\). Distinct real \(x\)'s give disjoint pairs. Therefore
\[
N(a,b)=1+2\#\{x\in\mathbb R:P(x)=0,\ 3x^2>d\},
\]
where the set on the right counts distinct real roots rather than multiplicities.

The usual discriminant of \(P\) is \(64D\). If \(S\le0\), then \(D<0\). If \(S>0\), the positive stationary point of \(P\) is
\[
\xi=\sqrt{S/12},\qquad
P(\xi)=1-\frac{2S^{3/2}}{3\sqrt3}.
\]
Thus \(D<0\) gives exactly one real root, which is negative; \(D=0\) gives one simple negative root and one distinct **double positive** root \(\xi\); and \(D>0\) gives a negative root and two distinct positive roots \(r_1<\xi<r_2\).

For \(d\le0\), the eligibility inequality \(3x^2>d\) holds for all roots because \(P(0)=1\). Counting one, two, or three distinct real roots of \(P\) immediately gives the first table, including \(D=0\).

For \(d>0\), put \(t=\sqrt{d/3}>0\). Since
\[
P(-t)=1+\frac{2(a+2b)}{3}t>0,
\]
the unique negative root lies strictly below \(-t\), so it always contributes one nonreal conjugate pair. A positive root contributes a pair precisely when it exceeds \(t\). Moreover,
\[
t<\xi\ \Longleftrightarrow\ a>2d\ \Longleftrightarrow\ H>0,
\]
and
\[
P(t)=1-\frac{2(a+2b)}{3}\sqrt{d/3};
\qquad
\operatorname{sgn}P(t)=-\operatorname{sgn}E.
\]
The latter sign identity follows by squaring the strictly positive quantity \(\frac{2(a+2b)}3\sqrt{d/3}\): its square minus \(1\) is \(E/27\).

If \(D<0\), there are no positive real roots to count. If \(D=0\), the sole positive root \(\xi\) is eligible exactly when \(t<\xi\), equivalently \(H>0\). For \(D>0\), \(P\) is negative precisely on \((r_1,r_2)\) for positive arguments, and \(r_1<\xi<r_2\). If \(E>0\), then \(P(t)<0\), so \(r_1<t<r_2\): exactly one positive root is eligible. If \(E=0\), then \(t=r_1\) when \(H>0\), leaving \(r_2\) eligible; otherwise \(t=r_2\), leaving none. If \(E<0\), then \(t<r_1\) when \(H>0\), so both are eligible; otherwise \(t>r_2\), so neither is eligible. Combining these counts with the real zero and the always-eligible negative root yields every row of the second table.

For the seven-zero witness, \(P(x)=8x^3-4x+1=(2x-1)(4x^2+2x-1)\). All three roots are distinct and satisfy \(3x^2+1/2>0\). To check regularity, the real Jacobian at each nonreal root reduces to
\[
J_F(x+iy)=2y^2P'(x),
\]
which is nonzero because the roots of \(P\) are simple. At the real root, \(J_F(x_0)=(3x_0^2+a+b)(3x_0^2+a-b)>0\). In particular all seven persist under sufficiently small perturbations of \((a,b)\), establishing the asserted open maximal-valence region. This completes the proof.

## Verification

A standalone standard-library verifier, `verify_cubic.py`, checks the exact radical witness, the discriminant and real-axis collision surfaces, and compares the explicit phase table with an independent stationary-point/bisection root count on 20,000 deterministic parameter samples. Execute `python3 verify_cubic.py` from the folder containing that file. The reported successful checks are reproducible, but finite sampling cannot establish the two-parameter theorem; the exhaustive result follows from the case analysis above.

## Relationship to prior work

Carlson, *Counting Zeros of Complex-Valued Harmonic Functions via Rouché's Theorem* (arXiv:2508.06721, first public August 8, 2025), studies precisely the general family \(z^n+az^k+b\overline z^k-1\). Theorems 1.1 and 1.2 establish \(n+2k\) or \(n\) zeros in **asymptotic, coefficient-separated sectors**, rather than an exact phase table for every positive parameter pair. The present \(n=3,k=1\) classification contains both regimes and the off-diagonal open seven-zero phase, which is not entailed by either cited theorem. This is a deliberately specialized, all-parameter classification, not a general-degree theorem.

Brooks, Jenkins, Liechty and coauthors, *Using Real-Variable Techniques to Study Zeros of Complex-Valued Harmonic Functions* (arXiv:2506.14966), study the **equal-coefficient diagonal** \(a=b\); that special slice is prior work, not claimed independently novel here. Brilleslyper and coauthors (2020) treat the single co-analytic term with analytic linear coefficient absent. Alemu and Geleta (2022) study a different quadrinomial with a different constant-term and exponent structure. Sampson (arXiv:2508.06724) treats a one-parameter harmonic rational family with poles. None of the materially inspected theorems subsumes the two-dimensional classification above.

## Limitations

The theorem is specific to degree three, co-analytic degree one, positive real coefficients and constant term \(-1\). It concerns **distinct** zeros at critical parameters; no general multiplicity theory at singular zeros is claimed. The exact equal-coefficient slice is already covered in the literature; originality concerns the full off-diagonal phase diagram, including its additional collision boundary. Although relevant published primary results were compared, an unindexed equivalent formulation remains possible. The finding has undergone self-review only; no independent audit or external validation is claimed.

## References

1. J. Carlson, *Counting Zeros of Complex-Valued Harmonic Functions via Rouché's Theorem*, arXiv:2508.06721 (initial preprint August 8, 2025; inspected v3, March 10, 2026), Theorems 1.1–1.3, Sections 3–4. https://arxiv.org/abs/2508.06721
2. J. Brooks, M. Jenkins, S. Liechty et al., *Using Real-Variable Techniques to Study Zeros of Complex-Valued Harmonic Functions*, arXiv:2506.14966 (June 17, 2025), Theorem 1 and Section 2. https://arxiv.org/abs/2506.14966
3. M. Brilleslyper, J. Brooks, M. Dorff, R. Howell and L. Schaubroeck, *Zeros of a One-Parameter Family of Harmonic Trinomials*, Proc. Amer. Math. Soc. Ser. B 7 (2020), 82–90, Theorem 1.1. https://doi.org/10.1090/bproc/51
4. O. A. Alemu and H. L. Geleta, *Zeros of a Two-Parameter Family of Harmonic Quadrinomials*, SINET: Ethiopian Journal of Science 45 (2022), 105–114, Sections 3–4. https://doi.org/10.4314/sinet.v45i1.9
5. E. Sampson, *Zeros of Harmonic Functions whose Caustic is a Non-Singular Image of an Epicycloid*, arXiv:2508.06724 (August 8, 2025), Theorem 1. https://arxiv.org/abs/2508.06724
