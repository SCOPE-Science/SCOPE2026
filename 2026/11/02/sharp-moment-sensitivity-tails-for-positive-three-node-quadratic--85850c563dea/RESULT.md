# Sharp moment-sensitivity tails for positive three-node quadratic quadrature

## Finding

Let three independent nodes have the uniform distribution on \([-1,1]\). Conditional on the unique three-node degree-two interpolatory quadrature rule having **strictly positive weights**, its inverse monomial Vandermonde matrix has an exact quadratic upper tail with a nonzero constant. This shows a distinction between positivity-based control of the quadrature functional on bounded sampled functions and stability of the weights under separately perturbed target moments.

Write \(a<b<c\) for the sorted nodes, and define
\[
V=\begin{pmatrix}1&1&1\\ a&b&c\\ a^2&b^2&c^2\end{pmatrix},\qquad
m=(1,0,1/3)^{\mathsf T},\qquad w=V^{-1}m,\qquad N=\|V^{-1}\|_F.
\]
Let \(E\) be the event that all three coordinates of \(w\) are strictly positive. The exact assertions are
\[
\Pr(E)=P_+=\frac{\log3}{2}-\frac13,
\quad\lim_{T\to\infty}T^2\Pr(E,\,N>T)=K=1-\frac{\pi\sqrt3}{36},
\]
\[
\lim_{T\to\infty}T^2\Pr(N>T\mid E)=\frac{K}{P_+},\qquad
\mathbb E[N^p\mid E]<\infty\ \Longleftrightarrow\ 0<p<2
\quad(p>0).
\]
Numerically \(P_+=0.2159728110007216\), \(K=0.848850052980482\), and \(K/P_+=3.93035608995081\).

## Assumptions and scope

The nodes are iid from the probability measure \(dt/2\) on \([-1,1]\), and the monomial moments are \((1,0,1/3)\). The nodes are distinct with probability one. Positive means **strictly** positive quadrature weights, and all probability statements use the unconditioned iid law unless \(E\) appears after a conditioning bar. The monomial basis and Frobenius matrix norm are fixed: the coefficient \(K\) is not claimed to be invariant under arbitrary changes of moment-coordinate normalization. The Frobenius norm measures the root-sum-square response of the weights to orthonormal moment-coordinate perturbations, rather than the amplification of noise in the sampled integrand values.

## Proof

**Exact positivity domain.** The Lagrange-polynomial formula gives
\[
w_a=\frac{bc+1/3}{(a-b)(a-c)},\quad
w_b=\frac{ac+1/3}{(b-a)(b-c)},\quad
w_c=\frac{ab+1/3}{(c-a)(c-b)}.
\]
Since \(a<b<c\), the middle denominator is negative and the other two are positive. It follows that \(E\) holds exactly when
\[
a<-\frac13,\quad c>\frac13,\quad ac<-\frac13,\quad
-\frac{1}{3c}<b<-\frac{1}{3a}.
\]
Set \(s=-a\). The admissible region, up to sets of zero probability, is
\[
\frac13<s<1,\qquad \frac1{3s}<c<1,\qquad
-\frac1{3c}<b<\frac1{3s}.
\]
The ordered-node density is \(3/4\). Consequently
\[
\Pr(E)=\frac34\int_{1/3}^1\int_{1/(3s)}^1
\left(\frac1{3s}+\frac1{3c}\right)\,dc\,ds
=\frac12\log3-\frac13.
\]

**Where the inverse becomes singular.** Its three rows are the monomial-coefficient vectors of
\(\ell_a(t)=(t-b)(t-c)/[(a-b)(a-c)]\), and its two cyclic analogues. Throughout \(E\), the outer-node separation satisfies \(c-a\ge2/\sqrt3\). Thus there are no triple collisions and \(N\) is bounded on portions of the closure of \(E\) where both adjacent gaps stay bounded below. The only ways for \(N\to\infty\) are the two adjacent-node collision faces, which are exchanged by reflection \((a,b,c)\mapsto(-c,-b,-a)\). This reflection preserves both \(E\) and \(N\).

**Local collision scale.** On the left face write \(a=-s\), \(b=-s+h\), with \(h>0\) small and \(1/3<s<1\). Positivity confines the third node to
\[
\frac1{3s}<c<\frac1{3(s-h)},
\qquad \frac1{3(s-h)}-\frac1{3s}=\frac{h}{3s^2}+O_s(h^2).
\]
Consequently \(c\to1/(3s)\), and the first two rows of \(V^{-1}\) have opposite order-\(1/h\) singular parts. Their shared coefficient vector comes from \((t+s)(t-1/(3s))\) divided by \(s+1/(3s)\). It follows that
\[
\lim_{h\downarrow0}h^2N^2=C(s)^2,
\quad C(s)^2=\frac{2(9s^4+4s^2+1)}{(3s^2+1)^2}.
\]
The limit is uniform for \(s\) on compact interior subintervals and for \(c\) in the positivity strip. The two other rows' bounded contributions are negligible.

