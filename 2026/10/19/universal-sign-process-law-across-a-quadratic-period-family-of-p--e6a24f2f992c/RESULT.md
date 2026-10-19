# Universal sign-process law across a quadratic-period family of piecewise-linear plane maps

## Finding

For every integer \(n\geq3\), set \(q=n^2\), \(p=n-1\), \(a=2\cos(\pi/n)\), and define the area-preserving plane homeomorphism
\[
T_n(x,y)=(a|x|-y,x).
\]
Let \(\mu\) be **any** \(T_n\)-invariant Borel probability measure assigning mass zero to the union of the rays \(T_n^j\{(0,t):t>0\}\), \(0\leq j<q\). For \(Z\sim\mu\), observe the stationary binary sequence
\[
B_t={\bf1}_{\{(T_n^t Z)_1<0\}},\qquad t\in\mathbb Z.
\]
Its **entire joint law**, independent of the choice of \(\mu\), is the following finite cyclic process. If \(K\) is uniform on \(\mathbb Z/q\mathbb Z\), then
\[
(B_t)_{t\in\mathbb Z}\ \stackrel{\mathrm{law}}{=}\
\bigl({\bf1}_{\{(K+pt)\bmod q\in\{0,1,\ldots,n-1\}\}}\bigr)_{t\in\mathbb Z}.
\]
In particular, \(\mathbb P(B_t=1)=1/n\). For any integer \(k\), put
\[
d_k=(pk)\bmod q\ \in\{0,\ldots,q-1\},\qquad D_k=\min\{d_k,q-d_k\}.
\]
Then the **complete two-time law** is determined by
\[
\mathbb P(B_0=B_k=1)=\frac{(n-D_k)_+}{n^2},\qquad
\operatorname{Cov}(B_0,B_k)=\frac{(n-D_k)_+-1}{n^2},
\]
where \((u)_+=\max\{u,0\}\). Among all time differences modulo \(n^2\), pairwise independence occurs **exactly** at \(k\equiv\pm1\pmod{n^2}\); simultaneous negative observations are impossible exactly when \(D_k\geq n\). In particular,
\[
\mathbb P(B_0=B_1=1)=\frac1{n^2},\quad
\mathbb P(B_0=B_2=1)=0,\quad
\mathbb P(B_0=B_{n+1}=1)=\frac{n-1}{n^2}.
\]
Thus successive observations are independent, observations two steps apart are mutually exclusive, and the separation of \(n+1\) iterations produces a large positive recurrence, uniformly over every boundary-free invariant probability measure.

## Assumptions and scope

The assertion holds for **each** integer \(n\geq3\), each invariant Borel probability measure satisfying the stated zero-mass boundary condition, and **all** integer time indices; negative times use the inverse homeomorphism. The excluded rays form a finite union of lines through the origin restricted to positive radial half-lines and include both signs of the vertical axis. Every absolutely continuous invariant probability satisfies the condition. Such probabilities exist: since \(T_n\) has finite order and preserves Lebesgue area, averaging the forward images of normalized area on any bounded positive-area set produces an absolutely continuous invariant probability.

The statement is about the strict-negative first-coordinate observation, not the amplitudes of the coordinates or every possible observation partition. It does not assert the same law for measures charging the boundary rays.

## Proof

**1. The two branch matrices and an exact orbit of the switching ray.** Write \(\theta=\pi/n\) and
\[
A_+=\begin{pmatrix}a&-1\\1&0\end{pmatrix},\qquad
A_-=\begin{pmatrix}-a&-1\\1&0\end{pmatrix}.
\]
The eigenvalues of \(A_+\) are \(e^{\pm i\theta}\), hence \(A_+^n=-I\). Put
\[
u_j=\frac{\sin((j+1)\theta)}{\sin\theta},\qquad u_{-1}=0,
\]
so \(u_0=1\), \(u_j>0\) for \(0\leq j\leq n-2\), \(u_{n-1}=0\), and \(u_{j+1}=a u_j-u_{j-1}\). Starting from \(r_0=(0,1)\), the next vector is \(r_1=(-1,0)\). A negative-branch marker of the form \((-u_j,u_{j-1})\), for \(0\leq j\leq n-3\), is sent to \((u_{j+1},-u_j)\). Its following \(n\) positive-branch iterates have first coordinates
\[
\frac{u_{j+1}\sin((m+1)\theta)+u_j\sin(m\theta)}{\sin\theta}>0,
\qquad 0\leq m\leq n-1.
\]
Finally \(A_+^n(u_{j+1},-u_j)=(-u_{j+1},u_j)\), the next negative-branch marker. Inductively,
\[
T_n^{1+j(n+1)}(0,1)=(-u_j,u_{j-1}),\qquad 0\leq j\leq n-2.
\]
The last marker is \((-1,a)\) at time \(n^2-n-1\). Its next image is \((0,-1)\), so
\[
T_n^{q-n}(0,1)=(0,-1).
\]
For the next \(n\) iterations the positive branch applies (except at the initial zero first coordinate), and \(A_+^n(0,-1)=(0,1)\). The only zero first coordinates in this orbit before return occur at times \(0\) and \(q-n\), with opposite vertical directions. Therefore the orbit of the positive vertical ray has **exactly \(q=n^2\) distinct rays**. Positive homogeneity makes these ray statements valid at every positive radius.

