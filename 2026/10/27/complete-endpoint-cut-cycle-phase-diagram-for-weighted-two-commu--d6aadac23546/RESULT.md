# Complete endpoint cut–cycle phase diagram for weighted two-community cliques

## Finding

For any integer \(n\ge3\), partition the vertices of a complete graph into two classes \(A,B\) of size \(n\) each. Assign conductance \(1\) to every edge within either class and conductance \(x^2\), for \(x>0\), to every edge joining the classes. Define
\[
I_Q=\frac{2(n-1+nx)}{n(1+x^2)},\qquad
I_P=\frac{nx^2+2nx+3n-6}{n(1+x^2)}.
\]
For \(0<x\le1\), put
\[
X_Q=\frac{nx^2+2nx+n-2x}{n(1+x^2)},\qquad
X_P=\frac{2(n-1)((n-1)x^2+nx+n+1)}{n^2(1+x^2)}.
\]
For \(x\ge1\), use instead
\[
X_Q=\frac{(3n^2-4n+2)x^2+2n(n-1)x-n^2+4n-2}{n^2(1+x^2)},
\]
\[
X_P=\frac{2(n-1)((2n-2)x^2+nx+2)}{n^2(1+x^2)}.
\]
The two definitions agree at \(x=1\). The exact real endpoint norms of the canonical orthogonal cut projection \(Q\) and its cycle complement \(P=I-Q\) are
\[
\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=\max\{I_Q,X_Q\},
\qquad
\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=\max\{I_P,X_P\}.
\]
Every edge of a given class has the corresponding column sum. The maximizing edge classes have an exact, nonuniform phase diagram:

- **Cut:** within-class for \(0<x<1\), cross-class for \(x>1\), and all edges tie at \(x=1\).
- **Cycle, \(n=3,4\):** cross-class for every \(x\ne1\), with all edges tied at \(x=1\).
- **Cycle, \(n=5\):** cross-class for \(0<x<3/7\), within-class for \(3/7<x<1\), cross-class for \(x>1\); both classes tie at \(x=3/7\) and at \(x=1\). This is a cross–within–cross reentrance under increasing cross conductance.
- **Cycle, \(n\ge6\):** within-class for \(0<x<1\), cross-class for \(x>1\), with a tie at \(x=1\).

The sharp conductance-optimized norms for each finite \(n\ge3\) are
\[
\max_{x>0}\|Q\|=1+\frac{n-1}{n^2}\sqrt{5n^2-8n+4},
\]
\[
\max_{x>0}\|P\|=\frac{n-1}{n^2}\left(2n+\sqrt{5n^2-16n+16}\right).
\]
The cut optimum occurs uniquely at
\[
x_Q=\frac{2(n-1)+\sqrt{5n^2-8n+4}}{n},
\]
and the cycle optimum occurs at
\[
x_P=\frac{2(n-2)+\sqrt{5n^2-16n+16}}{n}.
\]
For \(n\ge4\), \(x_P\) is the unique cycle optimizer. For \(n=3\), there are exactly two cycle optimizers, \(x_P=(2+\sqrt{13})/3\) and \(x_P^{-1}=(\sqrt{13}-2)/3\). In every dimension, \(x_P<x_Q\). The sharp suprema over all finite community sizes and positive conductances are
\[
\sup_{n\ge3,x>0}\|Q\|=1+\sqrt5,
\qquad
\sup_{n\ge3,x>0}\|P\|=2+\sqrt5,
\]
and neither is attained for finite \(n\).

## Assumptions and scope

All edge spaces are real and carry their standard coordinate \(\ell_1\), Euclidean, and \(\ell_\infty\) norms; these are not conductance-weighted \(\ell_1\) norms. Give every edge an arbitrary orientation and let \(B\) be the vertex-by-edge incidence matrix. With \(W\) the diagonal conductance matrix, define \(D=BW^{1/2}\), the weighted graph Laplacian \(L=DD^{\mathsf T}\), and
\[
Q=D^{\mathsf T}L^+D,\qquad P=I-Q.
\]
Here \(L^+\) is the Moore–Penrose inverse. Then \(Q\) is the Euclidean-orthogonal projection onto \(\operatorname{ran}D^{\mathsf T}\), and \(P\) is the Euclidean-orthogonal projection onto \(\ker D\). The definition is invariant under edge reorientation up to coordinate sign conjugacy, which does not change the claimed endpoint norms. All \(n\ge3\) and all \(x>0\) are included; no zero-conductance limit is asserted as an actual member.

