# A logarithmic normal-cone crossover in near-regular Laplacian simplices

## Finding
Let \(K_{p,q}\) be a complete bipartite graph, let \(n=p+q\), and form its **canonical Euclidean Laplacian-row simplex** \(P_{p,q}\), the convex hull in \(\mathbf1^\perp\subset\mathbb R^n\) of the \(n\) rows of the ordinary graph Laplacian. Let \(U_n\) be Haar-uniform on the Euclidean unit sphere of \(\mathbf1^\perp\). Write \(W_n\) for the width of \(P_{p,q}\) in direction \(U_n\), and \(J_n^+,J_n^-\in\{0,1\}\) for the indicators that its unique upper and lower exposed vertices belong to the first part of size \(p\).

For every sequence of positive integers \(p=p_n,q=q_n\) with \(n\to\infty\) and the finite limit
\[
\tau_n=\frac{2(q-p)b_n^2}{n}\longrightarrow\tau\in\mathbb R,
\qquad b_n=\Phi^{-1}(1-2/n),\qquad s_n=\frac{n}{2b_n},
\]
where \(\Phi\) is the standard normal distribution function, the following joint convergence holds:
\[
\boxed{\left(\frac{\sqrt n\,W_n-nb_n}{s_n},J_n^+,J_n^-\right)
\ \Longrightarrow\ \left(G_1+G_2+2\log(2\cosh(\tau/2)),B_1,B_2\right).}
\]
Here \(G_1,G_2\) are independent standard Gumbel variables with distribution function \(\exp(-e^{-x})\); \(B_1,B_2\) are independent Bernoulli variables of common success probability \(\ell(\tau)=(1+e^{-\tau})^{-1}\); and all four limiting variables are independent.

Consequently, if \(\omega_i\) is the normalized spherical solid angle of the vertex normal cone, then, uniformly over vertices within each color class,
\[
\boxed{n\omega_i\longrightarrow
\begin{cases}2\ell(\tau),&i\text{ in the part of size }p,\\
2(1-\ell(\tau)),&i\text{ in the part of size }q.
\end{cases}}
\]
Yet the simplex is **asymptotically equilateral**: every pairwise vertex distance divided by \(n/\sqrt2\) tends to one. Thus vanishing relative distortion of all edge lengths coexists with a nontrivial, sharply tunable disparity of normal-cone angles. The crossover occurs at part-size difference of order \(n/\log n\).

## Assumptions and scope
All assertions concern the indicated Euclidean embedding in the sum-zero hyperplane, with the Euclidean metric induced from \(\mathbb R^n\). The usual integer-coordinate representative obtained by deleting a Laplacian column is lattice equivalent, but **not generally Euclidean-isometric** to this realization. The theorem concerns sequences \(p,q\ge2\) and \(n\to\infty\) satisfying the displayed finite-\(\tau\) condition. It does not assert the same centering or distribution for fixed unequal limiting part ratios. Ties between exposed vertices have probability zero.

The color-class indicators refer to the **part containing the exposed graph vertex**, not an arbitrary coloring of a different polytope. The first-publication anchor for this natural family is Braun--Meyer, arXiv:1706.07085, made public on 2017-06-21 (primary mathematical classification 52B20 in that manuscript).

## Proof
**1. The exact Gaussian optimization identity.** Let \(g=(g_1,\ldots,g_n)\) have independent standard Gaussian coordinates, partitioned into sets \(A,B\) with cardinalities \(p,q\). Put \(S_A=\sum_{i\in A}g_i\), \(S_B=\sum_{j\in B}g_j\). For the graph Laplacian \(L\), direct matrix multiplication gives
\[
(Lg)_i= qg_i-S_B\quad(i\in A),\qquad
(Lg)_j= pg_j-S_A\quad(j\in B).
\]
Because each row of \(L\) is orthogonal to \(\mathbf1\), the vector \(g_0=g-(n^{-1}\sum_i g_i)\mathbf1\) induces the same support values. Writing \(R_n=\|g_0\|_2\), \(g_0/R_n\) is uniform on the sphere of \(\mathbf1^\perp\), and \(R_n/\sqrt n\to1\) in probability. Therefore the exact spherical width is the range of the displayed \(n\) support values divided by \(R_n\).

**2. Extreme values in the two blocks.** The finite-\(\tau\) assumption implies \(p/n\to1/2\), \(q/n\to1/2\), and \(q-p=O(n/\log n)\). Write \(M_A=\max_{i\in A}g_i\), \(m_A=\min_{i\in A}g_i\), and similarly for \(B\). Since \(b_n\to\infty\) and \((n/2)\,[1-\Phi(b_n)]=1\), the classical normal-tail estimate implies, jointly,
\[
\bigl(b_n(M_A-b_n),b_n(-m_A-b_n),
 b_n(M_B-b_n),b_n(-m_B-b_n)\bigr)
\Longrightarrow (G_A^+,G_A^-,G_B^+,G_B^-),
\]
with four independent standard Gumbels. This follows directly from the product formula
\[
\Pr\{M_A\le b_n+x/b_n,\ m_A\ge-b_n-y/b_n\}
=\left[1-\overline\Phi(b_n+x/b_n)-\overline\Phi(b_n+y/b_n)\right]^p
\to e^{-e^{-x}-e^{-y}},
\]
and the corresponding formula for \(B\), where \(\overline\Phi=1-\Phi\). The ratio \(p/(n/2)\to1\) makes the same \(b_n\) valid for both blocks.

