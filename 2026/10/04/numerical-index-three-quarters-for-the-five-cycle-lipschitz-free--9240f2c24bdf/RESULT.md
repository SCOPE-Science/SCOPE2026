# Numerical index three quarters for the five-cycle Lipschitz-free space
## Finding
Let \(C_5\) be the graph cycle on vertices \(\{0,1,2,3,4\}\), every edge having length \(1\), equipped with its shortest-path metric and basepoint \(0\). For the real Lipschitz-free space \(X=\mathcal F(C_5)\),
\[
n(X)=\frac{3}{4}.
\]
Here \(n(X)=\inf\{v(T):\|T\|=1\}\), where \(v(T)\) is the numerical radius of a bounded linear operator \(T:X\to X\).

## Assumptions and scope
The scalar field is real. Write \(e_k=\delta_k\) for \(1\le k\le4\), with \(\delta_0=0\). In this basis the extreme points of \(B_X\) are the ten oriented edge molecules
\[
\pm e_1,\quad \pm(e_2-e_1),\quad \pm(e_3-e_2),\quad \pm(e_4-e_3),\quad \pm e_4.
\]
Every non-edge molecule decomposes along a shortest edge path, while every edge molecule is extreme because its metric segment contains only its two endpoints.

For \(f\in\operatorname{Lip}_0(C_5)\), put
\[
d_1=f(1),\quad d_2=f(2)-f(1),\quad d_3=f(3)-f(2),\quad d_4=f(4)-f(3),\quad d_5=-f(4).
\]
Then \(B_{X^*}\) is the section of \([-1,1]^5\) by \(d_1+\cdots+d_5=0\). Its extreme points are exactly the thirty vectors for which one \(d_i\) is \(0\) and the other four consist of two \(+1\)'s and two \(-1\)'s. There are exactly \(120\) pairs \((x,f)\) of primal and dual extreme points with \(f(x)=1\).

## Proof
For a finite-dimensional real polyhedral Banach space, the numerical radius of \(T\) is obtained from norming pairs of primal and dual extreme points. Hence
\[
v(T)=\max\{|f(Tx)|:x\in\operatorname{Ext}B_X,\ f\in\operatorname{Ext}B_{X^*},\ f(x)=1\}.
\]
Also
\[
\|T\|=\max\{f(Tx):x\in\operatorname{Ext}B_X,\ f\in\operatorname{Ext}B_{X^*}\},
\]
because the dual extreme set is symmetric.

Fix one of the \(10\cdot30=300\) possible active pairs \((x_0,f_0)\) and impose \(f_0(Tx_0)=1\). Minimizing \(t\) subject to \(f(Tx)\le1\) for all \(300\) primal-dual extreme pairs and \(-t\le f(Tx)\le t\) for all \(120\) norming incidence pairs is a finite linear program whose optimum is the least possible numerical radius among norm-one operators with that active pair. The accompanying certificate contains an exact rational dual feasible solution for every one of these \(300\) programs. Each dual objective is at least \(3/4\), so exact weak duality gives \(v(T)\ge3/4\) for every norm-one \(T\).

The reverse inequality is attained by the operator whose matrix in the basis \((e_1,e_2,e_3,e_4)\) is
\[
T=\begin{pmatrix}
-1/4&0&0&0\\
0&1/4&0&0\\
0&0&0&0\\
0&-1/2&0&0
\end{pmatrix}.
\]
Exact evaluation on the ten primal and thirty dual extreme points gives \(\|T\|=1\), while evaluation on all \(120\) norming incidence pairs gives \(v(T)=3/4\). Thus \(n(\mathcal F(C_5))=3/4\).

## Verification
Run `python3 artifacts/verify.py`. The checker reconstructs the ten primal extreme points, the thirty dual extreme points and all \(120\) norming incidence pairs. Using exact rational arithmetic, it checks sign, stationarity and objective for every sparse dual certificate for the \(300\) active-pair linear programs and independently evaluates the displayed attaining operator. A successful replay prints `VERIFY_OK cases=300 incidence=120 operator_norm=1 numerical_radius=3/4`.

This finite certificate is not evidence for an infinite extrapolation: the theorem itself is a finite-dimensional exact statement and every case in the finite reduction is checked.

## Relationship to prior work
Cobollo, Guirao and Montesinos give an explicit formula for numerical indices of all two-dimensional Lipschitz-free spaces and identify higher-dimensional Lipschitz-free numerical-index problems as a natural continuation. Their theorem does not determine the four-dimensional space \(\mathcal F(C_5)\). Aliaga and Guirao characterize extreme molecules in compact Lipschitz-free spaces, supplying the extremal criterion used above. Sain, Paul, Bhunia and Bag give a finite method for numerical indices of polyhedral Banach spaces and compute a particular three-dimensional family; that result does not supply the present four-dimensional cycle value.

Searches were also made for the cycle description, the quotient description of a cycle free space, and the combinatorial signature of a four-dimensional polytope with ten primal and thirty dual extreme points. No located source stated or implied the value \(3/4\) for \(\mathcal F(C_5)\). The remaining novelty risk is that the same four-dimensional norm may occur elsewhere under an unrecognized isometric description.

## Limitations
Only the real five-cycle is claimed. No formula is asserted for \(\mathcal F(C_n)\) with \(n\ne5\), for complex scalars, or for arbitrary graph metrics. The exact lower bound uses a complete finite polyhedral reduction; it is not a structural formula for all Lipschitz-free spaces. Bibliographic searches cannot exclude every unpublished or differently named equivalent computation.

## References
1. Ch. Cobollo, A. J. Guirao, V. Montesinos, “The numerical index of 2-dimensional Lipschitz-free spaces,” arXiv:2304.13183, first public version 2023-04-25.
2. R. J. Aliaga, A. J. Guirao, “On the preserved extremal structure of Lipschitz-free spaces,” arXiv:1705.09579, first public version 2017-05-26.
3. D. Sain, K. Paul, P. Bhunia, S. Bag, “On the numerical index of polyhedral Banach spaces,” arXiv:1809.04778, first public version 2018-09-13.
