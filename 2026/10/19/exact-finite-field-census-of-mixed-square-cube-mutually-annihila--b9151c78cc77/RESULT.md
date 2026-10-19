# Exact finite-field census of mixed square–cube mutually annihilating matrices

## Finding
For a prime power \(q\), integer \(n\geq 0\), and \(\mathbb F_q\), define
\[
T_n(q)=\#\{(A,B)\in M_n(\mathbb F_q)^2:A^2=0,\ B^3=0,\ AB=BA=0\}.
\]
Write \({a\brack b}_q\) for the Gaussian binomial coefficient, with its usual zero convention, and
\[g_j(q)=|\operatorname{GL}_j(\mathbb F_q)|=\prod_{i=0}^{j-1}(q^j-q^i),\qquad g_0(q)=1.\]
For \(r,v\geq0\), let
\[
H_{r,v}(q)=\sum_{h=0}^{\min(r,v)}{v\brack h}_q
\left(\prod_{i=0}^{h-1}(q^r-q^i)\right)q^{r(v-h)}.
\]
For nonnegative \(u,v,w\), set \(s=3u+2v+w\) and
\[
J_{u,v,w}(q)=\frac{g_s(q)}{q^{(u+v+w)^2+(u+v)^2+u^2}
\prod_{i=1}^{u}(1-q^{-i})\prod_{i=1}^{v}(1-q^{-i})\prod_{i=1}^{w}(1-q^{-i})}.
\]
All empty products are \(1\); despite its rational-looking expression, \(J_{u,v,w}(q)\) is an integer (a nilpotent similarity-class size). Then the **exact count, for every \(n\) and \(q\)**, is
\[
\boxed{T_n(q)=\sum_{r=0}^{\lfloor n/2\rfloor}
{n\brack r}_q{n-r\brack r}_q g_r(q)\,q^{r^2}
\sum_{\substack{u,v\geq0\\3u+2v\leq s}}
J_{u,v,s-3u-2v}(q)\,q^{2r(s-u-v)}H_{r,v}(q),\quad s=n-2r.}
\]
The formula includes the zero-dimensional case \(T_0(q)=1\). In dimensions two and three it simplifies to
\[
T_2(q)=q^3+q^2-q,\qquad
T_3(q)=q^7+2q^6-q^4-q^3.
\]
For instance \(T_3(2)=232\), \(T_3(3)=3537\), and \(T_4(2)=15856\).

## Assumptions and scope
All matrices are labeled, ordered, and counted as actual matrix pairs rather than similarity orbits; the two variables are not interchangeable because their nilpotency bounds differ. The field is any finite field of prime-power cardinality, with no restriction on characteristic. Matrix powers mean ordinary products. \(A^2=0\) allows \(A=0\), and \(B^3=0\) allows any Jordan blocks of sizes one, two, or three. The count does not classify simultaneous-conjugacy orbits or irreducible components.

The variety is the representation variety of the finite-dimensional Gelfand–Ponomarev algebra \(\mathbb F_q\langle x,y\rangle/(x^2,y^3,xy,yx)\) on \(\mathbb F_q^n\), which is the mixed-exponent case usually denoted \(V(n,2,3)\).

## Proof
**1. Fix the square-zero factor.** If \(\operatorname{rank}A=r\), then \(0\le r\le\lfloor n/2\rfloor\). Set \(s=n-2r\). Choose a decomposition \(\mathbb F_q^n=U\oplus W\oplus T\) with dimensions \((r,s,r)\), in which \(A\) maps \(T\) isomorphically to \(U\) and vanishes on \(U\oplus W\). The number of such labeled matrices \(A\), independent of their chosen normal-form bases, is
\[
{n\brack r}_q {n-r\brack r}_q g_r(q).
\]
Indeed, choose \(\operatorname{im}A=U\), then \(\ker A\supset U\) of dimension \(n-r\), then an isomorphism \(\mathbb F_q^n/\ker A\to U\).

**2. Parameterize the annihilator.** In the displayed \((U,W,T)\)-coordinates, the equations \(AB=BA=0\) are equivalent to
\[
B=\begin{pmatrix}0&X&Y\\0&Z&H\\0&0&0\end{pmatrix},
\quad X\in M_{r\times s}(\mathbb F_q),\ Z\in M_s(\mathbb F_q),\ H\in M_{s\times r}(\mathbb F_q),\ Y\in M_r(\mathbb F_q).
\]
The block \(Y\) is unconstrained by either annihilation or cube zero, contributing \(q^{r^2}\). Direct multiplication gives
\[
B^3=\begin{pmatrix}0&XZ^2&XZH\\0&Z^3&Z^2H\\0&0&0\end{pmatrix}.
\]
Consequently \(B^3=0\) if and only if \(Z^3=0\), \(XZ^2=0\), \(Z^2H=0\), and \(XZH=0\).

**3. Separate the size-two Jordan blocks.** A nilpotent \(Z\) with \(Z^3=0\) has Jordan type \((3^u,2^v,1^w)\) with \(3u+2v+w=s\). The constraints \(XZ^2=0\) and \(Z^2H=0\) remove one independent column parameter of \(X\) and one row parameter of \(H\) for every size-three Jordan block. Thus before imposing \(XZH=0\), there are \(q^{2r(s-u)}\) choices for \((X,H)\).

