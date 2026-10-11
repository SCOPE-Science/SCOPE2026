# Four-term von Neumann–Jordan profile of the Day–James hexagonal plane
## Finding
For the real Day–James hexagonal plane \(X_D=(\mathbb R^2,N)\) with \(N(s,t)=\max\{|s|,|t|,|s-t|\}\), and every \(\lambda\in[0,1]\), write \(m=\min\{\lambda,1-\lambda\}\). The four-term von Neumann–Jordan constant \(C'''_{\mathrm{NJ}}(\lambda,X_D)\) equals \(1+\frac32m-2m^2\). Consequently its parameter maximum is \(41/32\), attained exactly at \(\lambda=3/8\) and \(\lambda=5/8\).

In particular, at the balanced parameter \(\lambda=1/2\) the value is \(5/4\), whereas the full parameter profile is larger: its maximum is \(41/32\) at the two off-center parameters \(3/8\) and \(5/8\). Thus the balanced point is not extremal for this four-term invariant on the canonical Day–James hexagon.

## Assumptions and scope
Work over the real plane \(X_D=(\mathbb R^2,N)\) with
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
Its closed unit ball is the hexagon with vertices
\[
(1,1),\ (1,0),\ (0,-1),\ (-1,-1),\ (-1,0),\ (0,1).
\]
For \(\lambda\in[0,1]\), the four-term constant is
\[
C'''_{\mathrm{NJ}}(\lambda,X_D)=\sup_{x,y\in S_{X_D}}\frac12\Bigl(\|\lambda x+(1-\lambda)y\|^2+\|\lambda x-(1-\lambda)y\|^2+\lambda(1-\lambda)\|x-y\|^2+\lambda(1-\lambda)\|x+y\|^2\Bigr).
\]
The claim is only for this real two-dimensional norm and this definition of the four-term constant.

## Proof
Let \(F_\lambda(x,y)\) denote the expression inside the supremum. Each summand is the square of a norm of a linear image of \((x,y)\), hence is convex. Therefore \(F_\lambda\) is jointly convex on the compact polytope \(B_{X_D}\times B_{X_D}\). A convex function on a compact polytope attains its maximum at a vertex, so it suffices to consider the thirty-six ordered pairs of hexagon vertices. Those pairs already lie in \(S_{X_D}\), so enlarging from the sphere to the ball does not change the maximum.

The linear maps
\[
R(s,t)=(t,t-s),\qquad S(s,t)=(t,s)
\]
are isometries of \(N\). The map \(R\) cycles the six vertices, while \(S\) is a reflection. Moreover, replacing \(y\) by \(-y\) leaves \(F_\lambda(x,y)\) unchanged because it merely swaps the first two norm terms and swaps the last two norm terms. Hence the thirty-six ordered vertex pairs split into two classes: pairs with \(y=\pm x\), and all remaining pairs.

The source proves the parameter symmetry \(C'''_{\mathrm{NJ}}(\lambda,X)=C'''_{\mathrm{NJ}}(1-\lambda,X)\). Thus set \(m=\min\{\lambda,1-\lambda\}\in[0,1/2]\). For the first pair class, take \(x=y=(1,1)\). Then direct substitution gives
\[
F_m(x,x)=\frac12\left(1+(1-2m)^2+4m(1-m)\right)=1.
\]
For the second class, take \(x=(1,1)\) and \(y=(1,0)\). On \(0\le m\le1/2\),
\[
N(mx+(1-m)y)=N(1,m)=1,
\]
\[
N(mx-(1-m)y)=N(2m-1,m)=1-m,
\]
and
\[
N(x-y)=1,\qquad N(x+y)=2.
\]
The second identity follows because \(1-m\ge1-2m\) and \(1-m\ge m\) on this interval. Therefore
\[
F_m(x,y)=\frac12\left(1+(1-m)^2+5m(1-m)\right)=1+\frac32m-2m^2.
\]
This quantity is at least \(1\), and is strictly larger than \(1\) for \(0<m\le1/2\). Hence it is the global maximum over all vertex pairs and proves the stated profile.

Finally, the quadratic \(1+\frac32m-2m^2\) has derivative \(\frac32-4m\), so on \([0,1/2]\) its unique maximum occurs at \(m=3/8\), where its value is \(41/32\). Symmetry gives the two parameters \(\lambda=3/8\) and \(\lambda=5/8\).

## Verification
The companion `verify.py` checks the hexagon, the isometry generators, the two complete vertex-pair orbits, and exact rational values at representative parameters including the maximizing parameter. It prints `VERIFY_OK`. The continuum argument does not rely on finite sampling: the proof above identifies the active norm branch for the nontrivial representative throughout \(0\le m\le1/2\).

## Relationship to prior work
The primary source arXiv:2110.15741 introduces \(C'''_{\mathrm{NJ}}(\lambda,X)\), proves its symmetry in \(\lambda\), gives general bounds, and treats classical \(\ell_q\) examples. The inspected source does not state the Day–James hexagonal profile above. Searches for the same invariant together with Day–James terminology found no statement implying this formula. Related work on the same hexagonal plane computes classical James or Jordan–von Neumann quantities, and work on Day–James spaces studies skewness; those invariants do not imply the present four-term parameter profile.

## Limitations
The proof uses the polyhedral structure and dihedral symmetry of this particular hexagonal norm. It does not assert an analogous formula for other Day–James spaces, other polygonal norms, or complex scalars. Literature search cannot rule out every obscure or unindexed duplicate calculation, although no covering statement was found in the checked sources or database searches.

## References
1. Y. Wang et al., *Novel constants based on the generalization of Von Neumann-Jordan constant*, arXiv:2110.15741. Earliest public arXiv posting: 2021-10-29. Primary MSC: 46B20.
2. K. Mitani, K.-S. Saito, and N. Komuro, *Skewness of Day–James spaces*, Annals of Functional Analysis 13 (2022), DOI 10.1007/s43034-022-00222-4.
3. M. Kato, L. Maligranda, and Y. Takahashi, *On James and Jordan–von Neumann constants and the normal structure coefficient of Banach spaces*, Studia Mathematica 144 (2001), DOI 10.4064/sm144-3-5.
