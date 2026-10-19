# Reciprocal-slope collapse to four-cycles in a fixed-point-free affine map

## Finding

For every real \(r>1\), the four-branch interval map of García-Grimaldo and Campos, on its reciprocal-slope parameter curve, has a complete and explicit global orbit classification. All initial points except one repelling two-cycle enter a continuum of neutral prime-period-four cycles after finitely many steps. The entry time, for uniform initial conditions, has an exact geometric tail and a mean diverging as the reciprocal slopes approach one.

More precisely, let \(L>0\), \(I=[-r^2L,r^2L]\), and define \(F:I\to I\) by
\[
 F(x)=\begin{cases}
 x/r+L,&-r^2L\le x\le-rL,\\
 rx+r^2L,&-rL<x<0,\\
 rx-r^2L,&0\le x<rL,\\
 x/r-L,&rL\le x\le r^2L.
 \end{cases}
\]
Define the invariant periodic core
\[
 Q=L\Bigl([-r^2,-r)\cup[1-r,0)\cup[0,r-1)\cup[r,r^2)\Bigr).
\]
These four intervals are cyclically permuted, and \(F^4\) is exactly the identity on \(Q\). Every point of \(Q\) has **prime period four**. There are exactly two other periodic points, forming the repelling two-cycle
\[
 \left\{-\frac{r^2L}{r+1},\frac{r^2L}{r+1}\right\}.
\]
Every point of \(I\) other than these two enters \(Q\) after finitely many iterates. In particular there are no fixed points and no non-eventually-periodic trajectories.

The set outside the three-interval closed core \(P= L([-r^2,-r]\cup[1-r,r-1]\cup[r,r^2])\) consists of two holes
\[
 H=L\Bigl((-r,1-r)\cup(r-1,r)\Bigr).
\]
For \(N(x)=\min\{n\ge0:F^n(x)\in P\}\), a uniformly distributed \(X\) on \(I\) satisfies
\[
 \Pr[N(X)=0]=1-r^{-2},\qquad
 \Pr[N(X)=n]=\frac{r-1}{r^{n+2}}\quad(n\ge1),
 \qquad \mathbb E[N(X)]=\frac1{r(r-1)}.
\]
The only points with \(N=\infty\) are the two points of the repelling two-cycle (probability zero). For any integer \(n\ge0\), the Lebesgue measure of the initial points remaining in \(H\) for times \(0,1,\ldots,n\) is exactly \(2L/r^n\).

## Assumptions and scope

The result holds for **all real** \(r>1\) and \(L>0\), with the branch conventions displayed above, on the entire closed real interval \(I\). The original four-branch model uses parameters \(m_1=1/r\), \(m_2=r\), \(b_1=L\), \(a=rL\), \(b_2=r^2L\); hence \(m_1m_2=1\). No claim is made for other parameter relations, finite-precision electronic implementations, or real initial states outside the defining invariant interval. The probability assertions refer to exact real dynamics with normalized Lebesgue initial distribution on \(I\).

## Proof

Scale by \(L\), so it suffices to take \(L=1\). Set \(A=[-r^2,-r)\), \(B=[1-r,0)\), \(C=[r,r^2)\), and \(D=[0,r-1)\). Substituting the four affine formulas shows, **including the stated half-open boundary choices**,
\[
 F(A)=B,\quad F(B)=C,\quad F(C)=D,\quad F(D)=A.
\]
Each restriction is an affine bijection onto the next interval, with respective slopes \(1/r,r,1/r,r\). Their fourfold composition has slope one and maps each interval into itself. Because the successive affine endpoint formulas give zero net translation, \(F^4(x)=x\) on all four intervals. Every point in these intervals crosses four different disjoint intervals before returning, so its least period is four.

The complement of \(Q\) in the closed core \(P=[-r^2,-r]\cup[1-r,r-1]\cup[r,r^2]\) consists precisely of the three points \(-r\), \(r-1\), \(r^2\). They satisfy
\[
 r^2\mapsto r-1\mapsto-r\mapsto0\in Q.
\]
Also \(F(P)\subseteq P\). Thus every point of \(P\) enters \(Q\) in at most three steps. In particular the possible unusual branch values at \(-r\), \(0\), and \(r\) are covered.

