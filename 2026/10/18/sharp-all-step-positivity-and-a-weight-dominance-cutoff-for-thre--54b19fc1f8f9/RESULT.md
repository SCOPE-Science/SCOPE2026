# Sharp all-step positivity and a weight-dominance cutoff for three-site Gauss diffusion

## Finding

For three vertices with nonnegative symmetric edge conductances \(a=w_{12}\), \(b=w_{23}\), and \(c=w_{13}\), assume the conductance graph is connected, equivalently \(t=ab+bc+ca>0\). Put \(s=a+b+c\), let \(L\) be its weighted graph Laplacian, and define the completed two-stage fourth-order Gauss–Legendre diffusion step, for every real \(h\ge0\), by
\[
T(h)=\bigl(I-\tfrac h2L+\tfrac{h^2}{12}L^2\bigr)
      \bigl(I+\tfrac h2L+\tfrac{h^2}{12}L^2\bigr)^{-1}.
\]
The complete set of entrywise-nonnegative steps is \([0,\infty)\) **if and only if**
\[
\boxed{\max\{a,b,c\}\le2\bigl(s-\max\{a,b,c\}\bigr).}
\]
If this inequality fails, exactly one edge, of conductance \(x>2(y+z)\), is dominant. In this case, the complete positivity set is \([0,H]\), where \(t=x(y+z)+yz\) and
\[
\boxed{H=\frac{3t+\sqrt{9t^2+12xt(x-2(y+z))}}{t(x-2(y+z))}.}
\]
For \(h>H\), the two entries joining the endpoints of that unique dominant edge are negative, while all other off-diagonal entries are strictly positive. The diagonal entries are strictly positive for every \(h\ge0\), regardless of conductance imbalance.

The three-vertex class is smallest possible for this large-step positivity loss among connected symmetric graph-Laplacian generators: on one or two vertices the completed Gauss–Legendre step is entrywise nonnegative for every \(h\ge0\). For fixed \(y+z>0\) and \(x\to\infty\), the finite cutoff has the asymptotic law
\[
H\sim\sqrt{\frac{12}{x(y+z)}}.
\]

## Assumptions and scope

All edge conductances are finite real numbers, nonnegative, and time-independent; at least two edges of the triangle are positive so that \(t>0\). Zero conductances mean absent edges, allowing weighted three-vertex paths as well as triangles. The Laplacian convention is \(L_{ij}=-w_{ij}\) for distinct vertices and \(L_{ii}=\sum_{j\ne i}w_{ij}\). The claim concerns entrywise nonnegativity of the **completed** rational one-step matrix for all nonnegative initial states, not the signs of intermediate Runge–Kutta stages, uniform monotonicity on arbitrary dimensions, or positivity of arbitrary nonsymmetric generators. The step matrix is symmetric, doubly stochastic and positive definite for every finite nonnegative step, even when an off-diagonal entry is negative.

## Proof

**Spectral preliminaries.** The three eigenvalues of \(L\) are \(0\) and
\[
\lambda_{\pm}=s\pm\sqrt{s^2-3t}>0.
\]
Consequently \(L(L^2-2sL+3tI)=0\). For \(u\ge0\), define
\[
 r(u)=\frac{u^2-6u+12}{u^2+6u+12}.
\]
Its numerator is \((u-3)^2+3>0\), while its denominator exceeds its numerator when \(u>0\). Hence \(0<r(u)\le1\). Spectral calculus shows that \(T(h)=r(hL)\) is positive definite and fixes the all-ones vector. All diagonal entries are strictly positive; symmetry and row sums one are automatic.

**Exact off-diagonal formula.** Let
\[
 D=I+\tfrac h2L+\tfrac{h^2}{12}L^2,\quad
 A=1-\tfrac{th^2}{4},\quad
 B=\tfrac h2+\tfrac{sh^2}{6},\quad
 M=A^2+2sAB+3tB^2.
\]
On the range of \(L\), its quadratic identity gives \(D=A I+B L\). Also \(M=d(h\lambda_+)d(h\lambda_-)\), where \(d(u)=1+u/2+u^2/12\), so \(M>0\). Modulo the quadratic identity on this range,
\[
 (A I+B L)^{-1}=\frac{A+2sB-BL}{M}.
\]
Because \(T=I-hLD^{-1}\), for distinct vertices \(i,j\), with the joining edge weight \(x\) and the other two edge weights \(y,z\), direct multiplication using
\[
 L_{ij}=-x,\qquad (L^2)_{ij}=-x(x+s)+yz
\]
yields
\[
 T_{ij}(h)=\frac{h}{M}\bigl(xA+tB\bigr)
 =\frac{4h}{\Delta(h)}
 \left[12x+6th-t\bigl(x-2(y+z)\bigr)h^2\right],
\]
where the common strictly positive denominator is
\[
\Delta(h)=48+48sh+(16s^2+12t)h^2+12sth^3+3t^2h^4=48M.
\]
These are exact identities for every allowed conductance triple, including zero individual edge weights and repeated nonzero Laplacian eigenvalues.

