# A five-page spine-deletion threshold for fastest diffusion on pendant book graphs

## Finding
For every integer \(m\ge2\), start with the book graph \(K_2\vee\overline{K_m}\): adjacent hubs \(u,v\) share \(m\) other neighbors \(p_1,\ldots,p_m\), and no edges join distinct pages. Add one leaf \(z\) attached only to \(u\). For arbitrary **nonnegative** undirected conductances on the \(2m+2\) allowed edges, with total conductance exactly \(B>0\), write \(\lambda_2(L)\) for the second eigenvalue of the unnormalized weighted graph Laplacian.

Define
\[
D_m=\begin{cases}
 m+2-\dfrac{m^2}{4(m+3)},&2\le m\le4,\\[3pt]
 m+1+\dfrac4{m^2-8},&m\ge5.
\end{cases}
\]
Then the exact unrestricted optimum is
\[
\boxed{\max_{w\ge0,\,\sum_e w_e=B}\lambda_2(L(w))=\frac{B}{D_m}.}
\]
There is a sharp edge-screening transition: for \(m=2,3,4\) the construction below gives an optimal allocation with strictly positive conductance on every edge. For **every** \(m\ge5\), **every** globally optimal allocation gives the common hub–hub spine edge zero conductance; the other permitted edges can all be given positive conductance optimally. No symmetry condition is imposed on competitors.

Here is an explicit optimum. Set \(\lambda=B/D_m\) and assign the same weights within each indicated edge family: \(w_{uv}=\lambda x\), \(w_{up_i}=\lambda a\), \(w_{vp_i}=\lambda b\), and \(w_{uz}=\lambda c\), with
\[
(x,a,b,c)=\begin{cases}
\left(\dfrac{-m^2+2m+12}{4(m+3)},\dfrac{m+6}{2(m+3)},\dfrac{m}{2(m+3)},\dfrac{3(m+2)}{2(m+3)}\right),&2\le m\le4,\\[8pt]
\left(0,\dfrac{m}{m+2},\dfrac{2}{m+2},\dfrac{m^2-4}{m^2-8}\right),&m\ge5.
\end{cases}
\]
For example, \(D_2=19/5\), \(D_3=37/8\), \(D_4=38/7\), \(D_5=106/17\). The optimal second eigenvalue has multiplicity \(m\) for this displayed allocation.

## Assumptions and scope
The graph is simple, unweighted in its allowed-edge **topology**, and has exactly \(m+3\) vertices. Conductances may be zero, and \(B\) is any strictly positive real. The objective is the continuous-time symmetric Markov/diffusion decay rate \(\lambda_2(L)\), **not** the discrete-time second-largest-eigenvalue modulus or the largest Laplacian eigenvalue. The hub–hub edge is called the spine. The assertion about **all** optimizers concerns only its zero conductance for \(m\ge5\), not uniqueness of the other weights. The case \(m=1\) is excluded.

## Proof
**1. A universal geometric upper certificate.** Put \(N=m+3\) and \(A=(m+2)/2\). For any nonconstant points \(q_i\) in Euclidean space whose squared distances along all allowed edges do not exceed one, define their centered sum of squares
\[
V=\sum_i\|q_i-\bar q\|^2,\qquad \bar q=N^{-1}\sum_iq_i.
\]
For a weighted Laplacian and \(X=\sum_i(q_i-\bar q)(q_i-\bar q)^{\mathsf T}\), the Rayleigh principle, applied coordinatewise, gives
\[
\lambda_2(L)V\le\sum_{\{i,j\}}w_{ij}\|q_i-q_j\|^2\le B.
\]
Choose a unit axis \(e_0\), and choose unit regular-simplex vectors \(f_1,\ldots,f_m\), orthogonal to \(e_0\), with \(\sum_i f_i=0\). For \(s\in(0,1]\) put
\[
q_u=0,\quad q_v=s e_0,\quad q_z=-e_0,\quad
q_{p_i}=\frac{s}{2}e_0+\sqrt{1-\frac{s^2}{4}}\,f_i.
\]
The hub-to-page, other-hub-to-page, and leaf edge lengths are all exactly one, while the spine length is \(s\). Thus this is feasible for every \(s\le1\), and direct centering gives
\[
V(s)=m+1+s^2-\frac{(As-1)^2}{N}.
\]
Use \(s=1\) for \(2\le m\le4\), and \(s=2(m+2)/(m^2-8)\) for \(m\ge5\). In the latter regime \(0<s<1\). Direct substitution yields \(V(s)=D_m\), proving \(\lambda_2(L)\le B/D_m\) for **every**, including nonsymmetric, allocation. This does not assume that the geometric configuration solves the full dual problem: matching with an achievable primal bound below proves optimality.

