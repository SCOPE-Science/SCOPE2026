# A sharp log-concavity cutoff for Plücker degrees of Grassmannians
## Finding
Let \(G_{n,k}=\operatorname{Gr}(k,\mathbb C^n)\) with its Plücker embedding and let \(D_{n,k}=\deg G_{n,k}\). Then
\[
D_{n,k}=\frac{(k(n-k))!\prod_{i=0}^{k-1}i!}{\prod_{j=n-k}^{n-1}j!}.
\]
For every \(n\ge2\), the sequence \((D_{n,1},\ldots,D_{n,n-1})\) is symmetric and strictly increases toward its center, with the two central terms equal when \(n\) is odd. More sharply, this degree sequence is log-concave if and only if \(n\le11\). For every \(n\ge12\), the first interior inequality already fails:
\[
D_{n,2}^2<D_{n,1}D_{n,3}=D_{n,3}.
\]
Thus Plücker degrees remain unimodal in every ambient dimension even though cross-rank log-concavity breaks permanently beginning at \(n=12\).

## Assumptions and scope
The base field is \(\mathbb C\), although the degree formula and the resulting integer inequalities are characteristic-free wherever the standard Plücker degree formula applies. The theorem compares different Grassmannians \(\operatorname{Gr}(k,\mathbb C^n)\) at fixed \(n\); it is not a log-concavity statement for intersection numbers on one fixed variety. The endpoint terms satisfy \(D_{n,1}=D_{n,n-1}=1\).

## Proof
The hook-length formula for the \(k\times(n-k)\) rectangle gives the displayed Plücker degree formula. The rectangle transpose, equivalently Grassmannian duality, gives \(D_{n,k}=D_{n,n-k}\).

For \(k<(n-1)/2\), put \(h=n-2k-1>0\) and \(m=k(n-k)\). Direct cancellation in the factorial formula yields
\[
\frac{D_{n,k+1}}{D_{n,k}}
=\frac{(m+h)!}{m!}\frac{k!}{(k+h)!}
=\prod_{j=1}^h\frac{m+j}{k+j}>1,
\]
because \(m=k(n-k)>k\). Symmetry then proves the asserted strict central growth and hence unimodality.

For the log-concavity boundary, define
\[
Q_n=\frac{D_{n,3}}{D_{n,2}^2}
=\frac{2(n-2)(n-1)!(3n-9)!}{(2n-4)!^2}.
\]
Exact arithmetic gives \(Q_{11}=437/442<1\) and \(Q_{12}=3795/2584>1\). Moreover
\[
\frac{Q_{n+1}}{Q_n}
=\frac{3n(3n-8)(3n-7)}{4(n-1)(2n-3)^2},
\]
and subtracting \(1\) has numerator
\[
11n^3-71n^2+84n+36.
\]
Writing \(n=t+5\), this numerator becomes
\[
11t^3+94t^2+199t+56>0
\]
for every integer \(t\ge0\). Hence \(Q_n\) is strictly increasing for \(n\ge5\), so \(Q_n>1\) for every \(n\ge12\). This is exactly the failed log-concavity inequality at \(k=2\), because \(D_{n,1}=1\).

It remains only the finite range \(2\le n\le11\). Substitution into the same factorial formula and exact integer comparison of every interior triple gives \(D_{n,k}^2\ge D_{n,k-1}D_{n,k+1}\) for all admissible \(k\). The bundled checker performs this exhaustive finite verification without floating-point arithmetic. Together with the infinite argument above, this proves the if-and-only-if cutoff.

## Verification
The standalone verifier recomputes every Plücker degree from the factorial formula, checks symmetry and strict central growth for \(2\le n\le100\), checks every log-concavity inequality for \(2\le n\le11\), confirms failure at \((n,k)=(12,2)\), verifies \(Q_{11}=437/442\) and \(Q_{12}=3795/2584\), and checks the positive polynomial identity controlling \(Q_{n+1}/Q_n\) for \(5\le n\le1000\). The finite runs are regression checks; the proof of persistence for all \(n\ge12\) is the displayed symbolic factorization.

At the threshold,
\[
D_{11,2}=4862,\qquad D_{11,3}=23371634,
\]
so \(D_{11,2}^2>D_{11,3}\), whereas
\[
D_{12,2}=16796,\qquad D_{12,3}=414315330,
\]
and \(D_{12,2}^2<D_{12,3}\).

## Relationship to prior work
Cools, Draisma, Payne, and Robeva explicitly note that the hook-length count for a rectangular standard tableau is also the degree of the corresponding Grassmannian in its Plücker embedding. Their paper supplies the classical degree/tableau identification used here. The new statement compares these degrees across \(k\) at fixed \(n\), proving both unconditional central unimodality and the sharp cutoff \(n=11/12\) for log-concavity. Targeted literature and semantic-index searches for Plücker-degree log-concavity, fixed-\(n\) Grassmannian degree sequences, and rectangular-tableau log-concavity did not locate this cutoff statement or a stronger result implying it.

## Limitations
The novelty conclusion is literature-search based, not a proof that no equivalent formulation exists in all combinatorics literature. A specialized result on rectangular standard Young tableaux under simultaneous shape change could conceivably imply the cutoff under different terminology. The theorem concerns ordinary Plücker degrees only; it does not assert analogous behavior for quantum degrees, polar degrees, coisotropic degrees, or other homogeneous embeddings.

## References
F. Cools, J. Draisma, S. Payne, and E. Robeva, “A tropical proof of the Brill-Noether Theorem,” arXiv:1001.2774; Adv. Math. 230 (2012), 759–776. In the published text, the rectangular hook-length count is identified with the Plücker degree of the Grassmannian.
