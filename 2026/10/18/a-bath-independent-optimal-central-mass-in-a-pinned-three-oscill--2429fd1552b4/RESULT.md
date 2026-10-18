# A bath-independent optimal central mass in a pinned three-oscillator Langevin chain

## Finding

A three-oscillator classical harmonic chain with identical unit endpoint masses, a variable central mass, uniform positive onsite pinning, unit nearest-neighbor springs, and identical Langevin coupling strengths at the two ends has a unique conductance-maximizing central mass. The optimizer is strictly heavier than the endpoints, is independent of the reservoir coupling strength and reservoir temperatures, and obeys an exact positive-square resistance penalty.

Write \(b>0\) for the onsite spring constant, \(\gamma>0\) for each endpoint Langevin friction, and \(m>0\) for the middle mass. For endpoint bath temperatures \(T_L>T_R>0\), let \(J\) be the stationary left-to-right heat current and \(\mathcal K(m)=J/(T_L-T_R)\). Set
\[
\begin{aligned}
D(m)={}&1+\gamma^2\bigl[(b+1)^3m^2
 -(2b^3+8b^2+7b+1)m\\
&\hspace{32mm}+b^3+5b^2+7b+2\bigr]
 +\gamma^4(b^2+3b+1)m.
\end{aligned}
\]
Then the exact conductance is
\[
\boxed{\mathcal K(m)=\frac{\gamma[1+\gamma^2(b+1)m]}{2D(m)}.}
\]
Its unique global maximizer over all \(m>0\) is
\[
\boxed{m_*(b)=1+\frac{b}{(b+1)^2},\qquad
\mathcal K(m_*)=\frac{\gamma(b+1)}{2[b+1+\gamma^2(b^2+3b+1)]}.}
\]
More precisely, for every admissible \(m,b,\gamma\),
\[
\boxed{\frac1{\mathcal K(m)}-\frac1{\mathcal K(m_*)}
=\frac{2\gamma(b+1)^3[m-m_*(b)]^2}{1+\gamma^2(b+1)m}.}
\]
The identity certifies uniqueness without numerical optimization. In particular \(1<m_*(b)\le5/4\), with equality in the upper bound only at \(b=1\); the uniform-mass chain \(m=1\) is strictly suboptimal for every \(b>0\). For \(b=\gamma=1\), the optimizer \(m_*=5/4\) yields \(\mathcal K=1/7\), whereas \(\mathcal K(1)=3/22\).

## Assumptions and scope

The positions and canonical momenta are \((q_1,q_2,q_3,p_1,p_2,p_3)\in\mathbb R^6\). The endpoint masses are \(1\), the central mass is \(m>0\), the two spring constants are \(1\), and every site has onsite potential \(bq_i^2/2\), with \(b>0\). The energy is
\[
H=\frac{p_1^2}2+\frac{p_2^2}{2m}+\frac{p_3^2}2+
\frac b2\sum_{i=1}^3q_i^2+
\frac12(q_2-q_1)^2+\frac12(q_3-q_2)^2.
\]
The endpoint Langevin equations are
\[
\begin{aligned}
dp_1&=[-(b+1)q_1+q_2-\gamma p_1]dt+\sqrt{2\gamma T_L}\,dB_L,\\
dp_3&=[q_2-(b+1)q_3-\gamma p_3]dt+\sqrt{2\gamma T_R}\,dB_R,
\end{aligned}
\]
where \(B_L,B_R\) are independent standard Brownian motions. The interior site evolves as \(dq_2=p_2dt/m\) and \(dp_2=[q_1+q_3-(b+2)q_2]dt\); the endpoint positions satisfy \(dq_1=p_1dt\), \(dq_3=p_3dt\). Temperature is in units with Boltzmann's constant equal to one. The bath-to-chain heat flux is \(J=\gamma(T_L-\mathbb E_\pi[p_1^2])\), where \(\pi\) is the stationary probability law. Equal positive bath frictions are assumed throughout.

Positive pinning makes the force matrix positive definite. The noiseless energy dissipation is \(-\gamma(p_1^2+p_3^2)\); its zero-dissipation invariant set is only the origin, since zero endpoint velocities force \(q_2=(b+1)q_1=(b+1)q_3\), and the remaining equations force every coordinate to vanish. By the linear invariance principle the drift is Hurwitz. Thus a unique stationary Gaussian law exists and its covariance solves the matrix Lyapunov equation. No infinite-chain or small-temperature-difference limit is used.

## Proof

Put \(B=b+1\), and introduce symmetric and antisymmetric endpoint variables
\[
y_-=(q_1-q_3,p_1-p_3)^\top,
\qquad
y_+=(q_1+q_3,q_2,p_1+p_3,p_2)^\top.
\]
The deterministic drift is block diagonal in these coordinates, with matrices
\[
A_-=
\begin{pmatrix}0&1\\-B&-\gamma\end{pmatrix},
\quad
A_+=
\begin{pmatrix}
0&0&1&0\\
0&0&0&1/m\\
-B&2&-\gamma&0\\
1&-(b+2)&0&0
\end{pmatrix}.
\]
Let \(W=\mathbb E_\pi[y_-y_+^\top]\), a \(2\)-by-\(4\) matrix. The two endpoint heat baths induce just one nonzero cross-noise covariance, at the row of \(p_1-p_3\) and column of \(p_1+p_3\), with value \(2\gamma(T_L-T_R)\). Hence
\[
A_-W+WA_+^\top+2\gamma(T_L-T_R)E_{2,3}=0,
\]
where \(E_{2,3}\) denotes the \(2\)-by-\(4\) elementary matrix. This gives eight linear scalar equations, independent of the equilibrium portions of the covariance.