**2. A matching explicit allocation.** Normalize the displayed conductances by setting \(\lambda=1\), so \(x+m(a+b)+c=D_m\). Write
\[
\mu=\frac{As-1}{N},\qquad
 a=1-\frac{\mu}{s},\quad b=\frac{\mu}{s},\quad
 c=1+\mu,\quad x=1-A\frac{\mu}{s}.
\]
These expressions reduce exactly to the two displayed formulas. All weights are nonnegative in the stated ranges: \(x>0\) for \(m=2,3,4\), and \(x=0\) for \(m\ge5\); also \(a,b,c>0\). The \(m-1\)-dimensional space of page vectors whose entries sum to zero is a Laplacian eigenspace with eigenvalue \(a+b=1\). The axial vector whose values on \(u,v,p_i,z\) are respectively \(0,s,s/2,-1\), after subtracting its mean \(\mu\), is another eigenvector with eigenvalue one. Indeed its four equations are
\[
-sx-\frac{mas}{2}+c=-\mu,\qquad
sx+\frac{mbs}{2}=s-\mu,\qquad
\frac{(a-b)s}{2}=\frac{s}{2}-\mu,\qquad
-c=-1-\mu.
\]
Consequently, eigenvalue one has multiplicity at least \(m\).

**3. No smaller positive eigenvalue.** On the remaining four-dimensional subspace, parameterize a vector by its entries at \(u,v\), a common entry at all pages, and its entry at \(z\). The restricted Laplacian is similar to the symmetric restriction and has matrix
\[
H=\begin{pmatrix}
x+ma+c&-x&-ma&-c\\
-x&x+mb&-mb&0\\
-a&-b&a+b&0\\
-c&0&0&c
\end{pmatrix}.
\]
Its eigenvalues are \(0,1,r_-,r_+\), with the last two real. Computing its characteristic polynomial gives \(r_-+r_+=S_m\) and \((r_--1)(r_+-1)=P_m\), where
\[
S_m=\begin{cases}
\dfrac{(m+2)(m+12)}{2(m+3)},&2\le m\le4,\\[3pt]
\dfrac{m^3+2m^2-8m-8}{m^2-8},&m\ge5,
\end{cases}
\]
and
\[
P_m=\begin{cases}
\dfrac{m^2(11m+24)}{8(m+3)^2},&2\le m\le4,\\[3pt]
\dfrac{m(m^3-m^2-6m+16)}{(m+2)(m^2-8)},&m\ge5.
\end{cases}
\]
For \(2\le m\le4\), both \(P_m>0\) and \(S_m-2=(m^2+6m+12)/(2(m+3))>0\). For \(m\ge5\), \(P_m>0\) and \(S_m-2=(m^3-8m+8)/(m^2-8)>0\). Since \(r_\pm\) are real, these inequalities imply \(r_->1\) and \(r_+>1\). Thus the smallest positive eigenvalue is exactly one, with multiplicity exactly \(m\). Rescaling the weights by \(B/D_m\) attains the universal upper bound.

**4. Necessity of deleting the spine.** In the geometric certificate for \(m\ge5\) the spine has squared length \(s^2<1\), while all other used-edge squared lengths equal one. For any feasible allocation,
\[
\lambda_2(L)D_m\le B-w_{uv}(1-s^2)\le B.
\]
At an optimal allocation the left and right endpoints both equal \(B\), forcing \(w_{uv}=0\). This holds without any symmetry assumption and proves the all-optimizers assertion. \(\square\)

## Verification
Running `python verify.py` with Python 3 and SymPy checks the characteristic-polynomial quotients, budget identities, and axial eigenvector equations **symbolically in the parameter** \(m\). With NumPy it additionally constructs and diagonalizes 119 complete matrices for the integer range \(2\le m\le120\), checking the gap, multiplicity, costs, and positivity. The executable checks were run and passed. The finite sample is corroboration, not a substitute for the displayed arbitrary-integer proof.

## Relationship to prior work
The continuous-time fastest-mixing formulation and maximum-variance embedding duality are due to Sun, Boyd, Xiao, and Diaconis (2006). They develop a general semidefinite method, with explicit examples for paths, cycles, and an irregular six-vertex graph; the paper does not give the above pendant-book evaluation. In its example a slack geometric edge may also vanish in all optima, but it does not imply a five-page threshold for this graph family. The weighted pendant-edge study of Berman and Förster (2005) concerns monotonicity with an increasing leaf weight and infinite-weight limits, mainly for trees, not unrestricted budget allocation on a family containing cycles. Earlier work by Fiedler studies absolute algebraic connectivity and trees. The present contribution is the explicit piecewise rational optimum and the forced hub-spine deletion transition for the specified book-with-leaf family. Some earlier specialized coverage remains possible.

## Limitations
This result treats only a pendant vertex attached to one hub of a triangular book graph with at least two pages and the uniform total conductance objective. It does not address different edge costs, nonuniform stationary distributions, the one-page case, or discrete-time mixing. No claim is made about uniqueness of the other optimal edge conductances. Literature searching and a direct comparison of accessible primary full text do not prove exhaustive novelty; the 1993 Fiedler article could not be inspected in full. No independent audit has been conducted.

## References
1. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review **48** (2006), 681–699, DOI:10.1137/S0036144504443821. Public electronic date: 2006-11-02. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.
2. A. Berman and K.-H. Förster, *Algebraic Connectivity of Trees with a Pendant Edge of Infinite Weight*, Electronic Journal of Linear Algebra **13** (2005), 175–186. Full text: https://emis.de/ft/15363.
3. M. Fiedler, *Some Minimax Problems for Graphs*, Discrete Mathematics **121** (1993), 65–74, DOI:10.1016/0012-365X(93)90538-5. Abstract-level comparison only.
