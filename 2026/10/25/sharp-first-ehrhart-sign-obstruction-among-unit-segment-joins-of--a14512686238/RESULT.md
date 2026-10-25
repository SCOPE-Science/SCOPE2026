# Sharp first Ehrhart-sign obstruction among unit-segment joins of four-dimensional lattice boxes

## Finding
Let \(a_1,a_2,a_3,a_4\) be positive integers, let \(B=\prod_{i=1}^4[0,a_i]\subset\mathbb R^4\), and let \(J=B*[0,1]\) be the standard height-one lattice join in \(\mathbb R^6\). Write \(e_j=e_j(a_1,a_2,a_3,a_4)\) for the elementary symmetric functions, and set
\[
\Delta=e_4-e_3-5e_2-10e_1-45.
\]
The Ehrhart polynomial \(L_J(t)\) has strictly positive coefficients in every degree other than degree one, while
\[
[t]L_J(t)=-\frac{\Delta}{30}.
\]
Thus it has a negative coefficient exactly when \(\Delta>0\); all its coefficients are nonnegative exactly when \(\Delta\le0\), and strictly positive exactly when \(\Delta<0\).

Among all such joins with a negative Ehrhart coefficient, the **least normalized six-dimensional volume** is
\[
\boxed{118272=24\cdot4928}.
\]
It is attained, up to coordinate permutation, **only** for side lengths \((7,8,8,11)\), when \(\Delta=14\) and \([t]L_J(t)=-7/15\). In particular the example with four equal side lengths first becomes negative at common integer length \(9\), whereas the minimum-volume witness has unequal sides.

The sign obstruction has an exact pair-balancing rule. With two other side lengths \(c,d\) fixed and integers \(1\le a<b-1\),
\[
\Delta(a+1,b-1,c,d)-\Delta(a,b,c,d)
=(b-a-1)\big((c-1)(d-1)-6\big).
\]
Thus balancing two sides at fixed sum increases, decreases, or preserves the coefficient obstruction according as \((c-1)(d-1)\) is greater than, less than, or equal to \(6\). This statement concerns \(\Delta\), not an unconditional monotonicity of the normalized volume.

## Assumptions and scope
The ambient lattice of \(J\) is the standard lattice \(\mathbb Z^6\); each side length is a strictly positive integer. The join is
\[
J=\operatorname{conv}\big((B,0,0)\cup(0,0,0,0,[0,1],1)\big),
\]
where the coordinates are four box coordinates, one segment coordinate, and one join-height coordinate. The normalized volume is \(6!\) times Euclidean volume. Ehrhart coefficients refer to the monomial basis, not the binomial or \(h^*\) basis.

The volume optimum is only among this particular family of box-by-unit-segment joins. No minimality among all six-dimensional lattice polytopes, all joins, or joins with arbitrary segment length is claimed.

## Proof
**1. Exact lattice-point formula.** A point of the integer dilation \(tJ\) has integer join height \(h\in\{0,1,\ldots,t\}\). The section at height \(h\) is \((t-h)B\times h[0,1]\). Consequently, for every integer \(t\ge0\),
\[
L_J(t)=\sum_{h=0}^t(h+1)\prod_{i=1}^4\big(a_i(t-h)+1\big)
=\sum_{k=0}^t(t-k+1)\prod_{i=1}^4(a_i k+1).
\]
The product is \(\sum_{j=0}^4e_jk^j\), with \(e_0=1\). Put \(F_j(t)=\sum_{k=0}^t(t-k+1)k^j\). Exact power sums give
\[
\begin{aligned}
F_0&=(t^2+3t+2)/2,\\
F_1&=(t^3+3t^2+2t)/6,\\
F_2&=(t^4+4t^3+5t^2+2t)/12,\\
F_3&=(3t^5+15t^4+25t^3+15t^2+2t)/60,\\
F_4&=(2t^6+12t^5+25t^4+20t^3+3t^2-2t)/60.
\end{aligned}
\]
Hence \(L_J=F_0+e_1F_1+e_2F_2+e_3F_3+e_4F_4\). Since all \(e_j>0\), all monomial coefficients except possibly that of \(t\) are strictly positive. Taking that coefficient gives
\[
[t]L_J=\frac32+\frac{e_1}{3}+\frac{e_2}{6}+\frac{e_3}{30}-\frac{e_4}{30}=-\frac{\Delta}{30}.
\]
This proves the complete coefficient-sign criterion.

