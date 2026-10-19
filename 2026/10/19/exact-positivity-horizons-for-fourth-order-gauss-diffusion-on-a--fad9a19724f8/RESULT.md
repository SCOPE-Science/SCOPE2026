# Exact positivity horizons for fourth-order Gauss diffusion on a star with one anomalous spoke

## Finding

Consider a symmetric diffusion network with one hub, \(k\ge2\) ordinary leaves of unit conductance, and one exceptional leaf of conductance \(x>0\). For the completed two-stage Gauss–Legendre method of order four, the **entire** entrywise-nonnegative timestep set is

\[
\{h\ge0:T(h)\ge0\}=\begin{cases}
[0,H_-(x)],&0<x<1/2,\\
[0,\infty),&1/2\le x\le (k+1)/k,\\
[0,H_+(k,x)],&x>(k+1)/k,
\end{cases}
\]

where

\[
H_-(x)=\frac{6x+\sqrt{36x^2+48x(1-2x)}}{2x(1-2x)},\qquad
H_+(k,x)=\frac{6+\sqrt{36+48(kx-k-1)}}{2(kx-k-1)}.
\]

Both finite endpoints are attained. At the lower-side horizon the first vanishing off-diagonal orbit connects the hub to each ordinary leaf; at the upper-side horizon it connects the hub to the exceptional leaf. The scheme is therefore unconditionally positivity-preserving **if and only if**
\[
\boxed{\frac12\le x\le1+\frac1k}. 
\]

There is a further sharp sign transition: if \(0<x<1/(k+4)\), then the ordinary-leaf-to-distinct-ordinary-leaf entries also become negative after a second, strictly larger, unique positive timestep. If \(x\ge1/(k+4)\), those entries remain strictly positive at every positive timestep. These assertions refer to the **completed update**, not to internal Runge–Kutta stages.

## Assumptions and scope

The vertex set is \(\{c,o_1,\ldots,o_k,e\}\), with \(k\) an integer at least two. The only undirected edges are \(co_i\) with conductance one and \(ce\) with conductance \(x>0\). Let \(L\) be the \((k+2)\)-by-\((k+2)\) real symmetric graph Laplacian, with positive weighted degrees on the diagonal and negative conductances off-diagonal. The heat evolution is \(\dot u=-Lu\). For every real \(h\ge0\), define

\[
T(h)=(12I-6hL+h^2L^2)(12I+6hL+h^2L^2)^{-1}.
\]

The claim concerns entrywise nonnegativity on **all** nonnegative initial vectors, exactly equivalent to \(T(h)_{ij}\ge0\) for every ordered pair of vertices. Time is normalized so that ordinary spoke conductance equals one. The weighted star is connected for every permitted \(x\); the method is well-defined for every \(h\ge0\) because the denominator is positive definite.

## Proof

**Step 1: invariant subspaces and denominator.** Write \(a=k+1+2x\) and \(b=(k+2)x\). On the three-dimensional subspace where every ordinary leaf has the same coordinate, the Laplacian acts on the coordinates (hub, common ordinary-leaf value, exceptional leaf) through

\[
M=\begin{pmatrix}k+x&-k&-x\\-1&1&0\\-x&0&x\end{pmatrix}.
\]

The orthogonal complement consists of ordinary-leaf coordinate vectors whose entries sum to zero; there \(L\) acts as the scalar \(1\). The eigenvalues of \(M\) are \(0,\lambda_+,\lambda_-\), where \(\lambda_\pm>0\) solve \(\lambda^2-a\lambda+b=0\). (Positive nonzero eigenvalues also follow directly from connectedness of the weighted star.) Define

\[
\begin{split}
\Delta(h)&=\prod_{\sigma\in\{+,-\}}(12+6h\lambda_\sigma+h^2\lambda_\sigma^2)\\
&=144+72ah+12(a^2+b)h^2+6ab h^3+b^2h^4>0.
\end{split}
\]

The scalar method response \(f(z)=(12-6z+z^2)/(12+6z+z^2)\) is strictly positive for \(z\ge0\), since its numerator is \((z-3)^2+3\). Consequently \(T(h)\) is symmetric positive definite for every \(h\ge0\), so all diagonal entries are strictly positive. Moreover \(L\mathbf1=0\) implies \(T(h)\mathbf1=\mathbf1\). Only the four off-diagonal orbit types need sign analysis.

**Step 2: all four off-diagonal types.** Define the polynomials

\[
\begin{aligned}
p(h)&=12+6xh+x(2x-1)h^2,\\
r(h)&=12+6h+(k+1-kx)h^2,\\
q(h)&=72+(12k+48x+24)h+(6kx+12x^2+12x)h^2\\
&\hspace{18mm}+x((k+4)x-1)h^3.
\end{aligned}
\]

Direct inversion of \(12I+6hM+h^2M^2\) on the three-dimensional invariant subspace, followed by adding back the ordinary-leaf zero-sum eigenspace, gives, for distinct ordinary leaves \(o_i,o_j\),

\[
\begin{aligned}
T_{c,o_i}(h)&=\frac{12h\,p(h)}{\Delta(h)},\\
T_{c,e}(h)&=\frac{12hx\,r(h)}{\Delta(h)},\\
T_{o_i,e}(h)&=\frac{12h^2x(6+ah)}{\Delta(h)},\\
T_{o_i,o_j}(h)&=\frac{12h^2 q(h)}{(h^2+6h+12)\Delta(h)}.
\end{aligned}
\]

For reproducibility, the quotient inverse is
\[
(12I-6hM+h^2M^2)(12I+6hM+h^2M^2)^{-1},
\]

