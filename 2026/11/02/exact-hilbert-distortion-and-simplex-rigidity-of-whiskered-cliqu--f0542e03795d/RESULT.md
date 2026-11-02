# Exact Hilbert distortion and simplex rigidity of whiskered cliques

## Finding

For every integer \(n\ge 2\), let \(H_n\) be the graph obtained by adjoining a distinct private leaf \(b_i\) to each vertex \(a_i\) of a complete graph on \(n\) vertices. Give its \(2n\) vertices the unit-edge shortest-path metric \(d\). Its exact least distortion into **any real Hilbert space** is
\[
\boxed{c_2(H_n)=\frac{3}{1+\sqrt{2n/(n-1)}}.}
\]
Every optimal embedding, after scaling to be noncontracting, is congruent to the following explicit configuration:
\[
p_i=\frac{c_2(H_n)}{\sqrt2}\left(e_i-\frac1n\mathbf1\right),\qquad
q_i=\frac3{\sqrt2}\left(e_i-\frac1n\mathbf1\right)
\quad(1\le i\le n),
\]
where \(a_i\mapsto p_i\), \(b_i\mapsto q_i\) and the vectors lie in the real zero-sum hyperplane. In particular, the affine dimension of **every** optimal configuration is exactly \(n-1\). The exact distortions increase strictly with \(n\), from \(1\) when \(n=2\), and converge to \(3/(1+\sqrt2)=3(\sqrt2-1)\).

## Assumptions and scope

Here \(H_n=K_n\odot K_1\), with a **single pendant vertex attached to every clique vertex**, for every integer \(n\ge2\). The unordered pair distances are \(d(a_i,a_j)=1\) and \(d(b_i,b_j)=3\) for \(i\ne j\), \(d(a_i,b_i)=1\), and \(d(a_i,b_j)=2\) for \(i\ne j\). All graph edges have length one. The distortion \(c_2(X)\) is the infimum over injective maps \(f\) into real Hilbert spaces of the ratio of their largest and smallest values of \(\|f(x)-f(y)\|/d(x,y)\) over distinct points. A map is **noncontracting** when all these ratios are at least \(1\); an optimal noncontracting map has largest ratio exactly \(c_2(X)\). Congruence permits Hilbert isometries between the affine spans, including translations.

## Proof

Write \(c_n=3/(1+\sqrt{2n/(n-1)})\) and \(A=(n-1)/(2n)\). Observe that \(1\le c_n<3\), and
\[
 c_n^2=A(3-c_n)^2. \tag{1}
\]

**Lower bound for arbitrary Hilbert embeddings.** Take any embedding \(f\), rescale it to be noncontracting, and let \(C\) be its largest pairwise expansion factor. Write \(P_i=f(a_i)\), \(Q_i=f(b_i)\), and \(\overline P=n^{-1}\sum_iP_i\), \(\overline Q=n^{-1}\sum_iQ_i\). Set
\[
V_P=\frac1n\sum_i\|P_i-\overline P\|^2,\qquad
V_Q=\frac1n\sum_i\|Q_i-\overline Q\|^2,\qquad
W=\frac1n\sum_i\|Q_i-P_i\|^2.
\]
The exact Hilbert variance identity and the corresponding graph-pair distances imply
\[
V_P=\frac1{n^2}\sum_{i<j}\|P_i-P_j\|^2\le A C^2,
\quad
V_Q=\frac1{n^2}\sum_{i<j}\|Q_i-Q_j\|^2\ge9A,
\quad W\le C^2. \tag{2}
\]
The reverse triangle inequality in the Hilbert space of \(n\)-tuples, combined with the centroid decomposition, gives
\[
W=\|\overline Q-\overline P\|^2
 +\frac1n\sum_i\|(Q_i-\overline Q)-(P_i-\overline P)\|^2
\ge(\sqrt{V_Q}-\sqrt{V_P})^2. \tag{3}
\]
If \(C\ge3\), then \(C\ge c_n\) immediately. If \(C<3\), the bounds in (2) force \(\sqrt{V_Q}-\sqrt{V_P}\ge\sqrt A(3-C)>0\). Consequently \(C^2\ge A(3-C)^2\), hence \(C\ge3\sqrt A/(1+\sqrt A)=c_n\). This argument never assumes symmetry, a target dimension, or a particular embedding form.

