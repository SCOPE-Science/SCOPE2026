# Exact binary step-reinforcement mixing profile and its sharp cubic specialization

## Finding

Consider a walk on \(\mathbb Z/2\mathbb Z\) whose first increment is fair, and whose subsequent increments either independently resample a fair bit or copy a uniformly selected previous increment. Let the copying probability be \(\alpha\in(0,1)\), and write \(S_n\) for the sum of the first \(n\) increments modulo two. Define the parity bias and total-variation distance by
\[
q_n=\mathbb E[(-1)^{S_n}],\qquad d_n=\|\mathcal L(S_n)-U_2\|_{\rm TV}=q_n/2,
\]
where \(U_2\) is uniform on two points. The sign \(q_n\ge0\) follows from the proof below.

**General exact profile.** The unique formal power series \(A(z),B(z)\), both with zero constant term, satisfying
\[
A'(z)=e^{A(z)}\sinh(\alpha B(z)),\qquad
B'(z)=e^{A(z)}\cosh(\alpha B(z))
\]
determine every marginal exactly through
\[
q_n=n[z^n]A(z),\qquad n\ge1.
\]
Equivalently, with the inverse relation \(B=B(z)\),
\[
A=\frac1\alpha\log\cosh(\alpha B),\qquad
z=\int_0^B\cosh(\alpha t)^{-1-1/\alpha}\,dt.
\]
Every odd-time marginal is uniform; at every positive even time the marginal is nonuniform.

**Sharp explicit profile at \(\alpha=1/3\).** For every integer \(m\ge1\),
\[
\boxed{q_{2m}=3^{1-2m}\sum_{j=0}^{m-1}\frac{1}{3^j}\binom{2m+j-1}{j},\qquad q_{2m+1}=0.}
\]
Moreover,
\[
\boxed{d_{2m}=\frac{q_{2m}}2\sim\frac34\,4^{-m}\quad(m\to\infty),\qquad d_{2m+1}=0.}
\]
Thus the binary marginal becomes exactly uniform at every odd time while showing a positive, sharply quantified even-time departure. The exponential rate \(4^{-m}\) and its leading constant are both exact.

## Assumptions and scope

Write \(X_1\in\{0,1\}\) for a uniform bit. Independently at each \(n\ge2\), with probability \(1-\alpha\) set \(X_n\) equal to a fresh uniform bit, and with probability \(\alpha\) set \(X_n=X_{J_n}\), where \(J_n\) is uniform on \(\{1,\dots,n-1\}\). All fresh bits and all mechanism choices are independent. Then \(S_n=\sum_{i=1}^nX_i\pmod2\). The formula covers every integer \(n\ge1\) and every fixed \(0<\alpha<1\); the elementary closed sum and sharp leading constant are asserted at \(\alpha=1/3\).

The result concerns one-time marginals, not independence across odd times or a total-variation mixing time under a monotone-in-time convention. It does not assert analogous closed sums for other groups or copying parameters.

## Proof

**1. The parity forest.** Independently of the fresh bit labels, form a random recursive forest on vertices \(1,\ldots,n\). At arrival \(j\ge2\), choose a uniformly random older vertex; retain the edge to it with probability \(\alpha\), or delete that edge with probability \(1-\alpha\). Each forest component receives the fresh fair bit assigned at its first vertex. The increment sequence is then the component-label sequence, because a retained edge copies its ancestor's label and a deleted edge creates a fresh label. This is the standard random-recursive-forest representation of reinforced steps.

Conditional on the forest, a component of size \(k\) contributes the \(k\)-fold multiple of its fair bit to \(S_n\). Consequently,
\[
\mathbb E[(-1)^{S_n}\mid\mathscr F_n]
=\prod_{C\in\mathscr F_n}\mathbb E[(-1)^{|C|X_C}]
=\mathbf1_{\{|C|\text{ is even for every component }C\}}.
\]
Therefore \(q_n\) is **exactly** the probability that every percolation component has even size. In particular \(q_n=0\) for odd \(n\). For even \(n\), the all-edges-retained event has probability \(\alpha^{n-1}>0\), so \(q_n>0\). Fourier inversion on two points yields \(\Pr(S_n=0)=(1+q_n)/2\), and hence \(d_n=q_n/2\).

**2. Increasing-tree generating functions.** Every increasing rooted tree on labels \(\{1,\ldots,n\}\) occurs with probability \(1/(n-1)!\) in the underlying recursive-tree model. Mark retained edges by \(\alpha\) and deleted edges by \(1-\alpha\). Let \(a_n\) and \(b_n\) be the total weights over decorated increasing trees of size \(n\) in which every component not containing the root has even size, and the root component is respectively even or odd. Define
\[
A(z)=\sum_{n\ge1}a_n\frac{z^n}{n!},\qquad
B(z)=\sum_{n\ge1}b_n\frac{z^n}{n!}.
\]
The desired event has weighted count \(a_n\), so \(q_n=a_n/(n-1)!=n[z^n]A(z)\).

