# Complete rational-rung controllability ranks on three-rail path grids

## Finding

For every integer \(n\ge2\), every rational rung conductance \(r\ge1\), and every single controlled vertex \((s,p)\) with \(1\le s\le n\), \(p\in\{1,2,3\}\), there is an explicit closed formula for the Kalman controllability rank of the symmetric consensus system on the three-rail weighted grid \(P_n\square P_3\). In particular, exactly four rational weights \(r\ge1\), namely \(1,3/2,2,3\), ever cause a *cross-branch spectral collision*, for any length. The uniform weight \(r=4/3\) guarantees full controllability from a corner of every length; at unit weight an additional exact mod-five resonance appears.

Put \(q=2s-1\), \(g=\gcd(n,q)\), and \(H=n-(g-1)/2\). Define the zero-one integers
\[
\begin{split}
 e&=\mathbf1_{2\mid n},\qquad f=\mathbf1_{3\mid n},\\
 u&=\mathbf1_{3\mid n,\,3\nmid q},\qquad v=\mathbf1_{5\mid n,\,5\nmid q},\\
 h&=\mathbf1_{6\mid n,\,3\nmid q}.
\end{split}
\]
For an **outer-rail** control \(p\in\{1,3\}\), the exact rank is
\[
\operatorname{rank}\mathcal C=
\begin{cases}
3H-(2u+h+2v+e+f),&r=1,\\
3H-f,&r=3/2,\\
3H-(e+u),&r=2,\\
3H-f,&r=3,\\
3H,&r\in\mathbb Q_{\ge1}\setminus\{1,3/2,2,3\}.
\end{cases}
\]
For the **middle-rail** control \(p=2\), the exact rank is
\[
\operatorname{rank}\mathcal C=2H-\mathbf1_{r=1}f.
\]
These formulas quantify reachable state-space dimension, not merely a binary controllability decision. The system is fully controllable from a corner for all lengths precisely when the fixed rational weight belongs to \(\mathbb Q_{\ge1}\setminus\{1,3/2,2,3\}\).

## Assumptions and scope

Every longitudinal edge in each of three copies of \(P_n\) has unit conductance. Each edge joining adjacent rails at the same longitudinal location has the same rational conductance \(r\ge1\). Let \(L_n\) be the ordinary combinatorial path Laplacian and \(L_3\) the three-vertex path Laplacian. The network Laplacian, in rail-major vertex order, is
\[
\boxed{L=I_3\otimes L_n+rL_3\otimes I_n.}
\]
The continuous-time dynamics are \(\dot z=-Lz+e_{(p,s)}a(t)\). The Kalman matrix is \(\mathcal C=[b,Lb,\ldots,L^{3n-1}b]\); changing \(L\) to \(-L\) does not change its rank. The column dimension is \(3n\). There is one unrestricted scalar input, not one independent input per rail.

## Proof

**1. Product eigenmodes and local visibility.** The path \(P_n\) has distinct Laplacian eigenvalues
\[
\lambda_j=2-2\cos(\pi j/n),\quad j=0,\ldots,n-1,
\]
with eigenvectors \(\phi_j(s)=\cos((2s-1)\pi j/(2n))\), up to nonzero normalization. The transverse three-path has eigenvalues \(0,1,3\) with eigenvectors proportional to \((1,1,1)\), \((1,0,-1)\), \((1,-2,1)\). Consequently the eigenvalue branches are \(\lambda_j\), \(\lambda_j+r\), \(\lambda_j+3r\). All three are locally visible from an outer-rail input whenever \(\phi_j(s)\ne0\). At a middle-rail input only the first and third are locally visible. For a real symmetric matrix with a single input, the reachable dimension equals the number of **distinct** eigenvalues whose spectral projection of the input is nonzero (the PBH theorem, or the spectral Vandermonde decomposition).

The zero condition \(\phi_j(s)=0\) is equivalent to \(qj/n\) being an odd integer. Since \(q\) is odd and \(g=\gcd(n,q)\) is odd, its solutions \(j\in\{1,\ldots,n-1\}\) are exactly \(j=(n/g)\ell\), for odd \(\ell\in\{1,3,\ldots,g-2\}\). Their number is \((g-1)/2\), leaving exactly \(H\) visible longitudinal modes.

**2. A sharp integer-gap lemma.** For any two distinct path eigenvalues, a rational difference is an integer, since both eigenvalues are algebraic integers. Every positive difference lies in \((0,4)\), so its rational value must be \(d=1,2,3\). More precisely, the **only** ordered pairs \((\lambda_i,\lambda_j)\) with \(\lambda_j-\lambda_i=d\) are

| \(d\) | Ordered pairs; required divisibility of \(n\) |
|---|---|
| \(1\) | \((0,1)\), \(3\mid n\); \((1,2)\), \((2,3)\), \(6\mid n\); \(((3-\sqrt5)/2,(5-\sqrt5)/2)\) and \(((3+\sqrt5)/2,(5+\sqrt5)/2)\), \(5\mid n\) |
| \(2\) | \((0,2)\), \(2\mid n\); \((1,3)\), \(3\mid n\) |
| \(3\) | \((0,3)\), \(3\mid n\) |


