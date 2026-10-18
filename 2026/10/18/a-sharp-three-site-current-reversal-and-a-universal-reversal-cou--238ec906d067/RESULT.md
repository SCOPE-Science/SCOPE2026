# A sharp three-site current reversal and a universal reversal-count bound for switching ratchets

## Finding

For any cycle with \(n\ge3\) sites, a particle moving in either of two individually reversible, irreducible nearest-neighbor continuous-time landscapes can switch landscapes at a common, position-independent rate \(\kappa>0\). The unique stationary oriented spatial current \(J(\kappa)\) is either identically zero or has at most \(n-2\) distinct positive zeros (in fact the total multiplicity of positive zeros is at most \(n-2\)). In particular there are at most \(n-2\) current-direction reversals as the switching rate increases.

This bound is attained at the first nontrivial cycle size, \(n=3\). There are explicit positive, reversible landscape rates for which
\[
J(\kappa)=\frac{\kappa(5\kappa-2)}{2(469\kappa^2+1236\kappa+792)}.
\]
The current is strictly negative for \(0<\kappa<2/5\), vanishes at \(\kappa=2/5\), and is strictly positive for \(\kappa>2/5\), even though each uncoupled landscape has exactly zero current.

## Assumptions and scope

Let \(\mathbb Z/n\mathbb Z\) be a cyclic spatial coordinate, \(n\ge3\). For each environment \(e\in\{0,1\}\), let \(Q_e\) be a row-generator matrix of an irreducible nearest-neighbor continuous-time Markov chain, with both directional rates on every cyclic edge strictly positive. Assume each \(Q_e\) is individually reversible: there exists a positive normalized row vector \(\pi_e\) satisfying \(\pi_eQ_e=0\) and detailed balance on each edge. The environment switches in either direction at one and the same spatially independent rate \(\kappa>0\), without moving the particle. The joint generator, in environment-first state order, is
\[
\mathcal Q(\kappa)=\begin{pmatrix}Q_0-\kappa I&\kappa I\\\kappa I&Q_1-\kappa I\end{pmatrix}.
\]
Write \(p_e(i)\) for its unique stationary probability of site \(i\) and environment \(e\). For any fixed spatial edge \(i\to i+1\), define
\[
J(\kappa)=\sum_{e=0}^{1}\bigl[p_e(i)q_e(i,i+1)-p_e(i+1)q_e(i+1,i)\bigr].
\]
The sum is independent of the chosen edge because total spatial probability satisfies stationary conservation. This signed edge flux is the unwrapped winding velocity divided by \(n\). No reversibility is assumed of the full switching process. The assertion concerns roots on the open half-line \(\kappa>0\), not the limiting disconnected chain at \(\kappa=0\).

## Proof

**Reduction to \(n-1\) dimensions.** Work with row vectors. Let \(V=\{v\in\mathbb R^n:v\mathbf1=0\}\), a space of dimension \(n-1\). Since \(Q_e\) is irreducible, its right action on \(V\) is invertible. Denote that inverse by \(R_e\), meaning \((vR_e)Q_e=v\) for every \(v\in V\). Put \(M=R_0+R_1\). Every eigenmode of \(Q_e\) outside the stationary direction lies in this restricted problem; in particular no singularity occurs in \(R_e\).

Stationarity of the environment marginal yields \(\sum_i p_0(i)=\sum_i p_1(i)=1/2\). Set \(r_e=2p_e\) and \(d=r_0-r_1\in V\). The two stationary equations are
\[
r_0Q_0=\kappa d,\qquad r_1Q_1=-\kappa d.
\]
Subtracting the individually stationary vectors and using the inverse operators on \(V\) gives
\[
r_0=\pi_0+\kappa dR_0,\qquad r_1=\pi_1-\kappa dR_1,
\]
and therefore
\[
d(I_V-\kappa M)=\pi_0-\pi_1.\tag{1}
\]

**Nonvanishing denominator.** For each \(\kappa>0\), the operator \(I_V-\kappa M\) is nonsingular. Indeed, if \(0\ne d\in V\) belonged to its left kernel, define \(r_0=\kappa dR_0\) and \(r_1=-\kappa dR_1\). Then \(r_0-r_1=\kappa dM=d\), and the two component stationarity equations hold. This would give a nonzero stationary signed vector of total mass zero for the irreducible joint generator \(\mathcal Q(\kappa)\), contradicting the one-dimensionality of its stationary left kernel. Consequently
\[
D(\kappa)=\det(I_V-\kappa M)
\]
is nonzero for \(\kappa>0\). Since \(D(0)=1\) and it is continuous, \(D(\kappa)>0\) for all \(\kappa\ge0\).

