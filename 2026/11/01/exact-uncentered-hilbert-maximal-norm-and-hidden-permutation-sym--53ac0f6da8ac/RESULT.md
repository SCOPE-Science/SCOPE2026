# Exact uncentered Hilbert maximal norm and hidden permutation symmetry on the four-cycle

## Finding

Let \(C_4\) be the unweighted simple four-cycle, endowed with counting measure and graph-distance closed balls. For a real function \(f\), define the uncentered Hardy–Littlewood maximal operator by
\[
\widetilde M f(v)=\max_{B\ni v}\frac{1}{|B|}\sum_{w\in B}|f(w)|,
\]
where \(B\) ranges over all nonempty graph-distance balls with any center. The exact, attained strong Hilbert operator norm is
\[
\boxed{\|\widetilde M\|_{\ell^2(C_4)\to\ell^2(C_4)}=\sqrt{\lambda_*}=1.2283685567782074\ldots},
\]
where \(\lambda_*\) is the unique real root greater than one of
\[
\boxed{81z^3-162z^2+64z-6=0},\qquad
\frac{377}{250}<\lambda_*<\frac{151}{100}.
\]
Define the positive numbers
\[
 a=\frac{\lambda_*-1}{\lambda_*},\quad
 b=\frac{2(2\lambda_*-1)}{\lambda_*(9\lambda_*-2)},\quad
 c=\frac{2\lambda_*-1}{\lambda_*(9\lambda_*-1)}.
\]
They satisfy \(1>a>b>c>0\) and \(a=b+c\). Every nonzero real extremizer is obtained from the absolute-value vector \((1,a,b,c)\) by an arbitrary permutation, independent changes of coordinate signs and nonzero scalar multiplication. There are exactly \(24\) labeled nonnegative extremizing rays. These form three orbits of eight under the graph automorphism group of \(C_4\), distinguished by which smaller value occurs at the vertex opposite the largest value.

Moreover, if \(M_c\) denotes the **centered** maximal operator for the same graph and measure, then
\[
\boxed{\|M_c\|_{2\to2}^{\,2}<\frac{377}{250}<\|\widetilde M\|_{2\to2}^{\,2}}.
\]
Thus the centered and uncentered norms differ strictly. Although \(C_4\) has only dihedral graph symmetries, its uncentered maximal operator commutes with **all \(24\) permutations** of its vertices.

## Assumptions and scope

All vertices and balls carry counting measure; graph edges have unit length; closed graph-metric balls have radii \(0,1,2\) up to repetitions. The domain and codomain are real \(\ell^2\) on four vertices. In evaluating maximal operators, absolute values are taken before averaging. The norm means the best constant for all real inputs, not a linearized derivative or variation seminorm.

## Proof

**1. Accidental symmetry and exact nonlinear reduction.** The distinct balls of \(C_4\) consist of its four singleton sets, all four three-element vertex subsets, and the entire vertex set. The latter fact follows because the radius-one ball centered at a vertex is the complement of its opposite vertex. Hence the complete family of balls is invariant under the full symmetric group \(S_4\), not merely the dihedral graph automorphism group.

After taking absolute values and permuting coordinates, write \(u\ge v\ge w\ge z\ge0\), and set
\[
S=\frac{u+v+w}{3},\qquad T=\frac{u+v+z}{3},\qquad m=\frac{u+v+w+z}{4}.
\]
The maximal output, in this same ordered coordinate labeling, is exactly
\[
\widetilde M(u,v,w,z)=\big(u,\max\{v,S\},S,\max\{T,m\}\big).
\]
Indeed, the best triple containing any of the first three indices is the triple of the three largest inputs; the best triple containing the fourth index replaces \(w\) by \(z\); the full average cannot exceed \(S\). Since averages never exceed the largest coordinate, the first output is exactly \(u\).

Consequently, the squared operator norm is bounded above by the largest spectral norm squared of four linear row matrices, formed by choosing either \(v\) or \(S\) in output two and either \(T\) or \(m\) in output four. In particular the candidate winning matrix is
\[
A=\begin{pmatrix}
1&0&0&0\\
1/3&1/3&1/3&0\\
1/3&1/3&1/3&0\\
1/3&1/3&0&1/3
\end{pmatrix}.
\]

**2. Exact exclusion of competing branches.** Put \(q=377/250\). For each of the other three row matrices \(B\), the four leading principal minors of \(qI-B^{\mathsf T}B\) are positive by exact rational arithmetic (recomputed by the standalone verifier). Sylvester's criterion gives \(\|B\|_{2\to2}^2<q\). The candidate matrix instead satisfies the exact characteristic identity
\[
\det(sI-A^{\mathsf T}A)=\frac{s}{81}(81s^3-162s^2+64s-6).
\]
For \(P(s)=81s^3-162s^2+64s-6\), one has
\[
P(q)=-1781227/15625000<0,\qquad
P(151/100)=142831/1000000>0.
\]
Because \(P(1)<0\) and \(P''(s)=486s-324>0\) for \(s\ge1\), there is precisely one root above one and it lies in the displayed interval. It is the largest eigenvalue of the nonnegative irreducible Gram matrix \(A^{\mathsf T}A\); this also follows from the positive eigenvector constructed next.