## Proof

**1. Spectral reduction.** Write \(\mathbf1_A,\mathbf1_B\) for the class indicator vectors, and \(v=\mathbf1_A-\mathbf1_B\). Let \(H_A,H_B\) denote the centered-mean orthogonal projections within the two vertex classes. The weighted Laplacian has eigenvalue \(n(1+x^2)\) on each of the within-class zero-sum subspaces, eigenvalue \(2nx^2\) on the span of \(v\), and eigenvalue zero on constants. Consequently
\[
L^+=a(H_A+H_B)+\frac{vv^{\mathsf T}}{4n^2x^2},
\qquad a=\frac1{n(1+x^2)}.
\]
This identity holds for all \(x>0\); in particular no singular zero-weight limit is used.

**2. Within-class source.** For an oriented source edge \(u\to v\) within \(A\), the potential vector is \(h=L^+(e_u-e_v)=a(e_u-e_v)\). Its associated \(Q\) column has absolute entries \(2a\) on the source edge, \(a\) on each of the \(2(n-2)\) other incident edges within \(A\), \(xa\) on each of the \(2n\) cross edges incident to exactly one of \(u,v\), and zero elsewhere. Hence
\[
I_Q=2a+2(n-2)a+2nxa.
\]
Since \(Q_{ee}=2a\) and \(0<Q_{ee}<1\), replacing \(Q\) by \(P=I-Q\) changes the absolute column sum to \(I_P=1+I_Q-4a\), giving the displayed formulas. The other class is symmetric.

**3. Cross-class source.** For an oriented source \(u\to v\), \(u\in A,v\in B\), its normalized weighted incidence column is \(x(e_u-e_v)\). The potential is
\[
h=xa\left[(e_u-\mathbf1_A/n)-(e_v-\mathbf1_B/n)\right]
+\frac{v_0}{2n^2x},\qquad v_0=\mathbf1_A-\mathbf1_B.
\]
The \(2(n-1)\) internal edges incident to one source endpoint each carry absolute normalized current \(xa\). On cross edges, the normalized transfer current equals one of
\[
c_2=\frac{1+(2n-1)x^2}{n^2(1+x^2)},\qquad
c_1=\frac{1+(n-1)x^2}{n^2(1+x^2)},\qquad
c_0=\frac{1-x^2}{n^2(1+x^2)},
\]
with multiplicities \(1\), \(2(n-1)\), and \((n-1)^2\), according as both, one, or neither of their endpoints match a source endpoint. The only sign-changing class is \(c_0\), at \(x=1\). Therefore
\[
X_Q=2(n-1)xa+c_2+2(n-1)c_1+(n-1)^2|c_0|,
\qquad X_P=1+X_Q-2c_2.
\]
Here \(0<c_2<1\), since \(n\ge3\); the cycle diagonal term is \(1-c_2\ge0\). Expanding these two formulas separately on \(0<x\le1\) and \(x\ge1\) yields exactly the two stated rational branches. The real \(\ell_1\) induced norm is the maximum of absolute column sums, and symmetry of both projection matrices gives the same \(\ell_\infty\) induced norm.

**4. Maximizing-edge phase diagram.** For \(0<x<1\), direct factorization gives
\[
X_Q-I_Q=\frac{(x-1)(nx+n-2)}{n(1+x^2)}<0,
\]
whereas for \(x>1\),
\[
X_Q-I_Q=\frac{(x-1)[(3n^2-4n+2)x+3n^2-6n+2]}{n^2(1+x^2)}>0.
\]
For the cycle projection, the corresponding difference is, on \(0<x<1\),
\[
X_P-I_P=\frac{(x-1)[(n^2-4n+2)x+n^2-6n+2]}{n^2(1+x^2)},
\]
and on \(x>1\),
\[
X_P-I_P=\frac{(x-1)[(3n^2-8n+4)x+3n^2-10n+4]}{n^2(1+x^2)}>0.
\]
For \(n=3,4\), the bracket in the first cycle expression is negative throughout \(0<x<1\); for \(n=5\) it is \(7x-3\); and for \(n\ge6\) it is positive. This proves all strict regions and ties, including the single reentrant size \(n=5\).

