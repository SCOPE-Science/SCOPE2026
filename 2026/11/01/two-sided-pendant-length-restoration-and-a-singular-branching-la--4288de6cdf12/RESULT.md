# Two-sided pendant-length restoration and a singular branching law for bipartite corona roundness

## Finding

For each integer \(q\ge3\), start with the complete bipartite graph \(K_{q,q}\) whose core edges all have length one. Attach one private leaf by an edge of length \(t>0\) to **every** core vertex, and retain all \(4q\) vertices in the shortest-path metric \(d_{q,t}\). This is the weighted one-leaf corona, not a leaf-only submetric. Let \(\wp_q(t)\) be its supremal exponent of negative type.

Define
\[
 p_0(q)=\log_2\frac{q}{q-1},\qquad
 X_{q,t}(p)=q-(q-1)2^p,
\]
\[
 Y_{q,t}(p)=q(1+t)^p-t^p-(q-1)(t+2)^p,\qquad
 Z_{q,t}(p)=q(1+2t)^p-(q-1)(2+2t)^p,
\]
and \(\Delta_{q,t}(p)=X_{q,t}(p)Z_{q,t}(p)-Y_{q,t}(p)^2\).

**Theorem.** There is exactly one \(\wp_q(t)\in(0,p_0(q))\) such that
\[
 \boxed{\Delta_{q,t}(\wp_q(t))=0.}
\]
The metric has strict \(p\)-negative type for \(0\le p<\wp_q(t)\), non-strict \(\wp_q(t)\)-negative type, and no \(p\)-negative type for \(p>\wp_q(t)\). At its endpoint the zero-sum equality space is one-dimensional. Consequently, for positive \(p\le\wp_q(t)\) the minimal Euclidean dimension of the snowflaked metric \(d_{q,t}^{p/2}\) equals \(4q-1\) for \(p<\wp_q(t)\) and \(4q-2\) at the endpoint.

There is a **two-sided recovery law**:
\[
 \boxed{\lim_{t\downarrow0}\wp_q(t)=\lim_{t\to\infty}\wp_q(t)=p_0(q),\qquad
 \wp_q(t)<p_0(q)\quad(t>0).}
\]
Hence at least one finite, positive pendant length minimizes the exponent for each fixed \(q\ge3\). No uniqueness of that minimizing length is asserted.

The **sharp large-branching law** is, with natural logarithms,
\[
 A=\log2,\quad B(t)=\log\frac{t+2}{t+1},\quad C(t)=\log\frac{2t+2}{2t+1},
\]
\[
 \boxed{\lim_{q\to\infty}q\wp_q(t)
 =\frac{2}{A+C(t)+\sqrt{(A-C(t))^2+4B(t)^2}}=:L(t).}
\]
The two limiting operations are singular:
\[
 \boxed{\lim_{t\downarrow0}\lim_{q\to\infty}q\wp_q(t)=\frac{1}{2\log2},
 \qquad
 \lim_{q\to\infty}\lim_{t\downarrow0}q\wp_q(t)=\frac1{\log2}.}
\]
For example, \(\wp_3(1)=0.554997356983611\ldots\) whereas the unmodified \(K_{3,3}\) exponent is \(\log_2(3/2)=0.584962500721156\ldots\); and \(L(1)=1.059615674703024\ldots\).

## Assumptions and scope

All lengths are strictly positive; core edges have length one and all pendant edges have the same length \(t\). Points are **all original and pendant vertices**. For \(p>0\), \(p\)-negative type means
\[
 \sum_{x,y}\alpha_x\alpha_y d_{q,t}(x,y)^p\le0
 \quad\text{for every real }(\alpha_x)\text{ with }\sum_x\alpha_x=0.
\]
The \(p=0\) convention sets all nonzero distances to one. The standard characterization by Euclidean squared-distance matrices identifies rank of \(-\tfrac12HD^pH\), where \(H=I-\mathbf1\mathbf1^{\mathsf T}/(4q)\), with the minimal dimension of the snowflake at an admissible positive exponent. No claim is made about unbalanced cores, heterogeneous leaf lengths, or zero-length edges.

## Proof

**1. Exact distance form.** Index the two core parts by \(A,B\), each with \(q\) vertices. If two distinct core indices are in the same part, their core distance is \(2\); if in opposite parts it is \(1\). The leaf over a core index adds \(t\) to its distance from every vertex outside its own core–leaf pair; the core-to-own-leaf distance is \(t\). In particular, core–leaf distances to other cores are \(t+1\) or \(t+2\), and leaf–leaf distances are \(2t+1\) or \(2t+2\).

