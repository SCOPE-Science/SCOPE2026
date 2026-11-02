# Sharp universal phaseless polynomial sampling on a parabola

## Finding

Let \(\Gamma=\{t+it^2:t\in\mathbb R\}\) and, for each nonnegative integer \(n\), let \(\mathcal P_n\) be the complex polynomials of degree at most \(n\). The following number of samples is **necessary and sufficient for universal deterministic phaseless recovery**:
\[
\boxed{N_{\mathrm{univ}}(n)=4n+1.}
\]
Precisely: for any \(4n+1\) **distinct** real parameters \(t_j\), equality \(|P(t_j+it_j^2)|=|Q(t_j+it_j^2)|\) for all \(j\), with \(P,Q\in\mathcal P_n\), implies \(P=\lambda Q\) for some \(|\lambda|=1\). Conversely, for each \(n\ge1\), there exist two non-phase-equivalent polynomials \(P,Q\) of degree exactly \(n\) and \(4n\) distinct real parameters on which their magnitudes agree. For \(n=0\), one sample is necessary and sufficient. This conclusion is invariant under Euclidean similarities of the plane, so it holds on any nondegenerate parabola.

A stronger infinite-data rigidity statement is also proved: **no nonconstant rational function has modulus identically one on \(\Gamma\)** (at its defined points). Thus equality of the magnitudes of two nonzero polynomials on any infinite subset of \(\Gamma\) also implies phase equivalence.

## Assumptions and scope

The sample positions are individually labelled and known, and magnitudes are measured exactly. The degrees of the unknown complex polynomials are at most the specified nonnegative integer \(n\); their coefficients and zeros are unrestricted. Parameters are distinct real numbers. “Universal” means recovery for every pair of degree-bounded polynomials and every selection of that many distinct sample positions. This is not a claim of optimality for generically placed samples, stable recovery under measurement noise, or recovery of arbitrary holomorphic functions.

For the sharpness construction it is useful to set \(u=t^2\ge0\) and to introduce the positive quadratic polynomial
\[
B_R(u)=(u-R)^2+u=|\sqrt u+iu-iR|^2,\qquad R>0.
\]

## Proof

**1. Rational phase rigidity.** Put \(z(t)=t+it^2\) and \(z^\sharp(t)=t-it^2\). These polynomial maps have distinct deck involutions:
\[
z(i-t)=z(t),\qquad z^\sharp(-i-t)=z^\sharp(t).
\]
For a polynomial \(P\), write \(P^\sharp(w)=\overline{P(\bar w)}\), obtained by conjugating its coefficients. If \(P,Q\) have equal magnitudes at infinitely many points \(z(t)\) with real \(t\), then the following identity of rational functions of \(t\) holds:
\[
h(t)h^\sharp(t)=1,\quad
h(t)=\frac{P(z(t))}{Q(z(t))},\quad
h^\sharp(t)=\frac{P^\sharp(z^\sharp(t))}{Q^\sharp(z^\sharp(t))}.
\]
Indeed the equality holds away from the finitely many zeros of \(Q(z(t))\), and a nonzero rational function cannot have infinitely many zeros. The first deck involution gives \(h(i-t)=h(t)\). The second, combined with \(h=1/h^\sharp\), gives \(h(-i-t)=h(t)\). Composing them yields
\[
h(t+2i)=h(t).
\]
A rational function with a nonzero additive period is constant: a finite pole would generate infinitely many poles under translations, and a pole-free rational function is a polynomial, whose leading term prevents a nonzero period unless it is constant. Thus \(h=\lambda\in\mathbb C\), with \(|\lambda|=1\) by its values on the real axis. Since \(z\) is nonconstant, \(P=\lambda Q\). If one polynomial is identically zero, the measured equality forces the other to vanish identically as well. The argument also applies to any rational quotient regular at infinitely many points on the parabola.

**2. The universal upper bound.** For \(P,Q\in\mathcal P_n\), the real-valued polynomial
\[
D(t)=|P(t+it^2)|^2-|Q(t+it^2)|^2
\]
is a polynomial of degree at most \(4n\) in the real variable \(t\): write each squared modulus as the product of a degree-at-most-\(2n\) polynomial in \(t\) with its conjugate-coefficient polynomial. If \(D\) vanishes at \(4n+1\) distinct parameters then \(D\equiv0\). By Step 1 the two polynomials differ only by global unimodular phase. This includes \(n=0\).

**3. All-degree sharpness.** We construct, for every \(n\ge1\), polynomials \(P_n,Q_n\), each of degree exactly \(n\), such that
\[
\Phi_n(u)=\frac{|P_n(\sqrt u+iu)|^2}{|Q_n(\sqrt u+iu)|^2}
\]
has exactly \(2n\) distinct, positive crossings of the level \(1\) and \(\lim_{u\to\infty}\Phi_n(u)=A_n>1\). The denominators below are strictly positive for \(u\ge0\).

Start with
\[
P_1(z)=z-100i,\qquad Q_1(z)=\tfrac14(z-50i).
\]
Then \(\Phi_1(u)=16B_{100}(u)/B_{50}(u)\); its values at \(u=0\), \(u=100\), and infinity lie respectively above, below, and above \(1\). Therefore it has at least two distinct positive crossings; as its difference of numerator and denominator is quadratic, it has exactly two, each simple. Also \(A_1=16>1\).

