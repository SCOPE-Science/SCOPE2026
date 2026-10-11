# A quantitative BCAP obstruction for nonuniform semigroups under Calkin nilpotence

## Finding
Let \(X\) be a real or complex Banach space and suppose that there is \(m\in\mathbb N\) such that
\[
a^m=0\qquad\text{for every noninvertible }a\in\operatorname{Cal}(X),
\]
where \(\operatorname{Cal}(X)=\mathcal L(X)/\mathcal K(X)\). Define
\[
\beta_{\mathcal K}(X)=\inf\Bigl\{{C\ge1:\text{ compact operators of norm at most }C\text{ approximate }I_X\text{ uniformly on every compact subset}}\Bigr\},
\]
with \(\beta_{\mathcal K}(X)=\infty\) if no finite bound exists.

If \((T(t))_{t\ge0}\) is a \(C_0\)-semigroup on \(X\) with unbounded infinitesimal generator, then
\[
\beta_{\mathcal K}(X)\le
\left(\limsup_{t\downarrow0}\|T(t)\|\right)^m.
\]
In particular,
\[
\limsup_{t\downarrow0}\|T(t)\|\ge \beta_{\mathcal K}(X)^{1/m}
\]
and, since \(\|T(t)-I_X\|\ge \|T(t)\|-1\),
\[
\limsup_{t\downarrow0}\|T(t)-I_X\|
\ge \beta_{\mathcal K}(X)^{1/m}-1.
\]
The recent Calkin criterion for the Lotz property is recovered when \(\beta_{\mathcal K}(X)=\infty\): then an unbounded generator is impossible. For finite \(\beta_{\mathcal K}(X)>1\), the same mechanism yields a quantitative operator-norm jump rather than only a qualitative contradiction.

## Assumptions and scope
The exponent \(m\) is fixed uniformly over all noninvertible elements of the Calkin algebra. The compact-approximation coefficient uses the same convention as the focal source: the approximating compact operators themselves have norm at most \(C\). This differs from another convention in the approximation-property literature that controls \(\|I-K\|\).

No analyticity, positivity, reflexivity, or weak compact generation is assumed for the semigroup. The conclusion is conditional on the Calkin nilpotence hypothesis and concerns the short-time operator norms of a strongly continuous semigroup with unbounded generator.

## Proof
Put
\[
L=\limsup_{t\downarrow0}\|T(t)\|.
\]
Strong continuity and the uniform boundedness principle imply that \(L<\infty\). Also \(L\ge1\), because \(T(t)x\to x\) for every unit vector \(x\).

Fix \(c>L\). By the definition of the limsup, there is \(\delta>0\) such that
\[
\|T(t)\|\le c\qquad(0\le t\le\delta).
\]
For \(t=n\delta+r\), where \(n\in\mathbb N_0\) and \(0\le r<\delta\), the semigroup law gives
\[
\|T(t)\|\le \|T(\delta)\|^n\|T(r)\|\le c^{n+1}.
\]
Hence, with \(\omega=(\log c)/\delta\),
\[
\|T(t)\|\le c e^{\omega t}\qquad(t\ge0).
\]
Thus the usual semigroup growth estimate is available with prefactor exactly \(c\).

Let \(A\) be the generator and, for real \(\lambda>\max\{\omega,0\}\), let
\[
R(\lambda,A)=(\lambda I_X-A)^{-1},
\qquad
J_\lambda=\lambda R(\lambda,A).
\]
Because \(A\) is unbounded, \(D(A)\ne X\). The resolvent \(R(\lambda,A)\) is injective with range \(D(A)\). If it were Fredholm, its range would be closed; since \(D(A)\) is dense, this would force \(D(A)=X\), contradicting unboundedness by the closed graph theorem. Therefore \(R(\lambda,A)\) is not Fredholm.