On a length-three Jordan chain, \(Z(\ker Z^2)\subseteq\operatorname{im} Z^2\), and \(X\) already annihilates \(\operatorname{im}Z^2\). Hence these chains contribute nothing to \(XZH\). Length-one chains contribute nothing because \(Z=0\). A length-two chain contributes precisely the product of the coefficient of \(X\) on its terminal vector with the coefficient of \(H\) on its initial vector. Collecting all \(v\) length-two chains makes the remaining equation exactly \(X_2 H_2=0\) for a pair \(X_2\in M_{r\times v}(\mathbb F_q)\), \(H_2\in M_{v\times r}(\mathbb F_q)\). Their \(2rv\) coefficients were included in the preceding free count. The other coefficients therefore give a factor \(q^{2r(s-u-v)}\).

To count the constrained pair \((X_2,H_2)\), first fix \(\operatorname{rank}H_2=h\). There are \({v\brack h}_q\prod_{i=0}^{h-1}(q^r-q^i)\) possible \(H_2\) (choose its image and a surjection onto it). Each has \(q^{r(v-h)}\) possible \(X_2\) vanishing on \(\operatorname{im}H_2\). Summing over \(h\) yields exactly \(H_{r,v}(q)\). Thus, for a fixed \(Z\) of the indicated type, the number of \(B\) is \(q^{r^2+2r(s-u-v)}H_{r,v}(q)\).

**4. Count the Jordan types and assemble.** The centralizer of a nilpotent of Jordan type \((3^u,2^v,1^w)\) has unit group of order
\[
q^{(u+v+w)^2+(u+v)^2+u^2}
\prod_{i=1}^{u}(1-q^{-i})\prod_{i=1}^{v}(1-q^{-i})\prod_{i=1}^{w}(1-q^{-i}).
\]
This follows by taking invertible elements in the endomorphism algebra of the \(\mathbb F_q[t]\)-module \((\mathbb F_q[t]/t^3)^u\oplus(\mathbb F_q[t]/t^2)^v\oplus(\mathbb F_q[t]/t)^w\): its semisimple quotient is \(M_u(\mathbb F_q)\times M_v(\mathbb F_q)\times M_w(\mathbb F_q)\), and the full endomorphism algebra has dimension \((u+v+w)^2+(u+v)^2+u^2\). Orbit-stabilizer gives \(J_{u,v,w}(q)\). Summing the fixed-\(A\) counts over types, and then multiplying by the number of matrices \(A\) of each rank, proves the boxed identity.

For \(n=2\), \(A=0\) contributes \(q^2\) nilpotent \(B\), while rank-one \(A\) contributes \((q^2-1)q\). For \(n=3\), \(A=0\) contributes \(q^6\) nilpotent \(B\), while rank-one \(A\) contributes \((q^2+q+1)(q^2-1)q^3\). These give the displayed simplified polynomials.

## Verification
The standalone file `check.py` independently constructs ambient \(n\times n\) matrices over the prime fields \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\), and directly enforces \(AB=BA=A^2=B^3=0\) on canonical representatives of each square-zero rank. It separately recomputes the Jordan-type formula with exact integer/Gaussian arithmetic and verifies every fixed-rank count, not only their sum. Run with `python3 check.py` (standard library only). Verified cases include \((n,q)=(4,2),(3,3),(2,5)\), and the zero-dimensional boundary; each comparison passed. The code checks finite samples only, while the proof establishes the identity for all prime powers and dimensions.

## Relationship to prior work
Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, studies exactly the varieties \(V(n,a,b)\) and classifies their irreducible components over an algebraically closed field. The present result addresses the different, arithmetic question of counting all finite-field points of \(V(n,2,3)\) and does not claim a new geometric component classification. Kinser–Lőrincz, *Representation varieties of algebras with nodes*, concerns geometric properties of representation varieties and includes the radical-square-zero setting; it supplies context but not this mixed square–cube point-count formula. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, computes generating functions with \(AB=BA=0\), including a nilpotent-pair variant, but its published formulas do not impose the asymmetric bounds \(A^2=B^3=0\) or exhibit this size-two-Jordan-block correction. Thus the new count is a refinement of a different question, not a restatement of those broader unrefined totals. Canonical-form work by Bondarenko–Gerasimova–Sergeichuk concerns classifications of mutually annihilating operators rather than this labeled finite-field count.

## Limitations
This is an exact cardinality, not a rank-by-rank joint Jordan-type census or a simultaneous similarity-class classification. The finite computational tests do not cover extension fields directly. Exact equivalence to an unindexed Hall-polynomial or quiver-representation point-count formula cannot be excluded; a targeted literature comparison has not established absolute novelty. The formula deliberately uses a finite sum and standard Gaussian/centralizer factors rather than claiming an unexpectedly simple closed polynomial for arbitrary dimension.

## References
1. R. Kinser and A. C. Lőrincz, *Representation varieties of algebras with nodes*, arXiv:1810.10997 (first posted 2018-10-25), Section 1 and main results. https://arxiv.org/abs/1810.10997
2. J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293; *Commentarii Mathematici Helvetici* 79 (2004), 396–426, especially Section 1 and component-classification theorems. https://arxiv.org/pdf/math/0211293
3. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566 (first posted 2021-10-29), especially Theorems 1.1–1.2 and Section 3. https://arxiv.org/abs/2110.15566
4. V. M. Bondarenko, T. G. Gerasimova, and V. V. Sergeichuk, *Pairs of mutually annihilating operators*, *Linear Algebra and its Applications* 430 (2009), 86–105, arXiv:0812.2155. https://arxiv.org/abs/0812.2155
