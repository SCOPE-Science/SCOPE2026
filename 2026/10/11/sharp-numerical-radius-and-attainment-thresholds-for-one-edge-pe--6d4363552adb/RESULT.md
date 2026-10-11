# Sharp numerical-radius and attainment thresholds for one-edge perturbations of \(\ell_p\) shifts
## Finding
Let \(1<p<\infty\), \(q=p/(p-1)\), \(t\ge0\) and let \(\mathbb F\in\{\mathbb R,\mathbb C\}\). Consider the bounded operators on \(X=\ell_p(\mathbb N;\mathbb F)\) defined by
\[
F_t(x_1,x_2,\ldots)=(0,tx_1,x_2,x_3,\ldots),\qquad B_t(x_1,x_2,\ldots)=(tx_2,x_3,x_4,\ldots).
\]
For the spatial numerical radius \(v\), the following are exact equivalences:
\[
v(F_t)=1\quad\Longleftrightarrow\quad 0\le t\le p^{1/p},
\qquad
v(B_t)=1\quad\Longleftrightarrow\quad 0\le t\le q^{1/q}.
\]
Above the respective threshold, the numerical radius is strictly greater than one. In either family it is **not attained** at or below the threshold and **is attained** above the threshold. Thus the same parameter value can separate the two shift orientations: at \(p=3\), \(t=4/3\), one has \(v(F_t)=1<v(B_t)\).

## Assumptions and scope
The scalar field is either real or complex. The exponent is strictly between one and infinity; no assertion is made at the endpoint spaces. We use the Banach-space (spatial) numerical radius
\[
v(T)=\sup\{\lvert x^*(Tx)\rvert:\ \|x\|_p=\|x^*\|=1,\ x^*(x)=1\}.
\]
Attainment means the displayed supremum is reached by a normalized vector and a norming functional. The weights other than the first equal one. This is **not** the Hilbert numerical radius except when \(p=2\), and is distinct from operator norm, spectral radius, disk-contractivity radius, and Schatten-type numerical norms.

## Proof
**1. Scalar variational reduction.** For a unit vector \(x=(x_n)\) in the smooth space \(\ell_p\), its norming functional is unique and equals \(x^*(y)=\sum_{n\ge1}|x_n|^{p-2}\overline{x_n}y_n\) (with the usual interpretation at zero coordinates). Taking absolute values bounds \(\lvert x^*(F_tx)\rvert\) or \(\lvert x^*(B_tx)\rvert\) by the corresponding expression on the nonnegative sequence \(u_n=|x_n|\), and nonnegative real vectors achieve all such expressions. By homogeneity, the radii are the suprema of
\[
G_F(u)=t u_1u_2^{p-1}+\sum_{n\ge2}u_nu_{n+1}^{p-1},
\qquad
G_B(u)=t u_1^{p-1}u_2+\sum_{n\ge2}u_n^{p-1}u_{n+1}
\]
over \(u\in\ell_p\), \(u_n\ge0\), \(\sum u_n^p=1\). All sums converge by Hölder's inequality.

**2. Sharp forward threshold.** Young's inequality gives
\[
u_nu_{n+1}^{p-1}\le \frac1p u_n^p+\frac{p-1}{p}u_{n+1}^p.
\]
Thus, for every nonnegative \(u\in\ell_p\),
\[
G_F(u)-\|u\|_p^p\le t u_1u_2^{p-1}-u_1^p-\frac{p-1}{p}u_2^p.
\]
The exact two-variable inequality
\[
a^p+\frac{p-1}{p}b^p\ge p^{1/p}a b^{p-1}\qquad(a,b\ge0)
\]
has equality for positive \(a,b\) when \(a/b=p^{-1/p}\). Hence \(G_F(u)\le\|u\|_p^p\) for \(t\le p^{1/p}\).

**3. Sharp backward threshold.** The conjugate Young inequality
\[
u_n^{p-1}u_{n+1}\le\frac{p-1}{p}u_n^p+\frac1p u_{n+1}^p
\]
yields
\[
G_B(u)-\|u\|_p^p\le t u_1^{p-1}u_2-u_1^p-\frac1p u_2^p.
\]
The sharp two-variable inequality
\[
a^p+\frac1p b^p\ge q^{1/q}a^{p-1}b\qquad(a,b\ge0)
\]
has equality for positive \(a,b\) when \((a/b)^p=(p-1)/p\). Thus \(G_B(u)\le\|u\|_p^p\) for \(t\le q^{1/q}\).

**4. Equality cannot occur in the unit regime.** Young's inequality is an equality for each tail summand only when the two neighboring nonnegative coordinates are equal. A nonzero nonnegative \(\ell_p\) sequence cannot have constant tail on all indices \(n\ge2\); if its tail is zero and \(u_1>0\), the operator value is zero. Hence, for any nonzero \(u\in\ell_p\) and every parameter in the respective unit-radius regime, the inequality \(G_F(u)<\|u\|_p^p\) (respectively \(G_B(u)<\|u\|_p^p\)) is strict. On the other hand, normalized constant blocks supported far beyond coordinate one, with block length tending to infinity, give values tending to one for both operators. Therefore their numerical radii equal one and are not attained throughout the closed unit-radius parameter intervals, including the endpoints.

