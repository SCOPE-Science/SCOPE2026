# Complete three-cycle census and simultaneous sinks in a quadratic nilpotent-Jacobian family

## Finding
Consider the real polynomial dynamical system
\[
F_{a,\nu}(x,y,z)=\bigl(y^2-z^2,\ z,\ \nu+a(y^2-z^2)^2\bigr),\qquad a>0,\ \nu\in\mathbb R.
\]
It is a polynomial coordinate conjugate of a member of the three-dimensional pointwise-nilpotent-Jacobian family introduced by Castañeda and Rebollo-Perdomo [1]. Write \(N_3(a,\nu)\) for its number of *distinct primitive three-cycles*, identifying cyclic rotations, not identifying reversal. Then
\[
N_3(a,\nu)=
\begin{cases}
1,&\nu\ge0,\\
1,&\nu<0,\ 0<a(-\nu)^3<27/32,\\
2,&\nu<0,\ a(-\nu)^3=27/32,\\
3,&\nu<0,\ 27/32<a(-\nu)^3\le125/96,\\
5,&\nu<0,\ a(-\nu)^3>125/96.
\end{cases}
\]
Exactly one primitive three-cycle is attracting for \(\nu<0\) and \(27/32<a(-\nu)^3<125/96\). Moreover, the five-cycle regime includes an explicit rational parameter at which **two distinct, all-different-coordinate, primitive three-cycles are simultaneously hyperbolic attracting**; by continuity this coexistence persists on a nonempty open parameter set.

The complete census distinguishes the previously studied cycles with two equal scalar coordinates from two further cycles in opposite cyclic orientations that exist only beyond the sharp threshold \(125/96\). These latter cycles are not mere cyclic rotations of one another.

## Assumptions and scope
All orbits and parameters are real, \(a>0\), and the dynamical time is discrete. A primitive three-cycle has least positive period exactly three. The starting three-dimensional polynomial map above is a *conjugate normal form*: its own Jacobian is **not** asserted to be pointwise nilpotent. The source family, before nonlinear conjugacy, has a pointwise nilpotent Jacobian [1, Section 3]. This distinction is essential.

Iterating the last two components is equivalent to the second-order scalar recurrence
\[
w_{n+2}=\nu+a(w_n^2-w_{n+1}^2)^2.
\]
A scalar periodic triple \((A,B,C)\) corresponds to the three-dimensional state \((C^2-A^2,A,B)\). The inverse correspondence on periodic orbits is unique because the first coordinate of the image is forced by the preceding last two coordinates. Hence counting cyclic classes of scalar triples counts all three-dimensional primitive three-cycles without loss or duplication.

## Proof
**1. Exhaustion by equality pattern.** For a scalar three-periodic sequence, the three exact return equations are
\[
\begin{split}
 C&=\nu+a(A^2-B^2)^2,\\
 A&=\nu+a(B^2-C^2)^2,\\
 B&=\nu+a(C^2-A^2)^2.
\end{split}
\tag{1}
\]
If \(A=B=C\), the only solution is the fixed triple \((\nu,\nu,\nu)\), which is not primitive. If exactly two coordinates coincide, cyclically rotate to \((A,B,C)=(\nu,s,s)\), with \(s\ne\nu\). Substitution into (1) yields the necessary and sufficient condition
\[
a(s-\nu)(s+\nu)^2=1.
\tag{2}
\]
In particular \(s>\nu\), and distinct roots of (2) determine distinct primitive cycles. No other two-equal form is possible.