Atkinson's theorem now says that the Calkin class of \(R(\lambda,A)\) is noninvertible. By the uniform nilpotence assumption,
\[
R(\lambda,A)^m\in\mathcal K(X),
\]
so
\[
J_\lambda^m\in\mathcal K(X).
\]
The Yosida approximants satisfy \(J_\lambda x\to x\) for every \(x\in X\). Since they are uniformly bounded on every sufficiently far tail, the identity
\[
J_\lambda^m-I_X=(I_X+J_\lambda+\cdots+J_\lambda^{m-1})(J_\lambda-I_X)
\]
shows that \(J_\lambda^m x\to x\) strongly.

The growth bound above yields the sharper asymptotic estimate
\[
\|J_\lambda\|
\le c\frac{\lambda}{\lambda-\omega}
\longrightarrow c
\qquad(\lambda\to\infty).
\]
Therefore, for every \(\eta>0\), a sufficiently far tail of the compact approximants \(J_\lambda^m\) has norm at most \((c+\eta)^m\) and converges strongly to the identity. Uniform boundedness plus strong convergence makes the convergence uniform on every compact subset. Consequently
\[
\beta_{\mathcal K}(X)\le(c+\eta)^m.
\]
Letting \(\eta\downarrow0\), then \(c\downarrow L\), gives
\[
\beta_{\mathcal K}(X)\le L^m.
\]
The two displayed lower bounds follow immediately.

## Verification
The critical implication was replayed from the actual hypotheses used in the focal Calkin proof: non-Fredholmness of each resolvent for an unbounded generator, Atkinson's theorem, uniform nilpotence in the Calkin algebra, compactness of the powered Yosida approximants, and strong convergence of those approximants. The only new quantitative step is to retain the asymptotically sharp estimate
\[
\|J_\lambda\|\le c\frac{\lambda}{\lambda-\omega}
\]
instead of replacing it by a coarse tail bound, and then optimize the admissible semigroup prefactor \(c\) down to the intrinsic short-time limsup \(L\).

No numerical experiment is used. The proof does not assert that equality must occur, nor that every value of \(\beta_{\mathcal K}(X)\) is realized under the Calkin hypothesis.

## Relationship to prior work
Araújo, Azevedo, Bezerra, and Barbosa prove that if \(X\) fails the bounded compact approximation property and every noninvertible Calkin element has a fixed nilpotent power, then every \(C_0\)-semigroup on \(X\) is uniformly continuous. Their proof constructs the compact approximants \(J_\lambda^m\) and records a convenient uniform estimate obtained from a semigroup growth bound. Their later discussion explicitly notes the qualitative implication “unbounded generator implies BCAP.” The present result keeps the approximation constant and optimizes the semigroup growth prefactor, obtaining the intrinsic inequality involving \(\limsup_{t\downarrow0}\|T(t)\|\).

Chen and Ruan study quantitative characterizations of BCAP using semi-Fredholm operational quantities. That work supplies nearby quantitative approximation-property context but does not formulate a \(C_0\)-semigroup, Yosida, or Calkin-nilpotence norm-jump theorem in the inspected material.

## Limitations
The result is a one-sided obstruction. It does not prove sharpness of the exponent \(1/m\), does not construct semigroups attaining the lower bound, and gives no extra numerical information when \(\beta_{\mathcal K}(X)=1\). The coefficient depends on the chosen equivalent norm on \(X\), as do the operator norms of the semigroup. An equivalent theorem could conceivably be implicit in older semigroup or approximation-property literature under different terminology; targeted searches did not locate one.

## References
1. G. Araújo, M. Azevedo, F. Bezerra, and A. Barbosa, *The Lotz Property in Weakly Compactly Generated Spaces*, arXiv:2609.38396v1, 2026.
2. D. Y. Chen and Y. B. Ruan, *Quantitative Characterizations of Bounded Compact Approximation Property by Semi-Fredholm Operators*, Acta Mathematica Sinica, English Series 39 (2023), 1115–1128, DOI: 10.1007/s10114-023-1007-3.
