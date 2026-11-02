# Strict blade-majorization of generalized roundness in heterogeneous clique bouquets

## Finding
For \(m\ge2\) and \(N\ge m+2\), consider a clique bouquet with one shared hub and \(m\) peripheral cliques of sizes \(k_1,\ldots,k_m\ge1\), with total \(N\). Its shortest-path metric has distance \(1\) within a clique or from hub to peripheral vertex and distance \(2\) between different peripheral cliques. Write \(\wp(k)\) for the supremal exponent of negative type, equivalently generalized roundness.

Define \(q_k>2\) as the unique root of
\[
F_k(q):=(q-2)\sum_{i=1}^{m}\frac{k_i}{1+(q-1)k_i}=1.
\]
Then \(\wp(k)=\log_2 q_k\). More importantly, **the exponent is strictly increasing under nontrivial majorization of blade sizes**: if \(k\) majorizes \(\ell\), \(\sum_i k_i=\sum_i\ell_i=N\), and they are not permutations, then \(\wp(k)>\wp(\ell)\).

Let \(b\) have \(N\bmod m\) entries equal to \(\lceil N/m\rceil\), and the remaining entries equal to \(\lfloor N/m\rfloor\). Let \(u=(N-m+1,1,\ldots,1)\). Among all integer blade distributions with fixed \((m,N)\), the minimum of \(\wp\) is attained **only** at permutations of \(b\), and the maximum **only** at permutations of \(u\). The two endpoints differ because \(N\ge m+2\).

The critical exponent is attained in the sense of non-strict negative type with an explicitly one-dimensional equality space. For \(p=\wp(k)\), the snowflaked metric \(d^{p/2}\) embeds isometrically in real Euclidean dimension \(N-1\), and this dimension is minimal. At every \(0<p<\wp(k)\), the least dimension is \(N\).

For example, for \((m,N)=(3,6)\), the minimum, intermediate and maximum exponents arise from \((2,2,2)\), \((1,2,3)\), \((1,1,4)\) respectively:
\[
\log_2(2.75)\approx1.459431619
<1.480148724<1.510144655.
\]

## Assumptions and scope
The finite simple graph is \(G(k)=K_1\vee(K_{k_1}\sqcup\cdots\sqcup K_{k_m})\). All edges have length one, the metric is the usual shortest-path metric on the **vertex set only**, and \(m\ge2\), \(k_i\in\mathbb Z_{\ge1}\), \(N=\sum_i k_i\ge m+2\). The conventions for negative type are: for \(p\ge0\), every nonzero real \(z\in\mathbb R^{N+1}\) with \(\sum z=0\) must satisfy
\[
\sum_{x,y\in V(G)}d(x,y)^p z_xz_y\le0,
\]
with \(d(x,x)^p=0\) and \(d(x,y)^0=1\) for distinct vertices. Strict negative type replaces \(\le0\) by \(<0\).

A vector \(k\) majorizes \(\ell\) when, after sorting each in nonincreasing order, all initial partial sums of \(k\) are at least those of \(\ell\), and their totals agree. Majorization becomes **strict** here if the vectors are not permutations.

## Proof
Let \(q=2^p\). Write \(s_i=\sum_{v\in B_i}z_v\) for the sum in peripheral blade \(B_i\), and \(s=\sum_i s_i\). The hub coefficient is \(z_o=-s\). Separate the ordered pairs at distances one and two. A direct expansion yields the exact identity
\[
Q_p(z)=\sum_{x,y}d(x,y)^p z_xz_y
=-\sum_{v\ne o}z_v^2+(1-q)\sum_i s_i^2+(q-2)s^2.
\]
This identity also follows by taking the all-off-diagonal-one form \(-\sum_x z_x^2\), and adding \((q-1)\) times the quadratic contribution of pairs in different peripheral blades.

By Cauchy--Schwarz inside each blade,
\[
\sum_{v\in B_i}z_v^2\ge\frac{s_i^2}{k_i},
\]
with equality if and only if all coefficients within that blade coincide. Hence
\[
Q_p(z)\le-\sum_{i=1}^m a_i(q)s_i^2+(q-2)\left(\sum_i s_i\right)^2,
\qquad a_i(q)=q-1+\frac1{k_i}.
\]
For \(q\le2\), the last term is nonpositive and the form is strictly negative on nonzero zero-sum vectors. For \(q>2\), weighted Cauchy--Schwarz gives
\[
\left(\sum_i s_i\right)^2\le\left(\sum_i\frac1{a_i(q)}\right)
\left(\sum_i a_i(q)s_i^2\right).
\]
Both Cauchy--Schwarz equalities can be attained simultaneously. Consequently, the full metric has \(p\)-negative type exactly if
\[
(q-2)\sum_i\frac1{a_i(q)}=F_k(q)\le1.
\]
Every summand of \(F_k\) increases strictly in \(q>2\), because
\[
\frac{d}{dq}\frac{q-2}{q-1+1/k_i}
=\frac{1+1/k_i}{(q-1+1/k_i)^2}>0.
\]
Moreover, \(F_k(2)=0\) and \(\lim_{q\to\infty}F_k(q)=m>1\). This proves the existence and uniqueness of \(q_k\), the exact exponent and strictness below it.

