# Two forbidden step intervals for Radau IIA diffusion on unequal complete bipartite graphs

## Finding

Fix integers \(p,q\ge2\) with \(p\ne q\), and consider the unit-conductance complete bipartite graph \(K_{p,q}\) with \(n=p+q\) vertices and combinatorial Laplacian \(L\). Apply the **unmodified two-stage, order-three Radau IIA** Runge–Kutta method to \(u'=-Lu\), with positive step \(h\). The endpoint matrix is
\[
P_h=\mathcal R(hL),\qquad \mathcal R(z)=\frac{6-2z}{z^2+4z+6}.
\]
The endpoint is always symmetric and row-stochastic in the algebraic sense (all row sums equal one), but may not be nonnegative. The following gives its **complete entrywise sign classification for every real positive step**.

**Theorem.** Every off-diagonal entry of \(P_h\) is strictly positive for every \(h>0\). If \(n\le11\), all entries of \(P_h\) are strictly positive for every \(h>0\). If \(n\ge12\), each of the two diagonal classes is negative on exactly one bounded open interval, and nonnegative elsewhere. Let
\[
\begin{aligned}
F_{p,q}(h)={}&q^2(p+q)h^4-2q\bigl((p+q)^2-3p-6q\bigr)h^3\\
&+\bigl(6p^2+4pq-2q^2+18q\bigr)h^2+(24p+12q)h+36.
\end{aligned}
\]
For \(n\ge12\), let \(a_-<a_+\) be the **exactly two positive simple roots** of \(F_{p,q}\), and let \(b_-<b_+\) be those of \(F_{q,p}\). The full nonnegative-stochastic end-step domain is precisely
\[
\boxed{[0,\infty)\setminus\bigl((a_-,a_+)\cup(b_-,b_+)\bigr).}
\]
The \(p\)-vertex-side diagonal is negative on \((a_-,a_+)\), while the \(q\)-vertex-side diagonal is negative on \((b_-,b_+)\). Off-diagonal entries never cause a positivity failure. Both forbidden intervals are nonempty for **every** \(n\ge12\), irrespective of part imbalance.

Unlike the already-understood equal-part case, the intervals can be disjoint or overlap. On \(K_{2,10}\), their positive roots lie in the disjoint rational brackets
\[
\begin{aligned}
a_-&\in(0.561,0.562),&a_+&\in(1.097,1.098),\\
b_-&\in(3.053,3.054),&b_+&\in(5.779,5.780).
\end{aligned}
\]
Consequently the endpoint has **three** nonnegative step-size windows: \([0,a_-]\), \([a_+,b_-]\), and \([b_+,\infty)\). In contrast, on \(K_{5,7}\), exact rational root brackets give
\[
0<a_-<b_-<a_+<b_+,
\]
so the forbidden intervals overlap and there are only **two** nonnegative windows. All brackets and the two distinct patterns are checkable using exact fractions.

## Assumptions and scope

The unequal sides have at least two vertices each; the equal-size case is deliberately excluded from the new claim. All graph edges have unit weight, and \(L=D-A\), not a normalized Laplacian. The endpoints are those of the standard, unperturbed third-order two-stage Radau IIA method, with Butcher coefficients
\[
A=\begin{pmatrix}5/12&-1/12\\3/4&1/4\end{pmatrix},\qquad b=(3/4,1/4).
\]
This gives the stated rational function \(\mathcal R(z)=R(-z)\) for the linear diffusion equation. Entrywise nonnegativity is a stronger and different property than spectral stability or energy decay. Nothing is asserted about internal stage positivity, directed generators, unbalanced multipartite graphs with more than two parts, arbitrary weights or other integrators.

## Proof

**1. Exact four-mode spectral resolution.** Let \(J\) be the all-ones \(n\)-by-\(n\) matrix, and let \(J_p,J_q\) be the all-ones matrices on the two parts. The Laplacian eigenvalues are \(0\), \(q\), \(p\) and \(n\), with multiplicities \(1\), \(p-1\), \(q-1\), and \(1\), respectively. The corresponding pairwise orthogonal projectors are
\[
\frac Jn,\quad \begin{pmatrix}I_p-J_p/p&0\\0&0\end{pmatrix},\quad
\begin{pmatrix}0&0\\0&I_q-J_q/q\end{pmatrix},\quad
\begin{pmatrix}(q/(pn))J_p&-(1/n)J_{p\times q}\\-(1/n)J_{q\times p}&(p/(qn))J_q\end{pmatrix}.
\]
Set \(\alpha=\mathcal R(qh)\), \(\beta=\mathcal R(ph)\), \(\gamma=\mathcal R(nh)\). Applying \(\mathcal R\) to these projectors gives the following five entry types:
\[
\begin{array}{ll}
P_h(i,i)=\dfrac{p+q\gamma+n(p-1)\alpha}{pn},&i\text{ in the first part},\\[3pt]
P_h(i,i)=\dfrac{q+p\gamma+n(q-1)\beta}{qn},&i\text{ in the second part},\\[3pt]
P_h(i,j)=\dfrac{p+q\gamma-n\alpha}{pn},&i\ne j\text{ both in the first part},\\[3pt]
P_h(i,j)=\dfrac{q+p\gamma-n\beta}{qn},&i\ne j\text{ both in the second part},\\[3pt]
P_h(i,j)=\dfrac{1-\gamma}{n},&i,j\text{ in opposite parts}.
\end{array}
\]
The projectors sum to the identity and the constant eigenvalue maps to \(\mathcal R(0)=1\), hence \(P_h\mathbf1=\mathbf1\).

**2. Strict off-diagonal positivity.** Write \(D(z)=z^2+4z+6\). For \(z>0\),
\[
1-\mathcal R(z)=\frac{z^2+6z}{D(z)}>0.
\]
For the within-first-part entries, clearing denominators yields the exact factorization
\[
p+q\mathcal R(nh)-n\mathcal R(qh)=\frac{h^2pqn\bigl(h^2qn+6hp+12hq+18\bigr)}{D(qh)D(nh)}>0.
\]
The within-second-part expression has the symmetric factorization obtained by interchanging \(p,q\). Thus every off-diagonal entry is strictly positive for all positive steps. Negative entries can occur only on the two diagonals.

**3. Exact diagonal quartics.** Collecting the denominators in the first-part diagonal expression, and analogously in the second, proves
\[
P_h(i,i)=\begin{cases}
\dfrac{F_{p,q}(h)}{D(qh)D(nh)},& i\text{ in the first part},\\[6pt]
\dfrac{F_{q,p}(h)}{D(ph)D(nh)},& i\text{ in the second part}.
\end{cases}
\]
The denominators are strictly positive for all \(h\ge0\). Consequently the signs of the two diagonal classes equal the signs of their explicitly stated quartics.

**4. No failure below twelve vertices.** Differentiating \(\mathcal R\) gives
\[
\mathcal R'(z)=\frac{2(z^2-6z-18)}{D(z)^2},
\]
so its global minimum on \([0,\infty)\) equals \(\mu=(5-3\sqrt3)/2\), attained at \(z=3+3\sqrt3\). In every connected regular or nonregular undirected graph, the constant Laplacian projector has diagonal \(1/n\) and the remaining projectors are positive semidefinite and have complementary diagonal sum \(1-1/n\). Hence each entry on the diagonal of \(P_h\) is at least
\[
\frac{1+(n-1)\mu}{n}\ge\frac{26-15\sqrt3}{n}>0\qquad(n\le11).
\]
Together with step 2, this establishes strict entrywise positivity for all positive steps in the small-size range.

**5. Both diagonals fail at twelve or more vertices.** For the first part choose \(h_A=8/q\). Since \(\mathcal R(8)=-5/51\), substitution and simplification give the exact formula
\[
P_{h_A}(i,i)=-\frac{H_n(p)}{51(51n^2-22np+3p^2)},\qquad
H_n(t)=15t^2+(1056-110n)t+255n^2-2848n.
\]
The quadratic \(H_n\) has positive leading coefficient and discriminant
\[
(1056-110n)^2-60(255n^2-2848n)=-128(25n^2+480n-8712)<0
\]
for all \(n\ge12\). Thus \(H_n(p)>0\) for every real \(p\), while \(51n^2-22np+3p^2=51q^2+80pq+32p^2>0\). The first-part diagonal is strictly negative at \(h=8/q\). Swapping \(p,q\) proves that the second-part diagonal is strictly negative at \(h=8/p\). Importantly, these witnesses can occur at **different** steps.

**6. Each diagonal fails on exactly one interval.** The leading coefficient of \(F_{p,q}\) is \(q^2n>0\); its constant and linear coefficients are positive. For \(n\ge12\), its cubic coefficient is strictly negative, because
\[
n^2-3p-6q=n(n-6)+3p>0.
\]
Whatever the sign of its quadratic coefficient, the ordered coefficient sign sequence has precisely two changes. Descartes' rule of signs therefore permits at most two positive zeros counted with multiplicity. Meanwhile \(F_{p,q}(0)=36>0\), \(F_{p,q}(h)\to+\infty\) as \(h\to\infty\), and step 5 exhibits a negative value at \(h=8/q\). By continuity there is a zero on either side of that negative value. Thus there are **exactly two distinct, simple** positive roots, and the sign is negative exactly between them. The argument for \(F_{q,p}\) is identical, using the witness \(h=8/p\). Combining the two sign conditions completes the theorem.

**7. Both safety-window patterns really occur.** Exact integer/rational evaluation shows \(F_{2,10}\) changes sign in each of \((561/1000,562/1000)\) and \((1097/1000,1098/1000)\), whereas \(F_{10,2}\) changes sign in \((3053/1000,3054/1000)\) and \((5779/1000,5780/1000)\). Since each polynomial has only two positive roots, these disjoint brackets completely isolate them. Similarly, the two roots of \(F_{5,7}\) lie in \((845/1000,846/1000)\) and \((1570/1000,1571/1000)\), whereas those of \(F_{7,5}\) lie in \((1212/1000,1213/1000)\) and \((2225/1000,2227/1000)\). Those ordered brackets prove overlap. This finishes the proof.

## Verification

The standalone `verify_radau_bipartite.py` requires only Python 3 standard-library `fractions.Fraction`. It checks exact quartic/diagonal and row-stochastic identities on all unequal integer pairs \(2\le p,q\le30\) at six rational steps, and verifies the explicit negative witnesses. It independently constructs complete bipartite Laplacians, performs dense exact-rational matrix inversion to calculate the Radau end-step, and checks every matrix entry for seven distinct small graph configurations and six steps each. Finally, it certifies the rational root brackets proving the two different positivity-window patterns. The expected output is `VERIFY_OK 30768 exact-rational assertions`. The all-parameter statements are established by the proof above, not by these finite tests.

## Relationship to prior work

Hairer and Lubich (published online 3 October 2013) prove energy-diminishing results for algebraically stable Runge–Kutta methods and examine the scalar stability function for quadratic gradient systems. These results do not determine entrywise positivity. Higueras, Ketcheson and Kocsis (first arXiv version 15 May 2015) develop general absolute-monotonicity and perturbation conditions for Runge–Kutta methods; these do not give the two explicit unperturbed Radau IIA diagonal quartics on \(K_{p,q}\). A previously established result for **balanced** complete multipartite graphs has equal block sizes, and so covers the \(p=q\) special case of the present graph but **not** the unequal case treated here: split internal eigenvalues and the two distinct diagonal classes create two potentially disjoint forbidden intervals. This work makes no new claim about that previously covered equal-part case, and no claim that searches constitute a proof of novelty.

## Limitations

The theorem assumes two **unequal** parts, each of size at least two, with all cross-edges present and equally weighted, and the unmodified two-stage Radau IIA end-step. It does not classify for which complete bipartite side ratios the forbidden intervals overlap versus remain disjoint; instead it provides a complete exact computable step-size domain via two pairs of positive quartic roots and proves both topologies are realized. It does not concern internal stage states, nonuniform edge weights, other Runge–Kutta methods, or arbitrary graph Laplacians. Finite verifier checks are supplementary. Specialist historical overlap and independent mathematical validation have not been excluded.

## References

1. E. Hairer and C. Lubich, *Energy-diminishing integration of gradient systems*, IMA Journal of Numerical Analysis **34** (2014), 452–461; first published online 3 October 2013, https://doi.org/10.1093/imanum/drt031 . Author manuscript: https://www.unige.ch/~hairer/preprints/gradientflow.pdf .
2. I. Higueras, D. I. Ketcheson and T. A. Kocsis, *Optimal monotonicity-preserving perturbations of a given Runge–Kutta method*, first arXiv version 15 May 2015, https://arxiv.org/abs/1505.04024 .
