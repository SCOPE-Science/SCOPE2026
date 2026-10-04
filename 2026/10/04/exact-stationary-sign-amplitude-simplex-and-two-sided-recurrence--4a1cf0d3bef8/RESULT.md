# Exact stationary sign-amplitude simplex and two-sided recurrence in the Lozi map
## Finding
Consider the Lozi homeomorphism
\[
L_{a,b}(x,y)
=
\bigl(1+y-a|x|,\;bx\bigr),
\]
with
\[
0<b<1,
\qquad
a>1-b.
\]

Its two fixed points have \(x\)-coordinates
\[
r_+
=
\frac{1}{1+a-b}
>0
\]
and
\[
r_-
=
-\frac{1}{a+b-1}
<0.
\]

For
\[
x_+=\max(x,0),
\qquad
x_-=\max(-x,0),
\]
every compactly supported invariant probability measure \(\mu\) satisfies the exact sign-amplitude simplex
\[
\frac{\mathbb E_\mu[x_+]}{r_+}
+
\frac{\mathbb E_\mu[x_-]}{-r_-}
=
1.
\]
Equivalently,
\[
a\,\mathbb E_\mu[|x|]
+
(1-b)\mathbb E_\mu[x]
=
1.
\]

If
\[
m=\mathbb E_\mu[x],
\]
then
\[
r_-\le m\le r_+.
\]
The upper endpoint is attained only by the positive fixed-point atom, and the lower endpoint only by the negative fixed-point atom.

Every other compact invariant probability measure satisfies
\[
\mu\{x>0\}>0,
\qquad
\mu\{x<0\}>0,
\]
and therefore
\[
r_-<m<r_+.
\]

The second coordinate has an exact marginal relation:
\[
y_\#\mu=(bx)_\#\mu.
\]
In particular,
\[
\mathbb E_\mu[y]
=
b\,\mathbb E_\mu[x],
\qquad
\mathbb E_\mu[|y|]
=
b\,\mathbb E_\mu[|x|],
\]
and
\[
\operatorname{Var}_\mu(y)
=
b^2\operatorname{Var}_\mu(x).
\]

For Lozi's classical parameters
\[
(a,b)=\left(\frac{17}{10},\frac12\right),
\]
the fixed-point coordinates are
\[
r_+=\frac5{11},
\qquad
r_-=-\frac56,
\]
and the simplex becomes
\[
11\,\mathbb E[x_+]
+
6\,\mathbb E[x_-]
=
5.
\]
Thus every stationary state other than one of the two fixed-point atoms obeys
\[
-\frac56
<
\mathbb E[x]
<
\frac5{11}
\]
and necessarily uses both symbols of the standard left/right Lozi itinerary.

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under \(L_{a,b}\) and supported on a compact subset of \(\mathbb R^2\).

The parameter assumptions
\[
0<b<1,
\qquad
a>1-b
\]
are broader than the classical robust-chaos region. They guarantee that the two displayed fixed points exist in opposite half-planes and that each affine half-plane branch has one eigenvalue inside and one outside the unit circle.

Because
\[
b\ne0,
\]
the Lozi map is a homeomorphism. Hence the support of an invariant probability measure is invariant in both forward and backward time.

The original Lozi map was published in August 1978. The earliest explicit day-level bibliographic record located for that publication gives 1 August 1978.

The sign partition
\[
x<0,\qquad x>0
\]
is the standard symbolic partition used in the Lozi-map literature. This makes the two-sided recurrence conclusion intrinsic to the established symbolic-dynamics framework rather than an arbitrary coordinate slice.

## Proof
Invariance of the first coordinate gives
\[
\mathbb E[x]
=
1+\mathbb E[y]-a\mathbb E[|x|].
\]
Invariance of the second coordinate gives
\[
\mathbb E[y]
=
b\mathbb E[x].
\]
Therefore
\[
a\mathbb E[|x|]
+
(1-b)\mathbb E[x]
=
1.
\]

Write
\[
P=\mathbb E[x_+],
\qquad
N=\mathbb E[x_-].
\]
Then
\[
\mathbb E[|x|]=P+N,
\qquad
\mathbb E[x]=P-N.
\]
Substitution gives
\[
(a+1-b)P
+
(a-1+b)N
=
1.
\]
Since
\[
\frac1{r_+}=a+1-b,
\qquad
\frac1{-r_-}=a-1+b,
\]
this is exactly
\[
\frac{P}{r_+}
+
\frac{N}{-r_-}
=
1.
\]

Both coefficients are positive. Hence
\[
P\le r_+,
\qquad
N\le -r_-.
\]
For
\[
m=P-N,
\]
we obtain
\[
m\le P\le r_+
\]
and
\[
m\ge -N\ge r_-.
\]

It remains to classify equality and one-sided stationary states.

Suppose first that
\[
N=0.
\]
Then
\[
x\ge0
\]
almost surely, so the invariant support lies in the closed right half-plane. On that half-plane the map is affine:
\[
u_{n+1}=A_+u_n+e,
\qquad
A_+
=
\begin{pmatrix}
-a&1\\
b&0
\end{pmatrix},
\qquad
e=
\binom10.
\]
After translation by the positive fixed point, every support orbit satisfies
\[
v_{n+1}=A_+v_n
\]
for all
\[
n\in\mathbb Z.
\]

The characteristic polynomial is
\[
q_+(\lambda)
=
\lambda^2+a\lambda-b.
\]
Because
\[
q_+(0)=-b<0,
\qquad
q_+(1)=1+a-b>0,
\]
one eigenvalue lies in
\[
(0,1).
\]
Also
\[
q_+(-1)=1-a-b<0
\]
because
\[
a+b>1,
\]
while
\[
q_+(\lambda)\to+\infty
\]
as
\[
\lambda\to-\infty.
\]
Thus the other eigenvalue is less than
\[
-1.
\]

