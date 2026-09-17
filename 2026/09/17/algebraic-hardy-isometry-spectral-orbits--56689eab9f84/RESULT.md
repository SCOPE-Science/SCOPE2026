# Spectral-orbit divisibility for algebraic isometries of vector Hardy spaces

## Main theorem

Let \(1\le p<\infty\), \(p\ne2\), let \(\mathcal K\ne\{0\}\) be a complex
Hilbert space, and let
\[
T:H^p(\mathcal K)\longrightarrow H^p(\mathcal K)
\]
be a surjective linear isometry which is algebraic.  Write \(q_T\) for its
monic minimal polynomial and \(d=\deg q_T\).

By Lin's representation theorem there are a disk automorphism
\(\varphi\in\operatorname{Aut}(\mathbb D)\), a unitary \(U\) on
\(\mathcal K\), and a nonvanishing analytic scalar weight \(a\) (in Lin's
normalization \(a=(\varphi')^{1/p}\)) such that
\[
(Tf)(z)=a(z)\,U f(\varphi(z)).
\]

Then the following hold.

1. The roots of \(q_T\) are distinct and unimodular.  They are precisely
   the spectrum of \(T\), and every one is an eigenvalue.
2. The automorphism \(\varphi\) has finite order \(m\), and
   \[
   \boxed{m\mid d.}
   \]
3. If \(m>1\) and \(\omega\) is a primitive \(m\)-th root of unity for
   which \(\varphi\) is conjugate to \(z\mapsto\omega z\), then
   \[
   \omega\,\sigma(T)=\sigma(T).
   \]
   Thus the spectrum is a disjoint union of full \(\omega\)-orbits.
4. Consequently
   \[
   \boxed{
   q_T(t)=\prod_{j=1}^{d/m}(t^m-\alpha_j)
   }
   \]
   for distinct unimodular constants \(\alpha_j\).  Equivalently,
   \(q_T(\omega t)=q_T(t)\).

The divisibility is sharp: for every pair \(m\mid d\) there is an algebraic
surjective isometry of some \(H^p(\mathbb C^{d/m})\) whose disk symbol has
exact order \(m\) and whose minimal polynomial is \(t^d-1\).

## Proof

### 1. Algebraic isometries are semisimple on the unit circle

Since \(T\) is an isometry, every eigenvalue \(\lambda\) satisfies
\(|\lambda|=1\).  Every root of the minimal polynomial of an algebraic
operator is an eigenvalue.

No root can occur with multiplicity greater than one.  Otherwise there are
vectors \(x\ne0\) and \(y\) with
\[
(T-\lambda I)x=0,\qquad (T-\lambda I)y=x.
\]
Then
\[
T^n y=\lambda^n y+n\lambda^{n-1}x,
\]
so
\[
\|T^n y\|\ge n\|x\|-\|y\|,
\]
contradicting \(\|T^n y\|=\|y\|\).  Hence \(q_T\) is square-free.  It follows
that its \(d\) roots are exactly \(\sigma(T)\), all are unimodular, and all
are eigenvalues.

### 2. Algebraicity forces the disk symbol to be periodic

Write
\[
q_T(t)=\sum_{k=0}^d c_k t^k,\qquad c_d=1.
\]
Iterating the weighted-composition representation gives
\[
(T^k f)(z)=a_k(z)\,U^k f(\varphi^k(z)),
\]
where every \(a_k(z)\) is nonzero.

Suppose that \(\varphi^r\ne\operatorname{id}\) for every
\(1\le r\le d\).  For each such \(r\), the fixed-point set of
\(\varphi^r\) in \(\mathbb D\) has at most one point.  We may therefore
choose \(z_0\in\mathbb D\) such that
\[
z_0,\varphi(z_0),\ldots,\varphi^d(z_0)
\]
are pairwise distinct.  Choose a scalar polynomial \(h\) satisfying
\[
h(\varphi^d(z_0))=1,\qquad
h(\varphi^k(z_0))=0\quad(0\le k<d),
\]
and choose \(0\ne v\in\mathcal K\).  For \(f=hv\),
evaluation of \(q_T(T)f=0\) at \(z_0\) leaves only its leading term:
\[
0=(q_T(T)f)(z_0)=a_d(z_0)U^d v,
\]
a contradiction.  Hence \(\varphi^r=\operatorname{id}\) for some
\(1\le r\le d\).  If \(m\) is its exact order, then \(m\le d\).

### 3. The symbol order produces spectral root-of-unity orbits

Assume \(m>1\).  A finite-order disk automorphism is elliptic, hence there
is \(\chi\in\operatorname{Aut}(\mathbb D)\) and a primitive \(m\)-th root
\(\omega\) such that
\[
\chi\circ\varphi=\omega\chi.
\]
Let \(M_\chi\) denote multiplication by \(\chi\) on \(H^p(\mathcal K)\).
It is bounded and injective.  Since \(\chi\) is scalar-valued,
\[
T M_\chi=\omega M_\chi T.
\]
Therefore, if \(Tx=\lambda x\), then
\[
T(M_\chi x)=\omega\lambda\,M_\chi x,
\]
and \(M_\chi x\ne0\).  Every spectral point of the algebraic operator \(T\)
is an eigenvalue, so
\[
\lambda\in\sigma(T)\quad\Longrightarrow\quad
\omega\lambda\in\sigma(T).
\]
Thus \(\sigma(T)\) is partitioned into \(\omega\)-orbits.  Each orbit has
exactly \(m\) elements because all spectral values are nonzero and
\(\omega\) has exact order \(m\).  Since \(q_T\) is square-free,
\(d=|\sigma(T)|\), and therefore \(m\mid d\).

Choosing one representative \(\rho_j\) from each orbit gives
\[
\prod_{k=0}^{m-1}(t-\rho_j\omega^k)=t^m-\rho_j^m.
\]
Different orbits give different values of \(\rho_j^m\), proving the
factorization with \(\alpha_j=\rho_j^m\).

For \(m=1\), the conclusions are immediate.

### 4. Sharpness for every divisor

Let \(m\mid d\) and put \(s=d/m\).  Let \(\eta\) be a primitive \(d\)-th
root of unity and set \(\omega=\eta^s\), which has exact order \(m\).
On \(\mathcal K=\mathbb C^s\), with standard basis
\(e_0,\ldots,e_{s-1}\), define the unitary
\[
A e_r=\eta^r e_r.
\]
Then
\[
(Tf)(z)=A f(\omega z)
\]
is a surjective isometry of \(H^p(\mathbb C^s)\).  Its symbol has exact
order \(m\).  Moreover
\[
T(z^k e_r)=\eta^{r+sk}z^k e_r.
\]
For \(0\le r<s\) and \(0\le k<m\), the exponents \(r+sk\) run through
\(0,\ldots,d-1\), so every \(d\)-th root of unity is an eigenvalue.
Also \(T^d=I\).  Hence the minimal polynomial is exactly
\[
q_T(t)=t^d-1.
\]

## Consequence for generalized tri-circular projections

Suppose \(P_0,P_1,P_2\) are nonzero pairwise annihilating projections on
\(H^p(\mathcal K)\) with \(P_0+P_1+P_2=I\), and
\[
T=P_0+\lambda_1P_1+\lambda_2P_2
\]
is a surjective isometry, where \(1,\lambda_1,\lambda_2\) are distinct
unimodular scalars.  Then all three scalars are eigenvalues and
\[
q_T(t)=(t-1)(t-\lambda_1)(t-\lambda_2),
\]
so \(d=3\).  The theorem implies that the disk-symbol order divides \(3\).
Therefore the symbol is either the identity or has exact order \(3\);
an exact order-\(2\) symbol is impossible.

In the nonidentity case, spectral invariance under a primitive cube root
\(\omega\), together with \(1\in\sigma(T)\), forces
\[
\{1,\lambda_1,\lambda_2\}=\{1,\omega,\omega^2\},
\]
and hence
\[
T^3=I.
\]

This gives a short spectral explanation for the cubic root-of-unity
phenomenon.  In particular, Theorem 3.1 of Kumar--Kumar--Abu Baker
(arXiv:2609.10718, 2026) states a three-case classification on
\(H^p(\mathcal K)\) with identity, order-\(2\), and order-\(3\) disk-symbol
alternatives.  Under the nonzero three-spectral-subspace hypotheses above,
the divisibility theorem shows that the order-\(2\) alternative is vacuous.

## Relation to prior literature

Lin's 1991 theorem supplies the weighted-composition representation of
surjective isometries of \(H^p(\mathcal K)\), \(p\ne2\).

Kumar, Kumar and Abu Baker (2026) study generalized tri-circular
projections on \(H^p(\mathcal K)\), \(H^\infty(E)\), and vector-valued
little Bloch spaces.  Their \(H^p(\mathcal K)\) theorem is cubic in nature;
the result here instead treats an arbitrary algebraic minimal polynomial
and identifies the exact divisor relation between its degree and the order
of the disk symbol.

Dutta and Abubaker (2012) prove root-of-unity conclusions for generalized
\(n\)-circular projections on Banach spaces under a hypothesis that
generalized bi-circular projections are averages of the identity with
isometric reflections.  The present argument uses the analytic
weighted-composition structure of \(H^p(\mathcal K)\), does not require
that global Banach-space hypothesis, and applies to arbitrary algebraic
surjective isometries rather than only a prescribed circular projection
decomposition.

Jiang, Han and Zhou (2020) characterize algebraic weighted composition
operators of degree at most two in a scalar \(H^2\) complex-symmetric
setting.  That result has different hypotheses and does not supply the
arbitrary-degree vector-valued divisor law above.

## Limitations and originality risk

Originality is claimed only to the best of our knowledge.

Two especially relevant older papers could not be inspected in full:
Botelho--Jamison (2015), *Algebraic and topological properties of the group
of isometries on classes of vector valued function spaces*, whose abstract
indicates a study of algebraic properties of surjective isometry groups on
vector-valued analytic spaces; and Botelho--Ilišević (2021), *On
isometries with finite spectrum*, whose abstract announces necessary
conditions for finite spectra of isometries on complex Banach spaces.
Their available abstracts do not state the \(H^p(\mathcal K)\)
disk-symbol divisibility or spectral-orbit factorization proved here, but
an equivalent result in the uninspected full text remains the principal
originality risk.

The proof uses the special weighted-composition representation of
surjective \(H^p(\mathcal K)\) isometries.  It is not asserted for arbitrary
Banach spaces or arbitrary weighted composition operators.

## References

1. P.-K. Lin, *The isometries of \(H^p(K)\)*, Journal of the Australian
   Mathematical Society 50 (1991), 23--33.
   https://doi.org/10.1017/S1446788700032523
2. H. Kumar, H. Kumar and A. B. Abu Baker, *Generalized tri-circular
   projections on some vector-valued spaces of analytic functions*,
   arXiv:2609.10718 (2026). https://arxiv.org/abs/2609.10718
3. S. Dutta and A. B. Abubaker, *Generalized 3-circular projections in
   some Banach spaces*, arXiv:1204.2360 (2012).
   https://arxiv.org/abs/1204.2360
4. F. Botelho and J. Jamison, *Generalized bi-circular projections on
   spaces of analytic functions*, Acta Scientiarum Mathematicarum 75
   (2009), 527--546.
   https://digitalcommons.memphis.edu/facpubs/4766/
5. F. Botelho and J. Jamison, *Algebraic and topological properties of the
   group of isometries on classes of vector valued function spaces*,
   Banach Journal of Mathematical Analysis 9 (2015), 221--233.
   https://doi.org/10.15352/bjma/09-4-11
6. F. Botelho and D. Ilišević, *On isometries with finite spectrum*,
   Journal of Operator Theory 86 (2021), 255--273.
   https://doi.org/10.7900/jot.2020apr11.2270
7. C. Jiang, S.-A. Han and Z.-H. Zhou, *Complex symmetric weighted
   composition operators on the Hardy space*, Czechoslovak Mathematical
   Journal 70 (2020), 817--831.
   https://doi.org/10.21136/CMJ.2020.0555-18
