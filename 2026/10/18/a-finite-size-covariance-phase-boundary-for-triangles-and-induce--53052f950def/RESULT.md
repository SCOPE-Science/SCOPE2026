# A finite-size covariance phase boundary for triangles and induced holes in random graphs

## Finding
For \(G\sim G(n,p)\), let \(T\) count copies of \(K_3\), and let \(H_\ell\) count **induced** chordless cycles \(C_\ell\), each once as an unlabeled subgraph, for integer \(n\ge\ell\ge4\) and \(0<p<1\). Set
\[
c_\ell=\frac{(\ell-1)!}{2},\qquad q_\ell=\binom\ell2-\ell=\frac{\ell(\ell-3)}2.
\]
The exact covariance is
\[
\boxed{\operatorname{Cov}(T,H_\ell)=\binom n3c_\ell p^{\ell+2}(1-p)^{q_\ell}\left[3\binom{n-3}{\ell-2}\left(\frac2{\ell-1}-p\right)-\binom{n-3}{\ell-3}p\right].}
\]
The binomial coefficient is zero when its lower index exceeds its upper index. For \(n=\ell\), the covariance is strictly negative for every \(0<p<1\). If \(n>\ell\), it is positive precisely below the single zero
\[
\boxed{p_{n,\ell}=\frac{6(n-\ell)}{(\ell-1)(3n-2\ell-2)}},
\]
and negative precisely above that zero. Equality holds exactly at this parameter. All thresholds satisfy \(0<p_{n,\ell}<2/(\ell-1)<1\). For each fixed \(\ell\) the threshold increases strictly in \(n\); for each fixed \(n\) it decreases strictly in \(\ell\) over \(4\le\ell<n\), and \(p_{n,n}=0\).

The exact finite-size displacement from the limiting density is
\[
\frac2{\ell-1}-p_{n,\ell}=\frac{2(\ell-2)}{(\ell-1)(3n-2\ell-2)}.
\]
In particular for fixed \(\ell\) the covariance, normalized by \(n^{\ell+1}\), converges to
\[
\frac{\ell-1}{4}p^{\ell+2}(1-p)^{q_\ell}\left(\frac2{\ell-1}-p\right).
\]
At the limiting critical density \(p=2/(\ell-1)\), the finite-size covariance is strictly negative, rather than zero, for every \(n\ge\ell\).

## Assumptions and scope
The probability space is the simple labeled graph on \([n]\), with distinct edges included independently with probability \(p\). A triangle is an unordered three-vertex set whose three edges are present; edges to vertices outside the triple are not constrained. An induced hole is an \(\ell\)-element vertex set with its \(\binom\ell2\) internal edge indicators matching a simple cycle: exactly \(\ell\) required edges and \(q_\ell\) forbidden chords. Every geometric cycle edge set on a fixed \(\ell\)-vertex subset is counted once, giving \(c_\ell\) possible cycles. We require \(\ell\ge4\): an induced cycle of length three is a triangle and has different covariance behavior. We exclude endpoints \(p=0,1\) because both counts degenerate there. No scaling restriction on \(n,p,\ell\) is imposed for the exact identity; the displayed normalized limit keeps \(\ell,p\) fixed.

## Proof
Write \(T=\sum_A I_A\), summed over unordered triples \(A\), and \(H_\ell=\sum_B\sum_\gamma J_{B,\gamma}\), where \(B\) ranges over \(\ell\)-subsets and \(\gamma\) ranges over the \(c_\ell\) undirected Hamilton cycles on \(B\). The expectations of the indicator variables are
\[
\mathbb E I_A=p^3,\quad \mathbb E J_{B,\gamma}=p^\ell(1-p)^{q_\ell}.
\]
For fixed \((A,B,\gamma)\), suppose \(s=|A\cap B|\). If \(s\le1\), the two events depend on disjoint sets of edge indicators, so their covariance is zero. If \(s=2\), the unique edge inside the intersection is required by the triangle. If it is a cycle edge of \(\gamma\), then exactly one of the triangle's three required edges was already required by the hole, so
\[
\mathbb E(I_AJ_{B,\gamma})=p^{\ell+2}(1-p)^{q_\ell};
\]
otherwise that edge is a forbidden chord and the joint probability is zero. For uniformly ranging \(\gamma\), the number of cycles containing a specified edge on \(B\) is \(2c_\ell/(\ell-1)\): each of the \(c_\ell\) cycles has \(\ell\) edges among \(\binom\ell2\) possible edges. Averaging over \(\gamma\), the pair-indicator covariance for intersection size two is therefore
\[
p^{\ell+2}(1-p)^{q_\ell}\left(\frac2{\ell-1}-p\right).
\]
If \(s=3\), the three triangle vertices lie inside an induced \(C_\ell\), which is triangle-free for \(\ell\ge4\); consequently \(I_AJ_{B,\gamma}=0\) and the covariance is \(-p^{\ell+3}(1-p)^{q_\ell}\). These are all possibilities.