Inductively assume the assertions at degree \(n\). Choose any real \(\alpha\) with \(A_n^{-1/2}<\alpha<1\), and for \(R>0\) set
\[
P_{n+1,R}(z)=P_n(z)(z-iR),\qquad
Q_{n+1,R}(z)=\alpha^{-1}Q_n(z)(z-i\alpha R).
\]
Their ratio obeys
\[
\Phi_{n+1,R}(u)=\Phi_n(u)\,\frac{\alpha^2 B_R(u)}{B_{\alpha R}(u)}.
\]
For every fixed \(u\ge0\), the final factor tends to \(1\) as \(R\to\infty\), preserving, for sufficiently large \(R\), the alternating strict signs of \(\Phi_n(u)-1\) at a finite set of witness points bracketing its \(2n\) simple positive roots. Choose the last witness point after the final root, where \(\Phi_n>1\). Moreover,
\[
\Phi_{n+1,R}(R)
=\Phi_n(R)\,\frac{\alpha^2 R}{(1-\alpha)^2R^2+R}\longrightarrow0,
\]
whereas \(\lim_{u\to\infty}\Phi_{n+1,R}(u)=\alpha^2 A_n>1\). Taking \(R\) larger than the final witness point, we therefore obtain two *additional* positive crossings: one between that witness and \(R\), and one beyond \(R\). Thus there are at least \(2n+2\) distinct positive roots of
\[
|P_{n+1,R}(\sqrt u+iu)|^2-|Q_{n+1,R}(\sqrt u+iu)|^2=0.
\]
The left side is a polynomial in \(u\) of degree at most \(2n+2\) because every factor of either modulus squared equals a quadratic \(B_\beta(u)\). Hence there are exactly \(2n+2\) distinct positive roots, all simple. The nonzero leading coefficient follows from the new asymptotic ratio \(\alpha^2 A_n>1\). This closes the induction.

Each positive root \(u\) gives the two distinct real parameters \(t=\pm\sqrt u\), so the constructed pair agrees in magnitude at exactly \(4n\) distinct parabola points. Since their asymptotic ratio exceeds \(1\), they are not constant-phase multiples. Thus even \(4n\) (and hence any smaller number of) *arbitrarily selected* measurement points cannot guarantee recovery. Combined with Step 2, this proves the sharp universal threshold \(4n+1\).

Any Euclidean similarity sends a nondegenerate parabola to a translate, rotation, and dilation of the standard model; precomposition with its inverse preserves polynomial degree and phase equivalence, transferring both implications.

## Verification

The standalone script `verify.py` uses exact rational arithmetic. It checks the two deck identities symbolically by coefficient expansion; the base construction; and, for degrees \(1\) through \(4\), explicit large-separated imaginary-root constructions with alternating exact rational witnesses and leading coefficients of the predicted degrees. These are supplementary checks, not substitutes for the all-degree induction and rational-periodicity proof. Reproduce with `python3 verify.py` in a standard Python 3 installation; no third-party packages are needed.

## Relationship to prior work

Chalendar and Partington, *Phase retrieval on circles and lines* (arXiv:2403.16255, first submitted March 24, 2024), examine analytic phase uniqueness on unions of straight lines and circles, plus finite samples with additional full-circle data. Their stated results do not give universal sharp \(4n+1\)-sample recovery on **one parabola**. Liehr, *Arithmetic progressions and holomorphic phase retrieval* (arXiv:2308.05722, first submitted August 2023), uses a periodicity argument for sets comprising multiple parallel lines, a related ingredient but distinct sampling geometry. Orevkov and Pakovich, *On intersection of lemniscates of rational functions* (arXiv:2309.04983, first submitted September 2023), establish intersection and irreducibility results for rational lemniscates. Their lemniscate-intersection theorem is not a finite-sample sharpness theorem for an arbitrary fixed parabola, and their constructions do not provide the nested all-degree crossing family used here.

Related polynomial phase-retrieval results on ellipses, hyperbolas, and pairs of lines involve different reflection groups and do not directly provide the sharp maximal number of magnitude coincidences on a parabola. The novelty assessment is provisional: an uncatalogued algebraic-geometry result on real intersections of generalized lemniscates and conics could still dominate the sharpness statement.

## Limitations

The construction proving necessity depends on specially chosen sample locations; generic placements might require fewer observations. No noise-conditioning or stable inverse estimate is asserted. The assertion is for polynomials (and rational-quotient rigidity), not arbitrary entire or meromorphic functions. Independent external mathematical audit and historical-priority verification have not been performed.

## References

1. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (v1: 2024-03-24). https://arxiv.org/abs/2403.16255
2. L. Liehr, *Arithmetic progressions and holomorphic phase retrieval*, arXiv:2308.05722 (2023). https://arxiv.org/abs/2308.05722
3. S. Orevkov and F. Pakovich, *On intersection of lemniscates of rational functions*, arXiv:2309.04983 (v1: 2023-09-10). https://arxiv.org/abs/2309.04983
