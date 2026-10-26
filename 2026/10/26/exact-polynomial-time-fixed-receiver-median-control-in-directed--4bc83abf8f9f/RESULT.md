# Exact polynomial-time fixed-receiver median control in directed Friedkin–Johnsen networks

## Finding
A structural majority intervention may add at most \(K\) missing directed follow edges, **all with one prescribed tail** \(i\). Although unrestricted structural median intervention is computationally hard [1], this fixed-receiver problem has an exact polynomial-time solution on every finite loopless directed network under the strictly substochastic Friedkin–Johnsen assumptions below. More strongly, one selected set of edges simultaneously maximizes **every** componentwise nondecreasing function of the eventual opinion vector: upper or lower median, every quantile, mean, and threshold counts. The same theorem provides an exact low-rank equilibrium law and a feedback-corrected edge ranking. The result concerns a restriction of the intervention set, not an algorithm for unrestricted edge additions.

## Assumptions and scope
Let \(V=\{1,\ldots,n\}\), \(n\ge2\). Each vertex \(v\) has a nonempty set \(N_v\subseteq V\setminus\{v\}\) of outgoing neighbors and \(d_v=|N_v|\). Define \(W_{vj}=1/d_v\) for \(j\in N_v\), zero otherwise. The innate opinions satisfy \(s\in[0,1]^n\); susceptibilities satisfy \(0<\lambda_v<1\). Write \(\Lambda=\operatorname{diag}(\lambda_v)\), \(A=I-\Lambda W\), \(G=A^{-1}\), and \(z=G(I-\Lambda)s\). The unique equilibrium solves \(z=(I-\Lambda)s+\Lambda Wz\). Fix receiver \(i\), set \(E_i=V\setminus(\{i\}\cup N_i)\), \(m=|E_i|\), and choose an arbitrary \(S\subseteq E_i\) with \(|S|\le K\) (replace \(K\) by \(\min\{K,m\}\) if needed). Only row \(i\) changes, to uniform probability over \(N_i\cup S\). Let \(b_i=d_i^{-1}\sum_{j\in N_i}z_j\), and let \(h=Ge_i\), with \(h_v\ge0\). Define \(\alpha(\varnothing)=0\).

**Exact response and universal order:** For all admissible \(S\),
\[
 z^{(S)}=z+\alpha(S)h,\qquad
 \alpha(S)=\frac{\lambda_i\sum_{j\in S}(z_j-b_i)}{d_i+|S|h_i-\lambda_i\sum_{j\in S}h_j}.
\]
The denominator is positive. In particular, \(z^{(S)}\le z^{(T)}\) componentwise if \(\alpha(S)\le\alpha(T)\). Hence a maximizer of \(\alpha\) under \(|S|\le K\) maximizes every coordinatewise nondecreasing opinion statistic. This assertion does **not** say that all such statistics share *all* of their optimal solutions.

**Exact algorithm:** For each \(k=1,\ldots,K\), form the finitely many rational crossing values
\[
 \mathcal B=\left\{\frac{z_b-z_a}{h_a-h_b}:a,b\in E_i,\ a<b,\ h_a\ne h_b\right\}.
\]
For each crossing and one sample in every complementary open interval of the real line, select the \(k\) indices with largest scores \(z_j+t h_j\); evaluate their exact \(\alpha\). Compare all such candidates with the empty set. This returns a globally optimal intervention. A direct implementation takes \(O(n^3+K m^3\log m)\) exact rational arithmetic operations; for rational inputs, standard exact linear algebra and rational comparisons give polynomial bit complexity. For \(m=0\) or \(K=0\), the empty intervention is optimal.

