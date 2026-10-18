# Two critical Rényi windows in the angular spectra of star-graph polytopes

## Finding
For integers \(n\ge2\) and \(1\le m\le n\), let \(G_n=K_{1,n}\) have hub \(0\) and leaves \(1,\ldots,n\). For \(S\subseteq\{0,\ldots,n\}\), write \(\Delta_S=\operatorname{conv}\{e_i:i\in S\}\). Study the intrinsic Euclidean polytope
\[
Q_{n,m}=\sum_{\substack{\varnothing\ne S\subseteq\{0,\ldots,n\}\\G_n[S]\text{ connected},\ |S|\le m+1}}\Delta_S
\]
in its fixed-coordinate-sum affine span. For an isotropic Gaussian exposing direction in its direction space, denote the probability of exposing vertex \(v\) by \(p_v\), and put \(Z_{n,m}(q)=\sum_v p_v^q\) and \(H_{n,m}(q)=\log Z_{n,m}(q)/(1-q)\) for \(q>0\), \(q\ne1\), with the continuous Shannon extension at \(q=1\).

**Exact angular spectra.** For \(m=1\), each subset \(A\) of \(k\) leaves determines one vertex, of normal-cone probability
\[
p_A=\frac{k!(n-k)!}{(n+1)!}=\frac1{(n+1)\binom nk}.
\]
For every \(m\ge2\), vertices instead correspond to ordered lists of \(k\) distinct leaves, \(0\le k\le n\). A list of length \(k\) has probability
\[
p_{k}=\frac{(n-k)!}{(n+1)!},\qquad
\#\{\text{lists of length }k\}=\frac{n!}{(n-k)!}.
\]
The normal fan, hence this spectrum, is identical for all \(2\le m\le n\). Consequently the complete power sums are
\[
\boxed{Z_{n,1}(q)=\frac1{(n+1)^q}\sum_{k=0}^n\binom nk^{1-q}},
\qquad
\boxed{Z_{n,m}(q)=\frac{n!}{((n+1)!)^q}\sum_{j=0}^n(j!)^{q-1}\quad(m\ge2).}
\]
These are exact for every real \(q>0\), including \(q=1\) by continuity.

**Two sharply different critical entropy windows.** Define \(h(x)=-x\log x-(1-x)\log(1-x)\) for \(0\le x\le1\), with \(0\log0=0\). For every fixed real \(t\), the following limits hold, with the displayed expressions interpreted continuously at \(t=0\):
\[
\boxed{\lim_{n\to\infty}\frac{H_{n,1}(1+t/n)}n
=\begin{cases}-t^{-1}\log\!\left(\int_0^1e^{-t h(x)}\,dx\right),&t\ne0,\\[2pt]\frac12,&t=0,\end{cases}}
\]
and, uniformly for every choice \(2\le m=m(n)\le n\),
\[
\boxed{\lim_{n\to\infty}\frac{H_{n,m}(1+t/(n\log n))}{n\log n}
=\begin{cases}-t^{-1}\log\!\left(\frac{1-e^{-t}}t\right),&t\ne0,\\[2pt]\frac12,&t=0.\end{cases}}
\]
Here each Rényi index is positive for all sufficiently large \(n\). In particular, for every *fixed* \(q\in(0,1)\), \(q=1\), or \(q>1\), respectively,
\[
\lim_{n\to\infty}\frac{H_{n,1}(q)}n
=\begin{cases}\log2,&q<1,\\1/2,&q=1,\\0,&q>1,\end{cases}\qquad
\lim_{n\to\infty}\frac{H_{n,m}(q)}{n\log n}
=\begin{cases}1,&q<1,\\1/2,&q=1,\\0,&q>1.\end{cases}
\]
The second statement remains uniform over all choices \(m(n)\ge2\). Thus the geometric Rényi transition is resolved in a window of size \(1/n\) for the initial graphical zonotope, but size \(1/(n\log n)\) after the first triangle simplices are added.

**Collision comparison.** Two independent Gaussian objectives select the same vertex with probabilities
\[
C_{n,1}=\frac{n!}{((n+1)!)^2}\sum_{k=0}^n k!(n-k)!,\qquad
C_{n,m}=\frac{n!}{((n+1)!)^2}\sum_{j=0}^n j!\quad(m\ge2).
\]
They satisfy \((n+1)^2 C_{n,1}\to2\) and \((n+1)^2 C_{n,m}\to1\). In particular, at the first angular refinement the collision probability is asymptotically halved, even though both constructions have the same uniform law for the number of leaves ranked above the hub.

