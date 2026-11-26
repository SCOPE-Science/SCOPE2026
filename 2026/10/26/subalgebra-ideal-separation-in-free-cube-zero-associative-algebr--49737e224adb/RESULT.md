# Subalgebra–ideal separation in free cube-zero associative algebras

## Finding

Fix a prime power \(q\). For each \(r\ge1\) let \(V=\mathbb F_q^r\), \(W=V\otimes V\), and \(A_r=V\oplus W\) with product \((v,a)(w,b)=(0,v\otimes w)\). Then \(W=A_r^2\) and \(A_r^3=0\). Let \(\pi:A_r\to V\) be projection. Subalgebras are \(\mathbb F_q\)-linear and need not be unital; ideals are \(\mathbb F_q\)-linear and two-sided.

As \(r\to\infty\), a uniformly chosen subalgebra \(S\) satisfies \(\dim\pi(S)=1\) with probability tending to one, whereas a uniformly chosen ideal \(I\) satisfies \(\dim\pi(I)=0\) with probability tending to one. Writing \(\mathcal S_r\) and \(\mathcal I_r\) for the two families, one has
\[
\frac{|\mathcal I_r|}{|\mathcal S_r|}\sim \frac{q-1}{q^r-1}\sim(q-1)q^{-r}.
\]
Thus ideal closure changes which subspaces dominate the count: most subalgebras contain one direction outside the square, but most ideals are contained in the square.

## Counting input

The exact two-variable subalgebra and ideal counts for this multiplication are already given in *Subalgebra and ideal Grassmannians of free class-two Zinbiel algebras* [1]. The same product defines the algebra here: the name differs, but both counts are of linear subspaces of \(V\oplus(V\otimes V)\) with the identical multiplication. We use those formulas as input and recount them briefly for clarity.

Let \(m=r^2\). A subspace \(X\) with \(U=\pi(X)\), \(T=X\cap W\), \(u=\dim U\), and \(t=\dim T\) corresponds, for fixed \(U,T\), to exactly one linear map \(U\to W/T\) describing its image modulo \(T\). The \(q^{u(m-t)}\) possible maps have no effect on the products, which depend only on the degree-one components. For subalgebras, \(T\) must contain \(U\otimes U\); for ideals, \(T\) must contain \((V\otimes U)+(U\otimes V)\). The compulsory dimension \(b\) is respectively \(u^2\) or \(2ru-u^2\), using a complement to \(U\) in each tensor factor. Thus the previously known joint count is
\[
{r\brack u}_q{m-b\brack t-b}_q q^{u(m-t)}\qquad (b\le t\le m).
\]
In particular, the count includes subspaces that are not graded.

## Proof of concentration and the ratio

Write \(S_u\) and \(I_u\) for the counts with projection dimension \(u\), and \(G_n=\sum_{j=0}^n{n\brack j}_q\). The product formula for Gaussian coefficients gives
\[
q^{j(n-j)}\le {n\brack j}_q\le C_q q^{j(n-j)},\qquad C_q=\prod_{j=1}^{\infty}(1-q^{-j})^{-1}.
\]
Summing about the central index gives \(q^{\lfloor n^2/4\rfloor}\le G_n\le B_q q^{\lfloor n^2/4\rfloor}\) for a finite \(B_q\) independent of \(n\). Indeed, the losses from the maximal exponent are squares for even \(n\) and products of consecutive integers for odd \(n\). Consequently \(G_{n-1}/G_n=O_q(q^{-\lfloor n/2\rfloor})\).

Both zero-projection counts are \(G_m\). For subalgebras with \(u=1\), Gaussian Pascal, or partitioning the subspaces of an \(m\)-space according to whether they are contained in a fixed hyperplane, gives
\[
S_1={r\brack1}_q\sum_{t=1}^m {m-1\brack t-1}_q q^{m-t}
={r\brack1}_q(G_m-G_{m-1}).
\]
For general \(u\), put \(j=m-t\); the exponent from the two Gaussian bounds and the graph-map factor is \(u(r-u)+j(m-b+u-j)\). For \(u\ge2\) and \(b=u^2\), set \(D=u(u-1)\). Completing the square gives at most \(u(r-u)+(m-D)^2/4\) for each exponent. Its difference from \(m^2/4\) is
\[
u(r-u)-mD/2+D^2/4\le m/4-mD/4\le-m/4,
\]
since \(2\le D<m\) and \(u(r-u)\le m/4\). The upper bound for \(\sum_{u\ge2}S_u\) is therefore \(r(m+1)C_q^2 q^{m^2/4-m/4}=o(G_m)\). Since \({r\brack1}_q\to\infty\) and \(G_{m-1}/G_m\to0\), the line stratum dominates and \(|\mathcal S_r|\sim {r\brack1}_q G_m\).

For ideals with \(u\ge1\), \(m-b=(r-u)^2\), and completing the same square gives at most \(u(r-u)+((r-u)^2+u)^2/4\) for each exponent. On \(1\le u\le r\) the convex function \((r-u)^2+u\) is at most its larger endpoint value \(m-2r+2\). Hence
\[
\sum_{u\ge1} I_u\le r(m+1)C_q^2 q^{m/4+(m-2r+2)^2/4}=o(G_m).
\]
The displayed exponent is \(m^2/4-r^3+O(r^2)\). Thus \(|\mathcal I_r|\sim G_m\), with the zero-projection stratum dominant. Dividing and using \({r\brack1}_q=(q^r-1)/(q-1)\) proves the claim.

## Verification and scope

The proof holds for every fixed prime power, including characteristic two. The companion `verify_free2.py` checks the known counting input in four small examples using actual multiplication and evaluates the formulas in larger examples to illustrate the limits; neither calculation substitutes for the uniform estimates. Neither a joint field-size limit nor a statement about a degree-two exterior square or a general cube-zero algebra is claimed.

## Relationship to prior work

The finite-field formulas and the graph parametrization in [1] are not claimed as new. The concentration and sharp proportion require estimating and comparing the strata as the generator count grows; these limits are not stated there. Bauer and Schein [2] study ideal zeta functions over compact discrete valuation rings; Siconolfi, Vantomme and Voll [3] treat local subalgebra zeta functions of free class-two Lie rings. Neither setting there yields the fixed-field limit for the ordered tensor-square multiplication considered here. No exhaustive publication-priority assertion is made.

## References

1. *Subalgebra and ideal Grassmannians of free class-two Zinbiel algebras*, Resultary record `48b9d8c23c72`, Finding, “Complete joint finite-field spectra,” https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-subalgebra-and-ideal-grassmannians-of-free-class-two-zinbiel-alg--48b9d8c23c72.
2. T. Bauer and M. M. Schein, *Ideal growth in amalgamated powers of nilpotent rings of class two and zeta functions of quiver representations*, arXiv:2202.10865, Theorems 1.1–1.2.
3. V. Siconolfi, M. Vantomme and C. Voll, *Subgroup growth in free class-2-nilpotent groups*, arXiv:2305.19665, Proposition 4.4.