Here is a self-contained classification proof. Write \(u=2\cos(\pi i/n)\), \(v=2\cos(\pi j/n)\), so \(u-v=d\). Each is a cyclotomic integer; under every Galois conjugation its value lies in \([-2,2]\). Hence every conjugate of \(u\) lies in \([d-2,2]\). For any primitive root of unity \(\zeta\) of order \(m\), if all primitive conjugates satisfy \(2\operatorname{Re}\zeta\ge-1\), then \(m\in\{1,3,4,6,10\}\). Indeed, for odd \(m\ge5\), the primitive power \((m-1)/2\) has real part \(-\cos(\pi/m)<-1/2\); for \(4\mid m\) with \(m\ge8\), the primitive power \(m/2-1\) has real part \(-\cos(2\pi/m)<-1/2\); for \(m=2t\), odd \(t\ge7\), the primitive power \(t-2\) has real part \(-\cos(2\pi/t)<-1/2\). The remaining orders are checked directly, with order two excluded. For \(d=1\), this permits \(u=2,1,0,-1,(1\pm\sqrt5)/2\). Requiring \(v=u-1\) also to be a path cosine and excluding the unattained endpoint \(v=-2\) yields exactly the listed integer and golden pairs. For \(d=2\), the condition that every conjugate of \(u\) be nonnegative removes orders three and ten; only \(u=2,1,0\) survive, with \(u=0\) excluded by the unattained endpoint. For \(d=3\), every conjugate of \(u\) is at least one, leaving \(u=2,1\), of which the latter has excluded endpoint \(v=-2\). Converting the remaining root angles to path indices gives precisely the divisibility conditions in the table.

**3. Only four rational collision weights.** Between transverse branches \(0,1,3\), the shift differences are \(r,2r,3r\). By the integer-gap lemma and \(r\ge1\), collisions are possible only at \(r\in\{1,3/2,2,3\}\). For \(r=3/2\) the only collision is the gap-three pair between the \(1\)- and \(3\)-branches. For \(r=2\) it is the gap-two pair between the \(0\)- and \(1\)-branches. For \(r=3\) it is the gap-three pair between the \(0\)- and \(1\)-branches. The exceptions are genuine: weights \(r=1,2\) collide for \(n=2\), and \(r=3/2,3\) collide for \(n=3\), already from a corner.

At \(r=1\), count visible overlap pairs between shifted branches. Gap-one pairs contribute \(u+h+\mathbf1_{6\mid n}+2v\), gap-two pairs contribute \(e+u\), and the gap-three pair contributes \(f\). The only possible three-way overlap is at the common eigenvalue \(3\), when \(6\mid n\): its three constituents are \((3,0)\), \((2,1)\), \((0,3)\), all longitudinally visible; it is counted three times pairwise but should cause only two lost dimensions. Subtracting the extra \(\mathbf1_{6\mid n}\) gives the stated outer-rail formula. For middle-rail controls, the transverse \(1\)-branch is invisible; only the shift \(3r\) can collide, which happens exactly at \(r=1\), \(3\mid n\), through \((0,3)\). This proves the middle-rail formula and completes the classification.

## Verification

Run \(\texttt{python3 verify_grid.py}\): it computes modular Krylov ranks of the **original weighted graph** at all \(3240\) combinations \(2\le n\le16\), all input sites, and eight rational edge weights \(1,3/2,2,3,4/3,5/4,7/3,4\), and checks every rank against the theorem. The modulus is \(1000003\), which does not divide any edge-weight denominator. Run \(\texttt{python3 verify_gaps.py}\) after installing \(\texttt{sympy}\): it verifies \(147\) exact polynomial-gcd identities for all \(2\le n\le50\), and all three integer spectral gaps. Neither finite calculation replaces the general cyclotomic proof. The scripts use no downloaded data.

At \(n=6\), outer-corner input and \(r=1\), the rank is \(13\) of \(18\); at \(r=4/3\) it is \(18\). For \(n=10\), the unit-weight outer-corner rank is \(27\) of \(30\), including two losses coming from golden-ratio longitudinal gaps.

## Relationship to prior work

Parlangeli and Notarstefano (2011) classify path and cycle controllability. Notarstefano and Parlangeli (arXiv version 2012; journal 2013) characterize unweighted grid Laplacian eigenstructures, visible modes, and controllability criteria. Those results provide the general PBH and path-mode framework; they do not state an arbitrary rational transverse-weight classification, the complete three-rail all-vertex rank formula, or the mod-five resonance law. Liu and coauthors (2024) give more general Cartesian-product controllability criteria but the publicly inspected abstract does not supply an all-rational three-rail rank classification. The new contribution is the concrete spectral-gap enumeration and the resulting exact rank phase diagram, not the general PBH test or path eigenvector formula.

## Limitations

The theorem assumes three rails, unit longitudinal weights, uniform transverse rung weights, rational \(r\ge1\), and one scalar vertex input. It does not address irrational weights, nonuniform rungs, internal state constraints, robustness, controllability Gramians, or control energy. A nonzero rank determinant may be arbitrarily ill-conditioned. Cross-document historical completeness and independent mathematical validation are not asserted.

## References

- G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556, initially submitted September 16, 2011. https://arxiv.org/abs/1109.3556
- G. Notarstefano and G. Parlangeli, *Controllability and observability of grid graphs via reduction and symmetries*, arXiv:1203.0129v1, initially submitted March 1, 2012; IEEE Transactions on Automatic Control 58 (2013), 1719–1731. https://arxiv.org/pdf/1203.0129
- B. Liu, M. Hu, J. Huang, Y. Chen, and H. Su, *Controllability of Multi-Agent Systems With Cartesian Product Networks*, IEEE Transactions on Circuits and Systems I 71 (2024), 838–850. https://doi.org/10.1109/TCSI.2023.3329423
