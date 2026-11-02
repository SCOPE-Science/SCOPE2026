# Cardinality spectrum and boundary-size law for \(P_3\)-convex sets on open ladders

## Finding
For the open two-row ladder \(L_n=P_n\square K_2\), write
\[F_n(z)=\sum_{S\subseteq V(L_n),\ S\ P_3\text{-convex}}z^{|S|},\qquad F_0(z)=1.\]
Here each vertex outside a \(P_3\)-convex set has at most one neighbor inside the set. Define
\[\begin{aligned}
D(t,z)&=1-(1+z+z^2)t+(z^2+z^3)t^2-(z+z^2)t^3+2z^3t^4+z^3t^5,\\
N(t,z)&=1+zt+(z+z^2-2z^3)t^2-3z^3t^3-z^3t^4.
\end{aligned}\]
Then, as an identity of formal power series in \(t\) over \(\mathbb Z[z]\),
\[\boxed{\sum_{n\ge0}F_n(z)t^n=\frac{N(t,z)}{D(t,z)}.}\]
Consequently every exact cardinality count is obtained by coefficient extraction; for example,
\[\begin{aligned}
F_3(z)&=1+6z+9z^2+2z^3+2z^4+z^6,\\
F_4(z)&=1+8z+18z^2+12z^3+6z^4+2z^6+z^8.
\end{aligned}\]

