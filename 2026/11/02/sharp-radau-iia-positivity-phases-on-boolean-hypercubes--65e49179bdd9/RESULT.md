# Sharp Radau IIA positivity phases on Boolean hypercubes

## Finding

Let \(Q_d\) be the unweighted Boolean hypercube of dimension \(d\ge 1\), with combinatorial graph Laplacian \(L_d\). The third-order, two-stage Radau IIA endpoint matrix for continuous-time diffusion \(u'=-L_du\) is
\[
M_d(h)=\mathcal R(hL_d),\qquad
\mathcal R(z)=\frac{6-2z}{z^2+4z+6},\qquad h\ge0.
\]
It is symmetric and has every row and column sum equal to one. Entrywise nonnegativity, however, has the following sharp dimension-dependent classification.

1. For \(1\le d\le3\), every \(M_d(h)\) is entrywise nonnegative, and every entry is strictly positive for \(h>0\).
2. For \(d=4\), there are exactly two positive real roots \(\alpha_4<\beta_4\) of
   \[
   Q_4(h)=192h^8-848h^7-1300h^6+168h^5+2242h^4
      +2216h^3+1050h^2+252h+27.
   \]
   Then \(M_4(h)\) is nonnegative exactly for \(h\in[0,\alpha_4]\cup[\beta_4,\infty)\), with \(\alpha_4\approx1.4654672552\) and \(\beta_4\approx5.5299494705\). All off-diagonal entries are strictly positive at every positive step; only the diagonal becomes negative.
3. For \(d=5\), put
   \[
   \begin{aligned}
   Q_5(h)={}&4800h^{10}-49040h^9-126924h^8-119100h^7-2890h^6\\
      &+78470h^5+71146h^4+31950h^3+8325h^2+1215h+81,\\
   G_5(h)={}&160h^5+1096h^4+1350h^3+510h^2+45h-3.
   \end{aligned}
   \]
   The polynomial \(G_5\) has a unique positive root \(\gamma_5\), and \(Q_5\) has exactly two positive roots \(\alpha_5<\beta_5\). They satisfy \(0<\gamma_5<\alpha_5<\beta_5\). The precise nonnegative-step set is
   \[
   \boxed{\{0\}\cup[\gamma_5,\alpha_5]\cup[\beta_5,\infty).}
   \]
   Numerically \(\gamma_5\approx0.04311268053\), \(\alpha_5\approx0.88788076468\), and \(\beta_5\approx12.49200993298\). The short-step obstruction lies at distance five, whereas the intermediate-step obstruction lies on the diagonal.
4. In every dimension \(d\ge5\), for vertices \(x,y\) with Hamming distance five,
   \[
   (M_d(h))_{xy}=-\frac{10}{9}h^5+O_d(h^6)\quad(h\downarrow0).
   \]
   Thus arbitrarily small positive steps fail nonnegativity in every such dimension. Moreover, the diagonal is strictly negative at \(h=3/2\) in every dimension \(d\ge4\). Nevertheless, for each fixed finite dimension \(d\), all entries are strictly positive for every sufficiently large \(h\).

In particular, the universal-in-step positivity cutoff for this natural graph family is exactly dimension three; dimension four has one bounded forbidden interval, and dimension five has a disjoint short-step forbidden interval as well as an intermediate one. The assertion for \(d\ge6\) specifies the small-step and one fixed intermediate-step obstructions and eventual recovery, not a complete list of all intermediate intervals.

## Assumptions and scope

The vertex set of \(Q_d\) is \(\{0,1\}^d\). Two vertices are adjacent exactly when their Hamming distance is one; every edge has unit conductance, so \(L_d=dI-A_d\). No mesh normalization, vertex-dependent weights, intermediate-stage positivity condition, or adaptive steps are assumed. The property tested is **entrywise nonnegativity of the accepted one-step endpoint matrix**: it is stronger than nonnegativity for selected initial data, but different from positivity of internal Runge--Kutta stages. The step \(h=0\) gives the identity matrix.

Let \(m_{d,r}(h)\) denote a matrix entry at Hamming distance \(r\). For \(0\le r\le d\), define
\[
 c_{d,r,k}=\sum_{j=\max(0,k-d+r)}^{\min(r,k)}(-1)^j
 \binom rj\binom{d-r}{k-j},\qquad 0\le k\le d.
\]
The following finite Walsh sum exactly defines every entry:
\[
 m_{d,r}(h)=2^{-d}\sum_{k=0}^{d}c_{d,r,k}\mathcal R(2kh).
\]
No conclusion is asserted about nonuniform or directed hypercube weights, other RK stability functions, or repeated products of possibly signed endpoint matrices.

## Proof

**1. Spectral reduction.** For every subset \(S\subseteq\{1,\ldots,d\}\), the Walsh character \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) is a Laplacian eigenvector of eigenvalue \(2|S|\). The normalized Walsh transform diagonalizes \(L_d\). Summing over subsets of cardinality \(k\) according to their intersection with the \(r\) differing coordinates yields the displayed formula for \(m_{d,r}\). Since \(\mathcal R(0)=1\), every row and column sum of \(M_d(h)\) is one. All denominators in the Walsh formula are strictly positive for \(h\ge0\).