A bi-infinite bounded orbit of this hyperbolic linear map must have zero components in both eigendirections: forward boundedness kills the unstable component and backward boundedness kills the stable component. Hence
\[
v_n=0
\]
for all \(n\), so the support is the positive fixed point. Therefore
\[
N=0
\]
forces the positive fixed-point atom.

The same argument in the left half-plane uses
\[
A_-
=
\begin{pmatrix}
a&1\\
b&0
\end{pmatrix}
\]
with characteristic polynomial
\[
q_-(\lambda)
=
\lambda^2-a\lambda-b.
\]
Now
\[
q_-(0)<0,
\qquad
q_-(1)=1-a-b<0,
\qquad
q_-(-1)=1+a-b>0.
\]
Thus one eigenvalue lies in
\[
(-1,0)
\]
and the other exceeds
\[
1.
\]
A compact bi-infinite orbit confined to the left half-plane is therefore the negative fixed point. Hence
\[
P=0
\]
forces the negative fixed-point atom.

Consequently every invariant measure other than the two pure fixed-point atoms has
\[
P>0,
\qquad
N>0.
\]
This is equivalent to positive mass in both open half-planes. The mean bounds are then strict.

Finally, invariance and the second coordinate equation
\[
y'=bx
\]
imply equality of pushforward measures
\[
y_\#\mu=(bx)_\#\mu.
\]
All displayed marginal moment identities follow immediately.

## Verification
The accompanying exact checker verifies the algebraic equivalence
\[
(a+1-b)P+(a-1+b)N
=
a(P+N)+(1-b)(P-N),
\]
the fixed-point reciprocal coefficients, and the classical rational specialization.

For
\[
(a,b)=\left(\frac{17}{10},\frac12\right),
\]
it confirms exactly
\[
r_+=\frac5{11},
\qquad
r_-=-\frac56,
\]
and
\[
(a+1-b)P+(a-1+b)N=1
\iff
11P+6N=5.
\]

The checker also verifies the branch characteristic-polynomial signs
\[
q_+(0)<0<q_+(1),
\qquad
q_+(-1)<0,
\]
and
\[
q_-(0)<0,
\qquad
q_-(1)<0<q_-(-1)
\]
for the classical parameters.

The general eigenvalue placement follows analytically from the same sign pattern under
\[
0<b<1,\qquad a>1-b.
\]
The bounded bi-infinite orbit classification is an analytic hyperbolicity argument, not a finite experiment.

The stored checker output is `VERIFY_OK`.

## Relationship to prior work
Lozi introduced the piecewise-linear Hénon-type map in 1978. Later symbolic-dynamics work records the now-standard normalization
\[
L_{a,b}(x,y)=(1+y-a|x|,bx),
\]
Lozi's classical parameters
\[
(a,b)=(1.7,0.5),
\]
and the two fixed points with the coordinates used above.

Collet and Levy gave a detailed invariant-measure treatment in 1984 for the strange-attractor regime. Their complete article constructs the Bowen–Ruelle measure and proves ergodic, \(K\)-system, Bernoulli, entropy, Lyapunov, and dimension properties. The article does not state the stationary sign-amplitude simplex, fixed-point mean interval, or the one-sided-support rigidity above.

Rychlik's later treatment proves existence and finiteness of SBR measures for Lozi maps and develops a variational principle. The inspected introductory material does not expose the accepted amplitude identity; the complete chapter was not securely available in the source inspected, so no whole-document noncoverage claim is made.

Modern symbolic-dynamics work centers the left/right itinerary relative to the singular line
\[
x=0.
\]
The accepted statement complements that topological coding by showing that every non-fixed compact stationary state must actually use both half-planes and that its first absolute moment is pinned to an exact simplex whose vertices are the two fixed points.

Targeted searches for invariant-measure means, absolute moments, positive/negative parts, sign crossing, and fixed-point amplitude balances did not locate a same-object statement implying the theorem.

## Limitations
The theorem is a stationary constraint. It does not prove existence or uniqueness of the strange attractor or of an SBR measure for every parameter pair satisfying
\[
0<b<1,\qquad a>1-b.
\]

The amplitude simplex controls the first absolute moment and sign use, not the probabilities of the two signs separately.

The complete Rychlik chapter was not available in the inspected source, and a differently phrased elementary moment identity could remain in unindexed Lozi literature.

No novelty is claimed for the Lozi equations, classical parameters, fixed-point coordinates, hyperbolicity of the classical attractor, existence of Bowen–Ruelle or SBR measures, or the established symbolic-dynamics machinery.

## References
1. R. Lozi, “Un attracteur étrange du type attracteur de Hénon,” Journal de Physique Colloques 39, C5-9–C5-10 (1978), DOI 10.1051/jphyscol:1978505.
2. P. Collet and Y. Levy, “Ergodic Properties of the Lozi Mappings,” Communications in Mathematical Physics 93, 461–481 (1984), DOI 10.1007/BF01212290.
3. M. Rychlik, “Invariant Measures and the Variational Principle for Lozi Mappings,” in The Theory of Chaotic Attractors, 190–221, DOI 10.1007/978-0-387-21830-4_13.
4. M. Misiurewicz and S. Štimac, “Symbolic dynamics for Lozi maps,” Nonlinearity 29, 3031–3056 (2016), DOI 10.1088/0951-7715/29/10/3031.
