# Eight-state barrier for Markov positivity of the [2/2] Padé map

## Result

Work in the row-generator convention for a finite continuous-time Markov chain:
\(Q_{ij}\ge 0\) for \(i\ne j\) and \(Q\mathbf 1=0\). Consider the diagonal \([2/2]\) Padé approximation to the exponential
\[
r(z)=\frac{1+z/2+z^2/12}{1-z/2+z^2/12}
=\frac{12+6z+z^2}{12-6z+z^2}.
\]
For a linear system this is also the end-step stability map of the two-stage, fourth-order Gauss--Legendre Runge--Kutta method.

### Theorem 1: eight states are minimal for arbitrarily-small loss of Markov positivity

1. For every CTMC generator \(Q\in\mathbb R^{n\times n}\) with \(n\le 7\), there is an \(\varepsilon_Q>0\) such that
\[
r(hQ)\ge 0\qquad\text{entrywise for every }0\le h\le \varepsilon_Q.
\]

2. In dimension \(8\) this is false. Let
\[
Q_*=\begin{pmatrix}
-1&1\\
&-1&1\\
&&-1&1\\
&&&-1&1\\
&&&&-1&1\\
&&&&&-1&1\\
&&&&&&-1&1\\
&&&&&&&0
\end{pmatrix},
\]
with omitted entries zero. This is the unit-rate pure-birth chain with state \(8\) absorbing. There is a constant
\[
h_0=0.596640561867168457\ldots
\]
such that \(r(hQ_*)\) has a negative entry for every \(0<h<h_0\).

Hence dimension \(8\) is the smallest finite state-space size for which the \([2/2]\) Padé/Gauss--Legendre end-step map can fail positivity for arbitrarily small positive steps while preserving total mass exactly.

### Theorem 2: exact stochasticity window for the eight-state witness

Let \(h_0\) be the unique positive root of
\[
p(h)=7h^6+126h^5+840h^4+2520h^3+3024h^2-1728.
\]
Then
\[
\boxed{\quad r(hQ_*)\text{ is row-stochastic }
\iff h=0\ \text{or}\ h_0\le h\le 2\sqrt 3.\quad}
\]
Thus the method is non-stochastic for all sufficiently small positive steps, becomes stochastic on a nonempty intermediate interval, and loses positivity again for \(h>2\sqrt3\).

For a pure-birth rate \(\lambda>0\), replace \(h\) by the dimensionless product \(x=\lambda h\).

## Proof

### 1. The map is mass-conserving whenever it is defined

The denominator polynomial \(1-z/2+z^2/12\) has roots \(3\pm i\sqrt3\), both in the open right half-plane. Every eigenvalue of a finite CTMC generator has nonpositive real part, so the denominator matrix is nonsingular for every \(h\ge0\).

Since \(Q\mathbf1=0\) and \(r(0)=1\),
\[
r(hQ)\mathbf1=\mathbf1.
\]
Therefore any failure below is a failure of entrywise nonnegativity, not of mass conservation.

### 2. Maclaurin coefficients and the lower-dimensional obstruction