**Sharp construction.** Set \(u_i=e_i-n^{-1}\mathbf1\in\mathbb R^n\), so \(\sum_i u_i=0\), \(\|u_i-u_j\|^2=2\) for \(i\ne j\), and \(\|u_i\|^2=(n-1)/n\). Put \(p_i=c_n u_i/\sqrt2\), \(q_i=3u_i/\sqrt2\). Distinct core points have Euclidean distance \(c_n\); distinct leaf points have distance \(3\); and a matched core-leaf pair has squared distance
\[
 \|q_i-p_i\|^2=A(3-c_n)^2=c_n^2.
\]
For \(i\ne j\), direct expansion using \(\langle u_i,u_j\rangle=-1/n\) yields
\[
 \|p_i-q_j\|^2=A(c_n^2+9)+\frac{3c_n}{n}=c_n^2+3c_n.
\]
As \(c_n\ge1\), one has \(4\le c_n^2+3c_n\le4c_n^2\). Therefore every pairwise ratio lies in \([1,c_n]\), with both endpoints realized, proving exact attainment.

**Rigidity of all optimizers.** If a noncontracting embedding attains \(C=c_n\), then equality holds throughout (2) and (3) and in \(c_n^2=A(3-c_n)^2\). Every distinct core pair must be exactly \(c_n\) apart, every distinct leaf pair exactly \(3\) apart, and every matched pair exactly \(c_n\) apart. Equality in the centroid decomposition forces \(\overline P=\overline Q\); equality in the reverse triangle inequality forces
\[
Q_i-\overline Q=\frac3{c_n}(P_i-\overline P)\quad \text{for every }i.
\]
The centered core vertices form a regular \((n-1)\)-simplex with edge length \(c_n\), uniquely determined up to Hilbert isometry. Their leaf partners are the stated homothetic simplex. Thus every optimal configuration is congruent to the construction and has affine dimension exactly \(n-1\).

The formula is strictly increasing in integer \(n\ge2\) because \(2n/(n-1)\) decreases strictly; taking \(n\to\infty\) proves the limit.

## Verification

Run `python checker.py` using the included standalone Python 3 script. It checks the defining quadratic-field identity exactly over rational coefficients for every integer \(2\le n\le100\), and independently recomputes all unordered pair distances in the explicit Euclidean configuration for \(2\le n\le17\) using high-precision arithmetic. Expected output:

`CHECK_OK exact_field_and_high_precision_assertions=693 exhaustive_coordinate_pairs=3416 n_exact=2..100 n_coordinate=2..17`

The finite enumerations are consistency checks, **not** an infinite proof; the full range is covered by the elementary Hilbert-space argument above. An external or independent mathematical audit has not been performed.

## Relationship to prior work

Robertson's *Negative type and bi-lipschitz embeddings into Hilbert space* (first public September 27, 2023, arXiv:2309.16070v1) gives the distorted-negative-type framework and explicit distortion calculations for complete bipartite graphs and Hamming cubes. This proof instead treats the complete-graph one-leaf corona, which is neither of those metric families, and establishes uniqueness of every optimal realization. Baskoro–Obata's *Determining finite connected graphs along the quadratic embedding constants of paths* (first public April 17, 2019, arXiv:1904.08059v1) studies quadratic embedding constants of graph distance matrices; those constants do not themselves evaluate minimum Hilbert distortion of the original distance metric. The later *Quadratic Embedding Constants of Corona Graphs* (arXiv:2512.17258, 2025) likewise addresses quadratic embedding constants rather than the two-sided optimal distortion studied here. This comparison does not establish absolute historical priority.

## Limitations

The theorem concerns **metric distortion**, not the Banach–Mazur distance of a Lipschitz-free space or the supremal exponent of negative type. The private-leaf multiplicity is one, the core is a complete graph, all edge lengths are one, and Hilbert targets are real. Weighted coronas, general base graphs, other target norms, and larger leaf multiplicities are not classified here. A related 2014 source on Euclidean graph-distance matrices was accessible only at the abstract level, leaving a historical-priority risk; no claim of independent novelty certification is made.

## References

1. Gavin Robertson, *Negative type and bi-lipschitz embeddings into Hilbert space*, arXiv:2309.16070v1 (public September 27, 2023), https://arxiv.org/abs/2309.16070.
2. Edy Tri Baskoro and Nobuaki Obata, *Determining finite connected graphs along the quadratic embedding constants of paths*, arXiv:1904.08059v1 (public April 17, 2019), https://arxiv.org/abs/1904.08059.
3. Ferdi, Edy Tri Baskoro, Nobuaki Obata, and Aditya Purwa Santika, *Quadratic Embedding Constants of Corona Graphs*, arXiv:2512.17258 (public December 2025), https://arxiv.org/abs/2512.17258.
4. A. Jaklič and J. Modic, *Euclidean graph distance matrices of generalizations of the star graph*, Applied Mathematics and Computation (2014), DOI:10.1016/j.amc.2013.12.158; full text not verified.