**2. Every all-distinct triple is algebraically forced.** Assume \(A,B,C\) are pairwise distinct and set
\[
S=A+B+C,\quad P=AB+BC+CA,\quad Q=A^2+B^2+C^2,\quad R=ABC.
\]
Subtracting successive equations in (1) and dividing by their nonzero coordinate differences gives
\[
(S-t)(Q-3t^2)=-\frac1a
\quad(t=A,B,C).
\tag{3}
\]
Thus \(A,B,C\) are the three roots of the monic cubic obtained by expanding (3). Comparing its coefficients with \(t^3-St^2+Pt-R\), and using \(Q=S^2-2P\), gives
\[
P=-S^2,\quad Q=3S^2,\quad R=-S^3-\frac1{3a}.
\tag{4}
\]
These identities imply
\[
\sum_{\mathrm{cyc}}(A^2-B^2)^2=-\frac{4S}{a}.
\]
Summing (1) then gives \(S-3\nu=-4S\), so \(S=3\nu/5\). Consequently \(A,B,C\) are exactly the roots of
\[
H_{a,\nu}(t)=t^3-\frac{3\nu}{5}t^2-\frac{9\nu^2}{25}t
+\frac{27\nu^3}{125}+\frac1{3a}.
\tag{5}
\]
Conversely, if (5) has three distinct real roots, its Viète relations imply (4) and \(S=3\nu/5\). The differences between the three residuals in (1) vanish by (3), while their sum vanishes by the displayed squared-difference identity and \(S-3\nu=-4S\). Therefore all three residuals vanish. This proves that **every** ordering of the roots is a genuine three-cycle. The six orderings form exactly two cyclic classes, one for each orientation.

The cubic discriminant is exactly
\[
\operatorname{Disc}_t(H_{a,\nu})=-\frac{3(96a\nu^3+125)}{125a^2}.
\tag{6}
\]
Because \(a>0\), there are three distinct real roots if and only if \(\nu<0\) and \(a(-\nu)^3>125/96\). Equality gives a repeated root and no all-distinct triple. Thus the contribution from (5) is exactly two cycles above that threshold and zero elsewhere.

**3. Complete count of two-equal cycles.** For \(\nu\ge0\), the left side of (2) is positive only for \(s>\nu\) and increases strictly from zero to infinity there, giving exactly one cycle. For \(\nu<0\), write \(r=-\nu>0\), \(u=s/r>-1\), and \(k=ar^3>0\). Then (2) is
\[
(u+1)(u-1)^2=\frac1k,
\qquad u>-1.
\tag{7}
\]
The function on the left increases from zero to its unique positive local maximum \(32/27\) at \(u=-1/3\), decreases to zero at \(u=1\), and increases thereafter. The numbers of distinct roots are accordingly \(1\) for \(k<27/32\), \(2\) for equality, and \(3\) for \(k>27/32\). Adding the two all-distinct cycles from Step 2 proves every case of the stated global census, including the double-root thresholds.

**4. Stability of the middle two-equal cycle.** For a state \((w_n,w_{n+1})\) the planar recurrence has Jacobian
\[
J(y,z)=\begin{pmatrix}0&1\\4ay(y^2-z^2)&-4az(y^2-z^2)\end{pmatrix}.
\]
On the cycle \((\nu,s,s)\), the three-step return has determinant zero and characteristic polynomial
\[
\lambda\left(\lambda-\frac{16s^2}{(s+\nu)^2}\right).
\tag{8}
\]
The third (three-dimensional) multiplier is also zero, because the first state coordinate is slaved to the other two. Hence this cycle is hyperbolic attracting exactly when \(|4s|<|s+\nu|\). For \(\nu=-r<0\), with \(s=ru\), this becomes \(-1/3<u<1/5\). The middle root of (7) lies in that interval exactly for \(27/32<k<125/96\): at the two respective endpoints the middle root is \(-1/3\) and \(1/5\). The other two-equal roots have a multiplier exceeding one. Thus exactly one two-equal cycle is a sink throughout the stated interval. For \(k\le125/96\), there are no all-distinct cycles by (6), establishing the asserted unique attracting three-cycle. The equality points have a unit return multiplier and are not claimed hyperbolic.