Writing the eight unknown entries of \(W\) in row-major order, the coefficient matrix of these eight equations has determinant \(4D(m)/m^2\). Direct elimination gives
\[
W_{2,3}=(T_L-T_R)\left[1-
\frac{1+\gamma^2(b+1)m}{D(m)}\right].
\]
Both identities follow by ordinary polynomial elimination; the attached symbolic checker builds and solves the eight equations from the displayed drift matrices rather than assuming the proposed conductance. The current exiting the right reservoir equals the current entering the left. Therefore
\[
\mathbb E_\pi[p_1^2]-\mathbb E_\pi[p_3^2]
=(T_L-T_R)-\frac{2J}{\gamma}
=W_{2,3}.
\]
Substitution yields exactly \(\mathcal K(m)=\gamma[1+\gamma^2(b+1)m]/[2D(m)]\).

Write \(C=b^2+3b+1\) and \(m_*=C/(b+1)^2\). Elementary expansion of the displayed rational formula yields the exact identity
\[
\frac{1}{\mathcal K(m)}
=\frac{2[b+1+\gamma^2C]}{\gamma(b+1)}
+\frac{2\gamma(b+1)^3(m-m_*)^2}{1+\gamma^2(b+1)m}.
\]
The right side is strictly positive, independently verifying \(D(m)>0\) for \(m>0\), and the second term is zero exactly at \(m=m_*\). Thus \(m_*\) is the unique global conductance maximum for each \(\gamma>0\), with the claimed optimized value. The identity also proves that conductance increases strictly to \(m_*\) and decreases strictly afterward: the derivative of \((m-m_*)^2/[1+\gamma^2(b+1)m]\) has the sign of \(m-m_*\). The bound \(b/(b+1)^2\le1/4\) follows from \((b-1)^2\ge0\). All endpoint and parameter assertions follow.

## Verification

The accompanying standalone `verify.py` uses exact symbolic arithmetic to construct the eight cross-covariance equations, compute their determinant, solve them for the heat-current correlation, establish the conductance formula, factor the inverse-conductance difference, and check the derivative. It also independently solves the unreduced six-coordinate, twenty-one-equation stationary covariance system at eight distinct rational parameter triples with positive and unequal bath temperatures. These calculations passed on the packaged program. They are reproducibility checks on a proof that is algebraic for all real positive parameters, not a replacement for that proof. Run `python verify.py` with SymPy installed (see `requirements.txt`).

## Relationship to prior work

Dhar and Roy (arXiv:cond-mat/0606465, first public 2006-06-19) derive general harmonic-lattice heat transport in terms of Green functions and reservoir self-energies. Kundu (arXiv:1009.0366, first public 2010-09-02) treats the same underlying class of pinned, mass-disordered chains with endpoint Langevin reservoirs, giving Green-function current and current-correlation representations. Their frameworks include this three-site model, and neither the harmonic-chain model nor its general transport formalism is claimed as new. Their inspected expressions do not state the present unique middle-mass optimizer or the exact positive-square resistance penalty; obtaining these requires specializing the finite covariance problem and comparing every positive mass.

Roy and Dhar (arXiv:0806.4693) analyze effects of pinning on disorder-averaged long-chain heat transport, a different observable and scale. Kim (arXiv:1304.1283) investigates exact finite quantum Brownian harmonic-chain transport and optimization of other couplings, under a different bath model; it does not imply the claimed classical central-mass optimum. The contribution here is the precise all-parameter optimal-defect classification for a natural minimal finite chain, not general Green-function heat transport.

## Limitations

The theorem is confined to three oscillator sites, equal endpoint masses, unit nearest-neighbor springs, uniform onsite pinning, identical Ohmic white-noise Langevin frictions on the endpoints, and a variable central mass. Positive pinning is essential to the stated stationary-position Gaussian argument; the unpinned translational zero mode is not included. The result concerns stationary *mean heat conductance* only, not current fluctuations, nonlinear interactions, quantum temperatures, arbitrarily unequal reservoir frictions, or long-chain conductance. General harmonic-lattice current formulas in prior work remain broader than this particular evaluation. A previously published equivalent special-case optimization could exist outside the inspected sources.

## References

1. A. Dhar and D. Roy, *Heat transport in harmonic lattices*, arXiv:cond-mat/0606465 (first submitted 2006-06-19), https://arxiv.org/abs/cond-mat/0606465.
2. A. Kundu, *Time auto-correlation function and Green-Kubo formula: A study on disordered harmonic chain*, arXiv:1009.0366 (first submitted 2010-09-02), https://arxiv.org/abs/1009.0366.
3. D. Roy and A. Dhar, *Role of pinning potentials in heat transport through disordered harmonic chain*, arXiv:0806.4693 (first submitted 2008-06-29), https://arxiv.org/abs/0806.4693.
4. I. Kim, *Heat transport through a quantum Brownian harmonic chain beyond the weak-coupling regime: An exact treatment*, arXiv:1304.1283 (first submitted 2013-04-04), https://arxiv.org/abs/1304.1283.
