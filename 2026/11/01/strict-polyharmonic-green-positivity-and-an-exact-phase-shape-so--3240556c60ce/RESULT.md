# Strict polyharmonic Green positivity and an exact phase–shape Sobolev deficit

## Finding

For every pair of positive integers \(\alpha,d\), let \(D:\mathbb C^d\to\mathbb C^{d+\alpha}\) be the zero-extended backward-difference operator of order \(\alpha\), \(Q=D^*D\), and \(K=Q^{-1}\). **Every entry of the real matrix \(K\) is strictly positive.** This gives an exact phase-sensitive version of the sharp finite discrete Sobolev inequality, including every equality case.

For unit complex coordinates \(s=(s_j)_{j=1}^d\), define
\[
 C^2=\frac{\binom{d+2\alpha}{2\alpha+1}}{\binom{2\alpha}{\alpha}},\qquad
 G(s)=\sum_{1\le j<k\le d}K_{jk}|s_j-s_k|^2.
\]
For any \(a\in\mathbb C^d\), choose \(s_j=a_j/|a_j|\) whenever \(a_j\ne0\), and arbitrary unit complex \(s_j\) otherwise. Then the following **exact identity** holds:
\[
\boxed{\ C^2\|Da\|_2^2-\|a\|_1^2
= G(s)\|Da\|_2^2+(s^*Ks)\min_{c\in\mathbb C}\|D(a-cKs)\|_2^2.\ }
\]
Moreover, for each such \(s\),
\[
\sup_{a\ne0}\frac{|s^*a|^2}{\|Da\|_2^2}=s^*Ks=C^2-G(s),
\]
attained by \(a=Ks\). The nonzero equality cases in the sharp Sobolev inequality are **exactly** the complex scalar multiples of the strictly positive vector
\[
 v_j=\binom{j+\alpha-1}{\alpha}\binom{d+\alpha-j}{\alpha},\qquad 1\le j\le d.
\]
For \(d=1\), the phase sum is empty, and the same characterization holds.

## Assumptions and scope

The Hilbert space is \(\mathbb C^d\) with the usual inner product \(\langle x,y\rangle=x^*y\). The zero extension is applied before taking differences. Precisely, for \(1\le r\le d+\alpha\) and \(1\le j\le d\),
\[
D_{rj}=(-1)^{r-j}\binom{\alpha}{r-j},
\]
where the binomial coefficient is zero unless \(0\le r-j\le\alpha\). Thus \(Da\) is the full finitely supported backward difference including both boundary layers. The index range is all integers \(\alpha,d\ge1\); coefficients and extremizers may be complex. The minimization over \(c\) is an ordinary finite-dimensional complex least-squares minimum.

## Proof

**Step 1: a positive inverse for every order.** Let \(J_m\) be diagonal with diagonal entries \((-1)^j\), \(1\le j\le m\), and set \(E=J_{d+\alpha}DJ_d\). Then \(E_{rj}=\binom{\alpha}{r-j}\ge0\). Write \(E\) as a product of \(\alpha\) rectangular elementary matrices \(H^{(n)}\), each of size \(n+1\) by \(n\) and satisfying \(H^{(n)}_{rj}=1\) for \(r=j\) or \(r=j+1\), and zero otherwise. Every minor of such a lower bidiagonal matrix is nonnegative; hence Cauchy–Binet shows that every minor of \(E\) is nonnegative. Therefore \(B=E^{\mathsf T}E=J_dQJ_d\) is totally nonnegative and positive definite.

We prove every complementary \((d-1)\)-minor of \(B\) is strictly positive. The case \(d=1\) is immediate. For \(d\ge2\), take \(I=\{1,\ldots,d\}\setminus\{i\}\) and \(J=\{1,\ldots,d\}\setminus\{j\}\). If \(i\le j\), select the row set \(R=I\) in the Cauchy–Binet expansion of \(\det B_{I,J}\). The factor \(\det E_{I,I}=1\), because the first \(d\) rows of \(E\) are lower triangular with diagonal one. The other factor \(\det E_{I,J}\ge1\): in the product representation for \(E\), first choose the intermediate rows \(I\) in \(H^{(d)}\), then retain those rows in all subsequent elementary factors. The first selected minor, with row \(i\) deleted and column \(j\) deleted, is one (it is a complementary minor of the lower bidiagonal \(d\)-by-\(d\) block), and each subsequent principal selected minor is one. All other Cauchy–Binet terms are nonnegative. If \(i>j\), interchange \(I,J\) and use symmetry. Thus \(\det B_{I,J}>0\) for every pair, including the principal case. Cofactor inversion now gives
\[
K_{ij}=\bigl(J_dB^{-1}J_d\bigr)_{ij}
=\frac{\det B_{\widehat j,\widehat i}}{\det B}>0.
\]
The signs cancel exactly; no entrywise-positivity assumption is used.

