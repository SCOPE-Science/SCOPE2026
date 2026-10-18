# Golden-ratio rank-one numerical index and nilpotent rigidity of the regular decagonal plane

## Finding
Let \(X_{10}\) be the real two-dimensional Banach space whose unit ball is the regular Euclidean decagon with vertices
\[
v_j=(\cos(j\pi/5),\sin(j\pi/5)),\qquad j=0,\ldots,9.
\]
For a bounded real linear operator \(T\), let \(v_X(T)\) denote its Banach-space numerical radius, and set
\[
n_1(X_{10})=\inf\{v_X(T):\operatorname{rank}T=1,\ \|T\|=1\}.
\]
Then, with \(r=(\sqrt5-1)/2\),
\[
\boxed{n_1(X_{10})=r.}
\]
More precisely, let \(q_j\) be the unique norm-one linear functional supporting the edge from \(v_j\) to \(v_{j+1}\), with all indices understood modulo ten. **Every norm-one rank-one operator attaining the index** is exactly one of
\[
\boxed{T=\pm T_i,\qquad T_i z=q_{i+2}(z)v_i,\qquad 0\le i\le4.}
\]
All these extremizers are square-zero: \(T_i^2=0\). The ordinary numerical index, already determined in the literature, is \(n(X_{10})=\sin(\pi/10)=r/2\). Thus \(n_1(X_{10})=2n(X_{10})\), a strict rank-one/full index separation.

## Assumptions and scope
The scalar field is \(\mathbb R\). The plane is exactly the Minkowski space with the convex, centrally symmetric regular decagon specified above; no assertion is made for irregular polygons, complexifications, higher dimensions, or arbitrary even regular polygons. For a norm-one vector \(x\), a *norming functional* is \(f\in X^*\) satisfying \(\|f\|_*=1\) and \(f(x)=1\). The numerical radius is
\[
v_X(T)=\sup\{|f(Tx)|:\|x\|=\|f\|_*=1,\ f(x)=1\}.
\]
Write the edge-supporting functionals in Euclidean coordinates as
\[
q_j(z)=\frac{\cos((j+1/2)\pi/5)z_1+\sin((j+1/2)\pi/5)z_2}{\cos(\pi/10)}.
\]
Consequently \(q_j(v_j)=q_j(v_{j+1})=1\), the ten \(q_j\) are the extreme points of the dual unit ball, and \(q_{j+5}=-q_j\).

## Proof
**1. An exact finite numerical-radius formula.** Every rank-one norm-one operator has a factorization \(Tz=\ell(z)u\), where \(\|u\|=\|\ell\|_*=1\). Since the unit sphere is polygonal, maximizing the absolute numerical pairing on each face reduces to its vertices and the extreme norming functionals at those vertices. Therefore
\[
v_X(u\otimes\ell)=\max_{0\le k\le9}|\ell(v_k)|\max\bigl\{|q_{k-1}(u)|,|q_k(u)|\bigr\}.\tag{1}
\]
The second maximum uses the two edge supports meeting at \(v_k\). The same reduction follows directly by convexity along each primal edge and dual norming segment.

**2. Golden-ratio incidence data.** Put \(r=(\sqrt5-1)/2\). Then \(r^2=1-r\), and the cyclic row of values \(q_0(v_k)\), for \(k=0,\ldots,9\), is exactly
\[
(1,1,r,0,-r,-1,-1,-r,0,r).\tag{2}
\]
This follows by substitution in the cosine formula above. Rotational symmetry gives \(q_j(v_k)=q_0(v_{k-j})\).

A dihedral symmetry of the decagon puts the unit vector \(u\) into the form
\[
u=(1-s)v_0+sv_1,\qquad 0\le s\le\tfrac12.
\]
Changing the sign of \(\ell\), if needed, puts it on one of the five dual edges
\[
\ell=(1-t)q_j+tq_{j+1},\qquad 0\le t\le1,\quad j\in\{0,1,2,3,4\}.
\]
Define \(B_k(s)=\max\{|q_{k-1}(u)|,|q_k(u)|\}\). The incidence row (2) gives, throughout this reduced sector,
\[
B_1=1,\qquad B_2=r+r^2s,\qquad B_4=1-r^2s,\qquad B_5=1.\tag{3}
\]

**3. A universal lower bound.** In each dual-edge case \(j\), the functional \(\ell\) takes value one at the common primal vertex \(v_{j+1}\).