For each fixed triangle set \(A\), there are exactly \(3\binom{n-3}{\ell-2}\) choices of \(B\) with \(|A\cap B|=2\), and \(\binom{n-3}{\ell-3}\) with \(|A\cap B|=3\). Multiplying their respective covariance contributions by \(c_\ell\), summing over the \(\binom n3\) triples, and factoring yields the boxed exact formula.

When \(n=\ell\), the two-vertex overlap count vanishes, whereas the triple-overlap term remains strictly negative. For \(n>\ell\), all prefactors outside the final square bracket are positive and the bracket is a strictly decreasing affine function of \(p\), with positive intercept. Its unique root is obtained from
\[
\frac{\binom{n-3}{\ell-3}}{\binom{n-3}{\ell-2}}=\frac{\ell-2}{n-\ell},
\]
which gives the stated \(p_{n,\ell}\). It is strictly between zero and \(2/(\ell-1)\), which is itself below one for \(\ell\ge4\).

Writing \(h=n-\ell\), the threshold is \(6h/((\ell-1)(3h+\ell-2))\), manifestly increasing in \(h\) for fixed \(\ell\). For fixed \(n\), replace \(\ell\) by \(n-h\), giving \(6h/((n-h-1)(n+2h-2))\). Each positive factor's logarithmic derivative with respect to \(h\) has sum
\[
\frac1h+\frac1{n-h-1}-\frac2{n+2h-2}>0,
\]
since the first term exceeds the magnitude of the last for \(n\ge4\). Therefore the threshold decreases with \(\ell\). Simple subtraction proves the displacement formula. Finally, dividing the exact expression by \(n^{\ell+1}\) and using the leading terms of both binomial coefficients gives the displayed limit. These arguments also handle all admissible boundary cases.

## Verification
Run \(`python3 verify.py`\) with Python 3 and only the standard library. The verifier exhaustively enumerates all labeled graphs through six vertices for selected hole lengths and rational edge probabilities, independently computes \(\operatorname{Cov}(T,H_\ell)\), checks motif compatibility on intersecting vertex sets, and tests exact rational sign thresholds and monotonicity across a finite grid. The current packaged verifier reports \(`PASS: 6063 exact checks`\). The unrestricted proof is the overlap analysis above; enumerations are not offered as an infinite certificate.

## Relationship to prior work
Classical overlap methods underlie the variance analysis of ordinary subgraph counts in Ellis and Ferry [1], whose graph-overlay polynomial concerns variance of one non-induced motif. The present result instead treats a **mixed** covariance of a triangle and an **induced** chordless hole: disjoint and one-vertex overlaps cancel, but shared pairs may require or forbid the same edge, and shared triples are mutually impossible. Their competition yields an explicit finite-size sign transition.

Sah and Sawhney [2] analyze local limit theorems for induced subgraph counts and exceptional edge densities. Their single-motif distributional theorems do not state the exact mixed triangle–hole covariance or the finite-size root. Janson [3] studies joint/asymptotic subgraph-count theory, including induced-count phenomena; the abstract of this older contribution does not determine whether its full text might contain a related calculation. The limiting density \(2/(\ell-1)\) here has a simple meaning: it equals the ratio of the number of edges of an induced hole to the number of possible vertex pairs. The theorem quantifies the finite-size, downward-shifted covariance-zero density rather than assuming the limiting density is an exact zero.

## Limitations
This is a self-reviewed analytic result, not independently audited or externally certified. General induced-subgraph count expansions may provide alternative derivations, and historically earlier formulations may exist; no claim of definitive priority is made. The theorem concerns the covariance sign, not positive/negative association of the full joint law or arbitrary nonlinear transforms of either statistic. The exact identity holds for independent edges only, not for the fixed-edge-count model \(G(n,m)\). The asymptotic statement holds for fixed \(\ell\) and fixed \(p\), not for growing hole length or an arbitrary varying edge probability.

## References
[1] R. B. Ellis and J. P. Ferry, “Variance of the subgraph count for sparse Erdős–Rényi graphs,” *Discrete Applied Mathematics* 158 (2010), 649–658, doi:10.1016/j.dam.2009.11.012. Publicly indexed publication date: 2010-03-28.

[2] A. Sah and M. Sawhney, “Local limit theorems for subgraph counts,” arXiv:2006.11369, first posted 2020-06-19, especially Theorem 1.2 and §4.2.

[3] S. Janson, “A functional limit theorem for random graphs with applications to subgraph count statistics,” *Random Structures & Algorithms* 1 (1990), 15–37, doi:10.1002/rsa.3240010103 (abstract and metadata available; full text not verified).
