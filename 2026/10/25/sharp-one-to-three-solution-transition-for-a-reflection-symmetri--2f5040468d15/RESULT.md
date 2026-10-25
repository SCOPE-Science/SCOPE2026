# Sharp one-to-three solution transition for a reflection-symmetric pentagonal cone-volume fiber

## Finding
Fix the five cyclic outward unit normals \(u_j=(\cos(2\pi j/5),\sin(2\pi j/5))\) for \(j=0,1,2,3,4\). Let \(S_t\) be the set of all positive support vectors of genuine pentagons \(P(h)=\{z\in\mathbb R^2:u_j\cdot z\le h_j\}\) with cone-volume vector \((t,t,1,1,t)\), where \(t>0\). The complete number of solutions is
\[
|S_t|=\begin{cases}1,&0<t\le t_*,\\3,&t>t_*;\end{cases}
\qquad t_*=3.085259816987\ldots.
\]
Exactly one solution is invariant under the reflection \(j\mapsto5-j\) for each parameter. The two additional solutions, when present, are a unique reflected pair. All three branches have explicit radical-and-cubic parametrizations below. In particular, the three solutions at \(t=4\) observed in the source literature belong to a sharp, fully classified symmetry-breaking transition, rather than an isolated example.

## Assumptions and scope
Define \(v=\sqrt5\), \(q=\cos(2\pi/5)=(v-1)/4\), and \(s=\sin(2\pi/5)>0\). Indices on support vectors are cyclic modulo five. The cone volume at normal \(u_j\) is exactly
\[
\gamma_j(h)=\frac{h_j(h_{j-1}+h_{j+1}-2q h_j)}{2s}.
\]
All five cone volumes are required strictly positive. No symmetry of the unknown polygon is imposed. Supports are measured from the fixed origin and are *not* identified under translations or scaling. The prescribed tuple is normalized exactly as above.

Set
\[
\begin{aligned}
J(B)&=B^3-\frac{1+19v}{11}B^2+\frac{42+6v}{11}B-\frac{12+8v}{11},\\
J_0(B)&=B^3-\frac{1+3v}{2}B^2+\frac{3+3v}{2}B+\frac{v-7}{2}.
\end{aligned}
\]
Each cubic has exactly one real root, denoted \(\beta_*\) for \(J\) and \(\beta_0\) for \(J_0\):
\[
2<\beta_0<\frac{21}{10}<\frac94<\beta_*<\frac{23}{10}.
\]
Define, for \(\beta_0<B<\beta_*\),
\[
\begin{aligned}
A(B)&=\frac{(v-1)(B^2+(1-v)B+1)}{B-v+1},\\
Z(B)&=\frac{(13-5v)J(B)}{(1-v)(B-v+1)},\\
H(B)&=\frac{4(3-v)(B+(3-v)/2)J_0(B)}{(v-1)(B-v+1)^3},\\
T(B)&=\frac{2A(B)(B-qA(B))}{H(B)}.
\end{aligned}
\]
All square roots and quotients below are positive or well-defined on this interval. The sharp transition is \(t_*=T(\beta_*)\); this is an exact algebraic specification of the constant.

## Proof
**1. Every solution lies in the positive pentagonal support cone.** For any positive vector \(h\), the intersections of successive supporting lines form a cyclic vertex chain. Its oriented edge at normal \(u_j\) has length \(\ell_j=(h_{j-1}+h_{j+1}-2q h_j)/s\). The positivity of all five cone volumes, with \(h_j>0\), forces \(\ell_j>0\). The chain then has five positive-length edges, equal strictly positive exterior turns \(2\pi/5\), and total turn \(2\pi\); consequently it is the boundary of a strictly convex pentagon with exactly the designated outward normals. Thus the quadratic cone-volume equations are both necessary and sufficient on the positive support orthant.

