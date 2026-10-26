# Exact strict two-leader coherence ranking on \(q\)-ary Hamming graphs

## Finding
For every pair of integers \(q\ge2\) and \(d\ge2\), consider the unweighted Hamming graph \(H(d,q)=K_q^{\square d}\). Fix exactly two distinct noise-free leader vertices and ground their states. Write \(J_k\) for the trace of the followers' grounded Laplacian inverse when the leaders have Hamming distance \(k\), for \(1\le k\le d\). The **entire distance-class ranking is strictly ordered**:
\[
 J_1>J_2>\cdots>J_d.
\]
Consequently the precisely optimal leader pairs differ in all \(d\) coordinates, and their number is \(q^d(q-1)^d/2\). The optimal-pair location alone is anticipated by an earlier general discussion of resistance-maximizing leader pairs; the distinct contribution here is the strict ordering of **every** intermediate Hamming-distance class, together with exact rational costs and a proof of strictness.

Put \(N=q^d\), \(h(t)=1+(q-1)t\), and for each \(k\in\{1,\ldots,d\}\) define
\[
 D_k(t)=h(t)^d-(1-t)^k h(t)^{d-k},\quad
 A_k=\int_0^1\!\frac{D_k(t)}t\,dt,\quad
 B_k=\int_0^1\!\frac{-\log t}{t}D_k(t)\,dt,
\]
and
\[
 a_d=\frac{1}{Nq}\sum_{j=1}^d\frac{\binom dj(q-1)^j}{j}.
\]
The exact rational coherence cost is
\[
 \boxed{J_k=2Na_d-\frac{A_k}{2q}-\frac{B_k}{qA_k}.}
\]
Although written as integrals, the coefficients are exact finite rational sums. Indeed, if \(D_k(t)=\sum_{j=1}^d c_{k,j}t^j\), then \(A_k=\sum_{j=1}^d c_{k,j}/j\) and \(B_k=\sum_{j=1}^d c_{k,j}/j^2\), with
\[
 c_{k,j}=\binom dj(q-1)^j-
 \sum_{\ell=\max(0,j-d+k)}^{\min(j,k)}
 (-1)^\ell\binom k\ell\binom{d-k}{j-\ell}(q-1)^{j-\ell}.
\]

## Assumptions and scope
The vertices are words in \(\{0,\ldots,q-1\}^d\); an edge joins words differing in exactly one coordinate and has conductance one. Let \(L\) denote the standard combinatorial graph Laplacian. For distinct grounded leaders \(S=\{u,v\}\), the remaining principal submatrix \(L_{FF}\), indexed by \(F=V\setminus S\), is strictly positive definite because the graph is connected. Define \(J(S)=\operatorname{tr}(L_{FF}^{-1})\). In unit-intensity independent follower white noise consensus, the total stationary variance is \(J(S)/2\); that factor does not change optimality. No edge reweighting, noise on leaders, leader penalties, or three-or-more-leader classification is asserted. The strict ranking is for all integers \(d,q\ge2\), including the boundary case \(H(2,2)\).

## Proof
**1. An exact two-terminal identity.** For a connected undirected graph write \(R_{xy}\) for effective resistance and \(L^+\) for its Laplacian pseudoinverse. If both \(u,v\) are grounded, the effective resistance from a third vertex \(z\) to this common ground is
\[
 R_{z,\{u,v\}}=\frac{R_{zu}+R_{zv}}2-\frac{R_{uv}}4-\frac{(R_{zu}-R_{zv})^2}{4R_{uv}}.
\]
For completeness, this identity follows by replacing the three terminals with their unique equivalent three-arm resistor star: its arm resistances are \((R_{zu}+R_{zv}-R_{uv})/2\), \((R_{zu}+R_{uv}-R_{zv})/2\), and \((R_{zv}+R_{uv}-R_{zu})/2\); the latter two arms are then in parallel when \(u,v\) are shorted. Also \((L_{FF}^{-1})_{zz}=R_{z,\{u,v\}}\), so \(J=\sum_{z\in V}R_{z,\{u,v\}}\), where grounded terms vanish. Vertex transitivity makes \(L^+_{xx}=a_d\) and \(((L^+)^2)_{xx}=b_d\) independent of \(x\). With \(c_{uv}=((L^+)^2)_{uv}\), the row-sum-zero identities give
\[
 J(u,v)=2Na_d-\frac{N R_{uv}}4-\frac{2(b_d-c_{uv})}{R_{uv}}.
\]
In detail \(\sum_z R_{zu}=2Na_d\) and \(\sum_z(R_{zu}-R_{zv})^2=8(b_d-c_{uv})\).

