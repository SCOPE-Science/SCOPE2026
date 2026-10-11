# Ambient-norm perturbations do not stabilize noninjective \(K\)-\(g\)-fusion frames

## Finding
Theorem 3.18 of Huang--Yang claims that a closed-range \(K\) turns a sufficiently small perturbation term of the form
\[
c\|f\|
\]
into a valid \(K\)-\(g\)-fusion stability criterion. The claim is false.

Let
\[
H=\mathbb C^2,\qquad
K=P_{\operatorname{span}\{e_1\}},\qquad
J=\{1\},\qquad
W_1=H,\qquad
v_1=1.
\]
Define
\[
\Lambda_1(xe_1+ye_2)=xe_1
\]
and, for any \(0<\delta<1\),
\[
\Phi_1(xe_1+ye_2)=(x+\delta y)e_1.
\]
Then \(\Lambda\) is a Parseval \(K\)-\(g\)-fusion frame, and the perturbation condition of Theorem 3.18 holds with
\[
a=b=0,\qquad c=\delta.
\]
Nevertheless \(\Phi\) is not a \(K\)-\(g\)-fusion frame.

Indeed, the vector
\[
f_\delta=-\delta e_1+e_2
\]
satisfies
\[
\Phi_1f_\delta=0
\]
but
\[
K^*f_\delta=-\delta e_1\ne0.
\]
Thus no positive lower \(K\)-frame bound exists for \(\Phi\).

The failure persists as \(\delta\downarrow0\), so arbitrarily small perturbations in the ambient operator norm can violate the theorem.

A sufficient repair is to add
\[
W_j\subseteq R(K)
\]
for every index. Under this range condition the proof's Moore--Penrose estimate is applied only where it is valid, and the lower bound printed in the theorem follows.

## Assumptions and scope
The example uses the paper's own definition of a \(K\)-\(g\)-fusion frame. The index set has one element, the sole fusion subspace is all of \(H\), and all operators are finite-dimensional. Hence there are no convergence, measurability, or closed-subspace issues.

The operator \(K\) is an orthogonal projection, so
\[
K^\dagger=K,\qquad
\|K^\dagger\|=1,
\qquad
R(K)=\operatorname{span}\{e_1\}.
\]

The correction concerns Theorem 3.18 and its ambient-norm perturbation term. The paper's preceding Theorem 3.17 uses a \(K^*\)-scaled perturbation term instead and is not contradicted by this example.

## Proof
For
\[
f=xe_1+ye_2
\]
we have
\[
K^*f=xe_1
\]
and
\[
\|\Lambda_1f\|^2=|x|^2=\|K^*f\|^2.
\]
Therefore \(\Lambda\) satisfies
\[
\|K^*f\|^2
\le
\|\Lambda_1f\|^2
\le
\|f\|^2,
\]
so \(A=B=1\) are admissible bounds.

The perturbation is
\[
(\Lambda_1-\Phi_1)(xe_1+ye_2)=-\delta y\,e_1.
\]
Hence
\[
\|(\Lambda_1-\Phi_1)f\|
=
\delta|y|
\le
\delta\|f\|.
\]
Taking
\[
a=b=0,\qquad c=\delta
\]
verifies the displayed perturbation hypothesis. The scalar requirement in Theorem 3.18 becomes
\[
0<\delta<1,
\]
which is exactly our parameter range.

The theorem then predicts the lower bound
\[
(1-\delta)^2\|K^*f\|^2
\le
\|\Phi_1f\|^2.
\]
But for
\[
f_\delta=-\delta e_1+e_2
\]
the right side is zero and the left side is
\[
(1-\delta)^2\delta^2>0.
\]
Thus the conclusion is false.

For the sufficient repair, suppose now that \(K\) has closed range and that
\[
W_j\subseteq R(K)
\]
for every \(j\). Given \(f\in H\), set
\[
g=P_{R(K)}f.
\]
Since \(R(K)^\perp=N(K^*)\),
\[
K^*g=K^*f.
\]
Also \(\pi_{W_j}f=\pi_{W_j}g\), so all \(\Lambda\)-energies, \(\Phi\)-energies, and perturbation energies at \(f\) equal those at \(g\).