**5. Explicit simultaneous attracting cycles.** Take
\[
\nu=-1,\qquad a=\frac{6331625}{4572288},\qquad
(A,B,C)=\left(-\frac{183}{185},\frac{57}{185},\frac3{37}\right).
\tag{9}
\]
Straight exact fraction arithmetic verifies (1), and \(a>125/96\), so the two opposite orderings \((A,B,C)\) and \((A,C,B)\) are primitive cycles from the two distinct orientation classes. Their planar return matrices have, respectively, the exact traces and determinants
\[
\begin{array}{c|cc}
\text{orientation}&\operatorname{tr}&\det\\\hline
(A,B,C)&-67853/250047&-318725/1000188\\
(A,C,B)&183019/500094&318725/1000188
\end{array}
\]
(The full three-dimensional return has one additional zero multiplier.) For the first orientation, the real quadratic Schur inequalities \(1-\operatorname{tr}+\det>0\), \(1+\operatorname{tr}+\det>0\), \(1-\det>0\) have the respective exact values
\[
\frac{15125}{15876},\quad\frac{410051}{1000188},\quad\frac{1318913}{1000188}.
\]
For the reversed orientation they are, respectively,
\[
\frac{15125}{15876},\quad\frac{1684951}{1000188},\quad\frac{681463}{1000188}.
\]
All six numbers are strictly positive. Both primitive cycles are therefore hyperbolic sinks. Their distinct scalar coordinate sets have no fixed points or coincident elements. Strict eigenvalue inequalities and the simple-root condition (6) persist under small perturbations of \((a,\nu)\), so an open parameter neighborhood also has two simultaneously attracting period-three cycles.

## Verification
The accompanying standalone `CHECK.py` uses exact integer and rational arithmetic from the Python standard library. It verifies the identity of every transition at (9), the three cyclic return Jacobians and their trace/determinant values, all six strict Schur inequalities, the two critical two-equal cycles, and representative root-count boundaries with exact polynomial division and rational signs. Run `python3 CHECK.py` from the extracted artifact directory. These finite computations check the explicit witness and critical algebra but do not substitute for the universal exhaustion in Steps 1–3 or the analytic continuation argument in Step 5.

## Relationship to prior work
Castañeda and Rebollo-Perdomo [1] introduce the original pointwise-nilpotent-Jacobian polynomial family and its conjugate normal form, establish a fixed point and the absence of period two, and construct at least one three-cycle (including a return multiplier formula for a two-equal pattern). Their original theorem is about **existence**, not a global period-three count. The concluding open questions explicitly ask whether the exhibited three-cycle is unique and attracting [1, Section 5], making exact multiplicity and stability directly motivated. The new conclusions are the complete quadratic case distinction, two additional opposite-orientation three-cycles, the sharp five-cycle onset, and the explicit pair of coexisting sinks. The full lawful arXiv version was inspected; the subsequently published journal version was available in abstract/bibliographic form only, leaving possible revision differences as a priority risk.

Chamberland [2] develops earlier related dynamics of nilpotent-Jacobian maps with specific defining functions and existence/uniqueness results for other special cases; it does not supply (5)–(9). A related public result [3] addresses the different **period-four** degree threshold for this same encompassing family. Its affine-versus-quadratic four-cycle conclusion implies neither a quadratic period-three census nor coexistence of two period-three sinks.

## Limitations
This is a complete census of primitive period three **only**, for the stated quadratic subfamily with \(a>0\). It does not classify periods four and above, full basins, other defining polynomials, or the nonlinear stability at the two-equal neutral boundaries. Explicit hyperbolic stability is certified for the two distinct all-different cycles at the rational witness and on some surrounding open set, not claimed for the entire five-cycle regime. An unpublished or unindexed equivalent derivation remains a historical priority risk; independent audit and validation have not been performed.

## References
1. Á. Castañeda and S. Rebollo-Perdomo, *Discrete and continuous dynamics of real 3-dimensional nilpotent polynomial vector fields*, arXiv:2209.06986v1 (first publicly posted September 15, 2022), https://arxiv.org/abs/2209.06986 ; later *Archiv der Mathematik*, DOI:10.1007/s00013-024-02085-8.
2. M. Chamberland, *Dynamics of Maps with Nilpotent Jacobians*, *Journal of Difference Equations and Applications* **12** (2006), 49–56, DOI:10.1080/10236190500267970; lawful author-hosted text https://chamberland.math.grinnell.edu/papers/nilpotent.pdf.
3. *A sharp degree threshold for four-cycles in a three-dimensional nilpotent-Jacobian family*, public research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-a-sharp-degree-threshold-for-four-cycles-in-a-three-dimensional--7541997decfd/RESULT.md.
