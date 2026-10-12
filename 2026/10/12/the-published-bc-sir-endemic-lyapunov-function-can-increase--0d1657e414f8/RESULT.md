# The published BC–SIR endemic Lyapunov function can increase
## Finding
For the autonomous behavior–climate SIR model of Parvez, Kholil, Daniyal-Ur-Rehman, and Aalam, the Volterra function used in the published endemic-stability proof can have positive derivative even when all assumptions of the stated theorem hold. An exact admissible instance has \(\mathcal R_0=34/11>1\), yet the source's Lyapunov function satisfies \(\dot W=2019503/13851000>0\) at an interior state. Therefore the differential inequality asserted as equation (13) is false, and the accompanying Lyapunov–LaSalle proof does not establish global asymptotic stability of the endemic equilibrium.

## Assumptions and scope
Use the constant-climate system
\[
\begin{aligned}
\dot S&=\Lambda-c(B)\frac{SI}{N}-dS+\omega R,\\
\dot I&=c(B)\frac{SI}{N}-(\gamma+d)I,\\
\dot R&=\gamma I-(\omega+d)R,\\
\dot B&=\alpha_0(1-B)+\alpha\frac{I}{N}(1-B)-\eta B,
\end{aligned}
\]
where \(N=S+I+R\) and
\[
c(B)=\beta\bar V(1-\varepsilon B)+\beta_0.
\]
Take
\[
\Lambda=d=1,\quad \gamma=2,\quad \omega=1,\quad
\beta=10,\quad \bar V=1,\quad \varepsilon=\frac45,
\]
\[
\beta_0=0,\quad \alpha_0=\frac1{10},\quad \alpha=5,\quad \eta=1.
\]
All parameters satisfy the nonnegativity and \(d>0\) hypotheses printed with the source theorem. The disease-free behavioral level is \(B_0=1/11\), so
\[
\mathcal R_0=\frac{10(1-(4/5)(1/11))}{3}=\frac{34}{11}>1.
\]
The scope of the finding is the published Lyapunov inequality and the proof that depends on it. It does not assert instability of the endemic equilibrium and does not disprove global convergence by some other argument.

## Proof
The point
\[
x^*=(S^*,I^*,R^*,B^*)=\left(\frac{27}{50},\frac{23}{100},\frac{23}{100},\frac59\right)
\]
is an interior equilibrium. Indeed \(N^*=1\), \(c(B^*)=50/9\), and hence \(c(B^*)S^*=3=\gamma+d\). The remaining equilibrium equations reduce respectively to
\[
1-\frac{69}{100}-\frac{27}{50}+\frac{23}{100}=0,
\qquad
2\frac{23}{100}-2\frac{23}{100}=0,
\]
and
\[
\frac1{10}\frac49+5\frac{23}{100}\frac49-\frac59=0.
\]

The source takes the unweighted four-term Volterra function
\[
W=\sum_{Z\in\{S,I,R,B\}}\left(Z-Z^*-Z^*\log\frac{Z}{Z^*}\right).
\]
For any interior state its exact derivative is
\[
\dot W=\sum_{Z\in\{S,I,R,B\}}\left(1-\frac{Z^*}{Z}\right)\dot Z.
\]
Now evaluate at
\[
x=\left(\frac34,\frac1{100},\frac1{20},\frac{19}{20}\right),
\qquad N=\frac{81}{100}.
\]
Here \(c(B)=12/5\), and direct substitution into the vector field gives
\[
(\dot S,\dot I,\dot R,\dot B)
=\left(\frac5{18},-\frac7{900},-\frac2{25},-\frac{15259}{16200}\right).
\]
Therefore
\[
\dot W=\frac{2019503}{13851000}>0.
\]
By contrast, the right-hand side asserted in equation (13) of the source equals
\[
-d\frac{(S-S^*)^2}{S}
-(\gamma+d)\frac{(I-I^*)^2}{I}
-(\omega+d)\frac{(R-R^*)^2}{R}
-\eta\frac{(B-B^*)^2}{B}
=-\frac{30854209}{1923750}<0.
\]
Thus the claimed upper bound would require a positive number to be at most a negative number. This is an exact contradiction, so equation (13) is not a valid derivative estimate for the displayed \(W\).

## Verification
The standalone verifier reproduces all equilibrium identities and both rational derivative values using exact fraction arithmetic. In particular it checks the model vector field, \(B_0\), \(\mathcal R_0\), the endemic equilibrium, the positive value of \(\dot W\), and the strictly negative value of the proposed upper bound.

## Relationship to prior work
The motivating article explicitly introduces the four-term Volterra function and uses equation (13) as the sign-definite step in its global endemic-stability proof. The present finding isolates an admissible state at which that step fails.

Earlier SIR/SEIR stability literature contains successful Lyapunov constructions under other structures, including the direct Lyapunov approach of Melnik and Korobeinikov and the Dulac-function approach of Dénes and Röst. Those results do not imply equation (13) for this behavior-feedback system: the additional behavioral coordinate changes transmission and introduces cross terms that must be controlled rather than discarded.

## Limitations
The counterexample invalidates the displayed Lyapunov inequality and the proof that relies on it. It does not show that the endemic equilibrium is unstable, does not produce a nonconvergent trajectory, and does not rule out a corrected Lyapunov function or a different global-stability proof. The calculation is for the autonomous constant-climate model used in the source's stability section, not its time-dependent climate simulations.

## References
1. M. M. Parvez, M. I. Kholil, Daniyal-Ur-Rehman, and B. Aalam, “A Behavior-Climate Coupled SIR Model for Dengue Transmission: A Data-Driven Approach for Bangladesh,” *Asia Pacific Journal of Mathematics* 13 (2026), Article 86. DOI: 10.28924/APJM/13-86.
2. S. Melnik and A. Korobeinikov, “Lyapunov functions and global stability for SIR and SEIR models with age-dependent susceptibility,” *Mathematical Biosciences and Engineering* 10 (2013), 369–378. DOI: 10.3934/mbe.2013.10.369.
3. A. Dénes and G. Röst, “Global stability for SIR and SIRS models with nonlinear incidence and removal terms via Dulac functions,” *Discrete and Continuous Dynamical Systems - B* 21 (2016), 1101–1117. DOI: 10.3934/dcdsb.2016.21.1101.
