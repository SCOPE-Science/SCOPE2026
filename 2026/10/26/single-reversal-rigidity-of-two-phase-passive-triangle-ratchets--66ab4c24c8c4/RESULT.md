# Single-reversal rigidity of two-phase passive triangle ratchets

## Finding

For two arbitrary continuous-time, reversible three-site spatial Markov chains whose mode variable flips at a site-independent, symmetric Poisson rate \(r>0\), the observed stationary clockwise cycle current is always
\[
J(r)=\frac{r(A+Br)}{d_0+d_1r+d_2r^2},\qquad d_0,d_2>0,\quad d_0+d_1r+d_2r^2>0\ \text{for every}\ r\ge0.
\]
Here \(A,B\) are real constants determined explicitly by the generators below. Thus the current changes sign at most once on the positive switching-rate axis; it changes sign exactly once if and only if \(AB<0\), at \(r_*=-A/B\). This bound is sharp, and a stall of the spatial current need not be an equilibrium state.

## Assumptions and scope

The sites are \(i\in\mathbb Z/3\mathbb Z\). A mode \(s\in\{0,1\}\) has arbitrary strictly positive numbers \(p_{s,i}\) (unnormalized equilibrium weights) and \(c_{s,i}\) (bond conductances). In mode \(s\), the jump rate from \(i\) to \(i+1\) is \(c_{s,i}/p_{s,i}\), and from \(i+1\) to \(i\) is \(c_{s,i}/p_{s,i+1}\). The mode flips between \(0\) and \(1\) at fixed spatial site at the same rate \(r\) in both directions, independent of position. All rates are strictly positive. Write \(L_s\) for each \(3\times3\) column probability generator and \(z_s\) for its three-component stationary subpopulation in the six-state system. The spatial current across bond \(0\to1\) is
\[
J(r)=\sum_{s=0}^1 c_{s,0}\left(\frac{z_{s,0}}{p_{s,0}}-\frac{z_{s,1}}{p_{s,1}}\right).
\]
By conservation, this equals the clockwise current through either other bond. The stationary distribution exists uniquely for every \(r>0\); at \(r=0\), the unique continuous extension uses equal mass \(1/2\) in the two isolated stationary modes.

## Proof

Set \(e=(1,1,1)^T\),
\[
U=\begin{pmatrix}1&0\\-1&1\\0&-1\end{pmatrix},\qquad
R=\begin{pmatrix}1&0&0\\0&0&-1\end{pmatrix},\qquad RU=I_2.
\]
The symmetric mode-flip process enforces stationary mass \(e^Tz_s=1/2\) in each mode. Hence, for unique \(w_s\in\mathbb R^2\), write \(z_s=e/6+Uw_s\). With
\[
B_s=-RL_sU,\qquad f_s=RL_s(e/6),
\]
stationarity is the four-dimensional system
\[
H(r)\begin{pmatrix}w_0\\w_1\end{pmatrix}=
\begin{pmatrix}f_0\\f_1\end{pmatrix},\qquad
H(r)=\begin{pmatrix}B_0+rI_2&-rI_2\\-rI_2&B_1+rI_2\end{pmatrix}.
\]
For scalar off-diagonal blocks, the block-determinant identity (initially when blocks are invertible and then by polynomial continuation) gives
\[
d(r):=\det H(r)=\det\left(B_0B_1+r(B_0+B_1)\right)
=d_0+d_1r+d_2r^2.
\]
Because each isolated generator is reversible and irreducible, its two nonzero eigenvalues are real and strictly negative; thus \(d_0=\det(B_0)\det(B_1)>0\). The sum \(L_0+L_1\) is also an irreducible generator. Its restriction to the zero-sum space has two eigenvalues with strictly positive-real-part negatives; its determinant \(d_2=\det(B_0+B_1)>0\). For \(r>0\), the full six-state process is irreducible, so its normalized stationary law is unique, implying \(H(r)\) is invertible. Since \(d(0)>0\) and the determinant never vanishes on the positive axis, \(d(r)>0\) for all \(r\ge0\).

