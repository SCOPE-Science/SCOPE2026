# A size-biased geometric escape law at the negative-doubling four-cycle threshold

## Finding

Consider the negative-doubling interval map
\[
T(x)=\begin{cases}1-2x,&0\le x<1/2,\\2-2x,&1/2<x\le1,\end{cases}
\]
and the open, symmetric hole \(H_a=(a,1-a)\), where \(0<a<1/2\). Write
\[
S_n(a)=\{x\in[0,1]:T^j(x)\notin H_a\text{ for }0\le j\le n\},\qquad
\ell_n(a)=\operatorname{Leb}(S_n(a)).
\]
The value assigned to \(T(1/2)\) is immaterial because \(1/2\in H_a\).

**Exact escape law at the period-four boundary.** At \(a=2/5\), for every integer \(n\ge0\),
\[
\boxed{\ell_n(2/5)=\frac{2n+4}{5\,2^n}.}
\]
If \(X\) is uniformly distributed on \([0,2/5]\cup[3/5,1]\), and \(N=\min\{j\ge1:T^j(X)\in(2/5,3/5)\}\), then
\[
\boxed{\Pr(N=n)=\frac{n}{2^{n+1}}\quad(n=1,2,\ldots),}
\qquad \mathbb E N=3,\quad\operatorname{Var}N=4.
\]
In particular \(N+1\) has the negative-binomial distribution of the number of independent fair-coin trials needed for a second success. The unconditioned survivor-length generating function is
\[
\boxed{\sum_{n=0}^\infty \ell_n(2/5)z^n
 =\frac{4-z}{5(1-z/2)^2},\qquad |z|<2.}
\]
Thus the escape exponent is \(\log2\), but the probability has a linear prefactor and the generating function has a double pole.

**A conditional uniform transition time.** Split the complement of \(H_{2/5}\) into four closed intervals (endpoints are irrelevant to Lebesgue probabilities):
\[
A=[0,1/5],\quad B=[1/5,2/5],\quad
C=[3/5,4/5],\quad D=[4/5,1].
\]
Set \(\tau=\inf\{j\ge0:T^j(X)\in B\cup C\}\), with \(\inf\varnothing=\infty\). When \(X\) is uniform on \(S_n(2/5)\), the exact conditional probabilities are
\[
\boxed{
\Pr(\tau=k\mid X\in S_n)=\frac1{n+2}\ (1\le k\le n),\quad
\Pr(\tau=0\mid X\in S_n)
=\Pr(\tau>n\mid X\in S_n)=\frac1{n+2}.}
\]
Consequently \(\min\{\tau,n\}/n\) converges in distribution to the uniform law on \([0,1]\) as \(n\to\infty\).

**Geometric comparison phase.** For every \(0<a\le1/3\) and every integer \(n\ge0\),
\[
\boxed{\ell_n(a)=\frac{2a}{2^n}.}
\]
Conditional on starting outside \(H_a\), the first-hole time is exactly geometric:
\(\Pr(N=n)=2^{-n}\) for \(n\ge1\), with mean \(2\). The parameter values \(a=1/3\) and \(a=2/5\) are the two periodic-orbit changes in the known zero-entropy symmetric-hole regime, but the present statements concern finite-time Lebesgue statistics rather than orbit counts.

## Assumptions and scope

Lebesgue measure is ordinary one-dimensional interval length. Survival includes time \(0\) and the times through \(n\), and the hole is **open**, so its two endpoints are retained; finitely or countably many endpoint or precritical trajectories do not affect the formulas. Conditional distributions are with respect to normalized Lebesgue measure on the stated initial set. The statistical claims concern exactly \(a=2/5\) and, for comparison, the whole range \(0<a\le1/3\); no formula is asserted for \(1/3<a<2/5\) or \(a>2/5\). The convergence assertion uses \(\min\{\tau,n\}/n\) for \(n\ge1\); it is a limit under changing conditional initial distributions, not a statement about a typical fixed initial point.

## Proof

**The geometric phase.** Put \(L=[0,a]\), \(R=[1-a,1]\). For \(0<a\le1/3\), the branch maps satisfy \(T(L)\cap(L\cup R)=R\) and \(T(R)\cap(L\cup R)=L\), up to isolated endpoints at equality. Moreover each restriction maps onto the entire opposite interval, with derivative of absolute value \(2\). Each allowed inverse transition therefore halves length. There are two initial intervals of length \(a\), so \(\ell_n(a)=2a\,2^{-n}\). Dividing by \(\ell_0(a)=2a\) gives \(\Pr(N>n)=2^{-n}\) and the geometric probability law.

**The four-cell Markov partition.** At \(a=2/5\), the branch images of the four equal-length cells are
\[
T(A)=C\cup D,\quad T(B)=[1/5,3/5],\quad
T(C)=[2/5,4/5],\quad T(D)=A\cup B.
\]
Intersecting these images with \(A\cup B\cup C\cup D\), and ignoring endpoints, gives the exact allowed arrows
\[
A\to C,D;\qquad B\to B;\qquad C\to C;\qquad D\to A,B.
\]
Their zero-one adjacency matrix, with rows/columns indexed by \(A,B,C,D\), is
\[
M=\begin{pmatrix}0&0&1&1\\0&1&0&0\\0&0&1&0\\1&1&0&0\end{pmatrix}.
\]
Every arrow covers its target interval *completely*. Thus every path of \(n\) arrows ending in any of the four cells has a distinct initial cylinder interval of length \(1/(5\,2^n)\); all such cylinders have disjoint interiors and cover \(S_n(2/5)\) modulo finitely many boundary points. Write \(\mathbf1=(1,1,1,1)^{\mathsf T}\). Direct induction using the displayed matrix gives
\[
M^n\mathbf1=(n+1,1,1,n+1)^{\mathsf T}\qquad(n\ge0).
\]
Hence the number of paths is \(\mathbf1^{\mathsf T}M^n\mathbf1=2n+4\), proving the exact survivor-length identity.