**2. Dimensions at most three.** The rational expressions for dimensions one and two have positive-coefficient numerators after factoring \(h^r\) at distance \(r>0\). For dimension three all four shells share the positive denominator
\[
 D_3=(2h^2+4h+3)(6h^2+4h+1)(8h^2+8h+3).
\]
Their respective numerators, for distances zero through three, are
\[
 \begin{array}{ll}
 12h^6-14h^5+22h^4+83h^3+98h^2+45h+9,\\
 h(12h^5+42h^4+92h^3+95h^2+45h+9),\\
 h^2(12h^4+58h^3+76h^2+45h+9),\\
 3h^3(4h^3+22h^2+18h+3).
 \end{array}
\]
The only apparent negative coefficient, in the first row, belongs to \(h^4(12h^2-14h+22)\); the quadratic is strictly positive because its discriminant is negative. Consequently every shell is positive when \(h>0\). The remaining dimensions are checked by the same rational Walsh identity; their explicit, coefficientwise-positive numerator and denominator identities are independently reconstructed in the supplied verifier.

**3. Exact four-dimensional phase.** Put
\[
 D_4=(2h^2+4h+3)(6h^2+4h+1)(8h^2+8h+3)(32h^2+16h+3).
\]
The diagonal entry is \(m_{4,0}=Q_4/D_4\). The four off-diagonal Hamming-distance numerators, using their respective positive denominators, are
\[
\begin{array}{ll}
 r=1:&h(24h^5+50h^4+168h^3+163h^2+60h+9),\\
 r=2:&h^2(16h^2+36h+9),\\
 r=3:&3h^3(8h^3+38h^2+24h+3),\\
 r=4:&6h^4(32h^4+200h^3+210h^2+60h+3).
\end{array}
\]
Their denominators are respectively the products of factors \((A,B,D)\), \((C,D)\), \((A,B,D)\), \((A,B,C,D)\), where \(A=2h^2+4h+3\), \(B=6h^2+4h+1\), \(C=8h^2+8h+3\), \(D=32h^2+16h+3\). All are strictly positive for \(h>0\). The coefficient signs of \(Q_4\), from largest degree down, have exactly two changes. Descartes' rule therefore permits at most two positive roots counting multiplicity. Since \(Q_4(0)>0\), \(Q_4(3/2)<0\), and \(Q_4(h)\to+\infty\), there are exactly two distinct positive roots, with the stated sign pattern.