An increasing rooted tree consists of its minimal root and an unordered labeled set of attached increasing subtrees. A cut parent edge requires the attached subtree's root component to be even and contributes \((1-\alpha)A\); a retained edge allows either parity and contributes \(\alpha(A+yB)\), where \(y\in\{1,-1\}\) marks root-component parity. The attached-subtree series therefore totals \(A+\alpha yB\). The root itself contributes parity \(y\). The increasing-tree root decomposition, with differentiation removing the minimum label, gives the pair of exact formal identities
\[
(A+yB)'=y\exp(A+\alpha yB),\qquad y\in\{1,-1\}.
\]
Adding and subtracting these two identities proves
\[
A'=e^A\sinh(\alpha B),\qquad B'=e^A\cosh(\alpha B).
\]
Both series have unique coefficients by recursion from \(A(0)=B(0)=0\); in particular \(B'(0)=1\). Dividing the differential equations gives \(dA/dB=\tanh(\alpha B)\), and integrating with zero initial value gives \(A=\alpha^{-1}\log\cosh(\alpha B)\). It follows that \(B'=\cosh(\alpha B)^{1+1/\alpha}\), yielding the claimed inverse integral. These manipulations are valid in formal power series at zero, so no analytic continuation assumption is needed for the coefficient identity.

**3. A cubic inverse and the closed sum.** Set \(\alpha=1/3\) and \(u=\tanh(B/3)\). The inverse integral from the preceding step simplifies to
\[
\frac{dz}{du}=3(1-u^2),\quad z=3u-u^3,\quad
A(z)=-\frac32\log(1-u(z)^2),\quad u(0)=0.
\]
Lagrange--Bürmann inversion, using the fact that \(z=u(3-u^2)\), gives for every \(m\ge1\),
\[
q_{2m}=2m[z^{2m}]A(z)
=3[v^{m-1}](1-v)^{-1}(3-v)^{-2m}
=3^{1-2m}\sum_{j=0}^{m-1}3^{-j}\binom{2m+j-1}{j}.
\]
The substitution \(v=u^2\) was used in the coefficient extraction. This is an equality of exact rational numbers for every positive integer \(m\), not an extrapolation from computations.

**4. The sharp exponential constant.** Let \(N_m\) count failures before \(2m\) successes in independent Bernoulli trials of success probability \(2/3\). Its mass function is
\[
\Pr(N_m=j)=\binom{2m+j-1}{j}\left(\frac23\right)^{2m}\left(\frac13\right)^j,
\qquad j\ge0.
\]
The closed sum becomes \(q_{2m}=3\,4^{-m}\Pr(N_m\le m-1)\). Writing \(N_m\) as a sum of \(2m\) iid geometric-failure counts, its mean is \(m\) and its variance is \(3m/2\). The classical central limit theorem therefore gives \(\Pr(N_m\le m-1)\to1/2\). Thus \(q_{2m}\sim(3/2)4^{-m}\), and \(d_{2m}\sim(3/4)4^{-m}\), as claimed.

## Verification

The included `verify_binary_step_reinforced.py` uses only exact rational arithmetic and the Python standard library. Its 60 coefficient checks compare the Lagrange coefficient extraction with a separate dynamic recursion for the exact percolation-component-size process, at five rational copying parameters and lengths \(1\) through \(12\). Thirty additional checks directly enumerate the actual reinforced increment histories at three parameters through length \(10\). Six cases compare the independent closed binomial sum at \(\alpha=1/3\) with the forest probabilities. The executed verifier reported:

`VERIFY_OK coefficient_cases=60 direct_history_cases=30 closed_one_third_cases=6 odd_uniform=PASS even_nonuniform=PASS`

These finite checks verify the stated arithmetic and the coupling in small cases; the formal generating-function proof and the central limit theorem establish the infinite identities and asymptotic constant.

## Relationship to prior work

Peres and Qin, *Mixing times of step-reinforced random walks* (arXiv:2604.07207v1, first public 2026-04-08), establish exponential convergence on finite groups and show that even the uniform two-element group can have a nonmonotone distance to stationarity. Their Section 2 and equation (17) give the recursive-forest representation from which the parity-event identity in Step 1 follows. **That representation and the odd/even parity observation are prior-method consequences, not the claimed new contribution.** The result here additionally evaluates the all-even forest-component probability by a coupled increasing-tree differential system and obtains a complete rational profile and sharp leading constant at \(\alpha=1/3\); those formulas do not follow from the source's mixing bound without the additional enumeration and inversion.

Peres and Qin, *Transition probabilities of step-reinforced random walks* (arXiv:2604.07227v1, 2026-04-08), treat general group transition-probability bounds via recursive forests and evolving sets rather than an exact parity-probability generating function. Kürsten, *Random Recursive Trees and the Elephant Random Walk* (arXiv:1512.05275v1, first posted 2015-12-16), develops the recursive-tree coupling and computes several cluster-size moments; it does not supply the all-even-component enumeration or the sharp binary marginal profile here. These works provide the mathematical setting and important tools.

## Limitations

The exact binomial sum and sharp exponential constant are shown at \(\alpha=1/3\); the coupled formal generating functions apply at any \(0<\alpha<1\) but no equally simple expression is claimed for general parameters. The calculation identifies one-time marginals and not multi-time joint distributions or cutoff in a growing family of groups. The parameter \(1/3\) is the smallest nontrivial reciprocal of an odd integer for which the inverse-integral substitution becomes a nonconstant polynomial; this motivates the cubic specialization rather than an arbitrary numerical slice. Equivalent formulations in enumerative probability or Yule--Simon forest models remain possible.

## References

- Y. Peres and S. Qin, *Mixing times of step-reinforced random walks*, arXiv:2604.07207v1 (2026-04-08), especially Definition 1.1, Example 1.1, Proposition 2.1, equation (17), and Section 4.5.
- Y. Peres and S. Qin, *Transition probabilities of step-reinforced random walks*, arXiv:2604.07227v1 (2026-04-08), especially Sections 1 and 2.
- R. Kürsten, *Random Recursive Trees and the Elephant Random Walk*, arXiv:1512.05275v1 (2015-12-16), especially Sections II--IV.