At \(q=q_k\), equality in the two Cauchy--Schwarz inequalities forces a one-dimensional space: choose \(s_i=1/a_i(q_k)\), distribute these equally inside blade \(i\), giving peripheral coefficient \(1/[1+(q_k-1)k_i]\), and set the hub coefficient to the negative sum. All equalities are then sharp; no other nonzero equality direction exists. Schoenberg's negative-type-to-Hilbert embedding theorem and the rank of the centered squared-distance matrix give minimal dimensions \(N-1\) at the critical exponent and \(N\) below it, since there are \(N+1\) vertices.

It remains to compare blade-size vectors. For fixed \(q>2\), the function
\[
h_q(x)=\frac{x}{1+(q-1)x}
\]
is strictly concave for \(x>0\), with
\[
h_q''(x)=-\frac{2(q-1)}{[1+(q-1)x]^3}<0.
\]
A nontrivial balancing transfer, replacing two integer blade sizes \((a,b)\) with \((a-1,b+1)\) for \(a\ge b+2\), strictly increases \(\sum_i h_q(k_i)\). An explicit finite-difference verification is
\[
h_q(b+1)-h_q(b)=\frac1{[1+(q-1)b][1+(q-1)(b+1)]},
\]
which strictly decreases with \(b\). Thus balancing strictly increases \(F_k(q)\) at every \(q>2\), and since each \(F_k\) is strictly increasing in \(q\), strictly decreases the unique root \(q_k\). Integer majorization is generated by such transfers. The unique most balanced integer vector is \(b\); the unique maximally majorizing vector is \(u\), up to permutations. Their strict extremal characterization follows. This proves every assertion.

## Verification
The included Python 3 standard-library program `verify.py` constructs full distance-power matrices and independently diagonalizes their restrictions to the zero-sum subspace by a Jacobi eigensolver, without using the closed-form secular proof for these matrix calculations. It covers \(131\) sorted integer blade vectors with \(2\le m\le5\), \(m\le N\le\min(m+7,12)\), tests five exponents per vector, verifies the critical zero eigenvalue and an explicit equality vector, and compares all fixed-\((m,N)\) balanced/unbalanced extremizers. The actual run passed 655 eigenvalue checks and 131 exact-form witness evaluations to floating-point tolerances. This is evidence for finite cases, **not** a proof of the universal classification; the preceding argument establishes the all-integer theorem.

## Relationship to prior work
Li and Weston (arXiv:0901.0695; earliest posted 2009-01-06) establish general strict negative-type interval results, not the mixed-clique structural comparison. Sánchez (arXiv:1108.0451; 2011-08-02) provides a generic finite distance-matrix method and a closed treatment of complete bipartite graph metrics. A 2011 conference abstract by Peterson, with collaborators, **already announces a formula for generalized roundness of ordinary windmill graphs**; the ordinary windmill has equal-size cliques meeting at the hub. The homogeneous case of our secular equation should therefore be regarded as known and is **not** claimed as the advance. The result here is specifically the classification for *heterogeneous* clique blades and their strict majorization/fixed-budget optimizing law. Deza--Maehara's earlier truncated-graph metric embedding framework is a further relevant generic method. A modern study of distance characteristic polynomials of windmills concerns a different matrix invariant.

## Limitations
The theorem concerns finite vertex metrics of one-hub unions of complete graphs, all at unit edge lengths; it does not address irregular internal blade graphs, unequal edge lengths, infinite bouquets, or continuous interiors. The 2011 windmill-roundness research was located at conference-abstract level but its original full manuscript was not located, leaving a specific risk that an unpublished derivation considers heterogeneous blades. A full original text of Deza--Maehara's 1990 metric-transform paper was not available. The proof gives exact finite spectral thresholds; it does not claim new general negative-type or Euclidean-embedding principles.

## References
1. H. Li and A. Weston, *Strict \(p\)-negative type of a metric space*, arXiv:0901.0695v1, first public 2009-01-06. Full updated preprint: https://arxiv.org/html/0901.0695v3.
2. S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451v1, 2011-08-02, https://arxiv.org/html/1108.0451v1, sections 2--3.
3. J. Peterson, *Generalized Roundness of Finite Graphs*, abstract for the Penn State Conference on Undergraduate Research in Mathematics, 2011-11-04--05, https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/7/80619/files/2018/02/talk_abstracts_2011-1cj4kj2.pdf, printed p. 10. With T. Alli and K. Vissuet.
4. K. Vissuet and collaborators, *Generalized Roundness of Graphs*, Young Mathematicians Conference abstract received 2011-08-01, https://ymc.math.osu.edu/2011/docs/AbstractBooklet-comb-Aug-12.pdf. Only abstract located; full manuscript not obtained.
5. M. Deza and H. Maehara, *Metric Transforms and Euclidean Embeddings* (1990), DOI:10.2307/2001482; full text not obtained.
6. A. Abiad et al., *Extending a conjecture of Graham and Lovász on the distance characteristic polynomial*, sections 4.1--4.2, 2024. This is a distance-matrix coefficient study of block/windmill graphs, not the critical powered-distance negative type.
