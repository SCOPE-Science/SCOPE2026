# Three mutually unbiased qubit bases are the unique extremizers of averaged Shannon certainty
## Finding
For three rank-one projective measurements of a qubit, choose unit Bloch axes \(n_1,n_2,n_3\in\mathbb R^3\); changing the sign of an axis does not change its measurement basis. For a pure state with Bloch vector \(r\in S^2\), put
\[
\bar S(r)=\frac13\sum_{j=1}^3 h\!\left(\frac{1+n_j\cdot r}2\right),
\qquad
h(p)=-p\log p-(1-p)\log(1-p),
\]
and define \(B_{\min}=\min_{r\in S^2}\bar S(r)\) and \(B_{\max}=\max_{r\in S^2}\bar S(r)\), using natural logarithms.

Then
\[
B_{\min}\le \frac23\log 2,
\qquad
B_{\max}\ge \beta_*,
\]
where
\[
\beta_*=h\!\left(\frac{1+1/\sqrt3}2\right)
=\frac12\log 6-\frac{1}{2\sqrt3}\log(2+\sqrt3).
\]
Each equality is rigid: \(B_{\min}=\frac23\log2\) if and only if \(B_{\max}=\beta_*\) if and only if \(n_i\cdot n_j=0\) for every \(i\ne j\). Thus three pairwise mutually unbiased qubit bases uniquely maximize the optimal uncertainty floor and uniquely minimize the optimal certainty ceiling. This proves both extremal assertions of Conjecture 1 of arXiv:1506.07709 in its first nontrivial case \(N=2\), \(L=3\).

## Assumptions and scope
The measurements are rank-one projective measurements on a single qubit, the optimization is over pure input states as in the source formulation, and the entropy is Shannon entropy with natural logarithm. A qubit basis corresponds to an unoriented Bloch axis. Pairwise mutual unbiasedness is therefore exactly the orthogonality condition \(n_i\cdot n_j=0\) for \(i\ne j\).

## Proof
Write
\[
g(x)=h\!\left(\frac{1+x}2\right),
\qquad
H(s)=g(\sqrt s),
\qquad 0\le s\le1.
\]
For \(0<s<1\), direct differentiation gives
\[
H''(s)=-\frac{\frac{\sqrt s}{1-s}-\operatorname{artanh}(\sqrt s)}{4s^{3/2}}<0.
\]
Indeed, for \(0<x<1\), \(\operatorname{artanh}x=\int_0^x(1-t^2)^{-1}dt<x/(1-x^2)\). Hence \(H\) is strictly concave on \([0,1]\), while \(g\) is strictly decreasing on \([0,1]\).

First suppose the three axes are orthonormal. With \(s_j=(n_j\cdot r)^2\), one has \(s_1+s_2+s_3=1\). Strict concavity gives
\[
\frac13\sum_{j=1}^3 H(s_j)\le H\!\left(\frac13\right)=\beta_*,
\]
with equality exactly when \(s_1=s_2=s_3=1/3\). Since a concave function on a simplex attains its minimum at a vertex,
\[
\frac13\sum_{j=1}^3H(s_j)\ge\frac{H(1)+2H(0)}3=\frac23\log2.
\]
Thus the displayed MUB values are exact.

For the lower extremum with arbitrary axes, take the input direction \(r=n_1\). The first entropy vanishes and each of the other two is at most \(\log2\), so \(B_{\min}\le2\log2/3\). If equality holds, both remaining entropies for this input must equal \(\log2\), forcing \(n_1\cdot n_2=n_1\cdot n_3=0\). Repeating the argument with \(r=n_2\) forces \(n_2\cdot n_3=0\). Therefore equality is possible only for three MUBs.

For the upper extremum, form the real \(3\times3\) matrix \(A\) whose rows are \(n_1^T,n_2^T,n_3^T\). If \(A\) is singular, choose a unit vector in its kernel; then all three measurements have entropy \(\log2>\beta_*\), so equality is impossible. Assume now that \(A\) is invertible, and let \(C=AA^T\). Its diagonal entries are one, hence \(\operatorname{tr}C=3\). For each sign vector \(\varepsilon\in\{-1,1\}^3\), define
\[
v_\varepsilon=A^{-1}\frac{\varepsilon}{\sqrt3}.
\]
Averaging over the eight sign vectors gives
\[
\frac18\sum_\varepsilon\|v_\varepsilon\|^2
=\frac13\operatorname{tr}(C^{-1})\ge1,
\]
where the final inequality is the arithmetic-harmonic mean inequality for the three positive eigenvalues of \(C\), whose sum is three. Equality occurs only when all three eigenvalues are one, equivalently \(C=I\).

If \(C\ne I\), some sign vector has \(\|v_\varepsilon\|>1\). For \(r=v_\varepsilon/\|v_\varepsilon\|\),
\[
|n_j\cdot r|=\frac1{\sqrt3\,\|v_\varepsilon\|}<\frac1{\sqrt3}
\qquad(j=1,2,3).
\]
Because \(g\) is strictly decreasing in the absolute Bloch overlap, every one of the three entropies is strictly larger than \(\beta_*\), so \(B_{\max}>\beta_*\). Consequently \(B_{\max}=\beta_*\) forces \(C=I\), which is exactly pairwise mutual unbiasedness. This completes both extremal statements and their equality classification.

## Verification
The proof is analytic and does not infer an infinite statement from numerical sampling. The accompanying `verify.py` checks the closed-form identity for \(\beta_*\), the sign-vector trace identity on deterministic test frames, the strict witness construction for nonorthogonal invertible triples, the singular-frame witness, and sampled instances of the orthogonal-frame entropy bounds. The checker is auxiliary: strict concavity and the arithmetic-harmonic mean step above are the proof of the universal claim.

## Relationship to prior work
Puchała, Rudnicki, Chabuda, Paraniak, and Życzkowski formulated the averaged-entropy extremal conjecture and explicitly treated three qubit measurements numerically. Their text states that the MUB values \(B_{\min}=2\log2/3\) and \(B_{\max}=\beta_*\) are tight for the MUB triple, but that the generic Shannon-entropy extremality was not proved analytically. The present result supplies that missing global comparison over every triple of qubit projective measurements and proves uniqueness of the MUB equality case.

Earlier certainty bounds for a fixed complete MUB determine the two MUB endpoint values but do not compare them with arbitrary non-MUB triples. Work on highly symmetric POVMs analyzes entropy and informational power of fixed symmetric measurements, including the octahedral qubit POVM associated with three MUBs; it does not imply the global extremal statement over all unions of three projective qubit measurements established here.

## Limitations
The theorem resolves only the \(N=2\), \(L=3\) instance of the source conjecture. It does not address higher prime-power dimensions, the separate Shannon-entropy variance conjecture, nonprojective measurements, unequal weights among the three measurements, or averaged entanglement across multiple tensor-product splittings. The classification is for the state-optimized entropy extrema defined above, not for every other certainty or uncertainty functional.

## References
1. Z. Puchała, Ł. Rudnicki, K. Chabuda, M. Paraniak, and K. Życzkowski, *Certainty relations, mutual entanglement and non-displacable manifolds*, arXiv:1506.07709; Phys. Rev. A 92, 032109 (2015), DOI 10.1103/PhysRevA.92.032109.
2. J. Sánchez-Ruiz, *Entropic uncertainty and certainty relations for complementary observables* (1993), cited in arXiv:1506.07709 for the tight complete-MUB endpoint bounds.
3. W. Słomczyński and A. Szymusiak, *Highly symmetric POVMs and their informational power*, Quantum Information Processing (2016), DOI 10.1007/s11128-015-1157-z.