**2. Product-spectrum evaluation.** Fourier characters of the \(q\)-ary word group diagonalize the graph Laplacian: a character supported on \(j\) coordinates has eigenvalue \(qj\), with multiplicity \(\binom dj(q-1)^j\). If the two words differ in precisely \(k\) coordinates, the character-weight generating polynomial is
\[
 \sum_{\chi}(1-\operatorname{Re}\chi(u-v))t^{|\operatorname{supp}\chi|}=D_k(t).
\]
The identity follows by multiplying the contributions \(h(t)\) of equal coordinates and \(1-t\) of unequal coordinates for the character sum, then subtracting from \(h(t)^d\). Since \(\int_0^1t^{j-1}\,dt=1/j\) and \(\int_0^1(-\log t)t^{j-1}\,dt=1/j^2\), the spectral resolutions of \(L^+\) and \((L^+)^2\) yield
\[
 R_{uv}=\frac{2A_k}{Nq},\quad b_d-c_{uv}=\frac{B_k}{Nq^2},\quad L^+_{uu}=a_d.
\]
Substitution in Step 1 proves the boxed exact formula. The finite coefficient expression above follows from the binomial theorem, and no limiting interchange is necessary because all sums are finite.

**3. Strict separation monotonicity.** For \(0<t<1\) put \(\rho(t)=(1-t)/h(t)\). It lies in \((0,1)\) and strictly decreases as \(t\) increases. Set \(w_k(t)=D_k(t)/t=h(t)^d(1-\rho(t)^k)/t>0\). Then \(w_{k+1}(t)>w_k(t)\) pointwise, proving \(A_{k+1}>A_k\). Moreover,
\[
 \frac{w_{k+1}(t)}{w_k(t)}
 =1+\frac{\rho(t)^k}{1+\rho(t)+\cdots+\rho(t)^{k-1}}.
\]
For every integer \(k\ge1\), the fraction on the right equals \(\bigl(\sum_{j=1}^k\rho^{-j}\bigr)^{-1}\), strictly increasing in \(\rho\), hence the ratio of densities is strictly **decreasing** in \(t\). Under the probability density \(w_k/A_k\), the expectation of \(-\log t\) is \(B_k/A_k\). Reweighting by the strictly decreasing positive factor \(w_{k+1}/w_k\) strictly increases the expectation of the also strictly decreasing function \(-\log t\): this follows from the strict positive covariance identity
\[
 2\operatorname{Cov}(f,g)=\iint(f(t)-f(s))(g(t)-g(s))\,d\mu(t)\,d\mu(s)>0.
\]
Therefore \(B_{k+1}/A_{k+1}>B_k/A_k\). Both subtracted quantities in the exact formula strictly increase with \(k\), so \(J_{k+1}<J_k\). Hamming graph automorphisms act transitively on ordered vertex pairs at fixed distance. Thus this strict cost ranking covers *all* unordered leader pairs, not only chosen representatives. Finally each vertex has exactly \((q-1)^d\) antipodes, so unordered optimal pairs number \(q^d(q-1)^d/2\).

## Verification
Run `python verify.py` after installing `requirements.txt` from the same directory. The standalone exact checker independently forms the grounded Laplacian for seven small Hamming graphs and compares the exact rational inverse traces with the formula at every distance. It also performs 147 strict exact rational comparisons for \(2\le q\le8\), \(2\le d\le7\), and seven exhaustive antipode-pair count checks. Its recorded output appears in `verification_output.txt`. Finite checks corroborate but are not used as a proof for unbounded \(q,d\); Step 3 supplies the universal proof.

## Relationship to prior work
Fitch and Leonard's 2013 conference paper and 2014 arXiv full paper establish joint centrality and exact two-leader pseudoinverse-based performance formulas. In Section V-C of the full paper they further assert that when all vertices have equivalent information centrality an optimal two-leader pair maximizes resistance distance. That general *maximizer-location* statement anticipates the fact that antipodal Hamming pairs are optimal. **The location or two-terminal pseudoinverse formula alone is not claimed new here.** The presently differentiated contribution is that *every one* of the \(d\) Hamming-distance strata has a distinct coherence cost in one strict order, with an exact rational formula and a direct positive-density proof. A general optimal-pair statement does not specify or imply all pairwise inequalities between suboptimal strata. Patterson, Yi, and Zhang (2017) subsequently derive resistance formulations and optimize leaders on paths, cycles, and trees; the inspected material does not give the stated \(q\)-ary Hamming graph all-distance ranking. A targeted comparison did not find an identical strict ordering, but literature coverage can be incomplete.

## Limitations
The graph factors must all be identical unit-conductance complete graphs, exactly two leaders must be noise-free, and the objective is grounded inverse trace. The result gives the full unweighted \(q\)-ary Hamming family and no claim about arbitrary Cartesian factors or nonuniform edge weights. Prior work already anticipates the *optimal locations*, so originality rests on the strict total distance-class ranking and its exact rational costs. Absence of a matching result in searches does not demonstrate absolute novelty. The present verification is mathematical plus exact finite checking; no independent audit has been performed.

## References
- Katherine E. Fitch and Naomi Ehrich Leonard, *Information Centrality and Optimal Leader Selection in Noisy Networks*, Proceedings of the IEEE Conference on Decision and Control (2013), author's PDF: https://naomi.princeton.edu/wp-content/uploads/sites/744/2021/03/FitchCDC2013ol.pdf .
- Katherine E. Fitch and Naomi Ehrich Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, initially public 2014-07-07, especially Sections IV–V and V-C. https://arxiv.org/abs/1407.1569 .
- Stacy Patterson, Yuhao Yi, and Zhongzhi Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (2017), especially Sections II–IV. https://arxiv.org/abs/1708.06873 .