There is also a sharp boundary correction for the size of a uniformly selected \(P_3\)-convex set. Let \(K_n=|S|\) under the uniform distribution on the \(F_n(1)\) eligible sets. Let \(r\) be the smallest positive root of \(D(t,1)=0\); it is simple and \(r\approx0.432450402724258\). Let \(r(z)\) denote the analytic root of \(D(r(z),z)=0\) with \(r(1)=r\), and let
\[c(z)=-\frac{N(r(z),z)}{r(z)D_t(r(z),z)}.\]
With derivatives evaluated at \(z=1\), put
\[\mu=-\frac{r'}r,\qquad \sigma^2=-\frac{r''+r'}r+\left(\frac{r'}r\right)^2,\qquad \beta=\frac{c'}c.\]
All three constants are algebraic and satisfy
\[\mu\approx0.514909291163714,\quad \sigma^2\approx0.359892854829278>0,\quad \beta\approx0.521089733595278.\]
For some \(0<\theta<1\), as \(n\to\infty\),
\[\boxed{\mathbb E K_n=\mu n+\beta+O(\theta^n),\qquad \operatorname{Var}K_n=\sigma^2n+O(1),}\]
and
\[\boxed{\frac{K_n-\mu n}{\sqrt{\sigma^2n}}\ \xrightarrow{\mathrm d}\ \mathcal N(0,1).}\]
The nonzero \(\beta\) measures the finite-strip boundary contribution to the expected number of selected vertices. The mean density per vertex tends to \(\mu/2\), since there are \(2n\) vertices.

## Assumptions and scope
The ladder has \(n\ge1\) rungs and the two vertices of each rung are joined by an edge; adjacent rungs have two horizontal edges. A \(P_3\)-convex set means a vertex subset \(S\) such that every vertex in \(V(L_n)\setminus S\) has at most one neighbor in \(S\). This definition allows the empty and full sets, uses ordinary (not induced-only) length-two paths, and counts labeled vertex subsets, not isomorphism classes. The dummy object \(L_0\) is empty and contributes \(F_0(z)=1\). The limit law uses the uniform distribution among the allowable subsets for a given \(n\).

## Proof
Encode the selection in each rung by a mask in \(\{0,1,2,3\}\); bit \(j\in\{0,1\}\) indicates whether the row-\(j\) vertex is selected. For consecutive masks \(a,b,c\), define \(I(a,b,c)=1\) precisely when, for both rows \(j\),
\[b_j=0\ \Longrightarrow\ a_j+b_{1-j}+c_j\le1.\]
Thus \(I(a,b,c)=1\) if and only if the central rung obeys the \(P_3\)-convexity condition. Enumerate the sixteen ordered pairs \((a,b)\). Let \(T(z)\) be the sixteen-by-sixteen matrix whose \(((a,b),(b,c))\)-entry is \(I(a,b,c)z^{b_0+b_1}\), and whose other entries vanish. Let \(u_{(a,b)}=\mathbf1_{a=0}\) and \(v_{(a,b)}=\mathbf1_{b=0}\). Then the missing rungs at either end are the all-zero dummy masks, and a state walk has exactly the weight of its unique selected-vertex subset. Therefore
\[F_n(z)=uT(z)^nv\quad(n\ge0),\qquad \sum_{n\ge0}F_n(z)t^n=u(I-tT(z))^{-1}v.\]
Exact rational-function elimination (reproducible in the accompanying verifier) yields
\[u(I-tT(z))^{-1}v=\frac{N(t,z)}{D(t,z)}.\]
In addition the exact characteristic identity is
\[\det(I-tT(z))=(1-zt+zt^2)D(t,z).\]
The rational identity, not finitely many initial coefficients, proves the enumeration for every \(n\). At \(z=1\), the totals start \(1,4,10,21,48,113,261,601,1390\), agreeing with the older scalar sequence from the second rung onward. Its first entry differs: the one-rung ladder has degree-one vertices, and the published strict-majority convention excludes mixed entries there while ordinary \(P_3\)-convexity permits all four subsets.

For the limit law, the nonzero transitions contain a strongly connected ten-state component with self-loops of different weights. Its Perron eigenvalue at \(z=1\) is \(\lambda=1/r\approx2.312403905049955\); all other eigenvalues have strictly smaller modulus. The end vectors have a positive Perron projection. This also follows directly from the five roots of \(D(t,1)\), since \(r\) is the unique pole closest to zero and its numerator is nonzero. Analytic perturbation and the simple-pole residue formula thus give, uniformly for complex \(z\) in a sufficiently small neighborhood of one,
\[F_n(z)=c(z)r(z)^{-n}\bigl(1+O(\theta^n)\bigr).\]
Here \(c(1)\approx1.70049779301899\) is positive. Normalizing this expression at \(z=1\), taking the logarithm, and replacing \(z\) by \(e^s\) gives
\[\log\mathbb E e^{sK_n}=n\log\frac{r(1)}{r(e^s)}+\log\frac{c(e^s)}{c(1)}+O(\theta^n).\]
The first and second derivatives at \(s=0\) yield the displayed expectation and variance, with the first derivative of the second summand giving \(\beta\). The variance constant is strictly positive; equivalently, the essential transition component contains one-step loops of different selected-vertex weights, so its additive weight cannot have zero asymptotic variance. Expanding the same logarithm at \(s=i x/\sqrt n\) proves the central limit theorem by characteristic functions.

For explicit evaluation, implicit differentiation of \(D(r(z),z)=0\) gives
\[r'=-D_z/D_t,\qquad r''=-(D_{tt}(r')^2+2D_{tz}r'+D_{zz})/D_t\]
at \((t,z)=(r,1)\). Likewise,
\[\beta=\frac{N_z+N_t r'}{N}-\frac{r'}r-\frac{D_{tz}+D_{tt}r'}{D_t},\]
where all derivatives and polynomial values on the right are evaluated at \((r,1)\). These formulas establish the stated numerical constants by algebraic root isolation and substitution.

## Verification
Run the standalone `verify.py` with Python 3.10+ and SymPy. It reconstructs the matrix independently from the local condition, checks both rational and determinant polynomial identities symbolically, enumerates all \(2^{2n}\) subsets directly for every \(1\le n\le8\), and checks the resulting cardinality polynomials against the transfer coefficients. Its tested run returned `VERIFY_OK open_cases=8 examined_subsets=87380 weighted_matrix_identities=2 mu=0.514909291164 variance=0.359892854829`. The finite enumeration is a cross-check: infinite validity follows from the matrix identity and analytic argument above.

## Relationship to prior work
Dourado, Grippo, Lin, and Protti (2026) formulate and study enumeration of \(P_3\)-convex graph subsets, including general counting complexity and algorithms for trees and threshold graphs. They do not give the open-ladder bivariate polynomial or its boundary-size law. R. H. Hardin's older OEIS A231376 already counts the same \(n\)-rung two-row binary arrays at \(z=1\) for \(n\ge2\); the one-rung count differs because the strict-majority threshold at degree one is more restrictive than ordinary \(P_3\)-convexity; an unweighted recurrence and an empirical scalar generating function are also recorded there. **Those unweighted totals, their growth constant, and the existence of scalar recurrences are not claimed as new.** The result here refines the known scalar sequence to every cardinality and gives an explicit sharp boundary constant and Gaussian fluctuations. Closely related circular-ladder enumerators have the same bulk quintic factor; the result does not claim the circular case and the boundary numerator is a distinct calculation.

## Limitations
This theorem applies to two-row open path ladders and ordinary \(P_3\)-convexity. It does not enumerate wider strips, cylindrical or twisted boundaries, or symmetry orbits. The Gaussian limit is for a uniformly chosen admissible subset; it does not assert a local limit theorem. Numerical decimal approximations are not substitutes for the exact algebraic definitions. Existing unweighted sequences and related cyclic transfer formulas substantially overlap with the method, and earlier work under equivalent majority-stable binary-array terminology may contain an undiscovered size-refined formula. No independent external mathematical audit has been performed.

## References
- M. C. Dourado, L. N. Grippo, M. C. Lin, and F. Protti, *Counting P3-convex sets in graphs*, arXiv:2603.04706v1, first posted 2026-03-05, https://arxiv.org/html/2603.04706v1.
- R. H. Hardin, OEIS A231376, *Number of n X 2 0..1 arrays with no element less than a strict majority of its horizontal and vertical neighbors*, entry dated 2013-11-08; scalar generating function attributed there to C. Barker, 2018, https://oeis.org/A231376.
