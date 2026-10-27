# Quadratic dyadic escape throughout an asymmetric negative-doubling hole chamber

## Finding

Let \(T:[0,1]\setminus\{1/2\}\to[0,1]\) be the negative-doubling map
\[
T(x)=\begin{cases}1-2x,&0\le x<1/2,\\2-2x,&1/2<x\le1.\end{cases}
\]
For a hole \(H=(a,b)\), define the finite-time survivor set \(E_n(a,b)=\{x\notin H:T^j(x)\notin H\text{ for }0\le j\le n\}\). Critical-point values may be assigned arbitrarily, as the exceptional precritical set is Lebesgue null. Write \(m\) for Lebesgue measure.

**Theorem (exact two-parameter quadratic escape).** For every real pair in the nonempty open chamber
\[
\mathcal R=\left\{(a,b):\frac{11}{18}<b<\frac23,\quad \frac{3-2b}{4}<a<\frac49\right\},
\]
one has
\[
m(E_0(a,b))=1+a-b,
\]
and, for each integer \(n\ge1\),
\[
\boxed{\displaystyle m(E_n(a,b))=2^{-n}\left[2+4a-4b+(n-1)(7a-4b)+\frac{(2-3b)(n-1)(n-2)}2\right].}
\]
In particular the complete leading asymptotic is
\[
\boxed{\displaystyle m(E_n(a,b))\sim \frac{2-3b}{2}\,n^2 2^{-n}\qquad(n\to\infty),}
\]
and the escape rate is exactly \(\log 2\). At fixed \(b\), the leading quadratic coefficient is independent of the other hole endpoint \(a\). The conditional one-step escape probability given survival through time \(n\) is \(1/2-1/n+O(n^{-2})\).

## Assumptions and scope

The inequalities defining \(\mathcal R\) are strict. They imply \(1/3<a<4/9<1/2<b<2/3\) and allow the entire nonstationary survivor process to be represented by five intervals. Time \(n\) means surviving observations at times \(0,1,\ldots,n\), so the origin-of-time convention is explicit. The measure is unnormalized Lebesgue measure on \([0,1]\). Dividing by \(1+a-b\) yields the survival probability for an initially uniform point conditioned to lie outside the hole. The same formulas hold whether endpoints are retained or discarded, since finite sets of boundaries and their preimages have zero Lebesgue measure.

## Proof

Set
\[
u=1-2a,\qquad v=2-2b,\qquad w=4a-1.
\]
The chamber inequalities imply \(0<u<a<b<v<w<1\), as well as
\[
a<4-8a<b,\qquad a<4b-2<b.
\]
For clarity: \(u<a\) follows from \(a>1/3\), \(v>b\) from \(b<2/3\), and \(w>v\) from \(4a+2b>3\). The inequality \(4-8a>a\) uses \(a<4/9\), and \(4-8a<b\) follows from \(a>(3-2b)/4>(4-b)/8\). Finally \(4b-2>a\) follows from \(b>11/18\) and \(a<4/9\).

Partition the complement of the hole, disregarding finitely many shared endpoints, into
\[
I_1=[0,u],\quad I_2=[u,a],\quad I_3=[b,v],\quad I_4=[v,w],\quad I_5=[w,1].
\]
These five intervals have positive lengths
\[
\ell=(1-2a,\ 3a-1,\ 2-3b,\ 4a+2b-3,\ 2-4a)^{\mathsf T}.
\]
Direct application of the two affine branches gives the following intersections with the retained set \(S=[0,a]\cup[b,1]\):
\[
\begin{array}{c|c|c}
\text{source}&T(I_i)&T(I_i)\cap S\ \text{up to endpoints}\\\hline
I_1&[w,1]&I_5\\
I_2&[u,w]&I_2\cup I_3\cup I_4\\
I_3&[4b-2,v]&I_3\\
I_4&[4-8a,4b-2]&\varnothing\\
I_5&[0,4-8a]&I_1\cup I_2
\end{array}
\]
Each nonempty destination interval is *completely covered* by the image of its indicated source; each corresponding inverse branch contracts length by exactly \(1/2\). Thus the zero-one transition matrix, with rows indexing sources and columns destinations, is
\[
M=\begin{pmatrix}
0&0&0&0&1\\
0&1&1&1&0\\
0&0&1&0&0\\
0&0&0&0&0\\
1&1&0&0&0
\end{pmatrix}.
\]
Every admissible length-\(n\) path ending in \(I_j\) determines a disjoint (up to endpoints) initial cylinder of length \(2^{-n}|I_j|\). Hence, **for every integer \(n\ge0\)**,
\[
2^n m(E_n)=\mathbf 1^{\mathsf T}M^n\ell.
\]
The row vector \(\mathbf 1^{\mathsf T}M^n\) is exactly
\[
(1,\ n+1,\ 1+n(n+1)/2,\ n,\ 1)\qquad(n\ge1).
\]
Indeed, \(\mathbf1^{\mathsf T}M=(1,2,2,1,1)\); if the displayed formula holds at \(n\), multiplication by \(M\) gives \((1,n+2,1+(n+1)(n+2)/2,n+1,1)\). At \(n=0\), the row vector is \((1,1,1,1,1)\), so \(m(E_0)=\sum_i\ell_i=1+a-b\).