For \(j=0\), (1) and (3) imply \(v_X(T)\ge B_1=1\). For \(j=1\), they imply \(v_X(T)\ge B_2=r+r^2s\ge r\). For \(j=3\), they imply
\[
v_X(T)\ge B_4=1-r^2s\ge1-r^2/2>r.
\]
For \(j=4\), they imply \(v_X(T)\ge B_5=1\).

The remaining case \(j=2\) contains the genuine optimization. Formula (2) gives
\[
\ell(v_2)=1-r^2t,\qquad \ell(v_4)=r+r^2t.
\]
Using just the two vertices \(v_2\) and \(v_4\) in (1),
\[
v_X(T)\ge\max\{(1-r^2t)(r+r^2s),\ (r+r^2t)(1-r^2s)\}.\tag{4}
\]
For fixed \(s\), the first displayed factor decreases in \(t\), and the second increases in \(t\). The expressions coincide at \(t=s\). Therefore their maximum, for \(0\le t\le1\), is bounded below by their common value at \(t=s\), namely
\[
(1-r^2s)(r+r^2s)=r+r^4s(1-s)\ge r.\tag{5}
\]
This proves \(n_1(X_{10})\ge r\) with no finite-search assumption.

**4. Sharpness and every equality case.** Take \(u=v_0\) and \(\ell=q_2\). Using (2), the ten terms in (1) are \(0,r,r,r,r,0,r,r,r,r\), so \(v_X(u\otimes\ell)=r\). Both factors have norm one, proving equality.

The cases \(j=0,3,4\) are strictly above \(r\). In case \(j=1\), equality first forces \(s=0\). The term at \(v_1\) then equals \(1-r^2t\), so equality also forces \(t=1\), hence \(\ell=q_2\). In case \(j=2\), (5) is strictly above \(r\) whenever \(s>0\). With \(s=0\), the second term of (4) is \(r+r^2t\), so equality forces \(t=0\), again \(\ell=q_2\). Reversing the earlier symmetries and allowing the overall operator sign yields precisely \(\{\pm T_i:0\le i\le4\}\).

Finally \(q_{i+2}(v_i)=0\) by (2), and hence \(T_i^2=0\). Martín and Merí's independently established formula for the ordinary index of a regular \(2m\)-gon gives \(n(X_{10})=\sin(\pi/10)=r/2\), proving the stated factor-two separation.

## Verification
Run `python checker.py` with SymPy installed. It reconstructs every primal/dual vertex incidence using exact trigonometric simplification, checks the symbolic golden-ratio identities and both competing branches of (4)–(5), and stress-tests (1) on finite samples. The run reported `PASS 895 checks`. Those finite samples are consistency checks only; the proof of the quantified inequality is (1)–(5), and equality rigidity follows from the strict inequalities described above.

## Relationship to prior work
Martín and Merí determined the **ordinary numerical index** of every real regular even-gonal normed plane; their Theorem 5 gives \(\sin(\pi/10)\) in the decagonal case. Chica, Martín and Merí introduced and studied the **rank-one numerical index**. Chica and Merí subsequently computed rank-one numerical indices for certain hexagonal and octagonal norm families. The latter cases do not contain the regular decagon. The result here determines the decagonal rank-one index and its complete extremizer set, not merely its already-known unrestricted numerical index.

## Limitations
This result concerns the regular decagonal real plane and its rank-one operators only. It does not determine rank-one indices of arbitrary regular polygons, nor classify all unrestricted operators attaining the ordinary numerical index. The literature comparison is restricted to the named primary sources; a relevant 2016 dissertation could not be inspected in full, and an equivalent historical formulation under other terminology cannot be excluded.

## References
1. M. Martín and J. Merí, *Numerical index of some polyhedral norms on the plane*, Linear and Multilinear Algebra 55 (2007), 175–190, Theorem 5. DOI: 10.1080/03081080600628323. Author manuscript: https://www.ugr.es/~mmartins/Curriculum/Papers/2007-Polygons.pdf.
2. M. Chica, M. Martín and J. Merí, *Numerical radius of rank-1 operators on Banach spaces*, Quarterly Journal of Mathematics 65 (2014), 89–100. DOI: 10.1093/qmath/has050. Author manuscript: https://www.ugr.es/~mmartins/Curriculum/Papers/pre-ChicaMartinMeri.pdf.
3. M. Chica and J. Merí, *Rank-1 numerical index of some families of norms on the plane*, Linear and Multilinear Algebra 63 (2015), 1817–1828, Theorems 1–2 and Corollary 3. DOI: 10.1080/03081087.2014.975670. Author manuscript: https://www.ugr.es/~jmeri/archivos/curriculum/pre-ChicaMeri-Rank1NumericalIndex.pdf.