**Scaling the two collision tubes.** Set \(h=u/T\) in the left tube. Because \(N/T\to C(s)/u\) and the permitted \(c\)-width is \(h/(3s^2)+O(h^2)\), its contribution to \(T^2\Pr(E,N>T)\) approaches
\[
\frac34\int_{1/3}^1\frac1{3s^2}\int_0^{C(s)}u\,du\,ds.
\]
Reflection doubles the result. To justify passage to the limit, the Lagrange-row denominators and the fixed outer-node gap give a uniform bound \(N\le M[1/(b-a)+1/(c-b)]\) on \(E\). Hence a sufficiently large value of \(N\) lies in a fixed small tube around one of the two collision faces; for \(N>T\) the corresponding gap is \(O(T^{-1})\), uniformly. The scaled \(u\)-variable therefore stays bounded. The length of the admissible transverse strip is at most a constant times \(h\), and endpoint truncations at \(s=1/3\) and \(s=1\) have vanishing contribution by dominated convergence. The two tubes are disjoint at small fixed width because \(c-a\ge2/\sqrt3\).

Thus
\[
K=\frac14\int_{1/3}^1\frac{C(s)^2}{s^2}\,ds
=\int_{1/3}^1\left[\frac1{2s^2}-\frac1{(1+3s^2)^2}\right]ds
=1-\frac{\pi\sqrt3}{36}.
\]
For the final equality use the primitive
\(s/[2(1+3s^2)]+\arctan(\sqrt3s)/(2\sqrt3)\)
for the second integrand; the rational endpoint terms cancel. Division by \(P_+\) proves the conditional limit. Finally, the tail-integral identity
\(\mathbb E[N^p\mid E]=p\int_0^\infty t^{p-1}\Pr(N>t\mid E)\,dt\)
shows exactly the stated moment cutoff.

## Verification

The supplied standalone file `verify_positive_tail.py` uses only the Python standard library. It checks exact rational interpolation identities and the positivity-domain equivalence on \(165\) distinct ordered triples, evaluates the one-dimensional tail integral independently, checks near-coalescence scaling for twelve positive triples, and importance-integrates the thin admissible collision strip at thresholds \(100\), \(200\), and \(400\). Execute `python3 verify_positive_tail.py`. The deterministic output ends with `CHECK_OK`. The numerical tests are supplementary; the proof of the continuous tail law rests on the analytic collision calculation and dominated convergence.

## Relationship to prior work

Neumayer, Schäfer and Ullrich prove existence and bounded positive quadrature weights from sufficiently many random nodes, with an oversampling and weight-adaptation mechanism; their theorem does not impose the unique minimally supported three-node rule or estimate the distribution of its inverse moment matrix. Van den Bos and Sanderse develop the Vandermonde geometry of positivity-preserving node addition and removal, but do not provide this conditional distributional coefficient. Kunis and Nagel study deterministic conditioning when nodes nearly collide, in a different complex exponential Vandermonde setting; the mere inverse-gap singularity does not imply the positivity-induced tube width or this precise constant. Earlier results on heavy tails of minimum-norm **affine-exact** weights for iid nodes concern different moment degree, weight selection, and norms; they do not imply this degree-two conditional inverse-Frobenius law. Priority among older specialized random-interpolation or positive-quadrature calculations cannot be claimed exhaustively.

## Limitations

The law is exact only for three iid **uniform real nodes**, degree-two exactness for the uniform interval measure, the stated moment normalization, and the Frobenius norm of the inverse square Vandermonde. It concerns sensitivity of weights to target moment errors, **not** numerical instability of evaluating a positive quadrature rule on bounded integrand data, and not the oversampled constructions of the motivating paper. Only the leading tail constant is proved, with no claimed finite-threshold error bound or high-dimensional extension. The result has not received an independent mathematical audit.

## References

1. S. Neumayer, M. Schäfer and T. Ullrich, *Random nodes with positive weights: Richter–Tchakaloff rules and optimal positive quadrature*, arXiv:2610.32699v1, publicly posted 2026-10-23. https://arxiv.org/html/2610.32699v1
2. L. M. M. van den Bos and B. Sanderse, *A geometrical interpretation of the addition of nodes to an interpolatory quadrature rule while preserving positive weights*, *J. Comput. Appl. Math.* 391 (2021), 113430. https://doi.org/10.1016/j.cam.2021.113430
3. S. Kunis and D. Nagel, *On the condition number of Vandermonde matrices with pairs of nearly-colliding nodes*, *Numerical Algorithms* (2020). https://doi.org/10.1007/s11075-020-00974-x