For \(g\in R(K)\), the Moore--Penrose identities give
\[
g=(K^\dagger)^*K^*g
\]
and therefore
\[
\|g\|\le \|K^\dagger\|\,\|K^*g\|.
\]
Applying the hypothesis of Theorem 3.18 to \(g\), then reversing the triangle estimate as in Theorem 3.17, yields
\[
(1+b)E_\Phi(g)^{1/2}
\ge
(1-a)E_\Lambda(g)^{1/2}-c\|g\|,
\]
where
\[
E_\Lambda(g)
=
\sum_jv_j^2\|\Lambda_j\pi_{W_j}g\|^2
\]
and \(E_\Phi\) is defined analogously. Since
\[
E_\Lambda(g)^{1/2}\ge\sqrt A\,\|K^*g\|,
\]
we obtain
\[
E_\Phi(f)^{1/2}
=
E_\Phi(g)^{1/2}
\ge
\frac{(1-a)\sqrt A-c\|K^\dagger\|}{1+b}
\|K^*f\|.
\]
Squaring gives the claimed repaired lower bound. The upper estimate follows from the same triangle inequality used in the source and does not require the Moore--Penrose conversion.

## Verification
The complete open-access article was inspected at Definition 2.3, Lemma 2.10, Theorems 3.17 and 3.18, and the displayed proof of Theorem 3.17 to which Theorem 3.18 refers.

The PDF page containing Theorem 3.18 was inspected visually. It states the perturbation term \(c\|f\|\), assumes only that \(K\) has closed range, and claims the positive lower bound
\[
\left(
\frac{(1-a)\sqrt A-c\|K^\dagger\|}{1+b}
\right)^2.
\]

The paper itself records the Moore--Penrose identity needed for the estimate only on the range of \(K\). The counterexample uses \(K\) equal to an orthogonal projection, so all pseudo-inverse calculations are exact.

No numerical experiment is used.

## Relationship to prior work
The target paper's Theorem 3.17 uses a perturbation term proportional to
\[
\|K^*f\|,
\]
which directly controls the relevant seminorm and does not suffer from the ambient-null-direction cancellation above. Theorem 3.18 replaces that term by \(c\|f\|\) and attempts to compensate with \(\|K^\dagger\|\); the compensation is valid only after restricting to \(R(K)\).

Hua--Huang's 2016 paper *\(K\)-\(g\)-frames and stability of \(K\)-\(g\)-frames in Hilbert spaces* is a highly relevant predecessor cited by the target article. Its public bibliographic record and abstract were checked, but the full theorem text was not available through the checked open sources, so no whole-document noncoverage claim is made for it.

Targeted searches using the exact article title, theorem number, ambient-norm perturbation, Moore--Penrose factor, closed-range formulation, and correction terminology did not locate an indexed erratum or a published counterexample to Theorem 3.18.

## Limitations
The finding refutes Theorem 3.18 as stated and proves one simple sufficient repair.

The range condition
\[
W_j\subseteq R(K)
\]
is not claimed necessary. More general repairs can require the analysis maps to annihilate \(R(K)^\perp\), or can formulate perturbation size directly in the \(K^*\)-seminorm.

A highly relevant 2016 predecessor could not be inspected theorem-by-theorem from the checked public sources; it remains a residual literature risk.

## References
1. Y. Huang and Y. Yang, *\(K\)-\(g\)-fusion frames in Hilbert spaces*, Journal of Inequalities and Applications 2020, Article 57, DOI 10.1186/s13660-020-02320-0.
2. D. Hua and Y. Huang, *\(K\)-\(g\)-frames and stability of \(K\)-\(g\)-frames in Hilbert spaces*, Journal of the Korean Mathematical Society 53(6) (2016), 1331--1345, DOI 10.4134/JKMS.j150499.