The coefficient of \(r\) in \(H(r)\) is
\[
K=\begin{pmatrix}I_2&-I_2\\-I_2&I_2\end{pmatrix},
\]
which has rank \(2\). Every \(3\times3\) minor of \(H(0)+rK\) is therefore a polynomial of degree at most \(2\): its putative cubic coefficient is a \(3\times3\) minor of \(K\), which vanishes. Consequently every entry of \(\operatorname{adj} H(r)\) has degree at most \(2\). Cramer's rule and the linear definition of \(J\) imply that \(d(r)J(r)\) is a polynomial of degree at most \(2\). At \(r=0\), both mode-conditional equilibria satisfy detailed balance on each bond, so \(J(0)=0\). This forces \(d(r)J(r)=r(A+Br)\). In fully constructive terms, \(A=N'(0)\) and \(B=N''(0)/2\) for \(N(r)=d(r)J(r)\), where \(N\) is obtained by the displayed \(4\times4\) matrix adjugate. Strict positivity of \(d\) makes the stated root/sign classification immediate. This proves the theorem without assuming special relations between the two mode potentials or conductances.

For sharpness, take \(p_0=c_0=(1,1,1)\), \(p_1=(1,2,3)\) and \(c_1=(4,1,2)\). Direct substitution into the stationary matrix yields
\[
J(r)=\frac{r(r-2)}{2(103r^2+339r+252)}.
\]
At the unique stall \(r=2\), the phase populations (sites in cyclic order) are
\[
z_0=\frac1{122}(17,21,23)^T,\qquad
z_1=\frac1{122}(12,22,27)^T.
\]
The phase-resolved clockwise bond currents are \((-2,-1,3)/61\) and \((2,1,-3)/61\), respectively, so the observed current is zero on every bond despite nonzero microscopic circulating fluxes. Moreover, the vertical edge at site \(0\) has forward stationary flux \(17/61\) and reverse flux \(12/61\), giving the strictly positive entropy-production contribution
\[
\frac5{61}\log\!\frac{17}{12}>0.
\]
Every other undirected-edge contribution is nonnegative by the inequality \((a-b)\log(a/b)\ge0\), so the full steady entropy production is strictly positive.

## Verification

The included standalone `checker.py` builds the complete six-state generator with exact rational arithmetic, independently solves its normalized stationary equations, verifies the reduced \(4\times4\) determinant and current identities for several nonequivalent parameter sets, and verifies the displayed sharp example and stall populations. Run `python checker.py` with SymPy installed. The general theorem is proved algebraically above; finitely many computational tests are corroborative only.

## Relationship to prior work

Jarzynski and Mazonka (1999) solved directed transport in an exactly solvable finite ratchet-and-pawl model, with transition structure tied to thermal reservoirs. Lee, Allison, Abbott, and Stanley (first public 2002; journal 2003) analyzed a three-state discrete-time ratchet with noise-induced current and current reversal; in particular, the special case with one fully mixing mode is closely related to their class of noisy three-state models, so current reversal alone is not asserted as novel. Levien and Bressloff (2015) derived quasi-steady-state approximations to flashing-ratchet transport in a different switching regime. The narrower point established here is the **global maximum of one positive current reversal**, uniformly across two *arbitrary* reversible three-state phases coupled by position-independent symmetric Poisson switching; it is not an asymptotic or special-potential formula. Reversible modes, unrestricted positive conductances, positivity of the full stationary law, and the two-mode rank bound are all essential to the stated scope.

## Limitations

The proof does not cover more than three spatial sites, more than two modes, site-dependent flip rates, asymmetric environmental flip rates, zero bond rates, or arbitrary irreversible frozen modes. It bounds sign changes in the **total spatial current** only, not all phase-resolved or environmental currents. The formula by itself does not determine the sign for given parameters without computing \(A,B\); this computation is finite linear algebra. A zero net spatial current is not necessarily detailed balance. The literature-priority comparison is not a claim of exhaustive coverage of all discrete motor models.

## References

1. C. Jarzynski and O. Mazonka, “Feynman's ratchet and pawl: an exactly solvable model,” first public 1999-02-03, arXiv:cond-mat/9902056; *Physical Review E* **59**, 6448 (1999).
2. Y. Lee, A. Allison, D. Abbott, and H. E. Stanley, “Minimal Brownian Ratchet: An Exactly Solvable Model,” first public 2002-05-15, arXiv:cond-mat/0205302; *Physical Review Letters* **91**, 220601 (2003).
3. E. Levien and P. C. Bressloff, “Quasi-steady-state analysis of coupled flashing ratchets,” *Physical Review E* **92**, 042129 (2015), doi:10.1103/PhysRevE.92.042129.