**2. Pair balancing.** Fix \(c,d\), and abbreviate the first two variables by \(a,b\). Expanding elementary symmetric functions and grouping the terms containing \(ab\) yields
\[
\Delta(a,b,c,d)=ab(cd-c-d-5)-(a+b)(cd+5c+5d+10)-5cd-10(c+d)-45.
\]
Replacing \((a,b)\) by \((a+1,b-1)\) fixes \(a+b\) and changes \(ab\) by \(b-a-1\). Subtracting proves the asserted exact sign-reversal identity.

**3. Sharp volume cutoff and finite exhaustive proof.** By the standard join-volume identity, or by integrating the product of dilated section volumes,
\[
6!\operatorname{vol}_6(J)=4!\prod_{i=1}^4a_i=24e_4.
\]
If any side is \(1\), with the other lengths denoted \(x,y,z\), direct expansion gives
\[
\Delta(1,x,y,z)=-6(xy+xz+yz)-15(x+y+z)-55<0.
\]
Thus any negative-coefficient witness has \(2\le a\le b\le c\le d\) after permutation. The tuple \((7,8,8,11)\) has product \(4928\) and \(\Delta=14>0\), so a smaller-volume or tied competitor must have \(abcd\le4928\). Necessarily
\[
a^4\le4928,\qquad ab^3\le4928,\qquad abc^2\le4928,\qquad c\le d\le\left\lfloor\frac{4928}{abc}\right\rfloor.
\]
The standalone `verify.py` loops through **every integer quadruple** satisfying these inequalities, with no unspecified cutoff or heuristic pruning. It evaluates the integer \(\Delta\) directly. Exactly \(10618\) sorted quadruples are inspected; the **only** one with \(\Delta>0\) is \((7,8,8,11)\). The preceding inequalities prove exhaustion, so this is a finite complete proof of the minimum and uniqueness, not extrapolation from sampled inputs. Multiplying its product by \(24\) proves the normalized-volume result.

For the equal-side statement, \(\Delta(r,r,r,r)=r^4-4r^3-30r^2-40r-45\). Its coefficients have exactly one sign change, so Descartes' rule gives at most one positive zero; the polynomial is negative at \(8\) and positive at \(9\). Continuity gives a positive zero between them, yielding the claimed sharp integer threshold.

## Verification
Run `python3 verify.py` using Python 3 and its standard library. The program reproduces the bound \(4928\), the count \(10618\), the unique sorted witness, and its obstruction \(14\). It independently recovers the linear coefficient using exact forward differences of the first seven lattice-point counts for eight parameter quadruples (including the minimizer). It checks the balancing identity for \(3402\) integer parameter choices and verifies the seventh difference vanishes in the tested cases. All arithmetic is integral or rational; the exhaustive part uses no floating point. See `VERIFICATION.md` for the division between analytic and finite checks.

## Relationship to prior work
Liu, Tao and Xin (2026), arXiv:2606.18794, prove eventual Ehrhart non-positivity of joins of sufficiently dilated Ehrhart-positive polytopes of dimension at least four. Their general theorem and example using a uniformly dilated four-cube of side length \(100\) supply the motivation and the lattice-join power-sum mechanism. Liu (2026), arXiv:2610.06338, reviews join-preservation results, repeats that example, and gives a different negative example for a pyramid over a four-cube. These published assertions do not state the exact four-side-length positivity region, the unique least-volume negative box-by-unit-interval join, or the complementary-pair sign-reversal rule.

The power-sum formulas are classical and are not claimed as independently new. The claim here is the combined sharp parameter classification, exact extremum and its documented finite-exhaustion proof. A historical-priority risk remains: an older treatment of joins, orthotopes, or generating-function coefficient signs could yield an equivalent criterion or already tabulate the optimum.

## Limitations
No claim is made about polytopes outside the stated box-join family, or about minimal volume among all joins or all lattice polytopes. The decisive finite computation is exhaustive only **after** the proved product bound \(abcd\le4928\); it is not an infinite computer search. There has been no independent external scientific audit. Historical priority is subject to further specialist literature checking, including older survey treatments that were not available in full during this review.

## References
- Feihu Liu, Sihao Tao and Guoce Xin, *Ehrhart Theory of the Join of Two Lattice Polytopes*, arXiv:2606.18794 (first posted 2026-06-17), especially Proposition 1.2 and Section 2. https://arxiv.org/abs/2606.18794
- Feihu Liu, *Ehrhart Properties under Operations on Lattice Polytopes*, arXiv:2610.06338 (2026), especially Sections 3 and 4. https://arxiv.org/abs/2610.06338
- Luis Ferroni and Akihiro Higashitani, *Examples and Counterexamples in Ehrhart Theory*, arXiv:2307.10852 (2023), general survey context. https://arxiv.org/abs/2307.10852