## Assumptions and scope
All coordinates are given the standard Euclidean inner product, restricted to the hyperplane orthogonal to \((1,\ldots,1)\); the choice of positive coefficients of the simplex summands does not change the normal fan. An isotropic Gaussian direction in that hyperplane has the same coordinate ordering as \((g_0,\ldots,g_n)\) with independent standard Gaussian entries, because orthogonal projection subtracts their mean. Therefore each strict coordinate ordering has probability \(1/(n+1)!\). The probability \(p_v\) is the normalized solid angle of the intrinsic outer normal cone at \(v\). The parameter \(m=1\) is the star graphical zonotope; \(m=n\) is the standard graph-associahedron (stellohedron), up to the singleton-translation convention. No affine-distortion invariance of these Euclidean angles is asserted.

## Proof
**1. Winner-pattern partition.** Each connected non-singleton induced subgraph of the star is \(S=\{0\}\cup A\), \(A\ne\varnothing\). A generic linear functional is uniquely maximized on \(\Delta_S\) at the coordinate with largest score in \(S\). The normal fan of a Minkowski sum is the common refinement of the summands' normal fans: two strict braid chambers belong to the same full-dimensional normal cone precisely when every included simplex has the same maximizing coordinate. This follows directly from additivity of support functions and uniqueness of each summand's generic maximizing vertex.

Let \(L=\{i\ge1:g_i>g_0\}\) and \(k=|L|\). For \(m=1\), the only nonsingleton simplices are \(\Delta_{\{0,i\}}\); their winners record exactly the subset \(L\). For \(m\ge2\), all \(\Delta_{\{0,i,j\}}\) are also present. Those triples record the relative order of any two leaves in \(L\), while the pairs record membership in \(L\). Conversely, once the decreasing ordered list \((i_1,\ldots,i_k)\) of elements of \(L\) is fixed, the winner in any included \(\Delta_{\{0\}\cup A}\) is the first \(i_s\) belonging to \(A\), if it exists, and otherwise \(0\). So the order of leaves below the hub cannot change any winner. Both descriptions are exact, not merely upper bounds, because different winner-patterns correspond to distinct maximal cones of the common-refinement fan. All these patterns are realized by strict coordinate orders.

**2. Gaussian cone masses.** With \(L\) fixed and \(|L|=k\), exactly \(k!(n-k)!\) full coordinate orders put those leaves above the hub, giving the first angle formula. With an ordered high list fixed, the \(n-k\) lower leaves can be arranged in exactly \((n-k)!\) orders; this gives the second formula and its \(n!/(n-k)!\) multiplicity. The total probability mass of each length class \(k\) is \(1/(n+1)\) in both constructions, since the hub's rank is uniform. Summing powers of the cone probabilities proves both finite formulas for \(Z_{n,m}(q)\), including the exact collision probabilities at \(q=2\).

**3. Critical window for the graphical zonotope.** For \(q_n=1+t/n\), the first power sum can be rewritten exactly as
\[
Z_{n,1}(q_n)=(n+1)^{-t/n}\frac1{n+1}\sum_{k=0}^n\exp\!\left(-t\frac{\log\binom nk}{n}\right).
\]
Uniform elementary Stirling bounds give \(\log\binom nk/n=h(k/n)+O(\log(n+1)/n)\) for all \(0\le k\le n\). Riemann-sum convergence proves \(Z_{n,1}(q_n)\to\int_0^1e^{-t h(x)}dx\). Dividing \(\log Z\) by \(1-q_n=-t/n\) gives the stated limit for \(t\ne0\). For \(t=0\) the exact Shannon formula is
\[
H_{n,1}(1)=\log(n+1)+\frac1{n+1}\sum_{k=0}^n\log\binom nk.
\]
Since \(\int_0^1h(x)\,dx=1/2\), this gives \(H_{n,1}(1)/n\to1/2\), also the continuous value of the critical curve at zero.

**4. Critical window for the refined star fan.** At \(q_n=1+t/(n\log n)\), group vertices by \(j=n-k\). The group mass at \(q=1\) is exactly \(1/(n+1)\), so
\[
Z_{n,m}(q_n)=\frac1{n+1}\sum_{j=0}^n\exp\!\left(\frac{t}{n\log n}[\log(j!)-\log((n+1)!)]\right),\qquad m\ge2.
\]
Uniformly for \(0\le j\le n\), one has \(\log(j!)/(n\log n)=j/n+O(1/\log n)\), by comparing \(\log(j!)\) with \(j\log j\) and using the boundedness of \(x\log x\) on \([0,1]\). Also \(\log((n+1)!)/(n\log n)\to1\). Hence this is a Riemann sum for \(\int_0^1e^{t(x-1)}dx=(1-e^{-t})/t\). Divide its logarithm by \(1-q_n\) as above. At \(t=0\), exact differentiation of the finite power sum yields
\[
H_{n,m}(1)=\log(n+1)+\frac1{n+1}\sum_{r=1}^n r\log r
=\frac n2\log n-\frac n4+O(\log n).
\]
Thus the limiting value is again \(1/2\). Fan independence proves uniformity in \(m\ge2\).

