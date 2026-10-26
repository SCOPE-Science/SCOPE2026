# Exact Ritt resolvent constants and angular bifurcation for Jordan contractions

## Finding

For \(0\le q<1\), put
\[
J=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
T_q=qI+(1-q)J,\qquad
K(T_q)=\sup_{|z|>1}|z-1|\,\|(zI-T_q)^{-1}\|_{2\to2}.
\]
These matrices are contractions and Ritt operators. Set
\[
q_*=\frac{7-2\sqrt6}{5}=\frac{\sqrt6-1}{\sqrt6+1}.
\]
The exact best Ritt resolvent constant is
\[
\boxed{K(T_q)=\begin{cases}
\dfrac{\sqrt{5+6q+5q^2}+1-q}{(1+q)^2},&0\le q\le q_*,\\[5pt]
\dfrac{\sqrt5}{2\sqrt q},&q_*\le q<1.
\end{cases}}
\]
Both formulas agree at \(q=q_*\). The supremum is approached radially from \(|z|>1\) and its boundary maximizers are uniquely \(z=-1\) for \(0\le q\le q_*\). For \(q_*<q<1\), the only boundary maximizing points are \(z=e^{\pm i\theta_q}\), where
\[
\theta_q=\arccos\!\left(1-\frac{5(1-q)^2}{2q}\right)\in(0,\pi).
\]
The two maximizers split from \(-1\) with a square-root angular law:
\[
\pi-\theta_q\sim\sqrt{5(q_*^{-2}-1)}\sqrt{q-q_*}
\qquad(q\downarrow q_*,\ q>q_*).
\]
Finally, \(T_q\to I\) in operator norm as \(q\uparrow1\), yet
\[
\lim_{q\uparrow1}K(T_q)=\frac{\sqrt5}{2}>1=K(I).
\]
Thus this exact resolvent invariant is discontinuous at the identity along a path of two-dimensional contractions.

## Assumptions and scope

Matrices act on \(\mathbb C^2\) with its standard Hilbert norm; \(\|\cdot\|_{2\to2}\) is the induced spectral operator norm. The parameter is real and lies in \([0,1)\). The resolvent is taken only at \(|z|>1\). Since \(\|J\|=\|I\|=1\), the convex combination \(T_q=qI+(1-q)J\) has norm at most \(1\), while its spectrum is \(\{q\}\) and lies strictly inside the unit disk. In particular the Ritt constant is finite. At \(q=1\) we separately set \(T_1=I\) and the same defining supremum equals \(1\), but the displayed piecewise expression does not extend to that endpoint.

## Proof

**1. Reduction of the exterior supremum to the circle.** For \(0\le q<1\), the matrix-valued function
\[
F_q(z)=(z-1)(zI-T_q)^{-1}
\]
is holomorphic for \(|z|>q\), continuous for \(|z|\ge1\), and satisfies \(F_q(\infty)=I\). The scalar function \(z\mapsto\|F_q(z)\|\) is subharmonic: it is the supremum over unit vectors of the modulus of scalar holomorphic matrix coefficients. Equivalently, for any two unit vectors, the scalar coefficient \(\langle F_q(z)x,y\rangle\) obeys the maximum-modulus principle. Applying that principle on \(1\le|z|\le R\) and letting \(R\to\infty\) gives
\[
K(T_q)=\max\left\{1,\max_{|z|=1}\|F_q(z)\|\right\}.
\]
The boundary values computed below exceed \(1\), so the value of \(K(T_q)\) is the boundary maximum. Because the exterior domain in the definition is open, boundary maximization means the supremum is a limit of exterior values.

**2. An exact triangular singular-value identity.** Since \(J^2=0\),
\[
F_q(z)=\frac{z-1}{z-q}\begin{pmatrix}
1&\dfrac{1-q}{z-q}\\0&1
\end{pmatrix}.
\]
For any complex \(w\), direct diagonalization of the Hermitian Gram matrix gives
\[
\left\|\begin{pmatrix}1&w\\0&1\end{pmatrix}\right\|_{2\to2}
=f(|w|),\qquad f(x)=\frac{\sqrt{4+x^2}+x}{2}.
\]
In particular, for \(|z|=1\), put \(u=|z-q|\), \(v=|z-1|\), and \(a=1-q\). Elementary circle geometry yields
\[
u^2=a^2+qv^2,\qquad 0\le v\le2,
\]
and hence
\[
\|F_q(z)\|=\frac vu\,f\!\left(\frac au\right).
\]

