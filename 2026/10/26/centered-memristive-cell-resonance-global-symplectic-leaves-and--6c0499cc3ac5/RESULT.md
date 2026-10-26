# Centered memristive-cell resonance: global symplectic leaves and the complete two-cycle spectrum

## Finding

For the fourth-order mixed-Euler discretization of a passive memristive cell, the centered choice \(\lambda=1/2\) is the unique mixing parameter in \(0<\lambda<1\) for which the full map preserves four-dimensional volume. Its second iterate has a global two-parameter foliation by area-preserving planar maps, each explicitly a composition of two symplectic shears. Every pair of distinct real flux values determines a prime period-two orbit, and these exhaust all prime-two orbits. Every such orbit has two neutral Floquet multipliers and a reciprocal pair whose elliptic, hyperbolic, or parabolic nature is determined exactly by the two derivatives of the memristive characteristic. None is asymptotically attracting; indeed the centered map has no asymptotically attracting periodic orbit of any period.

## Assumptions and scope

Let \(C,R_A,T>0\). Let \(H:\mathbb R\to\mathbb R\) be a \(C^2\) flux-charge characteristic. For the passive-memristor interpretation, one may additionally assume \(H(0)=0\) and \(H'(x)\ge0\) everywhere; the structural theorem requires only smoothness. Define

\[
L(x)=\frac{H(x)}{C}-\frac{x}{R_A C},\qquad
(\Delta_\lambda f)_k=\frac{\lambda f_{k+1}+(1-2\lambda)f_k-(1-\lambda)f_{k-1}}{T}.
\]

Consider all bi-infinite real sequences satisfying the discretized cell equation

\[
\Delta_\lambda\big(\Delta_\lambda\varphi+L(\varphi)\big)=0.
\]

For \(0<\lambda<1\), this equation determines the global diffeomorphism \(F_\lambda:\mathbb R^4\to\mathbb R^4\), advancing the state \((\varphi_{k-2},\varphi_{k-1},\varphi_k,\varphi_{k+1})\) by one time step. The assertion of uniqueness of the volume-preserving parameter is restricted to this open parameter interval; the endpoint schemes have lower-order or implicit-state dynamics.

**Theorem.** For every \(0<\lambda<1\),

\[
\det DF_\lambda=\left(\frac{1-\lambda}{\lambda}\right)^2.
\]

Consequently, \(\lambda=1/2\) is the unique volume-preserving mixing value; the determinant is strictly above one below this value and strictly below one above it.

At \(\lambda=1/2\), put \(z_k=(\varphi_{k+1}-\varphi_{k-1})/(2T)+L(\varphi_k)\). On every solution \(z_{2j}=\nu_e\) and \(z_{2j+1}=\nu_o\), for uniquely determined real constants \(\nu_e,\nu_o\). Under a globally invertible smooth coordinate transformation, the second iterate \(F_{1/2}^2\) is the skew product fixing \(\nu_e,\nu_o\), with planar evolution

\[
O'=O+2T[\nu_e-L(E)],\qquad
E'=E+2T[\nu_o-L(O')].
\]

This planar map preserves the standard area form \(dE\wedge dO\).

Every unordered pair of distinct real numbers \(\{u,v\}\) gives precisely one prime two-cycle with scalar fluxes alternating between \(u\) and \(v\); all prime two-cycles arise this way. The two-step Floquet eigenvalues at this orbit are \(1,1,\mu_+,\mu_-\), where

\[
\mu_+\mu_-=1,\qquad
\mu_++\mu_-=2+4T^2L'(u)L'(v).
\]

The transverse pair is elliptic (nonreal unit-modulus) exactly when \(-1<T^2L'(u)L'(v)<0\), hyperbolic (real reciprocal eigenvalues off the unit circle) exactly when \(T^2L'(u)L'(v)>0\) or \(T^2L'(u)L'(v)<-1\), and parabolic at the two equality values. No such two-cycle, nor any other periodic orbit of the centered map, can be asymptotically attracting.