## Proof
**Invertibility and a maximum principle.** Every row sum of \(\Lambda W\) is strictly below one, so \(A\) and all row-renormalized variants are invertible by the absolutely convergent nonnegative Neumann series. Thus \(G\ge0\), hence \(h=Ge_i\ge0\). Since
\[
 h_v=\mathbf1_{\{v=i\}}+\lambda_v\sum_jW_{vj}h_j,
\]
we have \(h_v\le\lambda_v\max_j h_j<\max_j h_j\) for every \(v\ne i\) that could attain a positive global maximum. Therefore the global maximum of \(h\) is attained at \(i\), and \(h_i\ge h_j\) for all \(j\); also \(h_i\ge1\).

**A single response direction.** Write \(k=|S|\) and \(\delta w=W^{(S)}_{i,*}-W_{i,*}\), the difference of old and new row \(i\). Direct computation gives, for any column vector \(u\),
\[
 \delta w\,u=\frac{\sum_{j\in S}u_j-kd_i^{-1}\sum_{j\in N_i}u_j}{d_i+k}.
\]
Subtracting equilibrium equations for \(z^{(S)}\) and \(z\) yields
\[
 A(z^{(S)}-z)=\lambda_i e_i(\delta w\,z^{(S)}),
\]
so \(z^{(S)}-z=\alpha h\), \(\alpha=\lambda_i\delta w\,z^{(S)}\). Substitution gives
\[
 \alpha\bigl(1-\lambda_i\delta w\,h\bigr)=\lambda_i\delta w\,z.
\]
The \(i\)-th coordinate of \(Ah=e_i\) gives \(\lambda_i d_i^{-1}\sum_{j\in N_i}h_j=h_i-1\). Consequently
\[
 (d_i+k)(1-\lambda_i\delta w\,h)
   =d_i+k h_i-\lambda_i\sum_{j\in S}h_j
   \ge d_i+k(1-\lambda_i)h_i>0.
\]
Using \(\delta w\,z=(\sum_{j\in S}z_j-kb_i)/(d_i+k)\) proves the exact formula, including for \(S=\varnothing\). Since \(h\ge0\), the comparison assertion and universal objective domination follow.

**Global optimization without enumerating edge subsets.** Fix the cardinality \(k\ge1\) and denote the numerator and denominator of \(\alpha(S)\) by \(N(S)\) and \(D(S)>0\). Let \(r=\max_{|S|=k}N(S)/D(S)\). The defining property of a fractional optimum is
\[
  N(S)-rD(S)\le0\quad\text{for all \(|S|=k\)},
\]
with equality for some maximizing set. For a fixed \(t\),
\[
 N(S)-tD(S)
 =\lambda_i\sum_{j\in S}(z_j+t h_j)-k\lambda_i b_i-t(d_i+k h_i).
\]
Thus maximizing this linearized expression over \(k\)-subsets is achieved by choosing the \(k\) largest affine scores. At \(t=r\), *every* top-scoring set has \(N(S)-rD(S)=0\), hence has ratio \(r\). The ordering of the affine scores is constant between their pairwise crossings; at a crossing, any tie-breaking produces a top-scoring set. Therefore the finite enumeration of breakpoints and their complementary intervals includes a set attaining the global best ratio for each \(k\). There are at most \(\binom m2\) crossings, and evaluating at most \(O(m^2)\) score orderings of length \(m\) costs \(O(m^3\log m)\) arithmetic per cardinality. Comparing over all \(k\le K\) and \(\varnothing\) completes the proof. The bit-size of the rational inverse and of all score crossings is polynomial in the rational input encoding size (by determinant bounds), making the procedure an exact polynomial-time algorithm.

**Feedback reverses the opinion-only ranking.** In the four-vertex network with outgoing neighborhoods
\[
 N_0=\{1,2\},\quad N_1=\{0\},\quad N_2=\{1\},\quad N_3=\{2\},
\]
let \(\lambda=(9/10,9/10,9/10,1/2)\) and \(s=(2/5,2/5,1,3/5)\). Fix receiver \(i=1\), eligible targets \(2,3\), budget one. The exact baseline is
\[
 z=\frac1{2305}(1192,1165,1279,1331),
\]
so \(z_3>z_2\). Nevertheless the scalar gain from choosing target \(2\) is \(27/1450\), while for target \(3\) it is \(1251/82550\), strictly smaller. Since \(h_i>0\), choosing target \(2\) gives a strictly larger opinion at vertex \(i\), and a weakly larger opinion at every other vertex. Thus an opinion-only choice of the highest-opinion donor can be suboptimal even with one added edge.

