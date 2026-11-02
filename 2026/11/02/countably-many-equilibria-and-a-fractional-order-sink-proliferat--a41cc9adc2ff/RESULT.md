# Countably many equilibria and a fractional-order sink-proliferation law in the sine–cubic map

## Finding
For the real-state commensurate Caputo-delta sine–cubic system, the equilibrium set has an abrupt change at \(c=1\): it is a singleton for \(0<c<1\), an integer lattice at \(c=1\), and four doubly infinite trigonometric branches together with the origin for \(c>1\). For each fixed fractional order \(0<\nu\le1\), an exact one-dimensional spectral threshold gives the linear stability of every nonzero branch. The number of nonzero equilibria with linearly asymptotically stable dynamics diverges as
\[
N_\nu(c)=\frac{d_\nu}{\pi\sqrt{c-1}}+O_\nu(1)\qquad(c\downarrow1).
\]
The exact coefficient \(d_\nu\) depends on the fractional order, and \(d_1=1\).

## Assumptions and scope
The state space is all of \(\mathbb R^2\), not a bounded plotting window. For \(c>0\) and a common Caputo-delta order \(0<\nu\le1\), the published system has fractional right-hand side
\[
G_c(x,y)=\big(\sin(\pi y)-x,\ [c(1-x^2)-1]y\big).
\]
A stationary state means a constant real sequence annihilated by this right-hand side. At \(\nu=1\), this is the ordinary discrete map \((x,y)\mapsto(\sin(\pi y),c(1-x^2)y)\). A linearly asymptotically stable equilibrium is one whose constant-coefficient Caputo-delta variational equation lies in the strict spectral stability region given in the 2015 linear stability reference. This is a local linear conclusion, not a statement about attracting basins or numerical finite-time behavior.

Put \(r=\sqrt{1-1/c}\) and \(\theta=\arcsin(r)/\pi\) when \(c>1\). Then the complete stationary set is \(\{(0,0)\}\) for \(0<c<1\), \(\{(0,m):m\in\mathbb Z\}\) for \(c=1\), and for \(c>1\) consists of \((0,0)\) and
\[
(r,2k+\theta),\quad(r,2k+1-\theta),\quad(-r,2k-\theta),\quad(-r,2k+1+\theta),\qquad k\in\mathbb Z.
\]
All these points are distinct for \(c>1\). Define the unique threshold \(d_\nu>1/4\) through
\[
\sqrt{d_\nu}=\left[2\cos\left(\frac{\arccos[-1/(2\sqrt{d_\nu})]-\pi}{2-\nu}\right)\right]^\nu.
\]
At a nonzero stationary state put \(D=2\pi cxy\cos(\pi y)\).

## Proof
First, \(G_c(x,y)=0\) gives \(x=\sin(\pi y)\) and \([c(1-x^2)-1]y=0\). If \(y=0\), then \(x=0\). If \(y\ne0\), then \(x^2=1-1/c\). For \(0<c<1\), there are no real nonzero solutions. At \(c=1\), this forces \(x=0\), while \(\sin(\pi y)=0\) forces precisely the integers \(y=m\). For \(c>1\), \(x=\pm r\), and the complete real solutions of the sine equation yield exactly the four displayed families. This proves exhaustiveness without a truncation in \(y\).

At each nonzero equilibrium the linearized fractional right-hand side is
\[
M=\begin{pmatrix}-1&\pi\cos(\pi y)\\-2cxy&0\end{pmatrix},\qquad
\operatorname{tr}M=-1,\quad\det M=D.
\]
Since \(|x|=r\), \(|\cos(\pi y)|=1/\sqrt c\), the determinant satisfies the exact identity
\[
|D|=2\pi\sqrt{c-1}\,|y|.
\]
If \(D<0\), the characteristic polynomial \(z^2+z+D\) has a positive real root, outside every asymptotic Caputo-delta stability sector. If \(0<D\le1/4\), both roots are real and lie strictly between \(-1\) and \(0\), so they lie within the stable sector for every \(0<\nu\le1\). For \(D>1/4\), the roots are \(-1/2\pm i\sqrt{D-1/4}\), of modulus \(\sqrt D\) and absolute argument \(\phi(D)=\arccos[-1/(2\sqrt D)]\). Their argument lies strictly between \(\pi/2\) and \(\pi\), hence exceeds \(\nu\pi/2\). The standard Caputo-delta linear stability criterion reduces exactly to
\[
\sqrt D<\left[2\cos\left(\frac{\phi(D)-\pi}{2-\nu}\right)\right]^\nu.
\]
As \(D\) increases from \(1/4\) to infinity, its left side strictly increases from \(1/2\) to infinity, whereas the right side strictly decreases from \(2^\nu\) to a positive finite value. Therefore the two sides cross exactly once, at \(D=d_\nu>1/4\). All nonzero equilibria with \(0<D<d_\nu\) and only those satisfy the strict linear asymptotic stability inequalities; \(D=d_\nu\) is a spectral boundary, with no claim of nonlinear stability. Substitution of \(\nu=1\) yields \(d_1=1\).

