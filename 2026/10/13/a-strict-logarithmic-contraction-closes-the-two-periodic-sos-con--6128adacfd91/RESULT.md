# A strict logarithmic contraction closes the two-periodic SOS conjecture
## Finding
For the invariant boundary-law branch \(I=\{(u,v):v=1\}\) of the three-state SOS model with nearest-neighbor and one-level next-nearest-neighbor interactions on the binary Cayley tree, there is no pure two-periodic Gibbs measure for any \(\theta>0\) and \(\theta_1>0\).

Equivalently, for
\[
f(u)=\frac{u^2+4\theta\theta_1u+2\theta^2(\theta_1^2+1)}
{\theta^2u^2+2\theta\theta_1(\theta^2+1)u+\theta^4+2\theta^2\theta_1^2+1},
\qquad u>0,
\]
the equation \(f(f(u))=u\) has no solution with \(f(u)\ne u\). This proves Conjecture 1 of the source on the stated invariant set.

## Assumptions and scope
The parameters satisfy \(\theta>0\) and \(\theta_1>0\). The claim concerns only the invariant set \(I\) used in the source. The source proves that positive nonfixed solutions of \(f(f(u))=u\) on this set are exactly the pure two-periodic boundary laws under consideration.

Write
\[
N(u)=u^2+4\theta\theta_1u+2\theta^2(\theta_1^2+1)
\]
and
\[
Q(u)=\theta^2u^2+2\theta\theta_1(\theta^2+1)u+\theta^4+2\theta^2\theta_1^2+1.
\]
Both are strictly positive for \(u>0\).

## Proof
Direct differentiation gives
\[
f'(u)=-\frac{2(\theta^2-1)P(u)}{Q(u)^2},
\]
where
\[
P(u)=2\theta^3\theta_1^3+2\theta^2\theta_1^2u+\theta\theta_1u^2
+2\theta\theta_1+\theta^2u+u.
\]
Every term of \(P\) is positive.

If \(0<\theta<1\), then \(f\) is strictly increasing. A strictly increasing self-map of an interval has no nontrivial two-cycle: if \(u<v=f(u)\), then \(f(u)<f(v)=u\), a contradiction, and the case \(v<u\) is symmetric.

If \(\theta=1\), then \(N(u)=Q(u)\), so \(f(u)=1\) for every \(u>0\); again there is no nontrivial two-cycle.

It remains to treat \(\theta>1\). Put
\[
g(x)=\log f(e^x),\qquad x\in\mathbb R,
\]
and set \(u=e^x\). Then
\[
g'(x)=\frac{u f'(u)}{f(u)}=
-\frac{2u(\theta^2-1)P(u)}{N(u)Q(u)}.
\]
The numerator is positive. Moreover,
\[
N(u)Q(u)-2u(\theta^2-1)P(u)=R(u,\theta,\theta_1),
\]
where
\[
\begin{aligned}
R={}&\theta^2u^4+4\theta^3\theta_1u^3+4\theta\theta_1u^3
+6\theta^4\theta_1^2u^2+\theta^4u^2+14\theta^2\theta_1^2u^2+3u^2\\
&+8\theta^5\theta_1u+16\theta^3\theta_1^3u+8\theta\theta_1u\\
&+2\theta^6\theta_1^2+2\theta^6+4\theta^4\theta_1^4
+4\theta^4\theta_1^2+2\theta^2\theta_1^2+2\theta^2.
\end{aligned}
\]
All coefficients are positive, hence \(R>0\) whenever \(u,\theta,\theta_1>0\). Therefore
\[
-1<g'(x)<0
\]
for every \(x\in\mathbb R\) when \(\theta>1\).

Suppose a nontrivial two-cycle existed. Write \(v=f(u)\), \(u=f(v)\), \(x=\log u\), and \(y=\log v\). Then \(x\ne y\), \(y=g(x)\), and \(x=g(y)\). The mean value theorem gives some \(\xi\) between \(x\) and \(y\) with
\[
y-x=g(x)-g(y)=-g'(\xi)(y-x).
\]
Division by \(y-x\ne0\) yields \(1=-g'(\xi)\), contradicting \(0<-g'(\xi)<1\). Thus no nontrivial positive two-cycle exists.

## Verification
The derivative factorization and the positive-polynomial identity above were expanded independently and checked exactly. The bundled `verify.py` uses rational arithmetic to replay these identities over a deterministic family of positive rational parameter triples, checks the \(\theta=1\) degeneration, and checks the strict logarithmic-slope inequalities for representative \(\theta>1\) cases. These finite checks corroborate the algebra; the proof of the universal statement is the displayed exact identity plus the order/mean-value arguments.

## Relationship to prior work
Rahmatullaev and Karshiboev introduced this invariant scalar map in arXiv:2307.02235v1 and reduced pure two-periodic Gibbs measures on \(I\) to nonfixed solutions of \(f(f(u))=u\). Their 2023 preprint and the 2025 journal version prove nonexistence only on the parameter region where a quadratic coefficient \(B\) is nonnegative. For the complementary region they report a computer analysis of a discriminant set and leave the global statement as Conjecture 1. The 2025 journal version still states that conjecture explicitly.

The nearest-neighbor three-state SOS work of Külske and Rozikov concerns a Hamiltonian without the one-level competing interaction and classifies translation-invariant phases; it does not imply the present period-two exclusion for the two-interaction map. The external-field periodic-SOS literature uses a different Hamiltonian and does admit a distinct period-two analysis.

## Limitations
The result is restricted to the invariant set \(I=\{(u,v):v=1\}\). It does not exclude two-periodic Gibbs measures outside \(I\), a possibility explicitly left open by the source. It also does not classify higher periods, extremality, reconstruction, or thermodynamic dominance.

## References
1. M. M. Rahmatullaev and O. Sh. Karshiboev, *The phase transition for the three-state SOS model with one-level competing interactions on the binary tree*, arXiv:2307.02235v1, 2023.
2. O. Sh. Karshiboev and M. M. Rahmatullaev, *The phase transition for the three-state SOS model with one-level competing interactions on the binary tree*, Nanosystems: Physics, Chemistry, Mathematics 16(2), 134–141, 2025, DOI:10.17586/2220-8054-2025-16-2-134-141.
3. C. Külske and U. A. Rozikov, *Extremality of translation-invariant phases for a three-state SOS-model on the binary tree*, Journal of Statistical Physics 160, 659–680, 2015, DOI:10.1007/s10955-015-1279-9.
4. O. Sh. Karshiboev, *Periodic Gibbs measures for the three-state SOS model on a Cayley tree with a translation-invariant external field*, Theoretical and Mathematical Physics 212, 2022.
