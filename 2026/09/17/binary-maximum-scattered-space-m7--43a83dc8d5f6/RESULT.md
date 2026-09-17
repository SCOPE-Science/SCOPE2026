# A binary maximum scattered 10-space in \(\mathbb F_{128}^3\)

## Result

Let
\[
F=\mathbb F_2[a]/(a^7+a+1).
\]
For \(c\in\{0,\ldots,127\}\), write \([c]\) for the field element whose binary expansion
\(c=\sum_{i=0}^6 c_i2^i\) represents \(\sum_{i=0}^6 c_i a^i\).

Let \(U\le F^3\) be the \(\mathbb F_2\)-span of the following ten vectors:
\[
\begin{array}{rcl}
(126,2,64),&&(38,5,32),\\
(36,12,16),&&(111,14,8),\\
(9,8,4),&&(46,3,2),\\
(12,8,1),&&(22,71,0),\\
(7,36,0),&&(32,18,0).
\end{array}
\]
Here every coordinate is interpreted using the encoding above.

**Theorem.** \(U\) has \(\mathbb F_2\)-dimension \(10\) and is scattered with respect to the
Desarguesian \(7\)-spread of \(F^3\); equivalently, for every one-dimensional
\(F\)-subspace \(L\le F^3\),
\[
\dim_{\mathbb F_2}(U\cap L)\le 1.
\]
Since the general scattered-subspace bound is
\(\dim_{\mathbb F_2}U\le \lfloor 3\cdot7/2\rfloor=10\), this \(U\) is maximum scattered.

As a coding-theoretic consequence, Corollary 3.5 of Borello--Polverino--Zullo
(arXiv:2604.02004) gives a nondegenerate rank-metric intersecting code with parameters
\[
[11,3,6]_{2^7/2}.
\]
Thus the extremal length \(2m-3\) is attained for the previously unresolved odd parameter
pair \((q,m)=(2,7)\).

## Exact verification

The polynomial \(x^7+x+1\) is primitive over \(\mathbb F_2\): the verification artifact
checks that the residue class \(a\) has multiplicative order \(127\). The ten displayed
vectors have binary rank \(10\).

For each \(\lambda\in F\setminus\mathbb F_2\), the artifact then computes
\[
\operatorname{rank}_{\mathbb F_2}\bigl(U+\lambda U\bigr)=20.
\]
Hence \(U\cap\lambda U=\{0\}\) for all such \(\lambda\). If an \(F\)-line contained two
\(\mathbb F_2\)-independent vectors \(u,v\in U\), then \(v=\lambda u\) for some
\(\lambda\in F\setminus\mathbb F_2\), contradicting \(U\cap\lambda U=\{0\}\).
This proves scatteredness.

As an independent finite check, all \(2^{10}-1=1023\) nonzero vectors of \(U\) are
enumerated and normalized as points of \(PG(2,128)\); all 1023 normalized points are
distinct.

## Context and originality boundary

Borello, Polverino and Zullo proved in 2026 that a nondegenerate extremal
\([2m-3,3,d]_{q^m/q}\) rank-metric intersecting code exists exactly when the relevant
dual \(q\)-system is a scattered \(\mathbb F_q\)-subspace of
\(\mathbb F_{q^m}^3\) of dimension \(m+3\), in which case \(d=m-1\). They obtain
existence for every even \(m\ge6\), and explicitly state that the odd-\(m\) case remains
largely open; any construction of a scattered subspace of dimension at least \(m+3\)
produces a new extremal code.

Earlier work gives several large scattered families, including constructions of rank
\(m+2\) in dimension three for infinite families with odd \(m\), but those results do not
supply the rank \(m+3=10\) binary case above. General results also emphasize that when
the ambient product \(mn\) is odd, existence of maximum scattered subspaces is not known
in general.

The originality claim is therefore limited to the explicit parameter instance
\((q,m)=(2,7)\), its exact certificate, and the resulting
\([11,3,6]_{2^7/2}\) extremal rank-metric intersecting code, to the best of our
knowledge. No claim is made that this settles odd \(m\) in general, other even
characteristics, or classification/equivalence of the constructed maximum scattered
space.

## Reproducibility

Run
`python3 artifacts/verify_scattered_m7_q2.py`.
It uses only the Python standard library and exhaustively verifies both equivalent
scatteredness certificates described above.

## References

1. M. Borello, O. Polverino, F. Zullo, *On the existence of linear rank-metric intersecting codes*, arXiv:2604.02004 (2026). https://arxiv.org/abs/2604.02004
2. A. Gruica, A. Ravagnani, J. Sheekey, F. Zullo, *Generalised evasive subspaces*, Journal of Combinatorial Designs 32 (2024), 642--678. https://arxiv.org/abs/2207.01027
3. S. Lia, G. Longobardi, G. Marino, R. Trombetti, *Short rank-metric codes and scattered subspaces*, SIAM Journal on Discrete Mathematics 38 (2024). https://arxiv.org/abs/2306.01315
4. D. Bartoli, A. Giannoni, G. Marino, *New scattered subspaces in higher dimensions*, Annali di Matematica Pura ed Applicata (2024/2025). https://arxiv.org/abs/2402.15223