The expansion at the origin is
\[
r(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{24}
+\frac{z^5}{144}+0\,z^6-\frac{z^7}{1728}+O(z^8).
\]
Write these coefficients as \(a_k\).

Fix distinct states \(i,j\), and let \(\ell\) be the length of a shortest directed path from \(i\) to \(j\) in the graph of positive off-diagonal rates. If there is no path, then \((Q^k)_{ij}=0\) for every \(k\) and hence \(r(hQ)_{ij}=0\). If a path exists, it can be chosen simple, so \(\ell\le n-1\), and
\[
(Q^k)_{ij}=0\quad(k<\ell),\qquad (Q^\ell)_{ij}>0.
\]

If \(n\le6\), then \(\ell\le5\), and \(a_\ell>0\). Thus
\[
r(hQ)_{ij}=a_\ell h^\ell(Q^\ell)_{ij}+O(h^{\ell+1})>0
\]
for all sufficiently small \(h>0\).

The only extra case for \(n=7\) is \(\ell=6\). Here \(a_6=0\). Any nonzero term contributing to \((Q^7)_{ij}\) must contain at least six off-diagonal transitions. Seven off-diagonal transitions are impossible: a seven-edge walk on seven vertices repeats a vertex, and deleting the resulting directed cycle would give an \(i\)-to-\(j\) walk of length at most five, contradicting \(\ell=6\). Hence every nonzero term contributing to \((Q^7)_{ij}\) has exactly six positive off-diagonal factors and one negative diagonal factor. At least one such term exists by inserting a diagonal stay along a shortest path, so
\[
(Q^7)_{ij}<0.
\]
Since \(a_7=-1/1728<0\),
\[
r(hQ)_{ij}=a_7h^7(Q^7)_{ij}+O(h^8)>0
\]
for all sufficiently small \(h>0\).

Diagonal entries equal \(1+O(h)\) and are therefore positive for sufficiently small \(h\). Taking the minimum of finitely many entrywise neighborhoods proves Theorem 1 for \(n\le7\).

### 3. Exact formulas for the eight-state pure-birth chain

Let
\[
D(h)=h^2+6h+12.
\]
The transient \(7\times7\) block of \(Q_*\) is \(-I+N\), where \(N\) is the nilpotent superdiagonal shift. Functional calculus for this Jordan block gives, for \(1\le i\le j\le7\) and \(d=j-i\),
\[
[r(hQ_*)]_{ij}
=\frac{h^d}{d!}\,r^{(d)}(-h).
\]
The absorbing-column entry is the complementary Taylor remainder required by the row sum one condition.

For the first row and absorbing state,
\[
[r(hQ_*)]_{1,8}
=
\frac{12h^7\,p(h)}{D(h)^7}.
\]
The polynomial \(p\) satisfies
\[
p(0)=-1728,\qquad
p'(h)=42h^5+630h^4+3360h^3+7560h^2+6048h>0
\quad(h>0).
\]
Therefore \(p\) has exactly one positive root \(h_0\), and this entry is negative precisely on \(0<h<h_0\). This proves the eight-state upper bound in Theorem 1.

For the nearest transient neighbor,
\[
[r(hQ_*)]_{1,2}
=h\,r'(-h)
=\frac{12h(12-h^2)}{D(h)^2},
\]
so positivity is impossible for \(h>2\sqrt3\).

It remains to check the interval \(h_0\le h\le2\sqrt3\). On this interval,
\[
r(-h)>0,\qquad r'(-h)\ge0,
\]
and direct differentiation gives \(r^{(d)}(-h)>0\) for \(d=2,\ldots,6\). For example,
\[
r''(-h)=\frac{24(72+36h-h^3)}{D(h)^3}>0,
\]
and the remaining numerators are positive there using \(h^2\le12\); the compact verification artifact checks the exact symbolic formulas.

The absorbing-column remainders after retaining derivatives \(d=0,\ldots,m\), for \(m=0,\ldots,5\), factor respectively as
\[
\frac{12h}{D},
\quad
\frac{24h^2(h+3)}{D^2},
\quad
\frac{36h^3(h+2)(h+4)}{D^3},
\]
\[
\frac{48h^4(h+3)(h^2+6h+6)}{D^4},
\quad
\frac{12h^5(5h^4+60h^3+240h^2+360h+144)}{D^5},
\]
\[
\frac{72h^7(h+2)(h+3)(h+4)(h+6)}{D^6},
\]
all strictly positive for \(h>0\). The remaining first-row remainder is exactly \(12h^7p(h)/D^7\), nonnegative precisely for \(h\ge h_0\). Hence every entry is nonnegative on \([h_0,2\sqrt3]\), completing Theorem 2.

## Context and direction of improvement

Zappavigna, Colaneri, Kirkland and Shorten (2012) already showed that diagonal Padé discretization can lose positivity for arbitrarily small steps. Their central \([2/2]\) example uses the same first negative Padé-series coefficient with an \(8\times8\) nilpotent nonnegative shift, and then a Hurwitz Metzler shift of that matrix. Those matrices do not satisfy the conservative CTMC constraint \(Q\mathbf1=0\).

The present result isolates what conservation changes. It gives a genuine finite-state Markov generator, proves that eight states are not merely sufficient but minimal for arbitrarily-small failure, and determines the complete positivity/stochasticity set of the explicit eight-state pure-birth witness.

Classical absolute-monotonicity theory already predicts that the fourth-order \((2,2)\) rational approximant has no positive uniform radius over unrestricted monotonicity problems. Lóczi and Ketcheson (2014), summarizing and extending earlier work of van de Griend and Kraaijevanger, record radius \(0\) for the \((s,p)=(2,4)\) class. That general obstruction does not by itself give the finite conservative state-space threshold proved here.

A recent preprint by Itkin and Kazbek (2026) studies positivity of rational maps for Fokker--Planck generators, with emphasis on large-step behavior and other Padé choices. Its accessible abstract does not state the eight-state small-step Markov threshold or the exact window above; the full theorem-level comparison was not available in the material inspected, so it remains a relevant originality risk.

## Computational model and limitations

The statements use exact arithmetic and the exact rational end-step map \(r(hQ)\). They concern finite real CTMC generators in the row convention and entrywise positivity/stochasticity of the one-step transition approximation. They do not assert positivity of internal Runge--Kutta stages, floating-point nonnegativity, accuracy superiority, efficiency, nonlinear positivity preservation, or an analogous minimal dimension for other Padé orders or other Runge--Kutta methods.

The lower-bound theorem is local in the step size for each fixed generator; it is not a dimension-only uniform positive step-size bound over generators with unbounded rates.

## Reproducibility

`artifacts/verify_pade_markov.py` symbolically reconstructs the eight-state map, verifies row sums, the key entries, all absorbing-column remainder factorizations, the Padé coefficients, and the two exact positivity boundaries. `artifacts/verification.txt` records a deterministic run.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “Essentially negative news about positive systems,” *Linear Algebra and its Applications* 436 (2012), 3425–3442. https://doi.org/10.1016/j.laa.2011.12.021
2. J. A. van de Griend, J. F. B. M. Kraaijevanger, “Absolute monotonicity of rational functions occurring in the numerical solution of initial value problems,” *Numerische Mathematik* 49 (1986), 413–424. https://doi.org/10.1007/BF01389539
3. L. Lóczi, D. I. Ketcheson, “Rational functions with maximal radius of absolute monotonicity,” *LMS Journal of Computation and Mathematics* 17 (2014), 159–205. https://doi.org/10.1112/S1461157013000326
4. A. Itkin, R. Kazbek, “Diagonal Frog meets ADI: trading matrix exponentials for rational maps in the Fokker--Planck equation,” arXiv:2608.22703 (2026). https://arxiv.org/abs/2608.22703

Same-model review: passed. Independent audit: not yet performed.