**First-hole distribution and moments.** For initial law normalized on the complement of the hole, the survival tail is
\[
\Pr(N>n)=\frac{\ell_n(2/5)}{\ell_0(2/5)}
=\frac{n+2}{2^{n+1}},\qquad n\ge0.
\]
Taking successive differences gives \(\Pr(N=n)=n/2^{n+1}\). The identities \(\sum_{n\ge1} n/2^n=2\), \(\sum_{n\ge1}n^2/2^n=6\), and \(\sum_{n\ge1}n^3/2^n=26\) give normalization, mean \(3\), second moment \(13\), and variance \(4\). Summing \((2n+4)/(5\,2^n)\) gives the stated generating function.

**Conditional histories.** Each length-\(n\) allowed path has the same initial-cylinder measure. Starting in \(B\) or \(C\) gives exactly one surviving path per initial cell, hence two paths with \(\tau=0\). Starting in \(A\) or \(D\), a surviving path can remain on the alternating \(A\leftrightarrow D\) cycle, giving two paths with \(\tau>n\), or use the unique exit into \(B\) or \(C\) at any chosen step \(k\in\{1,\ldots,n\}\). Each such \(k\) has exactly two paths (one for each starting phase). After entering \(B\) or \(C\), continuation under the survival constraint is unique. Dividing these \(2(n+2)\) equiprobable paths by their total proves all displayed conditional probabilities. The mass at \(\tau=0\) and \(\tau>n\) tends to zero, while the remaining mass is uniform on the mesh \(\{1/n,\ldots,1\}\). This proves convergence to uniform \([0,1]\).

The path matrix has characteristic polynomial \((\lambda-1)^3(\lambda+1)\), with a size-two Jordan block at eigenvalue \(1\). The associated off-diagonal transitions from an alternating two-cycle into the two fixed-cell channels cause the linear path-count factor and the double pole. This is independent of the extra period-four orbit lying on the partition endpoints, whose presence affects the periodic-point zeta function but not Lebesgue length.

## Verification

Running `verify_escape.py` with the Python standard library executes exact rational interval pullback calculations through \(n=23\), independently of the adjacency-matrix formula, and compares these lengths to the closed forms. It also checks the combinatorial path counts, first-hole probabilities, the four-cycle endpoint orbit, and rational test values in the geometric phase. These finite calculations are diagnostic only; the full quantified result follows from the preceding Markov and inverse-branch proof. The verifier has no network or nonstandard-package dependencies.

## Relationship to prior work

Ding–Steiner–Sun [1] classify symbolic survivor plateaux and dimension/entropy staircases for the negative-doubling map with interval holes. They do not establish finite-time Lebesgue survival probabilities or conditional transition-time limits. A prior published analysis [2] gives the periodic orbits and rational Artin–Mazur zeta function of the same symmetric holes through \(a=2/5\), locating the period-four orbit precisely at that endpoint. The periodic-orbit list is acknowledged and not claimed anew: fixed-point counts determine \(\operatorname{tr}(M^n)\), but they cannot determine the sums \(\mathbf1^{\mathsf T}M^n\mathbf1\) when transient arrows are present. The additional law here is the exact finite-time and conditional Lebesgue distribution, which uses those transient arrows.

A second related published analysis [3] quantifies negative-doubling **parameter plateau widths**, not survivor escape times. Glendinning–Hege [4] study the boundary of chaos and discuss absorption rates as motivation without giving the present four-cell laws. The general use of finite Markov partitions and transfer matrices to compute escape rates is classical; no novelty is attributed to that general method. The specific size-biased law, double-pole prefactor, and uniform conditional switching-time profile at this naturally selected endpoint are the claims assessed here.

## Limitations

The theorem does not classify escape rates for all hole widths, and it does not imply a parameter-continuity law as \(a\uparrow2/5\). No quasistationary limiting density or non-Lebesgue initial-law result is claimed. The survival identities disregard finitely many partition endpoints only for measure calculations; they do not erase the genuine period-four endpoint orbit. Earlier or differently worded calculations of this exact Markov-hole example might exist outside the inspected literature.

## References

[1] Y. Ding, W. Steiner, Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1, first public 2 October 2026; https://arxiv.org/html/2610.03327v1 .

[2] *A three-phase periodic-orbit and zeta trichotomy for symmetric negative-doubling holes*, published published-finding corpus finding, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-three-phase-periodic-orbit-and-zeta-trichotomy-for-symmetric-n--8027a957802c .

[3] *Exact parity law for negative-doubling survivor-plateau address widths*, published published-finding corpus finding, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-parity-law-for-negative-doubling-survivor-plateau-address--195a748d0893 .

[4] P. Glendinning, C. Hege, *The boundary of chaos for piecewise smooth maps and the boundary of positive Hausdorff dimension for survivor sets of open maps*, arXiv:2508.21429v1, first public 29 August 2025; https://arxiv.org/html/2508.21429v1 .