**5. Strictness past the thresholds.** Fix \(0<s<1\), set \(u_1=a>0\), \(u_n=s^{n-2}\) for \(n\ge2\). The vector belongs to \(\ell_p\). A direct geometric sum gives
\[
G_F(u)-\|u\|_p^p=t a-a^p-\frac{1-s^{p-1}}{1-s^p}.
\]
Choosing \(a=p^{-1/p}\), the limit as \(s\uparrow1\) is \(a(t-p^{1/p})>0\) whenever \(t>p^{1/p}\). Similarly,
\[
G_B(u)-\|u\|_p^p=t a^{p-1}-a^p-\frac{1-s}{1-s^p}.
\]
Choosing \(a=((p-1)/p)^{1/p}\), its limit is \(a^{p-1}(t-q^{1/q})>0\) when \(t>q^{1/q}\). After normalization, these vectors give numerical radius strictly greater than one.

**6. Attainment beyond the thresholds.** Let \(G\) be either scalar expression and set its radius \(\rho=\sup_{\|u\|_p=1,u\ge0}G(u)>1\). Choose a nonnegative normalized maximizing sequence \(u^{(k)}\). By reflexivity, after passing to a subsequence, \(u^{(k)}\rightharpoonup u\in\ell_p\), so every coordinate converges and \(\|u\|_p\le1\). For every fixed \(m\ge2\), Young's inequality bounds the contribution of all terms with \(n\ge m\) by \(\sum_{n\ge m}(u_n^{(k)})^p\); the finite prefix converges coordinatewise. Therefore
\[
\rho\le G(u)+1-\|u\|_p^p\le\rho\|u\|_p^p+1-\|u\|_p^p.
\]
Because \(\rho>1\), this forces \(\|u\|_p=1\) and then \(G(u)=\rho\). The corresponding positive real vector and its norming functional attain the original Banach numerical radius, over either scalar field.

**7. Directional asymmetry.** At \(p=3\), the forward threshold is \(3^{1/3}\), and the backward threshold is \((3/2)^{2/3}\). The strict inequalities \((3/2)^{2/3}<4/3<3^{1/3}\) give the displayed orientation difference. At \(p=2\), both thresholds reduce to \(\sqrt2\), the classical Hilbert threshold.

## Verification
The proof requires no finite numerical enumeration, computer-generated certificates, or external formal checker. All infinite-dimensional steps are explicit: norming functionals on \(\ell_p\), Young inequalities with their equality conditions, convergent geometric-tail witnesses, and weak sequential compactness in the reflexive space \(\ell_p\). The formulas at the thresholds follow by strictness of the tail Young inequalities; the argument is valid for real and complex scalars. Direct substitution into the geometric witness formulas checks the sign of their limiting defects. No exact supercritical radius formula is claimed.

## Relationship to prior work
Sharif (2023) studies the numerical radius of weighted unilateral shifts specifically on Hilbert \(\ell_2\); its introduction records Berger and Stampfli's one-exceptional-weight radius and the transition \(\sqrt2\), which the present theorem **includes but does not claim as new**. The arguments here use the nonlinear \(\ell_p\) duality map and establish both conjugate-exponent thresholds and their attainment behavior for general \(1<p<\infty\). Martín, Merí, and Popov (2010) give the spatial numerical-radius framework and related estimates for \(L_p\) operators but do not present this one-edge shift threshold theorem in their introductory numerical-radius discussion. Existing spectral-radius, power-norm, and shift functional-calculus results do not supply the spatial numerical-radius thresholds. Searches and primary-text inspections did not identify a covering non-Hilbert theorem; this is a qualified literature comparison, not a proof that no such theorem exists.

## Limitations
The weights are exactly \((t,1,1,\ldots)\); arbitrary weighted shifts, other \(L_p\) measure spaces, and \(p=1\) or \(p=\infty\) are not classified. The exact value of \(v\) **above** one is not determined, only strict positivity of the excess and its attainment. The \(p=2\) threshold is known from classical Hilbert-space work. Earlier unindexed or inaccessible literature may contain equivalent non-Hilbert statements; independent validation has not been performed.

## References
1. A. Sharif, *On the numerical radius of weighted shifts on \(\ell^2\) as a norm on \(\ell^\infty\) and connections to Banach limits*, arXiv:2303.00876, first submitted 2023-03-02; in particular the introduction's summary of Berger–Stampfli's one-weight result. https://arxiv.org/abs/2303.00876 and https://arxiv.org/pdf/2303.00876
2. M. Martín, J. Merí and M. Popov, *On numerical radius of operators in Lebesgue spaces*, arXiv:1011.4785 (2010). https://arxiv.org/pdf/1011.4785
3. C. A. Berger and J. G. Stampfli, classical weighted-shift numerical-radius result (1967), as reported and referenced in item 1; the original full text has not been independently inspected here.