**5. Fixed-index phase profiles and collisions.** For the graphical zonotope, if \(0<q<1\), the largest binomial coefficient and the \(n+1\) summands sandwich \(\log\sum_k\binom nk^{1-q}\) between \((1-q)n\log2-O(\log n)\) and \((1-q)n\log2+O(\log n)\). For fixed \(q>1\), \(\sum_k\binom nk^{1-q}\to2\): fix an integer \(K>1/(q-1)\), split off the first/last \(K\) indices, and bound the central \(n-2K+1\) terms using \(\binom nk\ge\binom nK\). These prove the fixed-index limits for \(m=1\).

For \(m\ge2\), when \(q<1\) the sum \(\sum_{j=0}^n(j!)^{q-1}\) converges to a finite positive constant, and Stirling's formula gives \(H_{n,m}(q)/(n\log n)\to1\). For fixed \(q>1\), \(\sum_{j=0}^n(j!/n!)^{q-1}\to1\), by an analogous split into the last \(K\) factorials and the remaining terms; thus \(H_{n,m}(q)=[q/(q-1)]\log(n+1)+o(1)\). The Shannon limits were proved in Steps 3 and 4.

Finally, \(\sum_{k=0}^n\binom nk^{-1}=2+O(1/n)\), since the two endpoint terms equal one and the interior terms are bounded using \(\binom n1=n\), \(\binom n2=n(n-1)/2\). Likewise \(\sum_{j=0}^n j!/n!=1+O(1/n)\). Substitution in the exact \(q=2\) power sums proves the two collision limits.

## Verification
The standalone \(checker.py\) enumerates all strict coordinate orders for each \(1\le n\le6\), directly maximizes the included simplices, checks that the resulting vertices coincide exactly with the stated subset or partial-permutation classes, and checks each normal-cone probability by exact rational arithmetic. It also recomputes the two exact collision sums and checks the critical-window Riemann sums numerically for larger finite dimensions. Run \(\texttt{python3 checker.py}\) with only the Python standard library. The finite tests are independent consistency checks; all \(n\), all permissible \(m\), all real \(q>0\), and the asymptotic limits are proved analytically above.

## Relationship to prior work
Pešović and Stojadinović (arXiv:2209.12053v1, first posted 2022-09-24), Definition 2.1 and Example 3.6, construct the graph-polytope interpolation and identify its star-graph fan stabilization; the latter is prior work. Postnikov, Reiner, and Williams (arXiv:math/0609184, Section 10.4) identify stellohedral vertices with partial permutations and give their number. Cardinal, Merino, and Mütze (arXiv:2106.16204, Introduction Section 1.5) also describe star elimination trees as partial permutations. General braid-fan/poset descriptions can recover the elementary angular multiplicities. The claim here is the jointly quantified complete angular power-sum comparison and, especially, the **two distinct shrinking Rényi critical windows** and their explicit crossover functions, not new fan combinatorics, partial-permutation enumeration, or an independence/certification claim.

## Limitations
Only this canonical coordinate Euclidean metric and isotropic direction model are treated; nonisotropic Gaussian objectives can change the probabilities. The distributional claims are over exposed vertices, not over uniformly sampled vertices. The source literature provides general normal-fan machinery from which the elementary finite angle counts can be derived; the originality claim is restricted to the explicit angular Rényi crossover and its two different critical scales. No inference of bibliographic uniqueness is made from unsuccessful searches. Independent validation is not asserted.

## References
1. Marko Pešović and Tanja Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053v1 (2022), Definition 2.1, Example 3.6, Theorem 3.12.
2. Alexander Postnikov, Victor Reiner, and Lauren Williams, *Faces of Generalized Permutohedra*, arXiv:math/0609184v2 (2007), especially Sections 3, 6, 8 and 10.4.
3. Jean Cardinal, Arturo Merino, and Torsten Mütze, *Combinatorial generation via permutation languages. IV. Elimination trees*, arXiv:2106.16204 (first posted 2021-06-30), especially Section 1.5.
