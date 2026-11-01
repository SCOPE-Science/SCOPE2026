# An explicit Blaschke counterexample to the symmetric H-domain third Hankel bound

## Finding

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and \(\phi_H(u)=1+u+u^2/3-u^3/9\). In the normalized Sakaguchi-type class
\[
\mathcal S^*_{\mathrm{sym}}(\phi_H)=\left\{f(z)=z+\sum_{k\ge2}a_kz^k:\frac{2zf'(z)}{f(z)-f(-z)}=\phi_H(\omega(z)),\ \omega(0)=0,\ |\omega(z)|<1\ (z\in\mathbb D)\right\},
\]
there exists a member with
\[
\boxed{H_{3,1}(f)=\det\begin{pmatrix}1&a_2&a_3\\a_2&a_3&a_4\\a_3&a_4&a_5\end{pmatrix}=-\frac{10700387}{169869312}.}
\]
In particular, its absolute determinant exceeds both the proposed bound \(1/16\) and the asserted 2026 upper bound \(769/12288\):
\[
|H_{3,1}(f)|-\frac1{16}=\frac{83555}{169869312}>0,\qquad
|H_{3,1}(f)|-\frac{769}{12288}=\frac{69731}{169869312}>0.
\]
This is a counterexample to those **upper bounds**, not a determination of the actual sharp supremum.

## Assumptions and scope

The class is defined by subordination of the symmetric-point logarithmic derivative to \(\phi_H\), with \(f(0)=0\) and \(f'(0)=1\). The independent Schwarz function is allowed to be any holomorphic disk self-map vanishing at the origin. No coefficient-reality restriction is required; the example has real Taylor coefficients. The determinant uses precisely the ordinary normalized coefficients \(a_1=1\), \(a_2\), \(a_3\), \(a_4\), and \(a_5\).

## Proof

**1. An admissible Schwarz function.** Set
\[
\omega(z)=\frac{z(1-3z+8z^2)}{8-3z+z^2}.
\]
Put \(\alpha=(3+i\sqrt{23})/16\), so \(|\alpha|^2=1/8\), and let \(\overline\alpha\) be its conjugate. Direct factorization gives
\[
\omega(z)=z\frac{(z-\alpha)(z-\overline\alpha)}{(1-\overline\alpha z)(1-\alpha z)}.
\]
Both roots lie strictly inside \(\mathbb D\). Each factor \((z-a)/(1-\overline a z)\) maps \(\mathbb D\) into itself, so \(\omega\) is a finite Blaschke product with \(\omega(0)=0\) and \(|\omega(z)|<1\) on \(\mathbb D\).

**2. Existence and exact class membership.** Define \(Q(z)=\phi_H(\omega(z))\) and its parity components \(Q_e(z)=(Q(z)+Q(-z))/2\), \(Q_o(z)=(Q(z)-Q(-z))/2\). Define two holomorphic functions on \(\mathbb D\):
\[
g(z)=z\exp\left(\int_0^z\frac{Q_e(t)-1}{t}\,dt\right),\qquad
h(z)=\int_0^z\frac{Q_o(t)g(t)}{t}\,dt,\qquad f(z)=g(z)+h(z).
\]
The quotients under the integrals extend holomorphically across \(0\), so the primitives are path-independent on the disk. By parity, \(g\) is odd and \(h\) is even; also \(g(z)=z+O(z^3)\), \(h(z)=O(z^2)\), and \(g(z)\ne0\) for \(z\ne0\). Thus \(f(0)=0\), \(f'(0)=1\), and
\[
\frac{2zf'(z)}{f(z)-f(-z)}=\frac{z(g'(z)+h'(z))}{g(z)}=Q_e(z)+Q_o(z)=\phi_H(\omega(z))
\]
throughout \(\mathbb D\), with the value at \(0\) understood by analytic continuation. This proves membership in the stated class, not merely membership of a truncated Taylor polynomial.

For completeness, the target has positive real part on the disk: writing \(c=\cos t\),
\[
\operatorname{Re}\phi_H(e^{it})=\frac29\bigl(3(1+c)^2-2c^3\bigr)>0,\qquad -1\le c\le1.
\]
Indeed the bracket is positive for \(c<0\) because \(-2c^3>0\), and for \(c\ge0\) it exceeds \(3-2=1\). The harmonic minimum principle gives \(\operatorname{Re}Q>0\).

**3. Exact coefficients.** Long division and substitution into \(\phi_H\) give
\[
\begin{aligned}
\omega(z)&=\tfrac18z-\tfrac{21}{64}z^2+\tfrac{441}{512}z^3+\tfrac{1491}{4096}z^4+O(z^5),\\
Q(z)&=1+\tfrac18z-\tfrac{31}{96}z^2+\tfrac{1921}{2304}z^3+\tfrac{1939}{4096}z^4+O(z^5).
\end{aligned}
\]
Writing \(Q(z)=1+\sum_{j\ge1}q_jz^j\), the identity in step 2 gives the exact coefficient relations
\[
a_2=\frac{q_1}{2},\quad a_3=\frac{q_2}{2},\quad
 a_4=\frac{q_3+q_1a_3}{4},\quad a_5=\frac{q_4+q_2a_3}{4}.
\]
Therefore
\[
\boxed{a_2=\frac1{16},\quad a_3=-\frac{31}{192},\quad a_4=\frac{3749}{18432},\quad a_5=\frac{19373}{147456}.}
\]
Substitution into \(H_{3,1}=2a_2a_3a_4-a_3^3-a_4^2+a_3a_5-a_2^2a_5\) yields exactly \(-10700387/169869312\). Subtracting the two stated rational constants gives the positive gaps in the finding.

## Verification

The standalone `CHECK.py` uses only Python's exact `fractions.Fraction` arithmetic. It recomputes the Schwarz-function series by formal division, forms the composition with \(\phi_H\) by truncated polynomial multiplication, reconstructs all four coefficients independently of the displayed decimal approximations, checks the symmetric-point identity to fourth order, and recomputes the determinant and both strict rational gaps. The disk-self-map property and all-order class membership follow analytically from steps 1 and 2 rather than from finite tests.

Run `python3 CHECK.py` from the directory containing this document and the checker. The calculation is an exact rational consistency certificate for the finite coefficient evaluation; it is not an independent mathematical audit.

## Relationship to prior work

Lupaş, Tayyah, and Sokół introduced the symmetric H-domain class and proposed the sharp \(1/16\) upper bound in their 2025 paper [1]. Tayyah, Hadi, and Lupaş asserted the stricter bound \(769/12288\) as Theorem 1 in their August 2026 paper [2]. Both works use the same defining subordination and the same ordinary third Hankel determinant. Neither work's inspected mathematical statement includes the concrete finite-Blaschke counterexample above; the new rational witness directly contradicts the stated inequalities. The earlier valid coarse estimate of approximately \(0.104485\) is not contradicted.

## Limitations

The construction establishes the rigorous lower bound \(\sup_{f\in\mathcal S^*_{\mathrm{sym}}(\phi_H)}|H_{3,1}(f)|\ge10700387/169869312\) and disproves the two smaller claimed upper bounds. It does **not** identify the sharp supremum, characterize extremizers, or assert that every bound from either cited work is incorrect. No external independent audit has been performed.

## References

[1] A. A. Lupaş, A. S. Tayyah, and J. Sokół, “Sharp Bounds on Hankel Determinants for Starlike Functions Defined by Symmetry with Respect to Symmetric Domains,” *Symmetry* **17** (2025), 1244, published 2025-08-05. DOI: 10.3390/sym17081244. https://doi.org/10.3390/sym17081244

[2] A. S. Tayyah, S. H. Hadi, and A. A. Lupaş, “Sharp Bound of the Third-Order Hankel Determinant for a Symmetric Domain,” *Symmetry* **18** (2026), 1307, published 2026-08-03. DOI: 10.3390/sym18081307. https://doi.org/10.3390/sym18081307