**3. Attainment and all equality cases.** Let \(\lambda=\lambda_*\), and set \(x=(1,a,b,c)^{\mathsf T}\) as above. Direct rational identities imply
\[
\lambda a=\lambda-1,\quad
\lambda b=\frac{2S_x}{3},\quad
\lambda c=\frac{T_x}{3},\quad
\lambda=1+\frac{2S_x}{3}+\frac{T_x}{3},
\]
where \(S_x=(1+a+b)/3\) and \(T_x=(1+a+c)/3\). The last two identities use \(P(\lambda)=0\), and together give \(A^{\mathsf T}Ax=\lambda x\). Exact factorization also yields
\[
\lambda(9\lambda-2)(9\lambda-1)(a-b-c)=P(\lambda)=0.
\]
Rational interval bounds throughout \((q,151/100)\) give \(1>a>b>c>0\), \(S_x>a\), and \(T_x>(1+a+b+c)/4\); therefore the nonlinear branch is **strictly** the matrix \(A\) at \(x\). Thus \(x\) attains its spectral norm, and the upper bound in Step 2 is sharp.

For any extremizer, sort its absolute coordinates. Because each competing branch has squared norm strictly below \(q<\lambda\), its active branch must be \(A\), and it must maximize the Rayleigh quotient of \(A^{\mathsf T}A\). This Gram matrix has a connected positive-entry graph, so its Perron eigenvalue is simple; therefore its positive maximizing ray is exactly \(\mathbb R_{>0}x\). All four entries of \(x\) differ, giving \(4!=24\) distinct nonnegative labeled rays. The dihedral group of order eight acts freely on each such ray, giving three orbits. Independent input signs do not alter the maximal averages, so all real equality cases have the stated description.

**4. Independent strict centered–uncentered comparison.** For the centered operator the choices at each of four vertices are the singleton ball, its own three-vertex radius-one ball, or the four-vertex ball. Thus \(M_c\) is the pointwise maximum of \(3^4=81\) finite row selections. The supplied exact-arithmetic verifier checks that all four leading principal minors of \(qI-B^{\mathsf T}B\) are positive for **every one** of these 81 matrices. It follows from Sylvester's criterion that \(\|M_c\|_{2\to2}^2<q\), which completes the claimed strict separation.

## Verification

Run \(`python3 verify_c4_uncentered.py`\) with Python 3 and no external dependencies. The verifier uses \(`fractions.Fraction`\) throughout for the four candidate branches, three strict spectral exclusions, characteristic polynomial, exact algebraic identities, positive eigenvector interval bounds, and all \(81\) centered selection matrices. This is an exhaustive **finite** certificate for the specified four-vertex graph, not a numerical extrapolation to other graph orders. The proof of the uniqueness of the root and the full equality classification is analytic and is given above.

## Relationship to prior work

Soria and Tradacete (arXiv:1410.6204, first publicly posted 2014-10-22) establish foundational finite-graph Hardy–Littlewood maximal estimates, with principal sharp \(\ell^p\) graph results in the range \(0<p\le1\). González-Riquelme and Madrid (arXiv:2005.03146 and arXiv:2011.02630) give exact Hilbert norm information for **centered** operators on complete graphs and stars and related variation results. Their inspected statements do not supply the uncentered four-cycle cubic or its complete equality classification. The centered four-cycle, the uncentered five-cycle and the uncentered four-vertex path concern different set systems; neither their constants nor their equality cases imply the present result. The genuinely distinguishing mechanism here is that the radius-one balls of the four-cycle exhaust *every three-element subset*, enlarging the uncentered operator's symmetry from dihedral to full permutation symmetry.

## Limitations

The sharp formula and classification are specific to the four-cycle with counting measure and all graph-distance balls containing the evaluation vertex. No result is claimed for weighted graphs, other \(\ell^p\) exponents, larger cycles, arbitrary uncentered neighborhood families, or infinite graphs. Absolute priority relative to unindexed or inaccessible work cannot be guaranteed; the mathematical claim is independently established by the proof and finite exact certificate.

## References

- J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204 (first version 2014-10-22), https://arxiv.org/abs/1410.6204.
- C. González-Riquelme and J. Madrid, *Sharp Inequalities for maximal operators on finite graphs*, arXiv:2005.03146 (2020), https://arxiv.org/abs/2005.03146.
- C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630 (2020), https://arxiv.org/abs/2011.02630.