**Sign analysis and classification.** The bracket for an edge of weight \(x\) equals \(12x+6th+t(2(y+z)-x)h^2\). If \(x\le2(y+z)\), it is strictly positive for every \(h>0\), since \(t>0\). If \(x>2(y+z)\), it is a strictly concave quadratic, positive at zero, with exactly one positive root \(H\) given above; it becomes negative exactly for \(h>H\). Two different edges cannot both have weight greater than twice the sum of the other two. Thus there is at most one restrictive entry pair, and the claimed complete step set follows, including equality at the endpoint. At \(h=0\), \(T(0)=I\). With \(x\to\infty\) and fixed \(y+z>0\), one has \(t=x(y+z)+O(1)\); substitution into the root formula proves the displayed asymptotic.

**Minimality.** For any connected two-vertex graph the weighted Laplacian has spectrum \(\{0,2w\}\), \(w>0\), and
\[
 T(h)=\tfrac12\begin{pmatrix}1+r(2wh)&1-r(2wh)\\1-r(2wh)&1+r(2wh)\end{pmatrix}\ge0
\]
entrywise for every \(h\ge0\). The one-vertex case is the identity. Conversely, a connected three-vertex example is \((a,b,c)=(5,1,1)\), for which at \(h=10\) the exact entry is \(T_{12}(10)=-950/290563<0\). Hence dimension three is sharp.

## Verification

Run `python3 verify.py` in the directory containing the supplied standalone file; it uses only the Python standard library and exact rational arithmetic. It directly constructs each \(3\times3\) Padé step by matrix multiplication and rational Gaussian elimination and independently compares every off-diagonal entry to the closed formula for connected conductance triples drawn from \(\{0,1/4,1,2,3,5,10\}\) and steps drawn from \(\{0,1/20,1/2,1,3,10,100\}\). It additionally checks symmetry, row sums, positivity of diagonals, the absence of two negative unordered edge pairs, and two explicit boundary examples. A successful run reports `VERIFY_OK 30485 exact rational checks`. These finite checks corroborate the exact algebra; they do not prove the quantified theorem independently of the displayed derivation.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten (2010) analyze diagonal Padé discretizations of positive systems, including the \([2/2]\) map, sufficient step restrictions, numerical counterexamples and a special analysis of dimension two. Their 2012 expanded study also proves limits of positivity for general Metzler systems using nonconservative high-dimensional counterexamples, but supplies no exact weighted three-vertex symmetric-conservative all-step classification. Their sufficient condition is not an exact characterization of three-state *singular symmetric Laplacians*. The present result identifies the complete three-state weighted conductance domain of unconditional positivity and gives an exact cutoff outside it. Horváth (2005) provides foundational Runge–Kutta positivity-step theory, rather than this graph-specific algebraic classification.

Related results on paths, cycles, complete multipartite and other unweighted diffusion networks address different graph families or different quantifiers. In particular, a general threshold for the onset of small-step negativity is not a condition for positivity at **every** step size. Existing large-step counterexamples on four-vertex paths do not imply a complete three-site weighted classification. The criterion is for the completed Gauss–Legendre step, not for universal strong-stability-preserving stage positivity.

## Limitations

This theorem does not extend to arbitrary four-or-more-site graphs, arbitrary nonsymmetric finite Markov generators, higher-order Padé maps, or stagewise nonnegativity. A particular graph's entrywise-nonnegative completed steps do not imply that the underlying two-stage method has a positive universal SSP coefficient. The originality assessment is limited by possible mathematically equivalent formulations in unindexed positivity and matrix-function literature; no independent external mathematical audit has been performed.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, MTNS 2010. Public repository record and full PDF: https://mural.maynoothuniversity.ie/id/eprint/2195/ (repository date 2010-10-15).
2. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356; DOI: 10.1016/j.apnum.2004.08.026 (contextual general positivity theory).
3. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, Linear Algebra and its Applications 436 (2012), 3425–3442; DOI: 10.1016/j.laa.2011.12.021. Accessible preprint: https://mural.maynoothuniversity.ie/id/eprint/3761/.
