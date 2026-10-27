# Exact negative motif–length covariance in the circular nearest-neighbor graph

## Finding

Let \(n\ge5\) points be independently uniform on a circle of circumference one. Direct an edge from each point to its unique nearest other point under the intrinsic circular distance. Write \(R_n\) for the number of unordered **mutual nearest-neighbor pairs** (equivalently, the number of weak connected components), and \(L_n\) for the sum of lengths of the \(n\) directed edges, so reciprocal edges contribute twice. Then

\[
\operatorname{Cov}(R_n,L_n)=-\frac1{36}\qquad(n\ge5).
\]

In fact the exact individual moments and their resulting correlation are

\[
\mathbb E R_n=\frac n3,\quad \operatorname{Var}(R_n)=\frac{2n}{45},\quad
\mathbb E L_n=\frac12,\quad \operatorname{Var}(L_n)=\frac1{6(n+1)},
\]

\[
\operatorname{Corr}(R_n,L_n)=-\frac{\sqrt{15}}{12}\sqrt{\frac{n+1}{n}}
\xrightarrow[n\to\infty]{}-\frac{\sqrt{15}}{12}.
\]

Thus the covariance does not decay with sample size, and the correlation tends to a strictly negative constant. The *joint mixed moment* is the main claim; some separate motif moments were previously known for uniform samples on a line.

## Assumptions and scope

The circumference is one. Sampling is with replacement from continuous uniform arc length; collisions and ties have probability zero. Distances are the shorter of the two arc lengths. The graph is **static**, not an online nearest-neighbor graph or a probabilistic connection model. The count \(R_n\) counts each reciprocal pair once. The length \(L_n\) counts one outgoing arc per vertex, including both arcs of a reciprocal pair. All displayed finite-sample identities are asserted for every integer \(n\ge5\), without additional asymptotics.

Label the points in cyclic order, and let \(S_i\) be the gap immediately following point \(i\), with indices modulo \(n\). Circular spacings satisfy \((S_1,\ldots,S_n)\sim\operatorname{Dirichlet}(1,\ldots,1)\). Equivalently, take independent unit-rate exponentials \(E_1,\ldots,E_n\), put \(T=\sum_iE_i\), and write \(S_i=E_i/T\). The random variable \(T\), distributed \(\operatorname{Gamma}(n,1)\), is independent of the normalized gap vector and of every function of it.

## Proof

**1. Gap representation.** Every vertex's nearest neighbor is one of its two cyclic neighbors. Define

\[
I_i=\mathbf1\{E_i<E_{i-1},\ E_i<E_{i+1}\},\qquad B_i=\min(E_{i-1},E_i),\qquad Q=\sum_i B_i.
\]

Then \(R_n=\sum_iI_i\) and \(L_n=Q/T\). Each weak component of a nearest-neighbor digraph has exactly one directed two-cycle: directed edge lengths strictly decrease along any non-reciprocal directed path, so no longer directed cycles occur, and an out-degree-one weak component has precisely one cycle. Hence the interpretations of \(R_n\) coincide.

By exponential symmetry, \(\mathbb EI_i=1/3\) and \(\mathbb EB_i=1/2\). Independence of \(T\) from \((R_n,L_n)\) gives

\[
\operatorname{Cov}(R_n,Q)=\operatorname{Cov}(R_n,TL_n)
=(\mathbb ET)\operatorname{Cov}(R_n,L_n)
=n\operatorname{Cov}(R_n,L_n).
\]

**2. Mixed covariances.** At fixed \(i\), only four \(B_j\)'s share an exponential variable with the event \(I_i=1\). For \(j=i,i+1\), this event forces \(B_j=E_i\), so

\[
\mathbb E(I_iB_j)=\mathbb E\bigl[E_i\mathbf1\{E_i<E_{i-1},E_i<E_{i+1}\}\bigr]
=\int_0^\infty x e^{-3x}\,dx=\frac19,
\]

\[
\operatorname{Cov}(I_i,B_j)=\frac19-\frac13\cdot\frac12=-\frac1{18}.
\]

For \(j=i-1,i+2\), use four independent unit-rate exponentials \(X,Y,Z,W\) and the event \(A=\{X<Y,X<Z\}\). With \(B=\min(W,Y)\), integration of the tail identity yields

\[
\begin{aligned}
\mathbb E[\mathbf1_A B]
&=\int_0^\infty e^{-t}\Pr(Y>t,X<Y,X<Z)\,dt\\
&=\int_0^\infty e^{-t}\left(\frac12e^{-t}-\frac16e^{-3t}\right)\,dt
=\frac5{24}.
\end{aligned}
\]

The inner probability follows by splitting the integral over \(X\) at \(t\). Therefore each such covariance is \(5/24-1/6=1/24\). All other pairs \((I_i,B_j)\) use disjoint sets of exponentials and are independent. For \(n\ge5\) the four indices are distinct, giving