Write the coefficient vector as core and leaf values \(a_{J,i},\ell_{J,i}\) for \(J\in\{A,B\}\). Subtract within-part means \(\bar a_J,\bar\ell_J\), obtaining zero-mean fluctuations \(a'_{J,i},\ell'_{J,i}\). The powered-distance quadratic form \(Q_p=\sum_{x,y}\alpha_x\alpha_y d(x,y)^p\) splits orthogonally (as a quadratic form) into two within-part fluctuation sectors and two inter-part radial sectors. On each fluctuation sector it is
\[
 -2^p\sum_i(a'_{J,i})^2
 +2\bigl[t^p-(t+2)^p\bigr]\sum_i a'_{J,i}\ell'_{J,i}
 -(2t+2)^p\sum_i(\ell'_{J,i})^2. \tag{1}
\]
For \(0<p<2\), this is strictly negative unless the fluctuations vanish. Indeed, it equals the powered-distance quadratic form on a four-point collinear configuration with successive gaps \(t,2,t\), restricted to two independent zero-mean directions. The Fourier identity for \(|x-y|^p\) proves strict negative type for every finite set of distinct real points when \(0<p<2\).

**2. The two radial forms.** Put \(c_+=(\bar a_A+\bar a_B)/2\), \(c_-=(\bar a_A-\bar a_B)/2\), and \(h_-=(\bar\ell_A-\bar\ell_B)/2\). The overall zero-sum condition forces \((\bar\ell_A+\bar\ell_B)/2=-c_+\). Direct substitution gives
\[
 Q_{p,\mathrm{sym}}=2q S_{q,t}(p)c_+^2,
\]
where
\[
 S_{q,t}(p)=(q-1)\bigl[2^p+(2t+2)^p-2(t+2)^p\bigr]
 +q\bigl[1+(2t+1)^p-2(t+1)^p\bigr]-2t^p.
\]
For \(0<p<1\), concavity of \(x\mapsto x^p\) makes both bracketed midpoint differences nonpositive; hence \(S_{q,t}(p)\le-2t^p<0\).

The antisymmetric radial form is
\[
 Q_{p,\mathrm{anti}}=-2q\bigl[X_{q,t}(p)c_-^2
 +2Y_{q,t}(p)c_-h_-+Z_{q,t}(p)h_-^2\bigr]. \tag{2}
\]
For \(0<p<p_0(q)\) we have \(X>0\). Because \((2t+2)/(2t+1)<2\), the same interval has \(Z>0\). As \(p_0(q)<1\), all other sectors are strictly negative there. Consequently, in this whole interval, negative type is equivalent to \(\Delta_{q,t}(p)\ge0\), with strictness equivalent to \(\Delta_{q,t}(p)>0\).

**3. Existence, uniqueness and embedding rank.** As \(p\downarrow0\), \((X,Y,Z)\to(1,0,1)\), so \(\Delta\to1\). Let \(r=p_0(q)\in(0,1)\). Then \(X(r)=0\) and \(q-1=1/(2^r-1)\). Since the increment \((x+t)^r-x^r\) strictly decreases with \(x>0\),
\[
 (2t+2)^r-(t+2)^r<(2t)^r-t^r=(2^r-1)t^r.
\]
It follows that \(Y(r)=(q-1)[(2t+2)^r-(t+2)^r]-t^r<0\). Thus \(\Delta(r)=-Y(r)^2<0\), proving an intermediate root. The general strict-negative-type inheritance theorem (Li–Weston, Theorem 5.4) states that \(p\)-negative type implies strict \(s\)-negative type for every \(0\le s<p\). Together with the equivalence above, this excludes multiple roots and establishes strictness below, failure above, and endpoint non-strictness. As \(X,Z>0\) at the root, (2) has exactly one null direction. The other sectors are strictly negative; therefore the centered Gram matrix has rank \(4q-2\) at the endpoint and rank \(4q-1\) below it.

**4. Two-sided restoration.** For fixed \(0<p<p_0(q)\) and \(t\downarrow0\), write \(X=X_{q,t}(p)>0\) (independent of \(t\)). Then
\[
 Z=X+O(t),\qquad Y=X-t^p+O(t),\qquad
 \Delta=2Xt^p+o(t^p)>0
\]
because \(p<1\). For \(t\to\infty\),
\[
 Z=(2t)^p(1+O(t^{-1})),\qquad Y=O(t^{p-1}),
\]
so \(\Delta>0\) again for sufficiently large \(t\). Since the critical exponent always lies below \(p_0(q)\), the two limits equal \(p_0(q)\). Continuity of the unique root in \(t\) and strict inequality at finite \(t\) imply attainment of an interior minimum.

**5. Branching and singular limit.** For fixed \(t>0\) and bounded \(c>0\), put \(p=c/q\) in (2). Taylor expansion, uniform for \(c\) in compact sets, yields
\[
 \begin{pmatrix}X&Y\\Y&Z\end{pmatrix}
 =I_2-c\begin{pmatrix}A&B(t)\\B(t)&C(t)\end{pmatrix}+O(q^{-1}).
\]
The largest eigenvalue of the positive-entry symmetric matrix on the right is
\[
 \lambda_+(t)=\tfrac12\left(A+C(t)+\sqrt{(A-C(t))^2+4B(t)^2}\right)>A.
\]
Its smaller eigenvalue is below \(A\). Hence the first loss of positive semidefiniteness as \(c\) increases occurs at \(c=1/\lambda_+(t)<1/A\). The unique-root characterization and uniform Taylor expansion imply \(q\wp_q(t)\to1/\lambda_+(t)=L(t)\).

Finally, as \(t\downarrow0\), \(B(t),C(t)\to A\), giving \(L(t)\to1/(2A)\), whereas for fixed \(q\), \(\wp_q(t)\to p_0(q)\) and \(qp_0(q)\to1/A\). This proves the stated noncommutation. As \(t\to\infty\), \(B(t),C(t)\to0\) and \(L(t)\to1/A\).

## Verification

Run \(`python verify_biclique_corona.py`\) with Python, NumPy and mpmath. The standalone checker compares the quadratic decomposition against exact rational powered-distance forms, tests centered full matrices on both sides of the critical root, confirms endpoint corank numerically, and compares large-branching estimates with the analytic limit. Exact identities and finite numerical diagnostics support, but do not replace, the universal proof. Example outputs include `EXACT_POWER_DISTANCE_QUADRATIC_DECOMPOSITION_OK 180`, `FULL_POWERED_DISTANCE_INERTIA_AND_ENDPOINT_RANK_OK 32`, and `NONCOMMUTING_SMALL_LENGTH_LARGE_BRANCH_LIMITS_OK`.

## Relationship to prior work

Sánchez, *On the supremal \(p\)-negative type of a finite metric space* (arXiv:1108.0451, 2011), computes the core \(K_{q,q}\) threshold \(p_0(q)\). Li and Weston, *Strict \(p\)-negative type of a metric space* (arXiv:0901.0695, 2009), establish the inheritance theorem used in the uniqueness argument. Ferdi and collaborators, *Quadratic Embedding Constants of Corona Graphs* (arXiv:2512.17258, 2025), study the ordinary \(p=1\) distance quadratic form for unweighted coronas; they do not evaluate a continuously varying negative-type exponent under weighted pendant lengths. The new statement concerns the two-sided pendant-length restoration and explicit singular large-branching law for a balanced bipartite core, not general corona spectral theory or an unweighted core's known exponent. Prior independently obtained descriptions of a different core family (clique coronas) and of cyclic sunlet stiffness also do not imply this bipartite exponent formula.

## Limitations

The result is restricted to balanced complete bipartite cores, one identical private leaf at every core vertex, unit core lengths, and positive equal pendant lengths. It neither gives the unique minimizing leaf length nor classifies unbalanced or heterogeneous cases. The embeddings concern \(d^{p/2}\), not undistorted embeddings of the original metric at exponents where negative type fails. Mathematical novelty remains subject to discovery of unindexed equivalent literature, and no external audit is claimed.

## References

1. H. Li and A. Weston, *Strict \(p\)-negative type of a metric space*, arXiv:0901.0695 (first posted January 6, 2009), Theorem 5.4. https://arxiv.org/abs/0901.0695
2. S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451 (first posted August 2, 2011), Theorem 3.1. https://arxiv.org/abs/1108.0451
3. Ferdi, E. T. Baskoro, N. Obata, and A. P. Santika, *Quadratic Embedding Constants of Corona Graphs*, arXiv:2512.17258 (first posted December 19, 2025). https://arxiv.org/abs/2512.17258
