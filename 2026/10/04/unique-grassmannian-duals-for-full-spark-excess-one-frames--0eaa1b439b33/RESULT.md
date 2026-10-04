# Unique Grassmannian duals for full-spark excess-one frames

## Finding
Let \(F=(f_1,\ldots,f_{n+1})\) be a full-spark frame for \(\mathbb C^n\), and let \(0\ne z\in\ker F\). Since the frame has excess one and is full spark, every coordinate of \(z\) is nonzero. Define
\[
a_i=|z_i|,\qquad b_i=\max_{j\ne i}|z_j|,\qquad
\mu_*=\left(\sum_{i=1}^{n+1}\frac{a_i}{b_i}\right)^{-1}.
\]
Among all dual frames \(H=(h_1,\ldots,h_{n+1})\), the Grassmannian cross-coherence
\[
\mu(F,H)=\max_{i\ne j}|\langle f_i,h_j\rangle|
\]
has a unique minimizer. Its cross-Gramian is
\[
G_*=F^*H_*=I-qz^*,\qquad
q_i=\frac{\mu_* z_i}{a_i b_i},
\]
and \(\mu(F,H_*)=\mu_*\).

The unique minimizer is the canonical dual if and only if \(a_i b_i\) is independent of \(i\). Thus every full-spark excess-one frame has an exclusive Grassmannian dual, but in general that dual is not canonical.

A concrete real counterexample is
\[
F=\begin{pmatrix}3&0&-1\\0&3&-2\end{pmatrix},\qquad
z=(1,2,3)^\mathsf T.
\]
Here \(\mu_*=2/5\), and the unique minimizing dual is
\[
H_*=\begin{pmatrix}13/45&-4/45&-2/15\\-2/45&11/45&-2/15\end{pmatrix}.
\]
Its cross-coherence is \(2/5\). The canonical dual instead has cross-coherence \(3/7\). Hence this frame is an exclusive Grassmannian pair with a noncanonical dual, giving a counterexample to Conjecture 42 of Aceska and Kaczanowski.

## Assumptions and scope
The theorem applies over \(\mathbb C\), and therefore also over \(\mathbb R\), to every full-spark frame of exactly \(n+1\) vectors in dimension \(n\). Full spark is used only to guarantee that every coordinate of the one-dimensional kernel vector \(z\) is nonzero, so all \(b_i\) are positive and the minimizer formula is well defined. The result concerns the maximal off-diagonal modulus of the cross-Gramian, the objective used in the cited definition of a Grassmannian pair.

## Proof
Let \(W=\operatorname{ran}F^*=(\ker F)^\perp=z^\perp\). If \(H\) is a dual frame, then \(FH^*=HF^*=I\). Therefore its cross-Gramian \(G=F^*H\) satisfies \(G^2=G\), has range \(W\), and acts as the identity on \(W\). Conversely, every projection \(G\) onto \(W\) gives a unique dual: because every column of \(G\) lies in \(W\), set
\[
H=(FF^*)^-1FG.
\]
Then \(F^*H=G\) and \(HF^*=I\). Since \(F^*\) is injective, the dual is uniquely determined by its cross-Gramian.

Every projection onto the hyperplane \(z^\perp\) has a unique representation
\[
G=I-qz^*,\qquad z^*q=1.
\]
For \(i\ne j\),
\[
G_{ij}=-q_i\overline{z_j},
\]
so
\[
\mu(F,H)=\max_i b_i|q_i|.
\]
If this maximum is \(\mu\), then
\[
1=|z^*q|\le \sum_i a_i|q_i|
\le \mu\sum_i\frac{a_i}{b_i}.
\]
Thus \(\mu\ge\mu_*\). Equality requires equality in both displayed inequalities. Because each weight \(a_i/b_i\) is positive, the second equality forces \(b_i|q_i|=\mu_*\) for every \(i\). Equality in the triangle inequality, together with \(z^*q=1\), forces every \(\overline{z_i}q_i\) to be a nonnegative real number. Hence necessarily
\[
q_i=\frac{\mu_*z_i}{a_i b_i},
\]
which indeed satisfies \(z^*q=1\). The minimizer is therefore unique.

The canonical cross-Gramian is the orthogonal projection onto \(z^\perp\), namely
\[
P=I-\frac{zz^*}{\|z\|^2}.
\]
It agrees with \(G_*\) exactly when \(\mu_*/(a_i b_i)=1/\|z\|^2\) for every \(i\), equivalently when all products \(a_i b_i\) are equal.

For the displayed real frame, \(a=(1,2,3)\), \(b=(3,3,2)\), and therefore \(\mu_*=2/5\). Direct substitution gives the stated \(H_*\) and verifies \(FH_*^\mathsf T=I\). The canonical dual is
\[
H_{\rm can}=\begin{pmatrix}13/42&-1/21&-1/14\\-1/21&5/21&-1/7\end{pmatrix},
\]
whose largest off-diagonal cross-Gramian modulus is \(3/7>2/5\).

## Verification
The general proof is analytic and does not rely on enumeration or numerical optimization. An exact rational checker included with this package verifies the concrete counterexample: both displayed dual identities, the two cross-Gramians, idempotence, and the exact coherences \(2/5\) and \(3/7\). The checker is supplementary evidence for the example, not a substitute for the general proof.

## Relationship to prior work
Aceska and Kaczanowski define Grassmannian pairs by minimizing the maximal off-diagonal modulus of the cross-Gramian over all duals. Their Conjecture 42 states that if a frame forms an exclusive Grassmannian pair with one of its duals, then that dual must be canonical. The theorem above gives the complete excess-one full-spark minimization and produces a noncanonical exclusive minimizer, so it directly contradicts that conjecture.

Christensen, Datta, and Kim prove a Welch-type lower bound for the maximal off-diagonal cross-coherence under the additional hypothesis that the diagonal pairings \(\langle f_i,h_i\rangle\) are constant, and characterize equality. That result does not cover the present fixed-frame minimization: the theorem here imposes no constant-diagonal condition, gives a frame-dependent exact minimum, and its optimizer can be noncanonical.

The earlier finite-dual-pair characterization of Christensen, Powell, and Xiao describes allowable diagonal pairings but does not minimize the off-diagonal cross-Gramian norm. Thus it also does not imply the formula above.

## Limitations
The explicit closed form uses the one-dimensional kernel of an excess-one frame. For larger excess, the family of projections onto \(\operatorname{ran}F^*\) has a higher-dimensional kernel parameter and the same scalar reduction no longer applies. No claim is made here about uniqueness or canonical optimality for excess at least two. A residual literature risk is that the same hyperplane minimax lemma may appear under oblique-projection or Chebyshev matrix-approximation terminology not indexed by frame-theoretic searches.

## References
1. R. Aceska and M. Kaczanowski, *Cross-Frame Potential*, arXiv:2205.05613; DOI: 10.1080/01630563.2022.2128818.
2. O. Christensen, S. Datta, and R. Y. Kim, *Equiangular frames and generalizations of the Welch bound to dual pairs of frames*, Linear and Multilinear Algebra 68 (2020), 2495–2505; DOI: 10.1080/03081087.2019.1586825.
3. O. Christensen, A. Powell, and X. C. Xiao, *A note on finite dual frame pairs*, Proceedings of the American Mathematical Society 140 (2012), 3921–3930; DOI: 10.1090/S0002-9939-2012-11256-0.