**2. Angular order and the invariant sector weights.** Lagarias and Rains established for this family that the induced orientation-preserving map on the circle of rays has rotation number
\[
\rho=\frac{n-1}{n^2}=\frac pq
\]
and is periodic with period \(q\); see their Example 3.2 and its specialization to opposite coefficients. Their general formula \(\rho=\vartheta/(\pi+n\vartheta)\), at \(\vartheta=(n-1)\pi/n\), gives exactly \(p/q\). Since the orbit of the positive vertical ray has length \(q\), its \(q\) rays cut the plane into \(q\) angular sectors, indexed counterclockwise by \(j\in\mathbb Z/q\mathbb Z\). The map sends sector \(j\) to sector \(j+p\): an orientation-preserving cyclic permutation with rotation number \(p/q\) must make that shift.

The negative first-coordinate half-plane is the counterclockwise region between the positive and negative vertical rays. By step 1, the negative vertical ray is reached after \(q-n\) time steps, hence its counterclockwise sector-index displacement is
\[
p(q-n)\equiv n\pmod q.
\]
Therefore the negative half-plane consists of **exactly \(n\) consecutive sectors** in the angular order. Because \(\gcd(p,q)=1\), the sector permutation is transitive. The zero-boundary-mass and invariance hypotheses then force every sector to have probability \(1/q\), for any admissible \(\mu\).

Choosing angular indices so the negative sectors are \(\{0,\ldots,n-1\}\), the uniformly distributed initial sector index \(K\) evolves as \(K+pt\bmod q\). This proves the asserted **entire process law**, including its multi-time cylinder probabilities, without assuming ergodicity or a specific invariant density.

**3. Exact overlap and independence classification.** For an interval of \(n\) consecutive residues in the cyclic group of order \(q=n^2\), its overlap with a translate by \(d\in\{0,\ldots,q-1\}\) has cardinality
\[
(n-d)_+ +(n-q+d)_+=(n-\min\{d,q-d\})_+,
\]
since \(q\geq2n\) for \(n\geq3\). Divide this overlap by \(q\) to obtain the two-time formula. Subtract \((1/n)^2=1/q\) for covariance. Two Bernoulli observations are independent if and only if their joint-one probability equals the product of their marginal-one probabilities. This is equivalent to \(D_k=n-1\), or \(pk\equiv\pm(n-1)\pmod{n^2}\). Multiplication by \(p=n-1\) is invertible modulo \(n^2\), so precisely \(k\equiv\pm1\) satisfies the condition. For \(k=2\) one has \(D_k\geq n\), hence exclusion; for \(k=n+1\) one has \(pk\equiv-1\), hence overlap \(n-1\). All statements follow.

## Verification

The supplied standalone script `check.py` verifies the branch-matrix identity for several exact algebraic coefficients, independently counts all cyclic interval overlaps for \(3\leq n<150\), and uses high-precision ray geometry to check angular order, sector shifts, sign-block lengths, and temporal intersections for \(3\leq n\leq10\). Run with `python check.py` in an environment containing SymPy and mpmath; the successful output ends in `VERIFY_OK`. These finite computations are consistency checks only: the all-\(n\), all-lag theorem rests on the analytic proof above and the cited established rotation-number result.

## Relationship to prior work

Lagarias and Rains (2003), Part I, introduced the underlying two-branch area-preserving family and established its rotation-number formula, finite-order specialization, and general sector mechanism. The periodic family and its rotation numbers also appeared in earlier work by Beardon, Bullett, and Rippon (1995). These are prior results, not contributions of this finding. The present result determines a **specific full invariant-measure-independent sign-process law**, including all joint cylinder probabilities and sharp independence/exclusion/recurrence classes across the entire quadratic-period family. Neither of the accessible Lagarias–Rains full texts inspected states this statistical classification. Because the classification is obtained from their angular dynamics plus an explicit switching-ray orbit calculation, its historical priority relative to earlier symbolic-dynamics treatments merits independent assessment.

## Limitations

No claim is made about invariant measures charging the switching rays, about generic parameter values outside the specified cosine family, about coordinate-amplitude correlations, or about measure-theoretic mixing (the dynamics is periodic). The present comparisons do not establish absolute priority; the full 1995 primary article could not be inspected through available access. The probability model depends crucially on invariance and on zero mass for the boundary ray orbit, not merely on selecting a uniform initial Euclidean angle.

## References

1. J. C. Lagarias and E. Rains, *Dynamics of a family of piecewise-linear area-preserving plane maps I. Rational rotation numbers* (first public preprint 25 January 2003), arXiv:math/0301294. https://arxiv.org/abs/math/0301294
2. J. C. Lagarias and E. M. Rains, *Dynamics of a family of piecewise-linear area-preserving plane maps II. Invariant circles* (first public preprint 1 March 2003), arXiv:math/0303007. https://arxiv.org/abs/math/0303007
3. A. F. Beardon, S. R. Bullett and P. J. Rippon, *Periodic orbits of difference equations*, Proc. Roy. Soc. Edinburgh Sect. A **125** (1995), 657–674. https://doi.org/10.1017/S0308210500030286