**4. Exact five-dimensional phase.** Let \(E=50h^2+20h+3\) and \(D_5=D_4E\). The diagonal entry is \(m_{5,0}=Q_5/D_5\), and the antipodal entry is \(m_{5,5}=30h^5G_5/D_5\). The four remaining entries are \(m_{5,r}=h^rU_r/D_5\) with
\[
\begin{aligned}
U_1={}&4800h^9+10480h^8+45540h^7+98956h^6+114450h^5\\
 &+77674h^4+32400h^3+8298h^2+1215h+81,\\
U_2={}&4800h^8+22960h^7+57676h^6+79040h^5+61358h^4\\
 &+28530h^3+7884h^2+1215h+81,\\
U_3={}&3(1600h^7+9360h^6+17860h^5+17504h^4+9450h^3\\
 &+2850h^2+450h+27),\\
U_4={}&6(800h^6+5160h^5+7846h^4+5250h^3+1755h^2\\
 &+255h+9).
\end{aligned}
\]
Thus those four shells are positive at every positive step. The signs of the nonzero coefficients of \(Q_5\) have exactly two changes; \(Q_5(1/2)>0\), \(Q_5(3/2)<0\), and the leading coefficient is positive. Therefore \(Q_5\) has exactly two positive roots, the first in \((1/2,3/2)\), the second beyond \(3/2\). The derivative \(G_5'(h)\) has strictly positive coefficients for \(h\ge0\), while \(G_5(0)<0<G_5(1/10)\), so it has exactly one positive root below \(1/10\). Their ordering and the exact positive windows follow.

**5. Uniform small-step and intermediate-step obstructions.** The scalar Taylor series begins
\[
 \mathcal R(z)=1-z+\frac{z^2}{2}-\frac{z^3}{6}+\frac{z^4}{36}+\frac{z^5}{108}+O(z^6).
\]
For distinct vertices separated by five edges, the first possibly nonzero off-diagonal power of \(L_d\) is the fifth; its entry is \((-1)^5 5!=-120\), because there are exactly \(5!\) shortest paths. Consequently the leading term of \(M_d(h)_{xy}\) is \(-120h^5/108=-10h^5/9\) in every dimension \(d\ge5\).

At \(h=3/2\), the diagonal is
\[
 2^{-d}\Bigl[1-\sum_{k=2}^d\binom dk a_k\Bigr],\qquad
 a_k=-\mathcal R(3k)>0\quad(k\ge2),
\]
with \(\mathcal R(3)=0\). The sum for \(d=4\) equals \(463/451>1\); it increases strictly with \(d\) by Pascal's identity. Hence the diagonal is negative at this step for all \(d\ge4\). Finally, \(\mathcal R(2kh)\to0\) as \(h\to\infty\) whenever \(k\ge1\), so the Walsh formula yields \(M_d(h)\to 2^{-d}\mathbf1\mathbf1^{\mathsf T}\). The convergence is entrywise and each finite matrix is therefore eventually strictly positive.

## Verification

The accompanying self-contained `verify.py` uses only the Python standard library and exact rational arithmetic. It constructs the Walsh-shell rational functions from their binomial sums, cross-multiplies polynomial coefficients to verify every displayed low-dimensional numerator and denominator identity, checks the Descartes/sign certificates, independently assembles and inverts endpoint matrices through dimension five at selected rational timesteps, and tests many additional exact rational samples. Its successful invocation produced `VERIFY_OK 12593 exact assertions`.

The executable checks are supplementary. The infinite-dimension statements depend on the Walsh diagonalization, fifth-distance Taylor coefficient, the Pascal-identity monotonicity argument, and the finite-dimensional spectral limit proved above. Numerical root approximations are illustrative; the exact bounds use algebraically specified roots and rational sign witnesses.

## Relationship to prior work

Lóczi and Ketcheson study rational stability functions through absolute-monotonicity radii and exact algebraic optimization [1]. That general methodology explains why positivity is a relevant RK property, but neither a radius bound nor a generic obstruction determines the actual endpoint-entry signs for a fixed graph at intermediate or very large steps. Higueras, Ketcheson and Kocsis study monotonicity-preserving *perturbations* of RK methods [2], whereas the present matrix uses the unmodified classical two-stage Radau IIA function. Blanes, Iserles and Macnamara discuss positivity-preserving integration for graph-Laplacian systems and the classical RK positivity order barrier [3]; their work does not state these exact hypercube shell thresholds or two algebraic positivity windows. A historical survey of Radau methods fixes the method's numerical context [4].

The specific new mathematical content assessed here is the sharp all-dimension cutoff, the exact four- and five-dimensional positivity domains, and the distance-five sign mechanism. The fact that some high-order RK methods fail universal positivity, and that finite-dimensional rational functions can regain positivity, is not claimed as new. This graph-specific statement is neither a classification of all RK schemes nor a universal Markov-chain obstruction.

## Limitations

The exact complete step domains are proved only through dimension five. In dimensions six and above, the proof shows a short-step forbidden neighborhood, negativity at the explicit step \(3/2\), and eventual positivity, but does not enumerate other possible phase windows. The finite verifier is not an independent audit and does not substitute for analytic statements. Similar hypercube-specialized results might exist in older unindexed literature; the novelty comparison rests on the specified checked sources and searches, not on a proof of worldwide uniqueness.

## References

[1] L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, first arXiv version 26 March 2013, https://arxiv.org/abs/1303.6651.

[2] I. Higueras, D. I. Ketcheson and T. A. Kocsis, *Optimal monotonicity-preserving perturbations of a given Runge–Kutta method*, first arXiv version 15 May 2015, https://arxiv.org/abs/1505.04024.

[3] S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, https://arxiv.org/abs/2102.08242.

[4] E. Hairer and G. Wanner, *Stiff differential equations solved by Radau methods*, Journal of Computational and Applied Mathematics 111 (1999), 93–111, https://doi.org/10.1016/S0377-0427(99)00134-X.