**2. Reflection coordinates and exact elimination.** Every support vector is uniquely written
\[
h=(a,b+x,d+y,d-y,b-x),\qquad a>0,\ b>0,\ d>0.
\]
Write \(F_j=2s\gamma_j\). The required reflection invariance of the *data*, not of \(h\), gives two linear antisymmetry equations:
\[
(a+d-4qb)x+by=0,\qquad dx+(b-4qd)y=0.
\]
The other three independent equations are
\[
\begin{aligned}
2a(b-qa)&=b(a+d-2qb)-2qx^2+xy,\\
2a(b-qa)&=2s t,\\
d(b+(1-2q)d)-(1+2q)y^2+xy&=2s.
\end{aligned}
\]
These identities follow by direct expansion of the displayed cone-volume formula.

**3. Unique symmetric branch.** If \(x=y=0\), let \(r=a/b>0\). The first symmetric equation implies
\[
\frac bd=\frac1{g(r)},\qquad g(r)=r+2q(1-r^2).
\]
Positivity holds precisely for \(0<r<r_{\max}\), where \(r_{\max}=(1+\sqrt{1+16q^2})/(4q)\). The last cone-volume equation fixes \(d>0\) uniquely, and the remaining normalized datum is
\[
t(r)=\frac{2r(1-qr)}{g(r)[1+(1-2q)g(r)]}.
\]
The numerator of \(t'(r)\), after multiplication by the positive squared denominator, factors exactly as
\[
(-176+80\sqrt5)(r-1-\sqrt5)^2\bigl(r^3+(1+\sqrt5)/4\bigr)>0
\]
for \(0<r<r_{\max}<1+\sqrt5\). As \(r\downarrow0\), \(t(r)\to0\), and as \(r\uparrow r_{\max}\), \(t(r)\to\infty\). Hence there is exactly one symmetric solution for each \(t>0\).

**4. Complete nonsymmetric parametrization.** If \((x,y)\ne(0,0)\), the determinant of the two antisymmetry equations vanishes. Setting \(A=a/d\) and \(B=b/d\), this condition is equivalent to \(A=A(B)\) and \(y/x=-1/(B-v+1)\). Since \(B^2+(1-v)B+1>0\), positivity of \(A\) forces \(B>v-1\). Set \(Z=(x/d)^2\). The first averaged equation gives exactly \(Z=Z(B)\), and the last gives \(d^2=2s/H(B)\). Then \(t=T(B)\).

The cubic discriminants are
\[
\operatorname{disc}(J)=-\frac{9232+2752\sqrt5}{1331}<0,
\qquad\operatorname{disc}(J_0)=\frac{343-157\sqrt5}{2}<0.
\]
Their unique real roots have the strict locations displayed above (checked by exact signs at the indicated rational endpoints). Since \(B>v-1\), the three essential positivity conditions factor as
\[
\begin{aligned}
Z>0 &\iff B<\beta_*,\\
H>0 &\iff B>\beta_0,\\
B^2-Z&=\frac{4(3-v)}{v-1}\frac{(B-(v+1)/2)(B^2+(1-v)B+1)}{B-v+1},\\
1-\frac{Z}{(B-v+1)^2}&=\frac{4(3-v)}{v-1}\frac{J_0(B)}{(B-v+1)^3}.
\end{aligned}
\]
Thus \(a,b+x,b-x,d+y,d-y\) are all positive exactly when \(\beta_0<B<\beta_*\). Furthermore
\[
B-qA(B)=\frac{v-1}{2}\frac{(B-(v+1)/2)(B+(3-v)/2)}{B-v+1}>0
\]
in this interval, so the prescribed \(t\) is positive. The complete nonsymmetric solutions are
\[
\begin{aligned}
d&=\sqrt{2s/H(B)},&a&=A(B)d,&b&=Bd,\\
x&=\varepsilon d\sqrt{Z(B)},&y&=-x/(B-v+1),&\varepsilon&\in\{-1,+1\},\\
h&=(a,b+x,d+y,d-y,b-x).&&&
\end{aligned}
\]
The two signs are distinct and exchanged by the reflection.

**5. Exact sharp transition and monotonicity.** Differentiating the rational-algebraic function \(T(B)\) gives
\[
T'(B)=\frac{(v-1)^2(1-v)}{4(v-3)}\frac{P_6(B)}{J_0(B)^2},
\]
where
\[
\begin{aligned}
P_6(B)={}&B^6-(1+3v)B^5+\tfrac{23+11v}{2}B^4+(-52+6v)B^3\\
&+(-64+44v)B^2+(-85+31v)B+\tfrac{21v-41}{2}.
\end{aligned}
\]
The prefactor is positive. To certify \(P_6<0\) throughout \([2,23/10]\), express it in the degree-six Bernstein basis on that interval. Its seven exact coefficients are, in order,
\[
\begin{gathered}
(-1293+577v)/2,\quad(-2683+1197v)/4,\quad(-86830+38729v)/125,\\
(-1435908+640303v)/2000,\quad(-74044279+33010077v)/100000,\\
(-152363899+67911527v)/200000,\quad(-781754391+348384260v)/1000000.
\end{gathered}
\]
All seven are strictly negative, by elementary rational squaring (for example \(223606797/10^8<v<223606799/10^8\) gives strict bounds). Since Bernstein basis functions are nonnegative and sum to one, \(P_6(B)<0\) on the whole interval. The admissible interval \((\beta_0,\beta_*)\) lies within it, so \(T\) is strictly decreasing. At the left endpoint \(H\downarrow0\), hence \(T(B)\to\infty\); at the right endpoint \(Z\downarrow0\), \(T(B)\to t_*>0\). It follows that no nonsymmetric solution exists for \(t\le t_*\), while exactly one \(B\), and hence precisely two reflected nonsymmetric supports, exist for each \(t>t_*\). Together with the unique symmetric branch this proves the theorem.

## Verification
The accompanying standalone symbolic checker `checks/pentagon_phase_checker.py` reproduces the critical identities for \(A,Z,H,T\), cubic discriminant signs, the derivative polynomial, all Bernstein coefficients, and direct substitution of both nonsymmetric solutions into the five original cone-volume equations for three rational parameter choices. Run using `python checks/pentagon_phase_checker.py` with SymPy installed. Its recorded result was `CONE_VOLUME_PENTAGON_OK` with \(\beta_0=2.057628370579981\), \(\beta_*=2.251826342639673\), and \(t_*=3.0852598169870777\). Symbolic algebra verifies identities; floating-point checks only corroborate substitutions and numerical values. The Bernstein sign certificate and proof are self-contained above.

## Relationship to prior work
Baumbach, Chen, and Henk, *On the Solution Sets of the Cone-Volume Map*, arXiv:2610.21533 (first publicly submitted 2026-10-15), Example 3.2, prove a three-solution instance for the very same five equally spaced normals at \((4,4,1,1,4)\). Their general theory concerns finite fibers, parity, and nonuniqueness. The instance \(t=4\) and its three solutions are prior work; the exact one-parameter sharp transition, complete classification at every positive \(t\), cubic roots, and monotonicity certificate are the findings here. The older planar discrete problem literature includes Stancu (2002, 2003), Chen–Li–Zhu (2019), and Liu–Lu–Sun–Xiong (2024); the last gives a four-normal classification rather than this five-normal parameter family.

## Limitations
This theorem fixes the normals to a regular pentagonal fan and restricts the cone-volume tuple to one specified reflection-invariant line. It neither classifies all five-normal fibers nor proves global novelty relative to every unindexed historical result. The primary source determines the cone-volume equations and already supplies a particular three-solution data point. The claimed additional theorem depends on its explicit algebraic reductions, unique root locations and exact sign certificates; finite numerical tests alone do not establish the classification.

## References
1. T. Baumbach, Z. Chen, M. Henk, *On the Solution Sets of the Cone-Volume Map*, arXiv:2610.21533v1, submitted 2026-10-15, https://arxiv.org/abs/2610.21533 .
2. A. Stancu, *The discrete planar \(L_0\)-Minkowski problem*, Advances in Mathematics 167 (2002), 160–174.
3. A. Stancu, *On the number of solutions to the discrete two-dimensional \(L_0\)-Minkowski problem*, Advances in Mathematics 180 (2003), 290–323.
4. Y. Liu, X. Lu, Q. Sun, G. Xiong, *The logarithmic Minkowski problem in \(\mathbb R^2\)*, Pure and Applied Mathematics Quarterly 20 (2024), 869–902.