For a fixed \(c>1\), the stable nonzero equilibria are precisely those with \(D>0\) and \(|y|<L_\nu(c)\), where \(L_\nu(c)=d_\nu/[2\pi\sqrt{c-1}]\). The four periodic families listed above have an exact density of one positive-\(D\) equilibrium per unit length on the positive \(y\)-axis and likewise on the negative axis, up to a bounded integer-part discrepancy. This follows directly by checking the signs of \(xy\cos(\pi y)\) on each family and counting translates of period \(2\). Consequently
\[
N_\nu(c)=2L_\nu(c)+O(1)=\frac{d_\nu}{\pi\sqrt{c-1}}+O_\nu(1).
\]
The integer-part error is bounded uniformly in \(c\) sufficiently near \(1\); the dependence on \(\nu\) enters through its fixed threshold. This proves the stated proliferating linear-stability census.

## Verification
The equilibrium formulas were substituted into both components of \(G_c\), and the Jacobian trace and determinant were reconstructed symbolically. A finite Python check before packaging counted stable ordinary-map equilibria at \(c=1.1,1.01,1.001,1.0001\), obtaining \(2,4,12,32\), respectively, versus the predicted leading terms \(1.0066,3.1831,10.0658,31.8310\). A scalar root check of the strict fractional threshold produced \(d_{1/4}\approx1.2690067363\), \(d_{1/2}\approx1.4476229869\), \(d_{3/4}\approx1.3750764795\), and \(d_1=1\). The infinite equilibrium count, exact stability criterion, and asymptotic law follow from the proof rather than the finite calculations.

## Relationship to prior work
The 2022 paper by Liu, Tang, and Hong supplies the precise Caputo-delta system and prints only the origin plus two principal-arcsine nonzero equilibria. The complete sine equation on the unbounded real state space produces the additional lattice and branches, and the stability-count divergence is a separate exact consequence. The 2013 paper by Bi and collaborators introduced the corresponding integer-order map and analyzed fixed points, so the integer-order special case is not presented as an independent discovery; the fractional-order threshold and stable-branch proliferation for all \(0<\nu\le1\) are the contribution here. The exact linear stability sector is taken from the standard Caputo-delta spectral criterion cited by the 2022 paper. Related literature and semantic research records were searched for full real-state equilibrium classification and the order-dependent count asymptotic; no equivalent statement was located. Absence from searches is not a proof of priority.

## Limitations
The result concerns the published real-state equations without imposing an artificial bounded plotting window. It does not classify nonlinear stability at spectral boundaries, prove global basin measures, or determine transient trajectories. The 2013 original paper's abstract and metadata were read, but its complete 14 MB PDF was not available for material comparison; an uninspected prior result addressing the full integer-order equilibrium census remains possible. The paper's 2022 full-text fixed-point section was inspected. The linear asymptotic stability statement uses the cited Caputo-delta spectral theorem and its strict conditions; no independent verification has been performed.

## References
Liu, X., Tang, D., and Hong, L. (2022), *A Fractional-Order Sinusoidal Discrete Map*, Entropy 24, 320. DOI: 10.3390/e24030320. First online 2022-02-23.

Bi, C., Zhang, Q., Xiang, Y., and Wang, J.-M. (2013), *Bifurcation and attractor of two-dimensional sinusoidal discrete map*, Acta Physica Sinica 62, 240503. DOI: 10.7498/aps.62.240503.

Čermák, J., Győri, I., and Nechvátal, L. (2015), *On explicit stability conditions for a linear fractional difference system*, Fractional Calculus and Applied Analysis 18, 651–672. DOI: 10.1515/fca-2015-0040.