**5. Global conductance optima.** Let \(z>1\) and compare values on the weak-cross side with those at \(z\). The following positive comparisons are exact:
\[
X_Q(z)-I_Q(1/z)=\frac{(z-1)[(n^2-2n+2)z+n^2-4n+2]}{n^2(1+z^2)}>0,
\]
\[
X_P(z)-I_P(1/z)=\frac{(z-1)[(n^2-2n+4)z+(n-2)^2]}{n^2(1+z^2)}>0,
\]
\[
X_P(z)-X_P(1/z)=\frac{2(n-3)(n-1)(z-1)(z+1)}{n^2(1+z^2)}\ge0.
\]
The first bracket is positive at \(z=1\), and its slope is positive. In the last comparison equality holds throughout precisely when \(n=3\). Thus every cut optimum and (except for reciprocal equality when \(n=3\)) every cycle optimum must occur on \(x>1\). There the two objective branches have respective derivatives with signs opposite to
\[
nx^2-4(n-1)x-n,\qquad nx^2-4(n-2)x-n.
\]
Each quadratic has exactly one positive root; it lies above one and gives a strict global maximum. These roots are \(x_Q\) and \(x_P\) stated above. The maximizing value of a quotient \((Ax^2+Bx+C)/(1+x^2)\) at its positive stationary point (for \(B>0\)) is \((A+C+\sqrt{(A-C)^2+B^2})/2\). Applying it to the two cross-class branches gives both optimized norms. Since \(x-1/x\) strictly increases for \(x>0\), the stationary equations imply \(x_Q>x_P\). For \(n=3\), the last identity above and strict comparisons with the other column class imply exactly one additional cycle maximizer at \(x_P^{-1}\).

**6. Bounds across sizes.** Rewrite the optimized cut norm as
\[
1+\left(1-\frac1n\right)\sqrt{\left(2-\frac2n\right)^2+1},
\]
and the cycle norm as
\[
\left(1-\frac1n\right)\left[2+\sqrt{\left(2-\frac4n\right)^2+1}\right].
\]
For every integer \(n\ge3\), these are strictly smaller than \(1+\sqrt5\) and \(2+\sqrt5\), respectively, since both prefactors are below one and the square-root arguments are strictly below five. Each expression tends to its claimed bound as \(n\to\infty\), proving sharpness without finite attainment.

## Verification

The accompanying standard-library checker `two_community_checker.py` constructs the grounded weighted Laplacian directly and inverts it with exact rational arithmetic, independently of the closed-form pseudoinverse above. It verifies every within- and cross-class projection column, both claimed absolute sums and all stated edge-class inequalities, for \(n=3,4,5,6,7,8\) at each of the rational weights \(x=1/5,3/7,2/3,4/5,1,6/5,2,3,5\). The successful run reported `TWO_COMMUNITY_HODGE_EXACT_OK graphs=54 verified_full_columns=3285`. Infinite-family correctness rests on the symbolic proof, not on this finite sample.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii's 2023 paper [1] develops invariant and minimal cycle-space projections, focusing on discrete tori and Hamming graphs; its introduction and named main graph-family sections do not state the present weighted two-community classification. Schild, Rao and Srivastava [2] bound aggregate electrical-flow localization and the absolute transfer-impedance operator for general networks, without these exact edge-orbit formulas. Gurel-Gurevich, Nachmias and Sachdeva [3] strengthen general localization bounds and explicitly use the same symmetrized weighted transfer-current operator, but do not provide the above parameter-by-parameter endpoint classification. These standard methods are acknowledged rather than claimed as new.

## Limitations

Only two equally sized complete vertex classes, equal conductances within each class, uniform positive conductance across classes, real coordinate norms and canonical Euclidean-orthogonal projections are treated. The theorem does not optimize among all possible nonorthogonal projections, extend to arbitrary inhomogeneous conductances or determine intermediate \(\ell_p\) norms. A less-indexed electrical-network computation could independently encode an equivalent endpoint formula, so originality is assessed with that residual risk. No independent mathematical audit has been performed.

## References

[1] S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1, first public 2023-05-21, https://arxiv.org/abs/2305.12582.

[2] A. Schild, S. Rao, N. Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632v1, 2017, https://arxiv.org/abs/1708.01632.

[3] O. Gurel-Gurevich, A. Nachmias, S. Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130v1, 2026, https://arxiv.org/abs/2605.24130.
