# The length-176 relative Fano scheme of lines on the characteristic-three Dwork quartic pencil

## Finding
Let \(k\) be an algebraically closed field of characteristic \(3\). On the Dwork quartic pencil
\[
S_\lambda:\quad X^4+Y^4+Z^4+W^4+\lambda XYZW=0\subset\mathbb P^3_k,
\qquad\lambda\in k,
\]
let \(\mathcal F\) denote the relative scheme of projective lines contained in the fibers, constructed as a closed subscheme of \(\operatorname{Gr}(2,4)_k\times\mathbb A^1_k\). Then, as a scheme over \(\mathbb A^1_k\),
\[
\mathcal F\simeq\coprod_{48}\operatorname{Spec}k[\lambda]/(\lambda)
\;\amalg\;\coprod_{64}\operatorname{Spec}k[\lambda]/(\lambda^2).
\]
The decomposition is noncanonical with respect to the ordering of components. In particular, \(\mathcal F\) has total length \(176\), is supported on \(\lambda=0\), and its central geometric fiber consists of exactly \(112\) reduced points. Exactly \(64\) central lines extend uniquely to first order in the pencil but not to second order; the other \(48\) lines are obstructed already at first order. Every \(S_\lambda\) with \(\lambda\ne0\) contains no projective line, even when \(S_\lambda\) is singular.

Additionally, \(S_\lambda\) is smooth precisely when \(\lambda^4\ne1\). If \(\lambda^4=1\), it has exactly \(16\) ordinary double points.

## Assumptions and scope
All statements are over an algebraically closed field \(k\) with \(\operatorname{char}k=3\). Parameters range over every element of \(k\), with no characteristic-zero lifting assumption. Scheme lengths refer to the *relative* line parameter scheme over the parameter line, not to its reduced central fiber. By “extending to first order” we mean a map from \(\operatorname{Spec}k[\lambda]/(\lambda^2)\) into the relative Fano scheme reducing to the indicated central line; extension to second order would require \(k[\lambda]/(\lambda^3)\).

## Proof
**1. Line equations and absence away from zero.** Every projective line admits a choice of two pivot coordinates; by permutation symmetry it suffices to work in the standard Grassmannian chart
\[
(X,Y,Z,W)=(s,t,as+ct,bs+dt).
\]
The five coefficients of the restriction of the quartic to this line, up to common invertible scalars on the mixed terms in characteristic \(3\), are exactly
\[
\begin{aligned}
A&=1+a^4+b^4,&B&=1+c^4+d^4,\\
C&=a^3c+b^3d+\lambda ab,&
D&=ac^3+bd^3+\lambda cd,\\
E&=\lambda(ad+bc).
\end{aligned}
\]
Indeed, the mixed binomial coefficients \(\binom43\) vanish modulo three, and the mixed coefficient \(\binom42=6\) vanishes as well. Suppose \(\lambda\ne0\) and these five vanish. None of \(a,b,c,d\) can be zero: for example, \(a=0\) forces \(b\ne0\) by \(A=0\), then \(d=0\) by \(C=0\), then \(c=0\) by \(E=0\), contradicting \(B=0\); the other three cases follow from the same equations or interchanging the two pivot variables. From \(E=0\), write \(c=\zeta a\), \(d=-\zeta b\) with \(\zeta\ne0\). Equations \(A=B=0\) give \(a^4+b^4=-1\) and \(\zeta^4=1\). Put \(\Delta=a^4-b^4\). Equations \(C=D=0\) become
\[
\zeta\Delta+\lambda ab=0,\qquad
\zeta^3\Delta-\lambda\zeta^2ab=0.
\]
Multiplying the first by \(\zeta^2\) and subtracting the second yields \(2\lambda\zeta^2ab=0\), a contradiction. Hence no line exists at a nonzero parameter. This argument is over the algebraic closure, not a finite-field enumeration.

**2. The 112 central lines.** At \(\lambda=0\), one obtains \(48\) coordinate-pair lines, arising from the three partitions of four coordinates into two pairs with fourth-root ratios satisfying \(\rho^4=\sigma^4=-1\). There are also \(64\) distinct lines
\[
L_{\alpha,\beta,\zeta}:\quad
(X,Y,Z,W)=(s,t,\alpha(s+\zeta t),\beta(s-\zeta t)),
\qquad \alpha^4=\beta^4=\zeta^4=1.
\]
Substitution into the Fermat equation proves containment because \((s+\zeta t)^4=s^4+\zeta s^3t+\zeta^3st^3+\zeta^4t^4\), and the two mixed terms cancel after multiplication by the fourth roots and the sign change. The two displayed sets are disjoint. A smooth quartic containing a line \(L\) has \(N_{L/S}\simeq\mathcal O_{\mathbb P^1}(-2)\), because \(L^2=-2\) by adjunction on a K3 surface. Therefore \(H^0(N_{L/S})=0\): its line Fano scheme is reduced at every central line. The known sharp bound of \(112\) for characteristic-three smooth quartics, attained by this Fermat surface [1], shows that these \(48+64\) lines exhaust the central fiber.

