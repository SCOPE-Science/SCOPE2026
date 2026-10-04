# Equilibrium-line correction and an exact stationary shell law for a 5D memristive flow
## Finding
For the classical integer-order system
\[
\dot x=a(w-x),\qquad \dot y=-w,\qquad \dot z=xw-bz,
\]
\[
\dot w=-xz+cw+dy,\qquad \dot u=-w+kx(m+3nu^2),
\]
with \(a,b,c,d>0\), the complete equilibrium set is
\[
\mathcal E=\{{(0,0,0,0,s):s\in\mathbb R\}},
\]
not only the origin. At every point of \(\mathcal E\), the characteristic polynomial is
\[
\lambda(\lambda+a)(\lambda+b)(\lambda^2-c\lambda+d).
\]
Thus the zero eigenvalue is the tangent direction of the equilibrium line, while the four nonzero factors describe the transverse linearization.

Every compactly supported invariant Borel probability measure \(\mu\) of the integer-order flow satisfies
\[
b\langle z\rangle=\langle x^2\rangle
\]
and the exact stationary shell law
\[
\left\langle\left(z-\frac c2\right)^2\right\rangle
=\frac{c^2}{4}+\frac{c}{a^2b}\langle\dot x^2\rangle.
\]
Equality holds exactly for invariant measures supported on \(\mathcal E\). Therefore every compact invariant measure not supported on equilibria gives positive measure to the set \(\{{z<0\}}\cup\{{z>c\}}\).

At the published integer-order parameters \(a=20\), \(b=2\), \(c=10\),
\[
\langle z\rangle=\frac12\langle x^2\rangle,
\qquad
\langle(z-5)^2\rangle=25+\frac1{80}\langle\dot x^2\rangle.
\]
Hence every non-equilibrium compact recurrent statistical state has the second quantity strictly larger than \(25\) and must spend positive statistical mass with \(z<0\) or \(z>10\).

## Assumptions and scope
The theorem concerns the smooth autonomous integer-order system displayed above and assumes \(a,b,c,d>0\). The parameters \(k,m,n\) may be arbitrary finite real numbers. Compactly supported invariant probability measure means a Borel probability measure invariant under the classical flow and having compact support. Angular brackets denote integration against that measure.

The equilibrium-line statement also applies algebraically to constant solutions of the associated Caputo fractional model because constant solutions are found by setting the right-hand side to zero. The invariant-measure identities are not asserted for the fractional-memory system: a Caputo equation is not the same finite-dimensional autonomous flow, so the generator argument below does not transfer without an augmented memory-state formulation.

## Proof
Setting all five right-hand sides to zero gives \(w=0\) from \(\dot y=0\), then \(x=0\) from \(\dot x=0\), then \(z=0\) from \(\dot z=0\) because \(b>0\), and finally \(y=0\) from \(\dot w=0\) because \(d>0\). With these four coordinates zero, \(\dot u=0\) for every \(u=s\), proving that the full equilibrium set is \(\mathcal E\).

At \(p_s=(0,0,0,0,s)\), the \(u\)-column of the Jacobian is zero. Expanding the characteristic determinant first in that column gives a factor \(\lambda\). The remaining \(z\)-direction contributes \(\lambda+b\), and the \(x,y,w\) block has determinant \( (\lambda+a)(\lambda^2-c\lambda+d)\). This proves the stated characteristic polynomial, independently of \(s,k,m,n\).

For a compactly supported invariant measure, stationarity gives zero mean derivative for every smooth polynomial observable used below. From \(\dot y=-w\) and \(\dot x=a(w-x)\),
\[
\langle w\rangle=\langle x\rangle=0.
\]
From the observables \(z\) and \(x^2\),
\[
0=\langle xw-bz\rangle,
\qquad
0=2a\langle x(w-x)\rangle,
\]
so
\[
\langle xw\rangle=\langle x^2\rangle=b\langle z\rangle.
\]
Now set
\[
E=\frac12(z^2+w^2+dy^2).
\]
Direct differentiation along the vector field cancels all mixed terms:
\[
\dot E=z(xw-bz)+w(-xz+cw+dy)+dy(-w)=-bz^2+cw^2.
\]
Stationarity therefore gives
\[
b\langle z^2\rangle=c\langle w^2\rangle.
\]
Finally,
\[
\langle\dot x^2\rangle
=a^2\langle(w-x)^2\rangle
=a^2(\langle w^2\rangle-\langle x^2\rangle),
\]
where the last equality uses \(\langle xw\rangle=\langle x^2\rangle\). Hence
\[
\begin{{aligned}}
\left\langle\left(z-\frac c2\right)^2\right\rangle
&=\langle z^2\rangle-c\langle z\rangle+\frac{{c^2}}4\\
&=\frac cb(\langle w^2\rangle-\langle x^2\rangle)+\frac{{c^2}}4\\
&=\frac{{c^2}}4+\frac{c}{a^2b}\langle\dot x^2\rangle.
\end{{aligned}}
\]