## Verification
The included `verify.py` uses only Python's standard-library rational arithmetic. Its deterministic tests construct and invert both baseline and perturbed FJ matrices independently, compare the exact low-rank formula against every admissible edge set for 90 small randomly generated rational graph instances, exhaustively compare the breakpoint-selection algorithm with all cardinality-constrained subsets, and verify the four-vertex ranking reversal. The completed run reported 764 cardinality-constrained optimizations and 2,155 individual exact matrix re-solves. Exact tests are finite consistency checks and do not certify the infinite family; the proof above supplies that guarantee.

## Relationship to prior work
Biondi–Boldrini–Passarella–Conti [1], the motivating October 2026 preprint, formulates structural median control under the same row-normalized directed FJ model, proves hardness when edges may be placed at multiple receivers, and offers continuous optimization plus opinion-aware heuristics. The present theorem isolates the fixed-receiver restriction and proves exact polynomial-time solvability and common optimality across all monotone statistics; its baseline rank-one inverse identity is an application of standard matrix algebra and is not independently claimed as a novel identity. The arbitrary-receiver hardness conclusion cannot be applied to the fixed-receiver family. Ristache et al. [2] change susceptibility/innate quantities instead of edges. Wang et al. [3] optimize external-influencer social power by adding edges to different regular recipients, including a special exactly tractable topology; neither their decision space nor objective is this same-tail median problem. Boudourides [4] provides a general resolvent and perturbation treatment, without a fixed-receiver combinatorial optimum. Zhu–Zhang [5] concerns leader-to-follower link recommendations optimizing total opinion and proves submodular approximation; the accessible abstract is not sufficient to eliminate all possible stronger results in the full article. Edge-sensitivity and linear-fractional subset optimization are standard mathematical tools; the claimed additional result is the complete social-network optimization consequence under this precise intervention restriction.

## Limitations
The theorem requires a *prescribed single receiver* and assumes equal weights among its outgoing neighbors and \(\lambda_v<1\) for all vertices. It does not solve arbitrary multi-receiver median edge additions, endogenous rewiring, negative weights, edge deletions, or susceptibility-one boundary cases. The claim is exact mathematical optimization, not evidence that a platform can force real-world users to accept links. Although current checked sources do not imply the full theorem, other literature may subsume it; no independent novelty audit has been conducted.

## References
[1] E. Biondi, C. Boldrini, A. Passarella, M. Conti, *Rewiring the Majority: Structural Median Opinion Control in the Friedkin-Johnsen Model*, first public 2026-10-15, arXiv:2610.21933, https://arxiv.org/abs/2610.21933 .

[2] M. Ristache et al., *Countering Election Sway: Strategic Algorithms in Friedkin-Johnsen Dynamics*, 2025, as cited and distinguished in [1].

[3] L. Wang, Y. Xing, Y. Yi, M. Cao, K. H. Johansson, *Adding links wisely: how an influencer seeks for leadership in opinion dynamics?*, arXiv:2506.12463, https://arxiv.org/abs/2506.12463 .

[4] M. Boudourides, *Friedkin-Johnsen Social Influence Dynamics on Networks: A Boundary-Value Formulation and Influenceability Measures*, arXiv:2602.08704, https://arxiv.org/abs/2602.08704 .

[5] L. Zhu and Z.-Z. Zhang, *Opinion Maximization in Social Networks via Link Recommendation*, Theoretical Computer Science 1033 (2025), article 115090, DOI:10.1016/j.tcs.2025.115090 .