\[
\operatorname{Cov}(R_n,Q)
=n\left[2\left(-\frac1{18}\right)+2\left(\frac1{24}\right)\right]
=-\frac n{36}.
\]

Division by \(n\) proves the asserted exact covariance.

**3. Variance of reciprocal pairs.** A local-minimum indicator has variance \(2/9\). Adjacent local-minimum indicators are mutually exclusive, hence covariance \(-1/9\). For indicators whose indices differ by two, condition on the common exponential value \(y\); the two outside choices are independent and each succeeds with probability \((1-e^{-2y})/2\). Consequently their joint success probability is

\[
\frac14\int_0^\infty e^{-y}(1-e^{-2y})^2\,dy=\frac2{15},
\]

so their covariance is \(2/15-1/9=1/45\). More distant indicators are independent. Cyclic counting for \(n\ge5\) yields

\[
\operatorname{Var}(R_n)=n\frac29+2n\left(-\frac19\right)+2n\frac1{45}=\frac{2n}{45}.
\]

**4. Variance of directed length.** Each \(B_i\) is exponential of rate two, so \(\operatorname{Var}(B_i)=1/4\). Nonadjacent \(B_i\) are independent. For independent unit-rate exponentials \(X,Y,Z\), conditioning on \(Y=y\) gives

\[
\mathbb E[\min(X,Y)\min(Y,Z)]
=\mathbb E[(1-e^{-Y})^2]=\frac13,
\]

so adjacent \(B_i\)'s have covariance \(1/3-1/4=1/12\). Thus

\[
\mathbb EQ=\frac n2,\qquad\operatorname{Var}(Q)=\frac n4+2n\frac1{12}=\frac{5n}{12}.
\]

Since \(Q=TL_n\) and \(T\) is independent of \(L_n\), while \(\mathbb ET=n\) and \(\mathbb ET^2=n(n+1)\),

\[
\mathbb EL_n=\frac12,\qquad
\mathbb EL_n^2=\frac{\frac{n^2}{4}+\frac{5n}{12}}{n(n+1)}
=\frac{3n+5}{12(n+1)},
\]

and subtracting \(1/4\) gives \(\operatorname{Var}(L_n)=1/[6(n+1)]\). Combining the two variances with the exact mixed covariance proves the correlation formula and its limit.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic. It exhaustively enumerates all \(n!\) circular gap-rank orders for \(n=5,6,7,8\), computing the conditional expected directed edge length from exact Dirichlet order-statistic means. It checks the mutual-pair mean and variance, directed-length mean, and joint covariance. It separately checks the local exponential moment constants in the proof. Finite enumeration is a diagnostic; the preceding integrations and independence calculations prove the statements for every integer \(n\ge5\).

Run `python verify.py` in an ordinary Python 3 environment; no external packages are required.

## Relationship to prior work

Bahadır and Ceyhan [2] study reflexive and shared nearest neighbors in **uniform interval** samples, obtaining exact separate moments for reflexive-pair counts; they credit the earlier count results to Enns and collaborators. Their result \(\operatorname{Var}(R_n)=2n/45\) for \(n\ge5\) is therefore **not claimed as new**. Their article does not supply a joint moment with the sum of directed nearest-neighbor lengths. Penrose and Wade [3] derive nearest-neighbor total-length moments for a uniform interval and treat the online model, but do not establish this static circular motif–length covariance. Wilsher, Dettmann and Ganesh [1] study isolated vertices in a soft random geometric graph on a one-dimensional torus with independent probabilistic connections, rather than the deterministic nearest-neighbor digraph. The present mixed-moment identity is not implied by either separate marginal moment result or a limit theorem about a different graph model.

## Limitations

This theorem is confined to iid uniform sampling on a circle and to intrinsic geodesic nearest neighbors. It does not assert the same value for an interval, nonuniform intensities, probabilistic connection graphs, Euclidean chordal arc weights, undirected edge-length counting, or higher dimensions. The correlation formula uses the *directed* length convention. Prior literature on one-dimensional nearest-neighbor graphs is extensive; historical-priority uncertainty remains even though no equivalent mixed covariance was identified in the inspected primary sources and searched records. Independent validation has not been performed.

## References

[1] M. Wilsher, C. Dettmann, A. Ganesh, *The Distribution of the Number of Isolated Nodes in the 1-Dimensional Soft Random Geometric Graph*, arXiv:2202.08044, first posted 2022-02-16. https://arxiv.org/abs/2202.08044

[2] S. Bahadır and E. Ceyhan, *On the Number of Reflexive and Shared Nearest Neighbor Pairs in One-Dimensional Uniform Data*, arXiv:1605.01940, first posted 2016-05-06. https://arxiv.org/abs/1605.01940

[3] M. D. Penrose and A. R. Wade, *Limit theory for the random on-line nearest-neighbor graph*, arXiv:math/0603561, first posted 2006-03-23. https://arxiv.org/abs/math/0603561