## Proof

**Four-dimensional Jacobian.** Let \(S\) denote the forward index shift. The Laurent polynomial of \(T\Delta_\lambda\) has coefficients \(\lambda\) at exponent \(+1\), \(1-2\lambda\) at exponent \(0\), and \(\lambda-1\) at exponent \(-1\). Hence \(\Delta_\lambda^2\varphi\) has coefficient \(\lambda^2/T^2\) on \(\varphi_{k+2}\) and coefficient \((1-\lambda)^2/T^2\) on \(\varphi_{k-2}\). The remaining term \(\Delta_\lambda L(\varphi)\) involves only \(\varphi_{k-1},\varphi_k,\varphi_{k+1}\). Solving explicitly for \(\varphi_{k+2}\) defines the forward companion map. Since the coefficient of \(\varphi_{k-2}\) is also nonzero, solving backwards defines its global smooth inverse. The companion determinant is the ratio of the extreme coefficients, \((1-\lambda)^2/\lambda^2\), independent of the state and of \(H\). It equals one precisely at \(\lambda=1/2\).

**Independent parity indices.** At the centered value, \((\Delta_{1/2}z)_k=(z_{k+1}-z_{k-1})/(2T)\), so the equation gives \(z_{k+1}=z_{k-1}\) at every index. Therefore the even and odd subsequences of \(z\) are separately constant. A two-step state chart may be defined from

\[
(p_0,p_1,p_2,p_3)=(\varphi_{2j-2},\varphi_{2j-1},\varphi_{2j},\varphi_{2j+1})
\]

by

\[
E=p_2,\quad O=p_1,\quad
\nu_o=\frac{p_2-p_0}{2T}+L(p_1),\quad
\nu_e=\frac{p_3-p_1}{2T}+L(p_2).
\]

The inverse is global:

\[
p_0=E-2T[\nu_o-L(O)],\quad p_1=O,\quad p_2=E,\quad
p_3=O+2T[\nu_e-L(E)].
\]