**Step 2: the exact constant.** Define \(v_j\) as above, and extend the product defining \(v_j\) polynomially to all integer arguments. That polynomial vanishes at \(j=-\alpha+1,\ldots,0\) and at \(j=d+1,\ldots,d+\alpha\), so applying \(Q\) to the finite vector agrees with the centered \(2\alpha\)-th difference of the polynomial. Its leading coefficient is \((-1)^\alpha/(\alpha!)^2\), and therefore its \(2\alpha\)-th forward difference equals \((-1)^\alpha\binom{2\alpha}{\alpha}\). Since
\[
Q_{ij}=(-1)^{i-j}\binom{2\alpha}{\alpha+i-j},
\]
we obtain \(Qv=\binom{2\alpha}{\alpha}\mathbf1\). Consequently \(K\mathbf1=v/\binom{2\alpha}{\alpha}\). Vandermonde convolution gives
\[
\sum_{j=1}^dv_j=\binom{d+2\alpha}{2\alpha+1};
\]
hence \(\mathbf1^*K\mathbf1=C^2\). This independently reproduces the exact sharp constant already proved in the cited discrete Sobolev theorem.

**Step 3: exact support and deficit identities.** Use the energy inner product \(\langle x,y\rangle_Q=x^*Qy\). The Riesz representative of the functional \(a\mapsto s^*a\) is \(Ks\). Cauchy–Schwarz, with equality at \(a=Ks\), gives the asserted support supremum. Because \(K\) is real symmetric and each \(|s_j|=1\),
\[
\mathbf1^*K\mathbf1-s^*Ks
=\sum_{j<k}K_{jk}|s_j-s_k|^2=G(s).
\]
The energy-orthogonal projection of \(a\) onto the line \(\mathbb C Ks\) satisfies
\[
\min_c\|D(a-cKs)\|_2^2
=\|Da\|_2^2-\frac{|s^*a|^2}{s^*Ks}.
\]
Since \(s^*a=\|a\|_1\) by the prescribed phases, substituting this and \(s^*Ks=C^2-G(s)\) gives the boxed equality without remainder.

Both defect terms are nonnegative. Strict positivity \(K_{jk}>0\) forces \(G(s)=0\) only when all \(s_j\) are equal (vacuously true for \(d=1\)). Equality in the second term then forces \(a=cKs=c\,e^{i\theta}K\mathbf1\), a complex multiple of \(v\). Conversely every such multiple attains equality. For zero \(a\), both sides of the identity vanish.

## Verification

The reproducible companion program `verify.py` checks exact rational Gram inverses, strict positivity, the polynomial Landau identity, and the sharp constant for orders \(1\le\alpha\le4\) and lengths \(1\le d\le8\). It additionally tests the full complex phase–shape identity for four input families per pair, including zero coordinates, and reports 1,120 supplementary assertions passed. Run `python3 verify.py` with Python 3 standard library. The symbolic argument above, rather than these finite cases, proves the claim for all positive integers.

## Relationship to prior work

Hindov–Nitzan–Olsen–Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences* (arXiv:2610.19010v1, first posted 2026-10-13), establishes the exact best constant and constructs Landau-type equality examples. In its Theorem 1 and Section 4.2 it does not classify **all complex equality cases**, prove **strict entrywise positivity of the inverse polyharmonic Gram matrix**, or give an **exact two-component phase and shape deficit**. The present result credits that theorem's constant and strengthens the stability and rigidity description at fixed order and length. Its proof instead uses a strictly positive Green matrix derived through total nonnegativity of binomial convolution.

The earlier continuous-space analog by Hindov–Lokharu, *On a class of sharp Sobolev type estimates with weights* (arXiv:2605.25637v1), concerns continuous functions and includes uniqueness statements there, not this discrete all-order phase kernel. Total positivity of elementary binomial-convolution matrices is classical and is explicitly used as a proof tool, rather than claimed as a new fact.

## Limitations

This is an **exact identity** rather than an all-parameter lower bound for distance to the extremizer manifold with a dimension-independent coefficient: the weights \(K_{jk}\) depend on \(\alpha,d\). No uniform-in-dimension spectral gap is claimed. The result does not extend automatically to alternative boundary conditions, other \(\ell^p\) derivative energies, or noninteger differences. Publication-priority risk remains for a differently phrased older theorem on discrete polyharmonic Green functions. The numerical checks are finite and are not a proof of the unrestricted theorem. No independent scientific audit is claimed.

## References

1. Raul Hindov, Shahaf Nitzan, Jan-Fredrik Olsen and Eskil Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences*, arXiv:2610.19010v1 (2026-10-13), https://arxiv.org/html/2610.19010v1 . Primary full text examined, especially Theorem 1 and Sections 3–4.
2. Raul Hindov and Evgeniy Lokharu, *On a class of sharp Sobolev type estimates with weights*, arXiv:2605.25637v1 (2026-05-25), https://arxiv.org/abs/2605.25637 . Continuous analogous context.
3. Classical Cauchy–Binet and cofactor identities and total nonnegativity of bidiagonal matrices are used as standard matrix results.
