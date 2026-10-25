# A sharp three-state positivity window for fifth-order Radau IIA

## Finding

The completed fifth-order three-stage Radau IIA integration step of a finite continuous-time Markov generator \(Q\) is the rational matrix
\[
T_Q(h)=(60I+24hQ+3h^2Q^2)(60I-36hQ+9h^2Q^2-h^3Q^3)^{-1},\qquad h\ge0.
\]
All one- and two-state Markov generators have \(T_Q(h)\) entrywise nonnegative for **every** \(h\ge0\). This dimension bound is sharp, even among three-state irreducible reversible birth-death generators.

For the three-state, unit-rate pure-birth generator
\[
Q_0=\begin{pmatrix}-1&1&0\\0&-1&1\\0&0&0\end{pmatrix},
\]
define
\[
p(h)=h^4-16h^3-48h^2+240h+1200.
\]
There are exactly two positive roots \(\alpha\in(4,5)\) and \(\beta\in(17,18)\), with numerical approximations \(\alpha=4.80841258070855\ldots\) and \(\beta=17.7285411579897\ldots\). The **complete** timestep classification for this fixed generator is
\[
T_{Q_0}(h)\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad h\in[0,\alpha]\cup[\beta,\infty).
\]
Thus both sufficiently small and sufficiently large positive steps preserve nonnegativity, whereas **every** intermediate step in \((\alpha,\beta)\) produces a negative entry. In particular,
\[
\bigl(T_{Q_0}(5)\bigr)_{1,2}=-\frac{105}{13924}.
\]
There is also an explicit irreducible reversible three-state counterexample at step \(h=5\): with \(\varepsilon=1/1000\) and
\[
Q_\varepsilon=\begin{pmatrix}-1&1&0\\\varepsilon&-1-\varepsilon&1\\0&\varepsilon&-\varepsilon\end{pmatrix},
\quad
\bigl(T_{Q_\varepsilon}(5)\bigr)_{1,2}=
-\frac{4448823545303000}{676819275720209897}<0.
\]
This generator is irreducible and reversible with stationary probabilities proportional to \((\varepsilon^2,\varepsilon,1)\).

## Assumptions and scope

A row-oriented continuous-time Markov generator is a finite real square matrix with nonnegative off-diagonal entries and zero row sums. No irreducibility or detailed balance is required for the universal two-state statement. A matrix is *endpoint-positive* here if its completed step is entrywise nonnegative; intermediate Runge–Kutta stage states are not claimed to be positive. No claim is made about arbitrary higher-dimensional generators or stagewise positivity. The rational step is well-defined for any such generator and any nonnegative step because its denominator polynomial has roots in the open right half-plane, while the spectrum of a generator lies in the closed left half-plane.

## Proof

Write the scalar stability function as
\[
R(z)=\frac{60+24z+3z^2}{60-36z+9z^2-z^3}
\quad\text{and}\quad
D(x)=x^3+9x^2+36x+60.
\]
For every \(x\ge0\),
\[
R(-x)=\frac{3((x-4)^2+4)}{D(x)}>0,\qquad
1-R(-x)=\frac{x(x^2+6x+60)}{D(x)}\ge0.
\]
Let \(Q=\begin{psmallmatrix}-a&a\\b&-b\end{psmallmatrix}\), \(a,b\ge0\), and set \(s=a+b\). If \(s>0\), the identity \(Q^2=-sQ\) gives
\[
T_Q(h)=I+\frac{1-R(-hs)}s\,Q.
\]
Its off-diagonal entries are nonnegative, and its diagonal entries are convex combinations of \(1\) and \(R(-hs)\), hence nonnegative. If \(s=0\), \(Q=0\) and \(T_Q(h)=I\). The one-state case is identical.

