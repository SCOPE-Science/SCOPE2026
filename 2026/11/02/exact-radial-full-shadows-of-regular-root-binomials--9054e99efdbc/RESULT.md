# Exact radial full shadows of regular-root binomials

## Finding

Fix an integer \(d\ge2\) and \(P_d(z)=z^d-1\). Put
\[
\mathcal R_d=\{t\zeta:0\le t\le1,\ \zeta^d=1\}.
\]
For every integer \(n\ge1\) and \(0\le m<dn\), every zero of \((P_d^n)^{(m)}\) lies in \(\mathcal R_d\). Write \(r_m\in\{0,\ldots,d-1\}\) for the representative of \(-m\) modulo \(d\). There is an exact factorization
\[
(P_d^n)^{(m)}(z)=z^{r_m}Q_m(z^d),
\]
where \(Q_m\) is a real polynomial with \(Q_m(0)\ne0\). All its zeros belong to \((0,1]\); those in \((0,1)\) are simple; and \(1\) has multiplicity precisely \(\max(n-m,0)\). The factor at the origin is therefore exactly \(z^{r_m}\).

The full shadow of \(P_d\), defined as the closure of the zeros of all these nonzero derivatives over all powers, is **exactly \(\mathcal R_d\)**. Its limiting core is the same star, with no transient zeros. This is an exact all-order result, including all powers and every derivative order.

## Assumptions and scope

All derivative orders are ordinary derivatives in the complex variable. The power \(n\) is a positive integer, \(d\ge2\) is an integer, and \(0\le m<dn\) ensures a nonzero polynomial. The definition of full shadow \(\mathcal S_P\), limiting core \(\mathcal K_P\), and transient set \(T_P=\mathcal S_P\setminus\mathcal K_P\) is that of Hägg and Shapiro [1]. The connectedness of the limiting core and its containment of all original roots are invoked as an established theorem [1, Theorem 1.4(i)]. No corresponding assertion is made for an arbitrary perturbation of \(P_d\).

## Proof