For \(n\ge1\), multiplying the explicit row by \(\ell\) gives
\[
2^n m(E_n)=(1-2a)+(n+1)(3a-1)
 +\left(1+\frac{n(n+1)}2\right)(2-3b)
 +n(4a+2b-3)+(2-4a).
\]
Collecting terms gives the asserted boxed polynomial. Since \(2-3b>0\) throughout the chamber, its leading term is \((2-3b)n^2/2\). Division by \(2^n\) proves the claimed asymptotic and escape rate. Finally the conditional escape hazard equals \(1-m(E_{n+1})/m(E_n)\), which is \(1/2-1/n+O(n^{-2})\) by the positive quadratic leading term. \(\square\)

## Verification

Run `python3 verify.py` from the folder containing this file. The standalone exact-rational checker independently forms finite-time survivor intervals by inverse-branch clipping and compares their Lebesgue lengths with the theorem for a grid of interior rational parameters and times through \(n=16\). It also checks all five transition images against the proposed Markov graph and tests the matrix path-count identity. These finite calculations test implementation and boundary inequalities; the unrestricted quantifiers follow from the proof above.

## Relationship to prior work

Ding, Steiner and Sun (2026), arXiv:2610.03327v1, analyze negative-doubling holes, symbolic admissibility, entropy and dimension staircases. Their theorems characterize invariant survivor sets and entropy, but the inspected text does not give a finite-time Lebesgue-measure polynomial in both hole endpoints. The present chamber concerns the *transient* mass, not merely the invariant survivor subshift.

Alcaraz Barrera (2015), arXiv:1506.00067v1, studies topological dynamics and subshifts of finite type for the *positive*-doubling map with asymmetric holes. These provide general symbolic context, not a formula for this negative-degree map and this parameter chamber. Dettmann (2011/2013), arXiv:1112.5390, derives small-hole escape-rate asymptotics for the ordinary doubling map, not this finite-time polynomial law for a large asymmetric hole.

A publicly indexed result on symmetric negative-doubling holes proves periodic-orbit and zeta classifications only along \(b=1-a\), \(0<a\le2/5\). An existing finite-time escape formula in the same symmetric range has a linear, rather than quadratic, prefactor. Neither covers the present open chamber (here \(a>5/12\)). The passage from a two-stage to a three-stage directed recurrence structure produces the quadratic prefactor. General finite-state transfer-matrix methods are standard and are not claimed as new.

## Limitations

The result does not classify every negative-doubling hole, nor determine maximality of the displayed chamber. There may be other chambers with the same polynomial order or an equivalent formula. The symbolic survivor has zero topological entropy in this chamber, so the result should not be interpreted as positive-entropy dynamics. The novelty assessment is based on examined sources, not an independent historical-priority certification. The displayed hazard expansion is pointwise for each fixed interior parameter pair, not uniform as \(b\uparrow2/3\).

## References

1. Y. Ding, W. Steiner, and Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1, first public 2026-10-02. https://arxiv.org/abs/2610.03327
2. R. Alcaraz Barrera, *Topological dynamics of the doubling map with asymmetrical holes*, arXiv:1506.00067v1, first public 2015-05-30. https://arxiv.org/abs/1506.00067
3. C. Dettmann, *Open circle maps: Small hole asymptotics*, arXiv:1112.5390, 2011; *Nonlinearity* 26 (2013), 307–317. https://arxiv.org/abs/1112.5390