**3. The crossover expansion.** Set \(c_n=nb_n/2\) and \(s_n=n/(2b_n)\). The upper block supports, after subtracting \(c_n\) and dividing by \(s_n\), converge jointly to
\[
G_A^++\tau/2,\qquad G_B^+-\tau/2.
\]
Indeed \((q-p)b_n/(2s_n)=\tau_n/2\) and \(S_A/s_n,S_B/s_n\to0\) in probability since their standard deviations are \(O(\sqrt n)\) whereas \(s_n\asymp n/\sqrt{\log n}\). The lower supports, after negating, give two independent limiting competitors \(G_A^-+\tau/2\) and \(G_B^--\tau/2\). Joint independence between upper and lower limiting competitors follows from step 2. Taking the two maxima establishes a Gaussian-width limit, together with its two maximizing color labels. By continuous mapping, the labels are well defined almost surely in the limit because independent Gumbels have no ties.

**4. Gumbel competition and independence.** If \(G_A,G_B\) are independent standard Gumbels, then
\[
\max(G_A+\tau/2,G_B-\tau/2)
\stackrel d=G+\log(e^{\tau/2}+e^{-\tau/2}).
\]
Its maximizing class is Bernoulli with probability \(e^{\tau}/(1+e^{\tau})\) for \(A\), and is independent of the maximum. For an explicit verification, the positive random variables \(e^{-G_A}\), \(e^{-G_B}\) are independent rate-one exponentials. After multiplication by \(e^{-\tau/2}\) and \(e^{\tau/2}\) they form a competing pair of exponentials with rates \(e^{\tau/2}\) and \(e^{-\tau/2}\). The winning identity is independent of the minimum time, and has the stated logistic probability. Applying this separately to the asymptotically independent upper and lower pairs gives both Bernoulli variables, their independence, and the limiting sum of two Gumbels.

**5. Spherical normalization.** The Gaussian width is \(O_{\Pr}(nb_n)\). Since \(R_n/\sqrt n=1+O_{\Pr}(n^{-1/2})\), replacing Gaussian width by \(\sqrt n\,W_n\) changes the centered, \(s_n\)-normalized quantity by \(O_{\Pr}(b_n^2/\sqrt n)=o_{\Pr}(1)\). This proves the joint limit in the statement.

**6. Normal cones and near-equilateral geometry.** Each part acts transitively on its own vertex set. Its aggregate spherical normal-cone measure is exactly the probability that the upper exposed vertex lies in that part. Step 4 and \(p/n,q/n\to1/2\) give the two per-vertex limits. The squared distances between two distinct Laplacian rows from \(A\), from \(B\), and from different parts are respectively
\[
2q^2,\qquad2p^2,\qquad p^2+q^2+3n.
\]
All are asymptotic to \(n^2/2\) in the critical window. The claimed asymptotic equilateral property follows. This distance comparison is a geometric observation, not a substitute for the normal-cone calculation.

## Verification
The accompanying standalone script `verify.py` reconstructs the graph Laplacian and checks the support identity, spherical normalization, and vertex optimization directly for \(320\) independently generated small instances. It also performs numerical finite-dimensional comparisons of observed exposed-vertex classes and centered widths with the predicted logistic and Gumbel limits at \(n=6000\). The script prints the finite-sample deviations rather than treating the Monte Carlo run as a proof. The rigorous infinite-sequence argument consists of the six steps above and the normal-tail asymptotics they explicitly invoke.

## Relationship to prior work
Braun and Meyer introduced Laplacian simplices and examined lattice, reflexivity, and Ehrhart invariants [1]. Meyer and Pllaha studied coding-theoretic constructions arising from them [2]. Juhnke-Kubitzke and Köhne developed Laplacian polytopes for higher-dimensional simplicial complexes [3]. Kabluchko, Litvak and Zaporozhets established Gaussian mean-width and Gumbel projection-width results for **regular** simplices [4]. The present object has two unequal-degree vertex classes, and the main new invariant is the sharp normal-cone mass transfer through a logarithmic imbalance window. In particular, the nonconstant limiting logistic bias cannot follow from the vertex symmetry of the regular-simplex theorem, despite asymptotically equal edge lengths.

## Limitations
Only the critical window with finite \(\tau\) is proved with the stated universal centering. Other graph families, higher-part multipartite Laplacian simplices, and fluctuations outside this window are not classified. The claim of originality is based on the identified literature and comparison of mathematical implications, not on a proof that no unindexed or unpublished equivalent result exists. The theorem has not undergone independent validation. It concerns the canonical orthogonal Euclidean realization; arbitrary lattice-equivalent coordinate embeddings can change mean widths and normal angles. Simulations support selected finite cases but provide no infinite-dimensional certification.

## References
[1] Benjamin Braun and Marie Meyer, *Laplacian Simplices*, arXiv:1706.07085, first submitted 2017-06-21. https://arxiv.org/abs/1706.07085

[2] Marie Meyer and Tefjol Pllaha, *Laplacian Simplices II: A Coding Theoretic Approach*, arXiv:1809.02960. https://arxiv.org/abs/1809.02960

[3] Martina Juhnke-Kubitzke and Daniel Köhne, *Laplacian Polytopes of Simplicial Complexes*, arXiv:2301.11602. https://arxiv.org/abs/2301.11602

[4] Zakhar Kabluchko, Alexander E. Litvak, and Dmitry Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479, especially Theorem 3.7. https://arxiv.org/abs/1511.08479