and the ordinary-leaf-to-distinct-ordinary-leaf entry equals \((T^{\rm quotient}_{22}-f(h))/k\), where indices in the quotient are numbered starting at one. The standalone exact-arithmetic program `verify.py` checks all four formulas as symbolic identities in \(k,x,h\), in addition to direct matrix inversions. The expressions above establish the signs independent of any experiments.

**Step 3: unconditional interval.** Every denominator displayed is strictly positive for \(h>0\), and the ordinary-to-exceptional numerator is strictly positive. If \(1/2\le x\le(k+1)/k\), every coefficient of \(p\) and \(r\) is nonnegative and their constant coefficients are positive. Because \(k\ge2\), in this same range \((k+4)x-1>0\); every coefficient of \(q\) is positive. Hence every off-diagonal entry is positive for finite \(h>0\) in the stated closed conductance interval.

If \(x<1/2\), the leading coefficient of \(p\) is negative, so \(p\) has exactly one positive zero \(H_-\); solving its quadratic yields the formula stated above. For larger \(h\), the hub-to-ordinary entries are negative. If \(x>(k+1)/k\), similarly \(r\) has the unique positive zero \(H_+\), and the hub-to-exceptional entries are negative for larger \(h\). These exclusions prove necessity of the conductance interval.

**Step 4: no earlier sign loss.** On the upper side \(x>(k+1)/k\), the polynomials \(p\) and \(q\) have positive coefficients and only \(r\) changes sign. On the lower side \(0<x<1/2\), the polynomial \(r\) is positive. If \(x\ge1/(k+4)\), every coefficient of \(q\) is nonnegative and its constant coefficient is positive. It remains to treat \(0<x<1/(k+4)\). Here \(q\) has exactly one positive zero by its sign pattern (negative cubic coefficient, all lower coefficients positive). Polynomial division of \(q\) by \(p\), evaluated at \(p(H_-)=0\), yields the *exact identity*

\[
q(H_-)=\frac{12(1-x)}{(1-2x)^2}
\big[(k(1+x)+1+6x-4x^2)H_-+6k+12\big]>0.
\]

Therefore the unique positive zero of \(q\) lies strictly above \(H_-\). It follows that all four off-diagonal orbits are nonnegative for the entire claimed \([0,H_-]\), and not merely up to an unchecked smaller cutoff. The same sign-pattern argument establishes the asserted second ordinary-to-ordinary sign transition precisely for \(0<x<1/(k+4)\). This completes the proof.

## Verification

The included standalone program `verify.py` uses exact SymPy algebra to verify the quotient determinant, the four orbit formulas, and the polynomial remainder identity, all with symbolic parameters. It then checks direct \((k+2)\)-dimensional rational-matrix inversions for \(k=2,3,4,5,6\), six rational conductance values and three rational timesteps, including every row sum, diagonal sign and off-diagonal orbit equality. Run `python verify.py` after installing `requirements.txt`. In its tested environment the output was `VERIFY_OK 2886 exact symbolic, quotient, direct-matrix and orbit identities`.

The finite rational samples are **not** an exhaustive proof over arbitrary dimension, conductance or time. The parameter-uniform conclusions follow instead from the displayed algebraic identities, positive denominators, polynomial sign arguments and exact remainder identity.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten (2010) study diagonal Padé discretizations of positive systems and prove general sufficient step conditions; their result does not give necessary-and-sufficient all-time positivity criteria for conservative weighted star Laplacians. Their later paper (2012) develops related sufficient conditions and counterexamples and does not identify the present one-parameter sharp window or the second orbit-sign transition. The 2013 chapter on positive-system discretization addresses related general issues, but the available chapter description did not permit a full-text comparison.

For a unit-conductance star \(x=1\), positivity is consistent with previously known unweighted complete-multipartite results; this special case is **not** claimed as new. The three-vertex star is already covered by general three-vertex weighted Laplacian classifications; the present theorem starts at \(k=2\), where a nontrivial ordinary-leaf zero-sum eigenspace exists. Results for three-eigenvalue Laplacians do not cover the generic one-defect star, which has four distinct Laplacian eigenvalues for \(x\ne1\). A broad historical search did not identify a theorem implying the whole arbitrary-size and arbitrary-defect classification; absence from a search is not proof of historical novelty.

## Limitations

Only one spoke may have a different conductance, all other spokes being normalized to one. The result does not establish a positivity criterion for arbitrary heterogeneous stars, for other Runge–Kutta methods, or for positivity of internal stages. It concerns exact arithmetic and completed linear diffusion steps, not roundoff guarantees. The 2013 related book chapter was not available in full text; an equivalent specialized result elsewhere remains a bibliographic risk. No independent mathematical audit is asserted.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, MTNS 2010, repository deposit dated 15 October 2010. Public full text: https://mural.maynoothuniversity.ie/id/eprint/2195/1/SK-pade_MTNS10_long.pdf ; repository metadata: https://mural.maynoothuniversity.ie/id/eprint/2195/ .
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, Linear Algebra and its Applications 436 (2012), 3425–3442. Author-hosted full text: https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf ; repository metadata: https://mural.maynoothuniversity.ie/id/eprint/3761/ .
3. P. Colaneri, M. Farina, S. Kirkland, R. Scattolini, R. Shorten, *Positive Systems: Discretization with Positivity and Constraints*, in *Hybrid Systems with Constraints*, Wiley, 2013, chapter 1, DOI:10.1002/9781118639856.ch1. The chapter's accessible abstract and table of contents were inspected; its full text was unavailable.
