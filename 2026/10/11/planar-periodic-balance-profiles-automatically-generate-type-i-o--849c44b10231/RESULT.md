# Planar periodic balance profiles automatically generate type-I oscillatory blow-up
## Finding
Let \(f\in AQH_2(\alpha,k)\), with \(k>0\), satisfy Assumption 4.2 in Matsue's algebraic-dynamical correspondence. Suppose the balance law
\[
Y_0'(\eta)=-\frac1k\Lambda_\alpha Y_0(\eta)+f_{\alpha,k}(Y_0(\eta))
\]
has a nonconstant \(T_\eta\)-periodic solution \(Y_0\) satisfying \(p_\alpha(Y_0(\eta))>0\) for every \(\eta\). Then the phase direction \(Y_0'(\eta)\) and the quasi-homogeneous scaling direction \(\Lambda_\alpha Y_0(\eta)\) are automatically linearly independent. Hence the full Floquet multiplier multiset of the balance-law variational equation is
\[
\{1,e^{T_\eta}\}.
\]
Thus the unit multiplier is simple, the other multiplier is strictly outside the unit circle, and Matsue's periodic-blow-up criterion yields a finite-time type-I periodic blow-up. No separate monodromy or Floquet calculation is needed in dimension two.

## Assumptions and scope
The statement concerns autonomous planar vector fields in the class \(AQH_2(\alpha,k)\) with \(k>0\), under the source's Assumption 4.2. The periodic balance profile must be nonconstant and must satisfy \(p_\alpha(Y_0(\eta))>0\) for every \(\eta\). The positivity condition implies \(\Lambda_\alpha Y_0(\eta)\neq0\). No assertion is made that such a periodic profile exists for every planar vector field.

The conclusion is specific to two phase dimensions. In higher dimensions the two distinguished phase/scaling directions span only a subbundle, and further quotient multipliers remain to be controlled.

## Proof
Write
\[
F(Y)=-\frac1k\Lambda_\alpha Y+f_{\alpha,k}(Y).
\]
Assume, toward a contradiction, that \(Y_0'(\eta)\) and \(\Lambda_\alpha Y_0(\eta)\) are dependent for every \(\eta\). Since \(p_\alpha(Y_0(\eta))>0\), the vector \(\Lambda_\alpha Y_0(\eta)\) never vanishes. Therefore there is a continuous scalar function \(a(\eta)\) such that
\[
Y_0'(\eta)=a(\eta)\Lambda_\alpha Y_0(\eta).
\]
Set
\[
s(\eta)=\exp\!\left(\int_0^\eta a(\xi)\,d\xi\right).
\]
The preceding linear equation gives
\[
Y_0(\eta)=s(\eta)^{\Lambda_\alpha}Y_0(0).
\]
At \(\eta=0\), the balance law gives
\[
f_{\alpha,k}(Y_0(0))=b\,\Lambda_\alpha Y_0(0),\qquad b=a(0)+\frac1k.
\]
By quasi-homogeneity of the principal vector field,
\[
f_{\alpha,k}(s^{\Lambda_\alpha}Y_0(0))
=s^k s^{\Lambda_\alpha}f_{\alpha,k}(Y_0(0))
=b s^k\Lambda_\alpha(s^{\Lambda_\alpha}Y_0(0)).
\]
Substituting \(Y_0(\eta)=s(\eta)^{\Lambda_\alpha}Y_0(0)\) into the balance law and cancelling the nonzero vector \(\Lambda_\alpha Y_0(\eta)\) yields, with \(u=\log s\),
\[
u'=-\frac1k+b e^{ku}.
\]
Because \(Y_0\) is periodic and at least one positively weighted coordinate is nonzero, \(s(T_\eta)=s(0)=1\), so \(u\) is periodic. A scalar autonomous ODE has no nonconstant periodic orbit; hence \(u\) is constant, which forces \(Y_0\) to be constant. This contradicts the hypothesis. Thus the two distinguished directions are independent at some time.

Matsue's Proposition 4.3 and Remark 4.4 then propagate this rank to every time. Corollary 4.5 gives characteristic multipliers \(1\) and \(e^{T_\eta}>1\) on their invariant two-dimensional subbundle. Since the whole phase space is two-dimensional, these are all Floquet multipliers, counted with algebraic multiplicity; they are distinct, so \(1\) is simple. The hypotheses of Theorem 5.1 are therefore automatic. Its conclusion gives a finite-time solution with
\[
y(t)\sim Y_0(-c'\log\theta(t))\,\theta(t)^{-(1/k)\Lambda_\alpha},\qquad \theta(t)=t_{\max}-t,
\]
for some \(c'>0\).

## Verification
The proof uses only the defining balance equation, the componentwise quasi-homogeneity identity
\[
f_{\alpha,k}(s^{\Lambda_\alpha}Y)=s^k s^{\Lambda_\alpha}f_{\alpha,k}(Y),
\]
and the exact invariant-bundle/Floquet statements of Proposition 4.3, Remark 4.4, Corollary 4.5, and Theorem 5.1 of arXiv:2610.05354v1. The critical contradiction is one-dimensional: persistent collinearity would confine the profile to one scaling ray and reduce its motion to the autonomous scalar equation \(u'=-1/k+b e^{ku}\), which cannot support a nonconstant periodic solution.

No numerical experiment or finite enumeration is used to prove the universal claim.

## Relationship to prior work
Matsue's 2026 preprint constructs the phase/scaling invariant subbundle and, under a rank hypothesis, proves that it carries multipliers \(1\) and \(e^{T_\eta}\). Its main periodic-blow-up theorem still assumes that \(1\) is simple and all remaining multipliers avoid the unit circle. In the paper's planar Liénard example, characteristic multipliers are discussed as part of a numerical Floquet computation, and the nontrivial multiplier is then observed to equal \(e^{T_\eta}\).

The present planar argument closes the missing logical step uniformly: a nonconstant periodic balance profile satisfying \(p_\alpha>0\) cannot have its phase direction everywhere parallel to its quasi-homogeneous scaling direction. Therefore the source's rank hypothesis is automatic in two dimensions, and its distinguished multiplier pair exhausts the spectrum. Earlier compactification-based blow-up work establishes that hyperbolic periodic dynamics at infinity can induce finite-time blow-up, but it does not state this balance-law-only planar reduction.

## Limitations
The theorem does not prove existence of a periodic balance profile. It does not remove Assumption 4.2 or the positivity condition \(p_\alpha(Y_0)>0\). It does not extend the automatic spectral conclusion to dimensions at least three, where quotient multipliers remain. It also does not claim optimality or stability properties beyond those forced by the multiplier pair \(\{1,e^{T_\eta}\}\).

## References
1. K. Matsue, *On Algebraic-Dynamical Correspondence of Oscillatory Blow-Up Solutions for ODEs*, arXiv:2610.05354v1, 2026.
2. K. Matsue, *On Blow-Up Solutions of Differential Equations with Poincaré-Type Compactifications*, SIAM Journal on Applied Dynamical Systems 17 (2018), DOI 10.1137/17M1124498.
3. K. Matsue, *Blow-up Behavior for ODEs with Normally Hyperbolic Nature in Dynamics at Infinity*, SIAM Journal on Applied Dynamical Systems 24 (2025), DOI 10.1137/23M1588561.