**Degree of the current numerator.** On the edge \(0\to1\), introduce the column \(f_e\) with components \((f_e)_0=q_e(0,1)\), \((f_e)_1=-q_e(1,0)\), and all other components zero. Detailed balance implies \(\pi_e f_e=0\). Equations (1) and the expressions for \(r_e\) give the exact rational identity
\[
J(\kappa)=\frac{\kappa}{2}(\pi_0-\pi_1)(I_V-\kappa M)^{-1}(R_0f_0-R_1f_1).\tag{2}
\]
Choose any basis of \(V\). Its inverse matrix is its adjugate divided by \(D(\kappa)\). The adjugate entries are polynomials in \(\kappa\) of degree at most \(n-2\); thus
\[
J(\kappa)=\frac{\kappa P(\kappa)}{D(\kappa)},\qquad \deg P\le n-2,\qquad D(\kappa)>0\ (\kappa\ge0).
\]
If \(P\) is the zero polynomial, then \(J\equiv0\). Otherwise its positive zeros and sign reversals are bounded by its polynomial degree, including multiplicity. This proves the general statement.

**A three-site sharp witness.** For each environment choose strictly positive site weights and cyclic edge conductances
\[
(w_{0,0},w_{0,1},w_{0,2})=(2,3,1),\quad (c_{0,0},c_{0,1},c_{0,2})=(1,2,3),
\]
\[
(w_{1,0},w_{1,1},w_{1,2})=(1,1,2),\quad (c_{1,0},c_{1,1},c_{1,2})=(1,1,1).
\]
For edge \(i\leftrightarrow i+1\), assign \(q_e(i,i+1)=c_{e,i}/w_{e,i}\) and \(q_e(i+1,i)=c_{e,i}/w_{e,i+1}\), with cyclic indices. Then \(\pi_e(i)=w_{e,i}/\sum_j w_{e,j}\) satisfies detailed balance. Solving the resulting six-state linear stationary equations exactly gives
\[
J(\kappa)=\frac{\kappa(5\kappa-2)}{2(469\kappa^2+1236\kappa+792)}.
\]
The denominator is strictly positive for positive \(\kappa\), so there is exactly one positive reversal at \(\kappa=2/5\). Since \(n-2=1\) for \(n=3\), the bound is sharp at this size. No claim of sharpness for every larger \(n\) is made.

## Verification

The standalone `VERIFY.py` reconstructs the six-state generator from the two positive conductance landscapes, solves its stationary equations over exact rational functions, and compares the current against the displayed formula. Independently it computes the restricted zero-sum resolvent representation (2) and compares that prediction with the full generator's current for synthetic positive reversible landscapes of sizes \(3\) through \(6\) at rational switching rates. Detailed balance, normalization, stationary environment masses, numerator signs, and strictly positive restricted determinants are checked using exact symbolic/rational arithmetic. Run with `python VERIFY.py` after installing `requirements.txt`. The recorded run passed 187 exact assertions; no finite enumeration is used as an infinite-size proof.

## Relationship to prior work

Lee, Allison, Abbott, and Stanley (2003) solved a different discrete-time three-state ratchet with an imposed stochastic mixing mechanism and derived a current-null curve. Their three-state generator has no independently reversible pair of landscapes with homogeneous continuous-time switching. Zhang (2010) obtained a general expression for the velocity of two-state hopping molecular motors, encompassing stationary-current equations of the present type; this is important prior coverage of the **current-computation framework**, not an asserted new discovery. The rate-polynomial degree obstruction and the explicitly reversible three-site sign-changing witness are additional properties not supplied by the inspected general equations or analyzed special cases. Levien and Bressloff (2015) developed a quasi-steady-state reduction for continuous-space flashing ratchets, primarily at fast state switching, rather than an all-rate exact finite-cycle zero bound. These mathematical distinctions should not be read as proof of exhaustive historical novelty.

## Limitations

The theorem requires finite cycles, strictly positive spatial nearest-neighbor rates, individual spatial detailed balance, and equal site-independent bidirectional environment switching. It does not classify unequal or spatially varying switching, multiple environments, lattice size two, interactions, or time-periodic protocols. The bound may be non-sharp for larger \(n\); only \(n=3\) has an explicit saturating example here. Prior work gives more general current-computation schemes. Full independent scientific and historical validation has not been performed.

## References

1. Y. Lee, A. Allison, D. Abbott and H. E. Stanley, “Minimal Brownian Ratchet: An Exactly Solvable Model,” *Physical Review Letters* **91**, 220601 (24 November 2003). DOI: 10.1103/PhysRevLett.91.220601. https://www.eleceng.adelaide.edu.au/personal/dabbott/publications/PRL_lee2003.pdf
2. Y. Zhang, “The mean velocity of two-state models of molecular motor,” arXiv:1007.1745 (first publicly submitted 10 July 2010), later *Modern Physics Letters B* **25** (2011), 1725–1747. https://arxiv.org/pdf/1007.1745
3. E. Levien and P. C. Bressloff, “Quasi-steady-state analysis of coupled flashing ratchets,” *Physical Review E* **92**, 042129 (12 October 2015). DOI: 10.1103/PhysRevE.92.042129. https://www.math.utah.edu/~bresslof/publications/15-12.pdf