Thus there are no singular coordinate patches or exceptional leaves. Writing the new odd flux as \(O'=\varphi_{2j+1}\) and the new even flux as \(E'=\varphi_{2j+2}\), the two parity equations give exactly the shears displayed in the theorem. The first fixes \(E\) while translating \(O\); the second fixes \(O'\) while translating \(E\). Their Jacobians each have determinant one, proving preservation of \(dE\wedge dO\) and supplying a global area-preserving diffeomorphism on each leaf.

**Complete period-two family and multipliers.** Inserting any alternating scalar sequence \((\ldots,u,v,u,v,\ldots)\) into the centered formula gives \(\Delta_{1/2}\varphi_k=0\), hence \(z_{2j}=L(u)\) and \(z_{2j+1}=L(v)\); the equation is satisfied without restrictions on \(u,v\). Conversely, a prime period-two orbit of the four-state shift map forces \(\varphi_{k+2}=\varphi_k\), and therefore is precisely such an alternating sequence with \(u\ne v\), up to exchanging the two starting phases. On the leaf \(\nu_e=L(u),\nu_o=L(v)\), \((E,O)=(u,v)\) is a fixed point of the two-step shear map. Put \(a=L'(u)\) and \(b=L'(v)\). Its derivative in the \((E,O)\) chart is

\[
J=\begin{pmatrix}1+4T^2ab&-2Tb\\-2Ta&1\end{pmatrix},\quad
\det J=1,\quad\operatorname{tr}J=2+4T^2ab.
\]

In the full two-step chart the parity constants are fixed, giving the additional two unit eigenvalues; the derivative is block-triangular with diagonal blocks \(I_2\) and \(J\). The quadratic characteristic equation \(\mu^2-(2+4T^2ab)\mu+1=0\) implies the stated sharp elliptic/hyperbolic/parabolic partition by whether the trace is strictly inside, strictly outside, or exactly at the interval \([-2,2]\).

**No attracting periodic orbit.** Under the global chart, \(F_{1/2}^2\) has two independent first integrals \(\nu_e,\nu_o\), making an asymptotically attracting periodic orbit in the full four-dimensional space impossible: any open neighborhood contains points with different invariant values. More strongly, the return map of any periodic orbit restricted to the appropriate two-dimensional invariant leaf preserves area. A planar smooth area-preserving diffeomorphism cannot have an asymptotically attracting periodic point, since positive-area neighborhoods cannot be compressed into arbitrarily small neighborhoods under its iterates. This argument includes odd-period orbits by applying an even iterate, which leaves both parity invariants fixed.

**Passive example realizing both transverse types.** Take \(C=R_A=T=1\) and \(H(x)=x+\tfrac12\log\cosh x\). Then \(H(0)=0\), \(H'(x)=1+\tfrac12\tanh x>0\) and \(L'(x)=\tfrac12\tanh x\). The orbit with \((u,v)=(-1,2)\) satisfies \(-1<L'(u)L'(v)<0\) and is transverse-elliptic. The orbit with \((u,v)=(1,2)\) has positive derivative product and is transverse-hyperbolic. Both are nonattracting. This example does not assert nonlinear KAM stability of elliptic cycles.

## Verification

The accompanying `CHECKER.py` uses exact rational arithmetic to check the extreme Laurent coefficients, five distinct mixing parameters and their Jacobians, 245 successive parity-invariance relations, and 25 nontrivial exact instances of the global two-shear conjugacy. Independent numerical substitutions check four passive-memristor alternating cycles and their reciprocal multipliers. `CHECKER_OUTPUT.txt` is the actual output of executing the packaged checker. These finite calculations do not prove the universal classifications; the preceding algebraic argument supplies the proof.

## Relationship to prior work

Innocenti, Tesi, Di Marco, Pancioni and Forti (2026) introduce this mixed-Euler memristive model, derive its fourth-order equation and its one-parameter invariant foliation, and identify the centered operator as the midpoint rule. They explicitly mention more general fourth-order invariant manifolds in Remark 4. Their article supplies the starting recurrence and not the above two-parameter parity foliation, global symplectic shear conjugacy, complete alternating two-cycle family, exact reciprocal Floquet classification, or universal nonattraction at the midpoint. Their 2025 input-output article develops the broader feature-preserving discretization framework. The interpretation as symplectic shears uses standard geometric-integration concepts; no priority is claimed for the general fact that compositions of shears preserve planar area. The novel claim is specific to the complete four-dimensional memristive map at its centered resonance.

## Limitations

The volume conclusion covers the explicit full fourth-order map for \(0<\lambda<1\), not the lower-order endpoint discretizations. The symplectic conclusion applies exactly at the centered value, not for other mixing parameters. Elliptic refers only to the two-dimensional transverse linear pair and does not prove nonlinear stability or the existence of KAM tori. The model is a mathematical discretization and not a claim about dynamical attraction in the original continuous-time physical circuit. The first verifiable public date of the motivating article is its online publication on May 12, 2026; no earlier public preprint has been verified. Historical reductions through general numerical-analysis results remain a priority risk.

## References

1. G. Innocenti, A. Tesi, M. Di Marco, L. Pancioni, and M. Forti, *Versatile discrete-time memristive cell*, Nonlinear Dynamics **114**, Article 692 (2026), publicly published May 12, 2026, DOI: 10.1007/s11071-026-12583-9, https://link.springer.com/article/10.1007/s11071-026-12583-9. See equations (9), (12), (13), (14), and Remark 4, equations (21)–(25).
2. G. Innocenti, A. Tesi, M. Di Marco, L. Pancioni, and M. Forti, *Feature preserving discretization of memristive circuits using an input-output approach*, Nonlinear Dynamics **113**, 28179–28206 (2025), DOI: 10.1007/s11071-025-11568-4, https://link.springer.com/article/10.1007/s11071-025-11568-4.