**3. Relative infinitesimal lengths.** At each of the \(112\) central lines, the Jacobian of \((A,B,C,D)\) with respect to the four chart variables \((a,b,c,d)\) is invertible. For a coordinate-pair line, choose the two pivot variables from different coordinate pairs, giving \((a,b,c,d)=(\rho,0,0,\sigma)\); the four equations have invertible linear parts. For an exceptional line, at \(\lambda=0\) the Jacobian rows are
\[
(a^3,b^3,0,0),\quad(0,0,c^3,d^3),\quad
(0,0,a^3,b^3),\quad(c^3,d^3,0,0).
\]
At \((a,b,c,d)=(\alpha,\beta,\alpha\zeta,-\beta\zeta)\), both relevant \(2\)-by-\(2\) determinants are nonzero (their summands differ by a sign, and \(2\ne0\)). The formal implicit-function theorem therefore determines unique formal functions \(a(\lambda),b(\lambda),c(\lambda),d(\lambda)\) satisfying \(A=B=C=D=0\). The completed local ring of the relative Fano scheme is controlled by the remaining equation \(E=\lambda h(\lambda)\), where \(h=ad+bc\).

On a coordinate-pair line \(h(0)=\rho\sigma\ne0\), so \(E\) generates \((\lambda)\). On an exceptional line \(h(0)=0\). Differentiate the four solved equations at zero; writing \(\kappa=\alpha\beta/\zeta\), one finds
\[
\frac{a'}a=-\kappa,\qquad
\frac{b'}b=\kappa,\qquad
\frac{c'}c=\kappa,\qquad
\frac{d'}d=-\kappa,
\]
all derivatives evaluated at zero. Consequently
\[
h'(0)=a'd+ad'+b'c+bc'=(\alpha\beta)^2\ne0.
\]
Thus \(h\) is a uniformizer and \(E\) generates \((\lambda^2)\). The local Artinian rings are respectively \(k[\lambda]/(\lambda)\) at the \(48\) coordinate-pair lines and \(k[\lambda]/(\lambda^2)\) at the \(64\) exceptional lines. The relative scheme is closed in the proper Grassmannian family, and it has finite support, hence is finite over the parameter line. A finite Artinian scheme over algebraically closed \(k\) is the disjoint union of its local factors, proving the asserted global decomposition and length \(48+2\cdot64=176\).

**4. Singular fibers.** The partial derivatives of the defining quartic are \(X^3+\lambda YZW\) and its permutations. At any common zero for \(\lambda\ne0\), all coordinates are nonzero, and multiplying each derivative by its corresponding coordinate yields \(X^4=Y^4=Z^4=W^4\). Normalizing \(X=1\) gives the \(16\) points with \((Y,Z,W)\in\mu_4^3\) and \(\lambda YZW=-1\), which exist exactly for \(\lambda^4=1\). These points lie on the quartic by Euler's homogeneous identity; in characteristic three the degree \(4\) is invertible. Their affine tangent-cone quadratic forms are \(\lambda(Wuv+Vuw+Uvw)\) (with \((U,V,W)=(Y,Z,W)\) at the point), whose determinants are nonzero because \(2\lambda^3UVW\ne0\). Thus all are ordinary nodes and no other singularities occur.

## Verification
The standalone `verify.py` constructs \(\mathbb F_9\), enumerates all Grassmannian reduced-row-echelon line charts, confirms the \(112\) central lines split as \(48+64\), verifies each exceptional line, computes the exact first derivatives via finite-field linear algebra, and checks \(h'(0)=(\alpha\beta)^2\ne0\) for every exceptional line. It additionally exhausts lines over \(\mathbb F_9\) for every nonzero parameter in that field. Running `python3 verify.py` returns `VERIFY_OK`. The algebraic derivation above, not finite enumeration, proves the assertions for arbitrary algebraically closed \(k\) of characteristic three.

## Relationship to prior work
Rams and Schütt [1] established the sharp \(112\)-line bound for smooth quartics in characteristic three and the Fermat surface realizing it. We use their central-fiber count, not as a new result. Bini and Garbagnati [2] studied the Dwork pencil and its quotients in characteristic zero. Eklund [3] investigated the line locus of the Heisenberg-invariant quartic family over characteristic zero. Veniani [4] developed the geometry of lines on characteristic-three quartic K3 surfaces. The claimed contribution here is specifically the finite scheme over the characteristic-three Dwork parameter line, the disappearance of *all* lines on nonzero fibers, and the \(48\)-simple/\(64\)-double infinitesimal structure. Related existing counts or generic line-locus descriptions do not immediately imply the asserted local Artin rings.

## Limitations
The statement concerns embedded lines in the indicated quartic model, not the line configurations on minimal resolutions of its nodal fibers. The central geometric line classification invokes the published \(112\)-line theorem [1], while the relative local multiplicities have independent formal calculations above. A result under a different parametrization or in specialized Dwork-family literature could duplicate the infinitesimal statement; a mathematical independence claim is not made. No independent scientific audit has been performed.

## References
[1] S. Rams and M. Schütt, *112 lines on smooth quartic surfaces (characteristic 3)*, arXiv:1409.7485 (first public 2014-09-26), https://arxiv.org/abs/1409.7485.

[2] G. Bini and A. Garbagnati, *Quotients of the Dwork Pencil*, arXiv:1207.7175 (first public 2012-07-31), https://arxiv.org/abs/1207.7175.

[3] D. Eklund, *Curves on Heisenberg invariant quartic surfaces*, 2018, https://arxiv.org/search/?query=Curves+on+Heisenberg+invariant+quartic+surfaces&searchtype=all.

[4] D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, arXiv:1608.04209 (first public 2016-08-15), https://arxiv.org/abs/1608.04209.