**3. A one-variable strictly unimodal maximization.** First suppose \(0<q<1\), and use \(x=a/u\). As \(z\) traverses the upper semicircle, \(x\) traverses the full interval
\[
\frac{1-q}{1+q}\le x\le1.
\]
The preceding expression becomes
\[
\|F_q(z)\|=\frac{\sqrt{1-x^2}}{\sqrt q}\,f(x).
\]
Since \(f(x)>0\) and \(\frac{d}{dx}\log f(x)=1/\sqrt{x^2+4}\), the logarithmic derivative on \((0,1)\) is
\[
\frac{d}{dx}\log\big(\sqrt{1-x^2}\,f(x)\big)
=\frac{1}{\sqrt{x^2+4}}-\frac{x}{1-x^2}.
\]
Its sign is positive precisely when \((1-x^2)^2>x^2(x^2+4)\), equivalently \(x<1/\sqrt6\), and is negative precisely when \(x>1/\sqrt6\). Thus the unrestricted positive maximum occurs uniquely at \(x_0=1/\sqrt6\). This critical point is in the actual interval if and only if
\[
\frac{1-q}{1+q}\le\frac1{\sqrt6}
\quad\Longleftrightarrow\quad q\ge q_*.
\]
If \(0<q\le q_*\), the maximum occurs at the interval's left endpoint, which corresponds to \(v=2\), i.e. \(z=-1\). Direct evaluation gives
\[
\|F_q(-1)\|=\frac{2}{1+q}\,f\!\left(\frac{1-q}{1+q}\right)
=\frac{\sqrt{5+6q+5q^2}+1-q}{(1+q)^2}.
\]
If \(q\ge q_*\), the optimal point is \(x_0\), and \(f(x_0)=3/\sqrt6\), so
\[
K(T_q)=\frac1{\sqrt q}\sqrt{\frac56}\frac3{\sqrt6}
=\frac{\sqrt5}{2\sqrt q}.
\]
The equality \(u=a\sqrt6\) at the interior optimum, together with \(u^2=a^2+qv^2\), gives \(v^2=5a^2/q\). Since \(v^2=2-2\cos\theta\), there are exactly two unit-circle maximizers, \(e^{\pm i\theta_q}\), as displayed. At \(q=q_*\) the critical point lies at the interval endpoint and yields the unique maximizer \(-1\). The case \(q=0\) follows separately because \(|z-q|=1\) on the circle: the norm is \(|z-1|f(1)\) and attains its unique maximum \(2f(1)=1+\sqrt5\) at \(-1\), agreeing with the first branch.

**4. Square-root splitting and the identity limit.** Differentiating \(5(1-q)^2/q=5(q^{-1}-2+q)\) at \(q=q_*\) gives slope \(-5(q_*^{-2}-1)\). Hence
\[
4-v^2=5(q_*^{-2}-1)(q-q_*)+O((q-q_*)^2).
\]
For \(\theta\to\pi\), the circle identity \(v^2=2-2\cos\theta\) becomes \(4-v^2=(\pi-\theta)^2+O((\pi-\theta)^4)\), yielding the asserted square-root law. Finally the second branch converges to \(\sqrt5/2\) as \(q\uparrow1\), while \(\|T_q-I\|=(1-q)\|J-I\|\to0\). For \(T_1=I\), \((z-1)(zI-I)^{-1}=I\) whenever \(|z|>1\), proving \(K(I)=1\). This establishes the discontinuity and completes the proof.

## Verification

The two-by-two Gram spectrum, exterior maximum principle, exact change of variables, single critical point, endpoint cases and asymptotic expansion furnish a proof for every \(q\in[0,1)\). The independent standard-library script `verify_ritt.py` checks the algebraic threshold identities, direct triangular spectral norms at predicted maximizing angles, 181,000 angular comparison samples and additional exterior samples. These checks are supplementary; finite sampling does not prove universal angular or exterior optimality.

## Relationship to prior work

Borichev, Gomilko and Tomilov (2026) define the Ritt resolvent estimate and develop a qualitative Beurling–Kato and Hardy–Sobolev characterization for general operators. Their sections on sharpness construct infinite-dimensional spectral and power-orbit obstructions, not an exact two-dimensional Ritt constant or its maximizing boundary angles. Schwenninger (2016) studies how estimates in terms of the Tadmor–Ritt constant control functional calculi, without determining the proposed family’s exact constant. Published sharp affine Jordan norm-pencil formulas concern minimization of \(\|(1-\lambda)I+\lambda J_n\|\), not the exterior \(z\)-resolvent supremum, and their conclusions do not imply the two-branch formula here. The classical norm and maximum-modulus identities used in the proof are not claimed as new.

## Limitations

The result concerns only the indicated real affine Jordan contraction path on \(\mathbb C^2\). The formula neither determines Ritt constants of arbitrary two-dimensional contractions nor provides dimension-free upper bounds. Although the source and the closely related results were compared at the level of their actual claims, equivalent scalar-model computations hidden in older resolvent or pseudospectral literature remain a publication-priority risk. Independent scientific validation has not been performed.

## References

1. A. Borichev, A. Gomilko and Yu. Tomilov, *Beurling--Kato theory, Hardy--Sobolev calculus and Ritt operators*, arXiv:2607.10507v1, first public 11 July 2026, https://arxiv.org/abs/2607.10507 ; specifically Section 2.2 and Section 6 in the accessible version.
2. F. L. Schwenninger, *Functional calculus estimates for Tadmor--Ritt operators*, Journal of Mathematical Analysis and Applications 439 (2016), 103--124, DOI:10.1016/j.jmaa.2016.02.049.
3. Related published finite Jordan norm-pencil classification, *The sharp affine Jordan norm pencil and its scaled \(q\)-spectral-set transition*, October 2026. The result is cited solely to distinguish a different optimization problem.