The two components of \(H=I\setminus P\) are \(H_-=(-r,1-r)\) and \(H_+=(r-1,r)\). We have \(F(H_-)=(0,r)\) and \(F(H_+)=(-r,0)\); a point that stays in \(H\) must alternate between \(H_-\) and \(H_+\). On each hole \(F\) is affine with slope \(r>1\). For an initial point in either chosen hole, the set whose next \(n\) iterates all remain in the holes is an interval of length \(r^{-n}\): its inverse is determined uniquely by the alternation, and every inverse step divides length by \(r\). Therefore these sets are nested and their intersection is a singleton. The two singletons form an alternating two-cycle, and directly solving the second-iterate equation gives \(x=\pm r^2/(r+1)\). Both lie strictly in the corresponding holes because \(r-1<r^2/(r+1)<r\). On their two-cycle, the multiplier is \(r^2>1\), hence the orbit is repelling.

Every other initial point in \(H\) must exit to \(P\) in finite time: otherwise its position would belong to one of the two singleton intersections. This proves the global classification. The map has no fixed point, since every orbit is eventually period four except the primitive period-two orbit; in particular no fixed point can occur in either part.

For the first-entry law, the two \(n\)-step survivor intervals have total length \(2r^{-n}\). The initial interval has length \(2r^2\), so \(\Pr[N>n]=r^{-n-2}\), for every integer \(n\ge0\). Subtract consecutive tails to obtain \(\Pr[N=n]=(r-1)/r^{n+2}\) for \(n\ge1\), while \(\Pr[N=0]=1-r^{-2}\). Summing the tails \(\mathbb E[N]=\sum_{n\ge0}\Pr[N>n]\) yields \(1/[r(r-1)]\). Multiplying spatial lengths by \(L\) restores general scaling. This establishes every quantifier without inference from finite experiments.

## Verification

The included independent-of-packaging Python script `verification/check.py` uses standard-library exact rational arithmetic. It evaluates seven rational values of \(r\), checks the two-cycle, verifies the half-open affine dynamics and eventual fourfold identities on 7,007 grid points, and recomputes the survivor interval lengths for ten successive steps. It reports 26,271 finite exact assertions. The entire continuum theorem and infinite survival tail follow from the affine interval proof above; the script is a consistency check, not a substitute for that proof.

## Relationship to prior work

García-Grimaldo and Campos introduced and investigated this four-branch, fixed-point-free piecewise-affine family [1]. Their analysis identifies fixed-point-free conditions and explores chaotic parameter choices. García-Grimaldo, Bermudez-Marquez, Tlelo-Cuautle and Campos-Cantón [2, Sections 2--4] provide the exact branch formulas and investigate the specific chaotic choice \((m_1,m_2,b_1)=(0.8,5,4)\), including periodic windows in a one-parameter bifurcation diagram. In particular, the period-four windows seen numerically at fixed \(m_2=5\) do not assert a global eventual-periodic classification on the distinct reciprocal-slope curve \(m_1m_2=1\), nor an exact geometric transient law. The present claim is the full orbit census and first-entry distribution for that entire curve, not the known absence of fixed points, nor the mere existence of period-four points.

## Limitations

The main conclusion applies only on the specific reciprocal-slope curve. The period-four cycles are neutral rather than attracting in the usual hyperbolic sense; trajectories outside the periodic core enter exactly after finitely many steps, rather than converge asymptotically to an isolated periodic orbit. An exceptional repelling two-cycle survives forever in the holes. Nonlinear parameter robustness, rounding-error behavior, cryptographic randomness, and dynamics beyond the invariant interval are unproved. Earlier analyses of this fixed-point-free family may contain equivalent results not available in full text; mathematical priority is not independently certified.

## References

1. C. García-Grimaldo and E. Campos, *Chaotic Features of a Class of Discrete Maps without Fixed Points*, International Journal of Bifurcation and Chaos **31** (2021), 2150200. DOI: `10.1142/S021812742150200X` (public bibliographic date October 26, 2021).
2. C. García-Grimaldo, C. F. Bermudez-Marquez, E. Tlelo-Cuautle and E. Campos-Cantón, *FPGA Implementation of a Chaotic Map with No Fixed Point*, Electronics **12** (2023), article 444. DOI: `10.3390/electronics12020444` (published January 14, 2023); see full accessible article, Sections 2--5.
3. C. García-Grimaldo and E. Campos-Cantón, *Comparative Analysis of Chaotic Features of Maps Without Fixed Points*, in *Complex Systems and Their Applications* (2022), pp. 151--176. DOI: `10.1007/978-3-031-02472-6_8` (abstract available; full text not inspected).