**1. Exact factorization and recursion.** Initially \(r_0=0\) and \(Q_0(y)=(y-1)^n\). If the current derivative is \(z^r Q(y)\) with \(y=z^d\), then
\[
\frac{d}{dz}[z^rQ(z^d)]=
\begin{cases}
 z^{r-1}(rQ(y)+dyQ'(y)),&r>0,\\
 z^{d-1}dQ'(y),&r=0.
\end{cases}
\]
Thus the exact coefficients, without arbitrary rescaling, satisfy the recurrence
\[
(r_{m+1},Q_{m+1})=
\begin{cases}
(r_m-1,\ r_mQ_m+dyQ_m'),&r_m>0,\\
(d-1,\ dQ_m'),&r_m=0.
\end{cases}
\]
At every step, \(r_m\equiv-m\pmod d\) and \(0\le r_m<d\). Before the last derivative, the polynomial has positive degree, so the next \(Q_m\) is nonzero.

**2. Root-preserving operators.** Let \(Q\) be a nonconstant real polynomial whose zeros are in \((0,1]\), and list its distinct zeros as \(0<a_1<\cdots<a_s\le1\), with multiplicities \(h_1,\ldots,h_s\). Ordinary Rolle interlacing gives the roots of \(Q'\): a root of multiplicity \(h_i-1\) at each \(a_i\), together with exactly one simple root in each \((a_i,a_{i+1})\). These account for all \(\deg Q-1\) roots.

For any \(c>0\), the operator \(cQ+yQ'\) is the derivative of \(y^cQ(y)\) multiplied by the positive factor \(y^{1-c}\) on \((0,1]\). Rolle's theorem, now using the additional vanishing at \(y=0\) of \(y^cQ(y)\), gives a simple root in \((0,a_1)\), one in every \((a_i,a_{i+1})\), and the \(h_i-1\) inherited zeros at \(a_i\). Counting \(1+(s-1)+\sum_i(h_i-1)=\deg Q\) roots proves that none others exist. All the new roots are strictly between the old distinct roots or between zero and the first. In particular both operators keep all roots in \((0,1]\) and never introduce a zero at the origin. The derivative of a nonconstant polynomial with all roots positive also has nonzero value at zero, since \(Q'(0)/Q(0)=-\sum_i h_i/a_i<0\).

**3. Complete finite-order localization and multiplicities.** Apply step 2 inductively to the operators in step 1. Since \(r_m/d>0\) whenever \(r_m>0\), the recurrence preserves the positive interval at every stage. It also shows that every root in \((0,1)\) is simple: initially there are none, while newly inserted roots are simple and distinct and any preexisting simple root disappears under differentiation. The only potentially repeated positive root is at \(y=1\), inherited from the original factor \((z^d-1)^n\). At each root of unity, differentiation \(m\) times lowers the original multiplicity \(n\) to \(\max(n-m,0)\), and hence this is exactly the multiplicity of \(y=1\) in \(Q_m\). A root \(z\ne0\) of the factorization satisfies \(z^d\in(0,1]\), so \(z=t\zeta\) for some \(0<t\le1\) and \(\zeta^d=1\). The only other possible zero is \(z=0\). Therefore each finite descendant has all its zeros on the asserted star.

**4. Equality of the full shadow and core.** By step 3, \(\mathcal S_{P_d}\subseteq\mathcal R_d\); also \(\mathcal K_{P_d}\subseteq\mathcal S_{P_d}\). The connectedness theorem of Hägg and Shapiro [1, Theorem 1.4(i)] states that \(\mathcal K_{P_d}\) is connected and contains every root of \(P_d\), namely the \(d\) endpoints \(\zeta^d=1\). A connected subset of the regular star containing all its endpoints must contain every radial segment: removing any point in the interior of one arm disconnects that arm's endpoint from all other endpoints. Thus \(\mathcal R_d\subseteq\mathcal K_{P_d}\). The reverse inclusions yield
\[
\mathcal R_d\subseteq\mathcal K_{P_d}\subseteq\mathcal S_{P_d}\subseteq\mathcal R_d,
\]
so \(\mathcal K_{P_d}=\mathcal S_{P_d}=\mathcal R_d\) and \(T_{P_d}=\varnothing\). This establishes an exact full-shadow classification, not merely a large-power approximation.

## Verification

The included stand-alone checker `CHECK.py` uses exact rational polynomial arithmetic. It reconstructs the 560 descendants obtained with \(2\le d\le6\), \(1\le n\le7\), \(0\le m<dn\), compares the recursive factorization with direct differentiation coefficient-for-coefficient, and uses rational isolating intervals to check that all zeros of each positive-degree \(Q_m\) belong to \((0,1]\). Its output is `CHECK_OK: 560 exact symbolic descendant identities and rational isolating intervals`. These finite tests do not establish the all-degree theorem; steps 1–4 do.

## Relationship to prior work

Hägg and Shapiro [1] introduce the full shadow, prove connectedness of its core, and exhibit examples with infinitely many transient zeros. Their general theorem supplies exactly the connectedness implication used in step 4; its statement alone does not force the star geometry for regular-root binomials. Bøgvad and Shapiro [2, Section 6] discuss the quadratic case \(P(z)=z^2-1\), whose derivatives already have real zeros by Gauss–Lucas. Leurs and Van Assche [3, Introduction and Section 3] study Jacobi–Angelesco polynomials on radial stars, including a Rodrigues representation for a designated derivative order and positive interval zeros of associated polynomials. The established single-order and quadratic facts are not asserted to be new here. The contribution claimed here is simultaneous, exact localization at **every** derivative order and power together with full-shadow/core equality and absence of transients for every regular-star degree.

## Limitations

The proof uses an external connectedness theorem for the global core conclusion. It gives root locations and multiplicities, not closed forms for each radial zero or individual limiting densities. It does not classify polynomials with perturbed or unequal-modulus root configurations. Although no equivalent all-order classification was identified in the inspected literature, it may be implicit in classical multiple-orthogonal-polynomial, hypergeometric, or differential-stability theory; independent priority validation remains outstanding.

## References

1. C. Hägg and B. Shapiro, *The full shadow of a polynomial I. The limiting core and the transient set*, arXiv:2610.09602v1, first posted 2026-10-07; especially Theorem 1.4.
2. R. Bøgvad and B. Shapiro, *Rodrigues' descendants of a polynomial and Boutroux curves*, arXiv:2107.05710v2; especially Section 6.
3. M. Leurs and W. Van Assche, *Jacobi-Angelesco multiple orthogonal polynomials on an r-star*, arXiv:1804.07512; especially Introduction and Section 3.