If equality holds, then the continuous nonnegative function \(\dot x^2\) has zero integral, so \(\dot x=0\) on the support of \(\mu\). The support of an invariant measure is flow-invariant. Along every complete orbit in that compact support, \(w=x\) and \(x\) is constant. If this constant were nonzero, \(\dot y=-x\) would make \(y\) unbounded in time, contradicting compactness. Thus \(x=w=0\). Then \(\dot z=-bz\); two-sided boundedness forces \(z=0\). Finally \(\dot w=dy\) with \(w\equiv0\) forces \(y=0\), and \(u\) is constant. Therefore the support lies in \(\mathcal E\). The converse is immediate because every probability measure supported on the equilibrium line is invariant and has \(\dot x=0\).

If a non-equilibrium compact invariant measure were supported in \(0\le z\le c\), then \(\left(z-c/2\right)^2\le c^2/4\) almost surely, contradicting the strict shell identity. Therefore it gives positive mass to \(z<0\) or \(z>c\).

## Verification
The accompanying `verify.py` independently checks the equilibrium substitution, multiplies the characteristic-polynomial factors, verifies the exact cancellation in \(\dot E\), and verifies the source-parameter specialization using exact rational arithmetic. Its successful output is `VERIFY_OK`.

The proof itself is symbolic and does not infer an infinite-time statement from finite simulation. No numerical trajectory is used to establish the equilibrium set, the moment identities, the equality case, or the excursion barrier.

## Relationship to prior work
The introducing article prints this five-dimensional integer-order system, analyzes its divergence and Lyapunov spectrum, and states only the origin as its equilibrium before proceeding to the fractional-order extension. The present result retains that published vector field but observes that the memristive state is free at equilibrium, producing a full line. It then derives stationary identities that are not consequences of the paper's finite-time Lyapunov calculations.

Line equilibria are a recognized phenomenon in other memristive hyperchaotic models. Pham's 2014 system, for example, has a line equilibrium in one parameter regime, while general work on bifurcations from lines of equilibria studies different vector fields. Those results motivate checking the equilibrium geometry but do not imply the source-specific shell law above.

## Limitations
This result does not claim that the reported hyperchaotic attractor is absent. The four transverse characteristic factors are compatible with the paper's local instability calculation; the correction is that the zero eigenvalue is geometrically explained by a nonisolated equilibrium family. The theorem also does not prove existence, uniqueness, or attraction of any non-equilibrium compact invariant measure.

The stationary shell law applies only to the classical integer-order flow. It is not transferred to the Caputo fractional-order model. A residual literature risk is that the four-dimensional base system cited by the introducing paper may contain related algebraic balances; accessible searches did not reveal the exact equilibrium-line correction plus stationary shell identity for this five-dimensional vector field.

## References
1. F. Yu, W. Zhang, X. Xiao, W. Yao, S. Cai, J. Zhang, C. Wang, and Y. Li, “Dynamic Analysis and Field-Programmable Gate Array Implementation of a 5D Fractional-Order Memristive Hyperchaotic System with Multiple Coexisting Attractors,” *Fractal and Fractional* 8 (2024), 271. DOI: 10.3390/fractalfract8050271.
2. V.-T. Pham, C. Volos, and L. V. Gambuzza, “A Memristive Hyperchaotic System without Equilibrium,” *The Scientific World Journal* (2014), Article 368986. DOI: 10.1155/2014/368986.
3. I. A. Korneev et al., “Subcritical Andronov-Hopf scenario for systems with a line of equilibria,” *Chaos* 31 (2021). DOI: 10.1063/5.0050009.