For \(Q_0\), the leading transient \(2\times2\) block is a Jordan block with eigenvalue \(-1\). Rational functional calculus therefore gives its off-diagonal entry as \(hR'(-h)\). Explicit differentiation yields
\[
R'(-h)=\frac{3p(h)}{D(h)^2},\quad
q(h)=h^4+12h^3+198h^2+960h+1800,
\]
and direct substitution gives the **entire** matrix
\[
T_{Q_0}(h)=\begin{pmatrix}
R(-h)&3hp(h)/D(h)^2&h^2q(h)/D(h)^2\\
0&R(-h)&h(h^2+6h+60)/D(h)\\
0&0&1
\end{pmatrix}.
\]
Every entry except the displayed multiple of \(p(h)\) is nonnegative on \(h\ge0\). The signs of \(p(4),p(5),p(17),p(18)\) are respectively \((+,-,-,+)\): their exact values are \((624,-175,-3679,1632)\). The coefficient sequence of \(p\) has exactly two changes of sign. Descartes' rule, together with the two sign-changing brackets, proves precisely two positive roots, simple, with \(p(h)<0\) exactly between them. This proves the full phase classification, including \(h=0\) and both endpoints.

At \(h=5\), the exact matrix identity gives the first negative fraction. The tridiagonal \(Q_\varepsilon\) has positive birth and death rates, hence is irreducible. Detailed balance holds for stationary weights \((\varepsilon^2,\varepsilon,1)\); exact rational evaluation gives the second negative fraction above, proving that irreducibility and reversibility do not rescue unconditional endpoint positivity.

To justify existence of the step, let \(w=-z\). The denominator \(D(w)=w^3+9w^2+36w+60\) is a Hurwitz polynomial: all coefficients are positive and \(9\cdot36>60\). Thus all poles of \(R\) have strictly positive real part; the generator spectrum has nonpositive real part.

## Verification

The accompanying standalone `verify_radau3.py` uses exact symbolic arithmetic to reproduce the scalar rational identities, the full three-state matrix, quartic sign brackets, both negative rational entries, generator row sums and detailed balance. Run `python verify_radau3.py` with SymPy installed. The analytical arguments (not a finite grid) establish the all-step and all-two-state statements; numerical roots are illustrative only.

## Relationship to prior work

Brugnano, Iavernaro and Magherini (arXiv:1302.1037v1) develop the implementation of Radau IIA collocation methods. Lóczi and Ketcheson (arXiv:1303.6651v1; DOI:10.1112/S1461157013000326) study absolute-monotonicity radii for rational stability functions, with a general fifth-order rational family in §4.2. Such scalar and stagewise monotonicity theory motivates the positivity question but does not itself give the stated smallest Markov-state dimension, the two separate sharp step intervals or the reversible three-state witness. The published Radau IIA3 method reference provides the fifth-order rational stability function. Other published endpoint-positivity cases treat different methods, including SSP-SDIRK2(2) and the diagonal \([2/2]\) Padé method; neither rational function is the three-stage Radau IIA \([2/3]\) function used here.

## Limitations

The sharp phase intervals belong to the specified equal-rate pure-birth generator, not to every three-state chain. The reversible example demonstrates failure at one exact step but is not assigned an all-step phase classification. The work concerns only the completed linear autonomous step; it does not establish positivity at internal stages, for nonlinear problems, or a universal step bound for all generators. Distinct or incompletely indexed literature could contain an equivalent statement.

## References

1. L. Brugnano, F. Iavernaro and C. Magherini, *Efficient implementation of Radau collocation methods*, arXiv:1302.1037v1 (first public 2013-02-05), https://arxiv.org/abs/1302.1037.
2. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1 (first public 2013-03-26); *LMS Journal of Computation and Mathematics* 17 (2014), 159–205, DOI:10.1112/S1461157013000326.
3. D. I. Ketcheson, *Numipedia: Radau IIA3*, https://ketch.github.io/numipedia/methods/RadauIIA3.html (online method summary; publication date not used in archival dating).
